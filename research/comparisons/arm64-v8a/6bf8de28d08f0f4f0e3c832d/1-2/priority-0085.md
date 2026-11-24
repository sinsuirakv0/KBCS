# v16.0.1 → v16.0.2 · 最優先の変更候補 (85)

[一覧の目次](README.md)

<a id="compare-2979a6f78e1756e3deff64c5ee48a24f"></a>

### [`00bd9390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9390.md) → [`00bd942c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd942c.md) _ZNK8firebase4auth10Credential8providerEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md) [`00c5b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9454",
      "incomplete_value": false,
      "site": "00bd9458",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd93b8",
      "incomplete_value": false,
      "site": "00bd93bc",
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
            "const:5d8:8"
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
      "definition_site": "00bd9470",
      "incomplete_value": true,
      "site": "00bd9478",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd93d4",
      "incomplete_value": true,
      "site": "00bd93dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a58:8"
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
      "00bd9454",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ],
    [
      "00bd9470",
      "READ",
      [
        "storage",
        "01126a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd9454",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      "00bd9470",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd93bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9390.md#insn-00bd93bc) · [`00bd93dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9390.md#insn-00bd93dc) · [`00bd93a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9390.md#insn-00bd93a8)
- 新版 [`00bd9458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd942c.md#insn-00bd9458) · [`00bd9478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd942c.md#insn-00bd9478) · [`00bd9444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd942c.md#insn-00bd9444)

~~~diff
- 00bd93bc ["INT_ADD", "register:40f0:8", ["const:bd93bc:8", "const:4:8"]]
- 00bd93bc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd9458 ["INT_ADD", "register:40f0:8", ["const:bd9458:8", "const:4:8"]]
+ 00bd9458 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd93bc bytes 11070294
+ 00bd9458 bytes 1e070294
- 00bd93dc ["INT_ADD", "register:40f0:8", ["const:bd93dc:8", "const:4:8"]]
- 00bd93dc ["CALL", null, ["callee:00497874:8"]]
+ 00bd9478 ["INT_ADD", "register:40f0:8", ["const:bd9478:8", "const:4:8"]]
+ 00bd9478 ["CALL", null, ["callee:00497874:8"]]
- 00bd93dc bytes 16f9e297
+ 00bd9478 bytes fff8e297
- 00bd93a8 ["INT_ADD", "register:40f0:8", ["const:bd93a8:8", "const:4:8"]]
- 00bd93a8 ["CALL", null, ["callee:00c5b330:8"]]
+ 00bd9444 ["INT_ADD", "register:40f0:8", ["const:bd9444:8", "const:4:8"]]
+ 00bd9444 ["CALL", null, ["callee:00c5b330:8"]]
- 00bd93a8 bytes ae070294
+ 00bd9444 bytes bb070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afcc5b29852334d2e7669e0c62ab8444"></a>

### [`00bd9424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9424.md) → [`00bd94c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd94c0.md) _ZN8firebase4auth17EmailAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.45% / 新版 93.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9518",
      "incomplete_value": false,
      "site": "00bd951c",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd947c",
      "incomplete_value": false,
      "site": "00bd9480",
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
            "const:5d8:8"
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
      "definition_site": "00bd955c",
      "incomplete_value": true,
      "site": "00bd9574",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd94c0",
      "incomplete_value": true,
      "site": "00bd94d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9560",
      "incomplete_value": true,
      "site": "00bd9574",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd94c4",
      "incomplete_value": true,
      "site": "00bd94d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a78:8"
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
      "00bd94fc",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9500",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd95f0"
      ]
    ],
    [
      "00bd9518",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd94fc",
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9500",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd968c"
      ]
    ],
    [
      "00bd9518",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9424.md#insn-00bd9480) · [`00bd94d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9424.md#insn-00bd94d8) · [`00bd9528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9424.md#insn-00bd9528)
- 新版 [`00bd951c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd94c0.md#insn-00bd951c) · [`00bd9574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd94c0.md#insn-00bd9574) · [`00bd95c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd94c0.md#insn-00bd95c4)

~~~diff
- 00bd9480 ["INT_ADD", "register:40f0:8", ["const:bd9480:8", "const:4:8"]]
- 00bd9480 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd951c ["INT_ADD", "register:40f0:8", ["const:bd951c:8", "const:4:8"]]
+ 00bd951c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9480 bytes e0060294
+ 00bd951c bytes ed060294
- 00bd94d8 ["INT_ADD", "register:40f0:8", ["const:bd94d8:8", "const:4:8"]]
- 00bd94d8 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bd9574 ["INT_ADD", "register:40f0:8", ["const:bd9574:8", "const:4:8"]]
+ 00bd9574 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bd94d8 bytes b2050294
+ 00bd9574 bytes bf050294
- 00bd9528 ["INT_ADD", "register:40f0:8", ["const:bd9528:8", "const:4:8"]]
- 00bd9528 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd95c4 ["INT_ADD", "register:40f0:8", ["const:bd95c4:8", "const:4:8"]]
+ 00bd95c4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9528 bytes b6060294
+ 00bd95c4 bytes c3060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3f0be6a4c7b0d733b1ef81de07a9b2f"></a>

### [`00bd9768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9768.md) → [`00bd9804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9804.md) _ZNK8firebase4auth19PhoneAuthCredential8sms_codeEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md) [`00c5b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9834",
      "incomplete_value": false,
      "site": "00bd9838",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9798",
      "incomplete_value": false,
      "site": "00bd979c",
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
            "const:5d8:8"
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
      "definition_site": "00bd984c",
      "incomplete_value": true,
      "site": "00bd9854",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd97b0",
      "incomplete_value": true,
      "site": "00bd97b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce8:8"
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
      "00bd9834",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ],
    [
      "00bd984c",
      "READ",
      [
        "storage",
        "01126ce8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd9834",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      "00bd984c",
      "READ",
      [
        "storage",
        "01126de8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9768.md#insn-00bd979c) · [`00bd97b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9768.md#insn-00bd97b8) · [`00bd9788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9768.md#insn-00bd9788)
- 新版 [`00bd9838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9804.md#insn-00bd9838) · [`00bd9854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9804.md#insn-00bd9854) · [`00bd9824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9804.md#insn-00bd9824)

~~~diff
- 00bd979c ["INT_ADD", "register:40f0:8", ["const:bd979c:8", "const:4:8"]]
- 00bd979c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd9838 ["INT_ADD", "register:40f0:8", ["const:bd9838:8", "const:4:8"]]
+ 00bd9838 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd979c bytes 19060294
+ 00bd9838 bytes 26060294
- 00bd97b8 ["INT_ADD", "register:40f0:8", ["const:bd97b8:8", "const:4:8"]]
- 00bd97b8 ["CALL", null, ["callee:00497874:8"]]
+ 00bd9854 ["INT_ADD", "register:40f0:8", ["const:bd9854:8", "const:4:8"]]
+ 00bd9854 ["CALL", null, ["callee:00497874:8"]]
- 00bd97b8 bytes 1ff8e297
+ 00bd9854 bytes 08f8e297
- 00bd9788 ["INT_ADD", "register:40f0:8", ["const:bd9788:8", "const:4:8"]]
- 00bd9788 ["CALL", null, ["callee:00c5b330:8"]]
+ 00bd9824 ["INT_ADD", "register:40f0:8", ["const:bd9824:8", "const:4:8"]]
+ 00bd9824 ["CALL", null, ["callee:00c5b330:8"]]
- 00bd9788 bytes b6060294
+ 00bd9824 bytes c3060294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10283807f6ac41f011c7eabafb003392"></a>

### [`00bd97f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd97f0.md) → [`00bd988c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd988c.md) _ZN8firebase4auth26InternalAuthResultProvider13GetCredentialEP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dda0.md) · 呼出先 3件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)
- 新版 呼出元 1件 [`00c5de70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de70.md) · 呼出先 3件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)

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
      "definition_site": "00bd98b8",
      "incomplete_value": false,
      "site": "00bd98bc",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd981c",
      "incomplete_value": false,
      "site": "00bd9820",
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
            "const:5d8:8"
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
      "00bd98b8",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd98b8",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd97f0.md#insn-00bd9820) · [`00bd980c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd97f0.md#insn-00bd980c) · [`00bd981c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd97f0.md#insn-00bd981c)
- 新版 [`00bd98bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd988c.md#insn-00bd98bc) · [`00bd98a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd988c.md#insn-00bd98a8) · [`00bd98b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd988c.md#insn-00bd98b8)

~~~diff
- 00bd9820 ["INT_ADD", "register:40f0:8", ["const:bd9820:8", "const:4:8"]]
- 00bd9820 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd98bc ["INT_ADD", "register:40f0:8", ["const:bd98bc:8", "const:4:8"]]
+ 00bd98bc ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9820 bytes f8050294
+ 00bd98bc bytes 05060294
- 00bd980c ["INT_ADD", "register:40f0:8", ["const:bd980c:8", "const:4:8"]]
- 00bd980c ["CALL", null, ["callee:00c5b330:8"]]
+ 00bd98a8 ["INT_ADD", "register:40f0:8", ["const:bd98a8:8", "const:4:8"]]
+ 00bd98a8 ["CALL", null, ["callee:00c5b330:8"]]
- 00bd980c bytes 95060294
+ 00bd98a8 bytes a2060294
- 00bd981c ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00bd981c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd981c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd981c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd98b8 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bd98b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd98b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd98b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd981c bytes 00601791
+ 00bd98b8 bytes 00241891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd0bd23c65e04c685eee6233807baf43"></a>

### [`00bd9880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9880.md) → [`00bd991c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd991c.md) _ZN8firebase4auth20FacebookAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.16% / 新版 89.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9958",
      "incomplete_value": false,
      "site": "00bd995c",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd98bc",
      "incomplete_value": false,
      "site": "00bd98c0",
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
            "const:5d8:8"
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
      "definition_site": "00bd9984",
      "incomplete_value": true,
      "site": "00bd9998",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd98e8",
      "incomplete_value": true,
      "site": "00bd98fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a88:8"
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
      "definition_site": "00bd9988",
      "incomplete_value": true,
      "site": "00bd9998",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd98ec",
      "incomplete_value": true,
      "site": "00bd98fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a98:8"
              ]
            ]
          ]
        ]
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
      "00bd993c",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9940",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd998c"
      ]
    ],
    [
      "00bd9958",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd993c",
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9940",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9a28"
      ]
    ],
    [
      "00bd9958",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd98c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9880.md#insn-00bd98c0) · [`00bd98fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9880.md#insn-00bd98fc) · [`00bd9944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9880.md#insn-00bd9944)
- 新版 [`00bd995c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd991c.md#insn-00bd995c) · [`00bd9998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd991c.md#insn-00bd9998) · [`00bd99e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd991c.md#insn-00bd99e0)

~~~diff
- 00bd98c0 ["INT_ADD", "register:40f0:8", ["const:bd98c0:8", "const:4:8"]]
- 00bd98c0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd995c ["INT_ADD", "register:40f0:8", ["const:bd995c:8", "const:4:8"]]
+ 00bd995c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd98c0 bytes d0050294
+ 00bd995c bytes dd050294
- 00bd98fc ["INT_ADD", "register:40f0:8", ["const:bd98fc:8", "const:4:8"]]
- 00bd98fc ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bd9998 ["INT_ADD", "register:40f0:8", ["const:bd9998:8", "const:4:8"]]
+ 00bd9998 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bd98fc bytes a9040294
+ 00bd9998 bytes b6040294
- 00bd9944 ["INT_ADD", "register:40f0:8", ["const:bd9944:8", "const:4:8"]]
- 00bd9944 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd99e0 ["INT_ADD", "register:40f0:8", ["const:bd99e0:8", "const:4:8"]]
+ 00bd99e0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9944 bytes af050294
+ 00bd99e0 bytes bc050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-997a363c5da70deda78e982065824a6b"></a>

### [`00bd99cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd99cc.md) → [`00bd9a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9a68.md) _ZN8firebase4auth18GitHubAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.16% / 新版 89.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9aa4",
      "incomplete_value": false,
      "site": "00bd9aa8",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9a08",
      "incomplete_value": false,
      "site": "00bd9a0c",
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
            "const:5d8:8"
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
      "definition_site": "00bd9ad0",
      "incomplete_value": true,
      "site": "00bd9ae4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9a34",
      "incomplete_value": true,
      "site": "00bd9a48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa8:8"
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
      "definition_site": "00bd9ad4",
      "incomplete_value": true,
      "site": "00bd9ae4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9a38",
      "incomplete_value": true,
      "site": "00bd9a48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
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
      "00bd9a88",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9a8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9ad8"
      ]
    ],
    [
      "00bd9aa4",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9a88",
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9a8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9b74"
      ]
    ],
    [
      "00bd9aa4",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd99cc.md#insn-00bd9a0c) · [`00bd9a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd99cc.md#insn-00bd9a48) · [`00bd9a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd99cc.md#insn-00bd9a90)
- 新版 [`00bd9aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9a68.md#insn-00bd9aa8) · [`00bd9ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9a68.md#insn-00bd9ae4) · [`00bd9b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9a68.md#insn-00bd9b2c)

~~~diff
- 00bd9a0c ["INT_ADD", "register:40f0:8", ["const:bd9a0c:8", "const:4:8"]]
- 00bd9a0c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd9aa8 ["INT_ADD", "register:40f0:8", ["const:bd9aa8:8", "const:4:8"]]
+ 00bd9aa8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9a0c bytes 7d050294
+ 00bd9aa8 bytes 8a050294
- 00bd9a48 ["INT_ADD", "register:40f0:8", ["const:bd9a48:8", "const:4:8"]]
- 00bd9a48 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bd9ae4 ["INT_ADD", "register:40f0:8", ["const:bd9ae4:8", "const:4:8"]]
+ 00bd9ae4 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bd9a48 bytes 56040294
+ 00bd9ae4 bytes 63040294
- 00bd9a90 ["INT_ADD", "register:40f0:8", ["const:bd9a90:8", "const:4:8"]]
- 00bd9a90 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd9b2c ["INT_ADD", "register:40f0:8", ["const:bd9b2c:8", "const:4:8"]]
+ 00bd9b2c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9a90 bytes 5c050294
+ 00bd9b2c bytes 69050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a6955e924c04520992af6e5c538ccf3"></a>

### [`00bd9b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9b18.md) → [`00bd9bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9bb4.md) _ZN8firebase4auth18GoogleAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9d0.md) · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 1件 [`00c5aaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aaa0.md) · 呼出先 6件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 38.89% / 新版 38.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9bf0",
      "incomplete_value": false,
      "site": "00bd9bf4",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9b54",
      "incomplete_value": false,
      "site": "00bd9b58",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9ba8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9bbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd9bcc",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9bd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9bb4"
      ]
    ],
    [
      "unmatched:00bd9b54",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9bcc",
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9bd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9c50"
      ]
    ],
    [
      "00bd9bf0",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9b18.md#insn-00bd9b58) · [`00bd9ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9b18.md#insn-00bd9ba8) · [`00bd9bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9b18.md#insn-00bd9bbc)
- 新版 [`00bd9bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9bb4.md#insn-00bd9bf4)

~~~diff
- 00bd9b58 ["INT_ADD", "register:40f0:8", ["const:bd9b58:8", "const:4:8"]]
- 00bd9b58 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd9bf4 ["INT_ADD", "register:40f0:8", ["const:bd9bf4:8", "const:4:8"]]
+ 00bd9bf4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9b58 bytes 2a050294
+ 00bd9bf4 bytes 37050294
- 00bd9ba8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd9ba8 ["INT_ADD", "register:40f0:8", ["const:bd9ba8:8", "const:4:8"]]
- 00bd9ba8 ["CALLIND", null, ["register:0:8"]]
- 00bd9ba8 bytes 00013fd6
- 00bd9bbc ["INT_ADD", "register:40f0:8", ["const:bd9bbc:8", "const:4:8"]]
- 00bd9bbc ["CALL", null, ["callee:00c5ad70:8"]]
- 00bd9bbc bytes 39040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc060bf1c038747f7422515e840ba9ba"></a>

### [`00bd9cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9cbc.md) → [`00bd9d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9d58.md) _ZN8firebase4auth21PlayGamesAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.16% / 新版 89.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9d94",
      "incomplete_value": false,
      "site": "00bd9d98",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9cf8",
      "incomplete_value": false,
      "site": "00bd9cfc",
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
            "const:5d8:8"
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
      "definition_site": "00bd9dc0",
      "incomplete_value": true,
      "site": "00bd9dd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9d24",
      "incomplete_value": true,
      "site": "00bd9d38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae8:8"
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
      "definition_site": "00bd9dc4",
      "incomplete_value": true,
      "site": "00bd9dd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9d28",
      "incomplete_value": true,
      "site": "00bd9d38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af8:8"
              ]
            ]
          ]
        ]
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
      "00bd9d78",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9d7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9dc8"
      ]
    ],
    [
      "00bd9d94",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9d78",
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9d7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9e64"
      ]
    ],
    [
      "00bd9d94",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9cbc.md#insn-00bd9cfc) · [`00bd9d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9cbc.md#insn-00bd9d38) · [`00bd9d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9cbc.md#insn-00bd9d80)
- 新版 [`00bd9d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9d58.md#insn-00bd9d98) · [`00bd9dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9d58.md#insn-00bd9dd4) · [`00bd9e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9d58.md#insn-00bd9e1c)

~~~diff
- 00bd9cfc ["INT_ADD", "register:40f0:8", ["const:bd9cfc:8", "const:4:8"]]
- 00bd9cfc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd9d98 ["INT_ADD", "register:40f0:8", ["const:bd9d98:8", "const:4:8"]]
+ 00bd9d98 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9cfc bytes c1040294
+ 00bd9d98 bytes ce040294
- 00bd9d38 ["INT_ADD", "register:40f0:8", ["const:bd9d38:8", "const:4:8"]]
- 00bd9d38 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bd9dd4 ["INT_ADD", "register:40f0:8", ["const:bd9dd4:8", "const:4:8"]]
+ 00bd9dd4 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bd9d38 bytes 9a030294
+ 00bd9dd4 bytes a7030294
- 00bd9d80 ["INT_ADD", "register:40f0:8", ["const:bd9d80:8", "const:4:8"]]
- 00bd9d80 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd9e1c ["INT_ADD", "register:40f0:8", ["const:bd9e1c:8", "const:4:8"]]
+ 00bd9e1c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9d80 bytes a0040294
+ 00bd9e1c bytes ad040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ae90df5865236a79f7d97f13acf3c59"></a>

### [`00bd9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9e08.md) → [`00bd9ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9ea4.md) _ZN8firebase4auth19TwitterAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.72% / 新版 90.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9ee8",
      "incomplete_value": false,
      "site": "00bd9eec",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9e4c",
      "incomplete_value": false,
      "site": "00bd9e50",
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
            "const:5d8:8"
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
      "definition_site": "00bd9f2c",
      "incomplete_value": true,
      "site": "00bd9f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9e90",
      "incomplete_value": true,
      "site": "00bd9ea8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b08:8"
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
      "definition_site": "00bd9f30",
      "incomplete_value": true,
      "site": "00bd9f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9e94",
      "incomplete_value": true,
      "site": "00bd9ea8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b18:8"
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
      "00bd9ecc",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9ed0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9f4c"
      ]
    ],
    [
      "00bd9ee8",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9ecc",
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd9ed0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd9fe8"
      ]
    ],
    [
      "00bd9ee8",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9e08.md#insn-00bd9e50) · [`00bd9ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9e08.md#insn-00bd9ea8) · [`00bd9f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9e08.md#insn-00bd9f04)
- 新版 [`00bd9eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9ea4.md#insn-00bd9eec) · [`00bd9f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9ea4.md#insn-00bd9f44) · [`00bd9fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9ea4.md#insn-00bd9fa0)

~~~diff
- 00bd9e50 ["INT_ADD", "register:40f0:8", ["const:bd9e50:8", "const:4:8"]]
- 00bd9e50 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd9eec ["INT_ADD", "register:40f0:8", ["const:bd9eec:8", "const:4:8"]]
+ 00bd9eec ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9e50 bytes 6c040294
+ 00bd9eec bytes 79040294
- 00bd9ea8 ["INT_ADD", "register:40f0:8", ["const:bd9ea8:8", "const:4:8"]]
- 00bd9ea8 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bd9f44 ["INT_ADD", "register:40f0:8", ["const:bd9f44:8", "const:4:8"]]
+ 00bd9f44 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bd9ea8 bytes 3e030294
+ 00bd9f44 bytes 4b030294
- 00bd9f04 ["INT_ADD", "register:40f0:8", ["const:bd9f04:8", "const:4:8"]]
- 00bd9f04 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd9fa0 ["INT_ADD", "register:40f0:8", ["const:bd9fa0:8", "const:4:8"]]
+ 00bd9fa0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9f04 bytes 3f040294
+ 00bd9fa0 bytes 4c040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7057d54edbfdb4e1483dfc4ebe271726"></a>

### [`00bd9f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9f8c.md) → [`00bda028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda028.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.04% / 新版 92.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda078",
      "incomplete_value": false,
      "site": "00bda07c",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9fdc",
      "incomplete_value": false,
      "site": "00bd9fe0",
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
            "const:5d8:8"
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
      "definition_site": "00bda0d4",
      "incomplete_value": true,
      "site": "00bda0f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda038",
      "incomplete_value": true,
      "site": "00bda054",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b28:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda0d8",
      "incomplete_value": true,
      "site": "00bda0f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda03c",
      "incomplete_value": true,
      "site": "00bda054",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bda05c",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bda060",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bda10c"
      ]
    ],
    [
      "00bda078",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda05c",
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bda060",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda1a8"
      ]
    ],
    [
      "00bda078",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9f8c.md#insn-00bd9fe0) · [`00bda054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9f8c.md#insn-00bda054) · [`00bda078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9f8c.md#insn-00bda078)
- 新版 [`00bda07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda028.md#insn-00bda07c) · [`00bda0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda028.md#insn-00bda0f0) · [`00bda114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda028.md#insn-00bda114)

~~~diff
- 00bd9fe0 ["INT_ADD", "register:40f0:8", ["const:bd9fe0:8", "const:4:8"]]
- 00bd9fe0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bda07c ["INT_ADD", "register:40f0:8", ["const:bda07c:8", "const:4:8"]]
+ 00bda07c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd9fe0 bytes 08040294
+ 00bda07c bytes 15040294
- 00bda054 ["INT_ADD", "register:40f0:8", ["const:bda054:8", "const:4:8"]]
- 00bda054 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bda0f0 ["INT_ADD", "register:40f0:8", ["const:bda0f0:8", "const:4:8"]]
+ 00bda0f0 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bda054 bytes d3020294
+ 00bda0f0 bytes e0020294
- 00bda078 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bda078 ["INT_ADD", "register:40f0:8", ["const:bda078:8", "const:4:8"]]
- 00bda078 ["CALLIND", null, ["register:0:8"]]
+ 00bda114 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bda114 ["INT_ADD", "register:40f0:8", ["const:bda114:8", "const:4:8"]]
+ 00bda114 ["CALLIND", null, ["register:0:8"]]
- 00bda078 bytes 00013fd6
+ 00bda114 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c615d5446040e0cb5b9940bf09b7936"></a>

### [`00bda150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda150.md) → [`00bda1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda1ec.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_S3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.89% / 新版 94.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda240",
      "incomplete_value": false,
      "site": "00bda244",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda1a4",
      "incomplete_value": false,
      "site": "00bda1a8",
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
            "const:5d8:8"
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
      "definition_site": "00bda29c",
      "incomplete_value": true,
      "site": "00bda2b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda200",
      "incomplete_value": true,
      "site": "00bda214",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b28:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda2a0",
      "incomplete_value": true,
      "site": "00bda2b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda204",
      "incomplete_value": true,
      "site": "00bda214",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bda220",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bda224",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bda2e4"
      ]
    ],
    [
      "00bda240",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda220",
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bda224",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda380"
      ]
    ],
    [
      "00bda240",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda150.md#insn-00bda1a4) · [`00bda1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda150.md#insn-00bda1a8) · [`00bda214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda150.md#insn-00bda214)
- 新版 [`00bda240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda1ec.md#insn-00bda240) · [`00bda244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda1ec.md#insn-00bda244) · [`00bda2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda1ec.md#insn-00bda2b0)

~~~diff
- 00bda1a4 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00bda1a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bda1a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bda1a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bda240 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda240 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda240 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda240 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bda1a4 bytes 00601791
+ 00bda240 bytes 00241891
- 00bda1a8 ["INT_ADD", "register:40f0:8", ["const:bda1a8:8", "const:4:8"]]
- 00bda1a8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bda244 ["INT_ADD", "register:40f0:8", ["const:bda244:8", "const:4:8"]]
+ 00bda244 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bda1a8 bytes 96030294
+ 00bda244 bytes a3030294
- 00bda214 ["INT_ADD", "register:40f0:8", ["const:bda214:8", "const:4:8"]]
- 00bda214 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bda2b0 ["INT_ADD", "register:40f0:8", ["const:bda2b0:8", "const:4:8"]]
+ 00bda2b0 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bda214 bytes 63020294
+ 00bda2b0 bytes 70020294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80fcfd40dc0ac36d14b2d592880c20a3"></a>

### [`00bda410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda410.md) → [`00bda4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda4ac.md) _ZN8firebase4auth22GameCenterAuthProvider13GetCredentialEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00bdc428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc428.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00bdc4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc4c4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.33% / 新版 93.33%

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
      "definition_site": "00bda4f4",
      "incomplete_value": true,
      "site": "00bda508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda458",
      "incomplete_value": true,
      "site": "00bda46c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bda470",
      "incomplete_value": true,
      "site": "00bda478",
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
            "const:18:8"
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
      "definition_site": "00bda518",
      "incomplete_value": true,
      "site": "00bda51c",
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
            "const:28:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bda4f4",
      "READ",
      [
        "storage",
        "00c9ba30",
        null,
        "pointer"
      ]
    ],
    [
      "00bda4f4",
      "PARAM",
      [
        "storage",
        "00bdc428",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      "unmatched:00bda494",
      "PARAM",
      [
        "storage",
        "002b9cf0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda4f4",
      "READ",
      [
        "storage",
        "00c9bb00",
        null,
        "pointer"
      ]
    ],
    [
      "00bda4f4",
      "PARAM",
      [
        "storage",
        "00bdc4c4",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      "00bda530",
      "PARAM",
      [
        "storage",
        "002b9c9c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda410.md#insn-00bda46c) · [`00bda478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda410.md#insn-00bda478) · [`00bda480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda410.md#insn-00bda480)
- 新版 [`00bda508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda4ac.md#insn-00bda508) · [`00bda514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda4ac.md#insn-00bda514) · [`00bda51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda4ac.md#insn-00bda51c)

~~~diff
- 00bda46c ["INT_ADD", "register:40f0:8", ["const:bda46c:8", "const:4:8"]]
- 00bda46c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bda508 ["INT_ADD", "register:40f0:8", ["const:bda508:8", "const:4:8"]]
+ 00bda508 ["CALL", null, ["callee:00c5af10:8"]]
- 00bda46c bytes 75020294
+ 00bda508 bytes 82020294
- 00bda478 ["INT_ADD", "register:40f0:8", ["const:bda478:8", "const:4:8"]]
- 00bda478 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bda514 ["INT_ADD", "register:40f0:8", ["const:bda514:8", "const:4:8"]]
+ 00bda514 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bda478 bytes 62020294
+ 00bda514 bytes 6f020294
- 00bda480 ["INT_ADD", "register:40f0:8", ["const:bda480:8", "const:4:8"]]
- 00bda480 ["CALL", null, ["callee:00c5ab60:8"]]
+ 00bda51c ["INT_ADD", "register:40f0:8", ["const:bda51c:8", "const:4:8"]]
+ 00bda51c ["CALL", null, ["callee:00c5ab60:8"]]
- 00bda480 bytes 84010294
+ 00bda51c bytes 91010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fc131952fcbbe3f3da205cacfe983e5"></a>

### [`00bda658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda658.md) → [`00bda6f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda6f4.md) _ZN8firebase4auth22GameCenterAuthProvider21IsPlayerAuthenticatedEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda700",
      "incomplete_value": false,
      "site": "00bda704",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda664",
      "incomplete_value": false,
      "site": "00bda668",
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
            "const:927:8"
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
      "00bda700",
      "PARAM",
      [
        "storage",
        "002b4927",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda700",
      "PARAM",
      [
        "storage",
        "002b4958",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda658.md#insn-00bda668) · [`00bda664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda658.md#insn-00bda664)
- 新版 [`00bda704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda6f4.md#insn-00bda704) · [`00bda700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda6f4.md#insn-00bda700)

~~~diff
- 00bda668 ["INT_ADD", "register:40f0:8", ["const:bda668:8", "const:4:8"]]
- 00bda668 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bda704 ["INT_ADD", "register:40f0:8", ["const:bda704:8", "const:4:8"]]
+ 00bda704 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bda668 bytes 66020294
+ 00bda704 bytes 73020294
- 00bda664 ["COPY", "tmp:0:8", ["const:927:8"]]
- 00bda664 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bda664 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bda664 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bda700 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00bda700 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda700 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda700 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bda664 bytes 009c2491
+ 00bda700 bytes 00602591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dd2612c39d0a75fe3dd1ee6fb47fdb2"></a>

### [`00bda6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda6a4.md) → [`00bda740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda740.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda76c",
      "incomplete_value": false,
      "site": "00bda770",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda6d0",
      "incomplete_value": false,
      "site": "00bda6d4",
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
            "const:5d8:8"
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
      "00bda76c",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda76c",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda6a4.md#insn-00bda6d4) · [`00bda6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda6a4.md#insn-00bda6c0) · [`00bda6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda6a4.md#insn-00bda6d0)
- 新版 [`00bda770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda740.md#insn-00bda770) · [`00bda75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda740.md#insn-00bda75c) · [`00bda76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda740.md#insn-00bda76c)

~~~diff
- 00bda6d4 ["INT_ADD", "register:40f0:8", ["const:bda6d4:8", "const:4:8"]]
- 00bda6d4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bda770 ["INT_ADD", "register:40f0:8", ["const:bda770:8", "const:4:8"]]
+ 00bda770 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bda6d4 bytes 4b020294
+ 00bda770 bytes 58020294
- 00bda6c0 ["INT_ADD", "register:40f0:8", ["const:bda6c0:8", "const:4:8"]]
- 00bda6c0 ["CALL", null, ["callee:00c5b330:8"]]
+ 00bda75c ["INT_ADD", "register:40f0:8", ["const:bda75c:8", "const:4:8"]]
+ 00bda75c ["CALL", null, ["callee:00c5b330:8"]]
- 00bda6c0 bytes e8020294
+ 00bda75c bytes f5020294
- 00bda6d0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00bda6d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bda6d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bda6d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bda76c ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda76c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda76c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda76c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bda6d0 bytes 00601791
+ 00bda76c bytes 00241891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fbc17049fcf638456fc095d0ae04cf8"></a>

### [`00bda748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda748.md) → [`00bda7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda7e4.md) _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5de40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de40.md) · 呼出先 3件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)
- 新版 呼出元 1件 [`00c5df10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df10.md) · 呼出先 3件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda814",
      "incomplete_value": false,
      "site": "00bda818",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda778",
      "incomplete_value": false,
      "site": "00bda77c",
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
            "const:5d8:8"
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
      "definition_site": "00bda848",
      "incomplete_value": false,
      "site": "00bda84c",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda7ac",
      "incomplete_value": false,
      "site": "00bda7b0",
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
            "const:5d8:8"
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
      "00bda814",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ],
    [
      "00bda848",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda814",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      "00bda848",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda748.md#insn-00bda77c) · [`00bda7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda748.md#insn-00bda7b0) · [`00bda768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda748.md#insn-00bda768)
- 新版 [`00bda818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda7e4.md#insn-00bda818) · [`00bda84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda7e4.md#insn-00bda84c) · [`00bda804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda7e4.md#insn-00bda804)

~~~diff
- 00bda77c ["INT_ADD", "register:40f0:8", ["const:bda77c:8", "const:4:8"]]
- 00bda77c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bda818 ["INT_ADD", "register:40f0:8", ["const:bda818:8", "const:4:8"]]
+ 00bda818 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bda77c bytes 21020294
+ 00bda818 bytes 2e020294
- 00bda7b0 ["INT_ADD", "register:40f0:8", ["const:bda7b0:8", "const:4:8"]]
- 00bda7b0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bda84c ["INT_ADD", "register:40f0:8", ["const:bda84c:8", "const:4:8"]]
+ 00bda84c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bda7b0 bytes 14020294
+ 00bda84c bytes 21020294
- 00bda768 ["INT_ADD", "register:40f0:8", ["const:bda768:8", "const:4:8"]]
- 00bda768 ["CALL", null, ["callee:00c5b330:8"]]
+ 00bda804 ["INT_ADD", "register:40f0:8", ["const:bda804:8", "const:4:8"]]
+ 00bda804 ["CALL", null, ["callee:00c5b330:8"]]
- 00bda768 bytes be020294
+ 00bda804 bytes cb020294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-889929471d0fb1d57e8b9b597e9c321c"></a>

### [`00bda81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda81c.md) → [`00bda8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda8b8.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokeneqERKS2_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda8e0",
      "incomplete_value": false,
      "site": "00bda8e4",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda844",
      "incomplete_value": false,
      "site": "00bda848",
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
            "const:5d8:8"
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
      "00bda8e0",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda8e0",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda81c.md#insn-00bda848) · [`00bda834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda81c.md#insn-00bda834) · [`00bda844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda81c.md#insn-00bda844)
- 新版 [`00bda8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda8b8.md#insn-00bda8e4) · [`00bda8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda8b8.md#insn-00bda8d0) · [`00bda8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda8b8.md#insn-00bda8e0)

~~~diff
- 00bda848 ["INT_ADD", "register:40f0:8", ["const:bda848:8", "const:4:8"]]
- 00bda848 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bda8e4 ["INT_ADD", "register:40f0:8", ["const:bda8e4:8", "const:4:8"]]
+ 00bda8e4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bda848 bytes ee010294
+ 00bda8e4 bytes fb010294
- 00bda834 ["INT_ADD", "register:40f0:8", ["const:bda834:8", "const:4:8"]]
- 00bda834 ["CALL", null, ["callee:00c5b330:8"]]
+ 00bda8d0 ["INT_ADD", "register:40f0:8", ["const:bda8d0:8", "const:4:8"]]
+ 00bda8d0 ["CALL", null, ["callee:00c5b330:8"]]
- 00bda834 bytes 8b020294
+ 00bda8d0 bytes 98020294
- 00bda844 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00bda844 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bda844 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bda844 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bda8e0 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda8e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda8e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda8e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bda844 bytes 00601791
+ 00bda8e0 bytes 00241891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a6f0a3cd7ab389f7f952030255ac270"></a>

### [`00bda888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda888.md) → [`00bda924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda924.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokenneERKS2_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda94c",
      "incomplete_value": false,
      "site": "00bda950",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda8b0",
      "incomplete_value": false,
      "site": "00bda8b4",
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
            "const:5d8:8"
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
      "00bda94c",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda94c",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda888.md#insn-00bda8b4) · [`00bda8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda888.md#insn-00bda8a0) · [`00bda8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda888.md#insn-00bda8b0)
- 新版 [`00bda950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda924.md#insn-00bda950) · [`00bda93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda924.md#insn-00bda93c) · [`00bda94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda924.md#insn-00bda94c)

~~~diff
- 00bda8b4 ["INT_ADD", "register:40f0:8", ["const:bda8b4:8", "const:4:8"]]
- 00bda8b4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bda950 ["INT_ADD", "register:40f0:8", ["const:bda950:8", "const:4:8"]]
+ 00bda950 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bda8b4 bytes d3010294
+ 00bda950 bytes e0010294
- 00bda8a0 ["INT_ADD", "register:40f0:8", ["const:bda8a0:8", "const:4:8"]]
- 00bda8a0 ["CALL", null, ["callee:00c5b330:8"]]
+ 00bda93c ["INT_ADD", "register:40f0:8", ["const:bda93c:8", "const:4:8"]]
+ 00bda93c ["CALL", null, ["callee:00c5b330:8"]]
- 00bda8a0 bytes 70020294
+ 00bda93c bytes 7d020294
- 00bda8b0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00bda8b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bda8b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bda8b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bda94c ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda94c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda94c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda94c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bda8b0 bytes 00601791
+ 00bda94c bytes 00241891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5769fff52042665a134417717b7df6f1"></a>

### [`00bda8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda8fc.md) → [`00bda998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda998.md) _ZN8firebase4auth17PhoneAuthProviderD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9c0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)
- 新版 呼出元 1件 [`00c5da90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da90.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda9c0",
      "incomplete_value": false,
      "site": "00bda9c4",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda924",
      "incomplete_value": false,
      "site": "00bda928",
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
            "const:5d8:8"
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
      "00bda9c0",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda9c0",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda8fc.md#insn-00bda928) · [`00bda914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda8fc.md#insn-00bda914) · [`00bda924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda8fc.md#insn-00bda924)
- 新版 [`00bda9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda998.md#insn-00bda9c4) · [`00bda9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda998.md#insn-00bda9b0) · [`00bda9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda998.md#insn-00bda9c0)

~~~diff
- 00bda928 ["INT_ADD", "register:40f0:8", ["const:bda928:8", "const:4:8"]]
- 00bda928 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bda9c4 ["INT_ADD", "register:40f0:8", ["const:bda9c4:8", "const:4:8"]]
+ 00bda9c4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bda928 bytes b6010294
+ 00bda9c4 bytes c3010294
- 00bda914 ["INT_ADD", "register:40f0:8", ["const:bda914:8", "const:4:8"]]
- 00bda914 ["CALL", null, ["callee:00c5b330:8"]]
+ 00bda9b0 ["INT_ADD", "register:40f0:8", ["const:bda9b0:8", "const:4:8"]]
+ 00bda9b0 ["CALL", null, ["callee:00c5b330:8"]]
- 00bda914 bytes 53020294
+ 00bda9b0 bytes 60020294
- 00bda924 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00bda924 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bda924 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bda924 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bda9c0 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda9c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda9c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda9c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bda924 bytes 00601791
+ 00bda9c0 bytes 00241891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0621cf1583934c137d8ff9f832bf4b3"></a>

### [`00bda96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda96c.md) → [`00bdaa08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdaa08.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerC2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bdaa20",
      "incomplete_value": true,
      "site": "00bdaa24",
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
      "definition_site": "00bda984",
      "incomplete_value": true,
      "site": "00bda988",
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
      "definition_site": "00bdaa48",
      "incomplete_value": false,
      "site": "00bdaa4c",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda9ac",
      "incomplete_value": false,
      "site": "00bda9b0",
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
            "const:5d8:8"
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
      "definition_site": "00bdaa60",
      "incomplete_value": true,
      "site": "00bdaa70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda9c4",
      "incomplete_value": true,
      "site": "00bda9d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
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
      "00bdaa18",
      "READ",
      [
        "storage",
        "00c9ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00bdaa24",
      "DATA",
      [
        "storage",
        "00c92540",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bdaa48",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdaa18",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bdaa24",
      "DATA",
      [
        "storage",
        "00c92610",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bdaa48",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda96c.md#insn-00bda9b0) · [`00bda9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda96c.md#insn-00bda9d4) · [`00bda97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda96c.md#insn-00bda97c)
- 新版 [`00bdaa4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdaa08.md#insn-00bdaa4c) · [`00bdaa70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdaa08.md#insn-00bdaa70) · [`00bdaa18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdaa08.md#insn-00bdaa18)

~~~diff
- 00bda9b0 ["INT_ADD", "register:40f0:8", ["const:bda9b0:8", "const:4:8"]]
- 00bda9b0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdaa4c ["INT_ADD", "register:40f0:8", ["const:bdaa4c:8", "const:4:8"]]
+ 00bdaa4c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bda9b0 bytes 94010294
+ 00bdaa4c bytes a1010294
- 00bda9d4 ["INT_ADD", "register:40f0:8", ["const:bda9d4:8", "const:4:8"]]
- 00bda9d4 ["CALL", null, ["callee:00589734:8"]]
+ 00bdaa70 ["INT_ADD", "register:40f0:8", ["const:bdaa70:8", "const:4:8"]]
+ 00bdaa70 ["CALL", null, ["callee:00589734:8"]]
- 00bda9d4 bytes 48bbe697
+ 00bdaa70 bytes 31bbe697
- 00bda97c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a40:8"]]
- 00bda97c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdaa18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b10:8"]]
+ 00bdaa18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bda97c bytes 082145f9
+ 00bdaa18 bytes 088945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80136b0fe66f254012d308ae01a71618"></a>

### [`00bdaa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa00.md) → [`00bdaa9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdaa9c.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bdaab4",
      "incomplete_value": true,
      "site": "00bdaab8",
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
      "definition_site": "00bdaa18",
      "incomplete_value": true,
      "site": "00bdaa1c",
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
      "definition_site": "00bdaacc",
      "incomplete_value": false,
      "site": "00bdaad0",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdaa30",
      "incomplete_value": false,
      "site": "00bdaa34",
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
            "const:5d8:8"
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
      "definition_site": "00bdaae4",
      "incomplete_value": true,
      "site": "00bdaaf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdaa48",
      "incomplete_value": true,
      "site": "00bdaa54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00bdaaac",
      "READ",
      [
        "storage",
        "00c9ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00bdaab8",
      "DATA",
      [
        "storage",
        "00c92540",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bdaacc",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdaaac",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bdaab8",
      "DATA",
      [
        "storage",
        "00c92610",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bdaacc",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaa34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa00.md#insn-00bdaa34) · [`00bdaa54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa00.md#insn-00bdaa54) · [`00bdaa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa00.md#insn-00bdaa10)
- 新版 [`00bdaad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdaa9c.md#insn-00bdaad0) · [`00bdaaf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdaa9c.md#insn-00bdaaf0) · [`00bdaaac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdaa9c.md#insn-00bdaaac)

~~~diff
- 00bdaa34 ["INT_ADD", "register:40f0:8", ["const:bdaa34:8", "const:4:8"]]
- 00bdaa34 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdaad0 ["INT_ADD", "register:40f0:8", ["const:bdaad0:8", "const:4:8"]]
+ 00bdaad0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdaa34 bytes 73010294
+ 00bdaad0 bytes 80010294
- 00bdaa54 ["INT_ADD", "register:40f0:8", ["const:bdaa54:8", "const:4:8"]]
- 00bdaa54 ["CALL", null, ["callee:00574d2c:8"]]
+ 00bdaaf0 ["INT_ADD", "register:40f0:8", ["const:bdaaf0:8", "const:4:8"]]
+ 00bdaaf0 ["CALL", null, ["callee:00574d2c:8"]]
- 00bdaa54 bytes a668e697
+ 00bdaaf0 bytes 8f68e697
- 00bdaa10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a40:8"]]
- 00bdaa10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdaaac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b10:8"]]
+ 00bdaaac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdaa10 bytes 082145f9
+ 00bdaaac bytes 088945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd02f62357f11688b2db9237fc938cc9"></a>

### [`00bdaa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa98.md) → [`00bdab34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdab34.md) _ZN8firebase4auth17PhoneAuthProvider17VerifyPhoneNumberERKNS0_16PhoneAuthOptionsEPNS1_8ListenerE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.85% / 新版 95.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件

アドレスに依存する影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdaba0",
      "incomplete_value": true,
      "site": "00bdabb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdab04",
      "incomplete_value": true,
      "site": "00bdab1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b78:8"
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
      "definition_site": "00bdabac",
      "incomplete_value": true,
      "site": "00bdabb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdab10",
      "incomplete_value": true,
      "site": "00bdab1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b88:8"
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
      "definition_site": "00bdabd0",
      "incomplete_value": false,
      "site": "00bdabd8",
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
            "const:8c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdab34",
      "incomplete_value": false,
      "site": "00bdab3c",
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
            "const:91d:8"
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
      "00bdaba0",
      "READ",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdabac",
      "READ",
      [
        "storage",
        "01126b88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdabd0",
      "PARAM",
      [
        "storage",
        "002be91d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdaba0",
      "READ",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdabac",
      "READ",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdabd0",
      "PARAM",
      [
        "storage",
        "002be8c9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdab1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa98.md#insn-00bdab1c) · [`00bdab3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa98.md#insn-00bdab3c) · [`00bdab50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa98.md#insn-00bdab50)
- 新版 [`00bdabb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdab34.md#insn-00bdabb8) · [`00bdabd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdab34.md#insn-00bdabd8) · [`00bdabec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdab34.md#insn-00bdabec)

~~~diff
- 00bdab1c ["INT_ADD", "register:40f0:8", ["const:bdab1c:8", "const:4:8"]]
- 00bdab1c ["CALL", null, ["callee:00589734:8"]]
+ 00bdabb8 ["INT_ADD", "register:40f0:8", ["const:bdabb8:8", "const:4:8"]]
+ 00bdabb8 ["CALL", null, ["callee:00589734:8"]]
- 00bdab1c bytes f6bae697
+ 00bdabb8 bytes dfbae697
- 00bdab3c ["INT_ADD", "register:40f0:8", ["const:bdab3c:8", "const:4:8"]]
- 00bdab3c ["CALL", null, ["callee:00c5b690:8"]]
+ 00bdabd8 ["INT_ADD", "register:40f0:8", ["const:bdabd8:8", "const:4:8"]]
+ 00bdabd8 ["CALL", null, ["callee:00c5b690:8"]]
- 00bdab3c bytes a1020294
+ 00bdabd8 bytes ae020294
- 00bdab50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdab50 ["INT_ADD", "register:40f0:8", ["const:bdab50:8", "const:4:8"]]
- 00bdab50 ["CALLIND", null, ["register:0:8"]]
+ 00bdabec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdabec ["INT_ADD", "register:40f0:8", ["const:bdabec:8", "const:4:8"]]
+ 00bdabec ["CALLIND", null, ["register:0:8"]]
- 00bdab50 bytes 00013fd6
+ 00bdabec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce965b8d02b71b24c11f49b8e145b863"></a>

### [`00bdafb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdafb8.md) → [`00bdb054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb054.md) _ZN8firebase4auth17PhoneAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.58% / 新版 91.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb0cc",
      "incomplete_value": true,
      "site": "00bdb0e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdb030",
      "incomplete_value": true,
      "site": "00bdb048",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
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
      "definition_site": "00bdb0d0",
      "incomplete_value": true,
      "site": "00bdb0e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdb034",
      "incomplete_value": true,
      "site": "00bdb048",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
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
      "definition_site": "00bdb13c",
      "incomplete_value": false,
      "site": "00bdb140",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdb0a0",
      "incomplete_value": false,
      "site": "00bdb0a4",
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
            "const:5d8:8"
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
      "00bdb07c",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdb080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bdb104"
      ]
    ],
    [
      "00bdb0cc",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdb07c",
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdb080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdb1a0"
      ]
    ],
    [
      "00bdb0cc",
      "READ",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdafb8.md#insn-00bdb048) · [`00bdb0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdafb8.md#insn-00bdb0a4) · [`00bdb10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdafb8.md#insn-00bdb10c)
- 新版 [`00bdb0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb054.md#insn-00bdb0e4) · [`00bdb140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb054.md#insn-00bdb140) · [`00bdb1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb054.md#insn-00bdb1a8)

~~~diff
- 00bdb048 ["INT_ADD", "register:40f0:8", ["const:bdb048:8", "const:4:8"]]
- 00bdb048 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bdb0e4 ["INT_ADD", "register:40f0:8", ["const:bdb0e4:8", "const:4:8"]]
+ 00bdb0e4 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bdb048 bytes d6fe0194
+ 00bdb0e4 bytes e3fe0194
- 00bdb0a4 ["INT_ADD", "register:40f0:8", ["const:bdb0a4:8", "const:4:8"]]
- 00bdb0a4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdb140 ["INT_ADD", "register:40f0:8", ["const:bdb140:8", "const:4:8"]]
+ 00bdb140 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdb0a4 bytes d7ff0194
+ 00bdb140 bytes e4ff0194
- 00bdb10c ["INT_ADD", "register:40f0:8", ["const:bdb10c:8", "const:4:8"]]
- 00bdb10c ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bdb1a8 ["INT_ADD", "register:40f0:8", ["const:bdb1a8:8", "const:4:8"]]
+ 00bdb1a8 ["CALL", null, ["callee:00c5ad70:8"]]
- 00bdb10c bytes e5fe0194
+ 00bdb1a8 bytes f2fe0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0b3d3a059af46faa8968a9f0e31ecc5"></a>

### [`00bdb1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb1d4.md) → [`00bdb270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb270.md) _ZN8firebase4auth20JniAuthPhoneListener29nativeOnVerificationCompletedEP7_JNIEnvP8_jobjectlS5_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb2b0",
      "incomplete_value": false,
      "site": "00bdb2b4",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdb214",
      "incomplete_value": false,
      "site": "00bdb218",
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
            "const:5d8:8"
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
      "00bdb2b0",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdb2b0",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb1d4.md#insn-00bdb218) · [`00bdb204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb1d4.md#insn-00bdb204) · [`00bdb214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb1d4.md#insn-00bdb214)
- 新版 [`00bdb2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb270.md#insn-00bdb2b4) · [`00bdb2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb270.md#insn-00bdb2a0) · [`00bdb2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb270.md#insn-00bdb2b0)

~~~diff
- 00bdb218 ["INT_ADD", "register:40f0:8", ["const:bdb218:8", "const:4:8"]]
- 00bdb218 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdb2b4 ["INT_ADD", "register:40f0:8", ["const:bdb2b4:8", "const:4:8"]]
+ 00bdb2b4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdb218 bytes 7aff0194
+ 00bdb2b4 bytes 87ff0194
- 00bdb204 ["INT_ADD", "register:40f0:8", ["const:bdb204:8", "const:4:8"]]
- 00bdb204 ["CALL", null, ["callee:00c5b330:8"]]
+ 00bdb2a0 ["INT_ADD", "register:40f0:8", ["const:bdb2a0:8", "const:4:8"]]
+ 00bdb2a0 ["CALL", null, ["callee:00c5b330:8"]]
- 00bdb204 bytes 17000294
+ 00bdb2a0 bytes 24000294
- 00bdb214 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00bdb214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdb214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdb214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdb2b0 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdb2b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdb2b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdb2b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdb214 bytes 00601791
+ 00bdb2b0 bytes 00241891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64837d61c013acb4e082efc2052bb54b"></a>

### [`00bdb370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb370.md) → [`00bdb40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb40c.md) _ZN8firebase4auth20JniAuthPhoneListener16nativeOnCodeSentEP7_JNIEnvP8_jobjectlP8_jstringS5_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.41% / 新版 98.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb4b4",
      "incomplete_value": false,
      "site": "00bdb4b8",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdb418",
      "incomplete_value": false,
      "site": "00bdb41c",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdb4b4",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdb4b4",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb370.md#insn-00bdb41c) · [`00bdb3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb370.md#insn-00bdb3a8) · [`00bdb3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb370.md#insn-00bdb3bc)
- 新版 [`00bdb4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb40c.md#insn-00bdb4b8) · [`00bdb444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb40c.md#insn-00bdb444) · [`00bdb458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb40c.md#insn-00bdb458)

~~~diff
- 00bdb41c ["INT_ADD", "register:40f0:8", ["const:bdb41c:8", "const:4:8"]]
- 00bdb41c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdb4b8 ["INT_ADD", "register:40f0:8", ["const:bdb4b8:8", "const:4:8"]]
+ 00bdb4b8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdb41c bytes f9fe0194
+ 00bdb4b8 bytes 06ff0194
- 00bdb3a8 ["INT_ADD", "register:40f0:8", ["const:bdb3a8:8", "const:4:8"]]
- 00bdb3a8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bdb444 ["INT_ADD", "register:40f0:8", ["const:bdb444:8", "const:4:8"]]
+ 00bdb444 ["CALL", null, ["callee:00c57f60:8"]]
- 00bdb3a8 bytes baf20194
+ 00bdb444 bytes c7f20194
- 00bdb3bc ["INT_ADD", "register:40f0:8", ["const:bdb3bc:8", "const:4:8"]]
- 00bdb3bc ["CALL", null, ["callee:00c5df10:8"]]
+ 00bdb458 ["INT_ADD", "register:40f0:8", ["const:bdb458:8", "const:4:8"]]
+ 00bdb458 ["CALL", null, ["callee:00c5df10:8"]]
- 00bdb3bc bytes a10a0294
+ 00bdb458 bytes ae0a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c241908a889daae2bb0053c694ce0368"></a>

### [`00bdb6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb6d8.md) → [`00bdb774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb774.md) _ZN8firebase4auth22FederatedOAuthProviderD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 77.78% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb6fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdb798"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb78c",
      "incomplete_value": true,
      "site": "00bdb79c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:40:8"
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
      "00bdb788",
      "READ",
      [
        "storage",
        "00c9ba48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb6fc",
      "DATA",
      [
        "storage",
        "00c92580",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00bdb788",
      "READ",
      [
        "storage",
        "00c9bb18",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb798",
      "DATA",
      [
        "storage",
        "00c92650",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb6d8.md#insn-00bdb6fc) · [`00bdb700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb6d8.md#insn-00bdb700)
- 新版 [`00bdb79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb774.md#insn-00bdb79c) · [`00bdb798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb774.md#insn-00bdb798)

~~~diff
- 00bdb6fc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bdb6fc ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00bdb6fc ["INT_ADD", "register:4000:8", ["register:4000:8", "const:38:8"]]
- 00bdb6fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bdb6fc bytes 088403f8
- 00bdb700 ["INT_ADD", "register:40f0:8", ["const:bdb700:8", "const:4:8"]]
- 00bdb700 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00bdb79c ["INT_ADD", "register:40f0:8", ["const:bdb79c:8", "const:4:8"]]
+ 00bdb79c ["CALL", null, ["callee:0046d4d0:8"]]
- 00bdb700 bytes 6447e297
+ 00bdb79c bytes 4d47e297
+ 00bdb798 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00bdb798 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00bdb798 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:38:8"]]
+ 00bdb798 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00bdb798 bytes 088403f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04641944be65ccf933575dd4eaa5e01d"></a>

### [`00bdb784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb784.md) → [`00bdb820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb820.md) _ZN8firebase4auth22FederatedOAuthProviderD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 88.24% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bdb844",
      "incomplete_value": true,
      "site": "00bdb844",
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
      "definition_site": "00bdb7a8",
      "incomplete_value": true,
      "site": "00bdb7a8",
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
      "00bdb834",
      "READ",
      [
        "storage",
        "00c9ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb844",
      "DATA",
      [
        "storage",
        "00c92580",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00bdb834",
      "READ",
      [
        "storage",
        "00c9bb18",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb844",
      "DATA",
      [
        "storage",
        "00c92650",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb784.md#insn-00bdb798) · [`00bdb7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb784.md#insn-00bdb7ac) · [`00bdb7e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb784.md#insn-00bdb7e8)
- 新版 [`00bdb834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb820.md#insn-00bdb834) · [`00bdb848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb820.md#insn-00bdb848) · [`00bdb884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb820.md#insn-00bdb884)

~~~diff
- 00bdb798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a48:8"]]
- 00bdb798 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdb834 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b18:8"]]
+ 00bdb834 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb798 bytes 082545f9
+ 00bdb834 bytes 088d45f9
- 00bdb7ac ["INT_ADD", "register:40f0:8", ["const:bdb7ac:8", "const:4:8"]]
- 00bdb7ac ["CALL", null, ["callee:0046d4d0:8"]]
+ 00bdb848 ["INT_ADD", "register:40f0:8", ["const:bdb848:8", "const:4:8"]]
+ 00bdb848 ["CALL", null, ["callee:0046d4d0:8"]]
- 00bdb7ac bytes 3947e297
+ 00bdb848 bytes 2247e297
- 00bdb7e8 ["INT_ADD", "register:40f0:8", ["const:bdb7e8:8", "const:4:8"]]
- 00bdb7e8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bdb884 ["INT_ADD", "register:40f0:8", ["const:bdb884:8", "const:4:8"]]
+ 00bdb884 ["CALL", null, ["callee:00c57f80:8"]]
- 00bdb7e8 bytes b2f10194
+ 00bdb884 bytes bff10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49f54567371e0b50b0587d4033aface3"></a>

### [`00bdb828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb828.md) → [`00bdb8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb8c4.md) _ZN8firebase4auth22FederatedOAuthProvider15SetProviderDataERKNS0_26FederatedOAuthProviderDataE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b77c.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d030.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053b7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b7bc.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5d100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d100.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 70.37% / 新版 70.37%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb840"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb858"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb85c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb840",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdb924"
      ]
    ]
  ],
  "added": [
    [
      "00bdb8dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdb924"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb828.md#insn-00bdb840) · [`00bdb858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb828.md#insn-00bdb858) · [`00bdb85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb828.md#insn-00bdb85c)

~~~diff
- 00bdb840 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bdb840 bytes 40020054
- 00bdb858 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdb858 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bdb858 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bdb858 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00bdb858 bytes 2115819a
- 00bdb85c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00bdb85c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bdb85c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bdb85c ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00bdb85c bytes 62018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2f4a80fe12594da98cae346b8a2c8d2"></a>

### [`00bdb894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb894.md) → [`00bdb930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb930.md) _ZN8firebase4auth22FederatedOAuthProvider6SignInEPNS0_8AuthDataE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00bdbc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbc38.md) [`00bdcb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcb7c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bd48c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd48c8.md) [`00bdbcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbcd4.md) [`00bdcc18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcc18.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 75.00% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb898"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb898"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb89c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb898",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdb89c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdb8a0",
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
      "00bdb934",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bdb938",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bdb93c",
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

- 旧版 [`00bdb898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb894.md#insn-00bdb898) · [`00bdb89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb894.md#insn-00bdb89c) · [`00bdb8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb894.md#insn-00bdb8a0)

~~~diff
- 00bdb898 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bdb898 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bdb898 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 00bdb898 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdb898 bytes fc6f17a9
- 00bdb89c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bdb89c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bdb89c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 00bdb89c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdb89c bytes fa6718a9
- 00bdb8a0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bdb8a0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bdb8a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 00bdb8a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdb8a0 bytes f85f19a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edcde6e52c0ebb00bf47ff2d9d12b466"></a>

### [`00bdbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbb6c.md) → [`00bdbc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbc08.md) _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEiRKS5_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5dde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dde0.md) · 呼出先 7件 [`00bcfcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 1件 [`00c5deb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5deb0.md) · 呼出先 7件 [`00bcfd74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfd74.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdbbf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bdbc8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bdbbc0",
      "incomplete_value": true,
      "site": "00bdbbcc",
      "value": [
        "live",
        "register:40a8:8"
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
      "00bdbc54",
      "READ",
      [
        "storage",
        "00c9b9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdbc54",
      "PARAM",
      [
        "storage",
        "00bcfcd8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ],
    [
      "unmatched:00bdbbf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdbca8"
      ]
    ]
  ],
  "added": [
    [
      "00bdbc54",
      "READ",
      [
        "storage",
        "00c9bab8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdbc54",
      "PARAM",
      [
        "storage",
        "00bcfd74",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ],
    [
      "00bdbc8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdbca8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdbbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbb6c.md#insn-00bdbbcc) · [`00bdbbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbb6c.md#insn-00bdbbf0) · [`00bdbc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbb6c.md#insn-00bdbc08)
- 新版 [`00bdbc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbc08.md#insn-00bdbc68)

~~~diff
- 00bdbbcc ["INT_ADD", "register:40f0:8", ["const:bdbbcc:8", "const:4:8"]]
- 00bdbbcc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdbc68 ["INT_ADD", "register:40f0:8", ["const:bdbc68:8", "const:4:8"]]
+ 00bdbc68 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdbbcc bytes 9dfc0194
+ 00bdbc68 bytes aafc0194
- 00bdbbf0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdbbf0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bdbbf0 bytes e1000054
- 00bdbc08 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bdbc08 ["RETURN", null, ["register:0:8"]]
- 00bdbc08 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f61f27b1b3d2d8dce3963656c63ec582"></a>

### [`00bdbc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbc38.md) → [`00bdbcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbcd4.md) FUN_00bdbcd4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00bdb894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb894.md) [`00bdbe78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbe78.md) [`00bdc150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc150.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5afb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afb0.md)
- 新版 呼出元 3件 [`00bdb930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb930.md) [`00bdbf14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbf14.md) [`00bdc1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc1ec.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5b080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdbd30",
      "incomplete_value": true,
      "site": "00bdbd48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdbc94",
      "incomplete_value": true,
      "site": "00bdbcac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b28:8"
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
      "definition_site": "00bdbd34",
      "incomplete_value": true,
      "site": "00bdbd48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdbc98",
      "incomplete_value": true,
      "site": "00bdbcac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
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
      "definition_site": "00bdbda8",
      "incomplete_value": true,
      "site": "00bdbdb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdbd0c",
      "incomplete_value": true,
      "site": "00bdbd1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00bdbd30",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdbd34",
      "READ",
      [
        "storage",
        "01126b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdbda8",
      "READ",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdbd30",
      "READ",
      [
        "storage",
        "01126c28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdbd34",
      "READ",
      [
        "storage",
        "01126c40",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdbda8",
      "READ",
      [
        "storage",
        "01126d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdbcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbc38.md#insn-00bdbcac) · [`00bdbd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbc38.md#insn-00bdbd1c) · [`00bdbdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbc38.md#insn-00bdbdac)
- 新版 [`00bdbd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbcd4.md#insn-00bdbd48) · [`00bdbdb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbcd4.md#insn-00bdbdb8) · [`00bdbe48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbcd4.md#insn-00bdbe48)

~~~diff
- 00bdbcac ["INT_ADD", "register:40f0:8", ["const:bdbcac:8", "const:4:8"]]
- 00bdbcac ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bdbd48 ["INT_ADD", "register:40f0:8", ["const:bdbd48:8", "const:4:8"]]
+ 00bdbd48 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bdbcac bytes bdfb0194
+ 00bdbd48 bytes cafb0194
- 00bdbd1c ["INT_ADD", "register:40f0:8", ["const:bdbd1c:8", "const:4:8"]]
- 00bdbd1c ["CALL", null, ["callee:00497874:8"]]
+ 00bdbdb8 ["INT_ADD", "register:40f0:8", ["const:bdbdb8:8", "const:4:8"]]
+ 00bdbdb8 ["CALL", null, ["callee:00497874:8"]]
- 00bdbd1c bytes c6eee297
+ 00bdbdb8 bytes afeee297
- 00bdbdac ["INT_ADD", "register:40f0:8", ["const:bdbdac:8", "const:4:8"]]
- 00bdbdac ["CALL", null, ["callee:00497874:8"]]
+ 00bdbe48 ["INT_ADD", "register:40f0:8", ["const:bdbe48:8", "const:4:8"]]
+ 00bdbe48 ["CALL", null, ["callee:00497874:8"]]
- 00bdbdac bytes a2eee297
+ 00bdbe48 bytes 8beee297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcc38110ec087c7eaa4083ec534cb016"></a>

### [`00bdc150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc150.md) → [`00bdc1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc1ec.md) _ZN8firebase4auth22FederatedOAuthProvider14ReauthenticateEPNS0_8AuthDataE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00bdbc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbc38.md) [`00bdcb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcb7c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bd48c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd48c8.md) [`00bdbcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbcd4.md) [`00bdcc18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcc18.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 50.00% / 新版 47.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bdc384",
      "incomplete_value": true,
      "site": "00bdc384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00bdc2e8",
      "incomplete_value": true,
      "site": "00bdc2e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc370"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bdc40c"
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
      "00bdc324",
      "READ",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdc380",
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc384",
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
      "00bdc324",
      "READ",
      [
        "storage",
        "01126da0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdc380",
      "READ",
      [
        "storage",
        "00c9baf0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc384",
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

- 旧版 [`00bdc298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc150.md#insn-00bdc298) · [`00bdc2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc150.md#insn-00bdc2ac) · [`00bdc318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc150.md#insn-00bdc318)
- 新版 [`00bdc334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc1ec.md#insn-00bdc334) · [`00bdc348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc1ec.md#insn-00bdc348) · [`00bdc3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc1ec.md#insn-00bdc3b4)

~~~diff
- 00bdc298 ["INT_ADD", "register:40f0:8", ["const:bdc298:8", "const:4:8"]]
- 00bdc298 ["CALL", null, ["callee:00497874:8"]]
+ 00bdc334 ["INT_ADD", "register:40f0:8", ["const:bdc334:8", "const:4:8"]]
+ 00bdc334 ["CALL", null, ["callee:00497874:8"]]
- 00bdc298 bytes 67ede297
+ 00bdc334 bytes 50ede297
- 00bdc2ac ["INT_ADD", "register:40f0:8", ["const:bdc2ac:8", "const:4:8"]]
- 00bdc2ac ["CALL", null, ["callee:00c5dda0:8"]]
+ 00bdc348 ["INT_ADD", "register:40f0:8", ["const:bdc348:8", "const:4:8"]]
+ 00bdc348 ["CALL", null, ["callee:00c5dda0:8"]]
- 00bdc2ac bytes 89060294
+ 00bdc348 bytes 96060294
- 00bdc318 ["INT_ADD", "register:40f0:8", ["const:bdc318:8", "const:4:8"]]
- 00bdc318 ["CALL", null, ["callee:00c5b010:8"]]
+ 00bdc3b4 ["INT_ADD", "register:40f0:8", ["const:bdc3b4:8", "const:4:8"]]
+ 00bdc3b4 ["CALL", null, ["callee:00c5b010:8"]]
- 00bdc318 bytes 0afb0194
+ 00bdc3b4 bytes 17fb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-471cfb5e3a030a5e4771adef84c99649"></a>

### [`00bdc454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc454.md) → [`00bdc4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc4f0.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10CredentialEEEvRKNS_12FutureHandleEiPKcEUlPvE_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ddd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5ddd0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5dea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dea0.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdc554",
      "incomplete_value": false,
      "site": "00bdc558",
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
      "definition_site": "00bdc4b8",
      "incomplete_value": false,
      "site": "00bdc4bc",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdc554",
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
      "00bdc554",
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

- 旧版 [`00bdc4bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc454.md#insn-00bdc4bc) · [`00bdc480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc454.md#insn-00bdc480) · [`00bdc48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc454.md#insn-00bdc48c)
- 新版 [`00bdc558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc4f0.md#insn-00bdc558) · [`00bdc51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc4f0.md#insn-00bdc51c) · [`00bdc528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc4f0.md#insn-00bdc528)

~~~diff
- 00bdc4bc ["INT_ADD", "register:40f0:8", ["const:bdc4bc:8", "const:4:8"]]
- 00bdc4bc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdc558 ["INT_ADD", "register:40f0:8", ["const:bdc558:8", "const:4:8"]]
+ 00bdc558 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdc4bc bytes d1fa0194
+ 00bdc558 bytes defa0194
- 00bdc480 ["INT_ADD", "register:40f0:8", ["const:bdc480:8", "const:4:8"]]
- 00bdc480 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bdc51c ["INT_ADD", "register:40f0:8", ["const:bdc51c:8", "const:4:8"]]
+ 00bdc51c ["CALL", null, ["callee:00c5aad0:8"]]
- 00bdc480 bytes 60f90194
+ 00bdc51c bytes 6df90194
- 00bdc48c ["INT_ADD", "register:40f0:8", ["const:bdc48c:8", "const:4:8"]]
- 00bdc48c ["CALL", null, ["callee:00c5af50:8"]]
+ 00bdc528 ["INT_ADD", "register:40f0:8", ["const:bdc528:8", "const:4:8"]]
+ 00bdc528 ["CALL", null, ["callee:00c5af50:8"]]
- 00bdc48c bytes 7dfa0194
+ 00bdc528 bytes 8afa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dc4920c0df47b5f83891f1e3f46ef7f"></a>

### [`00bdc6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc6cc.md) → [`00bdc768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc768.md) _ZN8firebase4auth18AdditionalUserInfoC2ERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5de20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de20.md) · 呼出先 3件 [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md) [`00c5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd60.md) [`00c5de70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de70.md)
- 新版 呼出元 1件 [`00c5def0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5def0.md) · 呼出先 3件 [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md) [`00c5de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de30.md) [`00c5df40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.54% / 新版 82.54%

CFGの説明率　旧版 50.00% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc7a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc7a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc7a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc770",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc7c4"
      ]
    ],
    [
      "unmatched:00bdc788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bdc774"
      ]
    ]
  ],
  "added": [
    [
      "00bdc80c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc7c4"
      ]
    ],
    [
      "00bdc824",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc810"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc6cc.md#insn-00bdc6ec) · [`00bdc770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc6cc.md#insn-00bdc770) · [`00bdc788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc6cc.md#insn-00bdc788)
- 新版 [`00bdc788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc768.md#insn-00bdc788)

~~~diff
- 00bdc6ec ["INT_ADD", "register:40f0:8", ["const:bdc6ec:8", "const:4:8"]]
- 00bdc6ec ["CALL", null, ["callee:00c5b680:8"]]
+ 00bdc788 ["INT_ADD", "register:40f0:8", ["const:bdc788:8", "const:4:8"]]
+ 00bdc788 ["CALL", null, ["callee:00c5b680:8"]]
- 00bdc6ec bytes b1fb0194
+ 00bdc788 bytes befb0194
- 00bdc770 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00bdc770 bytes c0fdff54
- 00bdc788 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdc788 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00bdc788 bytes 61ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31dfc59dbfac41680e5a069493d7d964"></a>

### [`00bdc83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc83c.md) → [`00bdc8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc8d8.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emp

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5de70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de70.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5de60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de60.md)
- 新版 呼出元 1件 [`00c5df40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df40.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5df30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc8ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdc948"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc900"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc900",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc9bc"
      ]
    ]
  ],
  "added": [
    [
      "00bdc99c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc9bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc83c.md#insn-00bdc874) · [`00bdc8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc83c.md#insn-00bdc8a0) · [`00bdc8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc83c.md#insn-00bdc8ac)
- 新版 [`00bdc910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc8d8.md#insn-00bdc910) · [`00bdc93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc8d8.md#insn-00bdc93c)

~~~diff
- 00bdc874 ["INT_ADD", "register:40f0:8", ["const:bdc874:8", "const:4:8"]]
- 00bdc874 ["CALL", null, ["callee:00c5df30:8"]]
+ 00bdc910 ["INT_ADD", "register:40f0:8", ["const:bdc910:8", "const:4:8"]]
+ 00bdc910 ["CALL", null, ["callee:00c5df30:8"]]
- 00bdc874 bytes 7b050294
+ 00bdc910 bytes 88050294
- 00bdc8a0 ["INT_ADD", "register:40f0:8", ["const:bdc8a0:8", "const:4:8"]]
- 00bdc8a0 ["CALL", null, ["callee:00c5a9c0:8"]]
+ 00bdc93c ["INT_ADD", "register:40f0:8", ["const:bdc93c:8", "const:4:8"]]
+ 00bdc93c ["CALL", null, ["callee:00c5a9c0:8"]]
- 00bdc8a0 bytes 14f80194
+ 00bdc93c bytes 21f80194
- 00bdc8ac ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bdc8ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bdc8ac ["INT_ADD", "register:4000:8", ["register:4000:8", "const:38:8"]]
- 00bdc8ac ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:1:4"]]
- 00bdc8ac bytes 1f8c03b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-388c6fbc88571004d7a9166d6f9b7782"></a>

### [`00bdc950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc950.md) → [`00bdc9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc9ec.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__fin

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5de60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de60.md) · 呼出先 1件 [`00c5b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5a0.md)
- 新版 呼出元 1件 [`00c5df30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df30.md) · 呼出先 1件 [`00c5b670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b670.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 74.10% / 新版 74.10%

CFGの説明率　旧版 42.47% / 新版 43.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc980"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc9b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdca04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc980",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdca38"
      ]
    ],
    [
      "unmatched:00bdc9b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdca8c"
      ]
    ],
    [
      "unmatched:00bdca04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdca90"
      ]
    ]
  ],
  "added": [
    [
      "00bdca1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdca38"
      ]
    ],
    [
      "00bdca4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdca8c"
      ]
    ],
    [
      "00bdcaa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdca90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc950.md#insn-00bdc980) · [`00bdc9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc950.md#insn-00bdc9b0) · [`00bdc9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc950.md#insn-00bdc9bc)
- 新版 [`00bdca58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc9ec.md#insn-00bdca58)

~~~diff
- 00bdc980 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00bdc980 bytes e0000054
- 00bdc9b0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bdc9b0 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00bdc9b0 bytes 080200b4
- 00bdc9bc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bdc9bc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bdca58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bdca58 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bdc9bc bytes c8ffffb5
+ 00bdca58 bytes c8ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ad246b874eb3ac854435184fb5e77d0"></a>

### [`00bdcc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcc58.md) → [`00bdccf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdccf4.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5ddc0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5de90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de90.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 21.43% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdcc68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdcc68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdcd04"
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
      "unmatched:00bdcc68",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdccbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdcd68"
      ]
    ],
    [
      "unmatched:00bdccc4",
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
      "00bdcd04",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bdcd58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdcd68"
      ]
    ],
    [
      "00bdcd60",
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

- 旧版 [`00bdcc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcc58.md#insn-00bdcc68) · [`00bdcc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcc58.md#insn-00bdcc8c) · [`00bdcc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcc58.md#insn-00bdcc98)
- 新版 [`00bdcd28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdccf4.md#insn-00bdcd28) · [`00bdcd34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdccf4.md#insn-00bdcd34)

~~~diff
- 00bdcc68 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bdcc68 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bdcc68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bdcc68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdcc68 bytes fd7b04a9
- 00bdcc8c ["INT_ADD", "register:40f0:8", ["const:bdcc8c:8", "const:4:8"]]
- 00bdcc8c ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bdcd28 ["INT_ADD", "register:40f0:8", ["const:bdcd28:8", "const:4:8"]]
+ 00bdcd28 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bdcc8c bytes 5df70194
+ 00bdcd28 bytes 6af70194
- 00bdcc98 ["INT_ADD", "register:40f0:8", ["const:bdcc98:8", "const:4:8"]]
- 00bdcc98 ["CALL", null, ["callee:00c5af50:8"]]
+ 00bdcd34 ["INT_ADD", "register:40f0:8", ["const:bdcd34:8", "const:4:8"]]
+ 00bdcd34 ["CALL", null, ["callee:00c5af50:8"]]
- 00bdcc98 bytes 7af80194
+ 00bdcd34 bytes 87f80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29b6a65d9746ffc5f163786ea4450db0"></a>

### [`00bdce18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce18.md) → [`00bdceb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdceb4.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bdcee0",
      "incomplete_value": true,
      "site": "00bdcee0",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdce44",
      "incomplete_value": true,
      "site": "00bdce44",
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
            "const:d00:8"
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
      "definition_site": "00bdcec8",
      "incomplete_value": true,
      "site": "00bdcec8",
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
      "definition_site": "00bdce2c",
      "incomplete_value": true,
      "site": "00bdce2c",
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
      "definition_site": "00bdced4",
      "incomplete_value": false,
      "site": "00bdced8",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdce38",
      "incomplete_value": false,
      "site": "00bdce3c",
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
            "const:250:8"
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
      "00bdcec4",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdced4",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdcee0",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcec4",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdced4",
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      "00bdcee0",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdce3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce18.md#insn-00bdce3c) · [`00bdce44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce18.md#insn-00bdce44) · [`00bdce28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce18.md#insn-00bdce28)
- 新版 [`00bdced8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdceb4.md#insn-00bdced8) · [`00bdcee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdceb4.md#insn-00bdcee0) · [`00bdcec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdceb4.md#insn-00bdcec4)

~~~diff
- 00bdce3c ["INT_ADD", "register:40f0:8", ["const:bdce3c:8", "const:4:8"]]
- 00bdce3c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdced8 ["INT_ADD", "register:40f0:8", ["const:bdced8:8", "const:4:8"]]
+ 00bdced8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdce3c bytes 35f80194
+ 00bdced8 bytes 42f80194
- 00bdce44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
- 00bdce44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdcee0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdcee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdce44 bytes 608206f9
+ 00bdcee0 bytes 600207f9
- 00bdce28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
- 00bdce28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdcec4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdcec4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdce28 bytes 688246f9
+ 00bdcec4 bytes 680247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83a2956d009fb8cf18b6353b14df56f6"></a>

### [`00bdce58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce58.md) → [`00bdcef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcef4.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bdcf20",
      "incomplete_value": true,
      "site": "00bdcf20",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdce84",
      "incomplete_value": true,
      "site": "00bdce84",
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
            "const:d00:8"
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
      "definition_site": "00bdcf08",
      "incomplete_value": true,
      "site": "00bdcf08",
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
      "definition_site": "00bdce6c",
      "incomplete_value": true,
      "site": "00bdce6c",
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
      "definition_site": "00bdcf10",
      "incomplete_value": false,
      "site": "00bdcf18",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdce74",
      "incomplete_value": false,
      "site": "00bdce7c",
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
            "const:250:8"
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
      "00bdcf04",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcf10",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdcf20",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcf04",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcf10",
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      "00bdcf20",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdce7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce58.md#insn-00bdce7c) · [`00bdce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce58.md#insn-00bdce84) · [`00bdce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce58.md#insn-00bdce68)
- 新版 [`00bdcf18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcef4.md#insn-00bdcf18) · [`00bdcf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcef4.md#insn-00bdcf20) · [`00bdcf04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcef4.md#insn-00bdcf04)

~~~diff
- 00bdce7c ["INT_ADD", "register:40f0:8", ["const:bdce7c:8", "const:4:8"]]
- 00bdce7c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdcf18 ["INT_ADD", "register:40f0:8", ["const:bdcf18:8", "const:4:8"]]
+ 00bdcf18 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdce7c bytes 25f80194
+ 00bdcf18 bytes 32f80194
- 00bdce84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
- 00bdce84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdcf20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdcf20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdce84 bytes 608206f9
+ 00bdcf20 bytes 600207f9
- 00bdce68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
- 00bdce68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdcf04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdcf04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdce68 bytes 688246f9
+ 00bdcf04 bytes 680247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f01284de1b3a552a15ba10f8cb4662db"></a>

### [`00bdce98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce98.md) → [`00bdcf34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf34.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bdcf64",
      "incomplete_value": true,
      "site": "00bdcf64",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcec8",
      "incomplete_value": true,
      "site": "00bdcec8",
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
            "const:d00:8"
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
      "definition_site": "00bdcf48",
      "incomplete_value": true,
      "site": "00bdcf48",
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
      "definition_site": "00bdceac",
      "incomplete_value": true,
      "site": "00bdceac",
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
      "definition_site": "00bdcf54",
      "incomplete_value": false,
      "site": "00bdcf5c",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdceb8",
      "incomplete_value": false,
      "site": "00bdcec0",
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
            "const:250:8"
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
      "00bdcf44",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcf54",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdcf64",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcf44",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcf54",
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      "00bdcf64",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce98.md#insn-00bdcec0) · [`00bdcec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce98.md#insn-00bdcec8) · [`00bdcea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce98.md#insn-00bdcea8)
- 新版 [`00bdcf5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf34.md#insn-00bdcf5c) · [`00bdcf64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf34.md#insn-00bdcf64) · [`00bdcf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf34.md#insn-00bdcf44)

~~~diff
- 00bdcec0 ["INT_ADD", "register:40f0:8", ["const:bdcec0:8", "const:4:8"]]
- 00bdcec0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdcf5c ["INT_ADD", "register:40f0:8", ["const:bdcf5c:8", "const:4:8"]]
+ 00bdcf5c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdcec0 bytes 14f80194
+ 00bdcf5c bytes 21f80194
- 00bdcec8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
- 00bdcec8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdcf64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdcf64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdcec8 bytes 608206f9
+ 00bdcf64 bytes 600207f9
- 00bdcea8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
- 00bdcea8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdcf44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdcf44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcea8 bytes 688246f9
+ 00bdcf44 bytes 680247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb3cecf59e12d090715e03843e562b37"></a>

### [`00bdcedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcedc.md) → [`00bdcf78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf78.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdcfa8",
      "incomplete_value": true,
      "site": "00bdcfa8",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcf0c",
      "incomplete_value": true,
      "site": "00bdcf0c",
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
            "const:d00:8"
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
      "definition_site": "00bdcf8c",
      "incomplete_value": true,
      "site": "00bdcf8c",
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
      "definition_site": "00bdcef0",
      "incomplete_value": true,
      "site": "00bdcef0",
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
      "definition_site": "00bdcf94",
      "incomplete_value": false,
      "site": "00bdcfa0",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcef8",
      "incomplete_value": false,
      "site": "00bdcf04",
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
            "const:250:8"
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
      "00bdcf88",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcf94",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdcfa8",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcf88",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcf94",
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      "00bdcfa8",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcf04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcedc.md#insn-00bdcf04) · [`00bdcf0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcedc.md#insn-00bdcf0c) · [`00bdceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcedc.md#insn-00bdceec)
- 新版 [`00bdcfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf78.md#insn-00bdcfa0) · [`00bdcfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf78.md#insn-00bdcfa8) · [`00bdcf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf78.md#insn-00bdcf88)

~~~diff
- 00bdcf04 ["INT_ADD", "register:40f0:8", ["const:bdcf04:8", "const:4:8"]]
- 00bdcf04 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdcfa0 ["INT_ADD", "register:40f0:8", ["const:bdcfa0:8", "const:4:8"]]
+ 00bdcfa0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdcf04 bytes 03f80194
+ 00bdcfa0 bytes 10f80194
- 00bdcf0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
- 00bdcf0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdcfa8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdcfa8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdcf0c bytes 608206f9
+ 00bdcfa8 bytes 600207f9
- 00bdceec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
- 00bdceec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdcf88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdcf88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdceec bytes 688246f9
+ 00bdcf88 bytes 680247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe08098407ec6299e071fd17e4ec8427"></a>

### [`00bdcf2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcf2c.md) → [`00bdcfc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcfc8.md) _ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bdd020",
      "incomplete_value": true,
      "site": "00bdd020",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcf84",
      "incomplete_value": true,
      "site": "00bdcf84",
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
            "const:d08:8"
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
      "definition_site": "00bdcffc",
      "incomplete_value": true,
      "site": "00bdd008",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcf60",
      "incomplete_value": true,
      "site": "00bdcf6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "00bdcfdc",
      "READ",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdcffc",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd020",
      "WRITE",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdcfdc",
      "READ",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdcffc",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd020",
      "WRITE",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcf6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcf2c.md#insn-00bdcf6c) · [`00bdcf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcf2c.md#insn-00bdcf84) · [`00bdcf40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcf2c.md#insn-00bdcf40)
- 新版 [`00bdd008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcfc8.md#insn-00bdd008) · [`00bdd020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcfc8.md#insn-00bdd020) · [`00bdcfdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcfc8.md#insn-00bdcfdc)

~~~diff
- 00bdcf6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdcf6c ["INT_ADD", "register:40f0:8", ["const:bdcf6c:8", "const:4:8"]]
- 00bdcf6c ["CALLIND", null, ["register:0:8"]]
+ 00bdd008 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd008 ["INT_ADD", "register:40f0:8", ["const:bdd008:8", "const:4:8"]]
+ 00bdd008 ["CALLIND", null, ["register:0:8"]]
- 00bdcf6c bytes 00013fd6
+ 00bdd008 bytes 00013fd6
- 00bdcf84 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bdcf84 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d08:8"]]
- 00bdcf84 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bdd020 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bdd020 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e08:8"]]
+ 00bdd020 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bdcf84 bytes a0223439
+ 00bdd020 bytes a0223839
- 00bdcf40 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d08:8"]]
- 00bdcf40 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bdcf40 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bdcfdc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e08:8"]]
+ 00bdcfdc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bdcfdc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bdcf40 bytes a8227439
+ 00bdcfdc bytes a8227839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ea7f8d327c78fc1f05c1e5cab87d9f7"></a>

### [`00bdcf98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcf98.md) → [`00bdd034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd034.md) _ZN8firebase4auth11tokenresult12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bdd070",
      "incomplete_value": true,
      "site": "00bdd070",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcfd4",
      "incomplete_value": true,
      "site": "00bdcfd4",
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
            "const:d08:8"
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
      "definition_site": "00bdd090",
      "incomplete_value": true,
      "site": "00bdd090",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcff4",
      "incomplete_value": true,
      "site": "00bdcff4",
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
            "const:d00:8"
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
      "definition_site": "00bdd04c",
      "incomplete_value": true,
      "site": "00bdd04c",
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
      "definition_site": "00bdcfb0",
      "incomplete_value": true,
      "site": "00bdcfb0",
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
      "00bdd048",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd054",
      "READ",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd070",
      "WRITE",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd048",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd054",
      "READ",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd070",
      "WRITE",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcfd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcf98.md#insn-00bdcfd4) · [`00bdcff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcf98.md#insn-00bdcff0) · [`00bdcff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcf98.md#insn-00bdcff4)
- 新版 [`00bdd070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd034.md#insn-00bdd070) · [`00bdd08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd034.md#insn-00bdd08c) · [`00bdd090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd034.md#insn-00bdd090)

~~~diff
- 00bdcfd4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bdcfd4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bdcfd4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d08:8"]]
- 00bdcfd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdd070 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdd070 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdd070 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e08:8"]]
+ 00bdd070 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bdcfd4 bytes bf223439
+ 00bdd070 bytes bf223839
- 00bdcff0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdcff0 ["INT_ADD", "register:40f0:8", ["const:bdcff0:8", "const:4:8"]]
- 00bdcff0 ["CALLIND", null, ["register:0:8"]]
+ 00bdd08c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd08c ["INT_ADD", "register:40f0:8", ["const:bdd08c:8", "const:4:8"]]
+ 00bdd08c ["CALLIND", null, ["register:0:8"]]
- 00bdcff0 bytes 00013fd6
+ 00bdd08c bytes 00013fd6
- 00bdcff4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
- 00bdcff4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bdcff4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdd090 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bdd090 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdd090 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bdcff4 bytes 9f8206f9
+ 00bdd090 bytes 9f0207f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-530e8d917eb76eac7f5d3544fa8410c9"></a>

### [`00bdd008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd008.md) → [`00bdd0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd0a4.md) _ZN8firebase4auth11tokenresult14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd0e4",
      "incomplete_value": true,
      "site": "00bdd0e4",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd048",
      "incomplete_value": true,
      "site": "00bdd048",
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
            "const:d00:8"
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
      "definition_site": "00bdd0c0",
      "incomplete_value": true,
      "site": "00bdd0c0",
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
      "definition_site": "00bdd024",
      "incomplete_value": true,
      "site": "00bdd024",
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
      "definition_site": "00bdd0c8",
      "incomplete_value": false,
      "site": "00bdd0dc",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd02c",
      "incomplete_value": false,
      "site": "00bdd040",
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
            "const:250:8"
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
      "00bdd0b8",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd0c8",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdd0e4",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd0b8",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd0c8",
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      "00bdd0e4",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd008.md#insn-00bdd040) · [`00bdd048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd008.md#insn-00bdd048) · [`00bdd01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd008.md#insn-00bdd01c)
- 新版 [`00bdd0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd0a4.md#insn-00bdd0dc) · [`00bdd0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd0a4.md#insn-00bdd0e4) · [`00bdd0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd0a4.md#insn-00bdd0b8)

~~~diff
- 00bdd040 ["INT_ADD", "register:40f0:8", ["const:bdd040:8", "const:4:8"]]
- 00bdd040 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd0dc ["INT_ADD", "register:40f0:8", ["const:bdd0dc:8", "const:4:8"]]
+ 00bdd0dc ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd040 bytes b4f70194
+ 00bdd0dc bytes c1f70194
- 00bdd048 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
- 00bdd048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd0e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bdd0e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd048 bytes 808206f9
+ 00bdd0e4 bytes 800207f9
- 00bdd01c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
- 00bdd01c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd0b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bdd0b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd01c bytes 818246f9
+ 00bdd0b8 bytes 810247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1e2711ef60775b780c82e9f75aeff92"></a>

### [`00bdd078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd078.md) → [`00bdd114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd114.md) _ZN8firebase4auth11tokenresult11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bdd130",
      "incomplete_value": false,
      "site": "00bdd134",
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
      "definition_site": "00bdd094",
      "incomplete_value": false,
      "site": "00bdd098",
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
      "definition_site": "00bdd140",
      "incomplete_value": true,
      "site": "00bdd14c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdd0a4",
      "incomplete_value": true,
      "site": "00bdd0b0",
      "value": [
        "LOAD",
        "8",
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
      "00bdd130",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bdd140",
      "DATA",
      [
        "storage",
        "01126d10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd130",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bdd140",
      "DATA",
      [
        "storage",
        "01126e10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd078.md#insn-00bdd098) · [`00bdd094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd078.md#insn-00bdd094) · [`00bdd0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd078.md#insn-00bdd0a0)
- 新版 [`00bdd134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd114.md#insn-00bdd134) · [`00bdd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd114.md#insn-00bdd130) · [`00bdd13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd114.md#insn-00bdd13c)

~~~diff
- 00bdd098 ["INT_ADD", "register:40f0:8", ["const:bdd098:8", "const:4:8"]]
- 00bdd098 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdd134 ["INT_ADD", "register:40f0:8", ["const:bdd134:8", "const:4:8"]]
+ 00bdd134 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdd098 bytes daf70194
+ 00bdd134 bytes e7f70194
- 00bdd094 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bdd094 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd094 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd094 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd130 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bdd130 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd130 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd130 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdd094 bytes 009c0d91
+ 00bdd130 bytes 002c0c91
- 00bdd0a0 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00bdd0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdd13c ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 00bdd13c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd13c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd13c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdd0a0 bytes 08413491
+ 00bdd13c bytes 08413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb1f1931caf6b397e8606a94479be6e"></a>

### [`00bdd0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd0b4.md) → [`00bdd150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd150.md) _ZN8firebase4auth11tokenresult13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd190",
      "incomplete_value": true,
      "site": "00bdd190",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd0f4",
      "incomplete_value": true,
      "site": "00bdd0f4",
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
            "const:d00:8"
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
      "definition_site": "00bdd16c",
      "incomplete_value": true,
      "site": "00bdd16c",
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
      "definition_site": "00bdd0d0",
      "incomplete_value": true,
      "site": "00bdd0d0",
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
      "definition_site": "00bdd174",
      "incomplete_value": false,
      "site": "00bdd188",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd0d8",
      "incomplete_value": false,
      "site": "00bdd0ec",
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
            "const:250:8"
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
      "00bdd164",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd174",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdd190",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd164",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd174",
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      "00bdd190",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd0b4.md#insn-00bdd0ec) · [`00bdd0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd0b4.md#insn-00bdd0f4) · [`00bdd0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd0b4.md#insn-00bdd0c8)
- 新版 [`00bdd188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd150.md#insn-00bdd188) · [`00bdd190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd150.md#insn-00bdd190) · [`00bdd164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd150.md#insn-00bdd164)

~~~diff
- 00bdd0ec ["INT_ADD", "register:40f0:8", ["const:bdd0ec:8", "const:4:8"]]
- 00bdd0ec ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd188 ["INT_ADD", "register:40f0:8", ["const:bdd188:8", "const:4:8"]]
+ 00bdd188 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd0ec bytes 89f70194
+ 00bdd188 bytes 96f70194
- 00bdd0f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
- 00bdd0f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd190 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bdd190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd0f4 bytes 808206f9
+ 00bdd190 bytes 800207f9
- 00bdd0c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
- 00bdd0c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd164 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bdd164 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd0c8 bytes 818246f9
+ 00bdd164 bytes 810247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b33c86ee6502b81cf10215d28fc213d4"></a>

### [`00bdd124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd124.md) → [`00bdd1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd1c0.md) _ZN8firebase4auth11tokenresult10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bdd1dc",
      "incomplete_value": false,
      "site": "00bdd1e0",
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
      "definition_site": "00bdd140",
      "incomplete_value": false,
      "site": "00bdd144",
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
      "definition_site": "00bdd1ec",
      "incomplete_value": true,
      "site": "00bdd1f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdd150",
      "incomplete_value": true,
      "site": "00bdd15c",
      "value": [
        "LOAD",
        "8",
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
      "00bdd1dc",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bdd1ec",
      "DATA",
      [
        "storage",
        "01126d18",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdd1dc",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bdd1ec",
      "DATA",
      [
        "storage",
        "01126e18",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd124.md#insn-00bdd144) · [`00bdd140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd124.md#insn-00bdd140) · [`00bdd14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd124.md#insn-00bdd14c)
- 新版 [`00bdd1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd1c0.md#insn-00bdd1e0) · [`00bdd1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd1c0.md#insn-00bdd1dc) · [`00bdd1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd1c0.md#insn-00bdd1e8)

~~~diff
- 00bdd144 ["INT_ADD", "register:40f0:8", ["const:bdd144:8", "const:4:8"]]
- 00bdd144 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdd1e0 ["INT_ADD", "register:40f0:8", ["const:bdd1e0:8", "const:4:8"]]
+ 00bdd1e0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdd144 bytes aff70194
+ 00bdd1e0 bytes bcf70194
- 00bdd140 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bdd140 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd140 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd140 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd1dc ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bdd1dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd1dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd1dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdd140 bytes 00781491
+ 00bdd1dc bytes 00341591
- 00bdd14c ["COPY", "tmp:0:8", ["const:d18:8"]]
- 00bdd14c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd14c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd14c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdd1e8 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00bdd1e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd1e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd1e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdd14c bytes 08613491
+ 00bdd1e8 bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1388b6d98916ba729bb2fab0effd1024"></a>

### [`00bdd160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd160.md) → [`00bdd1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd1fc.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

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
      "definition_site": "00bdd228",
      "incomplete_value": true,
      "site": "00bdd228",
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
      "definition_site": "00bdd18c",
      "incomplete_value": true,
      "site": "00bdd18c",
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
      "definition_site": "00bdd210",
      "incomplete_value": true,
      "site": "00bdd210",
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
      "definition_site": "00bdd174",
      "incomplete_value": true,
      "site": "00bdd174",
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
      "definition_site": "00bdd21c",
      "incomplete_value": false,
      "site": "00bdd220",
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
            "const:8b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd180",
      "incomplete_value": false,
      "site": "00bdd184",
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
            "const:887:8"
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
      "00bdd20c",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd21c",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd228",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd20c",
      "READ",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd21c",
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      "00bdd228",
      "WRITE",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd160.md#insn-00bdd184) · [`00bdd18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd160.md#insn-00bdd18c) · [`00bdd170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd160.md#insn-00bdd170)
- 新版 [`00bdd220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd1fc.md#insn-00bdd220) · [`00bdd228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd1fc.md#insn-00bdd228) · [`00bdd20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd1fc.md#insn-00bdd20c)

~~~diff
- 00bdd184 ["INT_ADD", "register:40f0:8", ["const:bdd184:8", "const:4:8"]]
- 00bdd184 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd220 ["INT_ADD", "register:40f0:8", ["const:bdd220:8", "const:4:8"]]
+ 00bdd220 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd184 bytes 63f70194
+ 00bdd220 bytes 70f70194
- 00bdd18c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00bdd18c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd228 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bdd228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd18c bytes 609206f9
+ 00bdd228 bytes 601207f9
- 00bdd170 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00bdd170 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd20c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bdd20c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd170 bytes 689246f9
+ 00bdd20c bytes 681247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4a95c566d611156c829ac1d2a365a00"></a>

### [`00bdd1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd1a0.md) → [`00bdd23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd23c.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bdd268",
      "incomplete_value": true,
      "site": "00bdd268",
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
      "definition_site": "00bdd1cc",
      "incomplete_value": true,
      "site": "00bdd1cc",
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
      "definition_site": "00bdd250",
      "incomplete_value": true,
      "site": "00bdd250",
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
      "definition_site": "00bdd1b4",
      "incomplete_value": true,
      "site": "00bdd1b4",
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
      "definition_site": "00bdd258",
      "incomplete_value": false,
      "site": "00bdd260",
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
            "const:8b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd1bc",
      "incomplete_value": false,
      "site": "00bdd1c4",
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
            "const:887:8"
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
      "00bdd24c",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd258",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd268",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd24c",
      "READ",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd258",
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      "00bdd268",
      "WRITE",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd1a0.md#insn-00bdd1c4) · [`00bdd1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd1a0.md#insn-00bdd1cc) · [`00bdd1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd1a0.md#insn-00bdd1b0)
- 新版 [`00bdd260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd23c.md#insn-00bdd260) · [`00bdd268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd23c.md#insn-00bdd268) · [`00bdd24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd23c.md#insn-00bdd24c)

~~~diff
- 00bdd1c4 ["INT_ADD", "register:40f0:8", ["const:bdd1c4:8", "const:4:8"]]
- 00bdd1c4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd260 ["INT_ADD", "register:40f0:8", ["const:bdd260:8", "const:4:8"]]
+ 00bdd260 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd1c4 bytes 53f70194
+ 00bdd260 bytes 60f70194
- 00bdd1cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00bdd1cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd268 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bdd268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd1cc bytes 609206f9
+ 00bdd268 bytes 601207f9
- 00bdd1b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00bdd1b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd24c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bdd24c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd1b0 bytes 689246f9
+ 00bdd24c bytes 681247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8b9f741290d789797461faea7f783c3"></a>

### [`00bdd1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd1e0.md) → [`00bdd27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd27c.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bdd2ac",
      "incomplete_value": true,
      "site": "00bdd2ac",
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
      "definition_site": "00bdd210",
      "incomplete_value": true,
      "site": "00bdd210",
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
      "definition_site": "00bdd290",
      "incomplete_value": true,
      "site": "00bdd290",
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
      "definition_site": "00bdd1f4",
      "incomplete_value": true,
      "site": "00bdd1f4",
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
      "definition_site": "00bdd29c",
      "incomplete_value": false,
      "site": "00bdd2a4",
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
            "const:8b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd200",
      "incomplete_value": false,
      "site": "00bdd208",
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
            "const:887:8"
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
      "00bdd28c",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd29c",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd2ac",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd28c",
      "READ",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd29c",
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      "00bdd2ac",
      "WRITE",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd1e0.md#insn-00bdd208) · [`00bdd210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd1e0.md#insn-00bdd210) · [`00bdd1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd1e0.md#insn-00bdd1f0)
- 新版 [`00bdd2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd27c.md#insn-00bdd2a4) · [`00bdd2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd27c.md#insn-00bdd2ac) · [`00bdd28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd27c.md#insn-00bdd28c)

~~~diff
- 00bdd208 ["INT_ADD", "register:40f0:8", ["const:bdd208:8", "const:4:8"]]
- 00bdd208 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd2a4 ["INT_ADD", "register:40f0:8", ["const:bdd2a4:8", "const:4:8"]]
+ 00bdd2a4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd208 bytes 42f70194
+ 00bdd2a4 bytes 4ff70194
- 00bdd210 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00bdd210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd2ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bdd2ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd210 bytes 609206f9
+ 00bdd2ac bytes 601207f9
- 00bdd1f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00bdd1f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd28c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bdd28c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd1f0 bytes 689246f9
+ 00bdd28c bytes 681247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20a0c3a75e56f0692a305bce536ff440"></a>

### [`00bdd224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd224.md) → [`00bdd2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd2c0.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd2f0",
      "incomplete_value": true,
      "site": "00bdd2f0",
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
      "definition_site": "00bdd254",
      "incomplete_value": true,
      "site": "00bdd254",
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
      "definition_site": "00bdd2d4",
      "incomplete_value": true,
      "site": "00bdd2d4",
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
      "definition_site": "00bdd238",
      "incomplete_value": true,
      "site": "00bdd238",
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
      "definition_site": "00bdd2dc",
      "incomplete_value": false,
      "site": "00bdd2e8",
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
            "const:8b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd240",
      "incomplete_value": false,
      "site": "00bdd24c",
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
            "const:887:8"
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
      "00bdd2d0",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd2dc",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd2f0",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd2d0",
      "READ",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd2dc",
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      "00bdd2f0",
      "WRITE",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd224.md#insn-00bdd24c) · [`00bdd254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd224.md#insn-00bdd254) · [`00bdd234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd224.md#insn-00bdd234)
- 新版 [`00bdd2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd2c0.md#insn-00bdd2e8) · [`00bdd2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd2c0.md#insn-00bdd2f0) · [`00bdd2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd2c0.md#insn-00bdd2d0)

~~~diff
- 00bdd24c ["INT_ADD", "register:40f0:8", ["const:bdd24c:8", "const:4:8"]]
- 00bdd24c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd2e8 ["INT_ADD", "register:40f0:8", ["const:bdd2e8:8", "const:4:8"]]
+ 00bdd2e8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd24c bytes 31f70194
+ 00bdd2e8 bytes 3ef70194
- 00bdd254 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00bdd254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd2f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bdd2f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd254 bytes 609206f9
+ 00bdd2f0 bytes 601207f9
- 00bdd234 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
- 00bdd234 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd2d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bdd2d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd234 bytes 689246f9
+ 00bdd2d0 bytes 681247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06e603a9f8ce4687d5191bbbe1e94818"></a>

### [`00bdd274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd274.md) → [`00bdd310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd310.md) _ZN8firebase4auth4user15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bdd368",
      "incomplete_value": true,
      "site": "00bdd368",
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
      "definition_site": "00bdd2cc",
      "incomplete_value": true,
      "site": "00bdd2cc",
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
      "definition_site": "00bdd344",
      "incomplete_value": true,
      "site": "00bdd350",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd2a8",
      "incomplete_value": true,
      "site": "00bdd2b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bdd324",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd344",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd368",
      "WRITE",
      [
        "storage",
        "01126d28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd324",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd344",
      "READ",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd368",
      "WRITE",
      [
        "storage",
        "01126e28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd274.md#insn-00bdd2b4) · [`00bdd2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd274.md#insn-00bdd2cc) · [`00bdd288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd274.md#insn-00bdd288)
- 新版 [`00bdd350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd310.md#insn-00bdd350) · [`00bdd368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd310.md#insn-00bdd368) · [`00bdd324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd310.md#insn-00bdd324)

~~~diff
- 00bdd2b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdd2b4 ["INT_ADD", "register:40f0:8", ["const:bdd2b4:8", "const:4:8"]]
- 00bdd2b4 ["CALLIND", null, ["register:0:8"]]
+ 00bdd350 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd350 ["INT_ADD", "register:40f0:8", ["const:bdd350:8", "const:4:8"]]
+ 00bdd350 ["CALLIND", null, ["register:0:8"]]
- 00bdd2b4 bytes 00013fd6
+ 00bdd350 bytes 00013fd6
- 00bdd2cc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bdd2cc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d28:8"]]
- 00bdd2cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bdd368 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bdd368 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e28:8"]]
+ 00bdd368 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bdd2cc bytes a0a23439
+ 00bdd368 bytes a0a23839
- 00bdd288 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d28:8"]]
- 00bdd288 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bdd288 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bdd324 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e28:8"]]
+ 00bdd324 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd324 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bdd288 bytes a8a27439
+ 00bdd324 bytes a8a27839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-513dd41f84d635477eed4ce54d9d1974"></a>

### [`00bdd2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd2e0.md) → [`00bdd37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd37c.md) _ZN8firebase4auth4user12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bdd3b8",
      "incomplete_value": true,
      "site": "00bdd3b8",
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
      "definition_site": "00bdd31c",
      "incomplete_value": true,
      "site": "00bdd31c",
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
      "definition_site": "00bdd3d8",
      "incomplete_value": true,
      "site": "00bdd3d8",
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
      "definition_site": "00bdd33c",
      "incomplete_value": true,
      "site": "00bdd33c",
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
      "definition_site": "00bdd394",
      "incomplete_value": true,
      "site": "00bdd394",
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
      "definition_site": "00bdd2f8",
      "incomplete_value": true,
      "site": "00bdd2f8",
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
      "00bdd390",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd39c",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd3b8",
      "WRITE",
      [
        "storage",
        "01126d28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd390",
      "READ",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd39c",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd3b8",
      "WRITE",
      [
        "storage",
        "01126e28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd2e0.md#insn-00bdd31c) · [`00bdd338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd2e0.md#insn-00bdd338) · [`00bdd33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd2e0.md#insn-00bdd33c)
- 新版 [`00bdd3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd37c.md#insn-00bdd3b8) · [`00bdd3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd37c.md#insn-00bdd3d4) · [`00bdd3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd37c.md#insn-00bdd3d8)

~~~diff
- 00bdd31c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bdd31c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bdd31c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d28:8"]]
- 00bdd31c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdd3b8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdd3b8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdd3b8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e28:8"]]
+ 00bdd3b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bdd31c bytes bfa23439
+ 00bdd3b8 bytes bfa23839
- 00bdd338 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdd338 ["INT_ADD", "register:40f0:8", ["const:bdd338:8", "const:4:8"]]
- 00bdd338 ["CALLIND", null, ["register:0:8"]]
+ 00bdd3d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd3d4 ["INT_ADD", "register:40f0:8", ["const:bdd3d4:8", "const:4:8"]]
+ 00bdd3d4 ["CALLIND", null, ["register:0:8"]]
- 00bdd338 bytes 00013fd6
+ 00bdd3d4 bytes 00013fd6
- 00bdd33c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
- 00bdd33c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bdd33c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdd3d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00bdd3d8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdd3d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bdd33c bytes 9f9206f9
+ 00bdd3d8 bytes 9f1207f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6996b1dbf4306fb51a8065f9234e638c"></a>

### [`00bdd350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd350.md) → [`00bdd3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd3ec.md) _ZN8firebase4auth4user14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd42c",
      "incomplete_value": true,
      "site": "00bdd42c",
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
      "definition_site": "00bdd390",
      "incomplete_value": true,
      "site": "00bdd390",
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
      "definition_site": "00bdd408",
      "incomplete_value": true,
      "site": "00bdd408",
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
      "definition_site": "00bdd36c",
      "incomplete_value": true,
      "site": "00bdd36c",
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
      "definition_site": "00bdd410",
      "incomplete_value": false,
      "site": "00bdd424",
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
            "const:8b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd374",
      "incomplete_value": false,
      "site": "00bdd388",
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
            "const:887:8"
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
      "00bdd400",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd410",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd42c",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd400",
      "READ",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd410",
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      "00bdd42c",
      "WRITE",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd350.md#insn-00bdd388) · [`00bdd390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd350.md#insn-00bdd390) · [`00bdd364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd350.md#insn-00bdd364)
- 新版 [`00bdd424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd3ec.md#insn-00bdd424) · [`00bdd42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd3ec.md#insn-00bdd42c) · [`00bdd400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd3ec.md#insn-00bdd400)

~~~diff
- 00bdd388 ["INT_ADD", "register:40f0:8", ["const:bdd388:8", "const:4:8"]]
- 00bdd388 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd424 ["INT_ADD", "register:40f0:8", ["const:bdd424:8", "const:4:8"]]
+ 00bdd424 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd388 bytes e2f60194
+ 00bdd424 bytes eff60194
- 00bdd390 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
- 00bdd390 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd42c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00bdd42c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd390 bytes 809206f9
+ 00bdd42c bytes 801207f9
- 00bdd364 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
- 00bdd364 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd400 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00bdd400 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd364 bytes 819246f9
+ 00bdd400 bytes 811247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebe462e363407744a56c8053e6794a39"></a>

### [`00bdd3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd3c0.md) → [`00bdd45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd45c.md) _ZN8firebase4auth4user11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bdd478",
      "incomplete_value": false,
      "site": "00bdd47c",
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
      "definition_site": "00bdd3dc",
      "incomplete_value": false,
      "site": "00bdd3e0",
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
      "definition_site": "00bdd488",
      "incomplete_value": true,
      "site": "00bdd494",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdd3ec",
      "incomplete_value": true,
      "site": "00bdd3f8",
      "value": [
        "LOAD",
        "8",
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
      "00bdd478",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bdd488",
      "DATA",
      [
        "storage",
        "01126d30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd478",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bdd488",
      "DATA",
      [
        "storage",
        "01126e30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd3c0.md#insn-00bdd3e0) · [`00bdd3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd3c0.md#insn-00bdd3dc) · [`00bdd3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd3c0.md#insn-00bdd3e8)
- 新版 [`00bdd47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd45c.md#insn-00bdd47c) · [`00bdd478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd45c.md#insn-00bdd478) · [`00bdd484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd45c.md#insn-00bdd484)

~~~diff
- 00bdd3e0 ["INT_ADD", "register:40f0:8", ["const:bdd3e0:8", "const:4:8"]]
- 00bdd3e0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdd47c ["INT_ADD", "register:40f0:8", ["const:bdd47c:8", "const:4:8"]]
+ 00bdd47c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdd3e0 bytes 08f70194
+ 00bdd47c bytes 15f70194
- 00bdd3dc ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bdd3dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd3dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd3dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd478 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bdd478 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd478 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd478 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdd3dc bytes 009c0d91
+ 00bdd478 bytes 002c0c91
- 00bdd3e8 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 00bdd3e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd3e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd3e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdd484 ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 00bdd484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdd3e8 bytes 08c13491
+ 00bdd484 bytes 08c13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baa4a51b5d15b350d2d39f7c95d5ae39"></a>

### [`00bdd3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd3fc.md) → [`00bdd498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd498.md) _ZN8firebase4auth4user13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd4d8",
      "incomplete_value": true,
      "site": "00bdd4d8",
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
      "definition_site": "00bdd43c",
      "incomplete_value": true,
      "site": "00bdd43c",
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
      "definition_site": "00bdd4b4",
      "incomplete_value": true,
      "site": "00bdd4b4",
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
      "definition_site": "00bdd418",
      "incomplete_value": true,
      "site": "00bdd418",
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
      "definition_site": "00bdd4bc",
      "incomplete_value": false,
      "site": "00bdd4d0",
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
            "const:8b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd420",
      "incomplete_value": false,
      "site": "00bdd434",
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
            "const:887:8"
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
      "00bdd4ac",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd4bc",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd4d8",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd4ac",
      "READ",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd4bc",
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      "00bdd4d8",
      "WRITE",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd3fc.md#insn-00bdd434) · [`00bdd43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd3fc.md#insn-00bdd43c) · [`00bdd410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd3fc.md#insn-00bdd410)
- 新版 [`00bdd4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd498.md#insn-00bdd4d0) · [`00bdd4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd498.md#insn-00bdd4d8) · [`00bdd4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd498.md#insn-00bdd4ac)

~~~diff
- 00bdd434 ["INT_ADD", "register:40f0:8", ["const:bdd434:8", "const:4:8"]]
- 00bdd434 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd4d0 ["INT_ADD", "register:40f0:8", ["const:bdd4d0:8", "const:4:8"]]
+ 00bdd4d0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd434 bytes b7f60194
+ 00bdd4d0 bytes c4f60194
- 00bdd43c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
- 00bdd43c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd4d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00bdd4d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd43c bytes 809206f9
+ 00bdd4d8 bytes 801207f9
- 00bdd410 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
- 00bdd410 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd4ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00bdd4ac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd410 bytes 819246f9
+ 00bdd4ac bytes 811247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d095b308feb99519c551cbb85d72dab6"></a>

### [`00bdd46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd46c.md) → [`00bdd508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd508.md) _ZN8firebase4auth4user10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bdd524",
      "incomplete_value": false,
      "site": "00bdd528",
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
      "definition_site": "00bdd488",
      "incomplete_value": false,
      "site": "00bdd48c",
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
      "definition_site": "00bdd534",
      "incomplete_value": true,
      "site": "00bdd540",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdd498",
      "incomplete_value": true,
      "site": "00bdd4a4",
      "value": [
        "LOAD",
        "8",
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
      "00bdd524",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bdd534",
      "DATA",
      [
        "storage",
        "01126da8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdd524",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bdd534",
      "DATA",
      [
        "storage",
        "01126ea8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd46c.md#insn-00bdd48c) · [`00bdd488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd46c.md#insn-00bdd488) · [`00bdd494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd46c.md#insn-00bdd494)
- 新版 [`00bdd528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd508.md#insn-00bdd528) · [`00bdd524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd508.md#insn-00bdd524) · [`00bdd530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd508.md#insn-00bdd530)

~~~diff
- 00bdd48c ["INT_ADD", "register:40f0:8", ["const:bdd48c:8", "const:4:8"]]
- 00bdd48c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdd528 ["INT_ADD", "register:40f0:8", ["const:bdd528:8", "const:4:8"]]
+ 00bdd528 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdd48c bytes ddf60194
+ 00bdd528 bytes eaf60194
- 00bdd488 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bdd488 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd488 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd488 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd524 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bdd524 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd524 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd524 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdd488 bytes 00781491
+ 00bdd524 bytes 00341591
- 00bdd494 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 00bdd494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdd530 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00bdd530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdd494 bytes 08a13691
+ 00bdd530 bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc706d2bcb4e3997c4c2e8c2917a135a"></a>

### [`00bdd4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd4a8.md) → [`00bdd544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd544.md) _ZN8firebase4auth8userinfo19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00bdd570",
      "incomplete_value": true,
      "site": "00bdd570",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd4d4",
      "incomplete_value": true,
      "site": "00bdd4d4",
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
            "const:db0:8"
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
      "definition_site": "00bdd558",
      "incomplete_value": true,
      "site": "00bdd558",
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
      "definition_site": "00bdd4bc",
      "incomplete_value": true,
      "site": "00bdd4bc",
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
      "definition_site": "00bdd564",
      "incomplete_value": false,
      "site": "00bdd568",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd4c8",
      "incomplete_value": false,
      "site": "00bdd4cc",
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
            "const:77c:8"
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
      "00bdd554",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd564",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ],
    [
      "00bdd570",
      "WRITE",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd554",
      "READ",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd564",
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ],
    [
      "00bdd570",
      "WRITE",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd4a8.md#insn-00bdd4cc) · [`00bdd4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd4a8.md#insn-00bdd4d4) · [`00bdd4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd4a8.md#insn-00bdd4b8)
- 新版 [`00bdd568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd544.md#insn-00bdd568) · [`00bdd570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd544.md#insn-00bdd570) · [`00bdd554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd544.md#insn-00bdd554)

~~~diff
- 00bdd4cc ["INT_ADD", "register:40f0:8", ["const:bdd4cc:8", "const:4:8"]]
- 00bdd4cc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd568 ["INT_ADD", "register:40f0:8", ["const:bdd568:8", "const:4:8"]]
+ 00bdd568 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd4cc bytes 91f60194
+ 00bdd568 bytes 9ef60194
- 00bdd4d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00bdd4d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd570 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bdd570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd4d4 bytes 60da06f9
+ 00bdd570 bytes 605a07f9
- 00bdd4b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00bdd4b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd554 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bdd554 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd4b8 bytes 68da46f9
+ 00bdd554 bytes 685a47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dec2964f4ce2105565e7e7b91d396783"></a>

### [`00bdd4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd4e8.md) → [`00bdd584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd584.md) _ZN8firebase4auth8userinfo19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bdd5b0",
      "incomplete_value": true,
      "site": "00bdd5b0",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd514",
      "incomplete_value": true,
      "site": "00bdd514",
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
            "const:db0:8"
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
      "definition_site": "00bdd598",
      "incomplete_value": true,
      "site": "00bdd598",
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
      "definition_site": "00bdd4fc",
      "incomplete_value": true,
      "site": "00bdd4fc",
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
      "definition_site": "00bdd5a0",
      "incomplete_value": false,
      "site": "00bdd5a8",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd504",
      "incomplete_value": false,
      "site": "00bdd50c",
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
            "const:77c:8"
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
      "00bdd594",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd5a0",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ],
    [
      "00bdd5b0",
      "WRITE",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd594",
      "READ",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd5a0",
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ],
    [
      "00bdd5b0",
      "WRITE",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd4e8.md#insn-00bdd50c) · [`00bdd514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd4e8.md#insn-00bdd514) · [`00bdd4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd4e8.md#insn-00bdd4f8)
- 新版 [`00bdd5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd584.md#insn-00bdd5a8) · [`00bdd5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd584.md#insn-00bdd5b0) · [`00bdd594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd584.md#insn-00bdd594)

~~~diff
- 00bdd50c ["INT_ADD", "register:40f0:8", ["const:bdd50c:8", "const:4:8"]]
- 00bdd50c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd5a8 ["INT_ADD", "register:40f0:8", ["const:bdd5a8:8", "const:4:8"]]
+ 00bdd5a8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd50c bytes 81f60194
+ 00bdd5a8 bytes 8ef60194
- 00bdd514 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00bdd514 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd5b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bdd5b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd514 bytes 60da06f9
+ 00bdd5b0 bytes 605a07f9
- 00bdd4f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00bdd4f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd594 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bdd594 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd4f8 bytes 68da46f9
+ 00bdd594 bytes 685a47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49331670b367d3e9b9cd1620e68802b9"></a>

### [`00bdd528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd528.md) → [`00bdd5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd5c4.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bdd5f4",
      "incomplete_value": true,
      "site": "00bdd5f4",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd558",
      "incomplete_value": true,
      "site": "00bdd558",
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
            "const:db0:8"
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
      "definition_site": "00bdd5d8",
      "incomplete_value": true,
      "site": "00bdd5d8",
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
      "definition_site": "00bdd53c",
      "incomplete_value": true,
      "site": "00bdd53c",
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
      "definition_site": "00bdd5e4",
      "incomplete_value": false,
      "site": "00bdd5ec",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd548",
      "incomplete_value": false,
      "site": "00bdd550",
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
            "const:77c:8"
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
      "00bdd5d4",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd5e4",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ],
    [
      "00bdd5f4",
      "WRITE",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd5d4",
      "READ",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd5e4",
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ],
    [
      "00bdd5f4",
      "WRITE",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd528.md#insn-00bdd550) · [`00bdd558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd528.md#insn-00bdd558) · [`00bdd538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd528.md#insn-00bdd538)
- 新版 [`00bdd5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd5c4.md#insn-00bdd5ec) · [`00bdd5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd5c4.md#insn-00bdd5f4) · [`00bdd5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd5c4.md#insn-00bdd5d4)

~~~diff
- 00bdd550 ["INT_ADD", "register:40f0:8", ["const:bdd550:8", "const:4:8"]]
- 00bdd550 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd5ec ["INT_ADD", "register:40f0:8", ["const:bdd5ec:8", "const:4:8"]]
+ 00bdd5ec ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd550 bytes 70f60194
+ 00bdd5ec bytes 7df60194
- 00bdd558 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00bdd558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd5f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bdd5f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd558 bytes 60da06f9
+ 00bdd5f4 bytes 605a07f9
- 00bdd538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00bdd538 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd5d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bdd5d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd538 bytes 68da46f9
+ 00bdd5d4 bytes 685a47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a099d336887e1fb44c3f583a5118eb4f"></a>

### [`00bdd56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd56c.md) → [`00bdd608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd608.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd638",
      "incomplete_value": true,
      "site": "00bdd638",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd59c",
      "incomplete_value": true,
      "site": "00bdd59c",
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
            "const:db0:8"
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
      "definition_site": "00bdd61c",
      "incomplete_value": true,
      "site": "00bdd61c",
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
      "definition_site": "00bdd580",
      "incomplete_value": true,
      "site": "00bdd580",
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
      "definition_site": "00bdd624",
      "incomplete_value": false,
      "site": "00bdd630",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd588",
      "incomplete_value": false,
      "site": "00bdd594",
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
            "const:77c:8"
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
      "00bdd618",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd624",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ],
    [
      "00bdd638",
      "WRITE",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd618",
      "READ",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd624",
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ],
    [
      "00bdd638",
      "WRITE",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd56c.md#insn-00bdd594) · [`00bdd59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd56c.md#insn-00bdd59c) · [`00bdd57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd56c.md#insn-00bdd57c)
- 新版 [`00bdd630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd608.md#insn-00bdd630) · [`00bdd638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd608.md#insn-00bdd638) · [`00bdd618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd608.md#insn-00bdd618)

~~~diff
- 00bdd594 ["INT_ADD", "register:40f0:8", ["const:bdd594:8", "const:4:8"]]
- 00bdd594 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd630 ["INT_ADD", "register:40f0:8", ["const:bdd630:8", "const:4:8"]]
+ 00bdd630 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd594 bytes 5ff60194
+ 00bdd630 bytes 6cf60194
- 00bdd59c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00bdd59c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd638 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bdd638 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd59c bytes 60da06f9
+ 00bdd638 bytes 605a07f9
- 00bdd57c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00bdd57c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd618 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bdd618 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd57c bytes 68da46f9
+ 00bdd618 bytes 685a47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b2a95165d01c7d2db492924615d88a5"></a>

### [`00bdd5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd5bc.md) → [`00bdd658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd658.md) _ZN8firebase4auth8userinfo15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bdd6b0",
      "incomplete_value": true,
      "site": "00bdd6b0",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd614",
      "incomplete_value": true,
      "site": "00bdd614",
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
            "const:db8:8"
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
      "definition_site": "00bdd68c",
      "incomplete_value": true,
      "site": "00bdd698",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd5f0",
      "incomplete_value": true,
      "site": "00bdd5fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db0:8"
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
      "00bdd66c",
      "READ",
      [
        "storage",
        "01126db8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd68c",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd6b0",
      "WRITE",
      [
        "storage",
        "01126db8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd66c",
      "READ",
      [
        "storage",
        "01126eb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd68c",
      "READ",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd6b0",
      "WRITE",
      [
        "storage",
        "01126eb8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd5bc.md#insn-00bdd5fc) · [`00bdd614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd5bc.md#insn-00bdd614) · [`00bdd5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd5bc.md#insn-00bdd5d0)
- 新版 [`00bdd698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd658.md#insn-00bdd698) · [`00bdd6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd658.md#insn-00bdd6b0) · [`00bdd66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd658.md#insn-00bdd66c)

~~~diff
- 00bdd5fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdd5fc ["INT_ADD", "register:40f0:8", ["const:bdd5fc:8", "const:4:8"]]
- 00bdd5fc ["CALLIND", null, ["register:0:8"]]
+ 00bdd698 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd698 ["INT_ADD", "register:40f0:8", ["const:bdd698:8", "const:4:8"]]
+ 00bdd698 ["CALLIND", null, ["register:0:8"]]
- 00bdd5fc bytes 00013fd6
+ 00bdd698 bytes 00013fd6
- 00bdd614 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bdd614 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:db8:8"]]
- 00bdd614 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bdd6b0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bdd6b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:eb8:8"]]
+ 00bdd6b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bdd614 bytes a0e23639
+ 00bdd6b0 bytes a0e23a39
- 00bdd5d0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:db8:8"]]
- 00bdd5d0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bdd5d0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bdd66c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:eb8:8"]]
+ 00bdd66c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd66c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bdd5d0 bytes a8e27639
+ 00bdd66c bytes a8e27a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e95de907c061c2e19d4546befd96bdc"></a>

### [`00bdd628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd628.md) → [`00bdd6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd6c4.md) _ZN8firebase4auth8userinfo12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bdd700",
      "incomplete_value": true,
      "site": "00bdd700",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd664",
      "incomplete_value": true,
      "site": "00bdd664",
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
            "const:db8:8"
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
      "definition_site": "00bdd720",
      "incomplete_value": true,
      "site": "00bdd720",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd684",
      "incomplete_value": true,
      "site": "00bdd684",
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
            "const:db0:8"
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
      "definition_site": "00bdd6dc",
      "incomplete_value": true,
      "site": "00bdd6dc",
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
      "definition_site": "00bdd640",
      "incomplete_value": true,
      "site": "00bdd640",
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
      "00bdd6d8",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd6e4",
      "READ",
      [
        "storage",
        "01126db8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd700",
      "WRITE",
      [
        "storage",
        "01126db8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd6d8",
      "READ",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd6e4",
      "READ",
      [
        "storage",
        "01126eb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd700",
      "WRITE",
      [
        "storage",
        "01126eb8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd628.md#insn-00bdd664) · [`00bdd680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd628.md#insn-00bdd680) · [`00bdd684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd628.md#insn-00bdd684)
- 新版 [`00bdd700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd6c4.md#insn-00bdd700) · [`00bdd71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd6c4.md#insn-00bdd71c) · [`00bdd720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd6c4.md#insn-00bdd720)

~~~diff
- 00bdd664 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bdd664 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bdd664 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:db8:8"]]
- 00bdd664 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdd700 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdd700 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdd700 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:eb8:8"]]
+ 00bdd700 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bdd664 bytes bfe23639
+ 00bdd700 bytes bfe23a39
- 00bdd680 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdd680 ["INT_ADD", "register:40f0:8", ["const:bdd680:8", "const:4:8"]]
- 00bdd680 ["CALLIND", null, ["register:0:8"]]
+ 00bdd71c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd71c ["INT_ADD", "register:40f0:8", ["const:bdd71c:8", "const:4:8"]]
+ 00bdd71c ["CALLIND", null, ["register:0:8"]]
- 00bdd680 bytes 00013fd6
+ 00bdd71c bytes 00013fd6
- 00bdd684 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
- 00bdd684 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bdd684 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdd720 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:eb0:8"]]
+ 00bdd720 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdd720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bdd684 bytes 9fda06f9
+ 00bdd720 bytes 9f5a07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b3b0c5a64bf51f8c952244082154faf"></a>

### [`00bdd698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd698.md) → [`00bdd734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd734.md) _ZN8firebase4auth8userinfo14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "site": "00bdd6d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd774"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdd6b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd6ac",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdd6b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd778"
      ]
    ],
    [
      "unmatched:00bdd6bc",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdd748",
      "READ",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd750",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd778"
      ]
    ],
    [
      "00bdd758",
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd698.md#insn-00bdd6b4) · [`00bdd6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd698.md#insn-00bdd6d0) · [`00bdd6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd698.md#insn-00bdd6d8)
- 新版 [`00bdd76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd734.md#insn-00bdd76c)

~~~diff
- 00bdd6b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bdd6b4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bdd6b4 bytes 410100b5
- 00bdd6d0 ["INT_ADD", "register:40f0:8", ["const:bdd6d0:8", "const:4:8"]]
- 00bdd6d0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd76c ["INT_ADD", "register:40f0:8", ["const:bdd76c:8", "const:4:8"]]
+ 00bdd76c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd6d0 bytes 10f60194
+ 00bdd76c bytes 1df60194
- 00bdd6d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
- 00bdd6d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd6d8 bytes 80da06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dc8d9927f6717c59d068ee910ad9c82"></a>

### [`00bdd744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd744.md) → [`00bdd7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd7e0.md) _ZN8firebase4auth8userinfo13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd820",
      "incomplete_value": true,
      "site": "00bdd820",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd784",
      "incomplete_value": true,
      "site": "00bdd784",
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
            "const:db0:8"
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
      "definition_site": "00bdd7fc",
      "incomplete_value": true,
      "site": "00bdd7fc",
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
      "definition_site": "00bdd760",
      "incomplete_value": true,
      "site": "00bdd760",
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
      "definition_site": "00bdd804",
      "incomplete_value": false,
      "site": "00bdd818",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd768",
      "incomplete_value": false,
      "site": "00bdd77c",
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
            "const:77c:8"
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
      "00bdd7f4",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd804",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ],
    [
      "00bdd820",
      "WRITE",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd7f4",
      "READ",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd804",
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ],
    [
      "00bdd820",
      "WRITE",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd744.md#insn-00bdd77c) · [`00bdd784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd744.md#insn-00bdd784) · [`00bdd758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd744.md#insn-00bdd758)
- 新版 [`00bdd818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd7e0.md#insn-00bdd818) · [`00bdd820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd7e0.md#insn-00bdd820) · [`00bdd7f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd7e0.md#insn-00bdd7f4)

~~~diff
- 00bdd77c ["INT_ADD", "register:40f0:8", ["const:bdd77c:8", "const:4:8"]]
- 00bdd77c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd818 ["INT_ADD", "register:40f0:8", ["const:bdd818:8", "const:4:8"]]
+ 00bdd818 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd77c bytes e5f50194
+ 00bdd818 bytes f2f50194
- 00bdd784 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
- 00bdd784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd820 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:eb0:8"]]
+ 00bdd820 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd784 bytes 80da06f9
+ 00bdd820 bytes 805a07f9
- 00bdd758 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
- 00bdd758 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd7f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:eb0:8"]]
+ 00bdd7f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd758 bytes 81da46f9
+ 00bdd7f4 bytes 815a47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-401100fa8a950fbdef2a7646373567f5"></a>

### [`00bdd7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd7b4.md) → [`00bdd850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd850.md) _ZN8firebase4auth8userinfo10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bdd86c",
      "incomplete_value": false,
      "site": "00bdd870",
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
      "definition_site": "00bdd7d0",
      "incomplete_value": false,
      "site": "00bdd7d4",
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
      "definition_site": "00bdd87c",
      "incomplete_value": true,
      "site": "00bdd888",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdd7e0",
      "incomplete_value": true,
      "site": "00bdd7ec",
      "value": [
        "LOAD",
        "8",
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
      "00bdd86c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bdd87c",
      "DATA",
      [
        "storage",
        "01126df8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdd86c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bdd87c",
      "DATA",
      [
        "storage",
        "01126ef8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd7b4.md#insn-00bdd7d4) · [`00bdd7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd7b4.md#insn-00bdd7d0) · [`00bdd7dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd7b4.md#insn-00bdd7dc)
- 新版 [`00bdd870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd850.md#insn-00bdd870) · [`00bdd86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd850.md#insn-00bdd86c) · [`00bdd878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd850.md#insn-00bdd878)

~~~diff
- 00bdd7d4 ["INT_ADD", "register:40f0:8", ["const:bdd7d4:8", "const:4:8"]]
- 00bdd7d4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdd870 ["INT_ADD", "register:40f0:8", ["const:bdd870:8", "const:4:8"]]
+ 00bdd870 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdd7d4 bytes 0bf60194
+ 00bdd870 bytes 18f60194
- 00bdd7d0 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bdd7d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd7d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd7d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd86c ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bdd86c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd86c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd86c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdd7d0 bytes 00781491
+ 00bdd86c bytes 00341591
- 00bdd7dc ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00bdd7dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd7dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd7dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdd878 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 00bdd878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdd7dc bytes 08e13791
+ 00bdd878 bytes 08e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dc3b0a8e492fc0aa303c8aca31acc22"></a>

### [`00bdd7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd7f0.md) → [`00bdd88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd88c.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00bdd8b8",
      "incomplete_value": true,
      "site": "00bdd8b8",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd81c",
      "incomplete_value": true,
      "site": "00bdd81c",
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
            "const:e00:8"
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
      "definition_site": "00bdd8a0",
      "incomplete_value": true,
      "site": "00bdd8a0",
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
      "definition_site": "00bdd804",
      "incomplete_value": true,
      "site": "00bdd804",
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
      "definition_site": "00bdd8ac",
      "incomplete_value": false,
      "site": "00bdd8b0",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd810",
      "incomplete_value": false,
      "site": "00bdd814",
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
      "00bdd89c",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd8ac",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ],
    [
      "00bdd8b8",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd89c",
      "READ",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd8ac",
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ],
    [
      "00bdd8b8",
      "WRITE",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd7f0.md#insn-00bdd814) · [`00bdd81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd7f0.md#insn-00bdd81c) · [`00bdd800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd7f0.md#insn-00bdd800)
- 新版 [`00bdd8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd88c.md#insn-00bdd8b0) · [`00bdd8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd88c.md#insn-00bdd8b8) · [`00bdd89c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd88c.md#insn-00bdd89c)

~~~diff
- 00bdd814 ["INT_ADD", "register:40f0:8", ["const:bdd814:8", "const:4:8"]]
- 00bdd814 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd8b0 ["INT_ADD", "register:40f0:8", ["const:bdd8b0:8", "const:4:8"]]
+ 00bdd8b0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd814 bytes bff50194
+ 00bdd8b0 bytes ccf50194
- 00bdd81c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
- 00bdd81c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd8b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f00:8"]]
+ 00bdd8b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd81c bytes 600207f9
+ 00bdd8b8 bytes 608207f9
- 00bdd800 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
- 00bdd800 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd89c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f00:8"]]
+ 00bdd89c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd800 bytes 680247f9
+ 00bdd89c bytes 688247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f65db2d0b169dd24b159943ab6ec341"></a>

### [`00bdd830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd830.md) → [`00bdd8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd8cc.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bdd8f8",
      "incomplete_value": true,
      "site": "00bdd8f8",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd85c",
      "incomplete_value": true,
      "site": "00bdd85c",
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
            "const:e00:8"
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
      "definition_site": "00bdd8e0",
      "incomplete_value": true,
      "site": "00bdd8e0",
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
      "definition_site": "00bdd844",
      "incomplete_value": true,
      "site": "00bdd844",
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
      "definition_site": "00bdd8e8",
      "incomplete_value": false,
      "site": "00bdd8f0",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd84c",
      "incomplete_value": false,
      "site": "00bdd854",
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
      "00bdd8dc",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd8e8",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ],
    [
      "00bdd8f8",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd8dc",
      "READ",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd8e8",
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ],
    [
      "00bdd8f8",
      "WRITE",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd830.md#insn-00bdd854) · [`00bdd85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd830.md#insn-00bdd85c) · [`00bdd840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd830.md#insn-00bdd840)
- 新版 [`00bdd8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd8cc.md#insn-00bdd8f0) · [`00bdd8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd8cc.md#insn-00bdd8f8) · [`00bdd8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd8cc.md#insn-00bdd8dc)

~~~diff
- 00bdd854 ["INT_ADD", "register:40f0:8", ["const:bdd854:8", "const:4:8"]]
- 00bdd854 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd8f0 ["INT_ADD", "register:40f0:8", ["const:bdd8f0:8", "const:4:8"]]
+ 00bdd8f0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd854 bytes aff50194
+ 00bdd8f0 bytes bcf50194
- 00bdd85c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
- 00bdd85c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd8f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f00:8"]]
+ 00bdd8f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd85c bytes 600207f9
+ 00bdd8f8 bytes 608207f9
- 00bdd840 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
- 00bdd840 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd8dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f00:8"]]
+ 00bdd8dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd840 bytes 680247f9
+ 00bdd8dc bytes 688247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbe78069cd7c08f1df8b92e5d69d87f8"></a>

### [`00bdd870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd870.md) → [`00bdd90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd90c.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bdd93c",
      "incomplete_value": true,
      "site": "00bdd93c",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd8a0",
      "incomplete_value": true,
      "site": "00bdd8a0",
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
            "const:e00:8"
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
      "definition_site": "00bdd920",
      "incomplete_value": true,
      "site": "00bdd920",
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
      "definition_site": "00bdd884",
      "incomplete_value": true,
      "site": "00bdd884",
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
      "definition_site": "00bdd92c",
      "incomplete_value": false,
      "site": "00bdd934",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd890",
      "incomplete_value": false,
      "site": "00bdd898",
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
      "00bdd91c",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd92c",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ],
    [
      "00bdd93c",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd91c",
      "READ",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd92c",
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ],
    [
      "00bdd93c",
      "WRITE",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd870.md#insn-00bdd898) · [`00bdd8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd870.md#insn-00bdd8a0) · [`00bdd880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd870.md#insn-00bdd880)
- 新版 [`00bdd934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd90c.md#insn-00bdd934) · [`00bdd93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd90c.md#insn-00bdd93c) · [`00bdd91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd90c.md#insn-00bdd91c)

~~~diff
- 00bdd898 ["INT_ADD", "register:40f0:8", ["const:bdd898:8", "const:4:8"]]
- 00bdd898 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd934 ["INT_ADD", "register:40f0:8", ["const:bdd934:8", "const:4:8"]]
+ 00bdd934 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd898 bytes 9ef50194
+ 00bdd934 bytes abf50194
- 00bdd8a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
- 00bdd8a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd93c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f00:8"]]
+ 00bdd93c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd8a0 bytes 600207f9
+ 00bdd93c bytes 608207f9
- 00bdd880 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
- 00bdd880 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd91c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f00:8"]]
+ 00bdd91c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd880 bytes 680247f9
+ 00bdd91c bytes 688247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41b9f0ec0739f276616ec459234d14c8"></a>

### [`00bdd8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd8b4.md) → [`00bdd950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd950.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00bdd8e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd980"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bdd964",
      "incomplete_value": true,
      "site": "00bdd964",
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
      "definition_site": "00bdd8c8",
      "incomplete_value": true,
      "site": "00bdd8c8",
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
      "00bdd960",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd964",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bdd8e8"
      ]
    ],
    [
      "unmatched:00bdd8d0",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdd960",
      "READ",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd964",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd984"
      ]
    ],
    [
      "00bdd96c",
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd8b4.md#insn-00bdd8dc) · [`00bdd8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd8b4.md#insn-00bdd8e4) · [`00bdd8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd8b4.md#insn-00bdd8f4)
- 新版 [`00bdd978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd950.md#insn-00bdd978)

~~~diff
- 00bdd8dc ["INT_ADD", "register:40f0:8", ["const:bdd8dc:8", "const:4:8"]]
- 00bdd8dc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdd978 ["INT_ADD", "register:40f0:8", ["const:bdd978:8", "const:4:8"]]
+ 00bdd978 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdd8dc bytes 8df50194
+ 00bdd978 bytes 9af50194
- 00bdd8e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
- 00bdd8e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd8e4 bytes 600207f9
- 00bdd8f4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bdd8f4 ["RETURN", null, ["register:0:8"]]
- 00bdd8f4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1d060a322373a114240506ea8ab0f75"></a>

### [`00bdd970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd970.md) → [`00bdda0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdda0c.md) _ZN8firebase4auth8metadata12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bdda48",
      "incomplete_value": true,
      "site": "00bdda48",
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
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd9ac",
      "incomplete_value": true,
      "site": "00bdd9ac",
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
            "const:e08:8"
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
      "definition_site": "00bdda68",
      "incomplete_value": true,
      "site": "00bdda68",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd9cc",
      "incomplete_value": true,
      "site": "00bdd9cc",
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
            "const:e00:8"
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
      "definition_site": "00bdda24",
      "incomplete_value": true,
      "site": "00bdda24",
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
      "definition_site": "00bdd988",
      "incomplete_value": true,
      "site": "00bdd988",
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
      "00bdda20",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdda2c",
      "READ",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdda48",
      "WRITE",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdda20",
      "READ",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdda2c",
      "READ",
      [
        "storage",
        "01126f08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdda48",
      "WRITE",
      [
        "storage",
        "01126f08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd970.md#insn-00bdd9ac) · [`00bdd9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd970.md#insn-00bdd9c8) · [`00bdd9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd970.md#insn-00bdd9cc)
- 新版 [`00bdda48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdda0c.md#insn-00bdda48) · [`00bdda64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdda0c.md#insn-00bdda64) · [`00bdda68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdda0c.md#insn-00bdda68)

~~~diff
- 00bdd9ac ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bdd9ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bdd9ac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e08:8"]]
- 00bdd9ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdda48 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdda48 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdda48 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:f08:8"]]
+ 00bdda48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bdd9ac bytes bf223839
+ 00bdda48 bytes bf223c39
- 00bdd9c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdd9c8 ["INT_ADD", "register:40f0:8", ["const:bdd9c8:8", "const:4:8"]]
- 00bdd9c8 ["CALLIND", null, ["register:0:8"]]
+ 00bdda64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdda64 ["INT_ADD", "register:40f0:8", ["const:bdda64:8", "const:4:8"]]
+ 00bdda64 ["CALLIND", null, ["register:0:8"]]
- 00bdd9c8 bytes 00013fd6
+ 00bdda64 bytes 00013fd6
- 00bdd9cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
- 00bdd9cc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bdd9cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdda68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f00:8"]]
+ 00bdda68 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdda68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bdd9cc bytes 9f0207f9
+ 00bdda68 bytes 9f8207f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feb49f3f76328d55cbfedb6b3eb78678"></a>

### [`00bdd9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd9e0.md) → [`00bdda7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdda7c.md) _ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bddabc",
      "incomplete_value": true,
      "site": "00bddabc",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdda20",
      "incomplete_value": true,
      "site": "00bdda20",
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
            "const:e00:8"
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
      "definition_site": "00bdda98",
      "incomplete_value": true,
      "site": "00bdda98",
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
      "definition_site": "00bdd9fc",
      "incomplete_value": true,
      "site": "00bdd9fc",
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
      "definition_site": "00bddaa0",
      "incomplete_value": false,
      "site": "00bddab4",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdda04",
      "incomplete_value": false,
      "site": "00bdda18",
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
      "00bdda90",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddaa0",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ],
    [
      "00bddabc",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdda90",
      "READ",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddaa0",
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ],
    [
      "00bddabc",
      "WRITE",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdda18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd9e0.md#insn-00bdda18) · [`00bdda20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd9e0.md#insn-00bdda20) · [`00bdd9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd9e0.md#insn-00bdd9f4)
- 新版 [`00bddab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdda7c.md#insn-00bddab4) · [`00bddabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdda7c.md#insn-00bddabc) · [`00bdda90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdda7c.md#insn-00bdda90)

~~~diff
- 00bdda18 ["INT_ADD", "register:40f0:8", ["const:bdda18:8", "const:4:8"]]
- 00bdda18 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bddab4 ["INT_ADD", "register:40f0:8", ["const:bddab4:8", "const:4:8"]]
+ 00bddab4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdda18 bytes 3ef50194
+ 00bddab4 bytes 4bf50194
- 00bdda20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
- 00bdda20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bddabc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f00:8"]]
+ 00bddabc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdda20 bytes 800207f9
+ 00bddabc bytes 808207f9
- 00bdd9f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
- 00bdd9f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdda90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f00:8"]]
+ 00bdda90 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd9f4 bytes 810247f9
+ 00bdda90 bytes 818247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-758c1b970145903a7ff4451fcbc66c51"></a>

### [`00bdda50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdda50.md) → [`00bddaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddaec.md) _ZN8firebase4auth8metadata11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bddb08",
      "incomplete_value": false,
      "site": "00bddb0c",
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
      "definition_site": "00bdda6c",
      "incomplete_value": false,
      "site": "00bdda70",
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
      "definition_site": "00bddb18",
      "incomplete_value": true,
      "site": "00bddb24",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdda7c",
      "incomplete_value": true,
      "site": "00bdda88",
      "value": [
        "LOAD",
        "8",
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
      "00bddb08",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bddb18",
      "DATA",
      [
        "storage",
        "01126e10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bddb08",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bddb18",
      "DATA",
      [
        "storage",
        "01126f10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdda70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdda50.md#insn-00bdda70) · [`00bdda6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdda50.md#insn-00bdda6c) · [`00bdda78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdda50.md#insn-00bdda78)
- 新版 [`00bddb0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddaec.md#insn-00bddb0c) · [`00bddb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddaec.md#insn-00bddb08) · [`00bddb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddaec.md#insn-00bddb14)

~~~diff
- 00bdda70 ["INT_ADD", "register:40f0:8", ["const:bdda70:8", "const:4:8"]]
- 00bdda70 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bddb0c ["INT_ADD", "register:40f0:8", ["const:bddb0c:8", "const:4:8"]]
+ 00bddb0c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdda70 bytes 64f50194
+ 00bddb0c bytes 71f50194
- 00bdda6c ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bdda6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdda6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdda6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bddb08 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bddb08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bddb08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bddb08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdda6c bytes 009c0d91
+ 00bddb08 bytes 002c0c91
- 00bdda78 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 00bdda78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdda78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdda78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bddb14 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 00bddb14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bddb14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bddb14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdda78 bytes 08413891
+ 00bddb14 bytes 08413c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e335176b1900d5ebce627e6159b5dde"></a>

### [`00bdda8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdda8c.md) → [`00bddb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb28.md) _ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bddb68",
      "incomplete_value": true,
      "site": "00bddb68",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddacc",
      "incomplete_value": true,
      "site": "00bddacc",
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
            "const:e00:8"
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
      "definition_site": "00bddb44",
      "incomplete_value": true,
      "site": "00bddb44",
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
      "definition_site": "00bddaa8",
      "incomplete_value": true,
      "site": "00bddaa8",
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
      "definition_site": "00bddb4c",
      "incomplete_value": false,
      "site": "00bddb60",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddab0",
      "incomplete_value": false,
      "site": "00bddac4",
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
      "00bddb3c",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddb4c",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ],
    [
      "00bddb68",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bddb3c",
      "READ",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddb4c",
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ],
    [
      "00bddb68",
      "WRITE",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdda8c.md#insn-00bddac4) · [`00bddacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdda8c.md#insn-00bddacc) · [`00bddaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdda8c.md#insn-00bddaa0)
- 新版 [`00bddb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb28.md#insn-00bddb60) · [`00bddb68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb28.md#insn-00bddb68) · [`00bddb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb28.md#insn-00bddb3c)

~~~diff
- 00bddac4 ["INT_ADD", "register:40f0:8", ["const:bddac4:8", "const:4:8"]]
- 00bddac4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bddb60 ["INT_ADD", "register:40f0:8", ["const:bddb60:8", "const:4:8"]]
+ 00bddb60 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bddac4 bytes 13f50194
+ 00bddb60 bytes 20f50194
- 00bddacc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
- 00bddacc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bddb68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f00:8"]]
+ 00bddb68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bddacc bytes 800207f9
+ 00bddb68 bytes 808207f9
- 00bddaa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
- 00bddaa0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bddb3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f00:8"]]
+ 00bddb3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bddaa0 bytes 810247f9
+ 00bddb3c bytes 818247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-753c3bc6f36404acd22f5f3eae8907e3"></a>

### [`00bddafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddafc.md) → [`00bddb98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb98.md) _ZN8firebase4auth8metadata10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bddbb4",
      "incomplete_value": false,
      "site": "00bddbb8",
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
      "definition_site": "00bddb18",
      "incomplete_value": false,
      "site": "00bddb1c",
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
      "definition_site": "00bddbc4",
      "incomplete_value": true,
      "site": "00bddbd0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bddb28",
      "incomplete_value": true,
      "site": "00bddb34",
      "value": [
        "LOAD",
        "8",
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
      "00bddbb4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bddbc4",
      "DATA",
      [
        "storage",
        "01126e20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bddbb4",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bddbc4",
      "DATA",
      [
        "storage",
        "01126f20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddafc.md#insn-00bddb1c) · [`00bddb18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddafc.md#insn-00bddb18) · [`00bddb24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddafc.md#insn-00bddb24)
- 新版 [`00bddbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb98.md#insn-00bddbb8) · [`00bddbb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb98.md#insn-00bddbb4) · [`00bddbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb98.md#insn-00bddbc0)

~~~diff
- 00bddb1c ["INT_ADD", "register:40f0:8", ["const:bddb1c:8", "const:4:8"]]
- 00bddb1c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bddbb8 ["INT_ADD", "register:40f0:8", ["const:bddbb8:8", "const:4:8"]]
+ 00bddbb8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bddb1c bytes 39f50194
+ 00bddbb8 bytes 46f50194
- 00bddb18 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bddb18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bddb18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bddb18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bddbb4 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bddbb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bddbb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bddbb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bddb18 bytes 00781491
+ 00bddbb4 bytes 00341591
- 00bddb24 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00bddb24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bddb24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bddb24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bddbc0 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00bddbc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bddbc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bddbc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bddb24 bytes 08813891
+ 00bddbc0 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73f2fa1a6b2e934e6a9374a425d62865"></a>

### [`00bddb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddb38.md) → [`00bddbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddbd4.md) _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00bddc00",
      "incomplete_value": true,
      "site": "00bddc00",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddb64",
      "incomplete_value": true,
      "site": "00bddb64",
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
            "const:e28:8"
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
      "definition_site": "00bddbe8",
      "incomplete_value": true,
      "site": "00bddbe8",
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
      "definition_site": "00bddb4c",
      "incomplete_value": true,
      "site": "00bddb4c",
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
      "definition_site": "00bddbf4",
      "incomplete_value": false,
      "site": "00bddbf8",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddb58",
      "incomplete_value": false,
      "site": "00bddb5c",
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
            "const:488:8"
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
      "00bddbe4",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddbf4",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ],
    [
      "00bddc00",
      "WRITE",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bddbe4",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddbf4",
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      "00bddc00",
      "WRITE",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddb38.md#insn-00bddb5c) · [`00bddb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddb38.md#insn-00bddb64) · [`00bddb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddb38.md#insn-00bddb48)
- 新版 [`00bddbf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddbd4.md#insn-00bddbf8) · [`00bddc00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddbd4.md#insn-00bddc00) · [`00bddbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddbd4.md#insn-00bddbe4)

~~~diff
- 00bddb5c ["INT_ADD", "register:40f0:8", ["const:bddb5c:8", "const:4:8"]]
- 00bddb5c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bddbf8 ["INT_ADD", "register:40f0:8", ["const:bddbf8:8", "const:4:8"]]
+ 00bddbf8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bddb5c bytes edf40194
+ 00bddbf8 bytes faf40194
- 00bddb64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
- 00bddb64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bddc00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bddc00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bddb64 bytes 601607f9
+ 00bddc00 bytes 609607f9
- 00bddb48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
- 00bddb48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bddbe4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bddbe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bddb48 bytes 681647f9
+ 00bddbe4 bytes 689647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cdc94082acd089f8700f0fb140fbf37"></a>

### [`00bddb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddb78.md) → [`00bddc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc14.md) _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00bddc40",
      "incomplete_value": true,
      "site": "00bddc40",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddba4",
      "incomplete_value": true,
      "site": "00bddba4",
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
            "const:e28:8"
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
      "definition_site": "00bddc28",
      "incomplete_value": true,
      "site": "00bddc28",
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
      "definition_site": "00bddb8c",
      "incomplete_value": true,
      "site": "00bddb8c",
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
      "definition_site": "00bddc30",
      "incomplete_value": false,
      "site": "00bddc38",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddb94",
      "incomplete_value": false,
      "site": "00bddb9c",
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
            "const:488:8"
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
      "00bddc24",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddc30",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ],
    [
      "00bddc40",
      "WRITE",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bddc24",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddc30",
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      "00bddc40",
      "WRITE",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddb78.md#insn-00bddb9c) · [`00bddba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddb78.md#insn-00bddba4) · [`00bddb88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddb78.md#insn-00bddb88)
- 新版 [`00bddc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc14.md#insn-00bddc38) · [`00bddc40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc14.md#insn-00bddc40) · [`00bddc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc14.md#insn-00bddc24)

~~~diff
- 00bddb9c ["INT_ADD", "register:40f0:8", ["const:bddb9c:8", "const:4:8"]]
- 00bddb9c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bddc38 ["INT_ADD", "register:40f0:8", ["const:bddc38:8", "const:4:8"]]
+ 00bddc38 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bddb9c bytes ddf40194
+ 00bddc38 bytes eaf40194
- 00bddba4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
- 00bddba4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bddc40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bddc40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bddba4 bytes 601607f9
+ 00bddc40 bytes 609607f9
- 00bddb88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
- 00bddb88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bddc24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bddc24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bddb88 bytes 681647f9
+ 00bddc24 bytes 689647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee18a04115681de27b8b31ecb587787a"></a>

### [`00bddbb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddbb8.md) → [`00bddc54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc54.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bddc84",
      "incomplete_value": true,
      "site": "00bddc84",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddbe8",
      "incomplete_value": true,
      "site": "00bddbe8",
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
            "const:e28:8"
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
      "definition_site": "00bddc68",
      "incomplete_value": true,
      "site": "00bddc68",
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
      "definition_site": "00bddbcc",
      "incomplete_value": true,
      "site": "00bddbcc",
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
      "definition_site": "00bddc74",
      "incomplete_value": false,
      "site": "00bddc7c",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddbd8",
      "incomplete_value": false,
      "site": "00bddbe0",
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
            "const:488:8"
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
      "00bddc64",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddc74",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ],
    [
      "00bddc84",
      "WRITE",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bddc64",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddc74",
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      "00bddc84",
      "WRITE",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddbb8.md#insn-00bddbe0) · [`00bddbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddbb8.md#insn-00bddbe8) · [`00bddbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddbb8.md#insn-00bddbc8)
- 新版 [`00bddc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc54.md#insn-00bddc7c) · [`00bddc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc54.md#insn-00bddc84) · [`00bddc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc54.md#insn-00bddc64)

~~~diff
- 00bddbe0 ["INT_ADD", "register:40f0:8", ["const:bddbe0:8", "const:4:8"]]
- 00bddbe0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bddc7c ["INT_ADD", "register:40f0:8", ["const:bddc7c:8", "const:4:8"]]
+ 00bddc7c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bddbe0 bytes ccf40194
+ 00bddc7c bytes d9f40194
- 00bddbe8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
- 00bddbe8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bddc84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bddc84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bddbe8 bytes 601607f9
+ 00bddc84 bytes 609607f9
- 00bddbc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
- 00bddbc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bddc64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bddc64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bddbc8 bytes 681647f9
+ 00bddc64 bytes 689647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b916ab3be908e251c25844e2d8970296"></a>

### [`00bddbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddbfc.md) → [`00bddc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc98.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bddcc8",
      "incomplete_value": true,
      "site": "00bddcc8",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddc2c",
      "incomplete_value": true,
      "site": "00bddc2c",
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
            "const:e28:8"
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
      "definition_site": "00bddcac",
      "incomplete_value": true,
      "site": "00bddcac",
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
      "definition_site": "00bddc10",
      "incomplete_value": true,
      "site": "00bddc10",
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
      "definition_site": "00bddcb4",
      "incomplete_value": false,
      "site": "00bddcc0",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddc18",
      "incomplete_value": false,
      "site": "00bddc24",
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
            "const:488:8"
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
      "00bddca8",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddcb4",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ],
    [
      "00bddcc8",
      "WRITE",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bddca8",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddcb4",
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      "00bddcc8",
      "WRITE",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddbfc.md#insn-00bddc24) · [`00bddc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddbfc.md#insn-00bddc2c) · [`00bddc0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddbfc.md#insn-00bddc0c)
- 新版 [`00bddcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc98.md#insn-00bddcc0) · [`00bddcc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc98.md#insn-00bddcc8) · [`00bddca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc98.md#insn-00bddca8)

~~~diff
- 00bddc24 ["INT_ADD", "register:40f0:8", ["const:bddc24:8", "const:4:8"]]
- 00bddc24 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bddcc0 ["INT_ADD", "register:40f0:8", ["const:bddcc0:8", "const:4:8"]]
+ 00bddcc0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bddc24 bytes bbf40194
+ 00bddcc0 bytes c8f40194
- 00bddc2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
- 00bddc2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bddcc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bddcc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bddc2c bytes 601607f9
+ 00bddcc8 bytes 609607f9
- 00bddc0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
- 00bddc0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bddca8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bddca8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bddc0c bytes 681647f9
+ 00bddca8 bytes 689647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c307cbe4bd1f7d2a3f3cc0fe4bf6942d"></a>

### [`00bddc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddc4c.md) → [`00bddce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddce8.md) _ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bddd40",
      "incomplete_value": true,
      "site": "00bddd40",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddca4",
      "incomplete_value": true,
      "site": "00bddca4",
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
            "const:e30:8"
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
      "definition_site": "00bddd1c",
      "incomplete_value": true,
      "site": "00bddd28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddc80",
      "incomplete_value": true,
      "site": "00bddc8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
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
      "00bddcfc",
      "READ",
      [
        "storage",
        "01126e30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bddd1c",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddd40",
      "WRITE",
      [
        "storage",
        "01126e30",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bddcfc",
      "READ",
      [
        "storage",
        "01126f30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bddd1c",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddd40",
      "WRITE",
      [
        "storage",
        "01126f30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddc4c.md#insn-00bddc8c) · [`00bddca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddc4c.md#insn-00bddca4) · [`00bddc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddc4c.md#insn-00bddc60)
- 新版 [`00bddd28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddce8.md#insn-00bddd28) · [`00bddd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddce8.md#insn-00bddd40) · [`00bddcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddce8.md#insn-00bddcfc)

~~~diff
- 00bddc8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bddc8c ["INT_ADD", "register:40f0:8", ["const:bddc8c:8", "const:4:8"]]
- 00bddc8c ["CALLIND", null, ["register:0:8"]]
+ 00bddd28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bddd28 ["INT_ADD", "register:40f0:8", ["const:bddd28:8", "const:4:8"]]
+ 00bddd28 ["CALLIND", null, ["register:0:8"]]
- 00bddc8c bytes 00013fd6
+ 00bddd28 bytes 00013fd6
- 00bddca4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bddca4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e30:8"]]
- 00bddca4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bddd40 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bddd40 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:f30:8"]]
+ 00bddd40 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bddca4 bytes a0c23839
+ 00bddd40 bytes a0c23c39
- 00bddc60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e30:8"]]
- 00bddc60 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bddc60 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bddcfc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f30:8"]]
+ 00bddcfc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bddcfc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bddc60 bytes a8c27839
+ 00bddcfc bytes a8c27c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f032155871d00122734dfbe94817759a"></a>

### [`00bddcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddcb8.md) → [`00bddd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddd54.md) _ZN8firebase4auth18userprofilebuilder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bddd90",
      "incomplete_value": true,
      "site": "00bddd90",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddcf4",
      "incomplete_value": true,
      "site": "00bddcf4",
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
            "const:e30:8"
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
      "definition_site": "00bdddb0",
      "incomplete_value": true,
      "site": "00bdddb0",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddd14",
      "incomplete_value": true,
      "site": "00bddd14",
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
            "const:e28:8"
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
      "definition_site": "00bddd6c",
      "incomplete_value": true,
      "site": "00bddd6c",
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
      "definition_site": "00bddcd0",
      "incomplete_value": true,
      "site": "00bddcd0",
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
      "00bddd68",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddd74",
      "READ",
      [
        "storage",
        "01126e30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bddd90",
      "WRITE",
      [
        "storage",
        "01126e30",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bddd68",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddd74",
      "READ",
      [
        "storage",
        "01126f30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bddd90",
      "WRITE",
      [
        "storage",
        "01126f30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddcf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddcb8.md#insn-00bddcf4) · [`00bddd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddcb8.md#insn-00bddd10) · [`00bddd14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddcb8.md#insn-00bddd14)
- 新版 [`00bddd90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddd54.md#insn-00bddd90) · [`00bdddac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddd54.md#insn-00bdddac) · [`00bdddb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddd54.md#insn-00bdddb0)

~~~diff
- 00bddcf4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bddcf4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bddcf4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e30:8"]]
- 00bddcf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bddd90 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bddd90 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bddd90 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:f30:8"]]
+ 00bddd90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bddcf4 bytes bfc23839
+ 00bddd90 bytes bfc23c39
- 00bddd10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bddd10 ["INT_ADD", "register:40f0:8", ["const:bddd10:8", "const:4:8"]]
- 00bddd10 ["CALLIND", null, ["register:0:8"]]
+ 00bdddac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdddac ["INT_ADD", "register:40f0:8", ["const:bdddac:8", "const:4:8"]]
+ 00bdddac ["CALLIND", null, ["register:0:8"]]
- 00bddd10 bytes 00013fd6
+ 00bdddac bytes 00013fd6
- 00bddd14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e28:8"]]
- 00bddd14 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bddd14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdddb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f28:8"]]
+ 00bdddb0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdddb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bddd14 bytes 9f1607f9
+ 00bdddb0 bytes 9f9607f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94f819089fc8ff1345e3e76c605bcc46"></a>

### [`00bddd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddd28.md) → [`00bdddc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdddc4.md) _ZN8firebase4auth18userprofilebuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdde04",
      "incomplete_value": true,
      "site": "00bdde04",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddd68",
      "incomplete_value": true,
      "site": "00bddd68",
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
            "const:e28:8"
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
      "definition_site": "00bddde0",
      "incomplete_value": true,
      "site": "00bddde0",
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
      "definition_site": "00bddd44",
      "incomplete_value": true,
      "site": "00bddd44",
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
      "definition_site": "00bddde8",
      "incomplete_value": false,
      "site": "00bdddfc",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddd4c",
      "incomplete_value": false,
      "site": "00bddd60",
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
            "const:488:8"
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
      "00bdddd8",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddde8",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ],
    [
      "00bdde04",
      "WRITE",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdddd8",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddde8",
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      "00bdde04",
      "WRITE",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddd28.md#insn-00bddd60) · [`00bddd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddd28.md#insn-00bddd68) · [`00bddd3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddd28.md#insn-00bddd3c)
- 新版 [`00bdddfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdddc4.md#insn-00bdddfc) · [`00bdde04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdddc4.md#insn-00bdde04) · [`00bdddd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdddc4.md#insn-00bdddd8)

~~~diff
- 00bddd60 ["INT_ADD", "register:40f0:8", ["const:bddd60:8", "const:4:8"]]
- 00bddd60 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bdddfc ["INT_ADD", "register:40f0:8", ["const:bdddfc:8", "const:4:8"]]
+ 00bdddfc ["CALL", null, ["callee:00c5afe0:8"]]
- 00bddd60 bytes 6cf40194
+ 00bdddfc bytes 79f40194
- 00bddd68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e28:8"]]
- 00bddd68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdde04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f28:8"]]
+ 00bdde04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bddd68 bytes 801607f9
+ 00bdde04 bytes 809607f9
- 00bddd3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e28:8"]]
- 00bddd3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdddd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f28:8"]]
+ 00bdddd8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bddd3c bytes 811647f9
+ 00bdddd8 bytes 819647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fc0d5c7275d5a172ec1081cee429133"></a>

### [`00bddd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddd98.md) → [`00bdde34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde34.md) _ZN8firebase4auth18userprofilebuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bdde50",
      "incomplete_value": false,
      "site": "00bdde54",
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
      "definition_site": "00bdddb4",
      "incomplete_value": false,
      "site": "00bdddb8",
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
      "definition_site": "00bdde60",
      "incomplete_value": true,
      "site": "00bdde6c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdddc4",
      "incomplete_value": true,
      "site": "00bdddd0",
      "value": [
        "LOAD",
        "8",
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
      "00bdde50",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bdde60",
      "DATA",
      [
        "storage",
        "01126e38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdde50",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bdde60",
      "DATA",
      [
        "storage",
        "01126f38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdddb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddd98.md#insn-00bdddb8) · [`00bdddb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddd98.md#insn-00bdddb4) · [`00bdddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddd98.md#insn-00bdddc0)
- 新版 [`00bdde54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde34.md#insn-00bdde54) · [`00bdde50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde34.md#insn-00bdde50) · [`00bdde5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde34.md#insn-00bdde5c)

~~~diff
- 00bdddb8 ["INT_ADD", "register:40f0:8", ["const:bdddb8:8", "const:4:8"]]
- 00bdddb8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdde54 ["INT_ADD", "register:40f0:8", ["const:bdde54:8", "const:4:8"]]
+ 00bdde54 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdddb8 bytes 92f40194
+ 00bdde54 bytes 9ff40194
- 00bdddb4 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bdddb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdddb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdddb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdde50 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bdde50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdde50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdde50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdddb4 bytes 009c0d91
+ 00bdde50 bytes 002c0c91
- 00bdddc0 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 00bdddc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdddc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdddc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdde5c ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00bdde5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdde5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdde5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdddc0 bytes 08e13891
+ 00bdde5c bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec1de1c10f998035360c941bf5ad41d"></a>

### [`00bdddd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdddd4.md) → [`00bdde70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde70.md) _ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bdde14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bddeb0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdddf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bddde8",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdddf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bddeb4"
      ]
    ],
    [
      "unmatched:00bdddf8",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdde84",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdde8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bddeb4"
      ]
    ],
    [
      "00bdde94",
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdddf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdddd4.md#insn-00bdddf0) · [`00bdde0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdddd4.md#insn-00bdde0c) · [`00bdde14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdddd4.md#insn-00bdde14)
- 新版 [`00bddea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde70.md#insn-00bddea8)

~~~diff
- 00bdddf0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bdddf0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bdddf0 bytes 410100b5
- 00bdde0c ["INT_ADD", "register:40f0:8", ["const:bdde0c:8", "const:4:8"]]
- 00bdde0c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bddea8 ["INT_ADD", "register:40f0:8", ["const:bddea8:8", "const:4:8"]]
+ 00bddea8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bdde0c bytes 41f40194
+ 00bddea8 bytes 4ef40194
- 00bdde14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e28:8"]]
- 00bdde14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdde14 bytes 801607f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92c8f45a1f1f13e2d29b66f68f6ae429"></a>

### [`00bdde44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde44.md) → [`00bddee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddee0.md) _ZN8firebase4auth18userprofilebuilder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bddefc",
      "incomplete_value": false,
      "site": "00bddf00",
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
      "definition_site": "00bdde60",
      "incomplete_value": false,
      "site": "00bdde64",
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
      "definition_site": "00bddf0c",
      "incomplete_value": true,
      "site": "00bddf18",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdde70",
      "incomplete_value": true,
      "site": "00bdde7c",
      "value": [
        "LOAD",
        "8",
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
      "00bddefc",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bddf0c",
      "DATA",
      [
        "storage",
        "01126e58",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bddefc",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bddf0c",
      "DATA",
      [
        "storage",
        "01126f58",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdde64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde44.md#insn-00bdde64) · [`00bdde60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde44.md#insn-00bdde60) · [`00bdde6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde44.md#insn-00bdde6c)
- 新版 [`00bddf00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddee0.md#insn-00bddf00) · [`00bddefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddee0.md#insn-00bddefc) · [`00bddf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddee0.md#insn-00bddf08)

~~~diff
- 00bdde64 ["INT_ADD", "register:40f0:8", ["const:bdde64:8", "const:4:8"]]
- 00bdde64 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bddf00 ["INT_ADD", "register:40f0:8", ["const:bddf00:8", "const:4:8"]]
+ 00bddf00 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdde64 bytes 67f40194
+ 00bddf00 bytes 74f40194
- 00bdde60 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bdde60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdde60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdde60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bddefc ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bddefc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bddefc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bddefc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdde60 bytes 00781491
+ 00bddefc bytes 00341591
- 00bdde6c ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00bdde6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdde6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdde6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bddf08 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00bddf08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bddf08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bddf08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdde6c bytes 08613991
+ 00bddf08 bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b08f3ad841ff2b04db7243c32c330925"></a>

### [`00bdde80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde80.md) → [`00bddf1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddf1c.md) _ZN8firebase4auth18CacheUserMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5dc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc50.md) · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5dd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd20.md) · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.05% / 新版 78.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 17件, `store_condition` 1件, `store_destination` 5件

アドレスに依存する影響 `branch_value` 4件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bddf60",
      "incomplete_value": true,
      "site": "00bddf60",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddec4",
      "incomplete_value": true,
      "site": "00bddec4",
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
            "const:d00:8"
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
      "definition_site": "00bddfb8",
      "incomplete_value": true,
      "site": "00bddfb8",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddf1c",
      "incomplete_value": true,
      "site": "00bddf1c",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00bde010",
      "incomplete_value": true,
      "site": "00bde010",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddf74",
      "incomplete_value": true,
      "site": "00bddf74",
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
      "00bddf34",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddf44",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bddf60",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bddf34",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddf44",
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      "00bddf60",
      "WRITE",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde80.md#insn-00bddebc) · [`00bddec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde80.md#insn-00bddec4) · [`00bdded8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde80.md#insn-00bdded8)
- 新版 [`00bddf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddf1c.md#insn-00bddf58) · [`00bddf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddf1c.md#insn-00bddf60) · [`00bddf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddf1c.md#insn-00bddf74)

~~~diff
- 00bddebc ["INT_ADD", "register:40f0:8", ["const:bddebc:8", "const:4:8"]]
- 00bddebc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bddf58 ["INT_ADD", "register:40f0:8", ["const:bddf58:8", "const:4:8"]]
+ 00bddf58 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bddebc bytes 15f40194
+ 00bddf58 bytes 22f40194
- 00bddec4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d00:8"]]
- 00bddec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bddf60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e00:8"]]
+ 00bddf60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bddec4 bytes a08206f9
+ 00bddf60 bytes a00207f9
- 00bdded8 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00bdded8 ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
- 00bdded8 ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
- 00bdded8 ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
+ 00bddf74 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 00bddf74 ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
+ 00bddf74 ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
+ 00bddf74 ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
- 00bdded8 bytes 84403491
+ 00bddf74 bytes 84403891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b17bbed7398aba32a83ca32b70c08d71"></a>

### [`00bde06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde06c.md) → [`00bde108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde108.md) _ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5dc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc70.md) · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 1件 [`00c5dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd40.md) · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_value, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 29.81% / 新版 29.81%

CFGの説明率　旧版 13.33% / 新版 13.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bde0a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bde0c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bde0f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bde11c",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bde124",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bde0cc"
      ]
    ],
    [
      "unmatched:00bde090",
      "READ",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bde11c",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bde124",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bde168"
      ]
    ],
    [
      "00bde16c",
      "READ",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde06c.md#insn-00bde094) · [`00bde0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde06c.md#insn-00bde0a8) · [`00bde0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde06c.md#insn-00bde0c8)

~~~diff
- 00bde094 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00bde094 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bde094 bytes c8000034
- 00bde0a8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bde0a8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bde0a8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d08:8"]]
- 00bde0a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bde0a8 bytes bf223439
- 00bde0c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
- 00bde0c8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bde0c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bde0c8 bytes 9f8206f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f8072b28a722b55f34fab27ed2a5960"></a>

### [`00bde6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde6a4.md) → [`00bde740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde740.md) _ZN8firebase4auth15ReadTokenResultEP8_jobjectPNS0_18FutureCallbackDataINSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde818.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00bde8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde8b4.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde7c4",
      "incomplete_value": false,
      "site": "00bde7c8",
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
            "const:f2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde728",
      "incomplete_value": false,
      "site": "00bde72c",
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
            "const:eef:8"
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
      "definition_site": "00bde7d0",
      "incomplete_value": true,
      "site": "00bde7dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde734",
      "incomplete_value": true,
      "site": "00bde740",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "00bde7c4",
      "PARAM",
      [
        "storage",
        "002b6eef",
        null,
        "string"
      ]
    ],
    [
      "00bde7d0",
      "READ",
      [
        "storage",
        "01126d10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bde7c4",
      "PARAM",
      [
        "storage",
        "002b6f2f",
        null,
        "string"
      ]
    ],
    [
      "00bde7d0",
      "READ",
      [
        "storage",
        "01126e10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde6a4.md#insn-00bde72c) · [`00bde740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde6a4.md#insn-00bde740) · [`00bde6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde6a4.md#insn-00bde6e8)
- 新版 [`00bde7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde740.md#insn-00bde7c8) · [`00bde7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde740.md#insn-00bde7dc) · [`00bde784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde740.md#insn-00bde784)

~~~diff
- 00bde72c ["INT_ADD", "register:40f0:8", ["const:bde72c:8", "const:4:8"]]
- 00bde72c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bde7c8 ["INT_ADD", "register:40f0:8", ["const:bde7c8:8", "const:4:8"]]
+ 00bde7c8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bde72c bytes 35f20194
+ 00bde7c8 bytes 42f20194
- 00bde740 ["INT_ADD", "register:40f0:8", ["const:bde740:8", "const:4:8"]]
- 00bde740 ["CALL", null, ["callee:00497874:8"]]
+ 00bde7dc ["INT_ADD", "register:40f0:8", ["const:bde7dc:8", "const:4:8"]]
+ 00bde7dc ["CALL", null, ["callee:00497874:8"]]
- 00bde740 bytes 3de4e297
+ 00bde7dc bytes 26e4e297
- 00bde6e8 ["INT_ADD", "register:40f0:8", ["const:bde6e8:8", "const:4:8"]]
- 00bde6e8 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bde784 ["INT_ADD", "register:40f0:8", ["const:bde784:8", "const:4:8"]]
+ 00bde784 ["CALL", null, ["callee:00c5b150:8"]]
- 00bde6e8 bytes 66f20194
+ 00bde784 bytes 73f20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d032c60b6705583d97ea0efbdb1200fd"></a>

### [`00bdeb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdeb7c.md) → [`00bdec18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdec18.md) _ZNK8firebase4auth4User13provider_dataEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aab0.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 1件 [`00c5ab80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab80.md) · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.47% / 新版 73.47%

CFGの説明率　旧版 24.54% / 新版 24.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_condition` 2件, `store_value` 1件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdeb7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdeb7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdeb80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdeb7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdeb80",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdeb84",
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
      "00bdec18",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bdec1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bdec20",
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

- 旧版 [`00bdeb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdeb7c.md#insn-00bdeb7c) · [`00bdeb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdeb7c.md#insn-00bdeb80) · [`00bdeb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdeb7c.md#insn-00bdeb84)

~~~diff
- 00bdeb7c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bdeb7c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bdeb7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00bdeb7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bdeb7c bytes fc6fbaa9
- 00bdeb80 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bdeb80 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bdeb80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bdeb80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdeb80 bytes fa6701a9
- 00bdeb84 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bdeb84 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bdeb84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bdeb84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdeb84 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14ce65b83f4fe4fcbba2ffff87636afb"></a>

### [`00bdf458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf458.md) → [`00bdf4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf4f4.md) _ZNK8firebase4auth22AndroidWrappedUserInfo5emailEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 55.56% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf458"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf45c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf45c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf458",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdf45c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdf460",
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
      "00bdf4f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bdf4f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bdf4fc",
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

- 旧版 [`00bdf458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf458.md#insn-00bdf458) · [`00bdf45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf458.md#insn-00bdf45c) · [`00bdf460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf458.md#insn-00bdf460)

~~~diff
- 00bdf458 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bdf458 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bdf458 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bdf458 bytes f50f1df8
- 00bdf45c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bdf45c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bdf45c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bdf45c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdf45c bytes f44f01a9
- 00bdf460 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bdf460 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bdf460 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bdf460 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdf460 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a6bfb742a991cefd3e58dcda6e20787"></a>

### [`00bdf4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf4dc.md) → [`00bdf578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf578.md) _ZNK8firebase4auth22AndroidWrappedUserInfo12display_nameEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 75.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdf5a4",
      "incomplete_value": true,
      "site": "00bdf5b0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ed0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf508",
      "incomplete_value": true,
      "site": "00bdf514",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
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
      "unmatched:00bdf508",
      "READ",
      [
        "storage",
        "01126dd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf5a4",
      "READ",
      [
        "storage",
        "01126ed0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf4dc.md#insn-00bdf514) · [`00bdf4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf4dc.md#insn-00bdf4f8) · [`00bdf500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf4dc.md#insn-00bdf500)
- 新版 [`00bdf5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf578.md#insn-00bdf5b0) · [`00bdf594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf578.md#insn-00bdf594) · [`00bdf59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf578.md#insn-00bdf59c)

~~~diff
- 00bdf514 ["INT_ADD", "register:40f0:8", ["const:bdf514:8", "const:4:8"]]
- 00bdf514 ["CALL", null, ["callee:00497874:8"]]
+ 00bdf5b0 ["INT_ADD", "register:40f0:8", ["const:bdf5b0:8", "const:4:8"]]
+ 00bdf5b0 ["CALL", null, ["callee:00497874:8"]]
- 00bdf514 bytes c8e0e297
+ 00bdf5b0 bytes b1e0e297
- 00bdf4f8 ["INT_ADD", "register:40f0:8", ["const:bdf4f8:8", "const:4:8"]]
- 00bdf4f8 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bdf594 ["INT_ADD", "register:40f0:8", ["const:bdf594:8", "const:4:8"]]
+ 00bdf594 ["CALL", null, ["callee:00c5b150:8"]]
- 00bdf4f8 bytes e2ee0194
+ 00bdf594 bytes efee0194
- 00bdf500 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00bdf500 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bdf59c ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00bdf59c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bdf500 bytes f50000b4
+ 00bdf59c bytes f50000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c712e915c65fcc3fa169427517ad19c"></a>

### [`00bdf560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf560.md) → [`00bdf5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf5fc.md) _ZNK8firebase4auth22AndroidWrappedUserInfo9photo_urlEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b2f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b3c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 28.57% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdf614",
      "incomplete_value": true,
      "site": "00bdf618",
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
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf578",
      "incomplete_value": true,
      "site": "00bdf57c",
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
      "definition_site": "00bdf628",
      "incomplete_value": true,
      "site": "00bdf634",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf58c",
      "incomplete_value": true,
      "site": "00bdf598",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
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
      "site": "00bdf5e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf58c",
      "READ",
      [
        "storage",
        "01126de0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf628",
      "READ",
      [
        "storage",
        "01126ee0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf560.md#insn-00bdf57c) · [`00bdf598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf560.md#insn-00bdf598) · [`00bdf5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf560.md#insn-00bdf5e0)
- 新版 [`00bdf618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf5fc.md#insn-00bdf618) · [`00bdf634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf5fc.md#insn-00bdf634)

~~~diff
- 00bdf57c ["INT_ADD", "register:40f0:8", ["const:bdf57c:8", "const:4:8"]]
- 00bdf57c ["CALL", null, ["callee:00c5b150:8"]]
+ 00bdf618 ["INT_ADD", "register:40f0:8", ["const:bdf618:8", "const:4:8"]]
+ 00bdf618 ["CALL", null, ["callee:00c5b150:8"]]
- 00bdf57c bytes c1ee0194
+ 00bdf618 bytes ceee0194
- 00bdf598 ["INT_ADD", "register:40f0:8", ["const:bdf598:8", "const:4:8"]]
- 00bdf598 ["CALL", null, ["callee:00497874:8"]]
+ 00bdf634 ["INT_ADD", "register:40f0:8", ["const:bdf634:8", "const:4:8"]]
+ 00bdf634 ["CALL", null, ["callee:00497874:8"]]
- 00bdf598 bytes a7e0e297
+ 00bdf634 bytes 90e0e297
- 00bdf5e0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bdf5e0 ["RETURN", null, ["register:0:8"]]
- 00bdf5e0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9ea7d618e6799e4f9317b2989e1aa59"></a>

### [`00bdf5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf5e4.md) → [`00bdf680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf680.md) _ZNK8firebase4auth22AndroidWrappedUserInfo11provider_idEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 44.44% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdf698",
      "incomplete_value": true,
      "site": "00bdf69c",
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
      "definition_site": "00bdf5fc",
      "incomplete_value": true,
      "site": "00bdf600",
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
            "register:4048:8"
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
      "definition_site": "00bdf6ac",
      "incomplete_value": true,
      "site": "00bdf6b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf610",
      "incomplete_value": true,
      "site": "00bdf61c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
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
      "00bdf6ac",
      "READ",
      [
        "storage",
        "01126dc8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf6ac",
      "READ",
      [
        "storage",
        "01126ec8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf5e4.md#insn-00bdf600) · [`00bdf61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf5e4.md#insn-00bdf61c) · [`00bdf5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf5e4.md#insn-00bdf5fc)
- 新版 [`00bdf69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf680.md#insn-00bdf69c) · [`00bdf6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf680.md#insn-00bdf6b8)

~~~diff
- 00bdf600 ["INT_ADD", "register:40f0:8", ["const:bdf600:8", "const:4:8"]]
- 00bdf600 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bdf69c ["INT_ADD", "register:40f0:8", ["const:bdf69c:8", "const:4:8"]]
+ 00bdf69c ["CALL", null, ["callee:00c5b150:8"]]
- 00bdf600 bytes a0ee0194
+ 00bdf69c bytes adee0194
- 00bdf61c ["INT_ADD", "register:40f0:8", ["const:bdf61c:8", "const:4:8"]]
- 00bdf61c ["CALL", null, ["callee:00497874:8"]]
+ 00bdf6b8 ["INT_ADD", "register:40f0:8", ["const:bdf6b8:8", "const:4:8"]]
+ 00bdf6b8 ["CALL", null, ["callee:00497874:8"]]
- 00bdf61c bytes 86e0e297
+ 00bdf6b8 bytes 6fe0e297
- 00bdf5fc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bdf5fc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf5fc bytes 200140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acb2cdde249695defd66fad3dde1afea"></a>

### [`00bdf668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf668.md) → [`00bdf704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf704.md) _ZNK8firebase4auth22AndroidWrappedUserInfo12phone_numberEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 37.50% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdf730",
      "incomplete_value": true,
      "site": "00bdf73c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf694",
      "incomplete_value": true,
      "site": "00bdf6a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
      "definition_site": "00bdf744",
      "incomplete_value": true,
      "site": "00bdf748",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
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
      "00bdf730",
      "READ",
      [
        "storage",
        "01126dd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf730",
      "READ",
      [
        "storage",
        "01126ed8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf668.md#insn-00bdf6a0) · [`00bdf6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf668.md#insn-00bdf6ac) · [`00bdf684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf668.md#insn-00bdf684)
- 新版 [`00bdf73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf704.md#insn-00bdf73c) · [`00bdf748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf704.md#insn-00bdf748) · [`00bdf720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf704.md#insn-00bdf720)

~~~diff
- 00bdf6a0 ["INT_ADD", "register:40f0:8", ["const:bdf6a0:8", "const:4:8"]]
- 00bdf6a0 ["CALL", null, ["callee:00497874:8"]]
+ 00bdf73c ["INT_ADD", "register:40f0:8", ["const:bdf73c:8", "const:4:8"]]
+ 00bdf73c ["CALL", null, ["callee:00497874:8"]]
- 00bdf6a0 bytes 65e0e297
+ 00bdf73c bytes 4ee0e297
- 00bdf6ac ["INT_ADD", "register:40f0:8", ["const:bdf6ac:8", "const:4:8"]]
- 00bdf6ac ["CALL", null, ["callee:00c5b030:8"]]
+ 00bdf748 ["INT_ADD", "register:40f0:8", ["const:bdf748:8", "const:4:8"]]
+ 00bdf748 ["CALL", null, ["callee:00c5b030:8"]]
- 00bdf6ac bytes 2dee0194
+ 00bdf748 bytes 3aee0194
- 00bdf684 ["INT_ADD", "register:40f0:8", ["const:bdf684:8", "const:4:8"]]
- 00bdf684 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bdf720 ["INT_ADD", "register:40f0:8", ["const:bdf720:8", "const:4:8"]]
+ 00bdf720 ["CALL", null, ["callee:00c5b150:8"]]
- 00bdf684 bytes 7fee0194
+ 00bdf720 bytes 8cee0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77f696b2b36730f12fdd328254819afb"></a>

### [`00bdf750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf750.md) → [`00bdf7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf7ec.md) _ZN8firebase4auth4User14UpdatePasswordEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bd055c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd055c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 93.91% / 新版 93.91%

CFGの説明率　旧版 21.05% / 新版 21.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf7e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdf888",
      "incomplete_value": true,
      "site": "00bdf89c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf7ec",
      "incomplete_value": true,
      "site": "00bdf800",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf818"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdf888",
      "READ",
      [
        "storage",
        "01126d50",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdf8a4",
      "READ",
      [
        "storage",
        "00c9ba18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf8a4",
      "PARAM",
      [
        "storage",
        "00bd04c0",
        "_ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdf888",
      "READ",
      [
        "storage",
        "01126e50",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdf940",
      "READ",
      [
        "storage",
        "00c9bae8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf940",
      "PARAM",
      [
        "storage",
        "00bd055c",
        "_ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf750.md#insn-00bdf7e0) · [`00bdf800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf750.md#insn-00bdf800) · [`00bdf818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf750.md#insn-00bdf818)
- 新版 [`00bdf89c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf7ec.md#insn-00bdf89c)

~~~diff
- 00bdf7e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdf7e0 ["INT_ADD", "register:40f0:8", ["const:bdf7e0:8", "const:4:8"]]
- 00bdf7e0 ["CALLIND", null, ["register:0:8"]]
- 00bdf7e0 bytes 00013fd6
- 00bdf800 ["INT_ADD", "register:40f0:8", ["const:bdf800:8", "const:4:8"]]
- 00bdf800 ["CALL", null, ["callee:00497874:8"]]
+ 00bdf89c ["INT_ADD", "register:40f0:8", ["const:bdf89c:8", "const:4:8"]]
+ 00bdf89c ["CALL", null, ["callee:00497874:8"]]
- 00bdf800 bytes 0de0e297
+ 00bdf89c bytes f6dfe297
- 00bdf818 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdf818 ["INT_ADD", "register:40f0:8", ["const:bdf818:8", "const:4:8"]]
- 00bdf818 ["CALLIND", null, ["register:0:8"]]
- 00bdf818 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fd8d75046431e392664f4ca8682b473"></a>

### [`00bdf978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf978.md) → [`00bdfa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfa14.md) _ZN8firebase4auth4User17UpdateUserProfileERKNS1_11UserProfileE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bd04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00bd055c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd055c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.16% / 新版 88.16%

CFGの説明率　旧版 32.76% / 新版 29.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdfb98"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bdfc34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdfa68",
      "incomplete_value": true,
      "site": "00bdfa74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:10:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfa04",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdfa08",
      "READ",
      [
        "storage",
        "01126e38",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdfad8",
      "READ",
      [
        "storage",
        "01126e40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdfaa0",
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdfaa4",
      "READ",
      [
        "storage",
        "01126f38",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdfad8",
      "READ",
      [
        "storage",
        "01126f40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf978.md#insn-00bdf9d8) · [`00bdfa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf978.md#insn-00bdfa18) · [`00bdfa34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf978.md#insn-00bdfa34)
- 新版 [`00bdfa74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfa14.md#insn-00bdfa74) · [`00bdfab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfa14.md#insn-00bdfab4)

~~~diff
- 00bdf9d8 ["INT_ADD", "register:40f0:8", ["const:bdf9d8:8", "const:4:8"]]
- 00bdf9d8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdfa74 ["INT_ADD", "register:40f0:8", ["const:bdfa74:8", "const:4:8"]]
+ 00bdfa74 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdf9d8 bytes 1aed0194
+ 00bdfa74 bytes 27ed0194
- 00bdfa18 ["INT_ADD", "register:40f0:8", ["const:bdfa18:8", "const:4:8"]]
- 00bdfa18 ["CALL", null, ["callee:00589734:8"]]
+ 00bdfab4 ["INT_ADD", "register:40f0:8", ["const:bdfab4:8", "const:4:8"]]
+ 00bdfab4 ["CALL", null, ["callee:00589734:8"]]
- 00bdfa18 bytes 37a7e697
+ 00bdfab4 bytes 20a7e697
- 00bdfa34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdfa34 ["INT_ADD", "register:40f0:8", ["const:bdfa34:8", "const:4:8"]]
- 00bdfa34 ["CALLIND", null, ["register:0:8"]]
- 00bdfa34 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0853697accafd364dbed3cefb98ef7e1"></a>

### [`00bdfda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfda0.md) → [`00bdfe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfe3c.md) _ZN8firebase4auth4User18LinkWithCredentialERKNS0_10CredentialE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bcfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md) [`00bd48c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd48c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 3.70% / 新版 4.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdfdb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdfdb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdfdc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfdb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdfdc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bdfea8",
      "READ",
      [
        "storage",
        "01126d60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdfe50",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bdfe64",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bdfea8",
      "READ",
      [
        "storage",
        "01126e60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfdb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfda0.md#insn-00bdfdb4) · [`00bdfdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfda0.md#insn-00bdfdc8) · [`00bdfe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfda0.md#insn-00bdfe1c)
- 新版 [`00bdfeb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfe3c.md#insn-00bdfeb8)

~~~diff
- 00bdfdb4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bdfdb4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bdfdb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00bdfdb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdfdb4 bytes fd7b07a9
- 00bdfdc8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00bdfdc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bdfdc8 bytes e91700f9
- 00bdfe1c ["INT_ADD", "register:40f0:8", ["const:bdfe1c:8", "const:4:8"]]
- 00bdfe1c ["CALL", null, ["callee:00497874:8"]]
+ 00bdfeb8 ["INT_ADD", "register:40f0:8", ["const:bdfeb8:8", "const:4:8"]]
+ 00bdfeb8 ["CALL", null, ["callee:00497874:8"]]
- 00bdfe1c bytes 86dee297
+ 00bdfeb8 bytes 6fdee297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca68a6926a0554a1dc25e8fcd57b317f"></a>

### [`00bdff78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdff78.md) → [`00be0014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0014.md) _ZNK8firebase4auth4User16LinkWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be0050",
      "incomplete_value": false,
      "site": "00be0054",
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
      "definition_site": "00bdffb4",
      "incomplete_value": false,
      "site": "00bdffb8",
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
      "00be0024",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bdffb0"
      ]
    ],
    [
      "unmatched:00bdffb4",
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
      "00be0024",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00be004c"
      ]
    ],
    [
      "00be0050",
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

- 旧版 [`00bdffb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdff78.md#insn-00bdffb8) · [`00bdff9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdff78.md#insn-00bdff9c) · [`00bdffa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdff78.md#insn-00bdffa0)
- 新版 [`00be0054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0014.md#insn-00be0054)

~~~diff
- 00bdffb8 ["INT_ADD", "register:40f0:8", ["const:bdffb8:8", "const:4:8"]]
- 00bdffb8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00be0054 ["INT_ADD", "register:40f0:8", ["const:be0054:8", "const:4:8"]]
+ 00be0054 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdffb8 bytes 12ec0194
+ 00be0054 bytes 1fec0194
- 00bdff9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:18:8"]]
- 00bdff9c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdff9c bytes 020d40f9
- 00bdffa0 ["COPY", "register:4040:8", ["register:4098:8"]]
- 00bdffa0 bytes e80313aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff71f7905d93af65398419fb34b6cf7e"></a>

### [`00bdfffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfffc.md) → [`00be0098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0098.md) _ZN8firebase4auth4User6UnlinkEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bcfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcfde0.md) [`00bd48c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd48c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.27% / 新版 87.27%

CFGの説明率　旧版 19.05% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0000"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0000"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0004"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0000",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00be0004",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00be0008",
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
      "00be009c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00be00a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00be00a4",
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

- 旧版 [`00be0000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfffc.md#insn-00be0000) · [`00be0004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfffc.md#insn-00be0004) · [`00be0008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfffc.md#insn-00be0008)

~~~diff
- 00be0000 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00be0000 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00be0000 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00be0000 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be0000 bytes fa6703a9
- 00be0004 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00be0004 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00be0004 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00be0004 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be0004 bytes f85f04a9
- 00be0008 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00be0008 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00be0008 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00be0008 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be0008 bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2af18da97d5da16e7a514584a169633"></a>

### [`00be0204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0204.md) → [`00be02a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be02a0.md) _ZN8firebase4auth4User27UpdatePhoneNumberCredentialERKNS0_19PhoneAuthCredentialE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd010c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd010c.md) [`00bd4c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4c3c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bd01a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd01a8.md) [`00bd4cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4cd8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.42% / 新版 76.42%

CFGの説明率　旧版 3.57% / 新版 3.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0208"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0208"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be020c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0208",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00be020c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00be0210",
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
      "00be02a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00be02a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00be02ac",
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

- 旧版 [`00be0208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0204.md#insn-00be0208) · [`00be020c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0204.md#insn-00be020c) · [`00be0210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0204.md#insn-00be0210)

~~~diff
- 00be0208 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00be0208 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00be0208 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00be0208 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be0208 bytes fa6704a9
- 00be020c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00be020c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00be020c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00be020c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be020c bytes f85f05a9
- 00be0210 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00be0210 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00be0210 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00be0210 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be0210 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d5133ef948e1eb8f6f24fee7defad6f"></a>

### [`00be0450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0450.md) → [`00be04ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be04ec.md) _ZN8firebase4auth4User6ReloadEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bd055c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd055c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 13.33% / 新版 13.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0458"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0454",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00be0458",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00be045c",
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
      "00be04f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00be04f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00be04f8",
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

- 旧版 [`00be0454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0450.md#insn-00be0454) · [`00be0458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0450.md#insn-00be0458) · [`00be045c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0450.md#insn-00be045c)

~~~diff
- 00be0454 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00be0454 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00be0454 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00be0454 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be0454 bytes fa6704a9
- 00be0458 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00be0458 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00be0458 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00be0458 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be0458 bytes f85f05a9
- 00be045c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00be045c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00be045c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00be045c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be045c bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

