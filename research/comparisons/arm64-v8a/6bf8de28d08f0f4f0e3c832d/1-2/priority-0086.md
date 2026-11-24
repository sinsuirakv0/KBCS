# v16.0.1 → v16.0.2 · 最優先の変更候補 (86)

[一覧の目次](README.md)

<a id="compare-71cb31546883e41255cea6f96a37fe5b"></a>

### [`00be0640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0640.md) → [`00be06dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be06dc.md) _ZN8firebase4auth4User14ReauthenticateERKNS0_10CredentialE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bd055c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd055c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 53.33% / 新版 52.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0668"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00be0704"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0670"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0668",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00be0670",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00be07d8"
      ]
    ],
    [
      "unmatched:00be0678",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00be07d8"
      ]
    ]
  ],
  "added": [
    [
      "00be0704",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00be070c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00be07d8"
      ]
    ],
    [
      "00be0714",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00be07d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0640.md#insn-00be0668) · [`00be0670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0640.md#insn-00be0670) · [`00be0678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0640.md#insn-00be0678)

~~~diff
- 00be0668 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00be0668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00be0668 bytes e91f00f9
- 00be0670 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00be0670 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00be0670 bytes 690600b4
- 00be0678 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00be0678 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00be0678 bytes 280600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d75c329e9c8c037980e09c2198b2c9d"></a>

### [`00be0a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0a10.md) → [`00be0aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0aac.md) _ZNK8firebase4auth4User26ReauthenticateWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be0ae8",
      "incomplete_value": false,
      "site": "00be0aec",
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
      "definition_site": "00be0a4c",
      "incomplete_value": false,
      "site": "00be0a50",
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
      "00be0ae8",
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
      "00be0ae8",
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

- 旧版 [`00be0a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0a10.md#insn-00be0a50) · [`00be0a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0a10.md#insn-00be0a4c) · [`00be0a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0a10.md#insn-00be0a5c)
- 新版 [`00be0aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0aac.md#insn-00be0aec) · [`00be0ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0aac.md#insn-00be0ae8) · [`00be0af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0aac.md#insn-00be0af8)

~~~diff
- 00be0a50 ["INT_ADD", "register:40f0:8", ["const:be0a50:8", "const:4:8"]]
- 00be0a50 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00be0aec ["INT_ADD", "register:40f0:8", ["const:be0aec:8", "const:4:8"]]
+ 00be0aec ["CALL", null, ["callee:00c5b0d0:8"]]
- 00be0a50 bytes 6ce90194
+ 00be0aec bytes 79e90194
- 00be0a4c ["COPY", "tmp:0:8", ["const:bc2:8"]]
- 00be0a4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00be0a4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00be0a4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00be0ae8 ["COPY", "tmp:0:8", ["const:c02:8"]]
+ 00be0ae8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00be0ae8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00be0ae8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00be0a4c bytes 00082f91
+ 00be0ae8 bytes 00083091
- 00be0a5c ["INT_ADD", "register:40f0:8", ["const:be0a5c:8", "const:4:8"]]
- 00be0a5c ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be0af8 ["INT_ADD", "register:40f0:8", ["const:be0af8:8", "const:4:8"]]
+ 00be0af8 ["CALL", null, ["callee:00c5ad40:8"]]
- 00be0a5c bytes 85e80194
+ 00be0af8 bytes 92e80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4936a944d19cb1dd9ca21bc60a5ecb3e"></a>

### [`00be10a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be10a4.md) → [`00be1140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1140.md) _ZNK8firebase4auth4User8metadataEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`0058f5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f5dc.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

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
      "definition_site": "00be1174",
      "incomplete_value": true,
      "site": "00be1180",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be10d8",
      "incomplete_value": true,
      "site": "00be10e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
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
      "definition_site": "00be119c",
      "incomplete_value": true,
      "site": "00be11a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be1100",
      "incomplete_value": true,
      "site": "00be110c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00be1174",
      "READ",
      [
        "storage",
        "01126da0",
        null,
        "undefined8"
      ]
    ],
    [
      "00be119c",
      "READ",
      [
        "storage",
        "01126e10",
        null,
        "undefined8"
      ]
    ],
    [
      "00be11ac",
      "READ",
      [
        "storage",
        "01126e18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00be1174",
      "READ",
      [
        "storage",
        "01126ea0",
        null,
        "undefined8"
      ]
    ],
    [
      "00be119c",
      "READ",
      [
        "storage",
        "01126f10",
        null,
        "undefined8"
      ]
    ],
    [
      "00be11ac",
      "READ",
      [
        "storage",
        "01126f18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be10e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be10a4.md#insn-00be10e4) · [`00be110c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be10a4.md#insn-00be110c) · [`00be10cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be10a4.md#insn-00be10cc)
- 新版 [`00be1180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1140.md#insn-00be1180) · [`00be11a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1140.md#insn-00be11a8) · [`00be1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1140.md#insn-00be1168)

~~~diff
- 00be10e4 ["INT_ADD", "register:40f0:8", ["const:be10e4:8", "const:4:8"]]
- 00be10e4 ["CALL", null, ["callee:00497874:8"]]
+ 00be1180 ["INT_ADD", "register:40f0:8", ["const:be1180:8", "const:4:8"]]
+ 00be1180 ["CALL", null, ["callee:00497874:8"]]
- 00be10e4 bytes d4d9e297
+ 00be1180 bytes bdd9e297
- 00be110c ["INT_ADD", "register:40f0:8", ["const:be110c:8", "const:4:8"]]
- 00be110c ["CALL", null, ["callee:0058f5dc:8"]]
+ 00be11a8 ["INT_ADD", "register:40f0:8", ["const:be11a8:8", "const:4:8"]]
+ 00be11a8 ["CALL", null, ["callee:0058f5dc:8"]]
- 00be110c bytes 24b9e697
+ 00be11a8 bytes 0db9e697
- 00be10cc ["INT_ADD", "register:40f0:8", ["const:be10cc:8", "const:4:8"]]
- 00be10cc ["CALL", null, ["callee:00c5b150:8"]]
+ 00be1168 ["INT_ADD", "register:40f0:8", ["const:be1168:8", "const:4:8"]]
+ 00be1168 ["CALL", null, ["callee:00c5b150:8"]]
- 00be10cc bytes ede70194
+ 00be1168 bytes fae70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09ec0a526dc3b58283969be52af10648"></a>

### [`00be1230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1230.md) → [`00be12cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be12cc.md) _ZN8firebase4auth22AndroidWrappedUserInfoD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5db80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5dc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00be12e8",
      "incomplete_value": true,
      "site": "00be12ec",
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
      "definition_site": "00be124c",
      "incomplete_value": true,
      "site": "00be1250",
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
      "00be12e0",
      "READ",
      [
        "storage",
        "00c9ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00be12ec",
      "DATA",
      [
        "storage",
        "00c92910",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00be12e0",
      "READ",
      [
        "storage",
        "00c9bb30",
        null,
        "pointer"
      ]
    ],
    [
      "00be12ec",
      "DATA",
      [
        "storage",
        "00c929e0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be1244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1230.md#insn-00be1244) · [`00be1258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1230.md#insn-00be1258) · [`00be1268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1230.md#insn-00be1268)
- 新版 [`00be12e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be12cc.md#insn-00be12e0) · [`00be12f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be12cc.md#insn-00be12f4) · [`00be1304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be12cc.md#insn-00be1304)

~~~diff
- 00be1244 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a60:8"]]
- 00be1244 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00be12e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b30:8"]]
+ 00be12e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00be1244 bytes 293145f9
+ 00be12e0 bytes 299945f9
- 00be1258 ["INT_ADD", "register:40f0:8", ["const:be1258:8", "const:4:8"]]
- 00be1258 ["CALL", null, ["callee:00c5b150:8"]]
+ 00be12f4 ["INT_ADD", "register:40f0:8", ["const:be12f4:8", "const:4:8"]]
+ 00be12f4 ["CALL", null, ["callee:00c5b150:8"]]
- 00be1258 bytes 8ae70194
+ 00be12f4 bytes 97e70194
- 00be1268 ["COPY", "register:0:8", ["register:4040:8"]]
- 00be1268 ["INT_ADD", "register:40f0:8", ["const:be1268:8", "const:4:8"]]
- 00be1268 ["CALLIND", null, ["register:0:8"]]
+ 00be1304 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00be1304 ["INT_ADD", "register:40f0:8", ["const:be1304:8", "const:4:8"]]
+ 00be1304 ["CALLIND", null, ["register:0:8"]]
- 00be1268 bytes 00013fd6
+ 00be1304 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dce5c56f818621cfe162f3d98845b89"></a>

### [`00be12ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be12ac.md) → [`00be1348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1348.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allo

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5de90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de90.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5df60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df60.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

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
      "definition_site": "00be13ac",
      "incomplete_value": false,
      "site": "00be13b0",
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
      "definition_site": "00be1310",
      "incomplete_value": false,
      "site": "00be1314",
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
      "00be13ac",
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
      "00be13ac",
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

- 旧版 [`00be1314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be12ac.md#insn-00be1314) · [`00be12d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be12ac.md#insn-00be12d8) · [`00be12e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be12ac.md#insn-00be12e4)
- 新版 [`00be13b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1348.md#insn-00be13b0) · [`00be1374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1348.md#insn-00be1374) · [`00be1380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1348.md#insn-00be1380)

~~~diff
- 00be1314 ["INT_ADD", "register:40f0:8", ["const:be1314:8", "const:4:8"]]
- 00be1314 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00be13b0 ["INT_ADD", "register:40f0:8", ["const:be13b0:8", "const:4:8"]]
+ 00be13b0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00be1314 bytes 3be70194
+ 00be13b0 bytes 48e70194
- 00be12d8 ["INT_ADD", "register:40f0:8", ["const:be12d8:8", "const:4:8"]]
- 00be12d8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1374 ["INT_ADD", "register:40f0:8", ["const:be1374:8", "const:4:8"]]
+ 00be1374 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be12d8 bytes cae50194
+ 00be1374 bytes d7e50194
- 00be12e4 ["INT_ADD", "register:40f0:8", ["const:be12e4:8", "const:4:8"]]
- 00be12e4 ["CALL", null, ["callee:00c5af50:8"]]
+ 00be1380 ["INT_ADD", "register:40f0:8", ["const:be1380:8", "const:4:8"]]
+ 00be1380 ["CALL", null, ["callee:00c5af50:8"]]
- 00be12e4 bytes e7e60194
+ 00be1380 bytes f4e60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8d56f95bc0df5e5f644b8db24bec0c0"></a>

### [`00be1488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1488.md) → [`00be1524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1524.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS_4auth14Fut

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5de80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de80.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5df50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df50.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be1590",
      "incomplete_value": false,
      "site": "00be1594",
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
      "definition_site": "00be14f4",
      "incomplete_value": false,
      "site": "00be14f8",
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
      "00be1590",
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
      "00be1590",
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

- 旧版 [`00be14f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1488.md#insn-00be14f8) · [`00be14bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1488.md#insn-00be14bc) · [`00be14c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1488.md#insn-00be14c8)
- 新版 [`00be1594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1524.md#insn-00be1594) · [`00be1558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1524.md#insn-00be1558) · [`00be1564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1524.md#insn-00be1564)

~~~diff
- 00be14f8 ["INT_ADD", "register:40f0:8", ["const:be14f8:8", "const:4:8"]]
- 00be14f8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00be1594 ["INT_ADD", "register:40f0:8", ["const:be1594:8", "const:4:8"]]
+ 00be1594 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00be14f8 bytes c2e60194
+ 00be1594 bytes cfe60194
- 00be14bc ["INT_ADD", "register:40f0:8", ["const:be14bc:8", "const:4:8"]]
- 00be14bc ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1558 ["INT_ADD", "register:40f0:8", ["const:be1558:8", "const:4:8"]]
+ 00be1558 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be14bc bytes 51e50194
+ 00be1558 bytes 5ee50194
- 00be14c8 ["INT_ADD", "register:40f0:8", ["const:be14c8:8", "const:4:8"]]
- 00be14c8 ["CALL", null, ["callee:00c5af50:8"]]
+ 00be1564 ["INT_ADD", "register:40f0:8", ["const:be1564:8", "const:4:8"]]
+ 00be1564 ["CALL", null, ["callee:00c5af50:8"]]
- 00be14c8 bytes 6ee60194
+ 00be1564 bytes 7be60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daf2f7b520217cc1a4106bd49edf6a7f"></a>

### [`00be2124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2124.md) → [`00be21c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be21c0.md) _ZN8firebase4auth17UserInfoInterfaceD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5db70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db70.md) [`00c5db80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db80.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00c5dc40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc40.md) [`00c5dc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc50.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00be21dc",
      "incomplete_value": true,
      "site": "00be21e0",
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
      "definition_site": "00be2140",
      "incomplete_value": true,
      "site": "00be2144",
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
      "00be21d4",
      "READ",
      [
        "storage",
        "00c9b9c8",
        null,
        "pointer"
      ]
    ],
    [
      "00be21e0",
      "DATA",
      [
        "storage",
        "00c92978",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00be21d4",
      "READ",
      [
        "storage",
        "00c9ba98",
        null,
        "pointer"
      ]
    ],
    [
      "00be21e0",
      "DATA",
      [
        "storage",
        "00c92a48",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be2138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2124.md#insn-00be2138) · [`00be2184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2124.md#insn-00be2184) · [`00be2194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2124.md#insn-00be2194)
- 新版 [`00be21d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be21c0.md#insn-00be21d4) · [`00be2220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be21c0.md#insn-00be2220) · [`00be2230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be21c0.md#insn-00be2230)

~~~diff
- 00be2138 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9c8:8"]]
- 00be2138 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00be21d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a98:8"]]
+ 00be21d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00be2138 bytes 29e544f9
+ 00be21d4 bytes 294d45f9
- 00be2184 ["INT_ADD", "register:40f0:8", ["const:be2184:8", "const:4:8"]]
- 00be2184 ["CALL", null, ["callee:00c57f80:8"]]
+ 00be2220 ["INT_ADD", "register:40f0:8", ["const:be2220:8", "const:4:8"]]
+ 00be2220 ["CALL", null, ["callee:00c57f80:8"]]
- 00be2184 bytes 4bd70194
+ 00be2220 bytes 58d70194
- 00be2194 ["INT_ADD", "register:40f0:8", ["const:be2194:8", "const:4:8"]]
- 00be2194 ["CALL", null, ["callee:00c57f80:8"]]
+ 00be2230 ["INT_ADD", "register:40f0:8", ["const:be2230:8", "const:4:8"]]
+ 00be2230 ["CALL", null, ["callee:00c57f80:8"]]
- 00be2194 bytes 47d70194
+ 00be2230 bytes 54d70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbd6314470cfb6e1a8d13edd2fc0a947"></a>

### [`00be30b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be30b4.md) → [`00be3150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md) FUN_00be3150

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be3098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3098.md) [`00be30b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be30b4.md) · 呼出先 4件 [`00be30b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be30b4.md) [`00be9dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9dc8.md) [`00bea088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea088.md) [`00bea1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea1b0.md)
- 新版 呼出元 2件 [`00be3134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3134.md) [`00be3150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md) · 呼出先 4件 [`00be3150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md) [`00be9e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9e64.md) [`00bea124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea124.md) [`00bea24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea24c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.56% / 新版 99.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be34dc",
      "value": [
        "leaf",
        "ram:be9e64:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be3440",
      "value": [
        "leaf",
        "ram:be9dc8:8"
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
      "site": "00be34f0",
      "value": [
        "leaf",
        "ram:be9e64:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be3454",
      "value": [
        "leaf",
        "ram:be9dc8:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be34dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be9dc8"
      ]
    ],
    [
      "00be34f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be9dc8"
      ]
    ]
  ],
  "added": [
    [
      "00be34dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be9e64"
      ]
    ],
    [
      "00be34f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be9e64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be3440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be30b4.md#insn-00be3440) · [`00be3454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be30b4.md#insn-00be3454) · [`00be3470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be30b4.md#insn-00be3470)
- 新版 [`00be34dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md#insn-00be34dc) · [`00be34f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md#insn-00be34f0) · [`00be350c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md#insn-00be350c)

~~~diff
- 00be3440 ["INT_ADD", "register:40f0:8", ["const:be3440:8", "const:4:8"]]
- 00be3440 ["CALL", null, ["ram:be9dc8:8"]]
+ 00be34dc ["INT_ADD", "register:40f0:8", ["const:be34dc:8", "const:4:8"]]
+ 00be34dc ["CALL", null, ["ram:be9e64:8"]]
- 00be3440 bytes 621a0094
+ 00be34dc bytes 621a0094
- 00be3454 ["INT_ADD", "register:40f0:8", ["const:be3454:8", "const:4:8"]]
- 00be3454 ["CALL", null, ["ram:be9dc8:8"]]
+ 00be34f0 ["INT_ADD", "register:40f0:8", ["const:be34f0:8", "const:4:8"]]
+ 00be34f0 ["CALL", null, ["ram:be9e64:8"]]
- 00be3454 bytes 5d1a0094
+ 00be34f0 bytes 5d1a0094
- 00be3470 ["INT_ADD", "register:40f0:8", ["const:be3470:8", "const:4:8"]]
- 00be3470 ["CALL", null, ["local:b0:8"]]
+ 00be350c ["INT_ADD", "register:40f0:8", ["const:be350c:8", "const:4:8"]]
+ 00be350c ["CALL", null, ["local:b0:8"]]
- 00be3470 bytes 11ffff97
+ 00be350c bytes 11ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efee92a234adb62194f83ea3a129c290"></a>

### [`00be3f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f20.md) → [`00be3fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md) FUN_00be3fbc

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be3f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f00.md) [`00be3f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f20.md) · 呼出先 4件 [`00be3f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f20.md) [`00beab80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00beab80.md) [`00beae40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00beae40.md) [`00beaf68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00beaf68.md)
- 新版 呼出元 2件 [`00be3f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3f9c.md) [`00be3fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md) · 呼出先 4件 [`00be3fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md) [`00beac1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00beac1c.md) [`00beaedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00beaedc.md) [`00beb004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb004.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.56% / 新版 99.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be434c",
      "value": [
        "leaf",
        "ram:beac1c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be42b0",
      "value": [
        "leaf",
        "ram:beab80:8"
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
      "site": "00be4360",
      "value": [
        "leaf",
        "ram:beac1c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be42c4",
      "value": [
        "leaf",
        "ram:beab80:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be434c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beab80"
      ]
    ],
    [
      "00be4360",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beab80"
      ]
    ]
  ],
  "added": [
    [
      "00be434c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beac1c"
      ]
    ],
    [
      "00be4360",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beac1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be42b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f20.md#insn-00be42b0) · [`00be42c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f20.md#insn-00be42c4) · [`00be42e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f20.md#insn-00be42e0)
- 新版 [`00be434c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md#insn-00be434c) · [`00be4360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md#insn-00be4360) · [`00be437c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md#insn-00be437c)

~~~diff
- 00be42b0 ["INT_ADD", "register:40f0:8", ["const:be42b0:8", "const:4:8"]]
- 00be42b0 ["CALL", null, ["ram:beab80:8"]]
+ 00be434c ["INT_ADD", "register:40f0:8", ["const:be434c:8", "const:4:8"]]
+ 00be434c ["CALL", null, ["ram:beac1c:8"]]
- 00be42b0 bytes 341a0094
+ 00be434c bytes 341a0094
- 00be42c4 ["INT_ADD", "register:40f0:8", ["const:be42c4:8", "const:4:8"]]
- 00be42c4 ["CALL", null, ["ram:beab80:8"]]
+ 00be4360 ["INT_ADD", "register:40f0:8", ["const:be4360:8", "const:4:8"]]
+ 00be4360 ["CALL", null, ["ram:beac1c:8"]]
- 00be42c4 bytes 2f1a0094
+ 00be4360 bytes 2f1a0094
- 00be42e0 ["INT_ADD", "register:40f0:8", ["const:be42e0:8", "const:4:8"]]
- 00be42e0 ["CALL", null, ["local:b0:8"]]
+ 00be437c ["INT_ADD", "register:40f0:8", ["const:be437c:8", "const:4:8"]]
+ 00be437c ["CALL", null, ["local:b0:8"]]
- 00be42e0 bytes 10ffff97
+ 00be437c bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4678f55a7ccb1d875f2a4d3cd603b8af"></a>

### [`00be465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be465c.md) → [`00be46f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md) FUN_00be46f8

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be463c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be463c.md) [`00be465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be465c.md) · 呼出先 4件 [`00be465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be465c.md) [`00beb264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb264.md) [`00beb524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb524.md) [`00beb64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb64c.md)
- 新版 呼出元 2件 [`00be46d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46d8.md) [`00be46f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md) · 呼出先 4件 [`00be46f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md) [`00beb300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb300.md) [`00beb5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb5c0.md) [`00beb6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb6e8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.56% / 新版 99.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be4a88",
      "value": [
        "leaf",
        "ram:beb300:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be49ec",
      "value": [
        "leaf",
        "ram:beb264:8"
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
      "site": "00be4a9c",
      "value": [
        "leaf",
        "ram:beb300:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be4a00",
      "value": [
        "leaf",
        "ram:beb264:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be4a88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb264"
      ]
    ],
    [
      "00be4a9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb264"
      ]
    ]
  ],
  "added": [
    [
      "00be4a88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb300"
      ]
    ],
    [
      "00be4a9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb300"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be49ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be465c.md#insn-00be49ec) · [`00be4a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be465c.md#insn-00be4a00) · [`00be4a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be465c.md#insn-00be4a1c)
- 新版 [`00be4a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md#insn-00be4a88) · [`00be4a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md#insn-00be4a9c) · [`00be4ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md#insn-00be4ab8)

~~~diff
- 00be49ec ["INT_ADD", "register:40f0:8", ["const:be49ec:8", "const:4:8"]]
- 00be49ec ["CALL", null, ["ram:beb264:8"]]
+ 00be4a88 ["INT_ADD", "register:40f0:8", ["const:be4a88:8", "const:4:8"]]
+ 00be4a88 ["CALL", null, ["ram:beb300:8"]]
- 00be49ec bytes 1e1a0094
+ 00be4a88 bytes 1e1a0094
- 00be4a00 ["INT_ADD", "register:40f0:8", ["const:be4a00:8", "const:4:8"]]
- 00be4a00 ["CALL", null, ["ram:beb264:8"]]
+ 00be4a9c ["INT_ADD", "register:40f0:8", ["const:be4a9c:8", "const:4:8"]]
+ 00be4a9c ["CALL", null, ["ram:beb300:8"]]
- 00be4a00 bytes 191a0094
+ 00be4a9c bytes 191a0094
- 00be4a1c ["INT_ADD", "register:40f0:8", ["const:be4a1c:8", "const:4:8"]]
- 00be4a1c ["CALL", null, ["local:b0:8"]]
+ 00be4ab8 ["INT_ADD", "register:40f0:8", ["const:be4ab8:8", "const:4:8"]]
+ 00be4ab8 ["CALL", null, ["local:b0:8"]]
- 00be4a1c bytes 10ffff97
+ 00be4ab8 bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-229a5dcc7ee58e26400a973d95a51fb5"></a>

### [`00be4d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d98.md) → [`00be4e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md) FUN_00be4e34

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be4d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d78.md) [`00be4d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d98.md) · 呼出先 4件 [`00be4d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d98.md) [`00beb948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb948.md) [`00bebbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00bebbe8.md) [`00bebd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00bebd10.md)
- 新版 呼出元 2件 [`00be4e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e14.md) [`00be4e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md) · 呼出先 4件 [`00be4e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md) [`00beb9e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb9e4.md) [`00bebc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00bebc84.md) [`00bebdac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00bebdac.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.55% / 新版 99.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be51c4",
      "value": [
        "leaf",
        "ram:beb9e4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be5128",
      "value": [
        "leaf",
        "ram:beb948:8"
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
      "site": "00be51d8",
      "value": [
        "leaf",
        "ram:beb9e4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be513c",
      "value": [
        "leaf",
        "ram:beb948:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be51c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb948"
      ]
    ],
    [
      "00be51d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb948"
      ]
    ]
  ],
  "added": [
    [
      "00be51c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb9e4"
      ]
    ],
    [
      "00be51d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb9e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be5128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d98.md#insn-00be5128) · [`00be513c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d98.md#insn-00be513c) · [`00be5158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d98.md#insn-00be5158)
- 新版 [`00be51c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md#insn-00be51c4) · [`00be51d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md#insn-00be51d8) · [`00be51f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md#insn-00be51f4)

~~~diff
- 00be5128 ["INT_ADD", "register:40f0:8", ["const:be5128:8", "const:4:8"]]
- 00be5128 ["CALL", null, ["ram:beb948:8"]]
+ 00be51c4 ["INT_ADD", "register:40f0:8", ["const:be51c4:8", "const:4:8"]]
+ 00be51c4 ["CALL", null, ["ram:beb9e4:8"]]
- 00be5128 bytes 081a0094
+ 00be51c4 bytes 081a0094
- 00be513c ["INT_ADD", "register:40f0:8", ["const:be513c:8", "const:4:8"]]
- 00be513c ["CALL", null, ["ram:beb948:8"]]
+ 00be51d8 ["INT_ADD", "register:40f0:8", ["const:be51d8:8", "const:4:8"]]
+ 00be51d8 ["CALL", null, ["ram:beb9e4:8"]]
- 00be513c bytes 031a0094
+ 00be51d8 bytes 031a0094
- 00be5158 ["INT_ADD", "register:40f0:8", ["const:be5158:8", "const:4:8"]]
- 00be5158 ["CALL", null, ["local:b0:8"]]
+ 00be51f4 ["INT_ADD", "register:40f0:8", ["const:be51f4:8", "const:4:8"]]
+ 00be51f4 ["CALL", null, ["local:b0:8"]]
- 00be5158 bytes 10ffff97
+ 00be51f4 bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0087a866dfa2e681ed56e4bde0acc053"></a>

### [`00be7828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7828.md) → [`00be78c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md) FUN_00be78c4

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be7808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7808.md) [`00be7828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7828.md) · 呼出先 4件 [`00be7828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7828.md) [`00bee1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00bee1e0.md) [`00bee480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00bee480.md) [`00bee5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00bee5a8.md)
- 新版 呼出元 2件 [`00be78a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78a4.md) [`00be78c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md) · 呼出先 4件 [`00be78c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md) [`00bee27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee27c.md) [`00bee51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee51c.md) [`00bee644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee644.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.55% / 新版 99.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be7c54",
      "value": [
        "leaf",
        "ram:bee27c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be7bb8",
      "value": [
        "leaf",
        "ram:bee1e0:8"
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
      "site": "00be7c68",
      "value": [
        "leaf",
        "ram:bee27c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be7bcc",
      "value": [
        "leaf",
        "ram:bee1e0:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be7c54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee1e0"
      ]
    ],
    [
      "00be7c68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee1e0"
      ]
    ]
  ],
  "added": [
    [
      "00be7c54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee27c"
      ]
    ],
    [
      "00be7c68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee27c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be7bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7828.md#insn-00be7bb8) · [`00be7bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7828.md#insn-00be7bcc) · [`00be7be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7828.md#insn-00be7be8)
- 新版 [`00be7c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md#insn-00be7c54) · [`00be7c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md#insn-00be7c68) · [`00be7c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md#insn-00be7c84)

~~~diff
- 00be7bb8 ["INT_ADD", "register:40f0:8", ["const:be7bb8:8", "const:4:8"]]
- 00be7bb8 ["CALL", null, ["ram:bee1e0:8"]]
+ 00be7c54 ["INT_ADD", "register:40f0:8", ["const:be7c54:8", "const:4:8"]]
+ 00be7c54 ["CALL", null, ["ram:bee27c:8"]]
- 00be7bb8 bytes 8a190094
+ 00be7c54 bytes 8a190094
- 00be7bcc ["INT_ADD", "register:40f0:8", ["const:be7bcc:8", "const:4:8"]]
- 00be7bcc ["CALL", null, ["ram:bee1e0:8"]]
+ 00be7c68 ["INT_ADD", "register:40f0:8", ["const:be7c68:8", "const:4:8"]]
+ 00be7c68 ["CALL", null, ["ram:bee27c:8"]]
- 00be7bcc bytes 85190094
+ 00be7c68 bytes 85190094
- 00be7be8 ["INT_ADD", "register:40f0:8", ["const:be7be8:8", "const:4:8"]]
- 00be7be8 ["CALL", null, ["local:b0:8"]]
+ 00be7c84 ["INT_ADD", "register:40f0:8", ["const:be7c84:8", "const:4:8"]]
+ 00be7c84 ["CALL", null, ["local:b0:8"]]
- 00be7be8 bytes 10ffff97
+ 00be7c84 bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe844ac5df1c0116afd21e34a7726db9"></a>

### [`00be7f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f40.md) → [`00be7fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md) FUN_00be7fdc

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be7f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f20.md) [`00be7f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f40.md) · 呼出先 4件 [`00be7f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f40.md) [`00bee880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00bee880.md) [`00beeb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beeb20.md) [`00beec48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beec48.md)
- 新版 呼出元 2件 [`00be7fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fbc.md) [`00be7fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md) · 呼出先 4件 [`00be7fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md) [`00bee91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee91c.md) [`00beebbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beebbc.md) [`00beece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beece4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.55% / 新版 99.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be836c",
      "value": [
        "leaf",
        "ram:bee91c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be82d0",
      "value": [
        "leaf",
        "ram:bee880:8"
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
      "site": "00be8380",
      "value": [
        "leaf",
        "ram:bee91c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be82e4",
      "value": [
        "leaf",
        "ram:bee880:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be836c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee880"
      ]
    ],
    [
      "00be8380",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee880"
      ]
    ]
  ],
  "added": [
    [
      "00be836c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee91c"
      ]
    ],
    [
      "00be8380",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee91c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be82d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f40.md#insn-00be82d0) · [`00be82e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f40.md#insn-00be82e4) · [`00be8300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f40.md#insn-00be8300)
- 新版 [`00be836c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md#insn-00be836c) · [`00be8380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md#insn-00be8380) · [`00be839c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be7fdc.md#insn-00be839c)

~~~diff
- 00be82d0 ["INT_ADD", "register:40f0:8", ["const:be82d0:8", "const:4:8"]]
- 00be82d0 ["CALL", null, ["ram:bee880:8"]]
+ 00be836c ["INT_ADD", "register:40f0:8", ["const:be836c:8", "const:4:8"]]
+ 00be836c ["CALL", null, ["ram:bee91c:8"]]
- 00be82d0 bytes 6c190094
+ 00be836c bytes 6c190094
- 00be82e4 ["INT_ADD", "register:40f0:8", ["const:be82e4:8", "const:4:8"]]
- 00be82e4 ["CALL", null, ["ram:bee880:8"]]
+ 00be8380 ["INT_ADD", "register:40f0:8", ["const:be8380:8", "const:4:8"]]
+ 00be8380 ["CALL", null, ["ram:bee91c:8"]]
- 00be82e4 bytes 67190094
+ 00be8380 bytes 67190094
- 00be8300 ["INT_ADD", "register:40f0:8", ["const:be8300:8", "const:4:8"]]
- 00be8300 ["CALL", null, ["local:b0:8"]]
+ 00be839c ["INT_ADD", "register:40f0:8", ["const:be839c:8", "const:4:8"]]
+ 00be839c ["CALL", null, ["local:b0:8"]]
- 00be8300 bytes 10ffff97
+ 00be839c bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a2d90868f0c498cc23aa0bd01205bbe"></a>

### [`00bef954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef954.md) → [`00bef9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef9f0.md) _ZNSt6__ndk16chrono12system_clock3nowEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) · 呼出先 3件 [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c59700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59700.md)
- 新版 呼出元 1件 [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md) · 呼出先 3件 [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c597d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00befa5c",
      "incomplete_value": false,
      "site": "00befa60",
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
            "const:a0e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bef9c0",
      "incomplete_value": false,
      "site": "00bef9c4",
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
            "const:9dd:8"
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
      "00befa5c",
      "PARAM",
      [
        "storage",
        "002b49dd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00befa5c",
      "PARAM",
      [
        "storage",
        "002b4a0e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bef9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef954.md#insn-00bef9c4) · [`00bef96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef954.md#insn-00bef96c) · [`00bef9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef954.md#insn-00bef9b4)
- 新版 [`00befa60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef9f0.md#insn-00befa60) · [`00befa08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef9f0.md#insn-00befa08) · [`00befa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef9f0.md#insn-00befa50)

~~~diff
- 00bef9c4 ["INT_ADD", "register:40f0:8", ["const:bef9c4:8", "const:4:8"]]
- 00bef9c4 ["CALL", null, ["callee:00c581f0:8"]]
+ 00befa60 ["INT_ADD", "register:40f0:8", ["const:befa60:8", "const:4:8"]]
+ 00befa60 ["CALL", null, ["callee:00c581f0:8"]]
- 00bef9c4 bytes d7a10194
+ 00befa60 bytes e4a10194
- 00bef96c ["INT_ADD", "register:40f0:8", ["const:bef96c:8", "const:4:8"]]
- 00bef96c ["CALL", null, ["callee:00c597d0:8"]]
+ 00befa08 ["INT_ADD", "register:40f0:8", ["const:befa08:8", "const:4:8"]]
+ 00befa08 ["CALL", null, ["callee:00c597d0:8"]]
- 00bef96c bytes 65a70194
+ 00befa08 bytes 72a70194
- 00bef9b4 ["INT_ADD", "register:40f0:8", ["const:bef9b4:8", "const:4:8"]]
- 00bef9b4 ["CALL", null, ["callee:00c58190:8"]]
+ 00befa50 ["INT_ADD", "register:40f0:8", ["const:befa50:8", "const:4:8"]]
+ 00befa50 ["CALL", null, ["callee:00c58190:8"]]
- 00bef9b4 bytes c3a10194
+ 00befa50 bytes d0a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-629e6170cc24c4cd8c8c04c3fbdbf6e2"></a>

### [`00befa08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa08.md) → [`00befaa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befaa4.md) _ZNSt6__ndk16chrono12steady_clock3nowEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ec0.md) · 呼出先 3件 [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c59700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59700.md)
- 新版 呼出元 1件 [`00c57f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f90.md) · 呼出先 3件 [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c597d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00befaf0",
      "incomplete_value": false,
      "site": "00befaf4",
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
            "const:143:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00befa54",
      "incomplete_value": false,
      "site": "00befa58",
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
            "const:19f:8"
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
      "00befaf0",
      "PARAM",
      [
        "storage",
        "002a519f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00befaf0",
      "PARAM",
      [
        "storage",
        "002a5143",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00befa58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa08.md#insn-00befa58) · [`00befa20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa08.md#insn-00befa20) · [`00befa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa08.md#insn-00befa48)
- 新版 [`00befaf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befaa4.md#insn-00befaf4) · [`00befabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befaa4.md#insn-00befabc) · [`00befae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befaa4.md#insn-00befae4)

~~~diff
- 00befa58 ["INT_ADD", "register:40f0:8", ["const:befa58:8", "const:4:8"]]
- 00befa58 ["CALL", null, ["callee:00c581f0:8"]]
+ 00befaf4 ["INT_ADD", "register:40f0:8", ["const:befaf4:8", "const:4:8"]]
+ 00befaf4 ["CALL", null, ["callee:00c581f0:8"]]
- 00befa58 bytes b2a10194
+ 00befaf4 bytes bfa10194
- 00befa20 ["INT_ADD", "register:40f0:8", ["const:befa20:8", "const:4:8"]]
- 00befa20 ["CALL", null, ["callee:00c597d0:8"]]
+ 00befabc ["INT_ADD", "register:40f0:8", ["const:befabc:8", "const:4:8"]]
+ 00befabc ["CALL", null, ["callee:00c597d0:8"]]
- 00befa20 bytes 38a70194
+ 00befabc bytes 45a70194
- 00befa48 ["INT_ADD", "register:40f0:8", ["const:befa48:8", "const:4:8"]]
- 00befa48 ["CALL", null, ["callee:00c58190:8"]]
+ 00befae4 ["INT_ADD", "register:40f0:8", ["const:befae4:8", "const:4:8"]]
+ 00befae4 ["CALL", null, ["callee:00c58190:8"]]
- 00befa48 bytes 9ea10194
+ 00befae4 bytes aba10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f9ab61d2706e7551f5fd7903552f69"></a>

### [`00befb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb0c.md) → [`00befba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befba8.md) _ZNSt16nested_exceptionC2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00befbc4",
      "incomplete_value": true,
      "site": "00befbc8",
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
      "definition_site": "00befb28",
      "incomplete_value": true,
      "site": "00befb2c",
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
      "00befbc0",
      "READ",
      [
        "storage",
        "00c9ba70",
        null,
        "pointer"
      ]
    ],
    [
      "00befbc8",
      "DATA",
      [
        "storage",
        "00c929d8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00befbc0",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00befbc8",
      "DATA",
      [
        "storage",
        "00c92aa8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00befb24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb0c.md#insn-00befb24) · [`00befb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb0c.md#insn-00befb30)
- 新版 [`00befbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befba8.md#insn-00befbc0) · [`00befbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befba8.md#insn-00befbcc)

~~~diff
- 00befb24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 00befb24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00befbc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b40:8"]]
+ 00befbc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00befb24 bytes 083945f9
+ 00befbc0 bytes 08a145f9
- 00befb30 ["INT_ADD", "register:40f0:8", ["const:befb30:8", "const:4:8"]]
- 00befb30 ["CALL", null, ["callee:00c5e010:8"]]
+ 00befbcc ["INT_ADD", "register:40f0:8", ["const:befbcc:8", "const:4:8"]]
+ 00befbcc ["CALL", null, ["callee:00c5e010:8"]]
- 00befb30 bytes 04b90194
+ 00befbcc bytes 11b90194
~~~


<a id="compare-1c0fe76272fdbc0365792cb3c068fc4a"></a>

### [`00befc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc28.md) → [`00befcc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcc4.md) _ZNSt6__ndk112__next_primeEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a820.md) · 呼出先 1件 [`00bf0348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0348.md)
- 新版 呼出元 1件 [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md) · 呼出先 1件 [`00bf03e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf03dc",
      "incomplete_value": false,
      "site": "00bf03e0",
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
            "const:23c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0340",
      "incomplete_value": false,
      "site": "00bf0344",
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
            "const:290:8"
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
      "00befcf4",
      "READ",
      [
        "storage",
        "00310328",
        null,
        "undefined4"
      ]
    ],
    [
      "00befcf4",
      "READ",
      [
        "storage",
        "003102f8",
        null,
        "undefined4"
      ]
    ],
    [
      "00befd08",
      "READ",
      [
        "storage",
        "003102c8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00befcf4",
      "READ",
      [
        "storage",
        "00310368",
        null,
        "undefined4"
      ]
    ],
    [
      "00befcf4",
      "READ",
      [
        "storage",
        "00310338",
        null,
        "undefined4"
      ]
    ],
    [
      "00befd08",
      "READ",
      [
        "storage",
        "00310308",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc28.md#insn-00bf0344) · [`00befc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc28.md#insn-00befc40) · [`00befcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc28.md#insn-00befcac)
- 新版 [`00bf03e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcc4.md#insn-00bf03e0) · [`00befcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcc4.md#insn-00befcdc) · [`00befd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcc4.md#insn-00befd48)

~~~diff
- 00bf0344 ["INT_ADD", "register:40f0:8", ["const:bf0344:8", "const:4:8"]]
- 00bf0344 ["CALL", null, ["callee:00bf03e4:8"]]
+ 00bf03e0 ["INT_ADD", "register:40f0:8", ["const:bf03e0:8", "const:4:8"]]
+ 00bf03e0 ["CALL", null, ["callee:00bf03e4:8"]]
- 00bf0344 bytes 01000094
+ 00bf03e0 bytes 01000094
- 00befc40 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 00befc40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00befc40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00befc40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00befcdc ["COPY", "tmp:0:8", ["const:308:8"]]
+ 00befcdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00befcdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00befcdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00befc40 bytes 08210b91
+ 00befcdc bytes 08210c91
- 00befcac ["COPY", "tmp:0:8", ["const:388:8"]]
- 00befcac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00befcac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00befcac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00befd48 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 00befd48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00befd48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00befd48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00befcac bytes 29210e91
+ 00befd48 bytes 29210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ad32616a5650eac8dbe47dd87081ed7"></a>

### [`00bf0348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0348.md) → [`00bf03e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md) FUN_00bf03e4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00befc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc28.md) · 呼出先 4件 [`00bf039c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf039c.md) [`00c37d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00befcc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcc4.md) · 呼出先 4件 [`00bf0438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0438.md) [`00c37df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37df8.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf0418",
      "incomplete_value": true,
      "site": "00bf0420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf037c",
      "incomplete_value": true,
      "site": "00bf0384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a78:8"
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
      "definition_site": "00bf041c",
      "incomplete_value": true,
      "site": "00bf0420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0380",
      "incomplete_value": true,
      "site": "00bf0384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a80:8"
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
      "00bf0418",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0418",
      "PARAM",
      [
        "storage",
        "00c968b0",
        "_ZTISt14overflow_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf041c",
      "READ",
      [
        "storage",
        "00c9ba80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf0418",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0418",
      "PARAM",
      [
        "storage",
        "00c96980",
        "_ZTISt14overflow_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf041c",
      "READ",
      [
        "storage",
        "00c9bb50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0348.md#insn-00bf0384) · [`00bf0360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0348.md#insn-00bf0360) · [`00bf036c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0348.md#insn-00bf036c)
- 新版 [`00bf0420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md#insn-00bf0420) · [`00bf03fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md#insn-00bf03fc) · [`00bf0408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md#insn-00bf0408)

~~~diff
- 00bf0384 ["INT_ADD", "register:40f0:8", ["const:bf0384:8", "const:4:8"]]
- 00bf0384 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf0420 ["INT_ADD", "register:40f0:8", ["const:bf0420:8", "const:4:8"]]
+ 00bf0420 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf0384 bytes e39e0194
+ 00bf0420 bytes f09e0194
- 00bf0360 ["INT_ADD", "register:40f0:8", ["const:bf0360:8", "const:4:8"]]
- 00bf0360 ["CALL", null, ["callee:00c57fc0:8"]]
+ 00bf03fc ["INT_ADD", "register:40f0:8", ["const:bf03fc:8", "const:4:8"]]
+ 00bf03fc ["CALL", null, ["callee:00c57fc0:8"]]
- 00bf0360 bytes e49e0194
+ 00bf03fc bytes f19e0194
- 00bf036c ["INT_ADD", "register:40f0:8", ["const:bf036c:8", "const:4:8"]]
- 00bf036c ["CALL", null, ["callee:00bf0438:8"]]
+ 00bf0408 ["INT_ADD", "register:40f0:8", ["const:bf0408:8", "const:4:8"]]
+ 00bf0408 ["CALL", null, ["callee:00bf0438:8"]]
- 00bf036c bytes 0c000094
+ 00bf0408 bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdae2b6a180036a230caf0856a43dc35"></a>

### [`00bf0408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0408.md) → [`00bf04a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf04a4.md) _ZNKSt6__ndk112bad_weak_ptr4whatEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf04ac",
      "incomplete_value": false,
      "site": "00bf04b0",
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
            "const:b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0410",
      "incomplete_value": false,
      "site": "00bf0414",
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
            "const:10b:8"
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
      "00bf04ac",
      "DATA",
      [
        "storage",
        "002bb10b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf04ac",
      "DATA",
      [
        "storage",
        "002bb0b7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0408.md#insn-00bf0410)
- 新版 [`00bf04ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf04a4.md#insn-00bf04ac)

~~~diff
- 00bf0410 ["COPY", "tmp:0:8", ["const:10b:8"]]
- 00bf0410 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf0410 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf0410 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf04ac ["COPY", "tmp:0:8", ["const:b7:8"]]
+ 00bf04ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf04ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf04ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf0410 bytes 002c0491
+ 00bf04ac bytes 00dc0291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2737b5f15f8edfd500e084b1a056683e"></a>

### [`00bf0718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0718.md) → [`00bf07b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07b4.md) _ZSt17__throw_bad_allocv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5df80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df80.md) · 呼出先 4件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a40.md)
- 新版 呼出元 1件 [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md) · 呼出先 4件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf07e0",
      "incomplete_value": true,
      "site": "00bf07e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0744",
      "incomplete_value": true,
      "site": "00bf074c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf07e4",
      "incomplete_value": true,
      "site": "00bf07e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0748",
      "incomplete_value": true,
      "site": "00bf074c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
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
      "00bf07e0",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf07e0",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf07e4",
      "READ",
      [
        "storage",
        "00c9adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf07e0",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf07e0",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf07e4",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf074c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0718.md#insn-00bf074c) · [`00bf072c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0718.md#insn-00bf072c) · [`00bf0734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0718.md#insn-00bf0734)
- 新版 [`00bf07e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07b4.md#insn-00bf07e8) · [`00bf07c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07b4.md#insn-00bf07c8) · [`00bf07d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07b4.md#insn-00bf07d0)

~~~diff
- 00bf074c ["INT_ADD", "register:40f0:8", ["const:bf074c:8", "const:4:8"]]
- 00bf074c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf07e8 ["INT_ADD", "register:40f0:8", ["const:bf07e8:8", "const:4:8"]]
+ 00bf07e8 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf074c bytes f19d0194
+ 00bf07e8 bytes fe9d0194
- 00bf072c ["INT_ADD", "register:40f0:8", ["const:bf072c:8", "const:4:8"]]
- 00bf072c ["CALL", null, ["callee:00c57fc0:8"]]
+ 00bf07c8 ["INT_ADD", "register:40f0:8", ["const:bf07c8:8", "const:4:8"]]
+ 00bf07c8 ["CALL", null, ["callee:00c57fc0:8"]]
- 00bf072c bytes f19d0194
+ 00bf07c8 bytes fe9d0194
- 00bf0734 ["INT_ADD", "register:40f0:8", ["const:bf0734:8", "const:4:8"]]
- 00bf0734 ["CALL", null, ["callee:00c58b10:8"]]
+ 00bf07d0 ["INT_ADD", "register:40f0:8", ["const:bf07d0:8", "const:4:8"]]
+ 00bf07d0 ["CALL", null, ["callee:00c58b10:8"]]
- 00bf0734 bytes c3a00194
+ 00bf07d0 bytes d0a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f323f92431b8c893cdf7160fecc289d"></a>

### [`00bf0750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0750.md) → [`00bf07ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07ec.md) _ZNSt11logic_errorC2ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5df90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df90.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c5e060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e060.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf080c",
      "incomplete_value": true,
      "site": "00bf0810",
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
      "definition_site": "00bf0770",
      "incomplete_value": true,
      "site": "00bf0774",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf0808",
      "READ",
      [
        "storage",
        "00c9ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0810",
      "DATA",
      [
        "storage",
        "00c966d8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf0808",
      "READ",
      [
        "storage",
        "00c9bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0810",
      "DATA",
      [
        "storage",
        "00c967a8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf076c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0750.md#insn-00bf076c) · [`00bf078c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0750.md#insn-00bf078c) · [`00bf0798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0750.md#insn-00bf0798)
- 新版 [`00bf0808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07ec.md#insn-00bf0808) · [`00bf0828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07ec.md#insn-00bf0828) · [`00bf0834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf07ec.md#insn-00bf0834)

~~~diff
- 00bf076c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
- 00bf076c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf0808 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
+ 00bf0808 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf076c bytes 084945f9
+ 00bf0808 bytes 08b145f9
- 00bf078c ["INT_ADD", "register:40f0:8", ["const:bf078c:8", "const:4:8"]]
- 00bf078c ["CALL", null, ["callee:00c580b0:8"]]
+ 00bf0828 ["INT_ADD", "register:40f0:8", ["const:bf0828:8", "const:4:8"]]
+ 00bf0828 ["CALL", null, ["callee:00c580b0:8"]]
- 00bf078c bytes 159e0194
+ 00bf0828 bytes 229e0194
- 00bf0798 ["INT_ADD", "register:40f0:8", ["const:bf0798:8", "const:4:8"]]
- 00bf0798 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf0834 ["INT_ADD", "register:40f0:8", ["const:bf0834:8", "const:4:8"]]
+ 00bf0834 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf0798 bytes be9d0194
+ 00bf0834 bytes cb9d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27d39b01b43a553667b4d94b36a218a4"></a>

### [`00bf07e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf07e4.md) → [`00bf0880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0880.md) _ZNSt11logic_errorC1EPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f30.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c58000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58000.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf08a4",
      "incomplete_value": true,
      "site": "00bf08a8",
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
      "definition_site": "00bf0808",
      "incomplete_value": true,
      "site": "00bf080c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf08a0",
      "READ",
      [
        "storage",
        "00c9ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00bf08a8",
      "DATA",
      [
        "storage",
        "00c966d8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf08a0",
      "READ",
      [
        "storage",
        "00c9bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00bf08a8",
      "DATA",
      [
        "storage",
        "00c967a8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf07e4.md#insn-00bf0804) · [`00bf0814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf07e4.md#insn-00bf0814) · [`00bf0820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf07e4.md#insn-00bf0820)
- 新版 [`00bf08a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0880.md#insn-00bf08a0) · [`00bf08b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0880.md#insn-00bf08b0) · [`00bf08bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0880.md#insn-00bf08bc)

~~~diff
- 00bf0804 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
- 00bf0804 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf08a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
+ 00bf08a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf0804 bytes 084945f9
+ 00bf08a0 bytes 08b145f9
- 00bf0814 ["INT_ADD", "register:40f0:8", ["const:bf0814:8", "const:4:8"]]
- 00bf0814 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bf08b0 ["INT_ADD", "register:40f0:8", ["const:bf08b0:8", "const:4:8"]]
+ 00bf08b0 ["CALL", null, ["callee:00c580b0:8"]]
- 00bf0814 bytes f39d0194
+ 00bf08b0 bytes 009e0194
- 00bf0820 ["INT_ADD", "register:40f0:8", ["const:bf0820:8", "const:4:8"]]
- 00bf0820 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf08bc ["INT_ADD", "register:40f0:8", ["const:bf08bc:8", "const:4:8"]]
+ 00bf08bc ["CALL", null, ["callee:00c57f60:8"]]
- 00bf0820 bytes 9c9d0194
+ 00bf08bc bytes a99d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b6f4b82facbaada72776e75100eb3d3"></a>

### [`00bf0900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0900.md) → [`00bf099c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf099c.md) _ZNSt13runtime_errorC1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5dfa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfa0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c5e070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e070.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf09bc",
      "incomplete_value": true,
      "site": "00bf09c0",
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
      "definition_site": "00bf0920",
      "incomplete_value": true,
      "site": "00bf0924",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf09b8",
      "READ",
      [
        "storage",
        "00c9ba98",
        null,
        "pointer"
      ]
    ],
    [
      "00bf09c0",
      "DATA",
      [
        "storage",
        "00c96700",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf09b8",
      "READ",
      [
        "storage",
        "00c9bb68",
        null,
        "pointer"
      ]
    ],
    [
      "00bf09c0",
      "DATA",
      [
        "storage",
        "00c967d0",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf091c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0900.md#insn-00bf091c) · [`00bf093c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0900.md#insn-00bf093c) · [`00bf0948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0900.md#insn-00bf0948)
- 新版 [`00bf09b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf099c.md#insn-00bf09b8) · [`00bf09d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf099c.md#insn-00bf09d8) · [`00bf09e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf099c.md#insn-00bf09e4)

~~~diff
- 00bf091c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a98:8"]]
- 00bf091c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf09b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b68:8"]]
+ 00bf09b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf091c bytes 084d45f9
+ 00bf09b8 bytes 08b545f9
- 00bf093c ["INT_ADD", "register:40f0:8", ["const:bf093c:8", "const:4:8"]]
- 00bf093c ["CALL", null, ["callee:00c580b0:8"]]
+ 00bf09d8 ["INT_ADD", "register:40f0:8", ["const:bf09d8:8", "const:4:8"]]
+ 00bf09d8 ["CALL", null, ["callee:00c580b0:8"]]
- 00bf093c bytes a99d0194
+ 00bf09d8 bytes b69d0194
- 00bf0948 ["INT_ADD", "register:40f0:8", ["const:bf0948:8", "const:4:8"]]
- 00bf0948 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf09e4 ["INT_ADD", "register:40f0:8", ["const:bf09e4:8", "const:4:8"]]
+ 00bf09e4 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf0948 bytes 529d0194
+ 00bf09e4 bytes 5f9d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5672935add9766f10fa24f4bbb8810bf"></a>

### [`00bf0994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0994.md) → [`00bf0a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0a30.md) _ZNSt13runtime_errorC1EPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5a8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8d0.md) [`00c5dfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfc0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 2件 [`00c5a9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9a0.md) [`00c5e090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e090.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf0a54",
      "incomplete_value": true,
      "site": "00bf0a58",
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
      "definition_site": "00bf09b8",
      "incomplete_value": true,
      "site": "00bf09bc",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf0a50",
      "READ",
      [
        "storage",
        "00c9ba98",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0a58",
      "DATA",
      [
        "storage",
        "00c96700",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf0a50",
      "READ",
      [
        "storage",
        "00c9bb68",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0a58",
      "DATA",
      [
        "storage",
        "00c967d0",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf09b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0994.md#insn-00bf09b4) · [`00bf09c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0994.md#insn-00bf09c4) · [`00bf09d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0994.md#insn-00bf09d0)
- 新版 [`00bf0a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0a30.md#insn-00bf0a50) · [`00bf0a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0a30.md#insn-00bf0a60) · [`00bf0a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0a30.md#insn-00bf0a6c)

~~~diff
- 00bf09b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a98:8"]]
- 00bf09b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf0a50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b68:8"]]
+ 00bf0a50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf09b4 bytes 084d45f9
+ 00bf0a50 bytes 08b545f9
- 00bf09c4 ["INT_ADD", "register:40f0:8", ["const:bf09c4:8", "const:4:8"]]
- 00bf09c4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bf0a60 ["INT_ADD", "register:40f0:8", ["const:bf0a60:8", "const:4:8"]]
+ 00bf0a60 ["CALL", null, ["callee:00c580b0:8"]]
- 00bf09c4 bytes 879d0194
+ 00bf0a60 bytes 949d0194
- 00bf09d0 ["INT_ADD", "register:40f0:8", ["const:bf09d0:8", "const:4:8"]]
- 00bf09d0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf0a6c ["INT_ADD", "register:40f0:8", ["const:bf0a6c:8", "const:4:8"]]
+ 00bf0a6c ["CALL", null, ["callee:00c57f60:8"]]
- 00bf09d0 bytes 309d0194
+ 00bf0a6c bytes 3d9d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47b598ee5e61bfa1b786b230a7d6690d"></a>

### [`00bf0ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0ab0.md) → [`00bf0b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0b4c.md) _ZNSt6__ndk121__throw_runtime_errorEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md) · 呼出先 4件 [`00c37d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5dfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfc0.md)
- 新版 呼出元 1件 [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md) · 呼出先 4件 [`00c37df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37df8.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5e090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf0b80",
      "incomplete_value": true,
      "site": "00bf0b88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0ae4",
      "incomplete_value": true,
      "site": "00bf0aec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa0:8"
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
      "definition_site": "00bf0b84",
      "incomplete_value": true,
      "site": "00bf0b88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0ae8",
      "incomplete_value": true,
      "site": "00bf0aec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa8:8"
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
      "00bf0b80",
      "READ",
      [
        "storage",
        "00c9baa0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0b80",
      "PARAM",
      [
        "storage",
        "00c96858",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf0b84",
      "READ",
      [
        "storage",
        "00c9baa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf0b80",
      "READ",
      [
        "storage",
        "00c9bb70",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0b80",
      "PARAM",
      [
        "storage",
        "00c96928",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf0b84",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0ab0.md#insn-00bf0aec) · [`00bf0ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0ab0.md#insn-00bf0ac8) · [`00bf0ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0ab0.md#insn-00bf0ad4)
- 新版 [`00bf0b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0b4c.md#insn-00bf0b88) · [`00bf0b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0b4c.md#insn-00bf0b64) · [`00bf0b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0b4c.md#insn-00bf0b70)

~~~diff
- 00bf0aec ["INT_ADD", "register:40f0:8", ["const:bf0aec:8", "const:4:8"]]
- 00bf0aec ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf0b88 ["INT_ADD", "register:40f0:8", ["const:bf0b88:8", "const:4:8"]]
+ 00bf0b88 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf0aec bytes 099d0194
+ 00bf0b88 bytes 169d0194
- 00bf0ac8 ["INT_ADD", "register:40f0:8", ["const:bf0ac8:8", "const:4:8"]]
- 00bf0ac8 ["CALL", null, ["callee:00c57fc0:8"]]
+ 00bf0b64 ["INT_ADD", "register:40f0:8", ["const:bf0b64:8", "const:4:8"]]
+ 00bf0b64 ["CALL", null, ["callee:00c57fc0:8"]]
- 00bf0ac8 bytes 0a9d0194
+ 00bf0b64 bytes 179d0194
- 00bf0ad4 ["INT_ADD", "register:40f0:8", ["const:bf0ad4:8", "const:4:8"]]
- 00bf0ad4 ["CALL", null, ["callee:00c5e090:8"]]
+ 00bf0b70 ["INT_ADD", "register:40f0:8", ["const:bf0b70:8", "const:4:8"]]
+ 00bf0b70 ["CALL", null, ["callee:00c5e090:8"]]
- 00bf0ad4 bytes 3bb50194
+ 00bf0b70 bytes 48b50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54aa88a92f8c0b696dcb60108fd331ac"></a>

### [`00bf20a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf20a4.md) → [`00bf2140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2140.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmRKS5_mm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf21e8",
      "incomplete_value": false,
      "site": "00bf21ec",
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
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf214c",
      "incomplete_value": false,
      "site": "00bf2150",
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
            "const:714:8"
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
      "00bf21e8",
      "PARAM",
      [
        "storage",
        "002af714",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf21e8",
      "PARAM",
      [
        "storage",
        "002af6b8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf2150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf20a4.md#insn-00bf2150) · [`00bf211c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf20a4.md#insn-00bf211c) · [`00bf214c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf20a4.md#insn-00bf214c)
- 新版 [`00bf21ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2140.md#insn-00bf21ec) · [`00bf21b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2140.md#insn-00bf21b8) · [`00bf21e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2140.md#insn-00bf21e8)

~~~diff
- 00bf2150 ["INT_ADD", "register:40f0:8", ["const:bf2150:8", "const:4:8"]]
- 00bf2150 ["CALL", null, ["callee:00442970:8"]]
+ 00bf21ec ["INT_ADD", "register:40f0:8", ["const:bf21ec:8", "const:4:8"]]
+ 00bf21ec ["CALL", null, ["callee:00442970:8"]]
- 00bf2150 bytes f841e197
+ 00bf21ec bytes e141e197
- 00bf211c ["INT_ADD", "register:40f0:8", ["const:bf211c:8", "const:4:8"]]
- 00bf211c ["CALL", null, ["callee:00c58120:8"]]
+ 00bf21b8 ["INT_ADD", "register:40f0:8", ["const:bf21b8:8", "const:4:8"]]
+ 00bf21b8 ["CALL", null, ["callee:00c58120:8"]]
- 00bf211c bytes cd970194
+ 00bf21b8 bytes da970194
- 00bf214c ["COPY", "tmp:0:8", ["const:714:8"]]
- 00bf214c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf214c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf214c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf21e8 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00bf21e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf21e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf21e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf214c bytes 00501c91
+ 00bf21e8 bytes 00e01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b70f77b676737e0116ecfe1b0b254115"></a>

### [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) → [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) FUN_00bf2974

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 17件 [`00bf2700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2700.md) [`00bf2ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2ddc.md) [`00bf301c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf301c.md) [`00bf3064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3064.md) [`00bf3210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3210.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 17件 [`00bf279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf279c.md) [`00bf2e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2e78.md) [`00bf30b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf30b8.md) [`00bf3100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3100.md) [`00bf32ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf32ac.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf2984",
      "incomplete_value": false,
      "site": "00bf2988",
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
            "const:ecf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf28e8",
      "incomplete_value": false,
      "site": "00bf28ec",
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
            "const:f23:8"
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
      "00bf2984",
      "PARAM",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf2984",
      "PARAM",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf28ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md#insn-00bf28ec) · [`00bf28e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md#insn-00bf28e8)
- 新版 [`00bf2988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md#insn-00bf2988) · [`00bf2984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md#insn-00bf2984)

~~~diff
- 00bf28ec ["INT_ADD", "register:40f0:8", ["const:bf28ec:8", "const:4:8"]]
- 00bf28ec ["CALL", null, ["callee:00442970:8"]]
+ 00bf2988 ["INT_ADD", "register:40f0:8", ["const:bf2988:8", "const:4:8"]]
+ 00bf2988 ["CALL", null, ["callee:00442970:8"]]
- 00bf28ec bytes 1140e197
+ 00bf2988 bytes fa3fe197
- 00bf28e8 ["COPY", "tmp:0:8", ["const:f23:8"]]
- 00bf28e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf28e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf28e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf2984 ["COPY", "tmp:0:8", ["const:ecf:8"]]
+ 00bf2984 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf2984 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf2984 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf28e8 bytes 008c3c91
+ 00bf2984 bytes 003c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbb43f92218a988816ee3680c3e9be63"></a>

### [`00bf4510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4510.md) → [`00bf45ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf45ac.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmRKS5_mm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00c5e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00c5e110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e110.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf465c",
      "incomplete_value": false,
      "site": "00bf4660",
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
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf45c0",
      "incomplete_value": false,
      "site": "00bf45c4",
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
            "const:714:8"
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
      "00bf465c",
      "PARAM",
      [
        "storage",
        "002af714",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf465c",
      "PARAM",
      [
        "storage",
        "002af6b8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf45c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4510.md#insn-00bf45c4) · [`00bf4594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4510.md#insn-00bf4594) · [`00bf45c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4510.md#insn-00bf45c0)
- 新版 [`00bf4660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf45ac.md#insn-00bf4660) · [`00bf4630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf45ac.md#insn-00bf4630) · [`00bf465c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf45ac.md#insn-00bf465c)

~~~diff
- 00bf45c4 ["INT_ADD", "register:40f0:8", ["const:bf45c4:8", "const:4:8"]]
- 00bf45c4 ["CALL", null, ["callee:00442970:8"]]
+ 00bf4660 ["INT_ADD", "register:40f0:8", ["const:bf4660:8", "const:4:8"]]
+ 00bf4660 ["CALL", null, ["callee:00442970:8"]]
- 00bf45c4 bytes db38e197
+ 00bf4660 bytes c438e197
- 00bf4594 ["INT_ADD", "register:40f0:8", ["const:bf4594:8", "const:4:8"]]
- 00bf4594 ["CALL", null, ["callee:00c5e110:8"]]
+ 00bf4630 ["INT_ADD", "register:40f0:8", ["const:bf4630:8", "const:4:8"]]
+ 00bf4630 ["CALL", null, ["callee:00c5e110:8"]]
- 00bf4594 bytes aba60194
+ 00bf4630 bytes b8a60194
- 00bf45c0 ["COPY", "tmp:0:8", ["const:714:8"]]
- 00bf45c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf45c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf45c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf465c ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00bf465c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf465c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf465c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf45c0 bytes 00501c91
+ 00bf465c bytes 00e01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbad3407c4900a07b55b1f03b8069c2d"></a>

### [`00bf4b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b70.md) → [`00bf4c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c0c.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_length_errorEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b090.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00c5b160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b160.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf4c1c",
      "incomplete_value": false,
      "site": "00bf4c20",
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
            "const:ecf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4b80",
      "incomplete_value": false,
      "site": "00bf4b84",
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
            "const:f23:8"
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
      "00bf4c1c",
      "PARAM",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf4c1c",
      "PARAM",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b70.md#insn-00bf4b84) · [`00bf4b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b70.md#insn-00bf4b80)
- 新版 [`00bf4c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c0c.md#insn-00bf4c20) · [`00bf4c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c0c.md#insn-00bf4c1c)

~~~diff
- 00bf4b84 ["INT_ADD", "register:40f0:8", ["const:bf4b84:8", "const:4:8"]]
- 00bf4b84 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00bf4c20 ["INT_ADD", "register:40f0:8", ["const:bf4c20:8", "const:4:8"]]
+ 00bf4c20 ["CALL", null, ["callee:0043b7b8:8"]]
- 00bf4b84 bytes fd1ae197
+ 00bf4c20 bytes e61ae197
- 00bf4b80 ["COPY", "tmp:0:8", ["const:f23:8"]]
- 00bf4b80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4b80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4b80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf4c1c ["COPY", "tmp:0:8", ["const:ecf:8"]]
+ 00bf4c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf4c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf4c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf4b80 bytes 008c3c91
+ 00bf4c1c bytes 003c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b85fb1c3f0b777950564e7932d03ba9"></a>

### [`00bf4b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b88.md) → [`00bf4c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c24.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_out_of_rangeEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d450.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 1件 [`00c5d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d520.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf4c34",
      "incomplete_value": false,
      "site": "00bf4c38",
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
            "const:ecf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4b98",
      "incomplete_value": false,
      "site": "00bf4b9c",
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
            "const:f23:8"
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
      "00bf4c34",
      "PARAM",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf4c34",
      "PARAM",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b88.md#insn-00bf4b9c) · [`00bf4b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b88.md#insn-00bf4b98)
- 新版 [`00bf4c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c24.md#insn-00bf4c38) · [`00bf4c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c24.md#insn-00bf4c34)

~~~diff
- 00bf4b9c ["INT_ADD", "register:40f0:8", ["const:bf4b9c:8", "const:4:8"]]
- 00bf4b9c ["CALL", null, ["callee:00442970:8"]]
+ 00bf4c38 ["INT_ADD", "register:40f0:8", ["const:bf4c38:8", "const:4:8"]]
+ 00bf4c38 ["CALL", null, ["callee:00442970:8"]]
- 00bf4b9c bytes 6537e197
+ 00bf4c38 bytes 4e37e197
- 00bf4b98 ["COPY", "tmp:0:8", ["const:f23:8"]]
- 00bf4b98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4b98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4b98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf4c34 ["COPY", "tmp:0:8", ["const:ecf:8"]]
+ 00bf4c34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf4c34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf4c34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf4b98 bytes 008c3c91
+ 00bf4c34 bytes 003c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ea6fde90b9ddea12e182b915d91c9c4"></a>

### [`00bf4ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4ba0.md) → [`00bf4c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c3c.md) _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58060.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`00bf817c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c58590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58590.md)
- 新版 呼出元 1件 [`00c58130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58130.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`00bf8218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58660.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf4d5c",
      "incomplete_value": true,
      "site": "00bf4d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4cc0",
      "incomplete_value": true,
      "site": "00bf4cc0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf4d64",
      "incomplete_value": true,
      "site": "00bf4d64",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4cc8",
      "incomplete_value": true,
      "site": "00bf4cc8",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf4d08",
      "incomplete_value": false,
      "site": "00bf4d18",
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
            "const:d72:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4c6c",
      "incomplete_value": false,
      "site": "00bf4c7c",
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
            "const:dc6:8"
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
      "00bf4d08",
      "PARAM",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf4d4c",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf4d50",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf4d08",
      "PARAM",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf4d4c",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf4d50",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4ba0.md#insn-00bf4c7c) · [`00bf4bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4ba0.md#insn-00bf4bf0) · [`00bf4c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4ba0.md#insn-00bf4c0c)
- 新版 [`00bf4d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c3c.md#insn-00bf4d18) · [`00bf4c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c3c.md#insn-00bf4c8c) · [`00bf4ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c3c.md#insn-00bf4ca8)

~~~diff
- 00bf4c7c ["INT_ADD", "register:40f0:8", ["const:bf4c7c:8", "const:4:8"]]
- 00bf4c7c ["CALL", null, ["callee:00481ec0:8"]]
+ 00bf4d18 ["INT_ADD", "register:40f0:8", ["const:bf4d18:8", "const:4:8"]]
+ 00bf4d18 ["CALL", null, ["callee:00481ec0:8"]]
- 00bf4c7c bytes 8134e297
+ 00bf4d18 bytes 6a34e297
- 00bf4bf0 ["INT_ADD", "register:40f0:8", ["const:bf4bf0:8", "const:4:8"]]
- 00bf4bf0 ["CALL", null, ["callee:00c58190:8"]]
+ 00bf4c8c ["INT_ADD", "register:40f0:8", ["const:bf4c8c:8", "const:4:8"]]
+ 00bf4c8c ["CALL", null, ["callee:00c58190:8"]]
- 00bf4bf0 bytes 348d0194
+ 00bf4c8c bytes 418d0194
- 00bf4c0c ["INT_ADD", "register:40f0:8", ["const:bf4c0c:8", "const:4:8"]]
- 00bf4c0c ["CALL", null, ["callee:00c58660:8"]]
+ 00bf4ca8 ["INT_ADD", "register:40f0:8", ["const:bf4ca8:8", "const:4:8"]]
+ 00bf4ca8 ["CALL", null, ["callee:00c58660:8"]]
- 00bf4c0c bytes 618e0194
+ 00bf4ca8 bytes 6e8e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-556dab66f70424c900fa076062e769bf"></a>

### [`00bf4cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4cfc.md) → [`00bf4d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4d98.md) _ZNSt6__ndk14stolERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`00bf817c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`00bf8218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf4e5c",
      "incomplete_value": false,
      "site": "00bf4e6c",
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
            "const:d72:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4dc0",
      "incomplete_value": false,
      "site": "00bf4dd0",
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
            "const:dc6:8"
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
      "00bf4e5c",
      "PARAM",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf4e5c",
      "PARAM",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4cfc.md#insn-00bf4dd0) · [`00bf4d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4cfc.md#insn-00bf4d4c) · [`00bf4d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4cfc.md#insn-00bf4d68)
- 新版 [`00bf4e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4d98.md#insn-00bf4e6c) · [`00bf4de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4d98.md#insn-00bf4de8) · [`00bf4e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4d98.md#insn-00bf4e04)

~~~diff
- 00bf4dd0 ["INT_ADD", "register:40f0:8", ["const:bf4dd0:8", "const:4:8"]]
- 00bf4dd0 ["CALL", null, ["callee:00481ec0:8"]]
+ 00bf4e6c ["INT_ADD", "register:40f0:8", ["const:bf4e6c:8", "const:4:8"]]
+ 00bf4e6c ["CALL", null, ["callee:00481ec0:8"]]
- 00bf4dd0 bytes 2c34e297
+ 00bf4e6c bytes 1534e297
- 00bf4d4c ["INT_ADD", "register:40f0:8", ["const:bf4d4c:8", "const:4:8"]]
- 00bf4d4c ["CALL", null, ["callee:00c58190:8"]]
+ 00bf4de8 ["INT_ADD", "register:40f0:8", ["const:bf4de8:8", "const:4:8"]]
+ 00bf4de8 ["CALL", null, ["callee:00c58190:8"]]
- 00bf4d4c bytes dd8c0194
+ 00bf4de8 bytes ea8c0194
- 00bf4d68 ["INT_ADD", "register:40f0:8", ["const:bf4d68:8", "const:4:8"]]
- 00bf4d68 ["CALL", null, ["callee:00c58660:8"]]
+ 00bf4e04 ["INT_ADD", "register:40f0:8", ["const:bf4e04:8", "const:4:8"]]
+ 00bf4e04 ["CALL", null, ["callee:00c58660:8"]]
- 00bf4d68 bytes 0a8e0194
+ 00bf4e04 bytes 178e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b4a640c4b57c303c17df7b7997f4bfe"></a>

### [`00bf4e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4e14.md) → [`00bf4eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4eb0.md) _ZNSt6__ndk15stoulERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c589f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589f0.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)
- 新版 呼出元 1件 [`00c58ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ac0.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.01% / 新版 89.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf4fac",
      "incomplete_value": true,
      "site": "00bf4fac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4f10",
      "incomplete_value": true,
      "site": "00bf4f10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
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
      "definition_site": "00bf4fb0",
      "incomplete_value": true,
      "site": "00bf4fb0",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4f14",
      "incomplete_value": true,
      "site": "00bf4f14",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
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
      "definition_site": "00bf4fec",
      "incomplete_value": true,
      "site": "00bf4fec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4f50",
      "incomplete_value": true,
      "site": "00bf4f50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf4f94",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf4f98",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf4fd4",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf4f94",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf4f98",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf4fd4",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4e14.md#insn-00bf4e70) · [`00bf4e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4e14.md#insn-00bf4e8c) · [`00bf4ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4e14.md#insn-00bf4ebc)
- 新版 [`00bf4f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4eb0.md#insn-00bf4f0c) · [`00bf4f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4eb0.md#insn-00bf4f28) · [`00bf4f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4eb0.md#insn-00bf4f58)

~~~diff
- 00bf4e70 ["INT_ADD", "register:40f0:8", ["const:bf4e70:8", "const:4:8"]]
- 00bf4e70 ["CALL", null, ["callee:00c58190:8"]]
+ 00bf4f0c ["INT_ADD", "register:40f0:8", ["const:bf4f0c:8", "const:4:8"]]
+ 00bf4f0c ["CALL", null, ["callee:00c58190:8"]]
- 00bf4e70 bytes 948c0194
+ 00bf4f0c bytes a18c0194
- 00bf4e8c ["INT_ADD", "register:40f0:8", ["const:bf4e8c:8", "const:4:8"]]
- 00bf4e8c ["CALL", null, ["callee:00c5e130:8"]]
+ 00bf4f28 ["INT_ADD", "register:40f0:8", ["const:bf4f28:8", "const:4:8"]]
+ 00bf4f28 ["CALL", null, ["callee:00c5e130:8"]]
- 00bf4e8c bytes 75a40194
+ 00bf4f28 bytes 82a40194
- 00bf4ebc ["INT_ADD", "register:40f0:8", ["const:bf4ebc:8", "const:4:8"]]
- 00bf4ebc ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf4f58 ["INT_ADD", "register:40f0:8", ["const:bf4f58:8", "const:4:8"]]
+ 00bf4f58 ["CALL", null, ["callee:00c5e120:8"]]
- 00bf4ebc bytes 65a40194
+ 00bf4f58 bytes 72a40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc7af3a951fb1c37a7a5eaace3d851bc"></a>

### [`00bf4f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4f80.md) → [`00bf501c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf501c.md) _ZNSt6__ndk15stollERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58230.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c585a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585a0.md)
- 新版 呼出元 1件 [`00c58300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58300.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58670.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.01% / 新版 89.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5118",
      "incomplete_value": true,
      "site": "00bf5118",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf507c",
      "incomplete_value": true,
      "site": "00bf507c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
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
      "definition_site": "00bf511c",
      "incomplete_value": true,
      "site": "00bf511c",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5080",
      "incomplete_value": true,
      "site": "00bf5080",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
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
      "definition_site": "00bf5158",
      "incomplete_value": true,
      "site": "00bf5158",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf50bc",
      "incomplete_value": true,
      "site": "00bf50bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf5100",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5104",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5140",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5100",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5104",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf5140",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4f80.md#insn-00bf4fdc) · [`00bf4ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4f80.md#insn-00bf4ff8) · [`00bf5028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4f80.md#insn-00bf5028)
- 新版 [`00bf5078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf501c.md#insn-00bf5078) · [`00bf5094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf501c.md#insn-00bf5094) · [`00bf50c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf501c.md#insn-00bf50c4)

~~~diff
- 00bf4fdc ["INT_ADD", "register:40f0:8", ["const:bf4fdc:8", "const:4:8"]]
- 00bf4fdc ["CALL", null, ["callee:00c58190:8"]]
+ 00bf5078 ["INT_ADD", "register:40f0:8", ["const:bf5078:8", "const:4:8"]]
+ 00bf5078 ["CALL", null, ["callee:00c58190:8"]]
- 00bf4fdc bytes 398c0194
+ 00bf5078 bytes 468c0194
- 00bf4ff8 ["INT_ADD", "register:40f0:8", ["const:bf4ff8:8", "const:4:8"]]
- 00bf4ff8 ["CALL", null, ["callee:00c58670:8"]]
+ 00bf5094 ["INT_ADD", "register:40f0:8", ["const:bf5094:8", "const:4:8"]]
+ 00bf5094 ["CALL", null, ["callee:00c58670:8"]]
- 00bf4ff8 bytes 6a8d0194
+ 00bf5094 bytes 778d0194
- 00bf5028 ["INT_ADD", "register:40f0:8", ["const:bf5028:8", "const:4:8"]]
- 00bf5028 ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf50c4 ["INT_ADD", "register:40f0:8", ["const:bf50c4:8", "const:4:8"]]
+ 00bf50c4 ["CALL", null, ["callee:00c5e120:8"]]
- 00bf5028 bytes 0aa40194
+ 00bf50c4 bytes 17a40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a10aa8788412f61f622874cf9e67e18d"></a>

### [`00bf50ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf50ec.md) → [`00bf5188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5188.md) _ZNSt6__ndk16stoullERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58240.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)
- 新版 呼出元 1件 [`00c58310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58310.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.13% / 新版 89.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5288",
      "incomplete_value": true,
      "site": "00bf5288",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf51ec",
      "incomplete_value": true,
      "site": "00bf51ec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
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
      "definition_site": "00bf528c",
      "incomplete_value": true,
      "site": "00bf528c",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf51f0",
      "incomplete_value": true,
      "site": "00bf51f0",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
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
      "definition_site": "00bf52c8",
      "incomplete_value": true,
      "site": "00bf52c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf522c",
      "incomplete_value": true,
      "site": "00bf522c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf5270",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5274",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf52b0",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5270",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5274",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf52b0",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf514c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf50ec.md#insn-00bf514c) · [`00bf5168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf50ec.md#insn-00bf5168) · [`00bf5198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf50ec.md#insn-00bf5198)
- 新版 [`00bf51e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5188.md#insn-00bf51e8) · [`00bf5204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5188.md#insn-00bf5204) · [`00bf5234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5188.md#insn-00bf5234)

~~~diff
- 00bf514c ["INT_ADD", "register:40f0:8", ["const:bf514c:8", "const:4:8"]]
- 00bf514c ["CALL", null, ["callee:00c58190:8"]]
+ 00bf51e8 ["INT_ADD", "register:40f0:8", ["const:bf51e8:8", "const:4:8"]]
+ 00bf51e8 ["CALL", null, ["callee:00c58190:8"]]
- 00bf514c bytes dd8b0194
+ 00bf51e8 bytes ea8b0194
- 00bf5168 ["INT_ADD", "register:40f0:8", ["const:bf5168:8", "const:4:8"]]
- 00bf5168 ["CALL", null, ["callee:00c5e140:8"]]
+ 00bf5204 ["INT_ADD", "register:40f0:8", ["const:bf5204:8", "const:4:8"]]
+ 00bf5204 ["CALL", null, ["callee:00c5e140:8"]]
- 00bf5168 bytes c2a30194
+ 00bf5204 bytes cfa30194
- 00bf5198 ["INT_ADD", "register:40f0:8", ["const:bf5198:8", "const:4:8"]]
- 00bf5198 ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf5234 ["INT_ADD", "register:40f0:8", ["const:bf5234:8", "const:4:8"]]
+ 00bf5234 ["CALL", null, ["callee:00c5e120:8"]]
- 00bf5198 bytes aea30194
+ 00bf5234 bytes bba30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9030efd59bc994cd9aabf310c31f0fb"></a>

### [`00bf525c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf525c.md) → [`00bf52f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf52f8.md) _ZNSt6__ndk14stofERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c585e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585e0.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c585b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585b0.md)
- 新版 呼出元 1件 [`00c586b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586b0.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf53d4",
      "incomplete_value": true,
      "site": "00bf53d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5338",
      "incomplete_value": true,
      "site": "00bf5338",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf53dc",
      "incomplete_value": true,
      "site": "00bf53dc",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5340",
      "incomplete_value": true,
      "site": "00bf5340",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
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
      "definition_site": "00bf540c",
      "incomplete_value": true,
      "site": "00bf540c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5370",
      "incomplete_value": true,
      "site": "00bf5370",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf53c4",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf53c8",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf53fc",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf53c4",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf53c8",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf53fc",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf52a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf525c.md#insn-00bf52a8) · [`00bf52c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf525c.md#insn-00bf52c0) · [`00bf52f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf525c.md#insn-00bf52f0)
- 新版 [`00bf5344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf52f8.md#insn-00bf5344) · [`00bf535c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf52f8.md#insn-00bf535c) · [`00bf538c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf52f8.md#insn-00bf538c)

~~~diff
- 00bf52a8 ["INT_ADD", "register:40f0:8", ["const:bf52a8:8", "const:4:8"]]
- 00bf52a8 ["CALL", null, ["callee:00c58190:8"]]
+ 00bf5344 ["INT_ADD", "register:40f0:8", ["const:bf5344:8", "const:4:8"]]
+ 00bf5344 ["CALL", null, ["callee:00c58190:8"]]
- 00bf52a8 bytes 868b0194
+ 00bf5344 bytes 938b0194
- 00bf52c0 ["INT_ADD", "register:40f0:8", ["const:bf52c0:8", "const:4:8"]]
- 00bf52c0 ["CALL", null, ["callee:00c58680:8"]]
+ 00bf535c ["INT_ADD", "register:40f0:8", ["const:bf535c:8", "const:4:8"]]
+ 00bf535c ["CALL", null, ["callee:00c58680:8"]]
- 00bf52c0 bytes bc8c0194
+ 00bf535c bytes c98c0194
- 00bf52f0 ["INT_ADD", "register:40f0:8", ["const:bf52f0:8", "const:4:8"]]
- 00bf52f0 ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf538c ["INT_ADD", "register:40f0:8", ["const:bf538c:8", "const:4:8"]]
+ 00bf538c ["CALL", null, ["callee:00c5e120:8"]]
- 00bf52f0 bytes 58a30194
+ 00bf538c bytes 65a30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe176ad9c209311b55348521e6f7b679"></a>

### [`00bf53a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf53a4.md) → [`00bf5440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5440.md) _ZNSt6__ndk14stodERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58250.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c585c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585c0.md)
- 新版 呼出元 1件 [`00c58320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58320.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf551c",
      "incomplete_value": true,
      "site": "00bf551c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5480",
      "incomplete_value": true,
      "site": "00bf5480",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5524",
      "incomplete_value": true,
      "site": "00bf5524",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5488",
      "incomplete_value": true,
      "site": "00bf5488",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
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
      "definition_site": "00bf5554",
      "incomplete_value": true,
      "site": "00bf5554",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf54b8",
      "incomplete_value": true,
      "site": "00bf54b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf550c",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5510",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5544",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf550c",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5510",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf5544",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf53f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf53a4.md#insn-00bf53f0) · [`00bf5408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf53a4.md#insn-00bf5408) · [`00bf5438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf53a4.md#insn-00bf5438)
- 新版 [`00bf548c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5440.md#insn-00bf548c) · [`00bf54a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5440.md#insn-00bf54a4) · [`00bf54d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5440.md#insn-00bf54d4)

~~~diff
- 00bf53f0 ["INT_ADD", "register:40f0:8", ["const:bf53f0:8", "const:4:8"]]
- 00bf53f0 ["CALL", null, ["callee:00c58190:8"]]
+ 00bf548c ["INT_ADD", "register:40f0:8", ["const:bf548c:8", "const:4:8"]]
+ 00bf548c ["CALL", null, ["callee:00c58190:8"]]
- 00bf53f0 bytes 348b0194
+ 00bf548c bytes 418b0194
- 00bf5408 ["INT_ADD", "register:40f0:8", ["const:bf5408:8", "const:4:8"]]
- 00bf5408 ["CALL", null, ["callee:00c58690:8"]]
+ 00bf54a4 ["INT_ADD", "register:40f0:8", ["const:bf54a4:8", "const:4:8"]]
+ 00bf54a4 ["CALL", null, ["callee:00c58690:8"]]
- 00bf5408 bytes 6e8c0194
+ 00bf54a4 bytes 7b8c0194
- 00bf5438 ["INT_ADD", "register:40f0:8", ["const:bf5438:8", "const:4:8"]]
- 00bf5438 ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf54d4 ["INT_ADD", "register:40f0:8", ["const:bf54d4:8", "const:4:8"]]
+ 00bf54d4 ["CALL", null, ["callee:00c5e120:8"]]
- 00bf5438 bytes 06a30194
+ 00bf54d4 bytes 13a30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afec945125e6115d24eaf2bbf5f916d1"></a>

### [`00bf54ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf54ec.md) → [`00bf5588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5588.md) _ZNSt6__ndk15stoldERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.76% / 新版 88.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf567c",
      "incomplete_value": true,
      "site": "00bf567c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf55e0",
      "incomplete_value": true,
      "site": "00bf55e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
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
      "definition_site": "00bf5680",
      "incomplete_value": true,
      "site": "00bf5680",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf55e4",
      "incomplete_value": true,
      "site": "00bf55e4",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
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
      "definition_site": "00bf56bc",
      "incomplete_value": true,
      "site": "00bf56bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5620",
      "incomplete_value": true,
      "site": "00bf5620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf5664",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5668",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf56a4",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5664",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5668",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf56a4",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf54ec.md#insn-00bf5544) · [`00bf555c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf54ec.md#insn-00bf555c) · [`00bf558c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf54ec.md#insn-00bf558c)
- 新版 [`00bf55e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5588.md#insn-00bf55e0) · [`00bf55f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5588.md#insn-00bf55f8) · [`00bf5628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5588.md#insn-00bf5628)

~~~diff
- 00bf5544 ["INT_ADD", "register:40f0:8", ["const:bf5544:8", "const:4:8"]]
- 00bf5544 ["CALL", null, ["callee:00c58190:8"]]
+ 00bf55e0 ["INT_ADD", "register:40f0:8", ["const:bf55e0:8", "const:4:8"]]
+ 00bf55e0 ["CALL", null, ["callee:00c58190:8"]]
- 00bf5544 bytes df8a0194
+ 00bf55e0 bytes ec8a0194
- 00bf555c ["INT_ADD", "register:40f0:8", ["const:bf555c:8", "const:4:8"]]
- 00bf555c ["CALL", null, ["callee:00c5e150:8"]]
+ 00bf55f8 ["INT_ADD", "register:40f0:8", ["const:bf55f8:8", "const:4:8"]]
+ 00bf55f8 ["CALL", null, ["callee:00c5e150:8"]]
- 00bf555c bytes c9a20194
+ 00bf55f8 bytes d6a20194
- 00bf558c ["INT_ADD", "register:40f0:8", ["const:bf558c:8", "const:4:8"]]
- 00bf558c ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf5628 ["INT_ADD", "register:40f0:8", ["const:bf5628:8", "const:4:8"]]
+ 00bf5628 ["CALL", null, ["callee:00c5e120:8"]]
- 00bf558c bytes b1a20194
+ 00bf5628 bytes bea20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-664fb467ec468e03c4fcc6be069168b0"></a>

### [`00bf5650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5650.md) → [`00bf56ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf56ec.md) _ZNSt6__ndk14stoiERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`00bf817c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`00bf8218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.41% / 新版 92.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5814",
      "incomplete_value": true,
      "site": "00bf5814",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5778",
      "incomplete_value": true,
      "site": "00bf5778",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf581c",
      "incomplete_value": true,
      "site": "00bf581c",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5780",
      "incomplete_value": true,
      "site": "00bf5780",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf57c0",
      "incomplete_value": false,
      "site": "00bf57d0",
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
            "const:d72:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5724",
      "incomplete_value": false,
      "site": "00bf5734",
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
            "const:dc6:8"
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
      "00bf57c0",
      "PARAM",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5804",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5808",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf57c0",
      "PARAM",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5804",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5808",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5650.md#insn-00bf5734) · [`00bf56a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5650.md#insn-00bf56a4) · [`00bf56c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5650.md#insn-00bf56c0)
- 新版 [`00bf57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf56ec.md#insn-00bf57d0) · [`00bf5740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf56ec.md#insn-00bf5740) · [`00bf575c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf56ec.md#insn-00bf575c)

~~~diff
- 00bf5734 ["INT_ADD", "register:40f0:8", ["const:bf5734:8", "const:4:8"]]
- 00bf5734 ["CALL", null, ["callee:00481ec0:8"]]
+ 00bf57d0 ["INT_ADD", "register:40f0:8", ["const:bf57d0:8", "const:4:8"]]
+ 00bf57d0 ["CALL", null, ["callee:00481ec0:8"]]
- 00bf5734 bytes d331e297
+ 00bf57d0 bytes bc31e297
- 00bf56a4 ["INT_ADD", "register:40f0:8", ["const:bf56a4:8", "const:4:8"]]
- 00bf56a4 ["CALL", null, ["callee:00c58190:8"]]
+ 00bf5740 ["INT_ADD", "register:40f0:8", ["const:bf5740:8", "const:4:8"]]
+ 00bf5740 ["CALL", null, ["callee:00c58190:8"]]
- 00bf56a4 bytes 878a0194
+ 00bf5740 bytes 948a0194
- 00bf56c0 ["INT_ADD", "register:40f0:8", ["const:bf56c0:8", "const:4:8"]]
- 00bf56c0 ["CALL", null, ["callee:00c5e160:8"]]
+ 00bf575c ["INT_ADD", "register:40f0:8", ["const:bf575c:8", "const:4:8"]]
+ 00bf575c ["CALL", null, ["callee:00c5e160:8"]]
- 00bf56c0 bytes 74a20194
+ 00bf575c bytes 81a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af866772629bb92eb6cd28fd573390ad"></a>

### [`00bf57b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf57b4.md) → [`00bf5850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5850.md) _ZNSt6__ndk14stolERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`00bf817c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`00bf8218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf591c",
      "incomplete_value": false,
      "site": "00bf592c",
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
            "const:d72:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5880",
      "incomplete_value": false,
      "site": "00bf5890",
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
            "const:dc6:8"
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
      "00bf591c",
      "PARAM",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf591c",
      "PARAM",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf57b4.md#insn-00bf5890) · [`00bf5808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf57b4.md#insn-00bf5808) · [`00bf5824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf57b4.md#insn-00bf5824)
- 新版 [`00bf592c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5850.md#insn-00bf592c) · [`00bf58a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5850.md#insn-00bf58a4) · [`00bf58c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5850.md#insn-00bf58c0)

~~~diff
- 00bf5890 ["INT_ADD", "register:40f0:8", ["const:bf5890:8", "const:4:8"]]
- 00bf5890 ["CALL", null, ["callee:00481ec0:8"]]
+ 00bf592c ["INT_ADD", "register:40f0:8", ["const:bf592c:8", "const:4:8"]]
+ 00bf592c ["CALL", null, ["callee:00481ec0:8"]]
- 00bf5890 bytes 7c31e297
+ 00bf592c bytes 6531e297
- 00bf5808 ["INT_ADD", "register:40f0:8", ["const:bf5808:8", "const:4:8"]]
- 00bf5808 ["CALL", null, ["callee:00c58190:8"]]
+ 00bf58a4 ["INT_ADD", "register:40f0:8", ["const:bf58a4:8", "const:4:8"]]
+ 00bf58a4 ["CALL", null, ["callee:00c58190:8"]]
- 00bf5808 bytes 2e8a0194
+ 00bf58a4 bytes 3b8a0194
- 00bf5824 ["INT_ADD", "register:40f0:8", ["const:bf5824:8", "const:4:8"]]
- 00bf5824 ["CALL", null, ["callee:00c5e160:8"]]
+ 00bf58c0 ["INT_ADD", "register:40f0:8", ["const:bf58c0:8", "const:4:8"]]
+ 00bf58c0 ["CALL", null, ["callee:00c5e160:8"]]
- 00bf5824 bytes 1ba20194
+ 00bf58c0 bytes 28a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c29c554891c90b5186b9d92ab750526e"></a>

### [`00bf58d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf58d4.md) → [`00bf5970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5970.md) _ZNSt6__ndk15stoulERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5a74",
      "incomplete_value": true,
      "site": "00bf5a74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf59d8",
      "incomplete_value": true,
      "site": "00bf59d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
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
      "definition_site": "00bf5a78",
      "incomplete_value": true,
      "site": "00bf5a78",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf59dc",
      "incomplete_value": true,
      "site": "00bf59dc",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
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
      "definition_site": "00bf5ab4",
      "incomplete_value": true,
      "site": "00bf5ab4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5a18",
      "incomplete_value": true,
      "site": "00bf5a18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
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
      "00bf5a5c",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5a64",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5a9c",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5a5c",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5a64",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf5a9c",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf592c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf58d4.md#insn-00bf592c) · [`00bf5948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf58d4.md#insn-00bf5948) · [`00bf5984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf58d4.md#insn-00bf5984)
- 新版 [`00bf59c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5970.md#insn-00bf59c8) · [`00bf59e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5970.md#insn-00bf59e4) · [`00bf5a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5970.md#insn-00bf5a20)

~~~diff
- 00bf592c ["INT_ADD", "register:40f0:8", ["const:bf592c:8", "const:4:8"]]
- 00bf592c ["CALL", null, ["callee:00c58190:8"]]
+ 00bf59c8 ["INT_ADD", "register:40f0:8", ["const:bf59c8:8", "const:4:8"]]
+ 00bf59c8 ["CALL", null, ["callee:00c58190:8"]]
- 00bf592c bytes e5890194
+ 00bf59c8 bytes f2890194
- 00bf5948 ["INT_ADD", "register:40f0:8", ["const:bf5948:8", "const:4:8"]]
- 00bf5948 ["CALL", null, ["callee:00c5e170:8"]]
+ 00bf59e4 ["INT_ADD", "register:40f0:8", ["const:bf59e4:8", "const:4:8"]]
+ 00bf59e4 ["CALL", null, ["callee:00c5e170:8"]]
- 00bf5948 bytes d6a10194
+ 00bf59e4 bytes e3a10194
- 00bf5984 ["INT_ADD", "register:40f0:8", ["const:bf5984:8", "const:4:8"]]
- 00bf5984 ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf5a20 ["INT_ADD", "register:40f0:8", ["const:bf5a20:8", "const:4:8"]]
+ 00bf5a20 ["CALL", null, ["callee:00c5e120:8"]]
- 00bf5984 bytes b3a10194
+ 00bf5a20 bytes c0a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc1566ce1b2982c552352392fc2155cd"></a>

### [`00bf5a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5a50.md) → [`00bf5aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5aec.md) _ZNSt6__ndk15stollERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5bf0",
      "incomplete_value": true,
      "site": "00bf5bf0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5b54",
      "incomplete_value": true,
      "site": "00bf5b54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
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
      "definition_site": "00bf5bf4",
      "incomplete_value": true,
      "site": "00bf5bf4",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5b58",
      "incomplete_value": true,
      "site": "00bf5b58",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
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
      "definition_site": "00bf5c30",
      "incomplete_value": true,
      "site": "00bf5c30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5b94",
      "incomplete_value": true,
      "site": "00bf5b94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
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
      "00bf5bd8",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5be0",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5c18",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5bd8",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5be0",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf5c18",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5a50.md#insn-00bf5aa8) · [`00bf5ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5a50.md#insn-00bf5ac4) · [`00bf5b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5a50.md#insn-00bf5b00)
- 新版 [`00bf5b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5aec.md#insn-00bf5b44) · [`00bf5b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5aec.md#insn-00bf5b60) · [`00bf5b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5aec.md#insn-00bf5b9c)

~~~diff
- 00bf5aa8 ["INT_ADD", "register:40f0:8", ["const:bf5aa8:8", "const:4:8"]]
- 00bf5aa8 ["CALL", null, ["callee:00c58190:8"]]
+ 00bf5b44 ["INT_ADD", "register:40f0:8", ["const:bf5b44:8", "const:4:8"]]
+ 00bf5b44 ["CALL", null, ["callee:00c58190:8"]]
- 00bf5aa8 bytes 86890194
+ 00bf5b44 bytes 93890194
- 00bf5ac4 ["INT_ADD", "register:40f0:8", ["const:bf5ac4:8", "const:4:8"]]
- 00bf5ac4 ["CALL", null, ["callee:00c5e180:8"]]
+ 00bf5b60 ["INT_ADD", "register:40f0:8", ["const:bf5b60:8", "const:4:8"]]
+ 00bf5b60 ["CALL", null, ["callee:00c5e180:8"]]
- 00bf5ac4 bytes 7ba10194
+ 00bf5b60 bytes 88a10194
- 00bf5b00 ["INT_ADD", "register:40f0:8", ["const:bf5b00:8", "const:4:8"]]
- 00bf5b00 ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf5b9c ["INT_ADD", "register:40f0:8", ["const:bf5b9c:8", "const:4:8"]]
+ 00bf5b9c ["CALL", null, ["callee:00c5e120:8"]]
- 00bf5b00 bytes 54a10194
+ 00bf5b9c bytes 61a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3602b3a408d7e217f4c66d0e55ea0a3"></a>

### [`00bf5bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5bcc.md) → [`00bf5c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5c68.md) _ZNSt6__ndk16stoullERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5d70",
      "incomplete_value": true,
      "site": "00bf5d70",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5cd4",
      "incomplete_value": true,
      "site": "00bf5cd4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
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
      "definition_site": "00bf5d74",
      "incomplete_value": true,
      "site": "00bf5d74",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5cd8",
      "incomplete_value": true,
      "site": "00bf5cd8",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
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
      "definition_site": "00bf5db0",
      "incomplete_value": true,
      "site": "00bf5db0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5d14",
      "incomplete_value": true,
      "site": "00bf5d14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf5d58",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5d60",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5d98",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5d58",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5d60",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf5d98",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5bcc.md#insn-00bf5c28) · [`00bf5c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5bcc.md#insn-00bf5c44) · [`00bf5c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5bcc.md#insn-00bf5c80)
- 新版 [`00bf5cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5c68.md#insn-00bf5cc4) · [`00bf5ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5c68.md#insn-00bf5ce0) · [`00bf5d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5c68.md#insn-00bf5d1c)

~~~diff
- 00bf5c28 ["INT_ADD", "register:40f0:8", ["const:bf5c28:8", "const:4:8"]]
- 00bf5c28 ["CALL", null, ["callee:00c58190:8"]]
+ 00bf5cc4 ["INT_ADD", "register:40f0:8", ["const:bf5cc4:8", "const:4:8"]]
+ 00bf5cc4 ["CALL", null, ["callee:00c58190:8"]]
- 00bf5c28 bytes 26890194
+ 00bf5cc4 bytes 33890194
- 00bf5c44 ["INT_ADD", "register:40f0:8", ["const:bf5c44:8", "const:4:8"]]
- 00bf5c44 ["CALL", null, ["callee:00c5e190:8"]]
+ 00bf5ce0 ["INT_ADD", "register:40f0:8", ["const:bf5ce0:8", "const:4:8"]]
+ 00bf5ce0 ["CALL", null, ["callee:00c5e190:8"]]
- 00bf5c44 bytes 1fa10194
+ 00bf5ce0 bytes 2ca10194
- 00bf5c80 ["INT_ADD", "register:40f0:8", ["const:bf5c80:8", "const:4:8"]]
- 00bf5c80 ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf5d1c ["INT_ADD", "register:40f0:8", ["const:bf5d1c:8", "const:4:8"]]
+ 00bf5d1c ["CALL", null, ["callee:00c5e120:8"]]
- 00bf5c80 bytes f4a00194
+ 00bf5d1c bytes 01a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5652b4db453fb7dff130a4d253a47698"></a>

### [`00bf5d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5d4c.md) → [`00bf5de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5de8.md) _ZNSt6__ndk14stofERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5ecc",
      "incomplete_value": true,
      "site": "00bf5ecc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5e30",
      "incomplete_value": true,
      "site": "00bf5e30",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5ed4",
      "incomplete_value": true,
      "site": "00bf5ed4",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5e38",
      "incomplete_value": true,
      "site": "00bf5e38",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
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
      "definition_site": "00bf5f04",
      "incomplete_value": true,
      "site": "00bf5f04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5e68",
      "incomplete_value": true,
      "site": "00bf5e68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf5ebc",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5ec0",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5ef4",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5ebc",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf5ec0",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf5ef4",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5d4c.md#insn-00bf5d9c) · [`00bf5db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5d4c.md#insn-00bf5db4) · [`00bf5de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5d4c.md#insn-00bf5de8)
- 新版 [`00bf5e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5de8.md#insn-00bf5e38) · [`00bf5e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5de8.md#insn-00bf5e50) · [`00bf5e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5de8.md#insn-00bf5e84)

~~~diff
- 00bf5d9c ["INT_ADD", "register:40f0:8", ["const:bf5d9c:8", "const:4:8"]]
- 00bf5d9c ["CALL", null, ["callee:00c58190:8"]]
+ 00bf5e38 ["INT_ADD", "register:40f0:8", ["const:bf5e38:8", "const:4:8"]]
+ 00bf5e38 ["CALL", null, ["callee:00c58190:8"]]
- 00bf5d9c bytes c9880194
+ 00bf5e38 bytes d6880194
- 00bf5db4 ["INT_ADD", "register:40f0:8", ["const:bf5db4:8", "const:4:8"]]
- 00bf5db4 ["CALL", null, ["callee:00c5e1a0:8"]]
+ 00bf5e50 ["INT_ADD", "register:40f0:8", ["const:bf5e50:8", "const:4:8"]]
+ 00bf5e50 ["CALL", null, ["callee:00c5e1a0:8"]]
- 00bf5db4 bytes c7a00194
+ 00bf5e50 bytes d4a00194
- 00bf5de8 ["INT_ADD", "register:40f0:8", ["const:bf5de8:8", "const:4:8"]]
- 00bf5de8 ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf5e84 ["INT_ADD", "register:40f0:8", ["const:bf5e84:8", "const:4:8"]]
+ 00bf5e84 ["CALL", null, ["callee:00c5e120:8"]]
- 00bf5de8 bytes 9aa00194
+ 00bf5e84 bytes a7a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac50470024241445550f1bd4a024408f"></a>

### [`00bf5ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5ea4.md) → [`00bf5f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5f40.md) _ZNSt6__ndk14stodERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf6024",
      "incomplete_value": true,
      "site": "00bf6024",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5f88",
      "incomplete_value": true,
      "site": "00bf5f88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf602c",
      "incomplete_value": true,
      "site": "00bf602c",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5f90",
      "incomplete_value": true,
      "site": "00bf5f90",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
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
      "definition_site": "00bf605c",
      "incomplete_value": true,
      "site": "00bf605c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5fc0",
      "incomplete_value": true,
      "site": "00bf5fc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf6014",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf6018",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf604c",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf6014",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf6018",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf604c",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5ea4.md#insn-00bf5ef4) · [`00bf5f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5ea4.md#insn-00bf5f0c) · [`00bf5f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5ea4.md#insn-00bf5f40)
- 新版 [`00bf5f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5f40.md#insn-00bf5f90) · [`00bf5fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5f40.md#insn-00bf5fa8) · [`00bf5fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5f40.md#insn-00bf5fdc)

~~~diff
- 00bf5ef4 ["INT_ADD", "register:40f0:8", ["const:bf5ef4:8", "const:4:8"]]
- 00bf5ef4 ["CALL", null, ["callee:00c58190:8"]]
+ 00bf5f90 ["INT_ADD", "register:40f0:8", ["const:bf5f90:8", "const:4:8"]]
+ 00bf5f90 ["CALL", null, ["callee:00c58190:8"]]
- 00bf5ef4 bytes 73880194
+ 00bf5f90 bytes 80880194
- 00bf5f0c ["INT_ADD", "register:40f0:8", ["const:bf5f0c:8", "const:4:8"]]
- 00bf5f0c ["CALL", null, ["callee:00c5e1b0:8"]]
+ 00bf5fa8 ["INT_ADD", "register:40f0:8", ["const:bf5fa8:8", "const:4:8"]]
+ 00bf5fa8 ["CALL", null, ["callee:00c5e1b0:8"]]
- 00bf5f0c bytes 75a00194
+ 00bf5fa8 bytes 82a00194
- 00bf5f40 ["INT_ADD", "register:40f0:8", ["const:bf5f40:8", "const:4:8"]]
- 00bf5f40 ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf5fdc ["INT_ADD", "register:40f0:8", ["const:bf5fdc:8", "const:4:8"]]
+ 00bf5fdc ["CALL", null, ["callee:00c5e120:8"]]
- 00bf5f40 bytes 44a00194
+ 00bf5fdc bytes 51a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c03f1ebf535248f51f8a4353d0213b61"></a>

### [`00bf5ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5ffc.md) → [`00bf6098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6098.md) _ZNSt6__ndk15stoldERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf618c",
      "incomplete_value": true,
      "site": "00bf618c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf60f0",
      "incomplete_value": true,
      "site": "00bf60f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
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
      "definition_site": "00bf6190",
      "incomplete_value": true,
      "site": "00bf6190",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf60f4",
      "incomplete_value": true,
      "site": "00bf60f4",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
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
      "definition_site": "00bf61cc",
      "incomplete_value": true,
      "site": "00bf61cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf6130",
      "incomplete_value": true,
      "site": "00bf6130",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50a:8"
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
      "00bf6174",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf617c",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf61b4",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf6174",
      "READ",
      [
        "storage",
        "002b9d72",
        null,
        "string"
      ]
    ],
    [
      "00bf617c",
      "READ",
      [
        "storage",
        "002b9d78",
        null,
        "string"
      ]
    ],
    [
      "00bf61b4",
      "READ",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf604c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5ffc.md#insn-00bf604c) · [`00bf6064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5ffc.md#insn-00bf6064) · [`00bf60a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5ffc.md#insn-00bf60a0)
- 新版 [`00bf60e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6098.md#insn-00bf60e8) · [`00bf6100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6098.md#insn-00bf6100) · [`00bf613c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6098.md#insn-00bf613c)

~~~diff
- 00bf604c ["INT_ADD", "register:40f0:8", ["const:bf604c:8", "const:4:8"]]
- 00bf604c ["CALL", null, ["callee:00c58190:8"]]
+ 00bf60e8 ["INT_ADD", "register:40f0:8", ["const:bf60e8:8", "const:4:8"]]
+ 00bf60e8 ["CALL", null, ["callee:00c58190:8"]]
- 00bf604c bytes 1d880194
+ 00bf60e8 bytes 2a880194
- 00bf6064 ["INT_ADD", "register:40f0:8", ["const:bf6064:8", "const:4:8"]]
- 00bf6064 ["CALL", null, ["callee:00c5e1c0:8"]]
+ 00bf6100 ["INT_ADD", "register:40f0:8", ["const:bf6100:8", "const:4:8"]]
+ 00bf6100 ["CALL", null, ["callee:00c5e1c0:8"]]
- 00bf6064 bytes 23a00194
+ 00bf6100 bytes 30a00194
- 00bf60a0 ["INT_ADD", "register:40f0:8", ["const:bf60a0:8", "const:4:8"]]
- 00bf60a0 ["CALL", null, ["callee:00c5e120:8"]]
+ 00bf613c ["INT_ADD", "register:40f0:8", ["const:bf613c:8", "const:4:8"]]
+ 00bf613c ["CALL", null, ["callee:00c5e120:8"]]
- 00bf60a0 bytes ec9f0194
+ 00bf613c bytes f99f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e774020ee1210a2c3b999347b04beae9"></a>

### [`00bf7db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf7/00bf7db4.md) → [`00bf7e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7e50.md) _ZNSt6__ndk110to_wstringEf

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a890.md) [`00c5e110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e110.md) [`00c5e120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e120.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a960.md) [`00c5e1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1e0.md) [`00c5e1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf7e8c",
      "incomplete_value": true,
      "site": "00bf7e94",
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
                "const:2c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf7df0",
      "incomplete_value": true,
      "site": "00bf7df8",
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf7e8c",
      "READ",
      [
        "storage",
        "002c3280",
        null,
        null
      ]
    ],
    [
      "00bf7ef4",
      "PARAM",
      [
        "storage",
        "003104f4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf7e8c",
      "READ",
      [
        "storage",
        "002c32c0",
        null,
        null
      ]
    ],
    [
      "00bf7ef4",
      "PARAM",
      [
        "storage",
        "00310534",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf7de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf7/00bf7db4.md#insn-00bf7de0) · [`00bf7df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf7/00bf7db4.md#insn-00bf7df0) · [`00bf7e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf7/00bf7db4.md#insn-00bf7e18)
- 新版 [`00bf7e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7e50.md#insn-00bf7e7c) · [`00bf7e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7e50.md#insn-00bf7e8c) · [`00bf7eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7e50.md#insn-00bf7eb4)

~~~diff
- 00bf7de0 ["INT_ADD", "register:40f0:8", ["const:bf7de0:8", "const:4:8"]]
- 00bf7de0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf7e7c ["INT_ADD", "register:40f0:8", ["const:bf7e7c:8", "const:4:8"]]
+ 00bf7e7c ["CALL", null, ["callee:00c57f60:8"]]
- 00bf7de0 bytes 2c800194
+ 00bf7e7c bytes 39800194
- 00bf7df0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
- 00bf7df0 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00bf7df0 ["COPY", "register:5030:8", ["const:0:8"]]
- 00bf7df0 ["COPY", "register:5038:8", ["const:0:8"]]
+ 00bf7e8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c0:8"]]
+ 00bf7e8c ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bf7e8c ["COPY", "register:5030:8", ["const:0:8"]]
+ 00bf7e8c ["COPY", "register:5038:8", ["const:0:8"]]
- 00bf7df0 bytes 01a1c03d
+ 00bf7e8c bytes 01b1c03d
- 00bf7e18 ["INT_ADD", "register:40f0:8", ["const:bf7e18:8", "const:4:8"]]
- 00bf7e18 ["CALL", null, ["callee:00c5a960:8"]]
+ 00bf7eb4 ["INT_ADD", "register:40f0:8", ["const:bf7eb4:8", "const:4:8"]]
+ 00bf7eb4 ["CALL", null, ["callee:00c5a960:8"]]
- 00bf7e18 bytes 9e8a0194
+ 00bf7eb4 bytes ab8a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9c4c913c65ec5f400fcdb047ee00e5c"></a>

### [`00bf7efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf7/00bf7efc.md) → [`00bf7f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7f98.md) _ZNSt6__ndk110to_wstringEd

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a890.md) [`00c5e110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e110.md) [`00c5e120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e120.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a960.md) [`00c5e1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1e0.md) [`00c5e1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1f0.md)

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
      "definition_site": "00bf7fd4",
      "incomplete_value": true,
      "site": "00bf7fdc",
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
                "const:2c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf7f38",
      "incomplete_value": true,
      "site": "00bf7f40",
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf7fd4",
      "READ",
      [
        "storage",
        "002c3280",
        null,
        null
      ]
    ],
    [
      "00bf8038",
      "PARAM",
      [
        "storage",
        "003104f4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf7fd4",
      "READ",
      [
        "storage",
        "002c32c0",
        null,
        null
      ]
    ],
    [
      "00bf8038",
      "PARAM",
      [
        "storage",
        "00310534",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf7f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf7/00bf7efc.md#insn-00bf7f28) · [`00bf7f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf7/00bf7efc.md#insn-00bf7f38) · [`00bf7f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf7/00bf7efc.md#insn-00bf7f60)
- 新版 [`00bf7fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7f98.md#insn-00bf7fc4) · [`00bf7fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7f98.md#insn-00bf7fd4) · [`00bf7ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf7/00bf7f98.md#insn-00bf7ffc)

~~~diff
- 00bf7f28 ["INT_ADD", "register:40f0:8", ["const:bf7f28:8", "const:4:8"]]
- 00bf7f28 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf7fc4 ["INT_ADD", "register:40f0:8", ["const:bf7fc4:8", "const:4:8"]]
+ 00bf7fc4 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf7f28 bytes da7f0194
+ 00bf7fc4 bytes e77f0194
- 00bf7f38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
- 00bf7f38 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00bf7f38 ["COPY", "register:5030:8", ["const:0:8"]]
- 00bf7f38 ["COPY", "register:5038:8", ["const:0:8"]]
+ 00bf7fd4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c0:8"]]
+ 00bf7fd4 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bf7fd4 ["COPY", "register:5030:8", ["const:0:8"]]
+ 00bf7fd4 ["COPY", "register:5038:8", ["const:0:8"]]
- 00bf7f38 bytes 01a1c03d
+ 00bf7fd4 bytes 01b1c03d
- 00bf7f60 ["INT_ADD", "register:40f0:8", ["const:bf7f60:8", "const:4:8"]]
- 00bf7f60 ["CALL", null, ["callee:00c5a960:8"]]
+ 00bf7ffc ["INT_ADD", "register:40f0:8", ["const:bf7ffc:8", "const:4:8"]]
+ 00bf7ffc ["CALL", null, ["callee:00c5a960:8"]]
- 00bf7f60 bytes 4c8a0194
+ 00bf7ffc bytes 598a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2db44827c6f596ed57003de4cdea4ec7"></a>

### [`00bf8040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8040.md) → [`00bf80dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf80dc.md) _ZNSt6__ndk110to_wstringEe

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a890.md) [`00c5e110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e110.md) [`00c5e120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e120.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a960.md) [`00c5e1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1e0.md) [`00c5e1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf8114",
      "incomplete_value": true,
      "site": "00bf811c",
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
                "const:2c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8078",
      "incomplete_value": true,
      "site": "00bf8080",
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf8114",
      "READ",
      [
        "storage",
        "002c3280",
        null,
        null
      ]
    ],
    [
      "00bf8178",
      "PARAM",
      [
        "storage",
        "00310564",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf8114",
      "READ",
      [
        "storage",
        "002c32c0",
        null,
        null
      ]
    ],
    [
      "00bf8178",
      "PARAM",
      [
        "storage",
        "003105a4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf8068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8040.md#insn-00bf8068) · [`00bf8078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8040.md#insn-00bf8078) · [`00bf80a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8040.md#insn-00bf80a0)
- 新版 [`00bf8104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf80dc.md#insn-00bf8104) · [`00bf8114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf80dc.md#insn-00bf8114) · [`00bf813c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf80dc.md#insn-00bf813c)

~~~diff
- 00bf8068 ["INT_ADD", "register:40f0:8", ["const:bf8068:8", "const:4:8"]]
- 00bf8068 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf8104 ["INT_ADD", "register:40f0:8", ["const:bf8104:8", "const:4:8"]]
+ 00bf8104 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf8068 bytes 8a7f0194
+ 00bf8104 bytes 977f0194
- 00bf8078 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
- 00bf8078 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00bf8078 ["COPY", "register:5030:8", ["const:0:8"]]
- 00bf8078 ["COPY", "register:5038:8", ["const:0:8"]]
+ 00bf8114 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c0:8"]]
+ 00bf8114 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bf8114 ["COPY", "register:5030:8", ["const:0:8"]]
+ 00bf8114 ["COPY", "register:5038:8", ["const:0:8"]]
- 00bf8078 bytes 01a1c03d
+ 00bf8114 bytes 01b1c03d
- 00bf80a0 ["INT_ADD", "register:40f0:8", ["const:bf80a0:8", "const:4:8"]]
- 00bf80a0 ["CALL", null, ["callee:00c5a960:8"]]
+ 00bf813c ["INT_ADD", "register:40f0:8", ["const:bf813c:8", "const:4:8"]]
+ 00bf813c ["CALL", null, ["callee:00c5a960:8"]]
- 00bf80a0 bytes fc890194
+ 00bf813c bytes 098a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-775051cdfc784a7ae03f24d75f0932fc"></a>

### [`00bf817c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md) → [`00bf8218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md) FUN_00bf8218

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00bf4ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4ba0.md) [`00bf4cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4cfc.md) [`00bf5650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5650.md) [`00bf57b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf57b4.md) · 呼出先 4件 [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)
- 新版 呼出元 4件 [`00bf4c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4c3c.md) [`00bf4d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4d98.md) [`00bf56ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf56ec.md) [`00bf5850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5850.md) · 呼出先 4件 [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c5e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf8230",
      "incomplete_value": false,
      "site": "00bf823c",
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
            "const:4ae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8194",
      "incomplete_value": false,
      "site": "00bf81a0",
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
            "const:50a:8"
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
      "00bf8230",
      "PARAM",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf8230",
      "PARAM",
      [
        "storage",
        "002a74ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf81a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md#insn-00bf81a0) · [`00bf8194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md#insn-00bf8194) · [`00bf81b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md#insn-00bf81b4)
- 新版 [`00bf823c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md#insn-00bf823c) · [`00bf8230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md#insn-00bf8230) · [`00bf8250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8218.md#insn-00bf8250)

~~~diff
- 00bf81a0 ["INT_ADD", "register:40f0:8", ["const:bf81a0:8", "const:4:8"]]
- 00bf81a0 ["CALL", null, ["callee:00481ec0:8"]]
+ 00bf823c ["INT_ADD", "register:40f0:8", ["const:bf823c:8", "const:4:8"]]
+ 00bf823c ["CALL", null, ["callee:00481ec0:8"]]
- 00bf81a0 bytes 3827e297
+ 00bf823c bytes 2127e297
- 00bf8194 ["COPY", "tmp:0:8", ["const:50a:8"]]
- 00bf8194 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bf8194 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bf8194 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bf8230 ["COPY", "tmp:0:8", ["const:4ae:8"]]
+ 00bf8230 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf8230 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf8230 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bf8194 bytes 21281491
+ 00bf8230 bytes 21b81291
- 00bf81b4 ["INT_ADD", "register:40f0:8", ["const:bf81b4:8", "const:4:8"]]
- 00bf81b4 ["CALL", null, ["callee:00bf8268:8"]]
+ 00bf8250 ["INT_ADD", "register:40f0:8", ["const:bf8250:8", "const:4:8"]]
+ 00bf8250 ["CALL", null, ["callee:00bf8268:8"]]
- 00bf81b4 bytes 06000094
+ 00bf8250 bytes 06000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7da8b8c817877373966848d0e6fc698"></a>

### [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) → [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) FUN_00bf8268

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 13件 [`00bf4e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4e14.md) [`00bf4f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4f80.md) [`00bf50ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf50ec.md) [`00bf525c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf525c.md) [`00bf53a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf53a4.md) · 呼出先 4件 [`00bf8220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8220.md) [`00c37ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ccc.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 13件 [`00bf4eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4eb0.md) [`00bf501c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf501c.md) [`00bf5188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5188.md) [`00bf52f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf52f8.md) [`00bf5440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5440.md) · 呼出先 4件 [`00bf82bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf82bc.md) [`00c37d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d68.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf829c",
      "incomplete_value": true,
      "site": "00bf82a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8200",
      "incomplete_value": true,
      "site": "00bf8208",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab8:8"
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
      "definition_site": "00bf82a0",
      "incomplete_value": true,
      "site": "00bf82a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8204",
      "incomplete_value": true,
      "site": "00bf8208",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ac0:8"
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
      "00bf829c",
      "READ",
      [
        "storage",
        "00c9bab8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf829c",
      "PARAM",
      [
        "storage",
        "00c96798",
        "_ZTISt16invalid_argument",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf82a0",
      "READ",
      [
        "storage",
        "00c9bac0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf829c",
      "READ",
      [
        "storage",
        "00c9bb88",
        null,
        "pointer"
      ]
    ],
    [
      "00bf829c",
      "PARAM",
      [
        "storage",
        "00c96868",
        "_ZTISt16invalid_argument",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf82a0",
      "READ",
      [
        "storage",
        "00c9bb90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf8208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md#insn-00bf8208) · [`00bf81e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md#insn-00bf81e4) · [`00bf81f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md#insn-00bf81f0)
- 新版 [`00bf82a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md#insn-00bf82a4) · [`00bf8280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md#insn-00bf8280) · [`00bf828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md#insn-00bf828c)

~~~diff
- 00bf8208 ["INT_ADD", "register:40f0:8", ["const:bf8208:8", "const:4:8"]]
- 00bf8208 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf82a4 ["INT_ADD", "register:40f0:8", ["const:bf82a4:8", "const:4:8"]]
+ 00bf82a4 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf8208 bytes 427f0194
+ 00bf82a4 bytes 4f7f0194
- 00bf81e4 ["INT_ADD", "register:40f0:8", ["const:bf81e4:8", "const:4:8"]]
- 00bf81e4 ["CALL", null, ["callee:00c57fc0:8"]]
+ 00bf8280 ["INT_ADD", "register:40f0:8", ["const:bf8280:8", "const:4:8"]]
+ 00bf8280 ["CALL", null, ["callee:00c57fc0:8"]]
- 00bf81e4 bytes 437f0194
+ 00bf8280 bytes 507f0194
- 00bf81f0 ["INT_ADD", "register:40f0:8", ["const:bf81f0:8", "const:4:8"]]
- 00bf81f0 ["CALL", null, ["callee:00bf82bc:8"]]
+ 00bf828c ["INT_ADD", "register:40f0:8", ["const:bf828c:8", "const:4:8"]]
+ 00bf828c ["CALL", null, ["callee:00bf82bc:8"]]
- 00bf81f0 bytes 0c000094
+ 00bf828c bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b18e062374317525d47df021d9f56686"></a>

### [`00bf8610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8610.md) → [`00bf86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf86ac.md) FUN_00bf86ac

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00bf8744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8744.md) [`00bf880c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf880c.md) [`00bfae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfae78.md) · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md)
- 新版 呼出元 3件 [`00bf87e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf87e0.md) [`00bf88a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf88a8.md) [`00bfaf14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf14.md) · 呼出先 8件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf871c",
      "incomplete_value": false,
      "site": "00bf8730",
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
            "const:e9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8680",
      "incomplete_value": false,
      "site": "00bf8694",
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
            "const:e5b:8"
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
      "00bf8710",
      "READ",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf871c",
      "PARAM",
      [
        "storage",
        "002b7e5b",
        null,
        "string"
      ]
    ],
    [
      "00bf8734",
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
      "00bf8710",
      "READ",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf871c",
      "PARAM",
      [
        "storage",
        "002b7e9b",
        null,
        "string"
      ]
    ],
    [
      "00bf8734",
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

- 旧版 [`00bf8694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8610.md#insn-00bf8694) · [`00bf8730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8610.md#insn-00bf8730) · [`00bf8634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8610.md#insn-00bf8634)
- 新版 [`00bf8730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf86ac.md#insn-00bf8730) · [`00bf87cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf86ac.md#insn-00bf87cc) · [`00bf86d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf86ac.md#insn-00bf86d0)

~~~diff
- 00bf8694 ["INT_ADD", "register:40f0:8", ["const:bf8694:8", "const:4:8"]]
- 00bf8694 ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00bf8730 ["INT_ADD", "register:40f0:8", ["const:bf8730:8", "const:4:8"]]
+ 00bf8730 ["CALL", null, ["callee:00c5e1d0:8"]]
- 00bf8694 bytes 9b960194
+ 00bf8730 bytes a8960194
- 00bf8730 ["INT_ADD", "register:40f0:8", ["const:bf8730:8", "const:4:8"]]
- 00bf8730 ["CALL", null, ["callee:00c5b210:8"]]
+ 00bf87cc ["INT_ADD", "register:40f0:8", ["const:bf87cc:8", "const:4:8"]]
+ 00bf87cc ["CALL", null, ["callee:00c5b210:8"]]
- 00bf8730 bytes 848a0194
+ 00bf87cc bytes 918a0194
- 00bf8634 ["INT_ADD", "register:40f0:8", ["const:bf8634:8", "const:4:8"]]
- 00bf8634 ["CALL", null, ["callee:00c58190:8"]]
+ 00bf86d0 ["INT_ADD", "register:40f0:8", ["const:bf86d0:8", "const:4:8"]]
+ 00bf86d0 ["CALL", null, ["callee:00c58190:8"]]
- 00bf8634 bytes a37e0194
+ 00bf86d0 bytes b07e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fd404eab14b0d81d2a5ab9f16204129"></a>

### [`00bf87ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf87ac.md) → [`00bf8848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8848.md) _ZNSt6__ndk116generic_categoryEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf887c",
      "incomplete_value": false,
      "site": "00bf8880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf87e0",
      "incomplete_value": false,
      "site": "00bf87e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "definition_site": "00bf888c",
      "incomplete_value": false,
      "site": "00bf8890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf87f0",
      "incomplete_value": false,
      "site": "00bf87f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:360:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf8868",
      "incomplete_value": false,
      "site": "00bf8874",
      "value": [
        "leaf",
        "const:ca48b8:8"
      ]
    },
    "old": {
      "definition_site": "00bf87cc",
      "incomplete_value": false,
      "site": "00bf87d8",
      "value": [
        "leaf",
        "const:ca47e8:8"
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
      "00bf885c",
      "READ",
      [
        "storage",
        "01127360",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf8868",
      "DATA",
      [
        "storage",
        "00ca47e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf887c",
      "PARAM",
      [
        "storage",
        "01127360",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bf885c",
      "READ",
      [
        "storage",
        "01127460",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf8868",
      "DATA",
      [
        "storage",
        "00ca48b8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf887c",
      "PARAM",
      [
        "storage",
        "01127460",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf87e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf87ac.md#insn-00bf87e4) · [`00bf87f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf87ac.md#insn-00bf87f4) · [`00bf87bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf87ac.md#insn-00bf87bc)
- 新版 [`00bf8880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8848.md#insn-00bf8880) · [`00bf8890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8848.md#insn-00bf8890) · [`00bf8858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8848.md#insn-00bf8858)

~~~diff
- 00bf87e4 ["INT_ADD", "register:40f0:8", ["const:bf87e4:8", "const:4:8"]]
- 00bf87e4 ["CALL", null, ["callee:00c57f20:8"]]
+ 00bf8880 ["INT_ADD", "register:40f0:8", ["const:bf8880:8", "const:4:8"]]
+ 00bf8880 ["CALL", null, ["callee:00c57f20:8"]]
- 00bf87e4 bytes 9b7d0194
+ 00bf8880 bytes a87d0194
- 00bf87f4 ["INT_ADD", "register:40f0:8", ["const:bf87f4:8", "const:4:8"]]
- 00bf87f4 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf8890 ["INT_ADD", "register:40f0:8", ["const:bf8890:8", "const:4:8"]]
+ 00bf8890 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf87f4 bytes 9f7d0194
+ 00bf8890 bytes ac7d0194
- 00bf87bc ["COPY", "tmp:0:8", ["const:360:8"]]
- 00bf87bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bf87bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bf87bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bf8858 ["COPY", "tmp:0:8", ["const:460:8"]]
+ 00bf8858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bf8858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bf8858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bf87bc bytes 08810d91
+ 00bf8858 bytes 08811191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50fed357b5a228a9c59898b725df16e5"></a>

### [`00bf8894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8894.md) → [`00bf8930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8930.md) _ZNSt6__ndk115system_categoryEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf8964",
      "incomplete_value": false,
      "site": "00bf8968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf88c8",
      "incomplete_value": false,
      "site": "00bf88cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:368:8"
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
      "definition_site": "00bf8974",
      "incomplete_value": false,
      "site": "00bf8978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf88d8",
      "incomplete_value": false,
      "site": "00bf88dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf8950",
      "incomplete_value": false,
      "site": "00bf895c",
      "value": [
        "leaf",
        "const:ca48c0:8"
      ]
    },
    "old": {
      "definition_site": "00bf88b4",
      "incomplete_value": false,
      "site": "00bf88c0",
      "value": [
        "leaf",
        "const:ca47f0:8"
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
      "00bf8944",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf8950",
      "DATA",
      [
        "storage",
        "00ca47f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8964",
      "PARAM",
      [
        "storage",
        "01127368",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bf8944",
      "READ",
      [
        "storage",
        "01127468",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf8950",
      "DATA",
      [
        "storage",
        "00ca48c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8964",
      "PARAM",
      [
        "storage",
        "01127468",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf88cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8894.md#insn-00bf88cc) · [`00bf88dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8894.md#insn-00bf88dc) · [`00bf88a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8894.md#insn-00bf88a4)
- 新版 [`00bf8968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8930.md#insn-00bf8968) · [`00bf8978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8930.md#insn-00bf8978) · [`00bf8940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8930.md#insn-00bf8940)

~~~diff
- 00bf88cc ["INT_ADD", "register:40f0:8", ["const:bf88cc:8", "const:4:8"]]
- 00bf88cc ["CALL", null, ["callee:00c57f20:8"]]
+ 00bf8968 ["INT_ADD", "register:40f0:8", ["const:bf8968:8", "const:4:8"]]
+ 00bf8968 ["CALL", null, ["callee:00c57f20:8"]]
- 00bf88cc bytes 617d0194
+ 00bf8968 bytes 6e7d0194
- 00bf88dc ["INT_ADD", "register:40f0:8", ["const:bf88dc:8", "const:4:8"]]
- 00bf88dc ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf8978 ["INT_ADD", "register:40f0:8", ["const:bf8978:8", "const:4:8"]]
+ 00bf8978 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf88dc bytes 657d0194
+ 00bf8978 bytes 727d0194
- 00bf88a4 ["COPY", "tmp:0:8", ["const:368:8"]]
- 00bf88a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bf88a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bf88a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bf8940 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 00bf8940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bf8940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bf8940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bf88a4 bytes 08a10d91
+ 00bf8940 bytes 08a11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-404242fec73f8aa0f16a82f2aa22a32b"></a>

### [`00bf8a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8a14.md) → [`00bf8ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8ab0.md) FUN_00bf8ab0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00bf891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf891c.md) [`00bf8ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8ae8.md) [`00bf8cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8cfc.md) [`00bf8e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8e08.md) · 呼出先 3件 [`007dcf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf1c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 4件 [`00bf89b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf89b8.md) [`00bf8b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8b84.md) [`00bf8d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8d98.md) [`00bf8ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8ea4.md) · 呼出先 3件 [`007dcf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dc/007dcf74.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf8af8",
      "incomplete_value": false,
      "site": "00bf8b00",
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
            "const:71a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8a5c",
      "incomplete_value": false,
      "site": "00bf8a64",
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
            "const:76e:8"
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
      "00bf8af8",
      "PARAM",
      [
        "storage",
        "002bd76e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf8af8",
      "PARAM",
      [
        "storage",
        "002bd71a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf8a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8a14.md#insn-00bf8a64) · [`00bf8a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8a14.md#insn-00bf8a5c) · [`00bf8a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8a14.md#insn-00bf8a7c)
- 新版 [`00bf8b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8ab0.md#insn-00bf8b00) · [`00bf8af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8ab0.md#insn-00bf8af8) · [`00bf8b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8ab0.md#insn-00bf8b18)

~~~diff
- 00bf8a64 ["INT_ADD", "register:40f0:8", ["const:bf8a64:8", "const:4:8"]]
- 00bf8a64 ["CALL", null, ["callee:00c58040:8"]]
+ 00bf8b00 ["INT_ADD", "register:40f0:8", ["const:bf8b00:8", "const:4:8"]]
+ 00bf8b00 ["CALL", null, ["callee:00c58040:8"]]
- 00bf8a64 bytes 437d0194
+ 00bf8b00 bytes 507d0194
- 00bf8a5c ["COPY", "tmp:0:8", ["const:76e:8"]]
- 00bf8a5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bf8a5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bf8a5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bf8af8 ["COPY", "tmp:0:8", ["const:71a:8"]]
+ 00bf8af8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf8af8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf8af8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bf8a5c bytes 21b81d91
+ 00bf8af8 bytes 21681c91
- 00bf8a7c ["COPY", "register:0:8", ["register:4048:8"]]
- 00bf8a7c ["INT_ADD", "register:40f0:8", ["const:bf8a7c:8", "const:4:8"]]
- 00bf8a7c ["CALLIND", null, ["register:0:8"]]
+ 00bf8b18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bf8b18 ["INT_ADD", "register:40f0:8", ["const:bf8b18:8", "const:4:8"]]
+ 00bf8b18 ["CALLIND", null, ["register:0:8"]]
- 00bf8a7c bytes 20013fd6
+ 00bf8b18 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9fc976fc33d150e80ca1d14335ed893"></a>

### [`00bf9088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9088.md) → [`00bf9124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9124.md) FUN_00bf9124

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bf9068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9068.md) · 呼出先 4件 [`00bf9034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9034.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5e1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1b0.md)
- 新版 呼出元 1件 [`00bf9104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9104.md) · 呼出先 4件 [`00bf90d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf90d0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5e280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e280.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf916c",
      "incomplete_value": true,
      "site": "00bf9174",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf90d0",
      "incomplete_value": true,
      "site": "00bf90d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae0:8"
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
      "definition_site": "00bf9170",
      "incomplete_value": true,
      "site": "00bf9174",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf90d4",
      "incomplete_value": true,
      "site": "00bf90d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad8:8"
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
      "00bf916c",
      "READ",
      [
        "storage",
        "00c9bae0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf916c",
      "PARAM",
      [
        "storage",
        "00c92ba0",
        "_ZTINSt6__ndk112system_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf9170",
      "READ",
      [
        "storage",
        "00c9bad8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf916c",
      "READ",
      [
        "storage",
        "00c9bbb0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf916c",
      "PARAM",
      [
        "storage",
        "00c92c70",
        "_ZTINSt6__ndk112system_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf9170",
      "READ",
      [
        "storage",
        "00c9bba8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf90d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9088.md#insn-00bf90d8) · [`00bf90ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9088.md#insn-00bf90ac) · [`00bf90c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9088.md#insn-00bf90c0)
- 新版 [`00bf9174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9124.md#insn-00bf9174) · [`00bf9148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9124.md#insn-00bf9148) · [`00bf915c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9124.md#insn-00bf915c)

~~~diff
- 00bf90d8 ["INT_ADD", "register:40f0:8", ["const:bf90d8:8", "const:4:8"]]
- 00bf90d8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf9174 ["INT_ADD", "register:40f0:8", ["const:bf9174:8", "const:4:8"]]
+ 00bf9174 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf90d8 bytes 8e7b0194
+ 00bf9174 bytes 9b7b0194
- 00bf90ac ["INT_ADD", "register:40f0:8", ["const:bf90ac:8", "const:4:8"]]
- 00bf90ac ["CALL", null, ["callee:00c57fc0:8"]]
+ 00bf9148 ["INT_ADD", "register:40f0:8", ["const:bf9148:8", "const:4:8"]]
+ 00bf9148 ["CALL", null, ["callee:00c57fc0:8"]]
- 00bf90ac bytes 917b0194
+ 00bf9148 bytes 9e7b0194
- 00bf90c0 ["INT_ADD", "register:40f0:8", ["const:bf90c0:8", "const:4:8"]]
- 00bf90c0 ["CALL", null, ["callee:00c5e280:8"]]
+ 00bf915c ["INT_ADD", "register:40f0:8", ["const:bf915c:8", "const:4:8"]]
+ 00bf915c ["CALL", null, ["callee:00c5e280:8"]]
- 00bf90c0 bytes 3c940194
+ 00bf915c bytes 49940194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de185e3bdbb78b656538b943a03f0a1f"></a>

### [`00bf955c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf955c.md) → [`00bf95f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf95f8.md) _ZNSt6__ndk115future_categoryEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58310.md) · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c583e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583e0.md) · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf962c",
      "incomplete_value": false,
      "site": "00bf9630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9590",
      "incomplete_value": false,
      "site": "00bf9594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "definition_site": "00bf963c",
      "incomplete_value": false,
      "site": "00bf9640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf95a0",
      "incomplete_value": false,
      "site": "00bf95a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf9618",
      "incomplete_value": false,
      "site": "00bf9624",
      "value": [
        "leaf",
        "const:ca48c8:8"
      ]
    },
    "old": {
      "definition_site": "00bf957c",
      "incomplete_value": false,
      "site": "00bf9588",
      "value": [
        "leaf",
        "const:ca47f8:8"
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
      "00bf960c",
      "READ",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9618",
      "DATA",
      [
        "storage",
        "00ca47f8",
        null,
        null
      ]
    ],
    [
      "00bf962c",
      "PARAM",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bf960c",
      "READ",
      [
        "storage",
        "01127470",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9618",
      "DATA",
      [
        "storage",
        "00ca48c8",
        null,
        null
      ]
    ],
    [
      "00bf962c",
      "PARAM",
      [
        "storage",
        "01127470",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf955c.md#insn-00bf9594) · [`00bf95a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf955c.md#insn-00bf95a4) · [`00bf956c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf955c.md#insn-00bf956c)
- 新版 [`00bf9630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf95f8.md#insn-00bf9630) · [`00bf9640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf95f8.md#insn-00bf9640) · [`00bf9608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf95f8.md#insn-00bf9608)

~~~diff
- 00bf9594 ["INT_ADD", "register:40f0:8", ["const:bf9594:8", "const:4:8"]]
- 00bf9594 ["CALL", null, ["callee:00c57f20:8"]]
+ 00bf9630 ["INT_ADD", "register:40f0:8", ["const:bf9630:8", "const:4:8"]]
+ 00bf9630 ["CALL", null, ["callee:00c57f20:8"]]
- 00bf9594 bytes 2f7a0194
+ 00bf9630 bytes 3c7a0194
- 00bf95a4 ["INT_ADD", "register:40f0:8", ["const:bf95a4:8", "const:4:8"]]
- 00bf95a4 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf9640 ["INT_ADD", "register:40f0:8", ["const:bf9640:8", "const:4:8"]]
+ 00bf9640 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf95a4 bytes 337a0194
+ 00bf9640 bytes 407a0194
- 00bf956c ["COPY", "tmp:0:8", ["const:370:8"]]
- 00bf956c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bf956c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bf956c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bf9608 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 00bf9608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bf9608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bf9608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bf956c bytes 08c10d91
+ 00bf9608 bytes 08c11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bddcb0b2f8db2f602d36a3608f0ab25"></a>

### [`00bf9a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9a10.md) → [`00bf9aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9aac.md) _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c584a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584a0.md) · 呼出先 3件 [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md)
- 新版 呼出元 1件 [`00c58570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58570.md) · 呼出先 3件 [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md)

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
      "definition_site": "00bf9b30",
      "incomplete_value": false,
      "site": "00bf9b38",
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
            "const:9c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9a94",
      "incomplete_value": false,
      "site": "00bf9a9c",
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
            "const:a1b:8"
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
      "00bf9b30",
      "PARAM",
      [
        "storage",
        "002bea1b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf9b30",
      "PARAM",
      [
        "storage",
        "002be9c7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9a10.md#insn-00bf9a9c) · [`00bf9a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9a10.md#insn-00bf9a3c) · [`00bf9a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9a10.md#insn-00bf9a6c)
- 新版 [`00bf9b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9aac.md#insn-00bf9b38) · [`00bf9ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9aac.md#insn-00bf9ad8) · [`00bf9b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9aac.md#insn-00bf9b08)

~~~diff
- 00bf9a9c ["INT_ADD", "register:40f0:8", ["const:bf9a9c:8", "const:4:8"]]
- 00bf9a9c ["CALL", null, ["callee:00c581f0:8"]]
+ 00bf9b38 ["INT_ADD", "register:40f0:8", ["const:bf9b38:8", "const:4:8"]]
+ 00bf9b38 ["CALL", null, ["callee:00c581f0:8"]]
- 00bf9a9c bytes a1790194
+ 00bf9b38 bytes ae790194
- 00bf9a3c ["INT_ADD", "register:40f0:8", ["const:bf9a3c:8", "const:4:8"]]
- 00bf9a3c ["CALL", null, ["callee:00c58550:8"]]
+ 00bf9ad8 ["INT_ADD", "register:40f0:8", ["const:bf9ad8:8", "const:4:8"]]
+ 00bf9ad8 ["CALL", null, ["callee:00c58550:8"]]
- 00bf9a3c bytes 917a0194
+ 00bf9ad8 bytes 9e7a0194
- 00bf9a6c ["INT_ADD", "register:40f0:8", ["const:bf9a6c:8", "const:4:8"]]
- 00bf9a6c ["CALL", null, ["callee:00c581c0:8"]]
+ 00bf9b08 ["INT_ADD", "register:40f0:8", ["const:bf9b08:8", "const:4:8"]]
+ 00bf9b08 ["CALL", null, ["callee:00c581c0:8"]]
- 00bf9a6c bytes a1790194
+ 00bf9b08 bytes ae790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3901e0c2be38ef8583f4f380be0f173"></a>

### [`00bf9ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ca4.md) → [`00bf9d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d40.md) _ZNSt6__ndk17promiseIvEC1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00bf9d70",
      "incomplete_value": true,
      "site": "00bf9d70",
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
      "definition_site": "00bf9cd4",
      "incomplete_value": true,
      "site": "00bf9cd4",
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
      "00bf9d64",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "00bf9d70",
      "DATA",
      [
        "storage",
        "00c92cd8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00bf9d64",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "00bf9d70",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ca4.md#insn-00bf9cbc) · [`00bf9cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ca4.md#insn-00bf9cc8)
- 新版 [`00bf9d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d40.md#insn-00bf9d58) · [`00bf9d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d40.md#insn-00bf9d64)

~~~diff
- 00bf9cbc ["INT_ADD", "register:40f0:8", ["const:bf9cbc:8", "const:4:8"]]
- 00bf9cbc ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf9d58 ["INT_ADD", "register:40f0:8", ["const:bf9d58:8", "const:4:8"]]
+ 00bf9d58 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf9cbc bytes 75780194
+ 00bf9d58 bytes 82780194
- 00bf9cc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
- 00bf9cc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf9d64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
+ 00bf9d64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf9cc8 bytes 082946f9
+ 00bf9d64 bytes 089146f9
~~~


<a id="compare-b0565ac3c2b0e481776b3f9d9d6f4e26"></a>

### [`00bf9cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9cf8.md) → [`00bf9d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d94.md) _ZNSt6__ndk17promiseIvED1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0045a6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6c8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0045a708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a708.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.11% / 新版 90.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf9e00",
      "incomplete_value": false,
      "site": "00bf9e00",
      "value": [
        "leaf",
        "const:ca48c8:8"
      ]
    },
    "old": {
      "definition_site": "00bf9d64",
      "incomplete_value": false,
      "site": "00bf9d64",
      "value": [
        "leaf",
        "const:ca47f8:8"
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf9e3c",
      "incomplete_value": true,
      "site": "00bf9e44",
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
      "definition_site": "00bf9da0",
      "incomplete_value": true,
      "site": "00bf9da8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9e58",
      "incomplete_value": true,
      "site": "00bf9e60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
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
      "definition_site": "00bf9dbc",
      "incomplete_value": true,
      "site": "00bf9dc4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
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
      "00bf9dec",
      "READ",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9e00",
      "DATA",
      [
        "storage",
        "00ca47f8",
        null,
        null
      ]
    ],
    [
      "00bf9e34",
      "READ",
      [
        "storage",
        "00c9ac60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf9dec",
      "READ",
      [
        "storage",
        "01127470",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9e00",
      "DATA",
      [
        "storage",
        "00ca48c8",
        null,
        null
      ]
    ],
    [
      "00bf9e34",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9cf8.md#insn-00bf9dc4) · [`00bf9e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9cf8.md#insn-00bf9e4c) · [`00bf9e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9cf8.md#insn-00bf9e5c)
- 新版 [`00bf9e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d94.md#insn-00bf9e60) · [`00bf9ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d94.md#insn-00bf9ee8) · [`00bf9ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9d94.md#insn-00bf9ef8)

~~~diff
- 00bf9dc4 ["INT_ADD", "register:40f0:8", ["const:bf9dc4:8", "const:4:8"]]
- 00bf9dc4 ["CALL", null, ["callee:00c58400:8"]]
+ 00bf9e60 ["INT_ADD", "register:40f0:8", ["const:bf9e60:8", "const:4:8"]]
+ 00bf9e60 ["CALL", null, ["callee:00c58400:8"]]
- 00bf9dc4 bytes 5b790194
+ 00bf9e60 bytes 68790194
- 00bf9e4c ["INT_ADD", "register:40f0:8", ["const:bf9e4c:8", "const:4:8"]]
- 00bf9e4c ["CALL", null, ["callee:00c57f20:8"]]
+ 00bf9ee8 ["INT_ADD", "register:40f0:8", ["const:bf9ee8:8", "const:4:8"]]
+ 00bf9ee8 ["CALL", null, ["callee:00c57f20:8"]]
- 00bf9e4c bytes 01780194
+ 00bf9ee8 bytes 0e780194
- 00bf9e5c ["INT_ADD", "register:40f0:8", ["const:bf9e5c:8", "const:4:8"]]
- 00bf9e5c ["CALL", null, ["callee:00c57f40:8"]]
+ 00bf9ef8 ["INT_ADD", "register:40f0:8", ["const:bf9ef8:8", "const:4:8"]]
+ 00bf9ef8 ["CALL", null, ["callee:00c57f40:8"]]
- 00bf9e5c bytes 05780194
+ 00bf9ef8 bytes 12780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c0fb391b0df0ccf3b26060a3a7906c3"></a>

### [`00bfa088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa088.md) → [`00bfa124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa124.md) FUN_00bfa124

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfa14c",
      "incomplete_value": true,
      "site": "00bfa14c",
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
      "definition_site": "00bfa0b0",
      "incomplete_value": true,
      "site": "00bfa0b0",
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
      "00bfa140",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "00bfa14c",
      "DATA",
      [
        "storage",
        "00c92cd8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00bfa140",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "00bfa14c",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa088.md#insn-00bfa0a4) · [`00bfa0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa088.md#insn-00bfa0b4) · [`00bfa0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa088.md#insn-00bfa0bc)
- 新版 [`00bfa140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa124.md#insn-00bfa140) · [`00bfa150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa124.md#insn-00bfa150) · [`00bfa158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa124.md#insn-00bfa158)

~~~diff
- 00bfa0a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
- 00bfa0a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfa140 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
+ 00bfa140 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfa0a4 bytes 082946f9
+ 00bfa140 bytes 089146f9
- 00bfa0b4 ["INT_ADD", "register:40f0:8", ["const:bfa0b4:8", "const:4:8"]]
- 00bfa0b4 ["CALL", null, ["callee:00c581a0:8"]]
+ 00bfa150 ["INT_ADD", "register:40f0:8", ["const:bfa150:8", "const:4:8"]]
+ 00bfa150 ["CALL", null, ["callee:00c581a0:8"]]
- 00bfa0b4 bytes 07780194
+ 00bfa150 bytes 14780194
- 00bfa0bc ["INT_ADD", "register:40f0:8", ["const:bfa0bc:8", "const:4:8"]]
- 00bfa0bc ["CALL", null, ["callee:00c57f30:8"]]
+ 00bfa158 ["INT_ADD", "register:40f0:8", ["const:bfa158:8", "const:4:8"]]
+ 00bfa158 ["CALL", null, ["callee:00c57f30:8"]]
- 00bfa0bc bytes 69770194
+ 00bfa158 bytes 76770194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38d2c9aed29a2645225a4d4c44489264"></a>

### [`00bfa130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa130.md) → [`00bfa1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1cc.md) _ZNSt6__ndk15mutex4lockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) · 呼出先 2件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md)
- 新版 呼出元 1件 [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) · 呼出先 2件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa1f0",
      "incomplete_value": false,
      "site": "00bfa1f4",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa154",
      "incomplete_value": false,
      "site": "00bfa158",
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
            "const:79e:8"
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
      "00bfa1f0",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa1f0",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa130.md#insn-00bfa158) · [`00bfa13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa130.md#insn-00bfa13c) · [`00bfa154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa130.md#insn-00bfa154)
- 新版 [`00bfa1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1cc.md#insn-00bfa1f4) · [`00bfa1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1cc.md#insn-00bfa1d8) · [`00bfa1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1cc.md#insn-00bfa1f0)

~~~diff
- 00bfa158 ["INT_ADD", "register:40f0:8", ["const:bfa158:8", "const:4:8"]]
- 00bfa158 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa1f4 ["INT_ADD", "register:40f0:8", ["const:bfa1f4:8", "const:4:8"]]
+ 00bfa1f4 ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa158 bytes f2770194
+ 00bfa1f4 bytes ff770194
- 00bfa13c ["INT_ADD", "register:40f0:8", ["const:bfa13c:8", "const:4:8"]]
- 00bfa13c ["CALL", null, ["callee:00c5b770:8"]]
+ 00bfa1d8 ["INT_ADD", "register:40f0:8", ["const:bfa1d8:8", "const:4:8"]]
+ 00bfa1d8 ["CALL", null, ["callee:00c5b770:8"]]
- 00bfa13c bytes 59850194
+ 00bfa1d8 bytes 66850194
- 00bfa154 ["COPY", "tmp:0:8", ["const:79e:8"]]
- 00bfa154 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa154 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa154 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfa1f0 ["COPY", "tmp:0:8", ["const:742:8"]]
+ 00bfa1f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa1f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa1f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bfa154 bytes 21781e91
+ 00bfa1f0 bytes 21081d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4654e9475e3f804da8570f33719dad9"></a>

### [`00bfa1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa1a4.md) → [`00bfa240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa240.md) _ZNSt6__ndk115recursive_mutexC1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0c0.md) · 呼出先 6件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5b690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b690.md) [`00c5be80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be80.md) [`00c5be90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bea0.md)
- 新版 呼出元 1件 [`00c5a190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a190.md) · 呼出先 6件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5b760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b760.md) [`00c5bf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf50.md) [`00c5bf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf60.md) [`00c5bf70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa2dc",
      "incomplete_value": false,
      "site": "00bfa2e0",
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
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa240",
      "incomplete_value": false,
      "site": "00bfa244",
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
            "const:8c3:8"
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
      "00bfa2dc",
      "PARAM",
      [
        "storage",
        "002a88c3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa2dc",
      "PARAM",
      [
        "storage",
        "002a8867",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa1a4.md#insn-00bfa244) · [`00bfa1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa1a4.md#insn-00bfa1c0) · [`00bfa1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa1a4.md#insn-00bfa1d0)
- 新版 [`00bfa2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa240.md#insn-00bfa2e0) · [`00bfa25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa240.md#insn-00bfa25c) · [`00bfa26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa240.md#insn-00bfa26c)

~~~diff
- 00bfa244 ["INT_ADD", "register:40f0:8", ["const:bfa244:8", "const:4:8"]]
- 00bfa244 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa2e0 ["INT_ADD", "register:40f0:8", ["const:bfa2e0:8", "const:4:8"]]
+ 00bfa2e0 ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa244 bytes b7770194
+ 00bfa2e0 bytes c4770194
- 00bfa1c0 ["INT_ADD", "register:40f0:8", ["const:bfa1c0:8", "const:4:8"]]
- 00bfa1c0 ["CALL", null, ["callee:00c5bf70:8"]]
+ 00bfa25c ["INT_ADD", "register:40f0:8", ["const:bfa25c:8", "const:4:8"]]
+ 00bfa25c ["CALL", null, ["callee:00c5bf70:8"]]
- 00bfa1c0 bytes 38870194
+ 00bfa25c bytes 45870194
- 00bfa1d0 ["INT_ADD", "register:40f0:8", ["const:bfa1d0:8", "const:4:8"]]
- 00bfa1d0 ["CALL", null, ["callee:00c5bf80:8"]]
+ 00bfa26c ["INT_ADD", "register:40f0:8", ["const:bfa26c:8", "const:4:8"]]
+ 00bfa26c ["CALL", null, ["callee:00c5bf80:8"]]
- 00bfa1d0 bytes 38870194
+ 00bfa26c bytes 45870194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b77679999305c73ccb1b023c5cf9a512"></a>

### [`00bfa268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa268.md) → [`00bfa304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa304.md) _ZNSt6__ndk115recursive_mutex4lockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0e0.md) · 呼出先 2件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md)
- 新版 呼出元 1件 [`00c5a1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1b0.md) · 呼出先 2件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa328",
      "incomplete_value": false,
      "site": "00bfa32c",
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
            "const:4be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa28c",
      "incomplete_value": false,
      "site": "00bfa290",
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
            "const:51a:8"
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
      "00bfa328",
      "PARAM",
      [
        "storage",
        "002a751a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa328",
      "PARAM",
      [
        "storage",
        "002a74be",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa268.md#insn-00bfa290) · [`00bfa274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa268.md#insn-00bfa274) · [`00bfa28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa268.md#insn-00bfa28c)
- 新版 [`00bfa32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa304.md#insn-00bfa32c) · [`00bfa310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa304.md#insn-00bfa310) · [`00bfa328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa304.md#insn-00bfa328)

~~~diff
- 00bfa290 ["INT_ADD", "register:40f0:8", ["const:bfa290:8", "const:4:8"]]
- 00bfa290 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa32c ["INT_ADD", "register:40f0:8", ["const:bfa32c:8", "const:4:8"]]
+ 00bfa32c ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa290 bytes a4770194
+ 00bfa32c bytes b1770194
- 00bfa274 ["INT_ADD", "register:40f0:8", ["const:bfa274:8", "const:4:8"]]
- 00bfa274 ["CALL", null, ["callee:00c5b770:8"]]
+ 00bfa310 ["INT_ADD", "register:40f0:8", ["const:bfa310:8", "const:4:8"]]
+ 00bfa310 ["CALL", null, ["callee:00c5b770:8"]]
- 00bfa274 bytes 0b850194
+ 00bfa310 bytes 18850194
- 00bfa28c ["COPY", "tmp:0:8", ["const:51a:8"]]
- 00bfa28c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa28c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa28c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfa328 ["COPY", "tmp:0:8", ["const:4be:8"]]
+ 00bfa328 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa328 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa328 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bfa28c bytes 21681491
+ 00bfa328 bytes 21f81291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df33c4035e5e26420246424c7fb4bdec"></a>

### [`00bfa2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa2f8.md) → [`00bfa394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa394.md) _ZNSt6__ndk111timed_mutexD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa3d8",
      "incomplete_value": false,
      "site": "00bfa3dc",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa33c",
      "incomplete_value": false,
      "site": "00bfa340",
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
            "const:79e:8"
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
      "00bfa3d8",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa3d8",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa2f8.md#insn-00bfa340) · [`00bfa30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa2f8.md#insn-00bfa30c) · [`00bfa318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa2f8.md#insn-00bfa318)
- 新版 [`00bfa3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa394.md#insn-00bfa3dc) · [`00bfa3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa394.md#insn-00bfa3a8) · [`00bfa3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa394.md#insn-00bfa3b4)

~~~diff
- 00bfa340 ["INT_ADD", "register:40f0:8", ["const:bfa340:8", "const:4:8"]]
- 00bfa340 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa3dc ["INT_ADD", "register:40f0:8", ["const:bfa3dc:8", "const:4:8"]]
+ 00bfa3dc ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa340 bytes 78770194
+ 00bfa3dc bytes 85770194
- 00bfa30c ["INT_ADD", "register:40f0:8", ["const:bfa30c:8", "const:4:8"]]
- 00bfa30c ["CALL", null, ["callee:00c5b770:8"]]
+ 00bfa3a8 ["INT_ADD", "register:40f0:8", ["const:bfa3a8:8", "const:4:8"]]
+ 00bfa3a8 ["CALL", null, ["callee:00c5b770:8"]]
- 00bfa30c bytes e5840194
+ 00bfa3a8 bytes f2840194
- 00bfa318 ["INT_ADD", "register:40f0:8", ["const:bfa318:8", "const:4:8"]]
- 00bfa318 ["CALL", null, ["callee:00c5b780:8"]]
+ 00bfa3b4 ["INT_ADD", "register:40f0:8", ["const:bfa3b4:8", "const:4:8"]]
+ 00bfa3b4 ["CALL", null, ["callee:00c5b780:8"]]
- 00bfa318 bytes e6840194
+ 00bfa3b4 bytes f3840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2329a6af9e442eb0863c954c7595717c"></a>

### [`00bfa34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa34c.md) → [`00bfa3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa3e8.md) _ZNSt6__ndk111timed_mutex4lockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa46c",
      "incomplete_value": false,
      "site": "00bfa470",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa3d0",
      "incomplete_value": false,
      "site": "00bfa3d4",
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
            "const:79e:8"
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
      "00bfa46c",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa46c",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa34c.md#insn-00bfa3d4) · [`00bfa370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa34c.md#insn-00bfa370) · [`00bfa388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa34c.md#insn-00bfa388)
- 新版 [`00bfa470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa3e8.md#insn-00bfa470) · [`00bfa40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa3e8.md#insn-00bfa40c) · [`00bfa424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa3e8.md#insn-00bfa424)

~~~diff
- 00bfa3d4 ["INT_ADD", "register:40f0:8", ["const:bfa3d4:8", "const:4:8"]]
- 00bfa3d4 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa470 ["INT_ADD", "register:40f0:8", ["const:bfa470:8", "const:4:8"]]
+ 00bfa470 ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa3d4 bytes 53770194
+ 00bfa470 bytes 60770194
- 00bfa370 ["INT_ADD", "register:40f0:8", ["const:bfa370:8", "const:4:8"]]
- 00bfa370 ["CALL", null, ["callee:00c5b770:8"]]
+ 00bfa40c ["INT_ADD", "register:40f0:8", ["const:bfa40c:8", "const:4:8"]]
+ 00bfa40c ["CALL", null, ["callee:00c5b770:8"]]
- 00bfa370 bytes cc840194
+ 00bfa40c bytes d9840194
- 00bfa388 ["INT_ADD", "register:40f0:8", ["const:bfa388:8", "const:4:8"]]
- 00bfa388 ["CALL", null, ["callee:00c58550:8"]]
+ 00bfa424 ["INT_ADD", "register:40f0:8", ["const:bfa424:8", "const:4:8"]]
+ 00bfa424 ["CALL", null, ["callee:00c58550:8"]]
- 00bfa388 bytes 3e780194
+ 00bfa424 bytes 4b780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-862b1a686a60ff2c7db7a98bad5e5e21"></a>

### [`00bfa43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa43c.md) → [`00bfa4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa4d8.md) _ZNSt6__ndk111timed_mutex6unlockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c59110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59110.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c591e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c591e0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa51c",
      "incomplete_value": false,
      "site": "00bfa520",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa480",
      "incomplete_value": false,
      "site": "00bfa484",
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
            "const:79e:8"
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
      "00bfa51c",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa51c",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa43c.md#insn-00bfa484) · [`00bfa450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa43c.md#insn-00bfa450) · [`00bfa460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa43c.md#insn-00bfa460)
- 新版 [`00bfa520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa4d8.md#insn-00bfa520) · [`00bfa4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa4d8.md#insn-00bfa4ec) · [`00bfa4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa4d8.md#insn-00bfa4fc)

~~~diff
- 00bfa484 ["INT_ADD", "register:40f0:8", ["const:bfa484:8", "const:4:8"]]
- 00bfa484 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa520 ["INT_ADD", "register:40f0:8", ["const:bfa520:8", "const:4:8"]]
+ 00bfa520 ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa484 bytes 27770194
+ 00bfa520 bytes 34770194
- 00bfa450 ["INT_ADD", "register:40f0:8", ["const:bfa450:8", "const:4:8"]]
- 00bfa450 ["CALL", null, ["callee:00c5b770:8"]]
+ 00bfa4ec ["INT_ADD", "register:40f0:8", ["const:bfa4ec:8", "const:4:8"]]
+ 00bfa4ec ["CALL", null, ["callee:00c5b770:8"]]
- 00bfa450 bytes 94840194
+ 00bfa4ec bytes a1840194
- 00bfa460 ["INT_ADD", "register:40f0:8", ["const:bfa460:8", "const:4:8"]]
- 00bfa460 ["CALL", null, ["callee:00c591e0:8"]]
+ 00bfa4fc ["INT_ADD", "register:40f0:8", ["const:bfa4fc:8", "const:4:8"]]
+ 00bfa4fc ["CALL", null, ["callee:00c591e0:8"]]
- 00bfa460 bytes 2c7b0194
+ 00bfa4fc bytes 397b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-161f0749c7a110a4d2dd1b06742a0cc0"></a>

### [`00bfa4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa4ac.md) → [`00bfa548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa548.md) _ZNSt6__ndk121recursive_timed_mutexD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa58c",
      "incomplete_value": false,
      "site": "00bfa590",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa4f0",
      "incomplete_value": false,
      "site": "00bfa4f4",
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
            "const:79e:8"
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
      "00bfa58c",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa58c",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa4ac.md#insn-00bfa4f4) · [`00bfa4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa4ac.md#insn-00bfa4c0) · [`00bfa4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa4ac.md#insn-00bfa4cc)
- 新版 [`00bfa590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa548.md#insn-00bfa590) · [`00bfa55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa548.md#insn-00bfa55c) · [`00bfa568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa548.md#insn-00bfa568)

~~~diff
- 00bfa4f4 ["INT_ADD", "register:40f0:8", ["const:bfa4f4:8", "const:4:8"]]
- 00bfa4f4 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa590 ["INT_ADD", "register:40f0:8", ["const:bfa590:8", "const:4:8"]]
+ 00bfa590 ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa4f4 bytes 0b770194
+ 00bfa590 bytes 18770194
- 00bfa4c0 ["INT_ADD", "register:40f0:8", ["const:bfa4c0:8", "const:4:8"]]
- 00bfa4c0 ["CALL", null, ["callee:00c5b770:8"]]
+ 00bfa55c ["INT_ADD", "register:40f0:8", ["const:bfa55c:8", "const:4:8"]]
+ 00bfa55c ["CALL", null, ["callee:00c5b770:8"]]
- 00bfa4c0 bytes 78840194
+ 00bfa55c bytes 85840194
- 00bfa4cc ["INT_ADD", "register:40f0:8", ["const:bfa4cc:8", "const:4:8"]]
- 00bfa4cc ["CALL", null, ["callee:00c5b780:8"]]
+ 00bfa568 ["INT_ADD", "register:40f0:8", ["const:bfa568:8", "const:4:8"]]
+ 00bfa568 ["CALL", null, ["callee:00c5b780:8"]]
- 00bfa4cc bytes 79840194
+ 00bfa568 bytes 86840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bee49ef10d3a31df30458f09343a1cd"></a>

### [`00bfa500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa500.md) → [`00bfa59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa59c.md) _ZNSt6__ndk121recursive_timed_mutex4lockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md) [`00c58620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58620.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md) [`00c586f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586f0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa648",
      "incomplete_value": false,
      "site": "00bfa64c",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa5ac",
      "incomplete_value": false,
      "site": "00bfa5b0",
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
            "const:79e:8"
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
      "definition_site": "00bfa654",
      "incomplete_value": false,
      "site": "00bfa65c",
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
            "const:d7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa5b8",
      "incomplete_value": false,
      "site": "00bfa5c0",
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
            "const:dc7:8"
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
      "00bfa648",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ],
    [
      "00bfa654",
      "PARAM",
      [
        "storage",
        "002a3dc7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa648",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ],
    [
      "00bfa654",
      "PARAM",
      [
        "storage",
        "002a3d7a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa500.md#insn-00bfa5b0) · [`00bfa5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa500.md#insn-00bfa5c0) · [`00bfa518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa500.md#insn-00bfa518)
- 新版 [`00bfa64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa59c.md#insn-00bfa64c) · [`00bfa65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa59c.md#insn-00bfa65c) · [`00bfa5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa59c.md#insn-00bfa5b4)

~~~diff
- 00bfa5b0 ["INT_ADD", "register:40f0:8", ["const:bfa5b0:8", "const:4:8"]]
- 00bfa5b0 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa64c ["INT_ADD", "register:40f0:8", ["const:bfa64c:8", "const:4:8"]]
+ 00bfa64c ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa5b0 bytes dc760194
+ 00bfa64c bytes e9760194
- 00bfa5c0 ["INT_ADD", "register:40f0:8", ["const:bfa5c0:8", "const:4:8"]]
- 00bfa5c0 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa65c ["INT_ADD", "register:40f0:8", ["const:bfa65c:8", "const:4:8"]]
+ 00bfa65c ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa5c0 bytes d8760194
+ 00bfa65c bytes e5760194
- 00bfa518 ["INT_ADD", "register:40f0:8", ["const:bfa518:8", "const:4:8"]]
- 00bfa518 ["CALL", null, ["callee:00c586f0:8"]]
+ 00bfa5b4 ["INT_ADD", "register:40f0:8", ["const:bfa5b4:8", "const:4:8"]]
+ 00bfa5b4 ["CALL", null, ["callee:00c586f0:8"]]
- 00bfa518 bytes 42780194
+ 00bfa5b4 bytes 4f780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7200c086b805967c3654b388666539d5"></a>

### [`00bfa668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa668.md) → [`00bfa704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa704.md) _ZNSt6__ndk121recursive_timed_mutex6unlockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c59110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59110.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c591e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c591e0.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa76c",
      "incomplete_value": false,
      "site": "00bfa770",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa6d0",
      "incomplete_value": false,
      "site": "00bfa6d4",
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
            "const:79e:8"
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
      "00bfa76c",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa76c",
      "PARAM",
      [
        "storage",
        "002b1742",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa668.md#insn-00bfa6d4) · [`00bfa67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa668.md#insn-00bfa67c) · [`00bfa698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa668.md#insn-00bfa698)
- 新版 [`00bfa770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa704.md#insn-00bfa770) · [`00bfa718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa704.md#insn-00bfa718) · [`00bfa734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa704.md#insn-00bfa734)

~~~diff
- 00bfa6d4 ["INT_ADD", "register:40f0:8", ["const:bfa6d4:8", "const:4:8"]]
- 00bfa6d4 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa770 ["INT_ADD", "register:40f0:8", ["const:bfa770:8", "const:4:8"]]
+ 00bfa770 ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa6d4 bytes 93760194
+ 00bfa770 bytes a0760194
- 00bfa67c ["INT_ADD", "register:40f0:8", ["const:bfa67c:8", "const:4:8"]]
- 00bfa67c ["CALL", null, ["callee:00c5b770:8"]]
+ 00bfa718 ["INT_ADD", "register:40f0:8", ["const:bfa718:8", "const:4:8"]]
+ 00bfa718 ["CALL", null, ["callee:00c5b770:8"]]
- 00bfa67c bytes 09840194
+ 00bfa718 bytes 16840194
- 00bfa698 ["INT_ADD", "register:40f0:8", ["const:bfa698:8", "const:4:8"]]
- 00bfa698 ["CALL", null, ["callee:00c5b780:8"]]
+ 00bfa734 ["INT_ADD", "register:40f0:8", ["const:bfa734:8", "const:4:8"]]
+ 00bfa734 ["CALL", null, ["callee:00c5b780:8"]]
- 00bfa698 bytes 06840194
+ 00bfa734 bytes 13840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21ff21754cac11e633066a7d3b6d9cb9"></a>

### [`00bfa704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa704.md) → [`00bfa7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7a0.md) _ZNSt6__ndk16thread4joinEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58170.md) · 呼出先 2件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5d640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d640.md)
- 新版 呼出元 1件 [`00c58240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58240.md) · 呼出先 2件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5d710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d710.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa7e4",
      "incomplete_value": false,
      "site": "00bfa7e8",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa748",
      "incomplete_value": false,
      "site": "00bfa74c",
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
            "const:2e7:8"
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
      "00bfa7e4",
      "PARAM",
      [
        "storage",
        "002a62e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa7e4",
      "PARAM",
      [
        "storage",
        "002a628b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa704.md#insn-00bfa74c) · [`00bfa724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa704.md#insn-00bfa724) · [`00bfa748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa704.md#insn-00bfa748)
- 新版 [`00bfa7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7a0.md#insn-00bfa7e8) · [`00bfa7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7a0.md#insn-00bfa7c0) · [`00bfa7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7a0.md#insn-00bfa7e4)

~~~diff
- 00bfa74c ["INT_ADD", "register:40f0:8", ["const:bfa74c:8", "const:4:8"]]
- 00bfa74c ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa7e8 ["INT_ADD", "register:40f0:8", ["const:bfa7e8:8", "const:4:8"]]
+ 00bfa7e8 ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa74c bytes 75760194
+ 00bfa7e8 bytes 82760194
- 00bfa724 ["INT_ADD", "register:40f0:8", ["const:bfa724:8", "const:4:8"]]
- 00bfa724 ["CALL", null, ["callee:00c5d710:8"]]
+ 00bfa7c0 ["INT_ADD", "register:40f0:8", ["const:bfa7c0:8", "const:4:8"]]
+ 00bfa7c0 ["CALL", null, ["callee:00c5d710:8"]]
- 00bfa724 bytes c78b0194
+ 00bfa7c0 bytes d48b0194
- 00bfa748 ["COPY", "tmp:0:8", ["const:2e7:8"]]
- 00bfa748 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa748 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa748 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfa7e4 ["COPY", "tmp:0:8", ["const:28b:8"]]
+ 00bfa7e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa7e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa7e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bfa748 bytes 219c0b91
+ 00bfa7e4 bytes 212c0a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f84d7a1b98e5580447e10ce1f3cc744d"></a>

### [`00bfa750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa750.md) → [`00bfa7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7ec.md) _ZNSt6__ndk16thread6detachEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58510.md) · 呼出先 2件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5e280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e280.md)
- 新版 呼出元 1件 [`00c585e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585e0.md) · 呼出先 2件 [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5e350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e350.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa82c",
      "incomplete_value": false,
      "site": "00bfa830",
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
            "const:4ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa790",
      "incomplete_value": false,
      "site": "00bfa794",
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
            "const:54b:8"
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
      "00bfa82c",
      "PARAM",
      [
        "storage",
        "002ae54b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa82c",
      "PARAM",
      [
        "storage",
        "002ae4ef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa750.md#insn-00bfa794) · [`00bfa76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa750.md#insn-00bfa76c) · [`00bfa790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa750.md#insn-00bfa790)
- 新版 [`00bfa830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7ec.md#insn-00bfa830) · [`00bfa808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7ec.md#insn-00bfa808) · [`00bfa82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa7ec.md#insn-00bfa82c)

~~~diff
- 00bfa794 ["INT_ADD", "register:40f0:8", ["const:bfa794:8", "const:4:8"]]
- 00bfa794 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa830 ["INT_ADD", "register:40f0:8", ["const:bfa830:8", "const:4:8"]]
+ 00bfa830 ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa794 bytes 63760194
+ 00bfa830 bytes 70760194
- 00bfa76c ["INT_ADD", "register:40f0:8", ["const:bfa76c:8", "const:4:8"]]
- 00bfa76c ["CALL", null, ["callee:00c5e350:8"]]
+ 00bfa808 ["INT_ADD", "register:40f0:8", ["const:bfa808:8", "const:4:8"]]
+ 00bfa808 ["CALL", null, ["callee:00c5e350:8"]]
- 00bfa76c bytes c58e0194
+ 00bfa808 bytes d28e0194
- 00bfa790 ["COPY", "tmp:0:8", ["const:54b:8"]]
- 00bfa790 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa790 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa790 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfa82c ["COPY", "tmp:0:8", ["const:4ef:8"]]
+ 00bfa82c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa82c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa82c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bfa790 bytes 212c1591
+ 00bfa82c bytes 21bc1391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe91dfea844a5ad86b58e45812d189a2"></a>

### [`00bfa844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa844.md) → [`00bfa8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa8e0.md) _ZNSt6__ndk119__thread_local_dataEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) · 呼出先 3件 [`00bfa8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8c8.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) · 呼出先 3件 [`00bfa964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfa940",
      "incomplete_value": true,
      "site": "00bfa940",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa8a4",
      "incomplete_value": true,
      "site": "00bfa8a4",
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
            "const:380:8"
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
      "definition_site": "00bfa91c",
      "incomplete_value": false,
      "site": "00bfa920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa880",
      "incomplete_value": false,
      "site": "00bfa884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "definition_site": "00bfa930",
      "incomplete_value": false,
      "site": "00bfa934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa894",
      "incomplete_value": false,
      "site": "00bfa898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "00bfa8fc",
      "READ",
      [
        "storage",
        "01127388",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfa904",
      "READ",
      [
        "storage",
        "01127380",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfa904",
      "DATA",
      [
        "storage",
        "01127378",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfa8fc",
      "READ",
      [
        "storage",
        "01127488",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfa904",
      "READ",
      [
        "storage",
        "01127480",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfa904",
      "DATA",
      [
        "storage",
        "01127478",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa844.md#insn-00bfa884) · [`00bfa898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa844.md#insn-00bfa898) · [`00bfa8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa844.md#insn-00bfa8a4)
- 新版 [`00bfa920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa8e0.md#insn-00bfa920) · [`00bfa934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa8e0.md#insn-00bfa934) · [`00bfa940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa8e0.md#insn-00bfa940)

~~~diff
- 00bfa884 ["INT_ADD", "register:40f0:8", ["const:bfa884:8", "const:4:8"]]
- 00bfa884 ["CALL", null, ["callee:00c57f20:8"]]
+ 00bfa920 ["INT_ADD", "register:40f0:8", ["const:bfa920:8", "const:4:8"]]
+ 00bfa920 ["CALL", null, ["callee:00c57f20:8"]]
- 00bfa884 bytes 73750194
+ 00bfa920 bytes 80750194
- 00bfa898 ["INT_ADD", "register:40f0:8", ["const:bfa898:8", "const:4:8"]]
- 00bfa898 ["CALL", null, ["callee:00bfa964:8"]]
+ 00bfa934 ["INT_ADD", "register:40f0:8", ["const:bfa934:8", "const:4:8"]]
+ 00bfa934 ["CALL", null, ["callee:00bfa964:8"]]
- 00bfa898 bytes 0c000094
+ 00bfa934 bytes 0c000094
- 00bfa8a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:380:8"]]
- 00bfa8a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00bfa940 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
+ 00bfa940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bfa8a4 bytes 93c201f9
+ 00bfa940 bytes 934202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63de06bce77ded33ec9ca47a929fe1ec"></a>

### [`00bfa8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8c8.md) → [`00bfa964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md) FUN_00bfa964

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bfa844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa844.md) · 呼出先 3件 [`00bfac7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac7c.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a300.md)
- 新版 呼出元 1件 [`00bfa8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa8e0.md) · 呼出先 3件 [`00bfad18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad18.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5a3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "definition_site": "00bfa974",
      "incomplete_value": false,
      "site": "00bfa978",
      "value": [
        "leaf",
        "const:bfad18:8"
      ]
    },
    "old": {
      "definition_site": "00bfa8d8",
      "incomplete_value": false,
      "site": "00bfa8dc",
      "value": [
        "leaf",
        "const:bfac7c:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa990",
      "incomplete_value": false,
      "site": "00bfa994",
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
            "const:da3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa8f4",
      "incomplete_value": false,
      "site": "00bfa8f8",
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
            "const:df0:8"
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
      "00bfa974",
      "PARAM",
      [
        "storage",
        "00bfac7c",
        null,
        null
      ]
    ],
    [
      "00bfa990",
      "PARAM",
      [
        "storage",
        "002a3df0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa974",
      "PARAM",
      [
        "storage",
        "00bfad18",
        null,
        null
      ]
    ],
    [
      "00bfa990",
      "PARAM",
      [
        "storage",
        "002a3da3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8c8.md#insn-00bfa8dc) · [`00bfa8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8c8.md#insn-00bfa8f8) · [`00bfa8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8c8.md#insn-00bfa8d8)
- 新版 [`00bfa978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md#insn-00bfa978) · [`00bfa994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md#insn-00bfa994) · [`00bfa974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa964.md#insn-00bfa974)

~~~diff
- 00bfa8dc ["INT_ADD", "register:40f0:8", ["const:bfa8dc:8", "const:4:8"]]
- 00bfa8dc ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00bfa978 ["INT_ADD", "register:40f0:8", ["const:bfa978:8", "const:4:8"]]
+ 00bfa978 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00bfa8dc bytes 897e0194
+ 00bfa978 bytes 967e0194
- 00bfa8f8 ["INT_ADD", "register:40f0:8", ["const:bfa8f8:8", "const:4:8"]]
- 00bfa8f8 ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfa994 ["INT_ADD", "register:40f0:8", ["const:bfa994:8", "const:4:8"]]
+ 00bfa994 ["CALL", null, ["callee:00c581f0:8"]]
- 00bfa8f8 bytes 0a760194
+ 00bfa994 bytes 17760194
- 00bfa8d8 ["COPY", "register:4008:8", ["const:bfac7c:8"]]
+ 00bfa974 ["COPY", "register:4008:8", ["const:bfad18:8"]]
- 00bfa8d8 bytes 211d0010
+ 00bfa974 bytes 211d0010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f49be379d8abb41b7657300f2aa1d31c"></a>

### [`00bfac4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac4c.md) → [`00bface8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bface8.md) FUN_00bface8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bfa9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa9c8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00bfaa64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaa64.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfacf8",
      "incomplete_value": false,
      "site": "00bfacfc",
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
      "definition_site": "00bfac5c",
      "incomplete_value": false,
      "site": "00bfac60",
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
      "00bfacf8",
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
      "00bfacf8",
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

- 旧版 [`00bfac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac4c.md#insn-00bfac60) · [`00bfac5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac4c.md#insn-00bfac5c)
- 新版 [`00bfacfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bface8.md#insn-00bfacfc) · [`00bfacf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bface8.md#insn-00bfacf8)

~~~diff
- 00bfac60 ["INT_ADD", "register:40f0:8", ["const:bfac60:8", "const:4:8"]]
- 00bfac60 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00bfacfc ["INT_ADD", "register:40f0:8", ["const:bfacfc:8", "const:4:8"]]
+ 00bfacfc ["CALL", null, ["callee:0043b7b8:8"]]
- 00bfac60 bytes c602e197
+ 00bfacfc bytes af02e197
- 00bfac5c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00bfac5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bfac5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bfac5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bfacf8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00bfacf8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfacf8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfacf8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bfac5c bytes 00303d91
+ 00bfacf8 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2223a055a113c661ff37e70a1c4f280b"></a>

### [`00bfac64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac64.md) → [`00bfad00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad00.md) FUN_00bfad00

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bfaac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaac4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00bfab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfab60.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfad10",
      "incomplete_value": false,
      "site": "00bfad14",
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
      "definition_site": "00bfac74",
      "incomplete_value": false,
      "site": "00bfac78",
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
      "00bfad10",
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
      "00bfad10",
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

- 旧版 [`00bfac78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac64.md#insn-00bfac78) · [`00bfac74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac64.md#insn-00bfac74)
- 新版 [`00bfad14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad00.md#insn-00bfad14) · [`00bfad10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad00.md#insn-00bfad10)

~~~diff
- 00bfac78 ["INT_ADD", "register:40f0:8", ["const:bfac78:8", "const:4:8"]]
- 00bfac78 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00bfad14 ["INT_ADD", "register:40f0:8", ["const:bfad14:8", "const:4:8"]]
+ 00bfad14 ["CALL", null, ["callee:0043b7b8:8"]]
- 00bfac78 bytes c002e197
+ 00bfad14 bytes a902e197
- 00bfac74 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00bfac74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bfac74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bfac74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bfad10 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00bfad10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfad10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfad10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bfac74 bytes 00303d91
+ 00bfad10 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47a8a3b4d645834483eb3d70d4e4c034"></a>

### [`00bfacb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfacb4.md) → [`00bfad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad50.md) _ZNSt6__ndk113random_deviceC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) · 呼出先 4件 [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5d610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d610.md)
- 新版 呼出元 1件 [`00c58470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58470.md) · 呼出先 4件 [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5d6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d6e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfadac",
      "incomplete_value": false,
      "site": "00bfadbc",
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
            "const:a33:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfad10",
      "incomplete_value": false,
      "site": "00bfad20",
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
            "const:a02:8"
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
      "00bfadac",
      "PARAM",
      [
        "storage",
        "002b4a02",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfadac",
      "PARAM",
      [
        "storage",
        "002b4a33",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfad20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfacb4.md#insn-00bfad20) · [`00bface4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfacb4.md#insn-00bface4) · [`00bfad04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfacb4.md#insn-00bfad04)
- 新版 [`00bfadbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad50.md#insn-00bfadbc) · [`00bfad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad50.md#insn-00bfad80) · [`00bfada0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad50.md#insn-00bfada0)

~~~diff
- 00bfad20 ["INT_ADD", "register:40f0:8", ["const:bfad20:8", "const:4:8"]]
- 00bfad20 ["CALL", null, ["callee:00c58180:8"]]
+ 00bfadbc ["INT_ADD", "register:40f0:8", ["const:bfadbc:8", "const:4:8"]]
+ 00bfadbc ["CALL", null, ["callee:00c58180:8"]]
- 00bfad20 bytes e4740194
+ 00bfadbc bytes f1740194
- 00bface4 ["INT_ADD", "register:40f0:8", ["const:bface4:8", "const:4:8"]]
- 00bface4 ["CALL", null, ["callee:00c5d6e0:8"]]
+ 00bfad80 ["INT_ADD", "register:40f0:8", ["const:bfad80:8", "const:4:8"]]
+ 00bfad80 ["CALL", null, ["callee:00c5d6e0:8"]]
- 00bface4 bytes 4b8a0194
+ 00bfad80 bytes 588a0194
- 00bfad04 ["INT_ADD", "register:40f0:8", ["const:bfad04:8", "const:4:8"]]
- 00bfad04 ["CALL", null, ["callee:00c58190:8"]]
+ 00bfada0 ["INT_ADD", "register:40f0:8", ["const:bfada0:8", "const:4:8"]]
+ 00bfada0 ["CALL", null, ["callee:00c58190:8"]]
- 00bfad04 bytes ef740194
+ 00bfada0 bytes fc740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a5a09642d48b5c3882293208ab3fedb"></a>

### [`00bfad7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad7c.md) → [`00bfae18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfae18.md) _ZNSt6__ndk113random_deviceclEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md) · 呼出先 3件 [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5d650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d650.md)
- 新版 呼出元 1件 [`00c58480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58480.md) · 呼出先 3件 [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c581f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581f0.md) [`00c5d720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfae94",
      "incomplete_value": false,
      "site": "00bfae98",
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
            "const:cee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfadf8",
      "incomplete_value": false,
      "site": "00bfadfc",
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
            "const:d42:8"
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
      "definition_site": "00bfaea0",
      "incomplete_value": false,
      "site": "00bfaea8",
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
            "const:44f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfae04",
      "incomplete_value": false,
      "site": "00bfae0c",
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
            "const:4ab:8"
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
      "00bfae94",
      "PARAM",
      [
        "storage",
        "002b8d42",
        null,
        "string"
      ]
    ],
    [
      "00bfaea0",
      "PARAM",
      [
        "storage",
        "002ac4ab",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfae94",
      "PARAM",
      [
        "storage",
        "002b8cee",
        null,
        "string"
      ]
    ],
    [
      "00bfaea0",
      "PARAM",
      [
        "storage",
        "002ac44f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfadfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad7c.md#insn-00bfadfc) · [`00bfae0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad7c.md#insn-00bfae0c) · [`00bfada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad7c.md#insn-00bfada0)
- 新版 [`00bfae98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfae18.md#insn-00bfae98) · [`00bfaea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfae18.md#insn-00bfaea8) · [`00bfae3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfae18.md#insn-00bfae3c)

~~~diff
- 00bfadfc ["INT_ADD", "register:40f0:8", ["const:bfadfc:8", "const:4:8"]]
- 00bfadfc ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfae98 ["INT_ADD", "register:40f0:8", ["const:bfae98:8", "const:4:8"]]
+ 00bfae98 ["CALL", null, ["callee:00c581f0:8"]]
- 00bfadfc bytes c9740194
+ 00bfae98 bytes d6740194
- 00bfae0c ["INT_ADD", "register:40f0:8", ["const:bfae0c:8", "const:4:8"]]
- 00bfae0c ["CALL", null, ["callee:00c581f0:8"]]
+ 00bfaea8 ["INT_ADD", "register:40f0:8", ["const:bfaea8:8", "const:4:8"]]
+ 00bfaea8 ["CALL", null, ["callee:00c581f0:8"]]
- 00bfae0c bytes c5740194
+ 00bfaea8 bytes d2740194
- 00bfada0 ["INT_ADD", "register:40f0:8", ["const:bfada0:8", "const:4:8"]]
- 00bfada0 ["CALL", null, ["callee:00c58190:8"]]
+ 00bfae3c ["INT_ADD", "register:40f0:8", ["const:bfae3c:8", "const:4:8"]]
+ 00bfae3c ["CALL", null, ["callee:00c58190:8"]]
- 00bfada0 bytes c8740194
+ 00bfae3c bytes d5740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae4092c106b4cfa3d7a033075c12e1eb"></a>

### [`00bfaeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaeec.md) → [`00bfaf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf88.md) _ZNSt6__ndk117iostream_categoryEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfafbc",
      "incomplete_value": false,
      "site": "00bfafc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfaf20",
      "incomplete_value": false,
      "site": "00bfaf24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "definition_site": "00bfafcc",
      "incomplete_value": false,
      "site": "00bfafd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfaf30",
      "incomplete_value": false,
      "site": "00bfaf34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bfafa8",
      "incomplete_value": false,
      "site": "00bfafb4",
      "value": [
        "leaf",
        "const:ca48d0:8"
      ]
    },
    "old": {
      "definition_site": "00bfaf0c",
      "incomplete_value": false,
      "site": "00bfaf18",
      "value": [
        "leaf",
        "const:ca4800:8"
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
      "00bfaf9c",
      "READ",
      [
        "storage",
        "01127390",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfafa8",
      "DATA",
      [
        "storage",
        "00ca4800",
        null,
        "pointer"
      ]
    ],
    [
      "00bfafbc",
      "PARAM",
      [
        "storage",
        "01127390",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bfaf9c",
      "READ",
      [
        "storage",
        "01127490",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfafa8",
      "DATA",
      [
        "storage",
        "00ca48d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfafbc",
      "PARAM",
      [
        "storage",
        "01127490",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfaf24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaeec.md#insn-00bfaf24) · [`00bfaf34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaeec.md#insn-00bfaf34) · [`00bfaefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaeec.md#insn-00bfaefc)
- 新版 [`00bfafc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf88.md#insn-00bfafc0) · [`00bfafd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf88.md#insn-00bfafd0) · [`00bfaf98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf88.md#insn-00bfaf98)

~~~diff
- 00bfaf24 ["INT_ADD", "register:40f0:8", ["const:bfaf24:8", "const:4:8"]]
- 00bfaf24 ["CALL", null, ["callee:00c57f20:8"]]
+ 00bfafc0 ["INT_ADD", "register:40f0:8", ["const:bfafc0:8", "const:4:8"]]
+ 00bfafc0 ["CALL", null, ["callee:00c57f20:8"]]
- 00bfaf24 bytes cb730194
+ 00bfafc0 bytes d8730194
- 00bfaf34 ["INT_ADD", "register:40f0:8", ["const:bfaf34:8", "const:4:8"]]
- 00bfaf34 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bfafd0 ["INT_ADD", "register:40f0:8", ["const:bfafd0:8", "const:4:8"]]
+ 00bfafd0 ["CALL", null, ["callee:00c57f40:8"]]
- 00bfaf34 bytes cf730194
+ 00bfafd0 bytes dc730194
- 00bfaefc ["COPY", "tmp:0:8", ["const:390:8"]]
- 00bfaefc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bfaefc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bfaefc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bfaf98 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 00bfaf98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bfaf98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bfaf98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bfaefc bytes 08410e91
+ 00bfaf98 bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c42d0e1dd860fcdc00ae9f7f8a692f23"></a>

### [`00bfb0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb0f4.md) → [`00bfb190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb190.md) _ZNSt6__ndk18ios_base6xallocEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb1a4",
      "incomplete_value": true,
      "site": "00bfb1a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb108",
      "incomplete_value": true,
      "site": "00bfb10c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af8:8"
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
      "00bfb1a4",
      "READ",
      [
        "storage",
        "00c9baf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb1a4",
      "PARAM",
      [
        "storage",
        "01127398",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bfb1a4",
      "READ",
      [
        "storage",
        "00c9bbc8",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb1a4",
      "PARAM",
      [
        "storage",
        "01127498",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb0f4.md#insn-00bfb10c) · [`00bfb108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb0f4.md#insn-00bfb108)
- 新版 [`00bfb1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb190.md#insn-00bfb1a8) · [`00bfb1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb190.md#insn-00bfb1a4)

~~~diff
- 00bfb10c ["INT_ADD", "register:40f0:8", ["const:bfb10c:8", "const:4:8"]]
- 00bfb10c ["CALL", null, ["callee:00c53d40:8"]]
+ 00bfb1a8 ["INT_ADD", "register:40f0:8", ["const:bfb1a8:8", "const:4:8"]]
+ 00bfb1a8 ["CALL", null, ["callee:00c53d40:8"]]
- 00bfb10c bytes e5620194
+ 00bfb1a8 bytes e6620194
- 00bfb108 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:af8:8"]]
- 00bfb108 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfb1a4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:bc8:8"]]
+ 00bfb1a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfb108 bytes 217c45f9
+ 00bfb1a4 bytes 21e445f9
~~~


<a id="compare-6b96fe531e964aecce228a8e329b0f78"></a>

### [`00bfb11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb11c.md) → [`00bfb1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb1b8.md) _ZNSt6__ndk18ios_base5iwordEi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bfb544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bfb5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5e0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfb2b8",
      "incomplete_value": false,
      "site": "00bfb2b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb21c",
      "incomplete_value": false,
      "site": "00bfb21c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb2c4",
      "incomplete_value": false,
      "site": "00bfb2c8",
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
            "const:4da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb228",
      "incomplete_value": false,
      "site": "00bfb22c",
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
            "const:536:8"
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
      "00bfb2b4",
      "DATA",
      [
        "storage",
        "011273a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb2b8",
      "WRITE",
      [
        "storage",
        "011273a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb2c4",
      "PARAM",
      [
        "storage",
        "002a7536",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb2b4",
      "DATA",
      [
        "storage",
        "011274a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb2b8",
      "WRITE",
      [
        "storage",
        "011274a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb2c4",
      "PARAM",
      [
        "storage",
        "002a74da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb11c.md#insn-00bfb22c) · [`00bfb174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb11c.md#insn-00bfb174) · [`00bfb1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb11c.md#insn-00bfb1c4)
- 新版 [`00bfb2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb1b8.md#insn-00bfb2c8) · [`00bfb210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb1b8.md#insn-00bfb210) · [`00bfb260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb1b8.md#insn-00bfb260)

~~~diff
- 00bfb22c ["INT_ADD", "register:40f0:8", ["const:bfb22c:8", "const:4:8"]]
- 00bfb22c ["CALL", null, ["callee:00bfb5e0:8"]]
+ 00bfb2c8 ["INT_ADD", "register:40f0:8", ["const:bfb2c8:8", "const:4:8"]]
+ 00bfb2c8 ["CALL", null, ["callee:00bfb5e0:8"]]
- 00bfb22c bytes c6000094
+ 00bfb2c8 bytes c6000094
- 00bfb174 ["INT_ADD", "register:40f0:8", ["const:bfb174:8", "const:4:8"]]
- 00bfb174 ["CALL", null, ["callee:00c5a170:8"]]
+ 00bfb210 ["INT_ADD", "register:40f0:8", ["const:bfb210:8", "const:4:8"]]
+ 00bfb210 ["CALL", null, ["callee:00c5a170:8"]]
- 00bfb174 bytes cb7b0194
+ 00bfb210 bytes d87b0194
- 00bfb1c4 ["INT_ADD", "register:40f0:8", ["const:bfb1c4:8", "const:4:8"]]
- 00bfb1c4 ["CALL", null, ["callee:00c58160:8"]]
+ 00bfb260 ["INT_ADD", "register:40f0:8", ["const:bfb260:8", "const:4:8"]]
+ 00bfb260 ["CALL", null, ["callee:00c58160:8"]]
- 00bfb1c4 bytes b3730194
+ 00bfb260 bytes c0730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00d986ea682c9ef189e1b5fbdde1cfe8"></a>

### [`00bfb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb230.md) → [`00bfb2cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb2cc.md) _ZNSt6__ndk18ios_base5pwordEi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bfb544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bfb5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5e0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfb3cc",
      "incomplete_value": false,
      "site": "00bfb3cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb330",
      "incomplete_value": false,
      "site": "00bfb330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb3d8",
      "incomplete_value": false,
      "site": "00bfb3dc",
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
            "const:4da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb33c",
      "incomplete_value": false,
      "site": "00bfb340",
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
            "const:536:8"
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
      "00bfb3c8",
      "DATA",
      [
        "storage",
        "011273a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb3cc",
      "WRITE",
      [
        "storage",
        "011273a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb3d8",
      "PARAM",
      [
        "storage",
        "002a7536",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb3c8",
      "DATA",
      [
        "storage",
        "011274a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb3cc",
      "WRITE",
      [
        "storage",
        "011274a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb3d8",
      "PARAM",
      [
        "storage",
        "002a74da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb230.md#insn-00bfb340) · [`00bfb288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb230.md#insn-00bfb288) · [`00bfb2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb230.md#insn-00bfb2d8)
- 新版 [`00bfb3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb2cc.md#insn-00bfb3dc) · [`00bfb324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb2cc.md#insn-00bfb324) · [`00bfb374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb2cc.md#insn-00bfb374)

~~~diff
- 00bfb340 ["INT_ADD", "register:40f0:8", ["const:bfb340:8", "const:4:8"]]
- 00bfb340 ["CALL", null, ["callee:00bfb5e0:8"]]
+ 00bfb3dc ["INT_ADD", "register:40f0:8", ["const:bfb3dc:8", "const:4:8"]]
+ 00bfb3dc ["CALL", null, ["callee:00bfb5e0:8"]]
- 00bfb340 bytes 81000094
+ 00bfb3dc bytes 81000094
- 00bfb288 ["INT_ADD", "register:40f0:8", ["const:bfb288:8", "const:4:8"]]
- 00bfb288 ["CALL", null, ["callee:00c5a170:8"]]
+ 00bfb324 ["INT_ADD", "register:40f0:8", ["const:bfb324:8", "const:4:8"]]
+ 00bfb324 ["CALL", null, ["callee:00c5a170:8"]]
- 00bfb288 bytes 867b0194
+ 00bfb324 bytes 937b0194
- 00bfb2d8 ["INT_ADD", "register:40f0:8", ["const:bfb2d8:8", "const:4:8"]]
- 00bfb2d8 ["CALL", null, ["callee:00c58160:8"]]
+ 00bfb374 ["INT_ADD", "register:40f0:8", ["const:bfb374:8", "const:4:8"]]
+ 00bfb374 ["CALL", null, ["callee:00c58160:8"]]
- 00bfb2d8 bytes 6e730194
+ 00bfb374 bytes 7b730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37d662e24eae26dc5e13d03938880431"></a>

### [`00bfb344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb344.md) → [`00bfb3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb3e0.md) _ZNSt6__ndk18ios_base17register_callbackEPFvNS0_5eventERS0_iEi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bfb544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bfb5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb4b8",
      "incomplete_value": false,
      "site": "00bfb4bc",
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
            "const:4da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb41c",
      "incomplete_value": false,
      "site": "00bfb420",
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
            "const:536:8"
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
      "00bfb4b8",
      "PARAM",
      [
        "storage",
        "002a7536",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb4b8",
      "PARAM",
      [
        "storage",
        "002a74da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb344.md#insn-00bfb420) · [`00bfb398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb344.md#insn-00bfb398) · [`00bfb3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb344.md#insn-00bfb3c4)
- 新版 [`00bfb4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb3e0.md#insn-00bfb4bc) · [`00bfb434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb3e0.md#insn-00bfb434) · [`00bfb460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb3e0.md#insn-00bfb460)

~~~diff
- 00bfb420 ["INT_ADD", "register:40f0:8", ["const:bfb420:8", "const:4:8"]]
- 00bfb420 ["CALL", null, ["callee:00bfb5e0:8"]]
+ 00bfb4bc ["INT_ADD", "register:40f0:8", ["const:bfb4bc:8", "const:4:8"]]
+ 00bfb4bc ["CALL", null, ["callee:00bfb5e0:8"]]
- 00bfb420 bytes 49000094
+ 00bfb4bc bytes 49000094
- 00bfb398 ["INT_ADD", "register:40f0:8", ["const:bfb398:8", "const:4:8"]]
- 00bfb398 ["CALL", null, ["callee:00c5a170:8"]]
+ 00bfb434 ["INT_ADD", "register:40f0:8", ["const:bfb434:8", "const:4:8"]]
+ 00bfb434 ["CALL", null, ["callee:00c5a170:8"]]
- 00bfb398 bytes 427b0194
+ 00bfb434 bytes 4f7b0194
- 00bfb3c4 ["INT_ADD", "register:40f0:8", ["const:bfb3c4:8", "const:4:8"]]
- 00bfb3c4 ["CALL", null, ["callee:00c5a170:8"]]
+ 00bfb460 ["INT_ADD", "register:40f0:8", ["const:bfb460:8", "const:4:8"]]
+ 00bfb460 ["CALL", null, ["callee:00c5a170:8"]]
- 00bfb3c4 bytes 377b0194
+ 00bfb460 bytes 447b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f6c885924fffadf250823277f66cf87"></a>

### [`00bfb424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb424.md) → [`00bfb4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb4c0.md) _ZNSt6__ndk18ios_baseD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5e2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2f0.md) · 呼出先 2件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 2件 [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md) [`00c5e3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3c0.md) · 呼出先 2件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfb4e4",
      "incomplete_value": true,
      "site": "00bfb4e8",
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
      "definition_site": "00bfb448",
      "incomplete_value": true,
      "site": "00bfb44c",
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
      "00bfb4dc",
      "READ",
      [
        "storage",
        "00c9bb00",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb4e8",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00bfb4dc",
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb4e8",
      "DATA",
      [
        "storage",
        "00c92e78",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb424.md#insn-00bfb440) · [`00bfb478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb424.md#insn-00bfb478) · [`00bfb48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb424.md#insn-00bfb48c)
- 新版 [`00bfb4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb4c0.md#insn-00bfb4dc) · [`00bfb514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb4c0.md#insn-00bfb514) · [`00bfb528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb4c0.md#insn-00bfb528)

~~~diff
- 00bfb440 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b00:8"]]
- 00bfb440 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfb4dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd0:8"]]
+ 00bfb4dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfb440 bytes 088145f9
+ 00bfb4dc bytes 08e945f9
- 00bfb478 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfb478 ["INT_ADD", "register:40f0:8", ["const:bfb478:8", "const:4:8"]]
- 00bfb478 ["CALLIND", null, ["register:0:8"]]
+ 00bfb514 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfb514 ["INT_ADD", "register:40f0:8", ["const:bfb514:8", "const:4:8"]]
+ 00bfb514 ["CALLIND", null, ["register:0:8"]]
- 00bfb478 bytes 00013fd6
+ 00bfb514 bytes 00013fd6
- 00bfb48c ["INT_ADD", "register:40f0:8", ["const:bfb48c:8", "const:4:8"]]
- 00bfb48c ["CALL", null, ["callee:00c58360:8"]]
+ 00bfb528 ["INT_ADD", "register:40f0:8", ["const:bfb528:8", "const:4:8"]]
+ 00bfb528 ["CALL", null, ["callee:00c58360:8"]]
- 00bfb48c bytes 81730194
+ 00bfb528 bytes 8e730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4962e26f2508238c9bc3d6ae7817647"></a>

### [`00bfb504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb504.md) → [`00bfb5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5a0.md) _ZNSt6__ndk18ios_base5clearEj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) · 呼出先 1件 [`00bfb544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md)
- 新版 呼出元 1件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) · 呼出先 1件 [`00bfb5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb5d8",
      "incomplete_value": false,
      "site": "00bfb5dc",
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
            "const:4da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb53c",
      "incomplete_value": false,
      "site": "00bfb540",
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
            "const:536:8"
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
      "00bfb5d8",
      "PARAM",
      [
        "storage",
        "002a7536",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb5d8",
      "PARAM",
      [
        "storage",
        "002a74da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb504.md#insn-00bfb540) · [`00bfb53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb504.md#insn-00bfb53c)
- 新版 [`00bfb5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5a0.md#insn-00bfb5dc) · [`00bfb5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5a0.md#insn-00bfb5d8)

~~~diff
- 00bfb540 ["INT_ADD", "register:40f0:8", ["const:bfb540:8", "const:4:8"]]
- 00bfb540 ["CALL", null, ["callee:00bfb5e0:8"]]
+ 00bfb5dc ["INT_ADD", "register:40f0:8", ["const:bfb5dc:8", "const:4:8"]]
+ 00bfb5dc ["CALL", null, ["callee:00bfb5e0:8"]]
- 00bfb540 bytes 01000094
+ 00bfb5dc bytes 01000094
- 00bfb53c ["COPY", "tmp:0:8", ["const:536:8"]]
- 00bfb53c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bfb53c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bfb53c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bfb5d8 ["COPY", "tmp:0:8", ["const:4da:8"]]
+ 00bfb5d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfb5d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfb5d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bfb53c bytes 00d81491
+ 00bfb5d8 bytes 00681391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df26aa8e3d485ec550a83a5cb801e0de"></a>

### [`00bfb544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md) → [`00bfb5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5e0.md) FUN_00bfb5e0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00bfb11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb11c.md) [`00bfb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb230.md) [`00bfb344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb344.md) [`00bfb504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb504.md) · 呼出先 6件 [`00bfafbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfafbc.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 4件 [`00bfb1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb1b8.md) [`00bfb2cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb2cc.md) [`00bfb3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb3e0.md) [`00bfb5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5a0.md) · 呼出先 6件 [`00bfb058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb058.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfb620",
      "incomplete_value": false,
      "site": "00bfb620",
      "value": [
        "leaf",
        "const:ca48d0:8"
      ]
    },
    "old": {
      "definition_site": "00bfb584",
      "incomplete_value": false,
      "site": "00bfb584",
      "value": [
        "leaf",
        "const:ca4800:8"
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb640",
      "incomplete_value": true,
      "site": "00bfb648",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb5a4",
      "incomplete_value": true,
      "site": "00bfb5ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b08:8"
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
      "definition_site": "00bfb644",
      "incomplete_value": true,
      "site": "00bfb648",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb5a8",
      "incomplete_value": true,
      "site": "00bfb5ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bfb60c",
      "READ",
      [
        "storage",
        "01127390",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfb620",
      "DATA",
      [
        "storage",
        "00ca4800",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb640",
      "READ",
      [
        "storage",
        "00c9bb08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfb60c",
      "READ",
      [
        "storage",
        "01127490",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfb620",
      "DATA",
      [
        "storage",
        "00ca48d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb640",
      "READ",
      [
        "storage",
        "00c9bbd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md#insn-00bfb5ac) · [`00bfb5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md#insn-00bfb5b8) · [`00bfb5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md#insn-00bfb5c8)
- 新版 [`00bfb648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5e0.md#insn-00bfb648) · [`00bfb654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5e0.md#insn-00bfb654) · [`00bfb664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb5e0.md#insn-00bfb664)

~~~diff
- 00bfb5ac ["INT_ADD", "register:40f0:8", ["const:bfb5ac:8", "const:4:8"]]
- 00bfb5ac ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bfb648 ["INT_ADD", "register:40f0:8", ["const:bfb648:8", "const:4:8"]]
+ 00bfb648 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bfb5ac bytes 59720194
+ 00bfb648 bytes 66720194
- 00bfb5b8 ["INT_ADD", "register:40f0:8", ["const:bfb5b8:8", "const:4:8"]]
- 00bfb5b8 ["CALL", null, ["callee:00c57f20:8"]]
+ 00bfb654 ["INT_ADD", "register:40f0:8", ["const:bfb654:8", "const:4:8"]]
+ 00bfb654 ["CALL", null, ["callee:00c57f20:8"]]
- 00bfb5b8 bytes 26720194
+ 00bfb654 bytes 33720194
- 00bfb5c8 ["INT_ADD", "register:40f0:8", ["const:bfb5c8:8", "const:4:8"]]
- 00bfb5c8 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bfb664 ["INT_ADD", "register:40f0:8", ["const:bfb664:8", "const:4:8"]]
+ 00bfb664 ["CALL", null, ["callee:00c57f40:8"]]
- 00bfb5c8 bytes 2a720194
+ 00bfb664 bytes 37720194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0a92beea055eecbdfea97191fc96690"></a>

### [`00bfb5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb5e4.md) → [`00bfb680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb680.md) _ZNSt6__ndk18ios_base4initEPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) · 呼出先 1件 [`00c5a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md)
- 新版 呼出元 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) · 呼出先 1件 [`00c5a870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a870.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfb690",
      "incomplete_value": true,
      "site": "00bfb6a4",
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
                "const:70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb5f4",
      "incomplete_value": true,
      "site": "00bfb608",
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
                "const:30:8"
              ]
            ]
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
      "00bfb690",
      "READ",
      [
        "storage",
        "002c3030",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfb690",
      "READ",
      [
        "storage",
        "002c3070",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb5e4.md#insn-00bfb5f4)
- 新版 [`00bfb690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb680.md#insn-00bfb690)

~~~diff
- 00bfb5f4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 00bfb5f4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00bfb5f4 ["COPY", "register:5010:8", ["const:0:8"]]
- 00bfb5f4 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00bfb690 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:70:8"]]
+ 00bfb690 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bfb690 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00bfb690 ["COPY", "register:5018:8", ["const:0:8"]]
- 00bfb5f4 bytes 200dc03d
+ 00bfb690 bytes 201dc03d
~~~


<a id="compare-65d3b15066248a961a09571b62729782"></a>

### [`00bfbb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb00.md) → [`00bfbb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbb9c.md) _ZNSt6__ndk18ios_base15sync_with_stdioEb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfbbac",
      "incomplete_value": false,
      "site": "00bfbbac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfbb10",
      "incomplete_value": false,
      "site": "00bfbb10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:808:8"
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
      "00bfbba8",
      "READ",
      [
        "storage",
        "00ca4808",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfbbac",
      "WRITE",
      [
        "storage",
        "00ca4808",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bfbba8",
      "READ",
      [
        "storage",
        "00ca48d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfbbac",
      "WRITE",
      [
        "storage",
        "00ca48d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfbb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb00.md#insn-00bfbb10) · [`00bfbb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb00.md#insn-00bfbb0c)
- 新版 [`00bfbbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbb9c.md#insn-00bfbbac) · [`00bfbba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbb9c.md#insn-00bfbba8)

~~~diff
- 00bfbb10 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bfbb10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "const:808:8"]]
- 00bfbb10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bfbbac ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bfbbac ["INT_ADD", "tmp:1:8", ["register:4050:8", "const:8d8:8"]]
+ 00bfbbac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bfbb10 bytes 49212039
+ 00bfbbac bytes 49612339
- 00bfbb0c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:808:8"]]
- 00bfbb0c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bfbb0c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bfbba8 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:8d8:8"]]
+ 00bfbba8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bfbba8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bfbb0c bytes 48216039
+ 00bfbba8 bytes 48616339
~~~


<a id="compare-76ea7feb27f77378ee4b0c96c29496a5"></a>

### [`00bfbe9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbe9c.md) → [`00bfbf38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbf38.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c581f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581f0.md) · 呼出先 1件 [`00c5a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md)
- 新版 呼出元 1件 [`00c582c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582c0.md) · 呼出先 1件 [`00c5a870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a870.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfbf58",
      "incomplete_value": true,
      "site": "00bfbf58",
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
      "definition_site": "00bfbebc",
      "incomplete_value": true,
      "site": "00bfbebc",
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
      "00bfbf50",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbf58",
      "DATA",
      [
        "storage",
        "00c90cb0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00bfbf50",
      "READ",
      [
        "storage",
        "00c9b918",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbf58",
      "DATA",
      [
        "storage",
        "00c90d80",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfbeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbe9c.md#insn-00bfbeb4) · [`00bfbec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbe9c.md#insn-00bfbec0)
- 新版 [`00bfbf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbf38.md#insn-00bfbf50) · [`00bfbf5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbf38.md#insn-00bfbf5c)

~~~diff
- 00bfbeb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:848:8"]]
- 00bfbeb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfbf50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:918:8"]]
+ 00bfbf50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfbeb4 bytes 082544f9
+ 00bfbf50 bytes 088d44f9
- 00bfbec0 ["INT_ADD", "register:40f0:8", ["const:bfbec0:8", "const:4:8"]]
- 00bfbec0 ["CALL", null, ["callee:00c5a870:8"]]
+ 00bfbf5c ["INT_ADD", "register:40f0:8", ["const:bfbf5c:8", "const:4:8"]]
+ 00bfbf5c ["CALL", null, ["callee:00c5a870:8"]]
- 00bfbec0 bytes 387a0194
+ 00bfbf5c bytes 457a0194
~~~


<a id="compare-e597a5f3252055756429407e03f8cbbe"></a>

### [`00bfbee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbee0.md) → [`00bfbf7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbf7c.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1ERKS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfbfa4",
      "incomplete_value": true,
      "site": "00bfbfa4",
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
      "definition_site": "00bfbf08",
      "incomplete_value": true,
      "site": "00bfbf08",
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
      "00bfbf98",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbfa4",
      "DATA",
      [
        "storage",
        "00c90cb0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00bfbf98",
      "READ",
      [
        "storage",
        "00c9b918",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbfa4",
      "DATA",
      [
        "storage",
        "00c90d80",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfbefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbee0.md#insn-00bfbefc) · [`00bfbf0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbee0.md#insn-00bfbf0c)
- 新版 [`00bfbf98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbf7c.md#insn-00bfbf98) · [`00bfbfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbf7c.md#insn-00bfbfa8)

~~~diff
- 00bfbefc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:848:8"]]
- 00bfbefc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfbf98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:918:8"]]
+ 00bfbf98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfbefc bytes 082544f9
+ 00bfbf98 bytes 088d44f9
- 00bfbf0c ["INT_ADD", "register:40f0:8", ["const:bfbf0c:8", "const:4:8"]]
- 00bfbf0c ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bfbfa8 ["INT_ADD", "register:40f0:8", ["const:bfbfa8:8", "const:4:8"]]
+ 00bfbfa8 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bfbf0c bytes 317a0194
+ 00bfbfa8 bytes 3e7a0194
~~~


<a id="compare-696742448d3680a33ecc34f4356f9b24"></a>

### [`00bfc0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc0e8.md) → [`00bfc184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc184.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfc1b0",
      "incomplete_value": true,
      "site": "00bfc1b0",
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
      "definition_site": "00bfc114",
      "incomplete_value": true,
      "site": "00bfc114",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfc1b4",
      "incomplete_value": true,
      "site": "00bfc1b4",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfc118",
      "incomplete_value": true,
      "site": "00bfc118",
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
            "const:18:8"
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
      "00bfc1a0",
      "READ",
      [
        "storage",
        "00c9b230",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc1b0",
      "DATA",
      [
        "storage",
        "00c92e38",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc1b4",
      "DATA",
      [
        "storage",
        "00c92e10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfc1a0",
      "READ",
      [
        "storage",
        "00c9b300",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc1b0",
      "DATA",
      [
        "storage",
        "00c92f08",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc1b4",
      "DATA",
      [
        "storage",
        "00c92ee0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc0e8.md#insn-00bfc104) · [`00bfc120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc0e8.md#insn-00bfc120)
- 新版 [`00bfc1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc184.md#insn-00bfc1a0) · [`00bfc1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc184.md#insn-00bfc1bc)

~~~diff
- 00bfc104 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:230:8"]]
- 00bfc104 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfc1a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:300:8"]]
+ 00bfc1a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfc104 bytes 081941f9
+ 00bfc1a0 bytes 088141f9
- 00bfc120 ["INT_ADD", "register:40f0:8", ["const:bfc120:8", "const:4:8"]]
- 00bfc120 ["CALL", null, ["callee:00c582b0:8"]]
+ 00bfc1bc ["INT_ADD", "register:40f0:8", ["const:bfc1bc:8", "const:4:8"]]
+ 00bfc1bc ["CALL", null, ["callee:00c582b0:8"]]
- 00bfc120 bytes 30700194
+ 00bfc1bc bytes 3d700194
~~~


<a id="compare-f813ebfcc5d1ad7d3b8c3a4626db83c8"></a>

### [`00bfc1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc1c8.md) → [`00bfc264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc264.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c58ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ef0.md)
- 新版 呼出元 1件 [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md) · 呼出先 5件 [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc2f4",
      "incomplete_value": true,
      "site": "00bfc2f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
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
    "old": {
      "definition_site": "00bfc258",
      "incomplete_value": true,
      "site": "00bfc25c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:c30:8"
              ]
            ]
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
      "00bfc2f4",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc2f4",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc2f4",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc2f4",
      "PARAM",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc1c8.md#insn-00bfc25c) · [`00bfc228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc1c8.md#insn-00bfc228) · [`00bfc24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc1c8.md#insn-00bfc24c)
- 新版 [`00bfc2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc264.md#insn-00bfc2f8) · [`00bfc2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc264.md#insn-00bfc2c4) · [`00bfc2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc264.md#insn-00bfc2e8)

~~~diff
- 00bfc25c ["INT_ADD", "register:40f0:8", ["const:bfc25c:8", "const:4:8"]]
- 00bfc25c ["CALL", null, ["callee:00c58350:8"]]
+ 00bfc2f8 ["INT_ADD", "register:40f0:8", ["const:bfc2f8:8", "const:4:8"]]
+ 00bfc2f8 ["CALL", null, ["callee:00c58350:8"]]
- 00bfc25c bytes 09700194
+ 00bfc2f8 bytes 16700194
- 00bfc228 ["INT_ADD", "register:40f0:8", ["const:bfc228:8", "const:4:8"]]
- 00bfc228 ["CALL", null, ["callee:00c58fc0:8"]]
+ 00bfc2c4 ["INT_ADD", "register:40f0:8", ["const:bfc2c4:8", "const:4:8"]]
+ 00bfc2c4 ["CALL", null, ["callee:00c58fc0:8"]]
- 00bfc228 bytes 32730194
+ 00bfc2c4 bytes 3f730194
- 00bfc24c ["INT_ADD", "register:40f0:8", ["const:bfc24c:8", "const:4:8"]]
- 00bfc24c ["CALL", null, ["callee:00c58340:8"]]
+ 00bfc2e8 ["INT_ADD", "register:40f0:8", ["const:bfc2e8:8", "const:4:8"]]
+ 00bfc2e8 ["CALL", null, ["callee:00c58340:8"]]
- 00bfc24c bytes 09700194
+ 00bfc2e8 bytes 16700194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd3cbd59cb231d09f53034dac7136336"></a>

### [`00bfc5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc5d8.md) → [`00bfc674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc674.md) FUN_00bfc674

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfc5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc5d0.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00bfc66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc66c.md) · 呼出先 5件 [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc6c8",
      "incomplete_value": true,
      "site": "00bfc6cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfc62c",
      "incomplete_value": true,
      "site": "00bfc630",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
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
      "00bfc6c8",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc6c8",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc6c8",
      "READ",
      [
        "storage",
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc6c8",
      "PARAM",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc5d8.md#insn-00bfc630) · [`00bfc604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc5d8.md#insn-00bfc604) · [`00bfc620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc5d8.md#insn-00bfc620)
- 新版 [`00bfc6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc674.md#insn-00bfc6cc) · [`00bfc6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc674.md#insn-00bfc6a0) · [`00bfc6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc674.md#insn-00bfc6bc)

~~~diff
- 00bfc630 ["INT_ADD", "register:40f0:8", ["const:bfc630:8", "const:4:8"]]
- 00bfc630 ["CALL", null, ["callee:00c58350:8"]]
+ 00bfc6cc ["INT_ADD", "register:40f0:8", ["const:bfc6cc:8", "const:4:8"]]
+ 00bfc6cc ["CALL", null, ["callee:00c58350:8"]]
- 00bfc630 bytes 146f0194
+ 00bfc6cc bytes 216f0194
- 00bfc604 ["INT_ADD", "register:40f0:8", ["const:bfc604:8", "const:4:8"]]
- 00bfc604 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfc6a0 ["INT_ADD", "register:40f0:8", ["const:bfc6a0:8", "const:4:8"]]
+ 00bfc6a0 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfc604 bytes f3750194
+ 00bfc6a0 bytes 00760194
- 00bfc620 ["INT_ADD", "register:40f0:8", ["const:bfc620:8", "const:4:8"]]
- 00bfc620 ["CALL", null, ["callee:00c58340:8"]]
+ 00bfc6bc ["INT_ADD", "register:40f0:8", ["const:bfc6bc:8", "const:4:8"]]
+ 00bfc6bc ["CALL", null, ["callee:00c58340:8"]]
- 00bfc620 bytes 146f0194
+ 00bfc6bc bytes 216f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f43a8d005cfa4ebaf90c0ce52d8192ec"></a>

### [`00bfc710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc710.md) → [`00bfc7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc7ac.md) FUN_00bfc7ac

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfc708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc708.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00bfc7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc7a4.md) · 呼出先 5件 [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.44% / 新版 98.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc800",
      "incomplete_value": true,
      "site": "00bfc804",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfc764",
      "incomplete_value": true,
      "site": "00bfc768",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
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
      "00bfc800",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc800",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc800",
      "READ",
      [
        "storage",
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc800",
      "PARAM",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc710.md#insn-00bfc768) · [`00bfc73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc710.md#insn-00bfc73c) · [`00bfc758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc710.md#insn-00bfc758)
- 新版 [`00bfc804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc7ac.md#insn-00bfc804) · [`00bfc7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc7ac.md#insn-00bfc7d8) · [`00bfc7f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc7ac.md#insn-00bfc7f4)

~~~diff
- 00bfc768 ["INT_ADD", "register:40f0:8", ["const:bfc768:8", "const:4:8"]]
- 00bfc768 ["CALL", null, ["callee:00c58350:8"]]
+ 00bfc804 ["INT_ADD", "register:40f0:8", ["const:bfc804:8", "const:4:8"]]
+ 00bfc804 ["CALL", null, ["callee:00c58350:8"]]
- 00bfc768 bytes c66e0194
+ 00bfc804 bytes d36e0194
- 00bfc73c ["INT_ADD", "register:40f0:8", ["const:bfc73c:8", "const:4:8"]]
- 00bfc73c ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfc7d8 ["INT_ADD", "register:40f0:8", ["const:bfc7d8:8", "const:4:8"]]
+ 00bfc7d8 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfc73c bytes a5750194
+ 00bfc7d8 bytes b2750194
- 00bfc758 ["INT_ADD", "register:40f0:8", ["const:bfc758:8", "const:4:8"]]
- 00bfc758 ["CALL", null, ["callee:00c58340:8"]]
+ 00bfc7f4 ["INT_ADD", "register:40f0:8", ["const:bfc7f4:8", "const:4:8"]]
+ 00bfc7f4 ["CALL", null, ["callee:00c58340:8"]]
- 00bfc758 bytes c66e0194
+ 00bfc7f4 bytes d36e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bd241fe3d3d68c30fb8e6631da2f22b"></a>

### [`00bfc888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc888.md) → [`00bfc924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc924.md) FUN_00bfc924

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfc880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc880.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00bfc91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc91c.md) · 呼出先 5件 [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc978",
      "incomplete_value": true,
      "site": "00bfc97c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfc8dc",
      "incomplete_value": true,
      "site": "00bfc8e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
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
      "00bfc978",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc978",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc978",
      "READ",
      [
        "storage",
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc978",
      "PARAM",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc888.md#insn-00bfc8e0) · [`00bfc8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc888.md#insn-00bfc8b4) · [`00bfc8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc888.md#insn-00bfc8d0)
- 新版 [`00bfc97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc924.md#insn-00bfc97c) · [`00bfc950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc924.md#insn-00bfc950) · [`00bfc96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc924.md#insn-00bfc96c)

~~~diff
- 00bfc8e0 ["INT_ADD", "register:40f0:8", ["const:bfc8e0:8", "const:4:8"]]
- 00bfc8e0 ["CALL", null, ["callee:00c58350:8"]]
+ 00bfc97c ["INT_ADD", "register:40f0:8", ["const:bfc97c:8", "const:4:8"]]
+ 00bfc97c ["CALL", null, ["callee:00c58350:8"]]
- 00bfc8e0 bytes 686e0194
+ 00bfc97c bytes 756e0194
- 00bfc8b4 ["INT_ADD", "register:40f0:8", ["const:bfc8b4:8", "const:4:8"]]
- 00bfc8b4 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfc950 ["INT_ADD", "register:40f0:8", ["const:bfc950:8", "const:4:8"]]
+ 00bfc950 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfc8b4 bytes 47750194
+ 00bfc950 bytes 54750194
- 00bfc8d0 ["INT_ADD", "register:40f0:8", ["const:bfc8d0:8", "const:4:8"]]
- 00bfc8d0 ["CALL", null, ["callee:00c58340:8"]]
+ 00bfc96c ["INT_ADD", "register:40f0:8", ["const:bfc96c:8", "const:4:8"]]
+ 00bfc96c ["CALL", null, ["callee:00c58340:8"]]
- 00bfc8d0 bytes 686e0194
+ 00bfc96c bytes 756e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35b16e94d3d1f909cea4456b2fe402f4"></a>

### [`00bfc9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc9c0.md) → [`00bfca5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfca5c.md) FUN_00bfca5c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfc9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc9b8.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00bfca54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfca54.md) · 呼出先 5件 [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfcab0",
      "incomplete_value": true,
      "site": "00bfcab4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfca14",
      "incomplete_value": true,
      "site": "00bfca18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
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
      "00bfcab0",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcab0",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfcab0",
      "READ",
      [
        "storage",
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcab0",
      "PARAM",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfca18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc9c0.md#insn-00bfca18) · [`00bfc9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc9c0.md#insn-00bfc9ec) · [`00bfca08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc9c0.md#insn-00bfca08)
- 新版 [`00bfcab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfca5c.md#insn-00bfcab4) · [`00bfca88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfca5c.md#insn-00bfca88) · [`00bfcaa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfca5c.md#insn-00bfcaa4)

~~~diff
- 00bfca18 ["INT_ADD", "register:40f0:8", ["const:bfca18:8", "const:4:8"]]
- 00bfca18 ["CALL", null, ["callee:00c58350:8"]]
+ 00bfcab4 ["INT_ADD", "register:40f0:8", ["const:bfcab4:8", "const:4:8"]]
+ 00bfcab4 ["CALL", null, ["callee:00c58350:8"]]
- 00bfca18 bytes 1a6e0194
+ 00bfcab4 bytes 276e0194
- 00bfc9ec ["INT_ADD", "register:40f0:8", ["const:bfc9ec:8", "const:4:8"]]
- 00bfc9ec ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfca88 ["INT_ADD", "register:40f0:8", ["const:bfca88:8", "const:4:8"]]
+ 00bfca88 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfc9ec bytes f9740194
+ 00bfca88 bytes 06750194
- 00bfca08 ["INT_ADD", "register:40f0:8", ["const:bfca08:8", "const:4:8"]]
- 00bfca08 ["CALL", null, ["callee:00c58340:8"]]
+ 00bfcaa4 ["INT_ADD", "register:40f0:8", ["const:bfcaa4:8", "const:4:8"]]
+ 00bfcaa4 ["CALL", null, ["callee:00c58340:8"]]
- 00bfca08 bytes 1a6e0194
+ 00bfcaa4 bytes 276e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e95aed9031f95399bbf68f33879725e"></a>

### [`00bfcb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcb3c.md) → [`00bfcbd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcbd8.md) FUN_00bfcbd8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfcb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcb34.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00bfcbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcbd0.md) · 呼出先 5件 [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfcc2c",
      "incomplete_value": true,
      "site": "00bfcc30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfcb90",
      "incomplete_value": true,
      "site": "00bfcb94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
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
      "00bfcc2c",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcc2c",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfcc2c",
      "READ",
      [
        "storage",
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcc2c",
      "PARAM",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfcb94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcb3c.md#insn-00bfcb94) · [`00bfcb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcb3c.md#insn-00bfcb68) · [`00bfcb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcb3c.md#insn-00bfcb84)
- 新版 [`00bfcc30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcbd8.md#insn-00bfcc30) · [`00bfcc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcbd8.md#insn-00bfcc04) · [`00bfcc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcbd8.md#insn-00bfcc20)

~~~diff
- 00bfcb94 ["INT_ADD", "register:40f0:8", ["const:bfcb94:8", "const:4:8"]]
- 00bfcb94 ["CALL", null, ["callee:00c58350:8"]]
+ 00bfcc30 ["INT_ADD", "register:40f0:8", ["const:bfcc30:8", "const:4:8"]]
+ 00bfcc30 ["CALL", null, ["callee:00c58350:8"]]
- 00bfcb94 bytes bb6d0194
+ 00bfcc30 bytes c86d0194
- 00bfcb68 ["INT_ADD", "register:40f0:8", ["const:bfcb68:8", "const:4:8"]]
- 00bfcb68 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfcc04 ["INT_ADD", "register:40f0:8", ["const:bfcc04:8", "const:4:8"]]
+ 00bfcc04 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfcb68 bytes 9a740194
+ 00bfcc04 bytes a7740194
- 00bfcb84 ["INT_ADD", "register:40f0:8", ["const:bfcb84:8", "const:4:8"]]
- 00bfcb84 ["CALL", null, ["callee:00c58340:8"]]
+ 00bfcc20 ["INT_ADD", "register:40f0:8", ["const:bfcc20:8", "const:4:8"]]
+ 00bfcc20 ["CALL", null, ["callee:00c58340:8"]]
- 00bfcb84 bytes bb6d0194
+ 00bfcc20 bytes c86d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb1a16dee1beff3bbe6f3e89c2aa4d19"></a>

### [`00bfcc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcc74.md) → [`00bfcd10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcd10.md) FUN_00bfcd10

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfcc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcc6c.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00bfcd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcd08.md) · 呼出先 5件 [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfcd64",
      "incomplete_value": true,
      "site": "00bfcd68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfccc8",
      "incomplete_value": true,
      "site": "00bfcccc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
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
      "00bfcd64",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcd64",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfcd64",
      "READ",
      [
        "storage",
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcd64",
      "PARAM",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfcccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcc74.md#insn-00bfcccc) · [`00bfcca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcc74.md#insn-00bfcca0) · [`00bfccbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcc74.md#insn-00bfccbc)
- 新版 [`00bfcd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcd10.md#insn-00bfcd68) · [`00bfcd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcd10.md#insn-00bfcd3c) · [`00bfcd58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcd10.md#insn-00bfcd58)

~~~diff
- 00bfcccc ["INT_ADD", "register:40f0:8", ["const:bfcccc:8", "const:4:8"]]
- 00bfcccc ["CALL", null, ["callee:00c58350:8"]]
+ 00bfcd68 ["INT_ADD", "register:40f0:8", ["const:bfcd68:8", "const:4:8"]]
+ 00bfcd68 ["CALL", null, ["callee:00c58350:8"]]
- 00bfcccc bytes 6d6d0194
+ 00bfcd68 bytes 7a6d0194
- 00bfcca0 ["INT_ADD", "register:40f0:8", ["const:bfcca0:8", "const:4:8"]]
- 00bfcca0 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfcd3c ["INT_ADD", "register:40f0:8", ["const:bfcd3c:8", "const:4:8"]]
+ 00bfcd3c ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfcca0 bytes 4c740194
+ 00bfcd3c bytes 59740194
- 00bfccbc ["INT_ADD", "register:40f0:8", ["const:bfccbc:8", "const:4:8"]]
- 00bfccbc ["CALL", null, ["callee:00c58340:8"]]
+ 00bfcd58 ["INT_ADD", "register:40f0:8", ["const:bfcd58:8", "const:4:8"]]
+ 00bfcd58 ["CALL", null, ["callee:00c58340:8"]]
- 00bfccbc bytes 6d6d0194
+ 00bfcd58 bytes 7a6d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09016db4153ca1af830adf8aa909d2d0"></a>

### [`00bfcdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcdac.md) → [`00bfce48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfce48.md) FUN_00bfce48

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfcda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcda4.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00bfce40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfce40.md) · 呼出先 5件 [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfce9c",
      "incomplete_value": true,
      "site": "00bfcea0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfce00",
      "incomplete_value": true,
      "site": "00bfce04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
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
      "00bfce9c",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfce9c",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfce9c",
      "READ",
      [
        "storage",
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfce9c",
      "PARAM",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfce04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcdac.md#insn-00bfce04) · [`00bfcdd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcdac.md#insn-00bfcdd8) · [`00bfcdf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcdac.md#insn-00bfcdf4)
- 新版 [`00bfcea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfce48.md#insn-00bfcea0) · [`00bfce74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfce48.md#insn-00bfce74) · [`00bfce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfce48.md#insn-00bfce90)

~~~diff
- 00bfce04 ["INT_ADD", "register:40f0:8", ["const:bfce04:8", "const:4:8"]]
- 00bfce04 ["CALL", null, ["callee:00c58350:8"]]
+ 00bfcea0 ["INT_ADD", "register:40f0:8", ["const:bfcea0:8", "const:4:8"]]
+ 00bfcea0 ["CALL", null, ["callee:00c58350:8"]]
- 00bfce04 bytes 1f6d0194
+ 00bfcea0 bytes 2c6d0194
- 00bfcdd8 ["INT_ADD", "register:40f0:8", ["const:bfcdd8:8", "const:4:8"]]
- 00bfcdd8 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfce74 ["INT_ADD", "register:40f0:8", ["const:bfce74:8", "const:4:8"]]
+ 00bfce74 ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfcdd8 bytes fe730194
+ 00bfce74 bytes 0b740194
- 00bfcdf4 ["INT_ADD", "register:40f0:8", ["const:bfcdf4:8", "const:4:8"]]
- 00bfcdf4 ["CALL", null, ["callee:00c58340:8"]]
+ 00bfce90 ["INT_ADD", "register:40f0:8", ["const:bfce90:8", "const:4:8"]]
+ 00bfce90 ["CALL", null, ["callee:00c58340:8"]]
- 00bfcdf4 bytes 1f6d0194
+ 00bfce90 bytes 2c6d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-917f6d727f497c1f693da4f96dcacaba"></a>

### [`00bfcee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcee4.md) → [`00bfcf80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcf80.md) FUN_00bfcf80

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfcedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcedc.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)
- 新版 呼出元 1件 [`00bfcf78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcf78.md) · 呼出先 5件 [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c59ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfcfd4",
      "incomplete_value": true,
      "site": "00bfcfd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfcf38",
      "incomplete_value": true,
      "site": "00bfcf3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
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
      "00bfcfd4",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcfd4",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfcfd4",
      "READ",
      [
        "storage",
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcfd4",
      "PARAM",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfcf3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcee4.md#insn-00bfcf3c) · [`00bfcf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcee4.md#insn-00bfcf10) · [`00bfcf2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcee4.md#insn-00bfcf2c)
- 新版 [`00bfcfd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcf80.md#insn-00bfcfd8) · [`00bfcfac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcf80.md#insn-00bfcfac) · [`00bfcfc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcf80.md#insn-00bfcfc8)

~~~diff
- 00bfcf3c ["INT_ADD", "register:40f0:8", ["const:bfcf3c:8", "const:4:8"]]
- 00bfcf3c ["CALL", null, ["callee:00c58350:8"]]
+ 00bfcfd8 ["INT_ADD", "register:40f0:8", ["const:bfcfd8:8", "const:4:8"]]
+ 00bfcfd8 ["CALL", null, ["callee:00c58350:8"]]
- 00bfcf3c bytes d16c0194
+ 00bfcfd8 bytes de6c0194
- 00bfcf10 ["INT_ADD", "register:40f0:8", ["const:bfcf10:8", "const:4:8"]]
- 00bfcf10 ["CALL", null, ["callee:00c59ea0:8"]]
+ 00bfcfac ["INT_ADD", "register:40f0:8", ["const:bfcfac:8", "const:4:8"]]
+ 00bfcfac ["CALL", null, ["callee:00c59ea0:8"]]
- 00bfcf10 bytes b0730194
+ 00bfcfac bytes bd730194
- 00bfcf2c ["INT_ADD", "register:40f0:8", ["const:bfcf2c:8", "const:4:8"]]
- 00bfcf2c ["CALL", null, ["callee:00c58340:8"]]
+ 00bfcfc8 ["INT_ADD", "register:40f0:8", ["const:bfcfc8:8", "const:4:8"]]
+ 00bfcfc8 ["CALL", null, ["callee:00c58340:8"]]
- 00bfcf2c bytes d16c0194
+ 00bfcfc8 bytes de6c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

