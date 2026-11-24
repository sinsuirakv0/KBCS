# v16.0.1 → v16.0.2 · 最優先の変更候補 (81)

[一覧の目次](README.md)

<a id="compare-0eea9f77795dd26a2c9575ecadee2044"></a>

### [`00bc5a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5a00.md) → [`00bc5a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5a9c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal8ActivateEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d840.md) · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc5120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5120.md) [`00bc9dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9dc8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c5d910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d910.md) · 呼出先 15件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bc51bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc51bc.md) [`00bc9e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9e64.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00bc5ae0",
      "incomplete_value": true,
      "site": "00bc5af4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5b1c",
      "incomplete_value": true,
      "site": "00bc5b24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5b48",
      "incomplete_value": false,
      "site": "00bc5b5c",
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
            "const:e54:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bc5ae0",
      "READ",
      [
        "storage",
        "00c9b990",
        null,
        "pointer"
      ]
    ],
    [
      "00bc5ae0",
      "PARAM",
      [
        "storage",
        "00bc9dc8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00bc5b1c",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc5ae0",
      "READ",
      [
        "storage",
        "00c9ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00bc5ae0",
      "PARAM",
      [
        "storage",
        "00bc9e64",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00bc5b1c",
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

- 旧版 [`00bc5a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5a00.md#insn-00bc5a58) · [`00bc5a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5a00.md#insn-00bc5a88) · [`00bc5ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5a00.md#insn-00bc5ac0)
- 新版 [`00bc5af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5a9c.md#insn-00bc5af4) · [`00bc5b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5a9c.md#insn-00bc5b24) · [`00bc5b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5a9c.md#insn-00bc5b5c)

~~~diff
- 00bc5a58 ["INT_ADD", "register:40f0:8", ["const:bc5a58:8", "const:4:8"]]
- 00bc5a58 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc5af4 ["INT_ADD", "register:40f0:8", ["const:bc5af4:8", "const:4:8"]]
+ 00bc5af4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc5a58 bytes fa540294
+ 00bc5af4 bytes 07550294
- 00bc5a88 ["INT_ADD", "register:40f0:8", ["const:bc5a88:8", "const:4:8"]]
- 00bc5a88 ["CALL", null, ["callee:00497874:8"]]
+ 00bc5b24 ["INT_ADD", "register:40f0:8", ["const:bc5b24:8", "const:4:8"]]
+ 00bc5b24 ["CALL", null, ["callee:00497874:8"]]
- 00bc5a88 bytes 6b47e397
+ 00bc5b24 bytes 5447e397
- 00bc5ac0 ["INT_ADD", "register:40f0:8", ["const:bc5ac0:8", "const:4:8"]]
- 00bc5ac0 ["CALL", null, ["callee:00c5d9d0:8"]]
+ 00bc5b5c ["INT_ADD", "register:40f0:8", ["const:bc5b5c:8", "const:4:8"]]
+ 00bc5b5c ["CALL", null, ["callee:00c5d9d0:8"]]
- 00bc5ac0 bytes 905f0294
+ 00bc5b5c bytes 9d5f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8712f757625c5462429a309377a23f7a"></a>

### [`00bc5d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5d2c.md) → [`00bc5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5dc8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal16FetchAndActivateEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d720.md) · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc5120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5120.md) [`00bc9dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9dc8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c5d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d7f0.md) · 呼出先 15件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bc51bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc51bc.md) [`00bc9e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9e64.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00bc5e0c",
      "incomplete_value": true,
      "site": "00bc5e20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5e48",
      "incomplete_value": true,
      "site": "00bc5e50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5e74",
      "incomplete_value": false,
      "site": "00bc5e88",
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
            "const:7c2:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bc5e0c",
      "READ",
      [
        "storage",
        "00c9b990",
        null,
        "pointer"
      ]
    ],
    [
      "00bc5e0c",
      "PARAM",
      [
        "storage",
        "00bc9dc8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00bc5e48",
      "READ",
      [
        "storage",
        "011264a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc5e0c",
      "READ",
      [
        "storage",
        "00c9ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00bc5e0c",
      "PARAM",
      [
        "storage",
        "00bc9e64",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00bc5e48",
      "READ",
      [
        "storage",
        "011265a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5d2c.md#insn-00bc5d84) · [`00bc5db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5d2c.md#insn-00bc5db4) · [`00bc5dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5d2c.md#insn-00bc5dec)
- 新版 [`00bc5e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5dc8.md#insn-00bc5e20) · [`00bc5e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5dc8.md#insn-00bc5e50) · [`00bc5e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5dc8.md#insn-00bc5e88)

~~~diff
- 00bc5d84 ["INT_ADD", "register:40f0:8", ["const:bc5d84:8", "const:4:8"]]
- 00bc5d84 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc5e20 ["INT_ADD", "register:40f0:8", ["const:bc5e20:8", "const:4:8"]]
+ 00bc5e20 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc5d84 bytes 2f540294
+ 00bc5e20 bytes 3c540294
- 00bc5db4 ["INT_ADD", "register:40f0:8", ["const:bc5db4:8", "const:4:8"]]
- 00bc5db4 ["CALL", null, ["callee:00497874:8"]]
+ 00bc5e50 ["INT_ADD", "register:40f0:8", ["const:bc5e50:8", "const:4:8"]]
+ 00bc5e50 ["CALL", null, ["callee:00497874:8"]]
- 00bc5db4 bytes a046e397
+ 00bc5e50 bytes 8946e397
- 00bc5dec ["INT_ADD", "register:40f0:8", ["const:bc5dec:8", "const:4:8"]]
- 00bc5dec ["CALL", null, ["callee:00c5d9d0:8"]]
+ 00bc5e88 ["INT_ADD", "register:40f0:8", ["const:bc5e88:8", "const:4:8"]]
+ 00bc5e88 ["CALL", null, ["callee:00c5d9d0:8"]]
- 00bc5dec bytes c55e0294
+ 00bc5e88 bytes d25e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ce4a2aeb48b38f589607cfd06853ec6"></a>

### [`00bc6058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6058.md) → [`00bc60f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc60f4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal5FetchEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7e0.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc5358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5358.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5d8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d8b0.md) · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bc53f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc53f4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00bc616c",
      "incomplete_value": true,
      "site": "00bc6178",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
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
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc619c",
      "incomplete_value": false,
      "site": "00bc61b0",
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
            "const:363:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 7,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc626c",
      "incomplete_value": true,
      "site": "00bc627c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bc616c",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc619c",
      "PARAM",
      [
        "storage",
        "002a73bf",
        null,
        "string"
      ]
    ],
    [
      "00bc626c",
      "READ",
      [
        "storage",
        "00c9b958",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bc616c",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc619c",
      "PARAM",
      [
        "storage",
        "002a7363",
        null,
        "string"
      ]
    ],
    [
      "00bc626c",
      "READ",
      [
        "storage",
        "00c9ba28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc60dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6058.md#insn-00bc60dc) · [`00bc6114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6058.md#insn-00bc6114) · [`00bc61b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6058.md#insn-00bc61b0)
- 新版 [`00bc6178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc60f4.md#insn-00bc6178) · [`00bc61b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc60f4.md#insn-00bc61b0) · [`00bc624c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc60f4.md#insn-00bc624c)

~~~diff
- 00bc60dc ["INT_ADD", "register:40f0:8", ["const:bc60dc:8", "const:4:8"]]
- 00bc60dc ["CALL", null, ["callee:00497874:8"]]
+ 00bc6178 ["INT_ADD", "register:40f0:8", ["const:bc6178:8", "const:4:8"]]
+ 00bc6178 ["CALL", null, ["callee:00497874:8"]]
- 00bc60dc bytes d645e397
+ 00bc6178 bytes bf45e397
- 00bc6114 ["INT_ADD", "register:40f0:8", ["const:bc6114:8", "const:4:8"]]
- 00bc6114 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bc61b0 ["INT_ADD", "register:40f0:8", ["const:bc61b0:8", "const:4:8"]]
+ 00bc61b0 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bc6114 bytes 23530294
+ 00bc61b0 bytes 30530294
- 00bc61b0 ["INT_ADD", "register:40f0:8", ["const:bc61b0:8", "const:4:8"]]
- 00bc61b0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bc624c ["INT_ADD", "register:40f0:8", ["const:bc624c:8", "const:4:8"]]
+ 00bc624c ["CALL", null, ["callee:00c57f80:8"]]
- 00bc61b0 bytes 40470294
+ 00bc624c bytes 4d470294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be83b9e087e0c94f9177b9272e559df0"></a>

### [`00bc6380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6380.md) → [`00bc641c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc641c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6f0.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc53d8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5d7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d7c0.md) · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bc5474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5474.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00bc6494",
      "incomplete_value": true,
      "site": "00bc64a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
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
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc64c4",
      "incomplete_value": false,
      "site": "00bc64d8",
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
            "const:bfb:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 7,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc6594",
      "incomplete_value": true,
      "site": "00bc65a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bc6494",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc64c4",
      "PARAM",
      [
        "storage",
        "002c0bbb",
        null,
        "string"
      ]
    ],
    [
      "00bc6594",
      "READ",
      [
        "storage",
        "00c9b968",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bc6494",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc64c4",
      "PARAM",
      [
        "storage",
        "002c0bfb",
        null,
        "string"
      ]
    ],
    [
      "00bc6594",
      "READ",
      [
        "storage",
        "00c9ba38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6380.md#insn-00bc6404) · [`00bc643c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6380.md#insn-00bc643c) · [`00bc64d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6380.md#insn-00bc64d8)
- 新版 [`00bc64a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc641c.md#insn-00bc64a0) · [`00bc64d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc641c.md#insn-00bc64d8) · [`00bc6574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc641c.md#insn-00bc6574)

~~~diff
- 00bc6404 ["INT_ADD", "register:40f0:8", ["const:bc6404:8", "const:4:8"]]
- 00bc6404 ["CALL", null, ["callee:00497874:8"]]
+ 00bc64a0 ["INT_ADD", "register:40f0:8", ["const:bc64a0:8", "const:4:8"]]
+ 00bc64a0 ["CALL", null, ["callee:00497874:8"]]
- 00bc6404 bytes 0c45e397
+ 00bc64a0 bytes f544e397
- 00bc643c ["INT_ADD", "register:40f0:8", ["const:bc643c:8", "const:4:8"]]
- 00bc643c ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bc64d8 ["INT_ADD", "register:40f0:8", ["const:bc64d8:8", "const:4:8"]]
+ 00bc64d8 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bc643c bytes 59520294
+ 00bc64d8 bytes 66520294
- 00bc64d8 ["INT_ADD", "register:40f0:8", ["const:bc64d8:8", "const:4:8"]]
- 00bc64d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bc6574 ["INT_ADD", "register:40f0:8", ["const:bc6574:8", "const:4:8"]]
+ 00bc6574 ["CALL", null, ["callee:00c57f80:8"]]
- 00bc64d8 bytes 76460294
+ 00bc6574 bytes 83460294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f038419fe6c27eaf49501b2808ab6ad5"></a>

### [`00bc6618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6618.md) → [`00bc66b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc66b4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_21ConfigKeyValueVariantEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5d6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6e0.md) · 呼出先 33件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bc53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc53d8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c5d7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d7b0.md) · 呼出先 33件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00bc5474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5474.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00bc6988",
      "incomplete_value": false,
      "site": "00bc698c",
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
            "const:7ba:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc6a94",
      "incomplete_value": true,
      "site": "00bc6aa0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 41,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc6ac8",
      "incomplete_value": false,
      "site": "00bc6adc",
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
            "const:bfb:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bc67ac",
      "DATA",
      [
        "storage",
        "0030e99a",
        "switchD_00bc6718::switchdataD_0030e99a",
        "byte"
      ]
    ],
    [
      "00bc6988",
      "PARAM",
      [
        "storage",
        "002a8816",
        null,
        "string"
      ]
    ],
    [
      "00bc6a94",
      "READ",
      [
        "storage",
        "011264b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc67ac",
      "DATA",
      [
        "storage",
        "0030e9da",
        "switchD_00bc67b4::switchdataD_0030e9da",
        "byte"
      ]
    ],
    [
      "00bc6988",
      "PARAM",
      [
        "storage",
        "002a87ba",
        null,
        "string"
      ]
    ],
    [
      "00bc6a94",
      "READ",
      [
        "storage",
        "011265b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc68f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6618.md#insn-00bc68f0) · [`00bc6a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6618.md#insn-00bc6a04) · [`00bc6a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6618.md#insn-00bc6a40)
- 新版 [`00bc698c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc66b4.md#insn-00bc698c) · [`00bc6aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc66b4.md#insn-00bc6aa0) · [`00bc6adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc66b4.md#insn-00bc6adc)

~~~diff
- 00bc68f0 ["INT_ADD", "register:40f0:8", ["const:bc68f0:8", "const:4:8"]]
- 00bc68f0 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bc698c ["INT_ADD", "register:40f0:8", ["const:bc698c:8", "const:4:8"]]
+ 00bc698c ["CALL", null, ["callee:00c5ad70:8"]]
- 00bc68f0 bytes ec500294
+ 00bc698c bytes f9500294
- 00bc6a04 ["INT_ADD", "register:40f0:8", ["const:bc6a04:8", "const:4:8"]]
- 00bc6a04 ["CALL", null, ["callee:00497874:8"]]
+ 00bc6aa0 ["INT_ADD", "register:40f0:8", ["const:bc6aa0:8", "const:4:8"]]
+ 00bc6aa0 ["CALL", null, ["callee:00497874:8"]]
- 00bc6a04 bytes 8c43e397
+ 00bc6aa0 bytes 7543e397
- 00bc6a40 ["INT_ADD", "register:40f0:8", ["const:bc6a40:8", "const:4:8"]]
- 00bc6a40 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bc6adc ["INT_ADD", "register:40f0:8", ["const:bc6adc:8", "const:4:8"]]
+ 00bc6adc ["CALL", null, ["callee:00c5ae70:8"]]
- 00bc6a40 bytes d8500294
+ 00bc6adc bytes e5500294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e6d6d6a7b9d7427025a9b7148746a34"></a>

### [`00bc6d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6d2c.md) → [`00bc6dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6dc8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_14ConfigKeyValueEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6d0.md) · 呼出先 21件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bc53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc53d8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c5d7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d7a0.md) · 呼出先 21件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00bc5474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5474.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00bc6fbc",
      "incomplete_value": true,
      "site": "00bc6fc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 19,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc6ff0",
      "incomplete_value": false,
      "site": "00bc7004",
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
            "const:bfb:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 22,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc70c4",
      "incomplete_value": true,
      "site": "00bc70d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bc6fbc",
      "READ",
      [
        "storage",
        "011264b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6ff0",
      "PARAM",
      [
        "storage",
        "002c0bbb",
        null,
        "string"
      ]
    ],
    [
      "00bc70c4",
      "READ",
      [
        "storage",
        "00c9b968",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bc6fbc",
      "READ",
      [
        "storage",
        "011265b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6ff0",
      "PARAM",
      [
        "storage",
        "002c0bfb",
        null,
        "string"
      ]
    ],
    [
      "00bc70c4",
      "READ",
      [
        "storage",
        "00c9ba38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6d2c.md#insn-00bc6f2c) · [`00bc6f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6d2c.md#insn-00bc6f68) · [`00bc7038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6d2c.md#insn-00bc7038)
- 新版 [`00bc6fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6dc8.md#insn-00bc6fc8) · [`00bc7004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6dc8.md#insn-00bc7004) · [`00bc70d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6dc8.md#insn-00bc70d4)

~~~diff
- 00bc6f2c ["INT_ADD", "register:40f0:8", ["const:bc6f2c:8", "const:4:8"]]
- 00bc6f2c ["CALL", null, ["callee:00497874:8"]]
+ 00bc6fc8 ["INT_ADD", "register:40f0:8", ["const:bc6fc8:8", "const:4:8"]]
+ 00bc6fc8 ["CALL", null, ["callee:00497874:8"]]
- 00bc6f2c bytes 4242e397
+ 00bc6fc8 bytes 2b42e397
- 00bc6f68 ["INT_ADD", "register:40f0:8", ["const:bc6f68:8", "const:4:8"]]
- 00bc6f68 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bc7004 ["INT_ADD", "register:40f0:8", ["const:bc7004:8", "const:4:8"]]
+ 00bc7004 ["CALL", null, ["callee:00c5ae70:8"]]
- 00bc6f68 bytes 8e4f0294
+ 00bc7004 bytes 9b4f0294
- 00bc7038 ["INT_ADD", "register:40f0:8", ["const:bc7038:8", "const:4:8"]]
- 00bc7038 ["CALL", null, ["callee:00c5b010:8"]]
+ 00bc70d4 ["INT_ADD", "register:40f0:8", ["const:bc70d4:8", "const:4:8"]]
+ 00bc70d4 ["CALL", null, ["callee:00c5b010:8"]]
- 00bc7038 bytes c24f0294
+ 00bc70d4 bytes cf4f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36e01bdcd7c761d9279666cef63c870c"></a>

### [`00bc72e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc72e8.md) → [`00bc7384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7384.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17SetConfigSettingsENS0_14ConfigSettingsE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d760.md) · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bc5250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c5d830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d830.md) · 呼出先 15件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00bc52ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc52ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00bc7400",
      "incomplete_value": true,
      "site": "00bc740c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7404",
      "incomplete_value": true,
      "site": "00bc740c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7420",
      "incomplete_value": true,
      "site": "00bc7440",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bc7400",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7404",
      "READ",
      [
        "storage",
        "011265d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7420",
      "READ",
      [
        "storage",
        "011265e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc7400",
      "READ",
      [
        "storage",
        "011266c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7404",
      "READ",
      [
        "storage",
        "011266d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7420",
      "READ",
      [
        "storage",
        "011266e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc7370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc72e8.md#insn-00bc7370) · [`00bc7384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc72e8.md#insn-00bc7384) · [`00bc73a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc72e8.md#insn-00bc73a4)
- 新版 [`00bc740c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7384.md#insn-00bc740c) · [`00bc7420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7384.md#insn-00bc7420) · [`00bc7440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7384.md#insn-00bc7440)

~~~diff
- 00bc7370 ["INT_ADD", "register:40f0:8", ["const:bc7370:8", "const:4:8"]]
- 00bc7370 ["CALL", null, ["callee:00589734:8"]]
+ 00bc740c ["INT_ADD", "register:40f0:8", ["const:bc740c:8", "const:4:8"]]
+ 00bc740c ["CALL", null, ["callee:00589734:8"]]
- 00bc7370 bytes e108e797
+ 00bc740c bytes ca08e797
- 00bc7384 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5e0:8"]]
- 00bc7384 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc7420 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6e0:8"]]
+ 00bc7420 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc7384 bytes 02f142f9
+ 00bc7420 bytes 027143f9
- 00bc73a4 ["INT_ADD", "register:40f0:8", ["const:bc73a4:8", "const:4:8"]]
- 00bc73a4 ["CALL", null, ["callee:00497874:8"]]
+ 00bc7440 ["INT_ADD", "register:40f0:8", ["const:bc7440:8", "const:4:8"]]
+ 00bc7440 ["CALL", null, ["callee:00497874:8"]]
- 00bc73a4 bytes 2441e397
+ 00bc7440 bytes 0d41e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53aa40d9fe0cbfb9f4ca14aba8d67a5d"></a>

### [`00bc773c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc773c.md) → [`00bc77d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc77d8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal16SetCustomSignalsERKNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d730.md) · 呼出先 18件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bc5250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5250.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c5d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d800.md) · 呼出先 18件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00bc52ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc52ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 79.05% / 新版 79.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7740"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7740"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7744"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc7740",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc7744",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc7748",
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
      "00bc77dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bc77e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bc77e4",
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

- 旧版 [`00bc7740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc773c.md#insn-00bc7740) · [`00bc7744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc773c.md#insn-00bc7744) · [`00bc7748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc773c.md#insn-00bc7748)

~~~diff
- 00bc7740 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bc7740 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bc7740 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00bc7740 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc7740 bytes fc6f07a9
- 00bc7744 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bc7744 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bc7744 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00bc7744 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc7744 bytes fa6708a9
- 00bc7748 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bc7748 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bc7748 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00bc7748 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc7748 bytes f85f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b0c1c14bb7c1b7c344db5c4c2197d39"></a>

### [`00bc7e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7e84.md) → [`00bc7f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7f20.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17GetConfigSettingsEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d750.md) · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 1件 [`00c5d820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d820.md) · 呼出先 4件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`0058f5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f5dc.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7f48",
      "incomplete_value": true,
      "site": "00bc7f50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:600:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc7eac",
      "incomplete_value": true,
      "site": "00bc7eb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
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
      "definition_site": "00bc7f64",
      "incomplete_value": true,
      "site": "00bc7f70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:688:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc7ec8",
      "incomplete_value": true,
      "site": "00bc7ed4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:588:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7f88",
      "incomplete_value": true,
      "site": "00bc7f94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc7eec",
      "incomplete_value": true,
      "site": "00bc7ef8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bc7f48",
      "READ",
      [
        "storage",
        "01126500",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7f64",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7f88",
      "READ",
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
      "00bc7f48",
      "READ",
      [
        "storage",
        "01126600",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7f64",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7f88",
      "READ",
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

- 旧版 [`00bc7eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7e84.md#insn-00bc7eb4) · [`00bc7ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7e84.md#insn-00bc7ed4) · [`00bc7ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7e84.md#insn-00bc7ef8)
- 新版 [`00bc7f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7f20.md#insn-00bc7f50) · [`00bc7f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7f20.md#insn-00bc7f70) · [`00bc7f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc7/00bc7f20.md#insn-00bc7f94)

~~~diff
- 00bc7eb4 ["INT_ADD", "register:40f0:8", ["const:bc7eb4:8", "const:4:8"]]
- 00bc7eb4 ["CALL", null, ["callee:00497874:8"]]
+ 00bc7f50 ["INT_ADD", "register:40f0:8", ["const:bc7f50:8", "const:4:8"]]
+ 00bc7f50 ["CALL", null, ["callee:00497874:8"]]
- 00bc7eb4 bytes 603ee397
+ 00bc7f50 bytes 493ee397
- 00bc7ed4 ["INT_ADD", "register:40f0:8", ["const:bc7ed4:8", "const:4:8"]]
- 00bc7ed4 ["CALL", null, ["callee:00497874:8"]]
+ 00bc7f70 ["INT_ADD", "register:40f0:8", ["const:bc7f70:8", "const:4:8"]]
+ 00bc7f70 ["CALL", null, ["callee:00497874:8"]]
- 00bc7ed4 bytes 583ee397
+ 00bc7f70 bytes 413ee397
- 00bc7ef8 ["INT_ADD", "register:40f0:8", ["const:bc7ef8:8", "const:4:8"]]
- 00bc7ef8 ["CALL", null, ["callee:0058f5dc:8"]]
+ 00bc7f94 ["INT_ADD", "register:40f0:8", ["const:bc7f94:8", "const:4:8"]]
+ 00bc7f94 ["CALL", null, ["callee:0058f5dc:8"]]
- 00bc7ef8 bytes a91de797
+ 00bc7f94 bytes 921de797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-703c6b91b8cdf0573ff785a1b860fcf0"></a>

### [`00bc7f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7f6c.md) → [`00bc8008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8008.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal10GetBooleanEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6c0.md) · 呼出先 4件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 1件 [`00c5d790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d790.md) · 呼出先 4件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00bc80fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc80fc.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc804c",
      "incomplete_value": true,
      "site": "00bc805c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:650:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc7fb0",
      "incomplete_value": true,
      "site": "00bc7fc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:550:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc80a4",
      "incomplete_value": false,
      "site": "00bc80b0",
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
            "const:c89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc8008",
      "incomplete_value": false,
      "site": "00bc8014",
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
            "const:cd6:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc80a8",
      "incomplete_value": false,
      "site": "00bc80b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:8c3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc800c",
      "incomplete_value": false,
      "site": "00bc8014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:91f:8"
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
      "00bc804c",
      "READ",
      [
        "storage",
        "01126550",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc80a4",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc80a8",
      "PARAM",
      [
        "storage",
        "002aa91f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc804c",
      "READ",
      [
        "storage",
        "01126650",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc80a4",
      "PARAM",
      [
        "storage",
        "002a0c89",
        null,
        "string"
      ]
    ],
    [
      "00bc80a8",
      "PARAM",
      [
        "storage",
        "002aa8c3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc7fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7f6c.md#insn-00bc7fc0) · [`00bc8014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7f6c.md#insn-00bc8014) · [`00bc7f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7f6c.md#insn-00bc7f90)
- 新版 [`00bc805c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8008.md#insn-00bc805c) · [`00bc80b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8008.md#insn-00bc80b0) · [`00bc802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8008.md#insn-00bc802c)

~~~diff
- 00bc7fc0 ["INT_ADD", "register:40f0:8", ["const:bc7fc0:8", "const:4:8"]]
- 00bc7fc0 ["CALL", null, ["callee:00497a88:8"]]
+ 00bc805c ["INT_ADD", "register:40f0:8", ["const:bc805c:8", "const:4:8"]]
+ 00bc805c ["CALL", null, ["callee:00497a88:8"]]
- 00bc7fc0 bytes a23ee397
+ 00bc805c bytes 8b3ee397
- 00bc8014 ["INT_ADD", "register:40f0:8", ["const:bc8014:8", "const:4:8"]]
- 00bc8014 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bc80b0 ["INT_ADD", "register:40f0:8", ["const:bc80b0:8", "const:4:8"]]
+ 00bc80b0 ["CALL", null, ["callee:00c5ad70:8"]]
- 00bc8014 bytes 234b0294
+ 00bc80b0 bytes 304b0294
- 00bc7f90 ["INT_ADD", "register:40f0:8", ["const:bc7f90:8", "const:4:8"]]
- 00bc7f90 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bc802c ["INT_ADD", "register:40f0:8", ["const:bc802c:8", "const:4:8"]]
+ 00bc802c ["CALL", null, ["callee:00c5b150:8"]]
- 00bc7f90 bytes 3c4c0294
+ 00bc802c bytes 494c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43eb71664d8c8fa5bcf2723732e84484"></a>

### [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) → [`00bc80fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc80fc.md) FUN_00bc80fc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00bc7f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7f6c.md) [`00bc8218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8218.md) [`00bc830c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc830c.md) [`00bc840c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc840c.md) [`00bc857c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc857c.md) · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 5件 [`00bc8008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8008.md) [`00bc82b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc82b4.md) [`00bc83a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc83a8.md) [`00bc84a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc84a8.md) [`00bc8618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8618.md) · 呼出先 4件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8134",
      "incomplete_value": true,
      "site": "00bc8148",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00bc8098",
      "incomplete_value": true,
      "site": "00bc80ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e8:8"
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
      "definition_site": "00bc81a4",
      "incomplete_value": false,
      "site": "00bc81b0",
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
            "const:c89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc8108",
      "incomplete_value": false,
      "site": "00bc8114",
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
            "const:cd6:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc81a8",
      "incomplete_value": false,
      "site": "00bc81b0",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc810c",
      "incomplete_value": false,
      "site": "00bc8114",
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
            "const:871:8"
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
      "00bc8134",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc81a4",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc81a8",
      "PARAM",
      [
        "storage",
        "002a9871",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc8134",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc81a4",
      "PARAM",
      [
        "storage",
        "002a0c89",
        null,
        "string"
      ]
    ],
    [
      "00bc81a8",
      "PARAM",
      [
        "storage",
        "002a98a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc80ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md#insn-00bc80ac) · [`00bc8114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md#insn-00bc8114) · [`00bc816c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md#insn-00bc816c)
- 新版 [`00bc8148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc80fc.md#insn-00bc8148) · [`00bc81b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc80fc.md#insn-00bc81b0) · [`00bc8208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc80fc.md#insn-00bc8208)

~~~diff
- 00bc80ac ["INT_ADD", "register:40f0:8", ["const:bc80ac:8", "const:4:8"]]
- 00bc80ac ["CALL", null, ["callee:00497874:8"]]
+ 00bc8148 ["INT_ADD", "register:40f0:8", ["const:bc8148:8", "const:4:8"]]
+ 00bc8148 ["CALL", null, ["callee:00497874:8"]]
- 00bc80ac bytes e23de397
+ 00bc8148 bytes cb3de397
- 00bc8114 ["INT_ADD", "register:40f0:8", ["const:bc8114:8", "const:4:8"]]
- 00bc8114 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bc81b0 ["INT_ADD", "register:40f0:8", ["const:bc81b0:8", "const:4:8"]]
+ 00bc81b0 ["CALL", null, ["callee:00c5ad70:8"]]
- 00bc8114 bytes e34a0294
+ 00bc81b0 bytes f04a0294
- 00bc816c ["INT_ADD", "register:40f0:8", ["const:bc816c:8", "const:4:8"]]
- 00bc816c ["CALL", null, ["callee:005762f8:8"]]
+ 00bc8208 ["INT_ADD", "register:40f0:8", ["const:bc8208:8", "const:4:8"]]
+ 00bc8208 ["CALL", null, ["callee:005762f8:8"]]
- 00bc816c bytes 53b8e697
+ 00bc8208 bytes 3cb8e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a09ddddc8f1c03565e38980ff485b325"></a>

### [`00bc8218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8218.md) → [`00bc82b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc82b4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7GetLongEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d830.md) · 呼出先 4件 [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 1件 [`00c5d900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d900.md) · 呼出先 4件 [`0058f5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f5dc.md) [`00bc80fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc80fc.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc82f8",
      "incomplete_value": true,
      "site": "00bc8308",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:630:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc825c",
      "incomplete_value": true,
      "site": "00bc826c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8350",
      "incomplete_value": false,
      "site": "00bc835c",
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
            "const:c89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc82b4",
      "incomplete_value": false,
      "site": "00bc82c0",
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
            "const:cd6:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8354",
      "incomplete_value": false,
      "site": "00bc835c",
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
            "const:ba2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc82b8",
      "incomplete_value": false,
      "site": "00bc82c0",
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
            "const:bef:8"
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
      "00bc82f8",
      "READ",
      [
        "storage",
        "01126530",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8350",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc8354",
      "PARAM",
      [
        "storage",
        "002a0bef",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc82f8",
      "READ",
      [
        "storage",
        "01126630",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8350",
      "PARAM",
      [
        "storage",
        "002a0c89",
        null,
        "string"
      ]
    ],
    [
      "00bc8354",
      "PARAM",
      [
        "storage",
        "002a0ba2",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc826c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8218.md#insn-00bc826c) · [`00bc82c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8218.md#insn-00bc82c0) · [`00bc823c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8218.md#insn-00bc823c)
- 新版 [`00bc8308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc82b4.md#insn-00bc8308) · [`00bc835c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc82b4.md#insn-00bc835c) · [`00bc82d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc82b4.md#insn-00bc82d8)

~~~diff
- 00bc826c ["INT_ADD", "register:40f0:8", ["const:bc826c:8", "const:4:8"]]
- 00bc826c ["CALL", null, ["callee:0058f5dc:8"]]
+ 00bc8308 ["INT_ADD", "register:40f0:8", ["const:bc8308:8", "const:4:8"]]
+ 00bc8308 ["CALL", null, ["callee:0058f5dc:8"]]
- 00bc826c bytes cc1ce797
+ 00bc8308 bytes b51ce797
- 00bc82c0 ["INT_ADD", "register:40f0:8", ["const:bc82c0:8", "const:4:8"]]
- 00bc82c0 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bc835c ["INT_ADD", "register:40f0:8", ["const:bc835c:8", "const:4:8"]]
+ 00bc835c ["CALL", null, ["callee:00c5ad70:8"]]
- 00bc82c0 bytes 784a0294
+ 00bc835c bytes 854a0294
- 00bc823c ["INT_ADD", "register:40f0:8", ["const:bc823c:8", "const:4:8"]]
- 00bc823c ["CALL", null, ["callee:00c5b150:8"]]
+ 00bc82d8 ["INT_ADD", "register:40f0:8", ["const:bc82d8:8", "const:4:8"]]
+ 00bc82d8 ["CALL", null, ["callee:00c5b150:8"]]
- 00bc823c bytes 914b0294
+ 00bc82d8 bytes 9e4b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-432c2a9acf3d1a61f4a8fbfbecffd4ee"></a>

### [`00bc830c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc830c.md) → [`00bc83a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc83a8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal9GetDoubleEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d850.md) · 呼出先 4件 [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b230.md)
- 新版 呼出元 1件 [`00c5d920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d920.md) · 呼出先 4件 [`00bc80fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc80fc.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc83ec",
      "incomplete_value": true,
      "site": "00bc83fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00bc8350",
      "incomplete_value": true,
      "site": "00bc8360",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:538:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8444",
      "incomplete_value": false,
      "site": "00bc8450",
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
            "const:c89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc83a8",
      "incomplete_value": false,
      "site": "00bc83b4",
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
            "const:cd6:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8448",
      "incomplete_value": false,
      "site": "00bc8450",
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
            "const:217:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc83ac",
      "incomplete_value": false,
      "site": "00bc83b4",
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
            "const:273:8"
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
      "00bc83ec",
      "READ",
      [
        "storage",
        "01126538",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8444",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc8448",
      "PARAM",
      [
        "storage",
        "002ae273",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc83ec",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8444",
      "PARAM",
      [
        "storage",
        "002a0c89",
        null,
        "string"
      ]
    ],
    [
      "00bc8448",
      "PARAM",
      [
        "storage",
        "002ae217",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc8360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc830c.md#insn-00bc8360) · [`00bc83b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc830c.md#insn-00bc83b4) · [`00bc8330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc830c.md#insn-00bc8330)
- 新版 [`00bc83fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc83a8.md#insn-00bc83fc) · [`00bc8450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc83a8.md#insn-00bc8450) · [`00bc83cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc83a8.md#insn-00bc83cc)

~~~diff
- 00bc8360 ["INT_ADD", "register:40f0:8", ["const:bc8360:8", "const:4:8"]]
- 00bc8360 ["CALL", null, ["callee:00c5b300:8"]]
+ 00bc83fc ["INT_ADD", "register:40f0:8", ["const:bc83fc:8", "const:4:8"]]
+ 00bc83fc ["CALL", null, ["callee:00c5b300:8"]]
- 00bc8360 bytes b44b0294
+ 00bc83fc bytes c14b0294
- 00bc83b4 ["INT_ADD", "register:40f0:8", ["const:bc83b4:8", "const:4:8"]]
- 00bc83b4 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bc8450 ["INT_ADD", "register:40f0:8", ["const:bc8450:8", "const:4:8"]]
+ 00bc8450 ["CALL", null, ["callee:00c5ad70:8"]]
- 00bc83b4 bytes 3b4a0294
+ 00bc8450 bytes 484a0294
- 00bc8330 ["INT_ADD", "register:40f0:8", ["const:bc8330:8", "const:4:8"]]
- 00bc8330 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bc83cc ["INT_ADD", "register:40f0:8", ["const:bc83cc:8", "const:4:8"]]
+ 00bc83cc ["CALL", null, ["callee:00c5b150:8"]]
- 00bc8330 bytes 544b0294
+ 00bc83cc bytes 614b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b97120649bb8eeae180f6927f187f5ee"></a>

### [`00bc840c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc840c.md) → [`00bc84a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc84a8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal9GetStringEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d860.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 1件 [`00c5d930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d930.md) · 呼出先 7件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bc80fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc80fc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8510",
      "incomplete_value": true,
      "site": "00bc851c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:640:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc8474",
      "incomplete_value": true,
      "site": "00bc8480",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:540:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8574",
      "incomplete_value": false,
      "site": "00bc8580",
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
            "const:c89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc84d8",
      "incomplete_value": false,
      "site": "00bc84e4",
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
            "const:cd6:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8578",
      "incomplete_value": false,
      "site": "00bc8580",
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
            "const:5d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc84dc",
      "incomplete_value": false,
      "site": "00bc84e4",
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
            "const:5aa:8"
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
      "00bc8510",
      "READ",
      [
        "storage",
        "01126540",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8574",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc8578",
      "PARAM",
      [
        "storage",
        "002a95aa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc8510",
      "READ",
      [
        "storage",
        "01126640",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8574",
      "PARAM",
      [
        "storage",
        "002a0c89",
        null,
        "string"
      ]
    ],
    [
      "00bc8578",
      "PARAM",
      [
        "storage",
        "002a95d9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc8480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc840c.md#insn-00bc8480) · [`00bc84e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc840c.md#insn-00bc84e4) · [`00bc8450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc840c.md#insn-00bc8450)
- 新版 [`00bc851c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc84a8.md#insn-00bc851c) · [`00bc8580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc84a8.md#insn-00bc8580) · [`00bc84ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc84a8.md#insn-00bc84ec)

~~~diff
- 00bc8480 ["INT_ADD", "register:40f0:8", ["const:bc8480:8", "const:4:8"]]
- 00bc8480 ["CALL", null, ["callee:00497874:8"]]
+ 00bc851c ["INT_ADD", "register:40f0:8", ["const:bc851c:8", "const:4:8"]]
+ 00bc851c ["CALL", null, ["callee:00497874:8"]]
- 00bc8480 bytes ed3ce397
+ 00bc851c bytes d63ce397
- 00bc84e4 ["INT_ADD", "register:40f0:8", ["const:bc84e4:8", "const:4:8"]]
- 00bc84e4 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bc8580 ["INT_ADD", "register:40f0:8", ["const:bc8580:8", "const:4:8"]]
+ 00bc8580 ["CALL", null, ["callee:00c5ad70:8"]]
- 00bc84e4 bytes ef490294
+ 00bc8580 bytes fc490294
- 00bc8450 ["INT_ADD", "register:40f0:8", ["const:bc8450:8", "const:4:8"]]
- 00bc8450 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bc84ec ["INT_ADD", "register:40f0:8", ["const:bc84ec:8", "const:4:8"]]
+ 00bc84ec ["CALL", null, ["callee:00c5b150:8"]]
- 00bc8450 bytes 0c4b0294
+ 00bc84ec bytes 194b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1df6a288fa99802fc2325f3dd34141f2"></a>

### [`00bc857c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc857c.md) → [`00bc8618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8618.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7GetDataEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d810.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 1件 [`00c5d8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d8e0.md) · 呼出先 7件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bc80fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc80fc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8680",
      "incomplete_value": true,
      "site": "00bc868c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00bc85e4",
      "incomplete_value": true,
      "site": "00bc85f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:548:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc86e4",
      "incomplete_value": false,
      "site": "00bc86f0",
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
            "const:c89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc8648",
      "incomplete_value": false,
      "site": "00bc8654",
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
            "const:cd6:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc86e8",
      "incomplete_value": false,
      "site": "00bc86f0",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc864c",
      "incomplete_value": false,
      "site": "00bc8654",
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
            "const:f4c:8"
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
      "00bc8680",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc86e4",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc86e8",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc8680",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc86e4",
      "PARAM",
      [
        "storage",
        "002a0c89",
        null,
        "string"
      ]
    ],
    [
      "00bc86e8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc85f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc857c.md#insn-00bc85f0) · [`00bc8654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc857c.md#insn-00bc8654) · [`00bc85c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc857c.md#insn-00bc85c0)
- 新版 [`00bc868c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8618.md#insn-00bc868c) · [`00bc86f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8618.md#insn-00bc86f0) · [`00bc865c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8618.md#insn-00bc865c)

~~~diff
- 00bc85f0 ["INT_ADD", "register:40f0:8", ["const:bc85f0:8", "const:4:8"]]
- 00bc85f0 ["CALL", null, ["callee:00497874:8"]]
+ 00bc868c ["INT_ADD", "register:40f0:8", ["const:bc868c:8", "const:4:8"]]
+ 00bc868c ["CALL", null, ["callee:00497874:8"]]
- 00bc85f0 bytes 913ce397
+ 00bc868c bytes 7a3ce397
- 00bc8654 ["INT_ADD", "register:40f0:8", ["const:bc8654:8", "const:4:8"]]
- 00bc8654 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bc86f0 ["INT_ADD", "register:40f0:8", ["const:bc86f0:8", "const:4:8"]]
+ 00bc86f0 ["CALL", null, ["callee:00c5ad70:8"]]
- 00bc8654 bytes 93490294
+ 00bc86f0 bytes a0490294
- 00bc85c0 ["INT_ADD", "register:40f0:8", ["const:bc85c0:8", "const:4:8"]]
- 00bc85c0 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bc865c ["INT_ADD", "register:40f0:8", ["const:bc865c:8", "const:4:8"]]
+ 00bc865c ["CALL", null, ["callee:00c5b150:8"]]
- 00bc85c0 bytes b04a0294
+ 00bc865c bytes bd4a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c55619b79b5035b0d0e7157063197fa2"></a>

### [`00bc86ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc86ec.md) → [`00bc8788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8788.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal15GetKeysByPrefixEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d710.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005408d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408d0.md) [`0054a4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a4f4.md) [`0054dc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dc50.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5d7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d7e0.md) · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00540910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540910.md) [`0054a534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a534.md) [`0054dc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054dc90.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 96.35% / 新版 96.35%

CFGの説明率　旧版 64.29% / 新版 65.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8834"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8864"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc88d0"
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
      "00bc8810",
      "READ",
      [
        "storage",
        "011264f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc8834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc8904"
      ]
    ],
    [
      "unmatched:00bc8864",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc8964"
      ]
    ]
  ],
  "added": [
    [
      "00bc8810",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc88d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc8904"
      ]
    ],
    [
      "00bc8900",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc8964"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc8780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc86ec.md#insn-00bc8780) · [`00bc881c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc86ec.md#insn-00bc881c) · [`00bc8834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc86ec.md#insn-00bc8834)
- 新版 [`00bc881c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8788.md#insn-00bc881c) · [`00bc88b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8788.md#insn-00bc88b8)

~~~diff
- 00bc8780 ["INT_ADD", "register:40f0:8", ["const:bc8780:8", "const:4:8"]]
- 00bc8780 ["CALL", null, ["callee:00497874:8"]]
+ 00bc881c ["INT_ADD", "register:40f0:8", ["const:bc881c:8", "const:4:8"]]
+ 00bc881c ["CALL", null, ["callee:00497874:8"]]
- 00bc8780 bytes 2d3ce397
+ 00bc881c bytes 163ce397
- 00bc881c ["INT_ADD", "register:40f0:8", ["const:bc881c:8", "const:4:8"]]
- 00bc881c ["CALL", null, ["callee:00c580b0:8"]]
+ 00bc88b8 ["INT_ADD", "register:40f0:8", ["const:bc88b8:8", "const:4:8"]]
+ 00bc88b8 ["CALL", null, ["callee:00c580b0:8"]]
- 00bc881c bytes f13d0294
+ 00bc88b8 bytes fe3d0294
- 00bc8834 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc8834 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00bc8834 bytes a1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e3ff31f1b4e5c163e27eed9c218011f"></a>

### [`00bc89d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc89d8.md) → [`00bc8a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8a74.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal6GetAllEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7f0.md) · 呼出先 26件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) [`0087f0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f0a4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 1件 [`00c5d8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d8c0.md) · 呼出先 26件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`0058f5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f5dc.md) [`0087f0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f0fc.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 80.04% / 新版 80.04%

CFGの説明率　旧版 85.53% / 新版 87.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 17件

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8ca0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8d18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8d90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc8acc",
      "READ",
      [
        "storage",
        "011264f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8c1c",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8c3c",
      "READ",
      [
        "storage",
        "01126530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc8acc",
      "READ",
      [
        "storage",
        "011265f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8c1c",
      "READ",
      [
        "storage",
        "01126620",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8c3c",
      "READ",
      [
        "storage",
        "01126630",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc8a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc89d8.md#insn-00bc8a38) · [`00bc8ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc89d8.md#insn-00bc8ad4) · [`00bc8af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc89d8.md#insn-00bc8af4)
- 新版 [`00bc8ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8a74.md#insn-00bc8ad4) · [`00bc8b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8a74.md#insn-00bc8b70) · [`00bc8b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc8/00bc8a74.md#insn-00bc8b90)

~~~diff
- 00bc8a38 ["INT_ADD", "register:40f0:8", ["const:bc8a38:8", "const:4:8"]]
- 00bc8a38 ["CALL", null, ["callee:00497874:8"]]
+ 00bc8ad4 ["INT_ADD", "register:40f0:8", ["const:bc8ad4:8", "const:4:8"]]
+ 00bc8ad4 ["CALL", null, ["callee:00497874:8"]]
- 00bc8a38 bytes 7f3be397
+ 00bc8ad4 bytes 683be397
- 00bc8ad4 ["BRANCH", null, ["local:b46:8"]]
+ 00bc8b70 ["BRANCH", null, ["local:b44:8"]]
- 00bc8ad4 bytes 5a010014
+ 00bc8b70 bytes 5a010014
- 00bc8af4 ["CBRANCH", null, ["local:b45:8", "register:101:1"]]
+ 00bc8b90 ["CBRANCH", null, ["local:b43:8", "register:101:1"]]
- 00bc8af4 bytes 00290054
+ 00bc8b90 bytes 00290054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3530b9d5e37c224d1d84039e71c66afe"></a>

### [`00bc91f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc91f4.md) → [`00bc9290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9290.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17Remote

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d790.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bc9998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9998.md) [`00bc9fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fd0.md) [`00bc9fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fd4.md)
- 新版 呼出元 1件 [`00c5d860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d860.md) · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00bc9a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9a34.md) [`00bca06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca06c.md) [`00bca070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc9448",
      "incomplete_value": false,
      "site": "00bc9448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c91000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc93ac",
      "incomplete_value": false,
      "site": "00bc93ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c91000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "definition_site": "00bc93a0",
      "incomplete_value": true,
      "site": "00bc93b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9304",
      "incomplete_value": true,
      "site": "00bc9314",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:658:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc93a4",
      "incomplete_value": true,
      "site": "00bc93b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:768:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9308",
      "incomplete_value": true,
      "site": "00bc9314",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc93a0",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc93a4",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc93c8",
      "PARAM",
      [
        "storage",
        "002a1c28",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc93a0",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc93a4",
      "READ",
      [
        "storage",
        "01126768",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc93c8",
      "PARAM",
      [
        "storage",
        "002a1bdb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc91f4.md#insn-00bc9278) · [`00bc9314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc91f4.md#insn-00bc9314) · [`00bc9330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc91f4.md#insn-00bc9330)
- 新版 [`00bc9314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9290.md#insn-00bc9314) · [`00bc93b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9290.md#insn-00bc93b0) · [`00bc93cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9290.md#insn-00bc93cc)

~~~diff
- 00bc9278 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc9278 ["INT_ADD", "register:40f0:8", ["const:bc9278:8", "const:4:8"]]
- 00bc9278 ["CALLIND", null, ["register:0:8"]]
+ 00bc9314 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc9314 ["INT_ADD", "register:40f0:8", ["const:bc9314:8", "const:4:8"]]
+ 00bc9314 ["CALLIND", null, ["register:0:8"]]
- 00bc9278 bytes 00013fd6
+ 00bc9314 bytes 00013fd6
- 00bc9314 ["INT_ADD", "register:40f0:8", ["const:bc9314:8", "const:4:8"]]
- 00bc9314 ["CALL", null, ["callee:00589734:8"]]
+ 00bc93b0 ["INT_ADD", "register:40f0:8", ["const:bc93b0:8", "const:4:8"]]
+ 00bc93b0 ["CALL", null, ["callee:00589734:8"]]
- 00bc9314 bytes f800e797
+ 00bc93b0 bytes e100e797
- 00bc9330 ["INT_ADD", "register:40f0:8", ["const:bc9330:8", "const:4:8"]]
- 00bc9330 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc93cc ["INT_ADD", "register:40f0:8", ["const:bc93cc:8", "const:4:8"]]
+ 00bc93cc ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc9330 bytes 34470294
+ 00bc93cc bytes 41470294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-423fdd9f272cee25b332639cd148cda6"></a>

### [`00bc99c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc99c4.md) → [`00bc9a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9a60.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_13remote_config10ConfigInfoEZNS0_26CompleteWithResultInternalIS3_EEvRKNS_12Fut

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8d0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5d9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d9a0.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 62.50% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9acc",
      "incomplete_value": false,
      "site": "00bc9ad0",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9a30",
      "incomplete_value": false,
      "site": "00bc9a34",
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
            "const:e4:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9aec"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bc9b88"
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
      "00bc9acc",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc9acc",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc99c4.md#insn-00bc9a34) · [`00bc9aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc99c4.md#insn-00bc9aec)
- 新版 [`00bc9ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9a60.md#insn-00bc9ad0) · [`00bc9b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9a60.md#insn-00bc9b88)

~~~diff
- 00bc9a34 ["INT_ADD", "register:40f0:8", ["const:bc9a34:8", "const:4:8"]]
- 00bc9a34 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc9ad0 ["INT_ADD", "register:40f0:8", ["const:bc9ad0:8", "const:4:8"]]
+ 00bc9ad0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc9a34 bytes 73450294
+ 00bc9ad0 bytes 80450294
- 00bc9aec ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc9aec ["RETURN", null, ["register:0:8"]]
- 00bc9aec bytes c0035fd6
+ 00bc9b88 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bc9b88 ["RETURN", null, ["register:0:8"]]
+ 00bc9b88 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a034f6d841051e307d22380621d8b76"></a>

### [`00bc9af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9af0.md) → [`00bc9b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9b8c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIbZNS0_26CompleteWithResultInternalIbEEvRKNS_12FutureHandleEiPKcRKT_EUlPbE_EEvS5_i

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8e0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5d9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d9b0.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 12.50% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9bf8",
      "incomplete_value": false,
      "site": "00bc9bfc",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9b5c",
      "incomplete_value": false,
      "site": "00bc9b60",
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
            "const:e4:8"
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
      "definition_site": "00bc9bb0",
      "incomplete_value": true,
      "site": "00bc9bb4",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9c10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc9bd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc9be0"
      ]
    ],
    [
      "unmatched:00bc9b5c",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc9bd0",
      "READ",
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
      "00bc9bd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc9c7c"
      ]
    ],
    [
      "00bc9bf8",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ],
    [
      "00bc9c6c",
      "READ",
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

- 旧版 [`00bc9b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9af0.md#insn-00bc9b60) · [`00bc9b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9af0.md#insn-00bc9b74) · [`00bc9bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9af0.md#insn-00bc9bb4)
- 新版 [`00bc9bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9b8c.md#insn-00bc9bfc) · [`00bc9c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9b8c.md#insn-00bc9c10) · [`00bc9c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9b8c.md#insn-00bc9c50)

~~~diff
- 00bc9b60 ["INT_ADD", "register:40f0:8", ["const:bc9b60:8", "const:4:8"]]
- 00bc9b60 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc9bfc ["INT_ADD", "register:40f0:8", ["const:bc9bfc:8", "const:4:8"]]
+ 00bc9bfc ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc9b60 bytes 28450294
+ 00bc9bfc bytes 35450294
- 00bc9b74 ["INT_ADD", "register:40f0:8", ["const:bc9b74:8", "const:4:8"]]
- 00bc9b74 ["CALL", null, ["callee:00c5af40:8"]]
+ 00bc9c10 ["INT_ADD", "register:40f0:8", ["const:bc9c10:8", "const:4:8"]]
+ 00bc9c10 ["CALL", null, ["callee:00c5af40:8"]]
- 00bc9b74 bytes bf440294
+ 00bc9c10 bytes cc440294
- 00bc9bb4 ["INT_ADD", "register:40f0:8", ["const:bc9bb4:8", "const:4:8"]]
- 00bc9bb4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00bc9c50 ["INT_ADD", "register:40f0:8", ["const:bc9c50:8", "const:4:8"]]
+ 00bc9c50 ["CALL", null, ["callee:00c5b140:8"]]
- 00bc9bb4 bytes 2f450294
+ 00bc9c50 bytes 3c450294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc17866a54a5053340f67ae4197652b5"></a>

### [`00bc9c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9c20.md) → [`00bc9cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9cbc.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_13remote_config10ConfigInfoEEEvRKNS_12FutureHandleEiP

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8f0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5d9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d9c0.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9d20",
      "incomplete_value": false,
      "site": "00bc9d24",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9c84",
      "incomplete_value": false,
      "site": "00bc9c88",
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
            "const:e4:8"
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
      "definition_site": "00bc9c8c",
      "incomplete_value": true,
      "site": "00bc9c9c",
      "value": [
        "live",
        "register:4098:8"
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
      "definition_site": "00bc9c90",
      "incomplete_value": true,
      "site": "00bc9c9c",
      "value": [
        "live",
        "register:40b0:8"
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
      "unmatched:00bc9c84",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc9d20",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9c20.md#insn-00bc9c88) · [`00bc9c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9c20.md#insn-00bc9c9c) · [`00bc9cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9c20.md#insn-00bc9cc0)
- 新版 [`00bc9d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9cbc.md#insn-00bc9d24) · [`00bc9d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9cbc.md#insn-00bc9d38) · [`00bc9d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9cbc.md#insn-00bc9d5c)

~~~diff
- 00bc9c88 ["INT_ADD", "register:40f0:8", ["const:bc9c88:8", "const:4:8"]]
- 00bc9c88 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc9d24 ["INT_ADD", "register:40f0:8", ["const:bc9d24:8", "const:4:8"]]
+ 00bc9d24 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc9c88 bytes de440294
+ 00bc9d24 bytes eb440294
- 00bc9c9c ["INT_ADD", "register:40f0:8", ["const:bc9c9c:8", "const:4:8"]]
- 00bc9c9c ["CALL", null, ["callee:00c5af40:8"]]
+ 00bc9d38 ["INT_ADD", "register:40f0:8", ["const:bc9d38:8", "const:4:8"]]
+ 00bc9d38 ["CALL", null, ["callee:00c5af40:8"]]
- 00bc9c9c bytes 75440294
+ 00bc9d38 bytes 82440294
- 00bc9cc0 ["INT_ADD", "register:40f0:8", ["const:bc9cc0:8", "const:4:8"]]
- 00bc9cc0 ["CALL", null, ["callee:00c5af20:8"]]
+ 00bc9d5c ["INT_ADD", "register:40f0:8", ["const:bc9d5c:8", "const:4:8"]]
+ 00bc9d5c ["CALL", null, ["callee:00c5af20:8"]]
- 00bc9cc0 bytes 64440294
+ 00bc9d5c bytes 71440294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e35cde9319fe37c8d2b2e23abe55ddb"></a>

### [`00bc9dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9dd4.md) → [`00bc9e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9e70.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIbEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d900.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5d9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d9d0.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 30.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9e8c",
      "incomplete_value": true,
      "site": "00bc9e9c",
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
    "old": {
      "definition_site": "00bc9df0",
      "incomplete_value": true,
      "site": "00bc9e00",
      "value": [
        "live",
        "register:40c0:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9ed4",
      "incomplete_value": false,
      "site": "00bc9ed8",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9e38",
      "incomplete_value": false,
      "site": "00bc9e3c",
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
            "const:e4:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ed8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc9eac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc9eb0"
      ]
    ],
    [
      "00bc9ed4",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "00bc9f28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc9f4c"
      ]
    ]
  ],
  "added": [
    [
      "00bc9eac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc9f4c"
      ]
    ],
    [
      "00bc9ed4",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ],
    [
      "00bc9f28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc9f64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9dd4.md#insn-00bc9e00) · [`00bc9e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9dd4.md#insn-00bc9e3c) · [`00bc9ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9dd4.md#insn-00bc9ed8)
- 新版 [`00bc9e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9e70.md#insn-00bc9e9c) · [`00bc9ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9e70.md#insn-00bc9ed8)

~~~diff
- 00bc9e00 ["INT_ADD", "register:40f0:8", ["const:bc9e00:8", "const:4:8"]]
- 00bc9e00 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bc9e9c ["INT_ADD", "register:40f0:8", ["const:bc9e9c:8", "const:4:8"]]
+ 00bc9e9c ["CALL", null, ["callee:00c5aad0:8"]]
- 00bc9e00 bytes 00430294
+ 00bc9e9c bytes 0d430294
- 00bc9e3c ["INT_ADD", "register:40f0:8", ["const:bc9e3c:8", "const:4:8"]]
- 00bc9e3c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc9ed8 ["INT_ADD", "register:40f0:8", ["const:bc9ed8:8", "const:4:8"]]
+ 00bc9ed8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc9e3c bytes 71440294
+ 00bc9ed8 bytes 7e440294
- 00bc9ed8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc9ed8 ["RETURN", null, ["register:0:8"]]
- 00bc9ed8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ab91b3fde2bfc5912ca85f4be0f0492"></a>

### [`00bc9fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fd8.md) → [`00bca074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca074.md) FUN_00bca074

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b340.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b410.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.91% / 新版 73.91%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9fd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9fd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9fdc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc9fd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc9fdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc9ff4",
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
      "00bca074",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bca078",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bca090",
      "READ",
      [
        "storage",
        "011267a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fd8.md#insn-00bc9fd8) · [`00bc9fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fd8.md#insn-00bc9fdc) · [`00bc9ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fd8.md#insn-00bc9ffc)
- 新版 [`00bca098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca074.md#insn-00bca098)

~~~diff
- 00bc9fd8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc9fd8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc9fd8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc9fd8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc9fd8 bytes f44fbea9
- 00bc9fdc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc9fdc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc9fdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc9fdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc9fdc bytes fd7b01a9
- 00bc9ffc ["INT_ADD", "register:40f0:8", ["const:bc9ffc:8", "const:4:8"]]
- 00bc9ffc ["CALL", null, ["callee:00574d2c:8"]]
+ 00bca098 ["INT_ADD", "register:40f0:8", ["const:bca098:8", "const:4:8"]]
+ 00bca098 ["CALL", null, ["callee:00574d2c:8"]]
- 00bc9ffc bytes 3cabe697
+ 00bca098 bytes 25abe697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b74ebc49a5915add3149ab96772c0390"></a>

### [`00bca05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca05c.md) → [`00bca0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca0f8.md) _INIT_289

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc3c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3c14.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc3cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3cb0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bca114",
      "incomplete_value": true,
      "site": "00bca114",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca078",
      "incomplete_value": true,
      "site": "00bca078",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca114",
      "incomplete_value": true,
      "site": "00bca118",
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
      "definition_site": "00bca078",
      "incomplete_value": true,
      "site": "00bca07c",
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
      "00bca108",
      "READ",
      [
        "storage",
        "00c9b978",
        null,
        "pointer"
      ]
    ],
    [
      "00bca114",
      "WRITE",
      [
        "storage",
        "011266b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ],
    [
      "00bca114",
      "PARAM",
      [
        "storage",
        "011266bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca108",
      "READ",
      [
        "storage",
        "00c9ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00bca114",
      "WRITE",
      [
        "storage",
        "011267b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ],
    [
      "00bca114",
      "PARAM",
      [
        "storage",
        "011267bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca05c.md#insn-00bca07c) · [`00bca06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca05c.md#insn-00bca06c) · [`00bca084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca05c.md#insn-00bca084)
- 新版 [`00bca118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca0f8.md#insn-00bca118) · [`00bca108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca0f8.md#insn-00bca108) · [`00bca120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca0f8.md#insn-00bca120)

~~~diff
- 00bca07c ["INT_ADD", "register:40f0:8", ["const:bca07c:8", "const:4:8"]]
- 00bca07c ["CALL", null, ["callee:00c5ad50:8"]]
+ 00bca118 ["INT_ADD", "register:40f0:8", ["const:bca118:8", "const:4:8"]]
+ 00bca118 ["CALL", null, ["callee:00c5ad50:8"]]
- 00bca07c bytes 01430294
+ 00bca118 bytes 0e430294
- 00bca06c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
- 00bca06c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bca108 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00bca108 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00bca06c bytes 73be44f9
+ 00bca108 bytes 732645f9
- 00bca084 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:998:8"]]
- 00bca084 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bca120 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:a68:8"]]
+ 00bca120 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00bca084 bytes 00cc44f9
+ 00bca120 bytes 003445f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-597634e8bf31df80fb2fb927444e02e2"></a>

### [`00bca200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca200.md) → [`00bca29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca29c.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 41.18% / 新版 41.18%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bca200"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bca204"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bca204"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bca200",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bca204",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bca214",
      "READ",
      [
        "storage",
        "00c9b928",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bca29c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bca2a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bca2b0",
      "READ",
      [
        "storage",
        "00c9b9f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca200.md#insn-00bca200) · [`00bca204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca200.md#insn-00bca204) · [`00bca220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca200.md#insn-00bca220)

~~~diff
- 00bca200 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bca200 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bca200 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bca200 bytes f30f1ef8
- 00bca204 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bca204 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bca204 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bca204 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bca204 bytes fd7b01a9
- 00bca220 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bca220 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bca220 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2b95a41664db8d3a753194666411771"></a>

### [`00bca4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4e4.md) → [`00bca580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca580.md) _ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9c0.md) · 呼出先 8件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md)
- 新版 呼出元 1件 [`00c5aa90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa90.md) · 呼出先 8件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.17% / 新版 99.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bca5cc",
      "incomplete_value": true,
      "site": "00bca5cc",
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
      "definition_site": "00bca530",
      "incomplete_value": true,
      "site": "00bca530",
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
      "definition_site": "00bca5ac",
      "incomplete_value": true,
      "site": "00bca5b0",
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
      "definition_site": "00bca510",
      "incomplete_value": true,
      "site": "00bca514",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca674",
      "incomplete_value": false,
      "site": "00bca680",
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
            "const:2f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca5d8",
      "incomplete_value": false,
      "site": "00bca5e4",
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
            "const:34e:8"
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
      "00bca59c",
      "READ",
      [
        "storage",
        "00c9b9a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bca5a8",
      "READ",
      [
        "storage",
        "01126720",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bca5b4",
      "READ",
      [
        "storage",
        "01126720",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bca59c",
      "READ",
      [
        "storage",
        "00c9ba70",
        null,
        "pointer"
      ]
    ],
    [
      "00bca5a8",
      "READ",
      [
        "storage",
        "01126820",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bca5b4",
      "READ",
      [
        "storage",
        "01126820",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4e4.md#insn-00bca514) · [`00bca5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4e4.md#insn-00bca5b0) · [`00bca5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4e4.md#insn-00bca5e4)
- 新版 [`00bca5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca580.md#insn-00bca5b0) · [`00bca64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca580.md#insn-00bca64c) · [`00bca680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca580.md#insn-00bca680)

~~~diff
- 00bca514 ["INT_ADD", "register:40f0:8", ["const:bca514:8", "const:4:8"]]
- 00bca514 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bca5b0 ["INT_ADD", "register:40f0:8", ["const:bca5b0:8", "const:4:8"]]
+ 00bca5b0 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bca514 bytes 3b410294
+ 00bca5b0 bytes 48410294
- 00bca5b0 ["INT_ADD", "register:40f0:8", ["const:bca5b0:8", "const:4:8"]]
- 00bca5b0 ["CALL", null, ["callee:00c5daa0:8"]]
+ 00bca64c ["INT_ADD", "register:40f0:8", ["const:bca64c:8", "const:4:8"]]
+ 00bca64c ["CALL", null, ["callee:00c5daa0:8"]]
- 00bca5b0 bytes 084d0294
+ 00bca64c bytes 154d0294
- 00bca5e4 ["INT_ADD", "register:40f0:8", ["const:bca5e4:8", "const:4:8"]]
- 00bca5e4 ["CALL", null, ["callee:00c5b200:8"]]
+ 00bca680 ["INT_ADD", "register:40f0:8", ["const:bca680:8", "const:4:8"]]
+ 00bca680 ["CALL", null, ["callee:00c5b200:8"]]
- 00bca5e4 bytes d3420294
+ 00bca680 bytes e0420294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdebcef5d18e85f18f919b6fc91754fa"></a>

### [`00bca790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca790.md) → [`00bca82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca82c.md) _ZN8firebase4auth4AuthC1EPNS_3AppEPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5da90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da90.md) · 呼出先 10件 [`00bcbdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbdac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md)
- 新版 呼出元 1件 [`00c5db60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db60.md) · 呼出先 10件 [`00bcbe48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbe48.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca87c",
      "incomplete_value": false,
      "site": "00bca880",
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
            "const:4b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca7e0",
      "incomplete_value": false,
      "site": "00bca7e4",
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
            "const:512:8"
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
      "definition_site": "00bca8a0",
      "incomplete_value": false,
      "site": "00bca8ac",
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
            "const:bb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca804",
      "incomplete_value": false,
      "site": "00bca810",
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
            "const:10f:8"
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
      "definition_site": "00bca904",
      "incomplete_value": false,
      "site": "00bca90c",
      "value": [
        "leaf",
        "const:bcbe48:8"
      ]
    },
    "old": {
      "definition_site": "00bca868",
      "incomplete_value": false,
      "site": "00bca870",
      "value": [
        "leaf",
        "const:bcbdac:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bca87c",
      "PARAM",
      [
        "storage",
        "002af512",
        null,
        "string"
      ]
    ],
    [
      "00bca8a0",
      "PARAM",
      [
        "storage",
        "002bc10f",
        null,
        null
      ]
    ],
    [
      "00bca904",
      "PARAM",
      [
        "storage",
        "00bcbdac",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca87c",
      "PARAM",
      [
        "storage",
        "002af4b6",
        null,
        "string"
      ]
    ],
    [
      "00bca8a0",
      "PARAM",
      [
        "storage",
        "002bc0bb",
        null,
        null
      ]
    ],
    [
      "00bca904",
      "PARAM",
      [
        "storage",
        "00bcbe48",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca790.md#insn-00bca7e4) · [`00bca810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca790.md#insn-00bca810) · [`00bca870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca790.md#insn-00bca870)
- 新版 [`00bca880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca82c.md#insn-00bca880) · [`00bca8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca82c.md#insn-00bca8ac) · [`00bca90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca82c.md#insn-00bca90c)

~~~diff
- 00bca7e4 ["INT_ADD", "register:40f0:8", ["const:bca7e4:8", "const:4:8"]]
- 00bca7e4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bca880 ["INT_ADD", "register:40f0:8", ["const:bca880:8", "const:4:8"]]
+ 00bca880 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bca7e4 bytes 07420294
+ 00bca880 bytes 14420294
- 00bca810 ["INT_ADD", "register:40f0:8", ["const:bca810:8", "const:4:8"]]
- 00bca810 ["CALL", null, ["callee:00c5be30:8"]]
+ 00bca8ac ["INT_ADD", "register:40f0:8", ["const:bca8ac:8", "const:4:8"]]
+ 00bca8ac ["CALL", null, ["callee:00c5be30:8"]]
- 00bca810 bytes 54450294
+ 00bca8ac bytes 61450294
- 00bca870 ["INT_ADD", "register:40f0:8", ["const:bca870:8", "const:4:8"]]
- 00bca870 ["CALL", null, ["callee:00c5acd0:8"]]
+ 00bca90c ["INT_ADD", "register:40f0:8", ["const:bca90c:8", "const:4:8"]]
+ 00bca90c ["CALL", null, ["callee:00c5acd0:8"]]
- 00bca870 bytes e4400294
+ 00bca90c bytes f1400294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e8fa686d4da5b664ac9d6bfa2e14a78"></a>

### [`00bcaa3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcaa3c.md) → [`00bcaad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcaad8.md) _ZN8firebase4auth4Auth14DeleteInternalEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5da30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da30.md) · 呼出先 14件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)
- 新版 呼出元 1件 [`00c5db00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db00.md) · 呼出先 14件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acc0.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.27% / 新版 99.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcab6c",
      "incomplete_value": true,
      "site": "00bcab70",
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
      "definition_site": "00bcaad0",
      "incomplete_value": true,
      "site": "00bcaad4",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcaaf8",
      "incomplete_value": true,
      "site": "00bcaafc",
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
      "definition_site": "00bcaa5c",
      "incomplete_value": true,
      "site": "00bcaa60",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcabe4",
      "incomplete_value": false,
      "site": "00bcabec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:bc9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcab48",
      "incomplete_value": false,
      "site": "00bcab50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:c16:8"
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
      "00bcaaec",
      "READ",
      [
        "storage",
        "00c9b9a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcaaf4",
      "READ",
      [
        "storage",
        "01126720",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bcab60",
      "READ",
      [
        "storage",
        "00c9b9a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bcaaec",
      "READ",
      [
        "storage",
        "00c9ba70",
        null,
        "pointer"
      ]
    ],
    [
      "00bcaaf4",
      "READ",
      [
        "storage",
        "01126820",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bcab60",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcaa60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcaa3c.md#insn-00bcaa60) · [`00bcaab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcaa3c.md#insn-00bcaab4) · [`00bcab50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcaa3c.md#insn-00bcab50)
- 新版 [`00bcaafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcaad8.md#insn-00bcaafc) · [`00bcab50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcaad8.md#insn-00bcab50) · [`00bcabec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcaad8.md#insn-00bcabec)

~~~diff
- 00bcaa60 ["INT_ADD", "register:40f0:8", ["const:bcaa60:8", "const:4:8"]]
- 00bcaa60 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcaafc ["INT_ADD", "register:40f0:8", ["const:bcaafc:8", "const:4:8"]]
+ 00bcaafc ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcaa60 bytes e83f0294
+ 00bcaafc bytes f53f0294
- 00bcaab4 ["INT_ADD", "register:40f0:8", ["const:bcaab4:8", "const:4:8"]]
- 00bcaab4 ["CALL", null, ["callee:00c5acc0:8"]]
+ 00bcab50 ["INT_ADD", "register:40f0:8", ["const:bcab50:8", "const:4:8"]]
+ 00bcab50 ["CALL", null, ["callee:00c5acc0:8"]]
- 00bcaab4 bytes 4f400294
+ 00bcab50 bytes 5c400294
- 00bcab50 ["INT_ADD", "register:40f0:8", ["const:bcab50:8", "const:4:8"]]
- 00bcab50 ["CALL", null, ["callee:00c5b200:8"]]
+ 00bcabec ["INT_ADD", "register:40f0:8", ["const:bcabec:8", "const:4:8"]]
+ 00bcabec ["CALL", null, ["callee:00c5b200:8"]]
- 00bcab50 bytes 78410294
+ 00bcabec bytes 85410294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f5fae9aa6279343cc4620c0dfece785"></a>

### [`00bcadfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcadfc.md) → [`00bcae98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcae98.md) _ZN8firebase4auth4Auth3appEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5da80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da80.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5db50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db50.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcaeb4",
      "incomplete_value": false,
      "site": "00bcaeb8",
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
            "const:6ac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcae18",
      "incomplete_value": false,
      "site": "00bcae1c",
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
            "const:708:8"
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
      "00bcaeb4",
      "PARAM",
      [
        "storage",
        "002b1708",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcaeb4",
      "PARAM",
      [
        "storage",
        "002b16ac",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcae1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcadfc.md#insn-00bcae1c) · [`00bcae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcadfc.md#insn-00bcae18)
- 新版 [`00bcaeb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcae98.md#insn-00bcaeb8) · [`00bcaeb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcae98.md#insn-00bcaeb4)

~~~diff
- 00bcae1c ["INT_ADD", "register:40f0:8", ["const:bcae1c:8", "const:4:8"]]
- 00bcae1c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bcaeb8 ["INT_ADD", "register:40f0:8", ["const:bcaeb8:8", "const:4:8"]]
+ 00bcaeb8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bcae1c bytes 79400294
+ 00bcaeb8 bytes 86400294
- 00bcae18 ["COPY", "tmp:0:8", ["const:708:8"]]
- 00bcae18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcae18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcae18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcaeb4 ["COPY", "tmp:0:8", ["const:6ac:8"]]
+ 00bcaeb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcaeb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcaeb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcae18 bytes 00201c91
+ 00bcaeb4 bytes 00b01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc8611aea392bf331bcb4e09a0236ab3"></a>

### [`00bcae34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcae34.md) → [`00bcaed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcaed0.md) _ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5daf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5daf0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5dbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dbc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcb048",
      "incomplete_value": false,
      "site": "00bcb04c",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcafac",
      "incomplete_value": false,
      "site": "00bcafb0",
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
            "const:c6c:8"
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
      "00bcb048",
      "PARAM",
      [
        "storage",
        "002b8c6c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcb048",
      "PARAM",
      [
        "storage",
        "002b8c18",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcafb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcae34.md#insn-00bcafb0) · [`00bcae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcae34.md#insn-00bcae70) · [`00bcaef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcae34.md#insn-00bcaef4)
- 新版 [`00bcb04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcaed0.md#insn-00bcb04c) · [`00bcaf0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcaed0.md#insn-00bcaf0c) · [`00bcaf90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcaed0.md#insn-00bcaf90)

~~~diff
- 00bcafb0 ["INT_ADD", "register:40f0:8", ["const:bcafb0:8", "const:4:8"]]
- 00bcafb0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bcb04c ["INT_ADD", "register:40f0:8", ["const:bcb04c:8", "const:4:8"]]
+ 00bcb04c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bcafb0 bytes 14400294
+ 00bcb04c bytes 21400294
- 00bcae70 ["INT_ADD", "register:40f0:8", ["const:bcae70:8", "const:4:8"]]
- 00bcae70 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcaf0c ["INT_ADD", "register:40f0:8", ["const:bcaf0c:8", "const:4:8"]]
+ 00bcaf0c ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcae70 bytes e43e0294
+ 00bcaf0c bytes f13e0294
- 00bcaef4 ["INT_ADD", "register:40f0:8", ["const:bcaef4:8", "const:4:8"]]
- 00bcaef4 ["CALL", null, ["callee:00c5dbc0:8"]]
+ 00bcaf90 ["INT_ADD", "register:40f0:8", ["const:bcaf90:8", "const:4:8"]]
+ 00bcaf90 ["CALL", null, ["callee:00c5dbc0:8"]]
- 00bcaef4 bytes ff4a0294
+ 00bcaf90 bytes 0c4b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-819a857ff35d124c52d4c4d05c27b873"></a>

### [`00bcb004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb004.md) → [`00bcb0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb0a0.md) _ZN8firebase4auth4Auth18AddIdTokenListenerEPNS0_15IdTokenListenerE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5d9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9e0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5dab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.68% / 新版 84.68%

CFGの説明率　旧版 29.31% / 新版 27.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb138"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcb1d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb0a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcb10c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcb0a4"
      ]
    ],
    [
      "00bcb128",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcb0a4"
      ]
    ],
    [
      "unmatched:00bcb0a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb12c"
      ]
    ]
  ],
  "added": [
    [
      "00bcb10c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb140"
      ]
    ],
    [
      "00bcb128",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb140"
      ]
    ],
    [
      "00bcb13c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb12c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb004.md#insn-00bcb040) · [`00bcb0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb004.md#insn-00bcb0a0) · [`00bcb0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb004.md#insn-00bcb0ac)
- 新版 [`00bcb0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb0a0.md#insn-00bcb0dc)

~~~diff
- 00bcb040 ["INT_ADD", "register:40f0:8", ["const:bcb040:8", "const:4:8"]]
- 00bcb040 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcb0dc ["INT_ADD", "register:40f0:8", ["const:bcb0dc:8", "const:4:8"]]
+ 00bcb0dc ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcb040 bytes 703e0294
+ 00bcb0dc bytes 7d3e0294
- 00bcb0a0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcb0a0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bcb0a0 bytes 81ffff54
- 00bcb0ac ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00bcb0ac bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bcde131bd775ae82aa574d7d5a9e641"></a>

### [`00bcb2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb2f0.md) → [`00bcb38c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb38c.md) _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5da60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da60.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5da00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da00.md)
- 新版 呼出元 1件 [`00c5db30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db30.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5dad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dad0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 83.72% / 新版 83.72%

CFGの説明率　旧版 47.50% / 新版 48.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb334"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb350"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb364"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcb334",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb42c"
      ]
    ],
    [
      "00bcb3dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcb368"
      ]
    ],
    [
      "unmatched:00bcb350",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb42c"
      ]
    ]
  ],
  "added": [
    [
      "00bcb3d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb42c"
      ]
    ],
    [
      "00bcb3dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb404"
      ]
    ],
    [
      "00bcb3ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb42c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb2f0.md#insn-00bcb308) · [`00bcb334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb2f0.md#insn-00bcb334) · [`00bcb350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb2f0.md#insn-00bcb350)
- 新版 [`00bcb3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb38c.md#insn-00bcb3a4)

~~~diff
- 00bcb308 ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
- 00bcb308 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
+ 00bcb3a4 ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
+ 00bcb3a4 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00bcb308 bytes 780900b4
+ 00bcb3a4 bytes 780900b4
- 00bcb334 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00bcb334 bytes e0020054
- 00bcb350 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00bcb350 bytes 00020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5310ed5d2c457a547d33af8c2ccf6b31"></a>

### [`00bcb554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb554.md) → [`00bcb5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb5f0.md) _ZN8firebase4auth24NotifyAuthStateListenersEPNS0_8AuthDataE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5da10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da10.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md)
- 新版 呼出元 1件 [`00c5dae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dae0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcb640",
      "incomplete_value": false,
      "site": "00bcb644",
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
            "const:3d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb5a4",
      "incomplete_value": false,
      "site": "00bcb5a8",
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
            "const:42a:8"
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
      "00bcb640",
      "PARAM",
      [
        "storage",
        "002bd42a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcb640",
      "PARAM",
      [
        "storage",
        "002bd3d6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb554.md#insn-00bcb5a8) · [`00bcb580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb554.md#insn-00bcb580) · [`00bcb590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb554.md#insn-00bcb590)
- 新版 [`00bcb644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb5f0.md#insn-00bcb644) · [`00bcb61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb5f0.md#insn-00bcb61c) · [`00bcb62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb5f0.md#insn-00bcb62c)

~~~diff
- 00bcb5a8 ["INT_ADD", "register:40f0:8", ["const:bcb5a8:8", "const:4:8"]]
- 00bcb5a8 ["CALL", null, ["callee:00c5b200:8"]]
+ 00bcb644 ["INT_ADD", "register:40f0:8", ["const:bcb644:8", "const:4:8"]]
+ 00bcb644 ["CALL", null, ["callee:00c5b200:8"]]
- 00bcb5a8 bytes e23e0294
+ 00bcb644 bytes ef3e0294
- 00bcb580 ["INT_ADD", "register:40f0:8", ["const:bcb580:8", "const:4:8"]]
- 00bcb580 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcb61c ["INT_ADD", "register:40f0:8", ["const:bcb61c:8", "const:4:8"]]
+ 00bcb61c ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcb580 bytes 203d0294
+ 00bcb61c bytes 2d3d0294
- 00bcb590 ["INT_ADD", "register:40f0:8", ["const:bcb590:8", "const:4:8"]]
- 00bcb590 ["CALL", null, ["callee:00c5dbd0:8"]]
+ 00bcb62c ["INT_ADD", "register:40f0:8", ["const:bcb62c:8", "const:4:8"]]
+ 00bcb62c ["CALL", null, ["callee:00c5dbd0:8"]]
- 00bcb590 bytes 5c490294
+ 00bcb62c bytes 69490294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5eea37a420830ed6be445ca741f2cfa"></a>

### [`00bcb77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb77c.md) → [`00bcb818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb818.md) _ZN8firebase4auth22NotifyIdTokenListenersEPNS0_8AuthDataE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9f0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md)
- 新版 呼出元 1件 [`00c5dac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dac0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcb868",
      "incomplete_value": false,
      "site": "00bcb86c",
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
            "const:18d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb7cc",
      "incomplete_value": false,
      "site": "00bcb7d0",
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
            "const:1e9:8"
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
      "00bcb868",
      "PARAM",
      [
        "storage",
        "002a61e9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcb868",
      "PARAM",
      [
        "storage",
        "002a618d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb77c.md#insn-00bcb7d0) · [`00bcb7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb77c.md#insn-00bcb7a8) · [`00bcb7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb77c.md#insn-00bcb7b8)
- 新版 [`00bcb86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb818.md#insn-00bcb86c) · [`00bcb844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb818.md#insn-00bcb844) · [`00bcb854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb818.md#insn-00bcb854)

~~~diff
- 00bcb7d0 ["INT_ADD", "register:40f0:8", ["const:bcb7d0:8", "const:4:8"]]
- 00bcb7d0 ["CALL", null, ["callee:00c5b200:8"]]
+ 00bcb86c ["INT_ADD", "register:40f0:8", ["const:bcb86c:8", "const:4:8"]]
+ 00bcb86c ["CALL", null, ["callee:00c5b200:8"]]
- 00bcb7d0 bytes 583e0294
+ 00bcb86c bytes 653e0294
- 00bcb7a8 ["INT_ADD", "register:40f0:8", ["const:bcb7a8:8", "const:4:8"]]
- 00bcb7a8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcb844 ["INT_ADD", "register:40f0:8", ["const:bcb844:8", "const:4:8"]]
+ 00bcb844 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcb7a8 bytes 963c0294
+ 00bcb844 bytes a33c0294
- 00bcb7b8 ["INT_ADD", "register:40f0:8", ["const:bcb7b8:8", "const:4:8"]]
- 00bcb7b8 ["CALL", null, ["callee:00c5dbb0:8"]]
+ 00bcb854 ["INT_ADD", "register:40f0:8", ["const:bcb854:8", "const:4:8"]]
+ 00bcb854 ["CALL", null, ["callee:00c5dbb0:8"]]
- 00bcb7b8 bytes ca480294
+ 00bcb854 bytes d7480294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-338638432d84b6272d3fd8559c3643c8"></a>

### [`00bcbb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbb54.md) → [`00bcbbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbbf0.md) _ZNK8firebase4auth4Auth45SignInAndRetrieveDataWithCredentialLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbb54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbb58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbb58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcbb54",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcbb58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcbb5c",
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
      "00bcbbf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcbbf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcbbf8",
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

- 旧版 [`00bcbb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbb54.md#insn-00bcbb54) · [`00bcbb58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbb54.md#insn-00bcbb58) · [`00bcbb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbb54.md#insn-00bcbb5c)

~~~diff
- 00bcbb54 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bcbb54 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcbb54 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcbb54 bytes f50f1df8
- 00bcbb58 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcbb58 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcbb58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcbb58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcbb58 bytes f44f01a9
- 00bcbb5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcbb5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcbb5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcbb5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcbb5c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87446524a28dabb3f453386db89b4c78"></a>

### [`00bcbbe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbbe4.md) → [`00bcbc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbc80.md) _ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcbc9c",
      "incomplete_value": true,
      "site": "00bcbca0",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": {
      "definition_site": "00bcbc00",
      "incomplete_value": true,
      "site": "00bcbc04",
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
            "const:18:8"
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
      "definition_site": "00bcbcc4",
      "incomplete_value": true,
      "site": "00bcbcc8",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbc04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbbe4.md#insn-00bcbc04) · [`00bcbc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbbe4.md#insn-00bcbc2c) · [`00bcbc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbbe4.md#insn-00bcbc00)
- 新版 [`00bcbca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbc80.md#insn-00bcbca0) · [`00bcbcc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbc80.md#insn-00bcbcc8)

~~~diff
- 00bcbc04 ["INT_ADD", "register:40f0:8", ["const:bcbc04:8", "const:4:8"]]
- 00bcbc04 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcbca0 ["INT_ADD", "register:40f0:8", ["const:bcbca0:8", "const:4:8"]]
+ 00bcbca0 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcbc04 bytes 7f3b0294
+ 00bcbca0 bytes 8c3b0294
- 00bcbc2c ["INT_ADD", "register:40f0:8", ["const:bcbc2c:8", "const:4:8"]]
- 00bcbc2c ["CALL", null, ["callee:00c5aee0:8"]]
+ 00bcbcc8 ["INT_ADD", "register:40f0:8", ["const:bcbcc8:8", "const:4:8"]]
+ 00bcbcc8 ["CALL", null, ["callee:00c5aee0:8"]]
- 00bcbc2c bytes 793c0294
+ 00bcbcc8 bytes 863c0294
- 00bcbc00 ["COPY", "register:4000:8", ["register:40a0:8"]]
- 00bcbc00 bytes e00314aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48a8d505f2c820075fc409fe3481a2be"></a>

### [`00bcbd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbd04.md) → [`00bcbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbda0.md) _ZNK8firebase4auth4Auth40CreateUserWithEmailAndPasswordLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcbdbc",
      "incomplete_value": true,
      "site": "00bcbdc0",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcbde4",
      "incomplete_value": true,
      "site": "00bcbde8",
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
            "const:30:8"
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
    "new": null,
    "old": {
      "definition_site": "00bcbd54",
      "incomplete_value": true,
      "site": "00bcbd58",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbd04.md#insn-00bcbd24) · [`00bcbd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbd04.md#insn-00bcbd4c) · [`00bcbd58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbd04.md#insn-00bcbd58)
- 新版 [`00bcbdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbda0.md#insn-00bcbdc0) · [`00bcbde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbda0.md#insn-00bcbde8) · [`00bcbdf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbda0.md#insn-00bcbdf4)

~~~diff
- 00bcbd24 ["INT_ADD", "register:40f0:8", ["const:bcbd24:8", "const:4:8"]]
- 00bcbd24 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcbdc0 ["INT_ADD", "register:40f0:8", ["const:bcbdc0:8", "const:4:8"]]
+ 00bcbdc0 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcbd24 bytes 373b0294
+ 00bcbdc0 bytes 443b0294
- 00bcbd4c ["INT_ADD", "register:40f0:8", ["const:bcbd4c:8", "const:4:8"]]
- 00bcbd4c ["CALL", null, ["callee:00c5aee0:8"]]
+ 00bcbde8 ["INT_ADD", "register:40f0:8", ["const:bcbde8:8", "const:4:8"]]
+ 00bcbde8 ["CALL", null, ["callee:00c5aee0:8"]]
- 00bcbd4c bytes 313c0294
+ 00bcbde8 bytes 3e3c0294
- 00bcbd58 ["INT_ADD", "register:40f0:8", ["const:bcbd58:8", "const:4:8"]]
- 00bcbd58 ["CALL", null, ["callee:00c5ae20:8"]]
+ 00bcbdf4 ["INT_ADD", "register:40f0:8", ["const:bcbdf4:8", "const:4:8"]]
+ 00bcbdf4 ["CALL", null, ["callee:00c5ae20:8"]]
- 00bcbd58 bytes fe3b0294
+ 00bcbdf4 bytes 0b3c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ad1fb899e83589fd4886086248dfe2b"></a>

### [`00bcbdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbdac.md) → [`00bcbe48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbe48.md) FUN_00bcbe48

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bca790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca790.md) · 呼出先 2件 [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5da30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da30.md)
- 新版 呼出元 1件 [`00bca82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca82c.md) · 呼出先 2件 [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5db00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcbe60",
      "incomplete_value": false,
      "site": "00bcbe6c",
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
            "const:c0f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbdc4",
      "incomplete_value": false,
      "site": "00bcbdd0",
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
            "const:c5c:8"
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
      "00bcbe60",
      "PARAM",
      [
        "storage",
        "002a3c5c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcbe60",
      "PARAM",
      [
        "storage",
        "002a3c0f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbdac.md#insn-00bcbdd0) · [`00bcbdc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbdac.md#insn-00bcbdc4)
- 新版 [`00bcbe6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbe48.md#insn-00bcbe6c) · [`00bcbe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbe48.md#insn-00bcbe60)

~~~diff
- 00bcbdd0 ["INT_ADD", "register:40f0:8", ["const:bcbdd0:8", "const:4:8"]]
- 00bcbdd0 ["CALL", null, ["callee:00c5aeb0:8"]]
+ 00bcbe6c ["INT_ADD", "register:40f0:8", ["const:bcbe6c:8", "const:4:8"]]
+ 00bcbe6c ["CALL", null, ["callee:00c5aeb0:8"]]
- 00bcbdd0 bytes 043c0294
+ 00bcbe6c bytes 113c0294
- 00bcbdc4 ["COPY", "tmp:0:8", ["const:c5c:8"]]
- 00bcbdc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcbdc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcbdc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcbe60 ["COPY", "tmp:0:8", ["const:c0f:8"]]
+ 00bcbe60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcbe60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcbe60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcbdc4 bytes 00703191
+ 00bcbe60 bytes 003c3091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40690e2c0ae136ec2a903a23c9adb07c"></a>

### [`00bcbe24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbe24.md) → [`00bcbec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbec0.md) _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5daf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5daf0.md) · 呼出先 5件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)
- 新版 呼出元 1件 [`00c5dbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dbc0.md) · 呼出先 5件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 85.48% / 新版 85.48%

CFGの説明率　旧版 58.82% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbe54"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbe78"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbe7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcbe54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbfb0"
      ]
    ],
    [
      "unmatched:00bcbe7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbfa8"
      ]
    ],
    [
      "00bcbf28",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcbef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbfb0"
      ]
    ],
    [
      "00bcbf18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbfa8"
      ]
    ],
    [
      "00bcbf28",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbe54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbe24.md#insn-00bcbe54) · [`00bcbe78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbe24.md#insn-00bcbe78) · [`00bcbe7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbe24.md#insn-00bcbe7c)

~~~diff
- 00bcbe54 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bcbe54 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00bcbe54 bytes 090600b5
- 00bcbe78 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcbe78 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bcbe78 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bcbe78 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bcbe78 bytes 1931899a
- 00bcbe7c ["INT_EQUAL", "tmp:0:1", ["register:40c8:8", "const:0:8"]]
- 00bcbe7c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00bcbe7c bytes 990400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fcdcdad20e8d5a7e94bb2b851b78e21"></a>

### [`00bcbf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbf1c.md) → [`00bcbfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbfb8.md) _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5db10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db10.md) · 呼出先 5件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)
- 新版 呼出元 1件 [`00c5dbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dbe0.md) · 呼出先 5件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.03% / 新版 79.03%

CFGの説明率　旧版 26.32% / 新版 27.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbf2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbf2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcbfc8"
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
      "unmatched:00bcbf2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcbf64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc028"
      ]
    ],
    [
      "unmatched:00bcbf74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc0a0"
      ]
    ]
  ],
  "added": [
    [
      "00bcbfc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcc000",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc028"
      ]
    ],
    [
      "00bcc010",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc0a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbf2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbf1c.md#insn-00bcbf2c) · [`00bcbf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbf1c.md#insn-00bcbf64) · [`00bcbf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbf1c.md#insn-00bcbf70)

~~~diff
- 00bcbf2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcbf2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcbf2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bcbf2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcbf2c bytes fd7b04a9
- 00bcbf64 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcbf64 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bcbf64 bytes 43010054
- 00bcbf70 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcbf70 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bcbf70 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bcbf70 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bcbf70 bytes 1931899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e955102fb484aecc56ec4fdfff18162"></a>

### [`00bcc014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc014.md) → [`00bcc0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc0b0.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5dad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dad0.md) · 呼出先 5件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)
- 新版 呼出元 1件 [`00c5dba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dba0.md) · 呼出先 5件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc118",
      "incomplete_value": false,
      "site": "00bcc11c",
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
            "const:61f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc07c",
      "incomplete_value": false,
      "site": "00bcc080",
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
            "const:67b:8"
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
      "00bcc118",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc118",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc014.md#insn-00bcc080) · [`00bcc07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc014.md#insn-00bcc07c) · [`00bcc08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc014.md#insn-00bcc08c)
- 新版 [`00bcc11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc0b0.md#insn-00bcc11c) · [`00bcc118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc0b0.md#insn-00bcc118) · [`00bcc128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc0b0.md#insn-00bcc128)

~~~diff
- 00bcc080 ["INT_ADD", "register:40f0:8", ["const:bcc080:8", "const:4:8"]]
- 00bcc080 ["CALL", null, ["callee:00b4035c:8"]]
+ 00bcc11c ["INT_ADD", "register:40f0:8", ["const:bcc11c:8", "const:4:8"]]
+ 00bcc11c ["CALL", null, ["callee:00b4035c:8"]]
- 00bcc080 bytes 90d0fd97
+ 00bcc11c bytes 90d0fd97
- 00bcc07c ["COPY", "tmp:0:8", ["const:67b:8"]]
- 00bcc07c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc07c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc07c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcc118 ["COPY", "tmp:0:8", ["const:61f:8"]]
+ 00bcc118 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc118 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc118 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcc07c bytes 00ec1991
+ 00bcc118 bytes 007c1891
- 00bcc08c ["INT_ADD", "register:40f0:8", ["const:bcc08c:8", "const:4:8"]]
- 00bcc08c ["CALL", null, ["callee:00c57f60:8"]]
+ 00bcc128 ["INT_ADD", "register:40f0:8", ["const:bcc128:8", "const:4:8"]]
+ 00bcc128 ["CALL", null, ["callee:00c57f60:8"]]
- 00bcc08c bytes 812f0294
+ 00bcc128 bytes 8e2f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fe122b5ae6fc7c2d6ec5dbbf74a26b7"></a>

### [`00bcc10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc10c.md) → [`00bcc1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc1a8.md) _INIT_290

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bca4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4d0.md) [`00bca4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4d8.md) [`00bca4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4dc.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bca56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca56c.md) [`00bca574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca574.md) [`00bca578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca578.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 75.68% / 新版 75.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 4件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc1d4",
      "incomplete_value": false,
      "site": "00bcc1d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc138",
      "incomplete_value": false,
      "site": "00bcc138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcc1d4",
      "incomplete_value": false,
      "site": "00bcc1d4",
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
            "const:b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc138",
      "incomplete_value": false,
      "site": "00bcc138",
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
            "const:10a:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc1d4",
      "incomplete_value": false,
      "site": "00bcc1d4",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:7e8:8"
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
      "definition_site": "00bcc138",
      "incomplete_value": false,
      "site": "00bcc138",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:6e8:8"
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
      "00bcc1c4",
      "PARAM",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc1d4",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc1d4",
      "DATA",
      [
        "storage",
        "002bc10a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcc1c4",
      "PARAM",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc1d4",
      "WRITE",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc1d4",
      "DATA",
      [
        "storage",
        "002bc0b6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc10c.md#insn-00bcc144) · [`00bcc170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc10c.md#insn-00bcc170) · [`00bcc128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc10c.md#insn-00bcc128)
- 新版 [`00bcc1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc1a8.md#insn-00bcc1e0) · [`00bcc20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc1a8.md#insn-00bcc20c) · [`00bcc1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc1a8.md#insn-00bcc1c4)

~~~diff
- 00bcc144 ["INT_ADD", "register:40f0:8", ["const:bcc144:8", "const:4:8"]]
- 00bcc144 ["CALL", null, ["callee:00c5ac90:8"]]
+ 00bcc1e0 ["INT_ADD", "register:40f0:8", ["const:bcc1e0:8", "const:4:8"]]
+ 00bcc1e0 ["CALL", null, ["callee:00c5ac90:8"]]
- 00bcc144 bytes 9f3a0294
+ 00bcc1e0 bytes ac3a0294
- 00bcc170 ["INT_ADD", "register:40f0:8", ["const:bcc170:8", "const:4:8"]]
- 00bcc170 ["CALL", null, ["callee:00c57f00:8"]]
+ 00bcc20c ["INT_ADD", "register:40f0:8", ["const:bcc20c:8", "const:4:8"]]
+ 00bcc20c ["CALL", null, ["callee:00c57f00:8"]]
- 00bcc170 bytes 302f0294
+ 00bcc20c bytes 3d2f0294
- 00bcc128 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 00bcc128 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc128 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc128 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcc1c4 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00bcc1c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc1c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc1c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcc128 bytes 00a01b91
+ 00bcc1c4 bytes 00a01f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2410c79461db2f922a1a81e3430e6f83"></a>

### [`00bcc30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc30c.md) → [`00bcc3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc3a8.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

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
      "definition_site": "00bcc3d4",
      "incomplete_value": true,
      "site": "00bcc3d4",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc338",
      "incomplete_value": true,
      "site": "00bcc338",
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
            "const:728:8"
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
      "definition_site": "00bcc3bc",
      "incomplete_value": true,
      "site": "00bcc3bc",
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
      "definition_site": "00bcc320",
      "incomplete_value": true,
      "site": "00bcc320",
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
      "definition_site": "00bcc3c8",
      "incomplete_value": false,
      "site": "00bcc3cc",
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
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc32c",
      "incomplete_value": false,
      "site": "00bcc330",
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
            "const:23c:8"
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
      "00bcc3b8",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc3c8",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      "00bcc3d4",
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc3b8",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc3c8",
      "PARAM",
      [
        "storage",
        "002ac1e0",
        null,
        "string"
      ]
    ],
    [
      "00bcc3d4",
      "WRITE",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc30c.md#insn-00bcc330) · [`00bcc338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc30c.md#insn-00bcc338) · [`00bcc31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc30c.md#insn-00bcc31c)
- 新版 [`00bcc3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc3a8.md#insn-00bcc3cc) · [`00bcc3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc3a8.md#insn-00bcc3d4) · [`00bcc3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc3a8.md#insn-00bcc3b8)

~~~diff
- 00bcc330 ["INT_ADD", "register:40f0:8", ["const:bcc330:8", "const:4:8"]]
- 00bcc330 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bcc3cc ["INT_ADD", "register:40f0:8", ["const:bcc3cc:8", "const:4:8"]]
+ 00bcc3cc ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcc330 bytes f83a0294
+ 00bcc3cc bytes 053b0294
- 00bcc338 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00bcc338 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc3d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00bcc3d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc338 bytes 609603f9
+ 00bcc3d4 bytes 601604f9
- 00bcc31c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00bcc31c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcc3b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00bcc3b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcc31c bytes 689643f9
+ 00bcc3b8 bytes 681644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d659a409fa88abdd23b506355cb6dcb"></a>

### [`00bcc34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc34c.md) → [`00bcc3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc3e8.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bcc378"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc414"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc3fc",
      "incomplete_value": true,
      "site": "00bcc3fc",
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
      "definition_site": "00bcc360",
      "incomplete_value": true,
      "site": "00bcc360",
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
      "00bcc3f8",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc368",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcc370",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00bcc3f8",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc404",
      "PARAM",
      [
        "storage",
        "002ac1e0",
        null,
        "string"
      ]
    ],
    [
      "00bcc40c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc34c.md#insn-00bcc360) · [`00bcc370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc34c.md#insn-00bcc370) · [`00bcc378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc34c.md#insn-00bcc378)
- 新版 [`00bcc3fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc3e8.md#insn-00bcc3fc)

~~~diff
- 00bcc360 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcc360 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcc3fc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcc3fc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc360 bytes e80000b5
+ 00bcc3fc bytes e80000b5
- 00bcc370 ["INT_ADD", "register:40f0:8", ["const:bcc370:8", "const:4:8"]]
- 00bcc370 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcc370 bytes e83a0294
- 00bcc378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00bcc378 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc378 bytes 609603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79b88080fe107a5812ed688f4b053179"></a>

### [`00bcc38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc38c.md) → [`00bcc428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc428.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bcc38c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc390"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc38c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc390",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcc438",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc428",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcc42c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcc438",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc38c.md#insn-00bcc38c) · [`00bcc390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc38c.md#insn-00bcc390) · [`00bcc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc38c.md#insn-00bcc3a0)
- 新版 [`00bcc43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc428.md#insn-00bcc43c)

~~~diff
- 00bcc38c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bcc38c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bcc38c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc38c bytes f30f1ef8
- 00bcc390 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc390 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc390 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcc390 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc390 bytes fd7b01a9
- 00bcc3a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcc3a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bcc43c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcc43c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcc3a0 bytes 080100b5
+ 00bcc43c bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eabc465a0275c625b930dda45b1e139"></a>

### [`00bcc3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc3d0.md) → [`00bcc46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc46c.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 33.33% / 新版 25.00%

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
      "site": "00bcc400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc49c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc480",
      "incomplete_value": true,
      "site": "00bcc480",
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
      "definition_site": "00bcc3e4",
      "incomplete_value": true,
      "site": "00bcc3e4",
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
      "00bcc47c",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc3ec",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcc400",
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc47c",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc488",
      "PARAM",
      [
        "storage",
        "002ac1e0",
        null,
        "string"
      ]
    ],
    [
      "00bcc49c",
      "WRITE",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc3d0.md#insn-00bcc3e4) · [`00bcc3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc3d0.md#insn-00bcc3f8) · [`00bcc400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc3d0.md#insn-00bcc400)
- 新版 [`00bcc480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc46c.md#insn-00bcc480) · [`00bcc494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc46c.md#insn-00bcc494)

~~~diff
- 00bcc3e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcc3e4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcc480 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcc480 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc3e4 bytes 080100b5
+ 00bcc480 bytes 080100b5
- 00bcc3f8 ["INT_ADD", "register:40f0:8", ["const:bcc3f8:8", "const:4:8"]]
- 00bcc3f8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bcc494 ["INT_ADD", "register:40f0:8", ["const:bcc494:8", "const:4:8"]]
+ 00bcc494 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcc3f8 bytes c63a0294
+ 00bcc494 bytes d33a0294
- 00bcc400 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00bcc400 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc400 bytes 609603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c5c3418e91e1cfa93d27ed20f4a58a3"></a>

### [`00bcc420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc420.md) → [`00bcc4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc4bc.md) _ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bcc514",
      "incomplete_value": true,
      "site": "00bcc514",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc478",
      "incomplete_value": true,
      "site": "00bcc478",
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
            "const:730:8"
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
      "definition_site": "00bcc4f0",
      "incomplete_value": true,
      "site": "00bcc4fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:828:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc454",
      "incomplete_value": true,
      "site": "00bcc460",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:728:8"
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
      "00bcc4d0",
      "READ",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc4f0",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc514",
      "WRITE",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc4d0",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc4f0",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc514",
      "WRITE",
      [
        "storage",
        "01126830",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc420.md#insn-00bcc460) · [`00bcc478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc420.md#insn-00bcc478) · [`00bcc434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc420.md#insn-00bcc434)
- 新版 [`00bcc4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc4bc.md#insn-00bcc4fc) · [`00bcc514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc4bc.md#insn-00bcc514) · [`00bcc4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc4bc.md#insn-00bcc4d0)

~~~diff
- 00bcc460 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc460 ["INT_ADD", "register:40f0:8", ["const:bcc460:8", "const:4:8"]]
- 00bcc460 ["CALLIND", null, ["register:0:8"]]
+ 00bcc4fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc4fc ["INT_ADD", "register:40f0:8", ["const:bcc4fc:8", "const:4:8"]]
+ 00bcc4fc ["CALLIND", null, ["register:0:8"]]
- 00bcc460 bytes 00013fd6
+ 00bcc4fc bytes 00013fd6
- 00bcc478 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bcc478 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:730:8"]]
- 00bcc478 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bcc514 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bcc514 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:830:8"]]
+ 00bcc514 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bcc478 bytes a0c21c39
+ 00bcc514 bytes a0c22039
- 00bcc434 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:730:8"]]
- 00bcc434 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bcc434 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bcc4d0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:830:8"]]
+ 00bcc4d0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bcc4d0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bcc434 bytes a8c25c39
+ 00bcc4d0 bytes a8c26039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5024e686b11b385daee5f937514b59e"></a>

### [`00bcc48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc48c.md) → [`00bcc528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc528.md) _ZN8firebase4auth4auth12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 33.33% / 新版 28.57%

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
      "site": "00bcc4c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc4e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc564"
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
      "00bcc53c",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc548",
      "READ",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcc4cc"
      ]
    ]
  ],
  "added": [
    [
      "00bcc53c",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc548",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc568"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc48c.md#insn-00bcc4a4) · [`00bcc4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc48c.md#insn-00bcc4c8) · [`00bcc4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc48c.md#insn-00bcc4d0)
- 新版 [`00bcc540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc528.md#insn-00bcc540)

~~~diff
- 00bcc4a4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc4a4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bcc540 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bcc540 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bcc4a4 bytes 410200b4
+ 00bcc540 bytes 410200b4
- 00bcc4c8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bcc4c8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bcc4c8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:730:8"]]
- 00bcc4c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bcc4c8 bytes bfc21c39
- 00bcc4d0 ["INT_ADD", "register:40f0:8", ["const:bcc4d0:8", "const:4:8"]]
- 00bcc4d0 ["CALL", null, ["callee:00c5b030:8"]]
- 00bcc4d0 bytes a43a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb2d2ba80165a442373e38c22f39fb68"></a>

### [`00bcc4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc4fc.md) → [`00bcc598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc598.md) _ZN8firebase4auth4auth14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "site": "00bcc4fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc4fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc500"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc4fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc500",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc510",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc598",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcc59c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcc5ac",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc4fc.md#insn-00bcc4fc) · [`00bcc500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc4fc.md#insn-00bcc500) · [`00bcc518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc4fc.md#insn-00bcc518)

~~~diff
- 00bcc4fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcc4fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcc4fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bcc4fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc4fc bytes f44fbea9
- 00bcc500 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc500 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc500 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcc500 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc500 bytes fd7b01a9
- 00bcc518 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc518 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc518 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-074c414892c7ca4979c37e84eeca9702"></a>

### [`00bcc5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc5a8.md) → [`00bcc644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc644.md) _ZN8firebase4auth4auth13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bcc5e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc684"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc5c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc5bc",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc5c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc688"
      ]
    ],
    [
      "unmatched:00bcc5cc",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc658",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc660",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc688"
      ]
    ],
    [
      "00bcc668",
      "PARAM",
      [
        "storage",
        "002ac1e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc5a8.md#insn-00bcc5c4) · [`00bcc5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc5a8.md#insn-00bcc5e0) · [`00bcc5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc5a8.md#insn-00bcc5e8)
- 新版 [`00bcc67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc644.md#insn-00bcc67c)

~~~diff
- 00bcc5c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc5c4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc5c4 bytes 410100b5
- 00bcc5e0 ["INT_ADD", "register:40f0:8", ["const:bcc5e0:8", "const:4:8"]]
- 00bcc5e0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bcc67c ["INT_ADD", "register:40f0:8", ["const:bcc67c:8", "const:4:8"]]
+ 00bcc67c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcc5e0 bytes 4c3a0294
+ 00bcc67c bytes 593a0294
- 00bcc5e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00bcc5e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc5e8 bytes 809603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c89363102f526b1a994c38c12ea323fc"></a>

### [`00bcc618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc618.md) → [`00bcc6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc6b4.md) _ZN8firebase4auth4auth10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bcc6d0",
      "incomplete_value": false,
      "site": "00bcc6d4",
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
      "definition_site": "00bcc634",
      "incomplete_value": false,
      "site": "00bcc638",
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
      "definition_site": "00bcc6e0",
      "incomplete_value": true,
      "site": "00bcc6ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bcc644",
      "incomplete_value": true,
      "site": "00bcc650",
      "value": [
        "LOAD",
        "8",
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
      "00bcc6d0",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bcc6e0",
      "DATA",
      [
        "storage",
        "011267c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcc6d0",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bcc6e0",
      "DATA",
      [
        "storage",
        "011268c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc618.md#insn-00bcc638) · [`00bcc634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc618.md#insn-00bcc634) · [`00bcc640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc618.md#insn-00bcc640)
- 新版 [`00bcc6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc6b4.md#insn-00bcc6d4) · [`00bcc6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc6b4.md#insn-00bcc6d0) · [`00bcc6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc6b4.md#insn-00bcc6dc)

~~~diff
- 00bcc638 ["INT_ADD", "register:40f0:8", ["const:bcc638:8", "const:4:8"]]
- 00bcc638 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bcc6d4 ["INT_ADD", "register:40f0:8", ["const:bcc6d4:8", "const:4:8"]]
+ 00bcc6d4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bcc638 bytes 723a0294
+ 00bcc6d4 bytes 7f3a0294
- 00bcc634 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bcc634 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc634 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc634 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcc6d0 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bcc6d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc6d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc6d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcc634 bytes 00781491
+ 00bcc6d0 bytes 00341591
- 00bcc640 ["COPY", "tmp:0:8", ["const:7c8:8"]]
- 00bcc640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcc6dc ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 00bcc6dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc6dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc6dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcc640 bytes 08211f91
+ 00bcc6dc bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b1aa85c650f75bc38251378440015af"></a>

### [`00bcc654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc654.md) → [`00bcc6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc6f0.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00bcc71c",
      "incomplete_value": true,
      "site": "00bcc71c",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc680",
      "incomplete_value": true,
      "site": "00bcc680",
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
            "const:7d0:8"
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
      "definition_site": "00bcc704",
      "incomplete_value": true,
      "site": "00bcc704",
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
      "definition_site": "00bcc668",
      "incomplete_value": true,
      "site": "00bcc668",
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
      "definition_site": "00bcc710",
      "incomplete_value": false,
      "site": "00bcc714",
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
            "const:c75:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc674",
      "incomplete_value": false,
      "site": "00bcc678",
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
            "const:cc2:8"
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
      "00bcc700",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc710",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      "00bcc71c",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc700",
      "READ",
      [
        "storage",
        "011268d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc710",
      "PARAM",
      [
        "storage",
        "002a2c75",
        null,
        "string"
      ]
    ],
    [
      "00bcc71c",
      "WRITE",
      [
        "storage",
        "011268d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc654.md#insn-00bcc678) · [`00bcc680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc654.md#insn-00bcc680) · [`00bcc664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc654.md#insn-00bcc664)
- 新版 [`00bcc714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc6f0.md#insn-00bcc714) · [`00bcc71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc6f0.md#insn-00bcc71c) · [`00bcc700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc6f0.md#insn-00bcc700)

~~~diff
- 00bcc678 ["INT_ADD", "register:40f0:8", ["const:bcc678:8", "const:4:8"]]
- 00bcc678 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bcc714 ["INT_ADD", "register:40f0:8", ["const:bcc714:8", "const:4:8"]]
+ 00bcc714 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcc678 bytes 263a0294
+ 00bcc714 bytes 333a0294
- 00bcc680 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bcc680 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc71c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
+ 00bcc71c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc680 bytes 60ea03f9
+ 00bcc71c bytes 606a04f9
- 00bcc664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bcc664 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcc700 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
+ 00bcc700 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcc664 bytes 68ea43f9
+ 00bcc700 bytes 686a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-918124324554821070bb30184b1bd4c6"></a>

### [`00bcc694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc694.md) → [`00bcc730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc730.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00bcc75c",
      "incomplete_value": true,
      "site": "00bcc75c",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc6c0",
      "incomplete_value": true,
      "site": "00bcc6c0",
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
            "const:7d0:8"
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
      "definition_site": "00bcc744",
      "incomplete_value": true,
      "site": "00bcc744",
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
      "definition_site": "00bcc6a8",
      "incomplete_value": true,
      "site": "00bcc6a8",
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
      "definition_site": "00bcc74c",
      "incomplete_value": false,
      "site": "00bcc754",
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
            "const:c75:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc6b0",
      "incomplete_value": false,
      "site": "00bcc6b8",
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
            "const:cc2:8"
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
      "00bcc740",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc74c",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      "00bcc75c",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc740",
      "READ",
      [
        "storage",
        "011268d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc74c",
      "PARAM",
      [
        "storage",
        "002a2c75",
        null,
        "string"
      ]
    ],
    [
      "00bcc75c",
      "WRITE",
      [
        "storage",
        "011268d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc694.md#insn-00bcc6b8) · [`00bcc6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc694.md#insn-00bcc6c0) · [`00bcc6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc694.md#insn-00bcc6a4)
- 新版 [`00bcc754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc730.md#insn-00bcc754) · [`00bcc75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc730.md#insn-00bcc75c) · [`00bcc740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc730.md#insn-00bcc740)

~~~diff
- 00bcc6b8 ["INT_ADD", "register:40f0:8", ["const:bcc6b8:8", "const:4:8"]]
- 00bcc6b8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bcc754 ["INT_ADD", "register:40f0:8", ["const:bcc754:8", "const:4:8"]]
+ 00bcc754 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcc6b8 bytes 163a0294
+ 00bcc754 bytes 233a0294
- 00bcc6c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bcc6c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc75c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
+ 00bcc75c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc6c0 bytes 60ea03f9
+ 00bcc75c bytes 606a04f9
- 00bcc6a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bcc6a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcc740 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
+ 00bcc740 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcc6a4 bytes 68ea43f9
+ 00bcc740 bytes 686a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-125900338fc3f1edc813f9a83dec68cc"></a>

### [`00bcc6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc6d4.md) → [`00bcc770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc770.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bcc704"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc7a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc784",
      "incomplete_value": true,
      "site": "00bcc784",
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
      "definition_site": "00bcc6e8",
      "incomplete_value": true,
      "site": "00bcc6e8",
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
      "00bcc780",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc784",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcc708"
      ]
    ],
    [
      "unmatched:00bcc6f4",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc780",
      "READ",
      [
        "storage",
        "011268d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc784",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc7a4"
      ]
    ],
    [
      "00bcc790",
      "PARAM",
      [
        "storage",
        "002a2c75",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc6d4.md#insn-00bcc6fc) · [`00bcc704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc6d4.md#insn-00bcc704) · [`00bcc714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc6d4.md#insn-00bcc714)

~~~diff
- 00bcc6fc ["INT_ADD", "register:40f0:8", ["const:bcc6fc:8", "const:4:8"]]
- 00bcc6fc ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcc6fc bytes 053a0294
- 00bcc704 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bcc704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc704 bytes 60ea03f9
- 00bcc714 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcc714 ["RETURN", null, ["register:0:8"]]
- 00bcc714 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f68e20cd299f1a593464aedf5adfac05"></a>

### [`00bcc718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc718.md) → [`00bcc7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc7b4.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bcc748"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc7e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc7c8",
      "incomplete_value": true,
      "site": "00bcc7c8",
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
      "definition_site": "00bcc72c",
      "incomplete_value": true,
      "site": "00bcc72c",
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
      "00bcc7c4",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc734",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcc748",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc7c4",
      "READ",
      [
        "storage",
        "011268d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc7d0",
      "PARAM",
      [
        "storage",
        "002a2c75",
        null,
        "string"
      ]
    ],
    [
      "00bcc7e4",
      "WRITE",
      [
        "storage",
        "011268d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc718.md#insn-00bcc72c) · [`00bcc740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc718.md#insn-00bcc740) · [`00bcc748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc718.md#insn-00bcc748)
- 新版 [`00bcc7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc7b4.md#insn-00bcc7c8) · [`00bcc7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc7b4.md#insn-00bcc7dc)

~~~diff
- 00bcc72c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcc72c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bcc7c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcc7c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcc72c bytes 080100b5
+ 00bcc7c8 bytes 080100b5
- 00bcc740 ["INT_ADD", "register:40f0:8", ["const:bcc740:8", "const:4:8"]]
- 00bcc740 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bcc7dc ["INT_ADD", "register:40f0:8", ["const:bcc7dc:8", "const:4:8"]]
+ 00bcc7dc ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcc740 bytes f4390294
+ 00bcc7dc bytes 013a0294
- 00bcc748 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00bcc748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc748 bytes 60ea03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2db6d98c41042c389faceaaaa0734e3"></a>

### [`00bcc768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc768.md) → [`00bcc804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc804.md) _ZN8firebase4auth17signinmethodquery15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc85c",
      "incomplete_value": true,
      "site": "00bcc85c",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc7c0",
      "incomplete_value": true,
      "site": "00bcc7c0",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc7a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bcc844"
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
      "00bcc818",
      "READ",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bcc79c",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc85c",
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc818",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc838",
      "READ",
      [
        "storage",
        "011268d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc85c",
      "WRITE",
      [
        "storage",
        "011268d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc768.md#insn-00bcc7a8) · [`00bcc7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc768.md#insn-00bcc7c0)
- 新版 [`00bcc85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc804.md#insn-00bcc85c) · [`00bcc844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc804.md#insn-00bcc844)

~~~diff
- 00bcc7a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc7a8 ["INT_ADD", "register:40f0:8", ["const:bcc7a8:8", "const:4:8"]]
- 00bcc7a8 ["CALLIND", null, ["register:0:8"]]
- 00bcc7a8 bytes 00013fd6
- 00bcc7c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bcc7c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7d8:8"]]
- 00bcc7c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bcc85c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bcc85c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8d8:8"]]
+ 00bcc85c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bcc7c0 bytes a0621f39
+ 00bcc85c bytes a0622339
+ 00bcc844 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc844 ["INT_ADD", "register:40f0:8", ["const:bcc844:8", "const:4:8"]]
+ 00bcc844 ["CALLIND", null, ["register:0:8"]]
+ 00bcc844 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-218dfe398cd44495cab70b8cde1ae55a"></a>

### [`00bcc7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc7d4.md) → [`00bcc870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc870.md) _ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bcc8ac",
      "incomplete_value": true,
      "site": "00bcc8ac",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc810",
      "incomplete_value": true,
      "site": "00bcc810",
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
            "const:7d8:8"
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
      "definition_site": "00bcc8cc",
      "incomplete_value": true,
      "site": "00bcc8cc",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc830",
      "incomplete_value": true,
      "site": "00bcc830",
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
            "const:7d0:8"
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
      "definition_site": "00bcc888",
      "incomplete_value": true,
      "site": "00bcc888",
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
      "definition_site": "00bcc7ec",
      "incomplete_value": true,
      "site": "00bcc7ec",
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
      "00bcc884",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc890",
      "READ",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc8ac",
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc884",
      "READ",
      [
        "storage",
        "011268d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc890",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc8ac",
      "WRITE",
      [
        "storage",
        "011268d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc7d4.md#insn-00bcc810) · [`00bcc82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc7d4.md#insn-00bcc82c) · [`00bcc830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc7d4.md#insn-00bcc830)
- 新版 [`00bcc8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc870.md#insn-00bcc8ac) · [`00bcc8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc870.md#insn-00bcc8c8) · [`00bcc8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc870.md#insn-00bcc8cc)

~~~diff
- 00bcc810 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bcc810 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bcc810 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7d8:8"]]
- 00bcc810 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bcc8ac ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bcc8ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bcc8ac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8d8:8"]]
+ 00bcc8ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bcc810 bytes bf621f39
+ 00bcc8ac bytes bf622339
- 00bcc82c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc82c ["INT_ADD", "register:40f0:8", ["const:bcc82c:8", "const:4:8"]]
- 00bcc82c ["CALLIND", null, ["register:0:8"]]
+ 00bcc8c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc8c8 ["INT_ADD", "register:40f0:8", ["const:bcc8c8:8", "const:4:8"]]
+ 00bcc8c8 ["CALLIND", null, ["register:0:8"]]
- 00bcc82c bytes 00013fd6
+ 00bcc8c8 bytes 00013fd6
- 00bcc830 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00bcc830 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bcc830 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bcc8cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
+ 00bcc8cc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bcc8cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bcc830 bytes 9fea03f9
+ 00bcc8cc bytes 9f6a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6717c6f7e2932216f73eab37573fb8b"></a>

### [`00bcc844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc844.md) → [`00bcc8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc8e0.md) _ZN8firebase4auth17signinmethodquery14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bcc884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc920"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc860"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc858",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc860",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc924"
      ]
    ],
    [
      "unmatched:00bcc868",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc8f4",
      "READ",
      [
        "storage",
        "011268d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc8fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc924"
      ]
    ],
    [
      "00bcc904",
      "PARAM",
      [
        "storage",
        "002a2c75",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc844.md#insn-00bcc860) · [`00bcc87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc844.md#insn-00bcc87c) · [`00bcc884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc844.md#insn-00bcc884)
- 新版 [`00bcc918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc8e0.md#insn-00bcc918)

~~~diff
- 00bcc860 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc860 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcc860 bytes 410100b5
- 00bcc87c ["INT_ADD", "register:40f0:8", ["const:bcc87c:8", "const:4:8"]]
- 00bcc87c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bcc918 ["INT_ADD", "register:40f0:8", ["const:bcc918:8", "const:4:8"]]
+ 00bcc918 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcc87c bytes a5390294
+ 00bcc918 bytes b2390294
- 00bcc884 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00bcc884 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc884 bytes 80ea03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-270a6b9336802cdd786e1c1671ea76b2"></a>

### [`00bcc8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8b4.md) → [`00bcc950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc950.md) _ZN8firebase4auth17signinmethodquery11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bcc96c",
      "incomplete_value": false,
      "site": "00bcc970",
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
      "definition_site": "00bcc8d0",
      "incomplete_value": false,
      "site": "00bcc8d4",
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
      "definition_site": "00bcc97c",
      "incomplete_value": true,
      "site": "00bcc988",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bcc8e0",
      "incomplete_value": true,
      "site": "00bcc8ec",
      "value": [
        "LOAD",
        "8",
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
      "00bcc96c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bcc97c",
      "DATA",
      [
        "storage",
        "011267e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc96c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bcc97c",
      "DATA",
      [
        "storage",
        "011268e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8b4.md#insn-00bcc8d4) · [`00bcc8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8b4.md#insn-00bcc8d0) · [`00bcc8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8b4.md#insn-00bcc8dc)
- 新版 [`00bcc970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc950.md#insn-00bcc970) · [`00bcc96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc950.md#insn-00bcc96c) · [`00bcc978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc950.md#insn-00bcc978)

~~~diff
- 00bcc8d4 ["INT_ADD", "register:40f0:8", ["const:bcc8d4:8", "const:4:8"]]
- 00bcc8d4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bcc970 ["INT_ADD", "register:40f0:8", ["const:bcc970:8", "const:4:8"]]
+ 00bcc970 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bcc8d4 bytes cb390294
+ 00bcc970 bytes d8390294
- 00bcc8d0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bcc8d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc8d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc8d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcc96c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bcc96c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc96c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc96c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcc8d0 bytes 009c0d91
+ 00bcc96c bytes 002c0c91
- 00bcc8dc ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00bcc8dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc8dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc8dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcc978 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 00bcc978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcc8dc bytes 08811f91
+ 00bcc978 bytes 08812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c951e3088ef10b85c9b08ca3c9ce99ea"></a>

### [`00bcc8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8f0.md) → [`00bcc98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc98c.md) _ZN8firebase4auth17signinmethodquery13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bcc930"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc9cc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc90c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc904",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc90c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc9d0"
      ]
    ],
    [
      "unmatched:00bcc914",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc9a0",
      "READ",
      [
        "storage",
        "011268d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc9a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc9d0"
      ]
    ],
    [
      "00bcc9b0",
      "PARAM",
      [
        "storage",
        "002a2c75",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8f0.md#insn-00bcc90c) · [`00bcc928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8f0.md#insn-00bcc928) · [`00bcc930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8f0.md#insn-00bcc930)
- 新版 [`00bcc9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc98c.md#insn-00bcc9c4)

~~~diff
- 00bcc90c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc90c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcc90c bytes 410100b5
- 00bcc928 ["INT_ADD", "register:40f0:8", ["const:bcc928:8", "const:4:8"]]
- 00bcc928 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bcc9c4 ["INT_ADD", "register:40f0:8", ["const:bcc9c4:8", "const:4:8"]]
+ 00bcc9c4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcc928 bytes 7a390294
+ 00bcc9c4 bytes 87390294
- 00bcc930 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00bcc930 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc930 bytes 80ea03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-564432103861caa3313a51dc0f3e388a"></a>

### [`00bcc99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc99c.md) → [`00bcca38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcca38.md) _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bcca64",
      "incomplete_value": true,
      "site": "00bcca64",
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
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc9c8",
      "incomplete_value": true,
      "site": "00bcc9c8",
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
            "const:7f0:8"
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
      "definition_site": "00bcca4c",
      "incomplete_value": true,
      "site": "00bcca4c",
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
      "definition_site": "00bcc9b0",
      "incomplete_value": true,
      "site": "00bcc9b0",
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
      "definition_site": "00bcca58",
      "incomplete_value": false,
      "site": "00bcca5c",
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
            "const:c1a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc9bc",
      "incomplete_value": false,
      "site": "00bcc9c0",
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
            "const:bda:8"
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
      "00bcca48",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcca58",
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ],
    [
      "00bcca64",
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcca48",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcca58",
      "PARAM",
      [
        "storage",
        "002b5c1a",
        null,
        "string"
      ]
    ],
    [
      "00bcca64",
      "WRITE",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc99c.md#insn-00bcc9c0) · [`00bcc9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc99c.md#insn-00bcc9c8) · [`00bcc9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc99c.md#insn-00bcc9ac)
- 新版 [`00bcca5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcca38.md#insn-00bcca5c) · [`00bcca64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcca38.md#insn-00bcca64) · [`00bcca48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcca38.md#insn-00bcca48)

~~~diff
- 00bcc9c0 ["INT_ADD", "register:40f0:8", ["const:bcc9c0:8", "const:4:8"]]
- 00bcc9c0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bcca5c ["INT_ADD", "register:40f0:8", ["const:bcca5c:8", "const:4:8"]]
+ 00bcca5c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcc9c0 bytes 54390294
+ 00bcca5c bytes 61390294
- 00bcc9c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
- 00bcc9c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcca64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00bcca64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc9c8 bytes 60fa03f9
+ 00bcca64 bytes 607a04f9
- 00bcc9ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
- 00bcc9ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcca48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00bcca48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcc9ac bytes 68fa43f9
+ 00bcca48 bytes 687a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8199fd0a8cede92b874923581e9cd8a0"></a>

### [`00bcc9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc9dc.md) → [`00bcca78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcca78.md) _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.75% / 新版 43.75%

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
      "site": "00bcca08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccaa4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcca8c",
      "incomplete_value": true,
      "site": "00bcca8c",
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
      "definition_site": "00bcc9f0",
      "incomplete_value": true,
      "site": "00bcc9f0",
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
      "00bcca88",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcca8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcca0c"
      ]
    ],
    [
      "unmatched:00bcc9f8",
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcca88",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcca8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccaa8"
      ]
    ],
    [
      "00bcca94",
      "PARAM",
      [
        "storage",
        "002b5c1a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc9dc.md#insn-00bcc9f0) · [`00bcca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc9dc.md#insn-00bcca00) · [`00bcca08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc9dc.md#insn-00bcca08)
- 新版 [`00bcca8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcca78.md#insn-00bcca8c)

~~~diff
- 00bcc9f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcc9f0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcca8c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcca8c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc9f0 bytes e80000b5
+ 00bcca8c bytes e80000b5
- 00bcca00 ["INT_ADD", "register:40f0:8", ["const:bcca00:8", "const:4:8"]]
- 00bcca00 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcca00 bytes 44390294
- 00bcca08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
- 00bcca08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcca08 bytes 60fa03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddcc870def1bf538414c8f5b2a32f01d"></a>

### [`00bcca1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca1c.md) → [`00bccab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccab8.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bcca1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcca20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcca20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcca1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcca20",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bccac8",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bccab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bccabc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bccac8",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcca1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca1c.md#insn-00bcca1c) · [`00bcca20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca1c.md#insn-00bcca20) · [`00bcca30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca1c.md#insn-00bcca30)
- 新版 [`00bccacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccab8.md#insn-00bccacc)

~~~diff
- 00bcca1c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bcca1c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bcca1c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcca1c bytes f30f1ef8
- 00bcca20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcca20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcca20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcca20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcca20 bytes fd7b01a9
- 00bcca30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcca30 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bccacc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bccacc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcca30 bytes 080100b5
+ 00bccacc bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a31af082cb838f9657b9b516c1176b3"></a>

### [`00bcca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca60.md) → [`00bccafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccafc.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bccb2c",
      "incomplete_value": true,
      "site": "00bccb2c",
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
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcca90",
      "incomplete_value": true,
      "site": "00bcca90",
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
            "const:7f0:8"
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
      "definition_site": "00bccb10",
      "incomplete_value": true,
      "site": "00bccb10",
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
      "definition_site": "00bcca74",
      "incomplete_value": true,
      "site": "00bcca74",
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
      "definition_site": "00bccb18",
      "incomplete_value": false,
      "site": "00bccb24",
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
            "const:c1a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcca7c",
      "incomplete_value": false,
      "site": "00bcca88",
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
            "const:bda:8"
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
      "00bccb0c",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccb18",
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ],
    [
      "00bccb2c",
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bccb0c",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccb18",
      "PARAM",
      [
        "storage",
        "002b5c1a",
        null,
        "string"
      ]
    ],
    [
      "00bccb2c",
      "WRITE",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcca88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca60.md#insn-00bcca88) · [`00bcca90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca60.md#insn-00bcca90) · [`00bcca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca60.md#insn-00bcca70)
- 新版 [`00bccb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccafc.md#insn-00bccb24) · [`00bccb2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccafc.md#insn-00bccb2c) · [`00bccb0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccafc.md#insn-00bccb0c)

~~~diff
- 00bcca88 ["INT_ADD", "register:40f0:8", ["const:bcca88:8", "const:4:8"]]
- 00bcca88 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bccb24 ["INT_ADD", "register:40f0:8", ["const:bccb24:8", "const:4:8"]]
+ 00bccb24 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcca88 bytes 22390294
+ 00bccb24 bytes 2f390294
- 00bcca90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
- 00bcca90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bccb2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00bccb2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcca90 bytes 60fa03f9
+ 00bccb2c bytes 607a04f9
- 00bcca70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
- 00bcca70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bccb0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00bccb0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcca70 bytes 68fa43f9
+ 00bccb0c bytes 687a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6843d3a05a28c490c93fd379d3356331"></a>

### [`00bccb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb1c.md) → [`00bccbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccbb8.md) _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bccbf4",
      "incomplete_value": true,
      "site": "00bccbf4",
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
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccb58",
      "incomplete_value": true,
      "site": "00bccb58",
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
            "const:7f8:8"
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
      "definition_site": "00bccc14",
      "incomplete_value": true,
      "site": "00bccc14",
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
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccb78",
      "incomplete_value": true,
      "site": "00bccb78",
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
            "const:7f0:8"
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
      "definition_site": "00bccbd0",
      "incomplete_value": true,
      "site": "00bccbd0",
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
      "definition_site": "00bccb34",
      "incomplete_value": true,
      "site": "00bccb34",
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
      "00bccbcc",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccbd8",
      "READ",
      [
        "storage",
        "011267f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bccbf4",
      "WRITE",
      [
        "storage",
        "011267f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bccbcc",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccbd8",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bccbf4",
      "WRITE",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccb58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb1c.md#insn-00bccb58) · [`00bccb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb1c.md#insn-00bccb74) · [`00bccb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb1c.md#insn-00bccb78)
- 新版 [`00bccbf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccbb8.md#insn-00bccbf4) · [`00bccc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccbb8.md#insn-00bccc10) · [`00bccc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccbb8.md#insn-00bccc14)

~~~diff
- 00bccb58 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bccb58 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bccb58 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7f8:8"]]
- 00bccb58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bccbf4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bccbf4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bccbf4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8f8:8"]]
+ 00bccbf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bccb58 bytes bfe21f39
+ 00bccbf4 bytes bfe22339
- 00bccb74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bccb74 ["INT_ADD", "register:40f0:8", ["const:bccb74:8", "const:4:8"]]
- 00bccb74 ["CALLIND", null, ["register:0:8"]]
+ 00bccc10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bccc10 ["INT_ADD", "register:40f0:8", ["const:bccc10:8", "const:4:8"]]
+ 00bccc10 ["CALLIND", null, ["register:0:8"]]
- 00bccb74 bytes 00013fd6
+ 00bccc10 bytes 00013fd6
- 00bccb78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f0:8"]]
- 00bccb78 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bccb78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bccc14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
+ 00bccc14 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bccc14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bccb78 bytes 9ffa03f9
+ 00bccc14 bytes 9f7a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de210cef450213c6dc0295eef149d7ee"></a>

### [`00bccb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb8c.md) → [`00bccc28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccc28.md) _ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccb8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccb8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccb90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bccb8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bccb90",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bccba0",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bccc28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bccc2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bccc3c",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb8c.md#insn-00bccb8c) · [`00bccb90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb8c.md#insn-00bccb90) · [`00bccba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb8c.md#insn-00bccba8)

~~~diff
- 00bccb8c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bccb8c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bccb8c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bccb8c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bccb8c bytes f44fbea9
- 00bccb90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bccb90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bccb90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bccb90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bccb90 bytes fd7b01a9
- 00bccba8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bccba8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bccba8 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5143f5f92d648ac52ffdefa5bdacb908"></a>

### [`00bccc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccc38.md) → [`00bcccd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcccd4.md) _ZN8firebase4auth11jnilistener13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bccc38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccc38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccc3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bccc38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bccc3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bccc4c",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcccd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcccd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bccce8",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccc38.md#insn-00bccc38) · [`00bccc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccc38.md#insn-00bccc3c) · [`00bccc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccc38.md#insn-00bccc54)

~~~diff
- 00bccc38 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bccc38 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bccc38 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bccc38 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bccc38 bytes f44fbea9
- 00bccc3c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bccc3c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bccc3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bccc3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bccc3c bytes fd7b01a9
- 00bccc54 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bccc54 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bccc54 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a4c605f46b5f4897e5195c5e611675f"></a>

### [`00bccce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccce4.md) → [`00bccd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccd80.md) _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00bccce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccce8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bccce4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bccce8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bccd90",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bccd80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bccd84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bccd90",
      "READ",
      [
        "storage",
        "01126918",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccce4.md#insn-00bccce4) · [`00bccce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccce4.md#insn-00bccce8) · [`00bccd08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccce4.md#insn-00bccd08)

~~~diff
- 00bccce4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bccce4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bccce4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bccce4 bytes f30f1ef8
- 00bccce8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bccce8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bccce8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bccce8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bccce8 bytes fd7b01a9
- 00bccd08 ["INT_ADD", "register:40f0:8", ["const:bccd08:8", "const:4:8"]]
- 00bccd08 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bccd08 bytes 82380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97890a588425e90afada7be11e8b1747"></a>

### [`00bccd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd24.md) → [`00bccdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccdc0.md) _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00bccdec",
      "incomplete_value": true,
      "site": "00bccdec",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccd50",
      "incomplete_value": true,
      "site": "00bccd50",
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
            "const:818:8"
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
      "definition_site": "00bccdd4",
      "incomplete_value": true,
      "site": "00bccdd4",
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
      "definition_site": "00bccd38",
      "incomplete_value": true,
      "site": "00bccd38",
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
      "definition_site": "00bccddc",
      "incomplete_value": false,
      "site": "00bccde4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:92e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccd40",
      "incomplete_value": false,
      "site": "00bccd48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:98a:8"
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
      "00bccdd0",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccddc",
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      "00bccdec",
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bccdd0",
      "READ",
      [
        "storage",
        "01126918",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccddc",
      "PARAM",
      [
        "storage",
        "002aa92e",
        null,
        "string"
      ]
    ],
    [
      "00bccdec",
      "WRITE",
      [
        "storage",
        "01126918",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd24.md#insn-00bccd48) · [`00bccd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd24.md#insn-00bccd50) · [`00bccd34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd24.md#insn-00bccd34)
- 新版 [`00bccde4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccdc0.md#insn-00bccde4) · [`00bccdec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccdc0.md#insn-00bccdec) · [`00bccdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccdc0.md#insn-00bccdd0)

~~~diff
- 00bccd48 ["INT_ADD", "register:40f0:8", ["const:bccd48:8", "const:4:8"]]
- 00bccd48 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bccde4 ["INT_ADD", "register:40f0:8", ["const:bccde4:8", "const:4:8"]]
+ 00bccde4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bccd48 bytes 72380294
+ 00bccde4 bytes 7f380294
- 00bccd50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:818:8"]]
- 00bccd50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bccdec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:918:8"]]
+ 00bccdec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bccd50 bytes 600e04f9
+ 00bccdec bytes 608e04f9
- 00bccd34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:818:8"]]
- 00bccd34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bccdd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:918:8"]]
+ 00bccdd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bccd34 bytes 680e44f9
+ 00bccdd0 bytes 688e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15ccf42462aebd672910132a26c78c3e"></a>

### [`00bccd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd64.md) → [`00bcce00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcce00.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bccd94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcce30"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcce14",
      "incomplete_value": true,
      "site": "00bcce14",
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
      "definition_site": "00bccd78",
      "incomplete_value": true,
      "site": "00bccd78",
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
      "00bcce10",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcce14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bccd98"
      ]
    ],
    [
      "unmatched:00bccd84",
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcce10",
      "READ",
      [
        "storage",
        "01126918",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcce14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcce34"
      ]
    ],
    [
      "00bcce20",
      "PARAM",
      [
        "storage",
        "002aa92e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd64.md#insn-00bccd8c) · [`00bccd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd64.md#insn-00bccd94) · [`00bccda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd64.md#insn-00bccda4)

~~~diff
- 00bccd8c ["INT_ADD", "register:40f0:8", ["const:bccd8c:8", "const:4:8"]]
- 00bccd8c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bccd8c bytes 61380294
- 00bccd94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:818:8"]]
- 00bccd94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bccd94 bytes 600e04f9
- 00bccda4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bccda4 ["RETURN", null, ["register:0:8"]]
- 00bccda4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f3ddce33cb415c20250c0ee48493b51"></a>

### [`00bccda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccda8.md) → [`00bcce44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcce44.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccdd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcce74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccdbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bccdb8",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bccdbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bccddc"
      ]
    ],
    [
      "unmatched:00bccdc4",
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcce54",
      "READ",
      [
        "storage",
        "01126918",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcce58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcce78"
      ]
    ],
    [
      "00bcce60",
      "PARAM",
      [
        "storage",
        "002aa92e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccda8.md#insn-00bccdbc) · [`00bccdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccda8.md#insn-00bccdd0) · [`00bccdd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccda8.md#insn-00bccdd8)
- 新版 [`00bcce6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcce44.md#insn-00bcce6c)

~~~diff
- 00bccdbc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bccdbc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bccdbc bytes 080100b5
- 00bccdd0 ["INT_ADD", "register:40f0:8", ["const:bccdd0:8", "const:4:8"]]
- 00bccdd0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bcce6c ["INT_ADD", "register:40f0:8", ["const:bcce6c:8", "const:4:8"]]
+ 00bcce6c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bccdd0 bytes 50380294
+ 00bcce6c bytes 5d380294
- 00bccdd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:818:8"]]
- 00bccdd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bccdd8 bytes 600e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-932ca42b82f354624283d182c2605cc0"></a>

### [`00bccdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccdf8.md) → [`00bcce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcce94.md) _ZN8firebase4auth21jni_id_token_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bcceec",
      "incomplete_value": true,
      "site": "00bcceec",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcce50",
      "incomplete_value": true,
      "site": "00bcce50",
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
            "const:820:8"
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
      "definition_site": "00bccec8",
      "incomplete_value": true,
      "site": "00bcced4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:918:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcce2c",
      "incomplete_value": true,
      "site": "00bcce38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:818:8"
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
      "00bccea8",
      "READ",
      [
        "storage",
        "01126820",
        null,
        "undefined1"
      ]
    ],
    [
      "00bccec8",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcceec",
      "WRITE",
      [
        "storage",
        "01126820",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bccea8",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined1"
      ]
    ],
    [
      "00bccec8",
      "READ",
      [
        "storage",
        "01126918",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcceec",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcce38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccdf8.md#insn-00bcce38) · [`00bcce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccdf8.md#insn-00bcce50) · [`00bcce0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccdf8.md#insn-00bcce0c)
- 新版 [`00bcced4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcce94.md#insn-00bcced4) · [`00bcceec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcce94.md#insn-00bcceec) · [`00bccea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcce94.md#insn-00bccea8)

~~~diff
- 00bcce38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcce38 ["INT_ADD", "register:40f0:8", ["const:bcce38:8", "const:4:8"]]
- 00bcce38 ["CALLIND", null, ["register:0:8"]]
+ 00bcced4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcced4 ["INT_ADD", "register:40f0:8", ["const:bcced4:8", "const:4:8"]]
+ 00bcced4 ["CALLIND", null, ["register:0:8"]]
- 00bcce38 bytes 00013fd6
+ 00bcced4 bytes 00013fd6
- 00bcce50 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bcce50 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:820:8"]]
- 00bcce50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bcceec ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bcceec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:920:8"]]
+ 00bcceec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bcce50 bytes a0822039
+ 00bcceec bytes a0822439
- 00bcce0c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:820:8"]]
- 00bcce0c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bcce0c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bccea8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:920:8"]]
+ 00bccea8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bccea8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bcce0c bytes a8826039
+ 00bccea8 bytes a8826439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8add7a85af243993fbae24fe8f98070"></a>

### [`00bcced4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcced4.md) → [`00bccf70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccf70.md) _ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bccf14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccfb0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccef0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bccee8",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bccef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccfb4"
      ]
    ],
    [
      "unmatched:00bccef8",
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bccf84",
      "READ",
      [
        "storage",
        "01126918",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccf8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccfb4"
      ]
    ],
    [
      "00bccf94",
      "PARAM",
      [
        "storage",
        "002aa92e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcced4.md#insn-00bccef0) · [`00bccf0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcced4.md#insn-00bccf0c) · [`00bccf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcced4.md#insn-00bccf14)
- 新版 [`00bccfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccf70.md#insn-00bccfa8)

~~~diff
- 00bccef0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bccef0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bccef0 bytes 410100b5
- 00bccf0c ["INT_ADD", "register:40f0:8", ["const:bccf0c:8", "const:4:8"]]
- 00bccf0c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bccfa8 ["INT_ADD", "register:40f0:8", ["const:bccfa8:8", "const:4:8"]]
+ 00bccfa8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bccf0c bytes 01380294
+ 00bccfa8 bytes 0e380294
- 00bccf14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:818:8"]]
- 00bccf14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bccf14 bytes 800e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1429e7c73804f67a1e61ecc79e31c61"></a>

### [`00bccf80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf80.md) → [`00bcd01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd01c.md) _ZN8firebase4auth21jni_id_token_listener13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bcd05c",
      "incomplete_value": true,
      "site": "00bcd05c",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccfc0",
      "incomplete_value": true,
      "site": "00bccfc0",
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
            "const:818:8"
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
      "definition_site": "00bcd038",
      "incomplete_value": true,
      "site": "00bcd038",
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
      "definition_site": "00bccf9c",
      "incomplete_value": true,
      "site": "00bccf9c",
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
      "definition_site": "00bcd040",
      "incomplete_value": false,
      "site": "00bcd054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:92e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccfa4",
      "incomplete_value": false,
      "site": "00bccfb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:98a:8"
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
      "00bcd030",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd040",
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      "00bcd05c",
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcd030",
      "READ",
      [
        "storage",
        "01126918",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd040",
      "PARAM",
      [
        "storage",
        "002aa92e",
        null,
        "string"
      ]
    ],
    [
      "00bcd05c",
      "WRITE",
      [
        "storage",
        "01126918",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf80.md#insn-00bccfb8) · [`00bccfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf80.md#insn-00bccfc0) · [`00bccf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf80.md#insn-00bccf94)
- 新版 [`00bcd054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd01c.md#insn-00bcd054) · [`00bcd05c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd01c.md#insn-00bcd05c) · [`00bcd030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd01c.md#insn-00bcd030)

~~~diff
- 00bccfb8 ["INT_ADD", "register:40f0:8", ["const:bccfb8:8", "const:4:8"]]
- 00bccfb8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bcd054 ["INT_ADD", "register:40f0:8", ["const:bcd054:8", "const:4:8"]]
+ 00bcd054 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bccfb8 bytes d6370294
+ 00bcd054 bytes e3370294
- 00bccfc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:818:8"]]
- 00bccfc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcd05c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:918:8"]]
+ 00bcd05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bccfc0 bytes 800e04f9
+ 00bcd05c bytes 808e04f9
- 00bccf94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:818:8"]]
- 00bccf94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcd030 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:918:8"]]
+ 00bcd030 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bccf94 bytes 810e44f9
+ 00bcd030 bytes 818e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e96dda121e4e61a1da5ecccddbc492e"></a>

### [`00bccff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccff0.md) → [`00bcd08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd08c.md) _ZN8firebase4auth21jni_id_token_listener10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bcd0a8",
      "incomplete_value": false,
      "site": "00bcd0ac",
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
      "definition_site": "00bcd00c",
      "incomplete_value": false,
      "site": "00bcd010",
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
      "definition_site": "00bcd0b8",
      "incomplete_value": true,
      "site": "00bcd0c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bcd01c",
      "incomplete_value": true,
      "site": "00bcd028",
      "value": [
        "LOAD",
        "8",
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
      "00bcd0a8",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bcd0b8",
      "DATA",
      [
        "storage",
        "01126838",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcd0a8",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bcd0b8",
      "DATA",
      [
        "storage",
        "01126938",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccff0.md#insn-00bcd010) · [`00bcd00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccff0.md#insn-00bcd00c) · [`00bcd018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccff0.md#insn-00bcd018)
- 新版 [`00bcd0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd08c.md#insn-00bcd0ac) · [`00bcd0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd08c.md#insn-00bcd0a8) · [`00bcd0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd08c.md#insn-00bcd0b4)

~~~diff
- 00bcd010 ["INT_ADD", "register:40f0:8", ["const:bcd010:8", "const:4:8"]]
- 00bcd010 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bcd0ac ["INT_ADD", "register:40f0:8", ["const:bcd0ac:8", "const:4:8"]]
+ 00bcd0ac ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bcd010 bytes fc370294
+ 00bcd0ac bytes 09380294
- 00bcd00c ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bcd00c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcd00c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcd00c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcd0a8 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bcd0a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcd0a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcd0a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcd00c bytes 00781491
+ 00bcd0a8 bytes 00341591
- 00bcd018 ["COPY", "tmp:0:8", ["const:838:8"]]
- 00bcd018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcd018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcd018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcd0b4 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00bcd0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcd0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcd0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcd018 bytes 08e12091
+ 00bcd0b4 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d522720a06d680b2a2db5e977c2d1f9"></a>

### [`00bcd02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd02c.md) → [`00bcd0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd0c8.md) _ZN8firebase4auth18CacheAuthMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5dc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc40.md) · 呼出先 3件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 1件 [`00c5dd10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd10.md) · 呼出先 3件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 37.86% / 新版 37.86%

CFGの説明率　旧版 17.14% / 新版 17.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd078"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd0d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd128"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcd048",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcd054",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcd07c"
      ]
    ],
    [
      "unmatched:00bcd05c",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcd0e4",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd0f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcd118"
      ]
    ],
    [
      "00bcd0f8",
      "PARAM",
      [
        "storage",
        "002ac1e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd02c.md#insn-00bcd054) · [`00bcd070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd02c.md#insn-00bcd070) · [`00bcd078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd02c.md#insn-00bcd078)

~~~diff
- 00bcd054 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcd054 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcd054 bytes 410100b5
- 00bcd070 ["INT_ADD", "register:40f0:8", ["const:bcd070:8", "const:4:8"]]
- 00bcd070 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bcd070 bytes a8370294
- 00bcd078 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 00bcd078 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcd078 bytes c09603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b618e368b85f3cc3a479640bebd791d"></a>

### [`00bcd25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd25c.md) → [`00bcd2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd2f8.md) _ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5dc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc60.md) · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 1件 [`00c5dd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd30.md) · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 28.24% / 新版 28.24%

CFGの説明率　旧版 10.71% / 新版 10.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd298"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd2b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd2e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcd30c",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd314",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcd2bc"
      ]
    ],
    [
      "unmatched:00bcd280",
      "READ",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcd30c",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd314",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcd358"
      ]
    ],
    [
      "00bcd31c",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd25c.md#insn-00bcd278) · [`00bcd284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd25c.md#insn-00bcd284) · [`00bcd294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd25c.md#insn-00bcd294)
- 新版 [`00bcd314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd2f8.md#insn-00bcd314)

~~~diff
- 00bcd278 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcd278 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bcd314 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bcd314 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bcd278 bytes 210200b4
+ 00bcd314 bytes 210200b4
- 00bcd284 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00bcd284 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcd284 bytes c8000034
- 00bcd294 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd294 ["INT_ADD", "register:40f0:8", ["const:bcd294:8", "const:4:8"]]
- 00bcd294 ["CALLIND", null, ["register:0:8"]]
- 00bcd294 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7e2d08a097bc2a280aa13acbd2cceb3"></a>

### [`00bcd3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd3b0.md) → [`00bcd44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd44c.md) _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc30.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 1件 [`00c5dd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd00.md) · 呼出先 7件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd3b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd3b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd3b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcd3b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd3b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd3b8",
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
      "00bcd44c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bcd450",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcd454",
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

- 旧版 [`00bcd3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd3b0.md#insn-00bcd3b0) · [`00bcd3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd3b0.md#insn-00bcd3b4) · [`00bcd3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd3b0.md#insn-00bcd3b8)

~~~diff
- 00bcd3b0 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00bcd3b0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00bcd3b0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcd3b0 bytes f70f1cf8
- 00bcd3b4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bcd3b4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bcd3b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcd3b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcd3b4 bytes f65701a9
- 00bcd3b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcd3b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcd3b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcd3b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcd3b8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25e1d401274ad172e57b0447e1c3d205"></a>

### [`00bcd46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd46c.md) → [`00bcd508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd508.md) _ZN8firebase4auth14SetEmulatorJniEPNS0_8AuthDataEPKcj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd548",
      "incomplete_value": true,
      "site": "00bcd55c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:888:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd4ac",
      "incomplete_value": true,
      "site": "00bcd4c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:788:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcd548",
      "READ",
      [
        "storage",
        "01126788",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcd548",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd46c.md#insn-00bcd4c0) · [`00bcd48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd46c.md#insn-00bcd48c) · [`00bcd4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd46c.md#insn-00bcd4a0)
- 新版 [`00bcd55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd508.md#insn-00bcd55c) · [`00bcd528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd508.md#insn-00bcd528) · [`00bcd53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd508.md#insn-00bcd53c)

~~~diff
- 00bcd4c0 ["INT_ADD", "register:40f0:8", ["const:bcd4c0:8", "const:4:8"]]
- 00bcd4c0 ["CALL", null, ["callee:00574d2c:8"]]
+ 00bcd55c ["INT_ADD", "register:40f0:8", ["const:bcd55c:8", "const:4:8"]]
+ 00bcd55c ["CALL", null, ["callee:00574d2c:8"]]
- 00bcd4c0 bytes 0b9ee697
+ 00bcd55c bytes f49de697
- 00bcd48c ["INT_ADD", "register:40f0:8", ["const:bcd48c:8", "const:4:8"]]
- 00bcd48c ["CALL", null, ["callee:00c5b150:8"]]
+ 00bcd528 ["INT_ADD", "register:40f0:8", ["const:bcd528:8", "const:4:8"]]
+ 00bcd528 ["CALL", null, ["callee:00c5b150:8"]]
- 00bcd48c bytes fd360294
+ 00bcd528 bytes 0a370294
- 00bcd4a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd4a0 ["INT_ADD", "register:40f0:8", ["const:bcd4a0:8", "const:4:8"]]
- 00bcd4a0 ["CALLIND", null, ["register:0:8"]]
+ 00bcd53c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd53c ["INT_ADD", "register:40f0:8", ["const:bcd53c:8", "const:4:8"]]
+ 00bcd53c ["CALLIND", null, ["register:0:8"]]
- 00bcd4a0 bytes 00013fd6
+ 00bcd53c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4920aa021a411e079161a02653e7c2ad"></a>

### [`00bcd4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd4ec.md) → [`00bcd588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd588.md) _ZN8firebase4auth13CheckEmulatorEPNS0_8AuthDataE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5dc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc20.md) · 呼出先 9件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58060.md) [`00c598a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c598a0.md)
- 新版 呼出元 1件 [`00c5dcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dcf0.md) · 呼出先 9件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58130.md) [`00c59970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59970.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.39% / 新版 74.39%

CFGの説明率　旧版 12.50% / 新版 11.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd514"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcd5b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd51c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcd510",
      "PARAM",
      [
        "storage",
        "002baf13",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcd514",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd518",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59970"
      ]
    ]
  ],
  "added": [
    [
      "00bcd5ac",
      "PARAM",
      [
        "storage",
        "002baebf",
        null,
        "string"
      ]
    ],
    [
      "00bcd5b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00bcd5b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59970"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd4ec.md#insn-00bcd514) · [`00bcd518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd4ec.md#insn-00bcd518) · [`00bcd51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd4ec.md#insn-00bcd51c)

~~~diff
- 00bcd514 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00bcd514 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bcd514 bytes e80f00f9
- 00bcd518 ["INT_ADD", "register:40f0:8", ["const:bcd518:8", "const:4:8"]]
- 00bcd518 ["CALL", null, ["callee:00c59970:8"]]
- 00bcd518 bytes e2300294
- 00bcd51c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bcd51c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00bcd51c bytes 200700b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-826d6d02a3fd9a36ebb6296b32c5cab6"></a>

### [`00bcd654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd654.md) → [`00bcd6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd6f0.md) _ZN8firebase4auth18CreatePlatformAuthEPNS_3AppE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9d0.md) · 呼出先 21件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aea0.md)
- 新版 呼出元 1件 [`00c5daa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5daa0.md) · 呼出先 21件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5af70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcd734",
      "incomplete_value": true,
      "site": "00bcd734",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd698",
      "incomplete_value": true,
      "site": "00bcd698",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd744",
      "incomplete_value": true,
      "site": "00bcd758",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:828:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd6a8",
      "incomplete_value": true,
      "site": "00bcd6bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:728:8"
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
    "new": {
      "definition_site": "00bcd748",
      "incomplete_value": true,
      "site": "00bcd758",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd6ac",
      "incomplete_value": true,
      "site": "00bcd6bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcd720",
      "READ",
      [
        "storage",
        "01126840",
        null,
        "undefined4"
      ]
    ],
    [
      "00bcd734",
      "WRITE",
      [
        "storage",
        "01126840",
        null,
        "undefined4"
      ]
    ],
    [
      "00bcd744",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcd720",
      "READ",
      [
        "storage",
        "01126940",
        null,
        "undefined4"
      ]
    ],
    [
      "00bcd734",
      "WRITE",
      [
        "storage",
        "01126940",
        null,
        "undefined4"
      ]
    ],
    [
      "00bcd744",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd654.md#insn-00bcd698) · [`00bcd6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd654.md#insn-00bcd6bc) · [`00bcd6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd654.md#insn-00bcd6d8)
- 新版 [`00bcd734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd6f0.md#insn-00bcd734) · [`00bcd758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd6f0.md#insn-00bcd758) · [`00bcd774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd6f0.md#insn-00bcd774)

~~~diff
- 00bcd698 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:840:8"]]
- 00bcd698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00bcd734 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:940:8"]]
+ 00bcd734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00bcd698 bytes e84208b9
+ 00bcd734 bytes e84209b9
- 00bcd6bc ["INT_ADD", "register:40f0:8", ["const:bcd6bc:8", "const:4:8"]]
- 00bcd6bc ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bcd758 ["INT_ADD", "register:40f0:8", ["const:bcd758:8", "const:4:8"]]
+ 00bcd758 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bcd6bc bytes 39350294
+ 00bcd758 bytes 46350294
- 00bcd6d8 ["INT_ADD", "register:40f0:8", ["const:bcd6d8:8", "const:4:8"]]
- 00bcd6d8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bcd774 ["INT_ADD", "register:40f0:8", ["const:bcd774:8", "const:4:8"]]
+ 00bcd774 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bcd6d8 bytes 4a360294
+ 00bcd774 bytes 57360294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0819b0b6e3eb7a48c50925c8b86a4004"></a>

### [`00bcd890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd890.md) → [`00bcd92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd92c.md) _ZN8firebase4auth4Auth16InitPlatformAuthEPNS0_8AuthDataE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5da40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da40.md) · 呼出先 6件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5dc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc20.md) [`00c5dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc30.md)
- 新版 呼出元 1件 [`00c5db10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db10.md) · 呼出先 6件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5dcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dcf0.md) [`00c5dd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd00.md)

変更の種類 call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 86.00% / 新版 86.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd950",
      "incomplete_value": true,
      "site": "00bcd960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd8b4",
      "incomplete_value": true,
      "site": "00bcd8c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f0:8"
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
    "new": {
      "definition_site": "00bcd954",
      "incomplete_value": true,
      "site": "00bcd960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:900:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd8b8",
      "incomplete_value": true,
      "site": "00bcd8c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:800:8"
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
      "definition_site": "00bcd970",
      "incomplete_value": true,
      "site": "00bcd980",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:860:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd8d4",
      "incomplete_value": true,
      "site": "00bcd8e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:760:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcd950",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd954",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd970",
      "READ",
      [
        "storage",
        "01126760",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcd950",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd954",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd970",
      "READ",
      [
        "storage",
        "01126860",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd890.md#insn-00bcd8c4) · [`00bcd8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd890.md#insn-00bcd8e4) · [`00bcd8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd890.md#insn-00bcd8f4)
- 新版 [`00bcd960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd92c.md#insn-00bcd960) · [`00bcd980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd92c.md#insn-00bcd980) · [`00bcd990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd92c.md#insn-00bcd990)

~~~diff
- 00bcd8c4 ["INT_ADD", "register:40f0:8", ["const:bcd8c4:8", "const:4:8"]]
- 00bcd8c4 ["CALL", null, ["callee:00589734:8"]]
+ 00bcd960 ["INT_ADD", "register:40f0:8", ["const:bcd960:8", "const:4:8"]]
+ 00bcd960 ["CALL", null, ["callee:00589734:8"]]
- 00bcd8c4 bytes 8cefe697
+ 00bcd960 bytes 75efe697
- 00bcd8e4 ["INT_ADD", "register:40f0:8", ["const:bcd8e4:8", "const:4:8"]]
- 00bcd8e4 ["CALL", null, ["callee:00574d2c:8"]]
+ 00bcd980 ["INT_ADD", "register:40f0:8", ["const:bcd980:8", "const:4:8"]]
+ 00bcd980 ["CALL", null, ["callee:00574d2c:8"]]
- 00bcd8e4 bytes 029de697
+ 00bcd980 bytes eb9ce697
- 00bcd8f4 ["INT_ADD", "register:40f0:8", ["const:bcd8f4:8", "const:4:8"]]
- 00bcd8f4 ["CALL", null, ["callee:00c5dd50:8"]]
+ 00bcd990 ["INT_ADD", "register:40f0:8", ["const:bcd990:8", "const:4:8"]]
+ 00bcd990 ["CALL", null, ["callee:00c5dd50:8"]]
- 00bcd8f4 bytes e3400294
+ 00bcd990 bytes f0400294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79d30a5ac2843b744ea66a522fdcfb8f"></a>

### [`00bcd958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd958.md) → [`00bcd9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd9f4.md) _ZN8firebase4auth4Auth19DestroyPlatformAuthEPNS0_8AuthDataE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5da50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da50.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af00.md) [`00c5afd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afd0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 1件 [`00c5db20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db20.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afd0.md) [`00c5b0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0a0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 30.00% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcdafc",
      "incomplete_value": true,
      "site": "00bcdafc",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcda60",
      "incomplete_value": true,
      "site": "00bcda60",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcda40",
      "incomplete_value": true,
      "site": "00bcda4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd9a4",
      "incomplete_value": true,
      "site": "00bcd9b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcda5c",
      "incomplete_value": true,
      "site": "00bcda6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:868:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcd9c0",
      "incomplete_value": true,
      "site": "00bcd9d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:768:8"
              ]
            ]
          ]
        ]
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
      "unmatched:00bcd9a4",
      "READ",
      [
        "storage",
        "01126808",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcd9c0",
      "READ",
      [
        "storage",
        "01126768",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcd9dc",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcda40",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcda5c",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcda78",
      "READ",
      [
        "storage",
        "01126930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd958.md#insn-00bcd9b0) · [`00bcd9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd958.md#insn-00bcd9d0) · [`00bcd9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd958.md#insn-00bcd9e8)
- 新版 [`00bcda4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd9f4.md#insn-00bcda4c) · [`00bcda6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd9f4.md#insn-00bcda6c) · [`00bcda84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd9f4.md#insn-00bcda84)

~~~diff
- 00bcd9b0 ["INT_ADD", "register:40f0:8", ["const:bcd9b0:8", "const:4:8"]]
- 00bcd9b0 ["CALL", null, ["callee:00574d2c:8"]]
+ 00bcda4c ["INT_ADD", "register:40f0:8", ["const:bcda4c:8", "const:4:8"]]
+ 00bcda4c ["CALL", null, ["callee:00574d2c:8"]]
- 00bcd9b0 bytes cf9ce697
+ 00bcda4c bytes b89ce697
- 00bcd9d0 ["INT_ADD", "register:40f0:8", ["const:bcd9d0:8", "const:4:8"]]
- 00bcd9d0 ["CALL", null, ["callee:00574d2c:8"]]
+ 00bcda6c ["INT_ADD", "register:40f0:8", ["const:bcda6c:8", "const:4:8"]]
+ 00bcda6c ["CALL", null, ["callee:00574d2c:8"]]
- 00bcd9d0 bytes c79ce697
+ 00bcda6c bytes b09ce697
- 00bcd9e8 ["INT_ADD", "register:40f0:8", ["const:bcd9e8:8", "const:4:8"]]
- 00bcd9e8 ["CALL", null, ["callee:00574d2c:8"]]
+ 00bcda84 ["INT_ADD", "register:40f0:8", ["const:bcda84:8", "const:4:8"]]
+ 00bcda84 ["CALL", null, ["callee:00574d2c:8"]]
- 00bcd9e8 bytes c19ce697
+ 00bcda84 bytes aa9ce697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83bac921495bdd1ddc9d4115688ece24"></a>

### [`00bcdab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdab4.md) → [`00bcdb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdb50.md) _ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d990.md) · 呼出先 5件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5bef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bef0.md) [`00c5da80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da80.md)
- 新版 呼出元 1件 [`00c5da60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da60.md) · 呼出先 5件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5bfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bfc0.md) [`00c5db50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db50.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcdb88",
      "incomplete_value": true,
      "site": "00bcdb9c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:828:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdaec",
      "incomplete_value": true,
      "site": "00bcdb00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:728:8"
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
      "definition_site": "00bcdb8c",
      "incomplete_value": true,
      "site": "00bcdb9c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdaf0",
      "incomplete_value": true,
      "site": "00bcdb00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
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
      "unmatched:00bcdaec",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcdaf0",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcdb38",
      "READ",
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
      "00bcdb88",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcdb8c",
      "READ",
      [
        "storage",
        "01126838",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcdbd4",
      "READ",
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

- 旧版 [`00bcdb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdab4.md#insn-00bcdb00) · [`00bcdad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdab4.md#insn-00bcdad0) · [`00bcdadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdab4.md#insn-00bcdadc)
- 新版 [`00bcdb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdb50.md#insn-00bcdb9c) · [`00bcdb6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdb50.md#insn-00bcdb6c) · [`00bcdb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdb50.md#insn-00bcdb78)

~~~diff
- 00bcdb00 ["INT_ADD", "register:40f0:8", ["const:bcdb00:8", "const:4:8"]]
- 00bcdb00 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bcdb9c ["INT_ADD", "register:40f0:8", ["const:bcdb9c:8", "const:4:8"]]
+ 00bcdb9c ["CALL", null, ["callee:00c5ac70:8"]]
- 00bcdb00 bytes 28340294
+ 00bcdb9c bytes 35340294
- 00bcdad0 ["INT_ADD", "register:40f0:8", ["const:bcdad0:8", "const:4:8"]]
- 00bcdad0 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bcdb6c ["INT_ADD", "register:40f0:8", ["const:bcdb6c:8", "const:4:8"]]
+ 00bcdb6c ["CALL", null, ["callee:00c5b150:8"]]
- 00bcdad0 bytes 6c350294
+ 00bcdb6c bytes 79350294
- 00bcdadc ["INT_ADD", "register:40f0:8", ["const:bcdadc:8", "const:4:8"]]
- 00bcdadc ["CALL", null, ["callee:00c5db50:8"]]
+ 00bcdb78 ["INT_ADD", "register:40f0:8", ["const:bcdb78:8", "const:4:8"]]
+ 00bcdb78 ["CALL", null, ["callee:00c5db50:8"]]
- 00bcdadc bytes e93f0294
+ 00bcdb78 bytes f63f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aac71bafda61eade9dcac944fbea93f"></a>

### [`00bcdb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb44.md) → [`00bcdbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdbe0.md) _ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5da10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da10.md) [`00c5dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5dae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dae0.md) [`00c5dd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd00.md)

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
      "definition_site": "00bcdbec",
      "incomplete_value": true,
      "site": "00bcdbf4",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcdb58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb44.md#insn-00bcdb58)
- 新版 [`00bcdbf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdbe0.md#insn-00bcdbf4)

~~~diff
- 00bcdb58 ["INT_ADD", "register:40f0:8", ["const:bcdb58:8", "const:4:8"]]
- 00bcdb58 ["CALL", null, ["callee:00c5dd00:8"]]
+ 00bcdbf4 ["INT_ADD", "register:40f0:8", ["const:bcdbf4:8", "const:4:8"]]
+ 00bcdbf4 ["CALL", null, ["callee:00c5dd00:8"]]
- 00bcdb58 bytes 36400294
+ 00bcdbf4 bytes 43400294
~~~


<a id="compare-7dd154849700a2fd29a42737b82c7ec0"></a>

### [`00bcdb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb6c.md) → [`00bcdc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc08.md) _ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9f0.md) [`00c5dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5dac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dac0.md) [`00c5dd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd00.md)

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
      "definition_site": "00bcdb8c",
      "incomplete_value": true,
      "site": "00bcdb90",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcdb90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb6c.md#insn-00bcdb90) · [`00bcdb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb6c.md#insn-00bcdb84) · [`00bcdb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb6c.md#insn-00bcdb98)
- 新版 [`00bcdc2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc08.md#insn-00bcdc2c) · [`00bcdc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc08.md#insn-00bcdc20) · [`00bcdc34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc08.md#insn-00bcdc34)

~~~diff
- 00bcdb90 ["INT_ADD", "register:40f0:8", ["const:bcdb90:8", "const:4:8"]]
- 00bcdb90 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bcdc2c ["INT_ADD", "register:40f0:8", ["const:bcdc2c:8", "const:4:8"]]
+ 00bcdc2c ["CALL", null, ["callee:00c5aae0:8"]]
- 00bcdb90 bytes a0330294
+ 00bcdc2c bytes ad330294
- 00bcdb84 ["INT_ADD", "register:40f0:8", ["const:bcdb84:8", "const:4:8"]]
- 00bcdb84 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcdc20 ["INT_ADD", "register:40f0:8", ["const:bcdc20:8", "const:4:8"]]
+ 00bcdc20 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcdb84 bytes 9f330294
+ 00bcdc20 bytes ac330294
- 00bcdb98 ["INT_ADD", "register:40f0:8", ["const:bcdb98:8", "const:4:8"]]
- 00bcdb98 ["CALL", null, ["callee:00c5dd00:8"]]
+ 00bcdc34 ["INT_ADD", "register:40f0:8", ["const:bcdc34:8", "const:4:8"]]
+ 00bcdc34 ["CALL", null, ["callee:00c5dd00:8"]]
- 00bcdb98 bytes 26400294
+ 00bcdc34 bytes 33400294
~~~


<a id="compare-e0a5364cd0edd36a5d68f193d46539ba"></a>

### [`00bcdbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) → [`00bcdc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc4c.md) _ZN8firebase4auth4Auth22FetchProvidersForEmailEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcdeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdeb4.md) [`00bcf8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf8a0.md) [`00bcfa2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bcdf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdf50.md) [`00bcf93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf93c.md) [`00bcfac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfac8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.82% / 新版 91.82%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdbb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdbb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdbb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcdbb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcdbb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcdbbc",
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
      "00bcdc50",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bcdc54",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bcdc58",
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

- 旧版 [`00bcdbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md#insn-00bcdbb4) · [`00bcdbb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md#insn-00bcdbb8) · [`00bcdbbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md#insn-00bcdbbc)

~~~diff
- 00bcdbb4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bcdbb4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bcdbb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bcdbb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcdbb4 bytes fa6704a9
- 00bcdbb8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bcdbb8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bcdbb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bcdbb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcdbb8 bytes f85f05a9
- 00bcdbbc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bcdbbc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bcdbbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bcdbbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcdbbc bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d41db8a9fb1a24b9cf08e1f91efceb4"></a>

### [`00bcddb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcddb0.md) → [`00bcde4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcde4c.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFut

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5dce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dce0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbd0.md)
- 新版 呼出元 1件 [`00c5ddb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ddb0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) [`00c5dca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dca0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 53.85% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcddd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcddd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcddd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcddd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcddd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcdddc",
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
      "00bcde70",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00bcde74",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bcde78",
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

- 旧版 [`00bcddd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcddb0.md#insn-00bcddd4) · [`00bcddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcddb0.md#insn-00bcddd8) · [`00bcdddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcddb0.md#insn-00bcdddc)

~~~diff
- 00bcddd4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bcddd4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00bcddd4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bcddd4 bytes a8831df8
- 00bcddd8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bcddd8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bcddd8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00bcddd8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00bcddd8 bytes ff7f02a9
- 00bcdddc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00bcdddc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bcdddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bcdddc bytes ff0f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f02944682cf35d84488e91fd9869818c"></a>

### [`00bcdeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdeb4.md) → [`00bcdf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdf50.md) FUN_00bcdf50

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bcdbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) · 呼出先 10件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 1件 [`00bcdc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdc4c.md) · 呼出先 10件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 54.17% / 新版 54.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdf78"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce0a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bce014"
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
      "00bcdfa8",
      "PARAM",
      [
        "storage",
        "002a0d25",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcdf1c",
      "READ",
      [
        "storage",
        "011267e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcdf78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bce03c"
      ]
    ]
  ],
  "added": [
    [
      "00bcdfa8",
      "PARAM",
      [
        "storage",
        "002a0cd8",
        null,
        "string"
      ]
    ],
    [
      "00bcdfb8",
      "READ",
      [
        "storage",
        "011268e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bce014",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bce03c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcdf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdeb4.md#insn-00bcdf10) · [`00bcdf28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdeb4.md#insn-00bcdf28) · [`00bcdf54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdeb4.md#insn-00bcdf54)
- 新版 [`00bcdfac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdf50.md#insn-00bcdfac) · [`00bcdfc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdf50.md#insn-00bcdfc4) · [`00bcdff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdf50.md#insn-00bcdff0)

~~~diff
- 00bcdf10 ["INT_ADD", "register:40f0:8", ["const:bcdf10:8", "const:4:8"]]
- 00bcdf10 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bcdfac ["INT_ADD", "register:40f0:8", ["const:bcdfac:8", "const:4:8"]]
+ 00bcdfac ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bcdf10 bytes 3c340294
+ 00bcdfac bytes 49340294
- 00bcdf28 ["INT_ADD", "register:40f0:8", ["const:bcdf28:8", "const:4:8"]]
- 00bcdf28 ["CALL", null, ["callee:00497874:8"]]
+ 00bcdfc4 ["INT_ADD", "register:40f0:8", ["const:bcdfc4:8", "const:4:8"]]
+ 00bcdfc4 ["CALL", null, ["callee:00497874:8"]]
- 00bcdf28 bytes 4326e397
+ 00bcdfc4 bytes 2c26e397
- 00bcdf54 ["INT_ADD", "register:40f0:8", ["const:bcdf54:8", "const:4:8"]]
- 00bcdf54 ["CALL", null, ["callee:005762f8:8"]]
+ 00bcdff0 ["INT_ADD", "register:40f0:8", ["const:bcdff0:8", "const:4:8"]]
+ 00bcdff0 ["CALL", null, ["callee:005762f8:8"]]
- 00bcdf54 bytes d9a0e697
+ 00bcdff0 bytes c2a0e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-634b149a1eaca7434f9847b37cd7dc3a"></a>

### [`00bce0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce0c8.md) → [`00bce164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce164.md) _ZN8firebase4auth4Auth21SignInWithCustomTokenEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bcfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md) [`00bd48c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd48c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.76% / 新版 87.76%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce1b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce1b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bce254"
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
      "00bce1d8",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bce1b4",
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bce1b8",
      "DATA",
      [
        "storage",
        "00bd482c",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bce1d8",
      "READ",
      [
        "storage",
        "01126898",
        null,
        "undefined8"
      ]
    ],
    [
      "00bce250",
      "READ",
      [
        "storage",
        "00c9baf0",
        null,
        "pointer"
      ]
    ],
    [
      "00bce254",
      "DATA",
      [
        "storage",
        "00bd48c8",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bce11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce0c8.md#insn-00bce11c) · [`00bce130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce0c8.md#insn-00bce130) · [`00bce150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce0c8.md#insn-00bce150)
- 新版 [`00bce1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce164.md#insn-00bce1b8) · [`00bce1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce164.md#insn-00bce1ec)

~~~diff
- 00bce11c ["INT_ADD", "register:40f0:8", ["const:bce11c:8", "const:4:8"]]
- 00bce11c ["CALL", null, ["callee:00c5b150:8"]]
+ 00bce1b8 ["INT_ADD", "register:40f0:8", ["const:bce1b8:8", "const:4:8"]]
+ 00bce1b8 ["CALL", null, ["callee:00c5b150:8"]]
- 00bce11c bytes d9330294
+ 00bce1b8 bytes e6330294
- 00bce130 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bce130 ["INT_ADD", "register:40f0:8", ["const:bce130:8", "const:4:8"]]
- 00bce130 ["CALLIND", null, ["register:0:8"]]
- 00bce130 bytes 00013fd6
- 00bce150 ["INT_ADD", "register:40f0:8", ["const:bce150:8", "const:4:8"]]
- 00bce150 ["CALL", null, ["callee:00497874:8"]]
+ 00bce1ec ["INT_ADD", "register:40f0:8", ["const:bce1ec:8", "const:4:8"]]
+ 00bce1ec ["CALL", null, ["callee:00497874:8"]]
- 00bce150 bytes b925e397
+ 00bce1ec bytes a225e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d332d391b7592d25e43b87806bd2f13"></a>

### [`00bce890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce890.md) → [`00bce92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce92c.md) _ZN8firebase4auth4Auth35SignInAndRetrieveDataWithCredentialERKNS0_10CredentialE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9e0.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5aab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aab0.md) · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bcfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md) [`00bd48c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd48c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 6.82% / 新版 7.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce894"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce894"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce898"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bce894",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bce898",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bce9d4",
      "READ",
      [
        "storage",
        "011267a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bce930",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bce934",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bce9d4",
      "READ",
      [
        "storage",
        "011268a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bce894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce890.md#insn-00bce894) · [`00bce898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce890.md#insn-00bce898) · [`00bce8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce890.md#insn-00bce8f8)
- 新版 [`00bce994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce92c.md#insn-00bce994)

~~~diff
- 00bce894 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bce894 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bce894 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bce894 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bce894 bytes fa6704a9
- 00bce898 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bce898 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bce898 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bce898 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bce898 bytes f85f05a9
- 00bce8f8 ["INT_ADD", "register:40f0:8", ["const:bce8f8:8", "const:4:8"]]
- 00bce8f8 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bce994 ["INT_ADD", "register:40f0:8", ["const:bce994:8", "const:4:8"]]
+ 00bce994 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bce8f8 bytes 42310294
+ 00bce994 bytes 4f310294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a50187fd24ed6ce83e55c78ccd5ec271"></a>

### [`00bcea7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcea7c.md) → [`00bceb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bceb18.md) _ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ab90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab90.md) · 呼出先 3件 [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5ac60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac60.md) · 呼出先 3件 [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bceb54",
      "incomplete_value": false,
      "site": "00bceb58",
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
            "const:c02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bceab8",
      "incomplete_value": false,
      "site": "00bceabc",
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
            "const:bc2:8"
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
      "unmatched:00bceab8",
      "PARAM",
      [
        "storage",
        "002b5bc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bceb54",
      "PARAM",
      [
        "storage",
        "002b5c02",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bceabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcea7c.md#insn-00bceabc) · [`00bcea8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcea7c.md#insn-00bcea8c) · [`00bceab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcea7c.md#insn-00bceab8)
- 新版 [`00bceb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bceb18.md#insn-00bceb58) · [`00bceb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bceb18.md#insn-00bceb28)

~~~diff
- 00bceabc ["INT_ADD", "register:40f0:8", ["const:bceabc:8", "const:4:8"]]
- 00bceabc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bceb58 ["INT_ADD", "register:40f0:8", ["const:bceb58:8", "const:4:8"]]
+ 00bceb58 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bceabc bytes 51310294
+ 00bceb58 bytes 5e310294
- 00bcea8c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcea8c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bceb28 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bceb28 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcea8c bytes 410100b4
+ 00bceb28 bytes 410100b4
- 00bceab8 ["COPY", "tmp:0:8", ["const:bc2:8"]]
- 00bceab8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bceab8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bceab8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bceab8 bytes 00082f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec18b4dbaa3394f4e155e3e17147b17c"></a>

### [`00bceb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bceb00.md) → [`00bceb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bceb9c.md) _ZN8firebase4auth4Auth17SignInAnonymouslyEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bcfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md) [`00bd48c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd48c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 55.56% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcec58",
      "incomplete_value": true,
      "site": "00bcec58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcebbc",
      "incomplete_value": true,
      "site": "00bcebbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a20:8"
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcec30"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bceccc"
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
      "00bcebf8",
      "READ",
      [
        "storage",
        "011267a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcec54",
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      "00bcec58",
      "DATA",
      [
        "storage",
        "00bd482c",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcebf8",
      "READ",
      [
        "storage",
        "011268a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcec54",
      "READ",
      [
        "storage",
        "00c9baf0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcec58",
      "DATA",
      [
        "storage",
        "00bd48c8",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bceb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bceb00.md#insn-00bceb50) · [`00bceb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bceb00.md#insn-00bceb68) · [`00bcebec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bceb00.md#insn-00bcebec)
- 新版 [`00bcebec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bceb9c.md#insn-00bcebec) · [`00bcec04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bceb9c.md#insn-00bcec04) · [`00bcec88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bceb9c.md#insn-00bcec88)

~~~diff
- 00bceb50 ["INT_ADD", "register:40f0:8", ["const:bceb50:8", "const:4:8"]]
- 00bceb50 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bcebec ["INT_ADD", "register:40f0:8", ["const:bcebec:8", "const:4:8"]]
+ 00bcebec ["CALL", null, ["callee:00c5b150:8"]]
- 00bceb50 bytes 4c310294
+ 00bcebec bytes 59310294
- 00bceb68 ["INT_ADD", "register:40f0:8", ["const:bceb68:8", "const:4:8"]]
- 00bceb68 ["CALL", null, ["callee:00497874:8"]]
+ 00bcec04 ["INT_ADD", "register:40f0:8", ["const:bcec04:8", "const:4:8"]]
+ 00bcec04 ["CALL", null, ["callee:00497874:8"]]
- 00bceb68 bytes 3323e397
+ 00bcec04 bytes 1c23e397
- 00bcebec ["INT_ADD", "register:40f0:8", ["const:bcebec:8", "const:4:8"]]
- 00bcebec ["CALL", null, ["callee:00c5b010:8"]]
+ 00bcec88 ["INT_ADD", "register:40f0:8", ["const:bcec88:8", "const:4:8"]]
+ 00bcec88 ["CALL", null, ["callee:00c5b010:8"]]
- 00bcebec bytes d5300294
+ 00bcec88 bytes e2300294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0b673e7401fdc50dafd8639a43a1126"></a>

### [`00bcec8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcec8c.md) → [`00bced28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bced28.md) _ZN8firebase4auth4Auth26SignInWithEmailAndPasswordEPKcS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bcfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md) [`00bd48c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd48c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 99.30% / 新版 99.30%

CFGの説明率　旧版 40.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcee6c",
      "incomplete_value": true,
      "site": "00bcee6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcedd0",
      "incomplete_value": true,
      "site": "00bcedd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a20:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcedd8",
      "incomplete_value": true,
      "site": "00bcedf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bced3c",
      "incomplete_value": true,
      "site": "00bced54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcedb4",
      "incomplete_value": false,
      "site": "00bcedb8",
      "value": [
        "leaf",
        "const:20:8"
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
      "00bcedd8",
      "READ",
      [
        "storage",
        "011267b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcee68",
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      "00bcee6c",
      "DATA",
      [
        "storage",
        "00bd482c",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcedd8",
      "READ",
      [
        "storage",
        "011268b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcee68",
      "READ",
      [
        "storage",
        "00c9baf0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcee6c",
      "DATA",
      [
        "storage",
        "00bd48c8",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bced54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcec8c.md#insn-00bced54) · [`00bcedb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcec8c.md#insn-00bcedb8) · [`00bcedf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcec8c.md#insn-00bcedf0)
- 新版 [`00bcedf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bced28.md#insn-00bcedf0) · [`00bcee54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bced28.md#insn-00bcee54) · [`00bcee8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bced28.md#insn-00bcee8c)

~~~diff
- 00bced54 ["INT_ADD", "register:40f0:8", ["const:bced54:8", "const:4:8"]]
- 00bced54 ["CALL", null, ["callee:00497874:8"]]
+ 00bcedf0 ["INT_ADD", "register:40f0:8", ["const:bcedf0:8", "const:4:8"]]
+ 00bcedf0 ["CALL", null, ["callee:00497874:8"]]
- 00bced54 bytes b822e397
+ 00bcedf0 bytes a122e397
- 00bcedb8 ["INT_ADD", "register:40f0:8", ["const:bcedb8:8", "const:4:8"]]
- 00bcedb8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bcee54 ["INT_ADD", "register:40f0:8", ["const:bcee54:8", "const:4:8"]]
+ 00bcee54 ["CALL", null, ["callee:00c57f60:8"]]
- 00bcedb8 bytes 36240294
+ 00bcee54 bytes 43240294
- 00bcedf0 ["INT_ADD", "register:40f0:8", ["const:bcedf0:8", "const:4:8"]]
- 00bcedf0 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bcee8c ["INT_ADD", "register:40f0:8", ["const:bcee8c:8", "const:4:8"]]
+ 00bcee8c ["CALL", null, ["callee:00c5aed0:8"]]
- 00bcedf0 bytes 04300294
+ 00bcee8c bytes 11300294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a92c9291eeb2702969fa5d8d89b1a2d9"></a>

### [`00bcef18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcef18.md) → [`00bcefb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bcefb4.md) _ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bcfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md) [`00bd48c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd48c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.30% / 新版 99.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcf0f8",
      "incomplete_value": true,
      "site": "00bcf0f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf05c",
      "incomplete_value": true,
      "site": "00bcf05c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a20:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf064",
      "incomplete_value": true,
      "site": "00bcf07c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcefc8",
      "incomplete_value": true,
      "site": "00bcefe0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf138",
      "incomplete_value": false,
      "site": "00bcf14c",
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
            "const:221:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf09c",
      "incomplete_value": false,
      "site": "00bcf0b0",
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
            "const:27d:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcf064",
      "READ",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcf0f4",
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      "00bcf0f8",
      "DATA",
      [
        "storage",
        "00bd482c",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcf064",
      "READ",
      [
        "storage",
        "011268b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcf0f4",
      "READ",
      [
        "storage",
        "00c9baf0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcf0f8",
      "DATA",
      [
        "storage",
        "00bd48c8",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcefe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcef18.md#insn-00bcefe0) · [`00bcf07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcef18.md#insn-00bcf07c) · [`00bcf0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcef18.md#insn-00bcf0b0)
- 新版 [`00bcf07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bcefb4.md#insn-00bcf07c) · [`00bcf118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bcefb4.md#insn-00bcf118) · [`00bcf14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bcefb4.md#insn-00bcf14c)

~~~diff
- 00bcefe0 ["INT_ADD", "register:40f0:8", ["const:bcefe0:8", "const:4:8"]]
- 00bcefe0 ["CALL", null, ["callee:00497874:8"]]
+ 00bcf07c ["INT_ADD", "register:40f0:8", ["const:bcf07c:8", "const:4:8"]]
+ 00bcf07c ["CALL", null, ["callee:00497874:8"]]
- 00bcefe0 bytes 1522e397
+ 00bcf07c bytes fe21e397
- 00bcf07c ["INT_ADD", "register:40f0:8", ["const:bcf07c:8", "const:4:8"]]
- 00bcf07c ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bcf118 ["INT_ADD", "register:40f0:8", ["const:bcf118:8", "const:4:8"]]
+ 00bcf118 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bcf07c bytes 612f0294
+ 00bcf118 bytes 6e2f0294
- 00bcf0b0 ["INT_ADD", "register:40f0:8", ["const:bcf0b0:8", "const:4:8"]]
- 00bcf0b0 ["CALL", null, ["callee:00c5dc90:8"]]
+ 00bcf14c ["INT_ADD", "register:40f0:8", ["const:bcf14c:8", "const:4:8"]]
+ 00bcf14c ["CALL", null, ["callee:00c5dc90:8"]]
- 00bcf0b0 bytes c43a0294
+ 00bcf14c bytes d13a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cf31f5128fe9d49b93639d7c6bd45c3"></a>

### [`00bcf1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf1a4.md) → [`00bcf240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf240.md) _ZN8firebase4auth4Auth12current_userEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aa30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa30.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa40.md)
- 新版 呼出元 1件 [`00c5ab00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab00.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 11件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcf29c",
      "incomplete_value": true,
      "site": "00bcf2bc",
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
      "definition_site": "00bcf200",
      "incomplete_value": true,
      "site": "00bcf220",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcf2dc",
      "incomplete_value": true,
      "site": "00bcf2fc",
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
      "definition_site": "00bcf240",
      "incomplete_value": true,
      "site": "00bcf260",
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf1bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcf1bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcf288"
      ]
    ],
    [
      "00bcf28c",
      "READ",
      [
        "storage",
        "00c9b9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcf2bc",
      "DATA",
      [
        "storage",
        "00c928a8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00bcf258",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcf288"
      ]
    ],
    [
      "00bcf28c",
      "READ",
      [
        "storage",
        "00c9ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00bcf2bc",
      "DATA",
      [
        "storage",
        "00c92978",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf1a4.md#insn-00bcf1bc) · [`00bcf1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf1a4.md#insn-00bcf1cc)
- 新版 [`00bcf258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf240.md#insn-00bcf258) · [`00bcf268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf240.md#insn-00bcf268)

~~~diff
- 00bcf1bc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bcf1bc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bcf1bc bytes 890100b4
+ 00bcf258 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bcf258 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bcf258 bytes 890100b4
- 00bcf1cc ["INT_ADD", "register:40f0:8", ["const:bcf1cc:8", "const:4:8"]]
- 00bcf1cc ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bcf268 ["INT_ADD", "register:40f0:8", ["const:bcf268:8", "const:4:8"]]
+ 00bcf268 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bcf1cc bytes 0d2e0294
+ 00bcf268 bytes 1a2e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f39272c445f846a3ba921f11586315e"></a>

### [`00bcf418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf418.md) → [`00bcf4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf4b4.md) _ZN8firebase4auth4Auth7SignOutEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aa20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa20.md) · 呼出先 6件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 1件 [`00c5aaf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aaf0.md) · 呼出先 6件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf41c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf41c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcf418",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcf41c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcf420",
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
      "00bcf4b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcf4b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcf4bc",
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

- 旧版 [`00bcf418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf418.md#insn-00bcf418) · [`00bcf41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf418.md#insn-00bcf41c) · [`00bcf420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf418.md#insn-00bcf420)

~~~diff
- 00bcf418 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bcf418 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcf418 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcf418 bytes f50f1df8
- 00bcf41c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcf41c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcf41c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcf41c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcf41c bytes f44f01a9
- 00bcf420 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcf420 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcf420 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcf420 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcf420 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15fb258644491028e5ffa2839127b4c4"></a>

### [`00bcf4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf4b0.md) → [`00bcf54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf54c.md) _ZN8firebase4auth4Auth22SendPasswordResetEmailEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bd055c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd055c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.65% / 新版 80.65%

CFGの説明率　旧版 4.17% / 新版 4.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf4e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcf580"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf598",
      "incomplete_value": true,
      "site": "00bcf59c",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": {
      "definition_site": "00bcf4fc",
      "incomplete_value": true,
      "site": "00bcf500",
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
            "const:10:8"
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
      "unmatched:00bcf4e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcf530",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b150"
      ]
    ],
    [
      "00bcf5ec",
      "READ",
      [
        "storage",
        "011267c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcf580",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bcf5cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b150"
      ]
    ],
    [
      "00bcf5ec",
      "READ",
      [
        "storage",
        "011268c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf4b0.md#insn-00bcf4e4) · [`00bcf500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf4b0.md#insn-00bcf500) · [`00bcf50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf4b0.md#insn-00bcf50c)
- 新版 [`00bcf59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf54c.md#insn-00bcf59c) · [`00bcf5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf54c.md#insn-00bcf5a8)

~~~diff
- 00bcf4e4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00bcf4e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bcf4e4 bytes e82700f9
- 00bcf500 ["INT_ADD", "register:40f0:8", ["const:bcf500:8", "const:4:8"]]
- 00bcf500 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcf59c ["INT_ADD", "register:40f0:8", ["const:bcf59c:8", "const:4:8"]]
+ 00bcf59c ["CALL", null, ["callee:00c5af10:8"]]
- 00bcf500 bytes 502e0294
+ 00bcf59c bytes 5d2e0294
- 00bcf50c ["INT_ADD", "register:40f0:8", ["const:bcf50c:8", "const:4:8"]]
- 00bcf50c ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bcf5a8 ["INT_ADD", "register:40f0:8", ["const:bcf5a8:8", "const:4:8"]]
+ 00bcf5a8 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bcf50c bytes 3d2e0294
+ 00bcf5a8 bytes 4a2e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ebcba543615fb448df590bf8bffcf5b"></a>

### [`00bcf6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf6fc.md) → [`00bcf798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf798.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd00.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 1件 [`00c5ddd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ddd0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ae70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae70.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 20.00% / 新版 17.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf75c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcf7f8"
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
      "unmatched:00bcf79c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcf864"
      ]
    ]
  ],
  "added": [
    [
      "00bcf838",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcf864"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf6fc.md#insn-00bcf744) · [`00bcf75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf6fc.md#insn-00bcf75c) · [`00bcf770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf6fc.md#insn-00bcf770)
- 新版 [`00bcf7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf798.md#insn-00bcf7e0) · [`00bcf80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf798.md#insn-00bcf80c)

~~~diff
- 00bcf744 ["INT_ADD", "register:40f0:8", ["const:bcf744:8", "const:4:8"]]
- 00bcf744 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bcf7e0 ["INT_ADD", "register:40f0:8", ["const:bcf7e0:8", "const:4:8"]]
+ 00bcf7e0 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bcf744 bytes af2d0294
+ 00bcf7e0 bytes bc2d0294
- 00bcf75c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bcf75c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bcf75c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bcf75c ["COPY", "register:4018:8", ["tmp:0:8"]]
- 00bcf75c bytes 4301899a
- 00bcf770 ["INT_ADD", "register:40f0:8", ["const:bcf770:8", "const:4:8"]]
- 00bcf770 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00bcf80c ["INT_ADD", "register:40f0:8", ["const:bcf80c:8", "const:4:8"]]
+ 00bcf80c ["CALL", null, ["callee:00c5ae70:8"]]
- 00bcf770 bytes 8c2d0294
+ 00bcf80c bytes 992d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1937ddb6f429ce3cf3deba08c038b2a"></a>

### [`00bcf800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf800.md) → [`00bcf89c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf89c.md) _ZN8firebase4auth4Auth11UseEmulatorENSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf8ec",
      "incomplete_value": true,
      "site": "00bcf900",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:888:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf850",
      "incomplete_value": true,
      "site": "00bcf864",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:788:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcf8ec",
      "READ",
      [
        "storage",
        "01126788",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcf8ec",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf800.md#insn-00bcf864) · [`00bcf830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf800.md#insn-00bcf830) · [`00bcf844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf800.md#insn-00bcf844)
- 新版 [`00bcf900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf89c.md#insn-00bcf900) · [`00bcf8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf89c.md#insn-00bcf8cc) · [`00bcf8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf89c.md#insn-00bcf8e0)

~~~diff
- 00bcf864 ["INT_ADD", "register:40f0:8", ["const:bcf864:8", "const:4:8"]]
- 00bcf864 ["CALL", null, ["callee:00574d2c:8"]]
+ 00bcf900 ["INT_ADD", "register:40f0:8", ["const:bcf900:8", "const:4:8"]]
+ 00bcf900 ["CALL", null, ["callee:00574d2c:8"]]
- 00bcf864 bytes 2295e697
+ 00bcf900 bytes 0b95e697
- 00bcf830 ["INT_ADD", "register:40f0:8", ["const:bcf830:8", "const:4:8"]]
- 00bcf830 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bcf8cc ["INT_ADD", "register:40f0:8", ["const:bcf8cc:8", "const:4:8"]]
+ 00bcf8cc ["CALL", null, ["callee:00c5b150:8"]]
- 00bcf830 bytes 142e0294
+ 00bcf8cc bytes 212e0294
- 00bcf844 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf844 ["INT_ADD", "register:40f0:8", ["const:bcf844:8", "const:4:8"]]
- 00bcf844 ["CALLIND", null, ["register:0:8"]]
+ 00bcf8e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcf8e0 ["INT_ADD", "register:40f0:8", ["const:bcf8e0:8", "const:4:8"]]
+ 00bcf8e0 ["CALLIND", null, ["register:0:8"]]
- 00bcf844 bytes 00013fd6
+ 00bcf8e0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

