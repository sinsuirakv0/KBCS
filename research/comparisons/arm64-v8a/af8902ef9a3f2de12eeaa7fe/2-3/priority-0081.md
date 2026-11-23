# v16.0.0 → v16.0.1 · 最優先の変更候補 (81)

[一覧の目次](README.md)

<a id="compare-07f176c5b97ebd616ca1fd8695ee6e75"></a>

### [`00bc7a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7a5c.md) → [`00bc7e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7e84.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17GetConfigSettingsEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d350.md) · 呼出先 4件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 1件 [`00c5d750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d750.md) · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

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
    "old": {
      "definition_site": "00bc7a84",
      "incomplete_value": true,
      "site": "00bc7a8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:100:8"
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
    "old": {
      "definition_site": "00bc7aa0",
      "incomplete_value": true,
      "site": "00bc7aac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:188:8"
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
    "old": {
      "definition_site": "00bc7ac4",
      "incomplete_value": true,
      "site": "00bc7ad0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a8:8"
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
      "00bc7eac",
      "READ",
      [
        "storage",
        "01126100",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7ec8",
      "READ",
      [
        "storage",
        "01126188",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7eec",
      "READ",
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
      "00bc7eac",
      "READ",
      [
        "storage",
        "01126500",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7ec8",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7eec",
      "READ",
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

- 旧版 [`00bc7a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7a5c.md#insn-00bc7a8c) · [`00bc7aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7a5c.md#insn-00bc7aac) · [`00bc7ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7a5c.md#insn-00bc7ad0)
- 新版 `00bc7eb4`（命令位置の公開資料なし） · `00bc7ed4`（命令位置の公開資料なし） · `00bc7ef8`（命令位置の公開資料なし）

~~~diff
- 00bc7a8c ["INT_ADD", "register:40f0:8", ["const:bc7a8c:8", "const:4:8"]]
- 00bc7a8c ["CALL", null, ["callee:00497834:8"]]
+ 00bc7eb4 ["INT_ADD", "register:40f0:8", ["const:bc7eb4:8", "const:4:8"]]
+ 00bc7eb4 ["CALL", null, ["callee:00497834:8"]]
- 00bc7a8c bytes 5a3fe397
+ 00bc7eb4 bytes 603ee397
- 00bc7aac ["INT_ADD", "register:40f0:8", ["const:bc7aac:8", "const:4:8"]]
- 00bc7aac ["CALL", null, ["callee:00497834:8"]]
+ 00bc7ed4 ["INT_ADD", "register:40f0:8", ["const:bc7ed4:8", "const:4:8"]]
+ 00bc7ed4 ["CALL", null, ["callee:00497834:8"]]
- 00bc7aac bytes 523fe397
+ 00bc7ed4 bytes 583ee397
- 00bc7ad0 ["INT_ADD", "register:40f0:8", ["const:bc7ad0:8", "const:4:8"]]
- 00bc7ad0 ["CALL", null, ["callee:0058f59c:8"]]
+ 00bc7ef8 ["INT_ADD", "register:40f0:8", ["const:bc7ef8:8", "const:4:8"]]
+ 00bc7ef8 ["CALL", null, ["callee:0058f59c:8"]]
- 00bc7ad0 bytes a31ee797
+ 00bc7ef8 bytes a91de797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c07ef33f6487cfa1823d40e8c449d6b3"></a>

### [`00bc7b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7b44.md) → [`00bc7f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7f6c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal10GetBooleanEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2c0.md) · 呼出先 4件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 1件 [`00c5d6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6c0.md) · 呼出先 4件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

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
    "old": {
      "definition_site": "00bc7b88",
      "incomplete_value": true,
      "site": "00bc7b98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:150:8"
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
    "old": {
      "definition_site": "00bc7be0",
      "incomplete_value": false,
      "site": "00bc7bec",
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
            "const:c09:8"
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
    "old": {
      "definition_site": "00bc7be4",
      "incomplete_value": false,
      "site": "00bc7bec",
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
            "const:852:8"
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
      "00bc7fb0",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8008",
      "PARAM",
      [
        "storage",
        "002a0c09",
        null,
        "string"
      ]
    ],
    [
      "00bc800c",
      "PARAM",
      [
        "storage",
        "002aa852",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc7fb0",
      "READ",
      [
        "storage",
        "01126550",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8008",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc800c",
      "PARAM",
      [
        "storage",
        "002aa91f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc7b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7b44.md#insn-00bc7b98) · [`00bc7bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7b44.md#insn-00bc7bec) · [`00bc7b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7b44.md#insn-00bc7b68)
- 新版 `00bc7fc0`（命令位置の公開資料なし） · `00bc8014`（命令位置の公開資料なし） · `00bc7f90`（命令位置の公開資料なし）

~~~diff
- 00bc7b98 ["INT_ADD", "register:40f0:8", ["const:bc7b98:8", "const:4:8"]]
- 00bc7b98 ["CALL", null, ["callee:00497a48:8"]]
+ 00bc7fc0 ["INT_ADD", "register:40f0:8", ["const:bc7fc0:8", "const:4:8"]]
+ 00bc7fc0 ["CALL", null, ["callee:00497a48:8"]]
- 00bc7b98 bytes 9c3fe397
+ 00bc7fc0 bytes a23ee397
- 00bc7bec ["INT_ADD", "register:40f0:8", ["const:bc7bec:8", "const:4:8"]]
- 00bc7bec ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bc8014 ["INT_ADD", "register:40f0:8", ["const:bc8014:8", "const:4:8"]]
+ 00bc8014 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bc7bec bytes 2d4b0294
+ 00bc8014 bytes 234b0294
- 00bc7b68 ["INT_ADD", "register:40f0:8", ["const:bc7b68:8", "const:4:8"]]
- 00bc7b68 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bc7f90 ["INT_ADD", "register:40f0:8", ["const:bc7f90:8", "const:4:8"]]
+ 00bc7f90 ["CALL", null, ["callee:00c5b080:8"]]
- 00bc7b68 bytes 464c0294
+ 00bc7f90 bytes 3c4c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dfa3fe8ae056d325682dcce6660638f"></a>

### [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) → [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) FUN_00bc8060

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00bc7b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7b44.md) [`00bc7df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7df0.md) [`00bc7ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7ee4.md) [`00bc7fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7fe4.md) [`00bc8154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8154.md) · 呼出先 4件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 5件 [`00bc7f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc7/00bc7f6c.md) [`00bc8218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8218.md) [`00bc830c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc830c.md) [`00bc840c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc840c.md) [`00bc857c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc857c.md) · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
    "old": {
      "definition_site": "00bc7c70",
      "incomplete_value": true,
      "site": "00bc7c84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e8:8"
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
    "old": {
      "definition_site": "00bc7ce0",
      "incomplete_value": false,
      "site": "00bc7cec",
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
            "const:c09:8"
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
    "old": {
      "definition_site": "00bc7ce4",
      "incomplete_value": false,
      "site": "00bc7cec",
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
            "const:7a4:8"
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
      "00bc8098",
      "READ",
      [
        "storage",
        "011260e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8108",
      "PARAM",
      [
        "storage",
        "002a0c09",
        null,
        "string"
      ]
    ],
    [
      "00bc810c",
      "PARAM",
      [
        "storage",
        "002a97a4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc8098",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8108",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc810c",
      "PARAM",
      [
        "storage",
        "002a9871",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc7c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md#insn-00bc7c84) · [`00bc7cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md#insn-00bc7cec) · [`00bc7d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md#insn-00bc7d44)
- 新版 `00bc80ac`（命令位置の公開資料なし） · `00bc8114`（命令位置の公開資料なし） · `00bc816c`（命令位置の公開資料なし）

~~~diff
- 00bc7c84 ["INT_ADD", "register:40f0:8", ["const:bc7c84:8", "const:4:8"]]
- 00bc7c84 ["CALL", null, ["callee:00497834:8"]]
+ 00bc80ac ["INT_ADD", "register:40f0:8", ["const:bc80ac:8", "const:4:8"]]
+ 00bc80ac ["CALL", null, ["callee:00497834:8"]]
- 00bc7c84 bytes dc3ee397
+ 00bc80ac bytes e23de397
- 00bc7cec ["INT_ADD", "register:40f0:8", ["const:bc7cec:8", "const:4:8"]]
- 00bc7cec ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bc8114 ["INT_ADD", "register:40f0:8", ["const:bc8114:8", "const:4:8"]]
+ 00bc8114 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bc7cec bytes ed4a0294
+ 00bc8114 bytes e34a0294
- 00bc7d44 ["INT_ADD", "register:40f0:8", ["const:bc7d44:8", "const:4:8"]]
- 00bc7d44 ["CALL", null, ["callee:005762b8:8"]]
+ 00bc816c ["INT_ADD", "register:40f0:8", ["const:bc816c:8", "const:4:8"]]
+ 00bc816c ["CALL", null, ["callee:005762b8:8"]]
- 00bc7d44 bytes 4db9e697
+ 00bc816c bytes 53b8e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-257215724d5b6f7b7bd7d408f4e2460f"></a>

### [`00bc7df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7df0.md) → [`00bc8218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8218.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7GetLongEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d430.md) · 呼出先 4件 [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md) [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 1件 [`00c5d830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d830.md) · 呼出先 4件 [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

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
    "old": {
      "definition_site": "00bc7e34",
      "incomplete_value": true,
      "site": "00bc7e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:130:8"
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
    "old": {
      "definition_site": "00bc7e8c",
      "incomplete_value": false,
      "site": "00bc7e98",
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
            "const:c09:8"
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
    "old": {
      "definition_site": "00bc7e90",
      "incomplete_value": false,
      "site": "00bc7e98",
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
            "const:b22:8"
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
      "00bc825c",
      "READ",
      [
        "storage",
        "01126130",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc82b4",
      "PARAM",
      [
        "storage",
        "002a0c09",
        null,
        "string"
      ]
    ],
    [
      "00bc82b8",
      "PARAM",
      [
        "storage",
        "002a0b22",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc825c",
      "READ",
      [
        "storage",
        "01126530",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc82b4",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc82b8",
      "PARAM",
      [
        "storage",
        "002a0bef",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc7e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7df0.md#insn-00bc7e44) · [`00bc7e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7df0.md#insn-00bc7e98) · [`00bc7e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7df0.md#insn-00bc7e14)
- 新版 `00bc826c`（命令位置の公開資料なし） · `00bc82c0`（命令位置の公開資料なし） · `00bc823c`（命令位置の公開資料なし）

~~~diff
- 00bc7e44 ["INT_ADD", "register:40f0:8", ["const:bc7e44:8", "const:4:8"]]
- 00bc7e44 ["CALL", null, ["callee:0058f59c:8"]]
+ 00bc826c ["INT_ADD", "register:40f0:8", ["const:bc826c:8", "const:4:8"]]
+ 00bc826c ["CALL", null, ["callee:0058f59c:8"]]
- 00bc7e44 bytes c61de797
+ 00bc826c bytes cc1ce797
- 00bc7e98 ["INT_ADD", "register:40f0:8", ["const:bc7e98:8", "const:4:8"]]
- 00bc7e98 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bc82c0 ["INT_ADD", "register:40f0:8", ["const:bc82c0:8", "const:4:8"]]
+ 00bc82c0 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bc7e98 bytes 824a0294
+ 00bc82c0 bytes 784a0294
- 00bc7e14 ["INT_ADD", "register:40f0:8", ["const:bc7e14:8", "const:4:8"]]
- 00bc7e14 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bc823c ["INT_ADD", "register:40f0:8", ["const:bc823c:8", "const:4:8"]]
+ 00bc823c ["CALL", null, ["callee:00c5b080:8"]]
- 00bc7e14 bytes 9b4b0294
+ 00bc823c bytes 914b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f77596a5e708d0c89ec889add1c1a2dd"></a>

### [`00bc7ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7ee4.md) → [`00bc830c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc830c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal9GetDoubleEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d450.md) · 呼出先 4件 [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae30.md)
- 新版 呼出元 1件 [`00c5d850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d850.md) · 呼出先 4件 [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b230.md)

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
    "old": {
      "definition_site": "00bc7f28",
      "incomplete_value": true,
      "site": "00bc7f38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:138:8"
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
    "old": {
      "definition_site": "00bc7f80",
      "incomplete_value": false,
      "site": "00bc7f8c",
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
            "const:c09:8"
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
    "old": {
      "definition_site": "00bc7f84",
      "incomplete_value": false,
      "site": "00bc7f8c",
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
            "const:233:8"
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
      "00bc8350",
      "READ",
      [
        "storage",
        "01126138",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc83a8",
      "PARAM",
      [
        "storage",
        "002a0c09",
        null,
        "string"
      ]
    ],
    [
      "00bc83ac",
      "PARAM",
      [
        "storage",
        "002ae233",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc8350",
      "READ",
      [
        "storage",
        "01126538",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc83a8",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc83ac",
      "PARAM",
      [
        "storage",
        "002ae273",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc7f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7ee4.md#insn-00bc7f38) · [`00bc7f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7ee4.md#insn-00bc7f8c) · [`00bc7f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7ee4.md#insn-00bc7f08)
- 新版 `00bc8360`（命令位置の公開資料なし） · `00bc83b4`（命令位置の公開資料なし） · `00bc8330`（命令位置の公開資料なし）

~~~diff
- 00bc7f38 ["INT_ADD", "register:40f0:8", ["const:bc7f38:8", "const:4:8"]]
- 00bc7f38 ["CALL", null, ["callee:00c5b230:8"]]
+ 00bc8360 ["INT_ADD", "register:40f0:8", ["const:bc8360:8", "const:4:8"]]
+ 00bc8360 ["CALL", null, ["callee:00c5b230:8"]]
- 00bc7f38 bytes be4b0294
+ 00bc8360 bytes b44b0294
- 00bc7f8c ["INT_ADD", "register:40f0:8", ["const:bc7f8c:8", "const:4:8"]]
- 00bc7f8c ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bc83b4 ["INT_ADD", "register:40f0:8", ["const:bc83b4:8", "const:4:8"]]
+ 00bc83b4 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bc7f8c bytes 454a0294
+ 00bc83b4 bytes 3b4a0294
- 00bc7f08 ["INT_ADD", "register:40f0:8", ["const:bc7f08:8", "const:4:8"]]
- 00bc7f08 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bc8330 ["INT_ADD", "register:40f0:8", ["const:bc8330:8", "const:4:8"]]
+ 00bc8330 ["CALL", null, ["callee:00c5b080:8"]]
- 00bc7f08 bytes 5e4b0294
+ 00bc8330 bytes 544b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a656bc27a01092a3efddca19ae255d4b"></a>

### [`00bc7fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7fe4.md) → [`00bc840c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc840c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal9GetStringEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d460.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d860.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
    "old": {
      "definition_site": "00bc804c",
      "incomplete_value": true,
      "site": "00bc8058",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:140:8"
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
    "old": {
      "definition_site": "00bc80b0",
      "incomplete_value": false,
      "site": "00bc80bc",
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
            "const:c09:8"
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
    "old": {
      "definition_site": "00bc80b4",
      "incomplete_value": false,
      "site": "00bc80bc",
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
            "const:4dd:8"
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
      "00bc8474",
      "READ",
      [
        "storage",
        "01126140",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc84d8",
      "PARAM",
      [
        "storage",
        "002a0c09",
        null,
        "string"
      ]
    ],
    [
      "00bc84dc",
      "PARAM",
      [
        "storage",
        "002a94dd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc8474",
      "READ",
      [
        "storage",
        "01126540",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc84d8",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc84dc",
      "PARAM",
      [
        "storage",
        "002a95aa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc8058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7fe4.md#insn-00bc8058) · [`00bc80bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7fe4.md#insn-00bc80bc) · [`00bc8028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7fe4.md#insn-00bc8028)
- 新版 `00bc8480`（命令位置の公開資料なし） · `00bc84e4`（命令位置の公開資料なし） · `00bc8450`（命令位置の公開資料なし）

~~~diff
- 00bc8058 ["INT_ADD", "register:40f0:8", ["const:bc8058:8", "const:4:8"]]
- 00bc8058 ["CALL", null, ["callee:00497834:8"]]
+ 00bc8480 ["INT_ADD", "register:40f0:8", ["const:bc8480:8", "const:4:8"]]
+ 00bc8480 ["CALL", null, ["callee:00497834:8"]]
- 00bc8058 bytes e73de397
+ 00bc8480 bytes ed3ce397
- 00bc80bc ["INT_ADD", "register:40f0:8", ["const:bc80bc:8", "const:4:8"]]
- 00bc80bc ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bc84e4 ["INT_ADD", "register:40f0:8", ["const:bc84e4:8", "const:4:8"]]
+ 00bc84e4 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bc80bc bytes f9490294
+ 00bc84e4 bytes ef490294
- 00bc8028 ["INT_ADD", "register:40f0:8", ["const:bc8028:8", "const:4:8"]]
- 00bc8028 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bc8450 ["INT_ADD", "register:40f0:8", ["const:bc8450:8", "const:4:8"]]
+ 00bc8450 ["CALL", null, ["callee:00c5b080:8"]]
- 00bc8028 bytes 164b0294
+ 00bc8450 bytes 0c4b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd21bf5dc700808e5b79c436f9a39461"></a>

### [`00bc8154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8154.md) → [`00bc857c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc857c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7GetDataEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d410.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5d810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d810.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc8060.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
    "old": {
      "definition_site": "00bc81bc",
      "incomplete_value": true,
      "site": "00bc81c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:148:8"
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
    "old": {
      "definition_site": "00bc8220",
      "incomplete_value": false,
      "site": "00bc822c",
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
            "const:c09:8"
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
    "old": {
      "definition_site": "00bc8224",
      "incomplete_value": false,
      "site": "00bc822c",
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
            "const:f0c:8"
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
      "00bc85e4",
      "READ",
      [
        "storage",
        "01126148",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8648",
      "PARAM",
      [
        "storage",
        "002a0c09",
        null,
        "string"
      ]
    ],
    [
      "00bc864c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc85e4",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8648",
      "PARAM",
      [
        "storage",
        "002a0cd6",
        null,
        "string"
      ]
    ],
    [
      "00bc864c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc81c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8154.md#insn-00bc81c8) · [`00bc822c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8154.md#insn-00bc822c) · [`00bc8198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8154.md#insn-00bc8198)
- 新版 `00bc85f0`（命令位置の公開資料なし） · `00bc8654`（命令位置の公開資料なし） · `00bc85c0`（命令位置の公開資料なし）

~~~diff
- 00bc81c8 ["INT_ADD", "register:40f0:8", ["const:bc81c8:8", "const:4:8"]]
- 00bc81c8 ["CALL", null, ["callee:00497834:8"]]
+ 00bc85f0 ["INT_ADD", "register:40f0:8", ["const:bc85f0:8", "const:4:8"]]
+ 00bc85f0 ["CALL", null, ["callee:00497834:8"]]
- 00bc81c8 bytes 8b3de397
+ 00bc85f0 bytes 913ce397
- 00bc822c ["INT_ADD", "register:40f0:8", ["const:bc822c:8", "const:4:8"]]
- 00bc822c ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bc8654 ["INT_ADD", "register:40f0:8", ["const:bc8654:8", "const:4:8"]]
+ 00bc8654 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bc822c bytes 9d490294
+ 00bc8654 bytes 93490294
- 00bc8198 ["INT_ADD", "register:40f0:8", ["const:bc8198:8", "const:4:8"]]
- 00bc8198 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bc85c0 ["INT_ADD", "register:40f0:8", ["const:bc85c0:8", "const:4:8"]]
+ 00bc85c0 ["CALL", null, ["callee:00c5b080:8"]]
- 00bc8198 bytes ba4a0294
+ 00bc85c0 bytes b04a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85f93a60149aeb4a57b27a6a1102d607"></a>

### [`00bc82c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc82c4.md) → [`00bc86ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc86ec.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal15GetKeysByPrefixEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d310.md) · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00540890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540890.md) [`0054a4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a4b4.md) [`0054dc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dc10.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5d710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d710.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005408d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408d0.md) [`0054a4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a4f4.md) [`0054dc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dc50.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 97.81% / 新版 97.81%

CFGの説明率　旧版 79.49% / 新版 73.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc843c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc8864"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8774",
      "incomplete_value": true,
      "site": "00bc8780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc834c",
      "incomplete_value": true,
      "site": "00bc8358",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f8:8"
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
      "00bc8774",
      "READ",
      [
        "storage",
        "011260f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc843c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc88c8"
      ]
    ]
  ],
  "added": [
    [
      "00bc8774",
      "READ",
      [
        "storage",
        "011264f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8864",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc88c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc8358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc82c4.md#insn-00bc8358) · [`00bc843c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc82c4.md#insn-00bc843c) · [`00bc84e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc82c4.md#insn-00bc84e0)
- 新版 `00bc8780`（命令位置の公開資料なし）

~~~diff
- 00bc8358 ["INT_ADD", "register:40f0:8", ["const:bc8358:8", "const:4:8"]]
- 00bc8358 ["CALL", null, ["callee:00497834:8"]]
+ 00bc8780 ["INT_ADD", "register:40f0:8", ["const:bc8780:8", "const:4:8"]]
+ 00bc8780 ["CALL", null, ["callee:00497834:8"]]
- 00bc8358 bytes 273de397
+ 00bc8780 bytes 2d3ce397
- 00bc843c ["CBRANCH", null, ["local:b24:8", "register:101:1"]]
- 00bc843c bytes 20030054
- 00bc84e0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc84e0 ["RETURN", null, ["register:0:8"]]
- 00bc84e0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9afdac64e0059b830bee0af5b3ee2c9"></a>

### [`00bc85b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc85b0.md) → [`00bc89d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc8/00bc89d8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal6GetAllEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3f0.md) · 呼出先 26件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md) [`0087f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f064.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`00c5d7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d7f0.md) · 呼出先 26件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) [`0087f0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f0a4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.11% / 新版 75.11%

CFGの説明率　旧版 52.50% / 新版 55.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 21件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc86e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc86e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc8b08"
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
      "00bc8a30",
      "READ",
      [
        "storage",
        "011260f0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc86e0",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "00bc8b80",
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
      "00bc8a30",
      "READ",
      [
        "storage",
        "011264f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8b08",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "00bc8b80",
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

- 旧版 [`00bc8610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc85b0.md#insn-00bc8610) · [`00bc8668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc85b0.md#insn-00bc8668) · [`00bc86e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc85b0.md#insn-00bc86e0)
- 新版 `00bc8a38`（命令位置の公開資料なし）

~~~diff
- 00bc8610 ["INT_ADD", "register:40f0:8", ["const:bc8610:8", "const:4:8"]]
- 00bc8610 ["CALL", null, ["callee:00497834:8"]]
+ 00bc8a38 ["INT_ADD", "register:40f0:8", ["const:bc8a38:8", "const:4:8"]]
+ 00bc8a38 ["CALL", null, ["callee:00497834:8"]]
- 00bc8610 bytes 793ce397
+ 00bc8a38 bytes 7f3be397
- 00bc8668 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc8668 ["INT_ADD", "register:40f0:8", ["const:bc8668:8", "const:4:8"]]
- 00bc8668 ["CALLIND", null, ["register:0:8"]]
- 00bc8668 bytes 00013fd6
- 00bc86e0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bc86e0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bc86e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc86e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc86e0 bytes fa2301a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7feea1189c793d74bb75fcbf5739fa"></a>

### [`00bc8dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8dcc.md) → [`00bc91f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc91f4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17Remote

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d390.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00bc9570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9570.md) [`00bc9ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9ba8.md) [`00bc9bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9bac.md)
- 新版 呼出元 1件 [`00c5d790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d790.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bc9998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9998.md) [`00bc9fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fd0.md) [`00bc9fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fd4.md)

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
    "old": {
      "definition_site": "00bc8f84",
      "incomplete_value": false,
      "site": "00bc8f84",
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
            "const:428:8"
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
    "old": {
      "definition_site": "00bc8edc",
      "incomplete_value": true,
      "site": "00bc8eec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:258:8"
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
    "old": {
      "definition_site": "00bc8ee0",
      "incomplete_value": true,
      "site": "00bc8eec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:268:8"
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
      "00bc9304",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc9308",
      "READ",
      [
        "storage",
        "01126268",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc932c",
      "PARAM",
      [
        "storage",
        "002a1b5b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc9304",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc9308",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc932c",
      "PARAM",
      [
        "storage",
        "002a1c28",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc8eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8dcc.md#insn-00bc8eec) · [`00bc8f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8dcc.md#insn-00bc8f08) · [`00bc8f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8dcc.md#insn-00bc8f20)
- 新版 `00bc9314`（命令位置の公開資料なし） · `00bc9330`（命令位置の公開資料なし） · `00bc9348`（命令位置の公開資料なし）

~~~diff
- 00bc8eec ["INT_ADD", "register:40f0:8", ["const:bc8eec:8", "const:4:8"]]
- 00bc8eec ["CALL", null, ["callee:005896f4:8"]]
+ 00bc9314 ["INT_ADD", "register:40f0:8", ["const:bc9314:8", "const:4:8"]]
+ 00bc9314 ["CALL", null, ["callee:005896f4:8"]]
- 00bc8eec bytes f201e797
+ 00bc9314 bytes f800e797
- 00bc8f08 ["INT_ADD", "register:40f0:8", ["const:bc8f08:8", "const:4:8"]]
- 00bc8f08 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc9330 ["INT_ADD", "register:40f0:8", ["const:bc9330:8", "const:4:8"]]
+ 00bc9330 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc8f08 bytes 3e470294
+ 00bc9330 bytes 34470294
- 00bc8f20 ["INT_ADD", "register:40f0:8", ["const:bc8f20:8", "const:4:8"]]
- 00bc8f20 ["CALL", null, ["callee:00497834:8"]]
+ 00bc9348 ["INT_ADD", "register:40f0:8", ["const:bc9348:8", "const:4:8"]]
+ 00bc9348 ["CALL", null, ["callee:00497834:8"]]
- 00bc8f20 bytes 353ae397
+ 00bc9348 bytes 3b39e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a97c2131b90a036fed398f4410e1d10d"></a>

### [`00bc959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc959c.md) → [`00bc99c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc99c4.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_13remote_config10ConfigInfoEZNS0_26CompleteWithResultInternalIS3_EEvRKNS_12Fut

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4d0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5d8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8d0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 85.71% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bc9608",
      "incomplete_value": false,
      "site": "00bc960c",
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
            "const:8:8"
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
      "site": "00bc96c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bc9aec"
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
      "00bc9a30",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc9a30",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc960c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc959c.md#insn-00bc960c) · [`00bc96c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc959c.md#insn-00bc96c4)
- 新版 `00bc9a34`（命令位置の公開資料なし） · `00bc9aec`（命令位置の公開資料なし）

~~~diff
- 00bc960c ["INT_ADD", "register:40f0:8", ["const:bc960c:8", "const:4:8"]]
- 00bc960c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc9a34 ["INT_ADD", "register:40f0:8", ["const:bc9a34:8", "const:4:8"]]
+ 00bc9a34 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc960c bytes 7d450294
+ 00bc9a34 bytes 73450294
- 00bc96c4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc96c4 ["RETURN", null, ["register:0:8"]]
- 00bc96c4 bytes c0035fd6
+ 00bc9aec ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bc9aec ["RETURN", null, ["register:0:8"]]
+ 00bc9aec bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ffd5c59aff600f9f7890f54b1792eb2"></a>

### [`00bc96c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc96c8.md) → [`00bc9af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9af0.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIbZNS0_26CompleteWithResultInternalIbEEvRKNS_12FutureHandleEiPKcRKT_EUlPbE_EEvS5_i

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4e0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5d8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8e0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 85.71% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bc9734",
      "incomplete_value": false,
      "site": "00bc9738",
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
            "const:8:8"
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
      "00bc9b5c",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc9b5c",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc96c8.md#insn-00bc9738) · [`00bc96fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc96c8.md#insn-00bc96fc) · [`00bc9708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc96c8.md#insn-00bc9708)
- 新版 `00bc9b60`（命令位置の公開資料なし） · `00bc9b24`（命令位置の公開資料なし） · `00bc9b30`（命令位置の公開資料なし）

~~~diff
- 00bc9738 ["INT_ADD", "register:40f0:8", ["const:bc9738:8", "const:4:8"]]
- 00bc9738 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc9b60 ["INT_ADD", "register:40f0:8", ["const:bc9b60:8", "const:4:8"]]
+ 00bc9b60 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc9738 bytes 32450294
+ 00bc9b60 bytes 28450294
- 00bc96fc ["INT_ADD", "register:40f0:8", ["const:bc96fc:8", "const:4:8"]]
- 00bc96fc ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc9b24 ["INT_ADD", "register:40f0:8", ["const:bc9b24:8", "const:4:8"]]
+ 00bc9b24 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc96fc bytes c1430294
+ 00bc9b24 bytes b7430294
- 00bc9708 ["INT_ADD", "register:40f0:8", ["const:bc9708:8", "const:4:8"]]
- 00bc9708 ["CALL", null, ["callee:00c5ae80:8"]]
+ 00bc9b30 ["INT_ADD", "register:40f0:8", ["const:bc9b30:8", "const:4:8"]]
+ 00bc9b30 ["CALL", null, ["callee:00c5ae80:8"]]
- 00bc9708 bytes de440294
+ 00bc9b30 bytes d4440294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31f98e53e22ce0579cc0d2018f906a5f"></a>

### [`00bc97f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc97f8.md) → [`00bc9c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9c20.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_13remote_config10ConfigInfoEEEvRKNS_12FutureHandleEiP

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4f0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5d8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8f0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.42% / 新版 92.42%

CFGの説明率　旧版 12.50% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bc985c",
      "incomplete_value": false,
      "site": "00bc9860",
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
            "const:8:8"
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
      "definition_site": "00bc989c",
      "incomplete_value": true,
      "site": "00bc98a4",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:00bc985c",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc98c8",
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
      "00bc9c84",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "00bc9cf0",
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

- 旧版 [`00bc9860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc97f8.md#insn-00bc9860) · [`00bc98a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc97f8.md#insn-00bc98a4) · [`00bc9824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc97f8.md#insn-00bc9824)
- 新版 `00bc9c88`（命令位置の公開資料なし） · `00bc9ccc`（命令位置の公開資料なし） · `00bc9c4c`（命令位置の公開資料なし）

~~~diff
- 00bc9860 ["INT_ADD", "register:40f0:8", ["const:bc9860:8", "const:4:8"]]
- 00bc9860 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc9c88 ["INT_ADD", "register:40f0:8", ["const:bc9c88:8", "const:4:8"]]
+ 00bc9c88 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc9860 bytes e8440294
+ 00bc9c88 bytes de440294
- 00bc98a4 ["INT_ADD", "register:40f0:8", ["const:bc98a4:8", "const:4:8"]]
- 00bc98a4 ["CALL", null, ["callee:00c5ae90:8"]]
+ 00bc9ccc ["INT_ADD", "register:40f0:8", ["const:bc9ccc:8", "const:4:8"]]
+ 00bc9ccc ["CALL", null, ["callee:00c5ae90:8"]]
- 00bc98a4 bytes 7b440294
+ 00bc9ccc bytes 71440294
- 00bc9824 ["INT_ADD", "register:40f0:8", ["const:bc9824:8", "const:4:8"]]
- 00bc9824 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc9c4c ["INT_ADD", "register:40f0:8", ["const:bc9c4c:8", "const:4:8"]]
+ 00bc9c4c ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc9824 bytes 77430294
+ 00bc9c4c bytes 6d430294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-190f3bb23f629d4d89c3084f9af5235d"></a>

### [`00bc99ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc99ac.md) → [`00bc9dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9dd4.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIbEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d500.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5d900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d900.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9a08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc9e30"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9df0",
      "incomplete_value": true,
      "site": "00bc9e00",
      "value": [
        "live",
        "register:40c0:8"
      ]
    },
    "old": {
      "definition_site": "00bc99c8",
      "incomplete_value": true,
      "site": "00bc99d8",
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
      "unmatched:00bc9a08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc9e40"
      ]
    ],
    [
      "unmatched:00bc9a10",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc9a00",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc9e30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc9e40"
      ]
    ],
    [
      "00bc9e38",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "00bc9e28",
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

- 旧版 [`00bc99d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc99ac.md#insn-00bc99d8) · [`00bc99e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc99ac.md#insn-00bc99e4) · [`00bc9a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc99ac.md#insn-00bc9a00)
- 新版 `00bc9e00`（命令位置の公開資料なし） · `00bc9e0c`（命令位置の公開資料なし）

~~~diff
- 00bc99d8 ["INT_ADD", "register:40f0:8", ["const:bc99d8:8", "const:4:8"]]
- 00bc99d8 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc9e00 ["INT_ADD", "register:40f0:8", ["const:bc9e00:8", "const:4:8"]]
+ 00bc9e00 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc99d8 bytes 0a430294
+ 00bc9e00 bytes 00430294
- 00bc99e4 ["INT_ADD", "register:40f0:8", ["const:bc99e4:8", "const:4:8"]]
- 00bc99e4 ["CALL", null, ["callee:00c5ae80:8"]]
+ 00bc9e0c ["INT_ADD", "register:40f0:8", ["const:bc9e0c:8", "const:4:8"]]
+ 00bc9e0c ["CALL", null, ["callee:00c5ae80:8"]]
- 00bc99e4 bytes 27440294
+ 00bc9e0c bytes 1d440294
- 00bc9a00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc9a00 ["INT_ADD", "register:40f0:8", ["const:bc9a00:8", "const:4:8"]]
- 00bc9a00 ["CALLIND", null, ["register:0:8"]]
- 00bc9a00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdfee68838894840a4817ff5ee6ca0e4"></a>

### [`00bc9ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9ab4.md) → [`00bc9edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9edc.md) _ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d520.md) · 呼出先 3件 [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9f0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5d920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d920.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.65% / 新版 80.65%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ab4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ab8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc9ab4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc9ab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc9abc",
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
      "00bc9edc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc9ee0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc9ee4",
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

- 旧版 [`00bc9ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9ab4.md#insn-00bc9ab4) · [`00bc9ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9ab4.md#insn-00bc9ab8) · [`00bc9abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9ab4.md#insn-00bc9abc)

~~~diff
- 00bc9ab4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bc9ab4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bc9ab4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc9ab4 bytes f50f1df8
- 00bc9ab8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc9ab8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc9ab8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc9ab8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc9ab8 bytes f44f01a9
- 00bc9abc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc9abc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc9abc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc9abc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc9abc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3965d3d3881f70b647152751854eb7a"></a>

### [`00bc9b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9b58.md) → [`00bc9f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9f80.md) FUN_00bc9f80

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00bc9f9c",
      "incomplete_value": false,
      "site": "00bc9fa0",
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
    "old": {
      "definition_site": "00bc9b74",
      "incomplete_value": false,
      "site": "00bc9b78",
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
            "const:428:8"
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
      "00bc9fa0",
      "DATA",
      [
        "storage",
        "00c91428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc9fa0",
      "DATA",
      [
        "storage",
        "00c91828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9b58.md#insn-00bc9b6c) · [`00bc9b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9b58.md#insn-00bc9b74)
- 新版 `00bc9f94`（命令位置の公開資料なし） · `00bc9f9c`（命令位置の公開資料なし）

~~~diff
- 00bc9b6c ["INT_ADD", "register:40f0:8", ["const:bc9b6c:8", "const:4:8"]]
- 00bc9b6c ["CALL", null, ["callee:00c57e90:8"]]
+ 00bc9f94 ["INT_ADD", "register:40f0:8", ["const:bc9f94:8", "const:4:8"]]
+ 00bc9f94 ["CALL", null, ["callee:00c57e90:8"]]
- 00bc9b6c bytes c9370294
+ 00bc9f94 bytes bf370294
- 00bc9b74 ["COPY", "tmp:0:8", ["const:428:8"]]
- 00bc9b74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9b74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9b74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc9f9c ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00bc9f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc9b74 bytes 08a11091
+ 00bc9f9c bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0b190a88e8ebd5e47040214f9a5385e"></a>

### [`00bc9bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9bb0.md) → [`00bc9fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fd8.md) FUN_00bc9fd8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5af40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b340.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 65.22% / 新版 65.22%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9bb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9bb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9bb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc9bb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc9bb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc9bcc",
      "READ",
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
      "00bc9fd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc9fdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc9ff4",
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

- 旧版 [`00bc9bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9bb0.md#insn-00bc9bb0) · [`00bc9bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9bb0.md#insn-00bc9bb4) · [`00bc9bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9bb0.md#insn-00bc9bd4)
- 新版 `00bc9ffc`（命令位置の公開資料なし）

~~~diff
- 00bc9bb0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc9bb0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc9bb0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc9bb0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc9bb0 bytes f44fbea9
- 00bc9bb4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc9bb4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc9bb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc9bb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc9bb4 bytes fd7b01a9
- 00bc9bd4 ["INT_ADD", "register:40f0:8", ["const:bc9bd4:8", "const:4:8"]]
- 00bc9bd4 ["CALL", null, ["callee:00574cec:8"]]
+ 00bc9ffc ["INT_ADD", "register:40f0:8", ["const:bc9ffc:8", "const:4:8"]]
+ 00bc9ffc ["CALL", null, ["callee:00574cec:8"]]
- 00bc9bd4 bytes 36ace697
+ 00bc9ffc bytes 3cabe697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c06d4c3bc43917768332173e240685c3"></a>

### [`00bc9d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9d90.md) → [`00bca1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca1b8.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bca1d4",
      "incomplete_value": true,
      "site": "00bca1d8",
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
      "definition_site": "00bc9dac",
      "incomplete_value": true,
      "site": "00bc9db0",
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
      "00bca1cc",
      "READ",
      [
        "storage",
        "00c9b528",
        null,
        "pointer"
      ]
    ],
    [
      "00bca1d8",
      "DATA",
      [
        "storage",
        "00c914a8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00bca1cc",
      "READ",
      [
        "storage",
        "00c9b928",
        null,
        "pointer"
      ]
    ],
    [
      "00bca1d8",
      "DATA",
      [
        "storage",
        "00c918a8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9d90.md#insn-00bc9da4) · [`00bc9dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9d90.md#insn-00bc9dc0)
- 新版 `00bca1cc`（命令位置の公開資料なし） · `00bca1e8`（命令位置の公開資料なし）

~~~diff
- 00bc9da4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:528:8"]]
- 00bc9da4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bca1cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:928:8"]]
+ 00bca1cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc9da4 bytes 299542f9
+ 00bca1cc bytes 299544f9
- 00bc9dc0 ["INT_ADD", "register:40f0:8", ["const:bc9dc0:8", "const:4:8"]]
- 00bc9dc0 ["CALL", null, ["callee:00c5ac10:8"]]
+ 00bca1e8 ["INT_ADD", "register:40f0:8", ["const:bca1e8:8", "const:4:8"]]
+ 00bca1e8 ["CALL", null, ["callee:00c5ac10:8"]]
- 00bc9dc0 bytes 94420294
+ 00bca1e8 bytes 8a420294
~~~


<a id="compare-0c6db8e5a20a5e92f6d7c34e112ad8d1"></a>

### [`00bc9dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9dd8.md) → [`00bca200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca200.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)

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
      "site": "00bc9dd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ddc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ddc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc9dd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc9ddc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc9dec",
      "READ",
      [
        "storage",
        "00c9b528",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bca200",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bca204",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bca214",
      "READ",
      [
        "storage",
        "00c9b928",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9dd8.md#insn-00bc9dd8) · [`00bc9ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9dd8.md#insn-00bc9ddc) · [`00bc9df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9dd8.md#insn-00bc9df8)

~~~diff
- 00bc9dd8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc9dd8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc9dd8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc9dd8 bytes f30f1ef8
- 00bc9ddc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc9ddc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc9ddc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc9ddc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc9ddc bytes fd7b01a9
- 00bc9df8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bc9df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc9df8 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-871bcf115189a76047c2b5aa1abaaa67"></a>

### [`00bc9e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e20.md) → [`00bca248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca248.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationaSERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc9f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9f38.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bca360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca360.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9e34"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bca25c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca28c",
      "incomplete_value": true,
      "site": "00bca298",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9e64",
      "incomplete_value": true,
      "site": "00bc9e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:520:8"
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
      "unmatched:00bc9e34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bca29c"
      ]
    ],
    [
      "00bca28c",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "00bca28c",
      "PARAM",
      [
        "storage",
        "00bc9f38",
        "_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca25c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bca29c"
      ]
    ],
    [
      "00bca28c",
      "READ",
      [
        "storage",
        "00c9b920",
        null,
        "pointer"
      ]
    ],
    [
      "00bca28c",
      "PARAM",
      [
        "storage",
        "00bca360",
        "_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e20.md#insn-00bc9e34) · [`00bc9e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e20.md#insn-00bc9e70)
- 新版 `00bca298`（命令位置の公開資料なし） · `00bca25c`（命令位置の公開資料なし）

~~~diff
- 00bc9e34 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00bc9e34 bytes 00020054
- 00bc9e70 ["INT_ADD", "register:40f0:8", ["const:bc9e70:8", "const:4:8"]]
- 00bc9e70 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bca298 ["INT_ADD", "register:40f0:8", ["const:bca298:8", "const:4:8"]]
+ 00bca298 ["CALL", null, ["callee:00c5ac00:8"]]
- 00bc9e70 bytes 64420294
+ 00bca298 bytes 5a420294
+ 00bca25c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00bca25c bytes 00020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cf9cf1ba9c9901db9ba197a2f7f7799"></a>

### [`00bc9e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e84.md) → [`00bca2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca2ac.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationaSEOS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc9f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9f38.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bca360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca360.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 46.15% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca2e4",
      "incomplete_value": true,
      "site": "00bca2ec",
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
            "const:138:8"
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
    "new": {
      "definition_site": "00bca2e8",
      "incomplete_value": true,
      "site": "00bca2ec",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca304",
      "incomplete_value": true,
      "site": "00bca310",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9edc",
      "incomplete_value": true,
      "site": "00bc9ee8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:520:8"
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
      "00bca304",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "00bca304",
      "PARAM",
      [
        "storage",
        "00bc9f38",
        "_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca304",
      "READ",
      [
        "storage",
        "00c9b920",
        null,
        "pointer"
      ]
    ],
    [
      "00bca304",
      "PARAM",
      [
        "storage",
        "00bca360",
        "_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e84.md#insn-00bc9ec4) · [`00bc9ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e84.md#insn-00bc9ee8) · [`00bc9ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e84.md#insn-00bc9ef8)
- 新版 `00bca2ec`（命令位置の公開資料なし） · `00bca310`（命令位置の公開資料なし）

~~~diff
- 00bc9ec4 ["INT_ADD", "register:40f0:8", ["const:bc9ec4:8", "const:4:8"]]
- 00bc9ec4 ["CALL", null, ["callee:00c5ac10:8"]]
+ 00bca2ec ["INT_ADD", "register:40f0:8", ["const:bca2ec:8", "const:4:8"]]
+ 00bca2ec ["CALL", null, ["callee:00c5ac10:8"]]
- 00bc9ec4 bytes 53420294
+ 00bca2ec bytes 49420294
- 00bc9ee8 ["INT_ADD", "register:40f0:8", ["const:bc9ee8:8", "const:4:8"]]
- 00bc9ee8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bca310 ["INT_ADD", "register:40f0:8", ["const:bca310:8", "const:4:8"]]
+ 00bca310 ["CALL", null, ["callee:00c5ac00:8"]]
- 00bc9ee8 bytes 46420294
+ 00bca310 bytes 3c420294
- 00bc9ef8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc9ef8 ["RETURN", null, ["register:0:8"]]
- 00bc9ef8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a3c368255c41c1e41cde17686a24a49"></a>

### [`00bca0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0bc.md) → [`00bca4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4e4.md) _ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5c0.md) · 呼出先 8件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md)
- 新版 呼出元 1件 [`00c5a9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9c0.md) · 呼出先 8件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md)

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
    "old": {
      "definition_site": "00bca108",
      "incomplete_value": true,
      "site": "00bca108",
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
    "old": {
      "definition_site": "00bca0e8",
      "incomplete_value": true,
      "site": "00bca0ec",
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
    "old": {
      "definition_site": "00bca1b0",
      "incomplete_value": false,
      "site": "00bca1bc",
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
            "const:30e:8"
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
      "00bca500",
      "READ",
      [
        "storage",
        "00c9b5a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bca50c",
      "READ",
      [
        "storage",
        "01126320",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bca518",
      "READ",
      [
        "storage",
        "01126320",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bca500",
      "READ",
      [
        "storage",
        "00c9b9a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bca50c",
      "READ",
      [
        "storage",
        "01126720",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bca518",
      "READ",
      [
        "storage",
        "01126720",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0bc.md#insn-00bca0ec) · [`00bca1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0bc.md#insn-00bca1bc) · [`00bca0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0bc.md#insn-00bca0d8)
- 新版 `00bca514`（命令位置の公開資料なし） · `00bca5e4`（命令位置の公開資料なし） · `00bca500`（命令位置の公開資料なし）

~~~diff
- 00bca0ec ["INT_ADD", "register:40f0:8", ["const:bca0ec:8", "const:4:8"]]
- 00bca0ec ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bca514 ["INT_ADD", "register:40f0:8", ["const:bca514:8", "const:4:8"]]
+ 00bca514 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bca0ec bytes 45410294
+ 00bca514 bytes 3b410294
- 00bca1bc ["INT_ADD", "register:40f0:8", ["const:bca1bc:8", "const:4:8"]]
- 00bca1bc ["CALL", null, ["callee:00c5b130:8"]]
+ 00bca5e4 ["INT_ADD", "register:40f0:8", ["const:bca5e4:8", "const:4:8"]]
+ 00bca5e4 ["CALL", null, ["callee:00c5b130:8"]]
- 00bca1bc bytes dd420294
+ 00bca5e4 bytes d3420294
- 00bca0d8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a0:8"]]
- 00bca0d8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bca500 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9a0:8"]]
+ 00bca500 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00bca0d8 bytes b5d242f9
+ 00bca500 bytes b5d244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b70d14bfb1e8f1ed63184efab8ec524"></a>

### [`00bca368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md) → [`00bca790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca790.md) _ZN8firebase4auth4AuthC1EPNS_3AppEPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d690.md) · 呼出先 10件 [`00bcb984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md)
- 新版 呼出元 1件 [`00c5da90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da90.md) · 呼出先 10件 [`00bcbdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbdac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md)

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
    "old": {
      "definition_site": "00bca3b8",
      "incomplete_value": false,
      "site": "00bca3bc",
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
            "const:4d2:8"
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
    "old": {
      "definition_site": "00bca3dc",
      "incomplete_value": false,
      "site": "00bca3e8",
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
            "const:cf:8"
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
      "definition_site": "00bca868",
      "incomplete_value": false,
      "site": "00bca870",
      "value": [
        "leaf",
        "const:bcbdac:8"
      ]
    },
    "old": {
      "definition_site": "00bca440",
      "incomplete_value": false,
      "site": "00bca448",
      "value": [
        "leaf",
        "const:bcb984:8"
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
      "00bca7e0",
      "PARAM",
      [
        "storage",
        "002af4d2",
        null,
        "string"
      ]
    ],
    [
      "00bca804",
      "PARAM",
      [
        "storage",
        "002bc0cf",
        null,
        null
      ]
    ],
    [
      "00bca868",
      "PARAM",
      [
        "storage",
        "00bcb984",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca7e0",
      "PARAM",
      [
        "storage",
        "002af512",
        null,
        "string"
      ]
    ],
    [
      "00bca804",
      "PARAM",
      [
        "storage",
        "002bc10f",
        null,
        null
      ]
    ],
    [
      "00bca868",
      "PARAM",
      [
        "storage",
        "00bcbdac",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md#insn-00bca3bc) · [`00bca3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md#insn-00bca3e8) · [`00bca448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md#insn-00bca448)
- 新版 `00bca7e4`（命令位置の公開資料なし） · `00bca810`（命令位置の公開資料なし） · `00bca870`（命令位置の公開資料なし）

~~~diff
- 00bca3bc ["INT_ADD", "register:40f0:8", ["const:bca3bc:8", "const:4:8"]]
- 00bca3bc ["CALL", null, ["callee:00c5b000:8"]]
+ 00bca7e4 ["INT_ADD", "register:40f0:8", ["const:bca7e4:8", "const:4:8"]]
+ 00bca7e4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bca3bc bytes 11420294
+ 00bca7e4 bytes 07420294
- 00bca3e8 ["INT_ADD", "register:40f0:8", ["const:bca3e8:8", "const:4:8"]]
- 00bca3e8 ["CALL", null, ["callee:00c5bd60:8"]]
+ 00bca810 ["INT_ADD", "register:40f0:8", ["const:bca810:8", "const:4:8"]]
+ 00bca810 ["CALL", null, ["callee:00c5bd60:8"]]
- 00bca3e8 bytes 5e450294
+ 00bca810 bytes 54450294
- 00bca448 ["INT_ADD", "register:40f0:8", ["const:bca448:8", "const:4:8"]]
- 00bca448 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bca870 ["INT_ADD", "register:40f0:8", ["const:bca870:8", "const:4:8"]]
+ 00bca870 ["CALL", null, ["callee:00c5ac00:8"]]
- 00bca448 bytes ee400294
+ 00bca870 bytes e4400294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-963ee7b818dfeeae57679d108ab4460d"></a>

### [`00bca614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca614.md) → [`00bcaa3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcaa3c.md) _ZN8firebase4auth4Auth14DeleteInternalEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d630.md) · 呼出先 14件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)
- 新版 呼出元 1件 [`00c5da30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da30.md) · 呼出先 14件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)

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
    "old": {
      "definition_site": "00bca6a8",
      "incomplete_value": true,
      "site": "00bca6ac",
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
    "old": {
      "definition_site": "00bca634",
      "incomplete_value": true,
      "site": "00bca638",
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
    "old": {
      "definition_site": "00bca720",
      "incomplete_value": false,
      "site": "00bca728",
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
            "const:b49:8"
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
      "00bcaa50",
      "READ",
      [
        "storage",
        "00c9b5a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcaa58",
      "READ",
      [
        "storage",
        "01126320",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bcaac4",
      "READ",
      [
        "storage",
        "00c9b5a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bcaa50",
      "READ",
      [
        "storage",
        "00c9b9a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcaa58",
      "READ",
      [
        "storage",
        "01126720",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bcaac4",
      "READ",
      [
        "storage",
        "00c9b9a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca614.md#insn-00bca638) · [`00bca728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca614.md#insn-00bca728) · [`00bca628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca614.md#insn-00bca628)
- 新版 `00bcaa60`（命令位置の公開資料なし） · `00bcab50`（命令位置の公開資料なし） · `00bcaa50`（命令位置の公開資料なし）

~~~diff
- 00bca638 ["INT_ADD", "register:40f0:8", ["const:bca638:8", "const:4:8"]]
- 00bca638 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcaa60 ["INT_ADD", "register:40f0:8", ["const:bcaa60:8", "const:4:8"]]
+ 00bcaa60 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bca638 bytes f23f0294
+ 00bcaa60 bytes e83f0294
- 00bca728 ["INT_ADD", "register:40f0:8", ["const:bca728:8", "const:4:8"]]
- 00bca728 ["CALL", null, ["callee:00c5b130:8"]]
+ 00bcab50 ["INT_ADD", "register:40f0:8", ["const:bcab50:8", "const:4:8"]]
+ 00bcab50 ["CALL", null, ["callee:00c5b130:8"]]
- 00bca728 bytes 82410294
+ 00bcab50 bytes 78410294
- 00bca628 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5a0:8"]]
- 00bca628 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcaa50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a0:8"]]
+ 00bcaa50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bca628 bytes 08d142f9
+ 00bcaa50 bytes 08d144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb53573ca96c0e06b6c8e4d3090c0dcf"></a>

### [`00bca9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9d4.md) → [`00bcadfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcadfc.md) _ZN8firebase4auth4Auth3appEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d680.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5da80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da80.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
    "old": {
      "definition_site": "00bca9f0",
      "incomplete_value": false,
      "site": "00bca9f4",
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
            "const:6c8:8"
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
      "00bcae18",
      "PARAM",
      [
        "storage",
        "002b16c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcae18",
      "PARAM",
      [
        "storage",
        "002b1708",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9d4.md#insn-00bca9f4) · [`00bca9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9d4.md#insn-00bca9f0)
- 新版 `00bcae1c`（命令位置の公開資料なし） · `00bcae18`（命令位置の公開資料なし）

~~~diff
- 00bca9f4 ["INT_ADD", "register:40f0:8", ["const:bca9f4:8", "const:4:8"]]
- 00bca9f4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcae1c ["INT_ADD", "register:40f0:8", ["const:bcae1c:8", "const:4:8"]]
+ 00bcae1c ["CALL", null, ["callee:00c5b000:8"]]
- 00bca9f4 bytes 83400294
+ 00bcae1c bytes 79400294
- 00bca9f0 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00bca9f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bca9f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bca9f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcae18 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00bcae18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcae18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcae18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bca9f0 bytes 00201b91
+ 00bcae18 bytes 00201c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-811dae6f2e0e59422f6b370aa9ad246b"></a>

### [`00bcaa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaa0c.md) → [`00bcae34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcae34.md) _ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5d6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5daf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5daf0.md)

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
    "old": {
      "definition_site": "00bcab84",
      "incomplete_value": false,
      "site": "00bcab88",
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
            "const:c2c:8"
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
      "00bcafac",
      "PARAM",
      [
        "storage",
        "002b8c2c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcafac",
      "PARAM",
      [
        "storage",
        "002b8c6c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcab88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaa0c.md#insn-00bcab88) · [`00bcaa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaa0c.md#insn-00bcaa48) · [`00bcaacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaa0c.md#insn-00bcaacc)
- 新版 `00bcafb0`（命令位置の公開資料なし） · `00bcae70`（命令位置の公開資料なし） · `00bcaef4`（命令位置の公開資料なし）

~~~diff
- 00bcab88 ["INT_ADD", "register:40f0:8", ["const:bcab88:8", "const:4:8"]]
- 00bcab88 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcafb0 ["INT_ADD", "register:40f0:8", ["const:bcafb0:8", "const:4:8"]]
+ 00bcafb0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcab88 bytes 1e400294
+ 00bcafb0 bytes 14400294
- 00bcaa48 ["INT_ADD", "register:40f0:8", ["const:bcaa48:8", "const:4:8"]]
- 00bcaa48 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcae70 ["INT_ADD", "register:40f0:8", ["const:bcae70:8", "const:4:8"]]
+ 00bcae70 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcaa48 bytes ee3e0294
+ 00bcae70 bytes e43e0294
- 00bcaacc ["INT_ADD", "register:40f0:8", ["const:bcaacc:8", "const:4:8"]]
- 00bcaacc ["CALL", null, ["callee:00c5daf0:8"]]
+ 00bcaef4 ["INT_ADD", "register:40f0:8", ["const:bcaef4:8", "const:4:8"]]
+ 00bcaef4 ["CALL", null, ["callee:00c5daf0:8"]]
- 00bcaacc bytes 094b0294
+ 00bcaef4 bytes ff4a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e22b7275a268ee6e93fe075596277361"></a>

### [`00bcabdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcabdc.md) → [`00bcb004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb004.md) _ZN8firebase4auth4Auth18AddIdTokenListenerEPNS0_15IdTokenListenerE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5d5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5e0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5d9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 92.79% / 新版 92.79%

CFGの説明率　旧版 65.38% / 新版 58.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcacdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcb104"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcad48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcacdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb0ec"
      ]
    ],
    [
      "unmatched:00bcad5c",
      "PARAM",
      [
        "storage",
        "002b8c2c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcad48",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcb104",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb0ec"
      ]
    ],
    [
      "00bcb184",
      "PARAM",
      [
        "storage",
        "002b8c6c",
        null,
        "string"
      ]
    ],
    [
      "00bcb170",
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

- 旧版 [`00bcacdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcabdc.md#insn-00bcacdc) · [`00bcad48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcabdc.md#insn-00bcad48) · [`00bcad60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcabdc.md#insn-00bcad60)
- 新版 `00bcb188`（命令位置の公開資料なし）

~~~diff
- 00bcacdc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcacdc ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00bcacdc bytes 41ffff54
- 00bcad48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcad48 ["INT_ADD", "register:40f0:8", ["const:bcad48:8", "const:4:8"]]
- 00bcad48 ["CALLIND", null, ["register:0:8"]]
- 00bcad48 bytes 00013fd6
- 00bcad60 ["INT_ADD", "register:40f0:8", ["const:bcad60:8", "const:4:8"]]
- 00bcad60 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcb188 ["INT_ADD", "register:40f0:8", ["const:bcb188:8", "const:4:8"]]
+ 00bcb188 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcad60 bytes a83f0294
+ 00bcb188 bytes 9e3f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36bc8cd01574f9ff2afbd2ab2bf76bb2"></a>

### [`00bcaec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaec8.md) → [`00bcb2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb2f0.md) _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d660.md) · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5d600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d600.md)
- 新版 呼出元 1件 [`00c5da60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da60.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5da00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.56% / 新版 82.56%

CFGの説明率　旧版 41.46% / 新版 42.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcaec8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcaec8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcaecc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcaec8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcaecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcaed0",
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
      "00bcb2f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bcb2f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcb2f8",
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

- 旧版 [`00bcaec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaec8.md#insn-00bcaec8) · [`00bcaecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaec8.md#insn-00bcaecc) · [`00bcaed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaec8.md#insn-00bcaed0)

~~~diff
- 00bcaec8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bcaec8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bcaec8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00bcaec8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcaec8 bytes f85fbca9
- 00bcaecc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bcaecc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bcaecc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcaecc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcaecc bytes f65701a9
- 00bcaed0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcaed0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcaed0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcaed0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcaed0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47039a6d84a48a7b5a51aa95366a6069"></a>

### [`00bcb098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb098.md) → [`00bcb4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb4c0.md) FUN_00bcb4c0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb098.md#insn-00bcb0a0)
- 新版 `00bcb4c8`（命令位置の公開資料なし）

~~~diff
- 00bcb0a0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bcb0a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bcb4c8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00bcb4c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcb0a0 bytes 600000b4
+ 00bcb4c8 bytes 600000b4
~~~


<a id="compare-3fd5c0c8c0c7fb84a13e6aea2f2885c4"></a>

### [`00bcb0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb0b4.md) → [`00bcb4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb4dc.md) _ZN8firebase4auth15IdTokenListenerD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d660.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5da60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da60.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 71.43% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcb4fc",
      "incomplete_value": true,
      "site": "00bcb4fc",
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
      "definition_site": "00bcb0d4",
      "incomplete_value": true,
      "site": "00bcb0d4",
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
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb110"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bcb538"
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
      "00bcb4ec",
      "READ",
      [
        "storage",
        "00c9b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcb4fc",
      "DATA",
      [
        "storage",
        "00c91500",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bcb4ec",
      "READ",
      [
        "storage",
        "00c9b9b0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcb4fc",
      "DATA",
      [
        "storage",
        "00c91900",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb0b4.md#insn-00bcb110) · [`00bcb0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb0b4.md#insn-00bcb0c4)
- 新版 `00bcb538`（命令位置の公開資料なし） · `00bcb4ec`（命令位置の公開資料なし）

~~~diff
- 00bcb110 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcb110 ["RETURN", null, ["register:0:8"]]
- 00bcb110 bytes c0035fd6
+ 00bcb538 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bcb538 ["RETURN", null, ["register:0:8"]]
+ 00bcb538 bytes c0035fd6
- 00bcb0c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
- 00bcb0c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcb4ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b0:8"]]
+ 00bcb4ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcb0c4 bytes 08d942f9
+ 00bcb4ec bytes 08d944f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26fae800033285a8a226f90117d16060"></a>

### [`00bcb12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb12c.md) → [`00bcb554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb554.md) _ZN8firebase4auth24NotifyAuthStateListenersEPNS0_8AuthDataE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d610.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)
- 新版 呼出元 1件 [`00c5da10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da10.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.79% / 新版 90.79%

CFGの説明率　旧版 63.64% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb130"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb130"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb134"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcb130",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcb134",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcb138",
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
      "00bcb558",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcb55c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcb560",
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

- 旧版 [`00bcb130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb12c.md#insn-00bcb130) · [`00bcb134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb12c.md#insn-00bcb134) · [`00bcb138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb12c.md#insn-00bcb138)

~~~diff
- 00bcb130 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bcb130 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bcb130 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcb130 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcb130 bytes f65702a9
- 00bcb134 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcb134 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcb134 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bcb134 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcb134 bytes f44f03a9
- 00bcb138 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcb138 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcb138 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bcb138 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcb138 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20a73ad18d4dc72f0e69248df894402b"></a>

### [`00bcb354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb354.md) → [`00bcb77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb77c.md) _ZN8firebase4auth22NotifyIdTokenListenersEPNS0_8AuthDataE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5f0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)
- 新版 呼出元 1件 [`00c5d9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9f0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md)

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
    "old": {
      "definition_site": "00bcb3a4",
      "incomplete_value": false,
      "site": "00bcb3a8",
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
            "const:10d:8"
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
      "00bcb7cc",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcb7cc",
      "PARAM",
      [
        "storage",
        "002a61e9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb354.md#insn-00bcb3a8) · [`00bcb380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb354.md#insn-00bcb380) · [`00bcb390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb354.md#insn-00bcb390)
- 新版 `00bcb7d0`（命令位置の公開資料なし） · `00bcb7a8`（命令位置の公開資料なし） · `00bcb7b8`（命令位置の公開資料なし）

~~~diff
- 00bcb3a8 ["INT_ADD", "register:40f0:8", ["const:bcb3a8:8", "const:4:8"]]
- 00bcb3a8 ["CALL", null, ["callee:00c5b130:8"]]
+ 00bcb7d0 ["INT_ADD", "register:40f0:8", ["const:bcb7d0:8", "const:4:8"]]
+ 00bcb7d0 ["CALL", null, ["callee:00c5b130:8"]]
- 00bcb3a8 bytes 623e0294
+ 00bcb7d0 bytes 583e0294
- 00bcb380 ["INT_ADD", "register:40f0:8", ["const:bcb380:8", "const:4:8"]]
- 00bcb380 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcb7a8 ["INT_ADD", "register:40f0:8", ["const:bcb7a8:8", "const:4:8"]]
+ 00bcb7a8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcb380 bytes a03c0294
+ 00bcb7a8 bytes 963c0294
- 00bcb390 ["INT_ADD", "register:40f0:8", ["const:bcb390:8", "const:4:8"]]
- 00bcb390 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00bcb7b8 ["INT_ADD", "register:40f0:8", ["const:bcb7b8:8", "const:4:8"]]
+ 00bcb7b8 ["CALL", null, ["callee:00c5dae0:8"]]
- 00bcb390 bytes d4480294
+ 00bcb7b8 bytes ca480294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4edee30ea13194311e8b0dc42351f077"></a>

### [`00bcb4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb4bc.md) → [`00bcb8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb8e4.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6e0.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5dae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dae0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb4bc.md#insn-00bcb4e0) · [`00bcb4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb4bc.md#insn-00bcb4ec) · [`00bcb4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb4bc.md#insn-00bcb4f4)
- 新版 `00bcb908`（命令位置の公開資料なし） · `00bcb914`（命令位置の公開資料なし） · `00bcb91c`（命令位置の公開資料なし）

~~~diff
- 00bcb4e0 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00bcb908 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00bcb4e0 bytes 60020054
+ 00bcb908 bytes 60020054
- 00bcb4ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcb4ec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bcb914 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcb914 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bcb4ec bytes 880200b5
+ 00bcb914 bytes 880200b5
- 00bcb4f4 ["INT_ADD", "register:40f0:8", ["const:bcb4f4:8", "const:4:8"]]
- 00bcb4f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bcb91c ["INT_ADD", "register:40f0:8", ["const:bcb91c:8", "const:4:8"]]
+ 00bcb91c ["CALL", null, ["callee:00c57e90:8"]]
- 00bcb4f4 bytes 67310294
+ 00bcb91c bytes 5d310294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2585efc00eaf6cc2aa4666d71558781"></a>

### [`00bcb60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb60c.md) → [`00bcba34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcba34.md) _ZNK8firebase4auth4Auth32SendPasswordResetEmailLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcba50",
      "incomplete_value": true,
      "site": "00bcba54",
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
    "old": {
      "definition_site": "00bcb628",
      "incomplete_value": true,
      "site": "00bcb62c",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb60c.md#insn-00bcb62c) · [`00bcb624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb60c.md#insn-00bcb624) · [`00bcb628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb60c.md#insn-00bcb628)
- 新版 `00bcba54`（命令位置の公開資料なし）

~~~diff
- 00bcb62c ["INT_ADD", "register:40f0:8", ["const:bcb62c:8", "const:4:8"]]
- 00bcb62c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcba54 ["INT_ADD", "register:40f0:8", ["const:bcba54:8", "const:4:8"]]
+ 00bcba54 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcb62c bytes f53b0294
+ 00bcba54 bytes eb3b0294
- 00bcb624 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00bcb624 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00bcb624 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00bcb624 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00bcb624 bytes b4620091
- 00bcb628 ["COPY", "register:4000:8", ["register:40a0:8"]]
- 00bcb628 bytes e00314aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3719f746ef50098c9a885ae6e278e0b6"></a>

### [`00bcb7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb7bc.md) → [`00bcbbe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbbe4.md) _ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

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
      "definition_site": "00bcb800",
      "incomplete_value": true,
      "site": "00bcb804",
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
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb7bc.md#insn-00bcb804) · [`00bcb7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb7bc.md#insn-00bcb7dc) · [`00bcb7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb7bc.md#insn-00bcb7e8)
- 新版 `00bcbc2c`（命令位置の公開資料なし） · `00bcbc04`（命令位置の公開資料なし） · `00bcbc10`（命令位置の公開資料なし）

~~~diff
- 00bcb804 ["INT_ADD", "register:40f0:8", ["const:bcb804:8", "const:4:8"]]
- 00bcb804 ["CALL", null, ["callee:00c5ae10:8"]]
+ 00bcbc2c ["INT_ADD", "register:40f0:8", ["const:bcbc2c:8", "const:4:8"]]
+ 00bcbc2c ["CALL", null, ["callee:00c5ae10:8"]]
- 00bcb804 bytes 833c0294
+ 00bcbc2c bytes 793c0294
- 00bcb7dc ["INT_ADD", "register:40f0:8", ["const:bcb7dc:8", "const:4:8"]]
- 00bcb7dc ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcbc04 ["INT_ADD", "register:40f0:8", ["const:bcbc04:8", "const:4:8"]]
+ 00bcbc04 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcb7dc bytes 893b0294
+ 00bcbc04 bytes 7f3b0294
- 00bcb7e8 ["INT_ADD", "register:40f0:8", ["const:bcb7e8:8", "const:4:8"]]
- 00bcb7e8 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bcbc10 ["INT_ADD", "register:40f0:8", ["const:bcbc10:8", "const:4:8"]]
+ 00bcbc10 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bcb7e8 bytes 8a3b0294
+ 00bcbc10 bytes 803b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09613a89cb5926dc14a8f73d100735ee"></a>

### [`00bcb84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb84c.md) → [`00bcbc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbc74.md) _ZNK8firebase4auth4Auth36SignInWithEmailAndPasswordLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb84c.md#insn-00bcb86c) · [`00bcb878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb84c.md#insn-00bcb878) · [`00bcb884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb84c.md#insn-00bcb884)
- 新版 `00bcbc94`（命令位置の公開資料なし） · `00bcbca0`（命令位置の公開資料なし） · `00bcbcac`（命令位置の公開資料なし）

~~~diff
- 00bcb86c ["INT_ADD", "register:40f0:8", ["const:bcb86c:8", "const:4:8"]]
- 00bcb86c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcbc94 ["INT_ADD", "register:40f0:8", ["const:bcbc94:8", "const:4:8"]]
+ 00bcbc94 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcb86c bytes 653b0294
+ 00bcbc94 bytes 5b3b0294
- 00bcb878 ["INT_ADD", "register:40f0:8", ["const:bcb878:8", "const:4:8"]]
- 00bcb878 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bcbca0 ["INT_ADD", "register:40f0:8", ["const:bcbca0:8", "const:4:8"]]
+ 00bcbca0 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bcb878 bytes 663b0294
+ 00bcbca0 bytes 5c3b0294
- 00bcb884 ["INT_ADD", "register:40f0:8", ["const:bcb884:8", "const:4:8"]]
- 00bcb884 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bcbcac ["INT_ADD", "register:40f0:8", ["const:bcbcac:8", "const:4:8"]]
+ 00bcbcac ["CALL", null, ["callee:00c5ac70:8"]]
- 00bcb884 bytes fb3b0294
+ 00bcbcac bytes f13b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1f20159e908f7978682549727d1201d"></a>

### [`00bcb8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb8dc.md) → [`00bcbd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbd04.md) _ZNK8firebase4auth4Auth40CreateUserWithEmailAndPasswordLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

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
      "definition_site": "00bcb8f8",
      "incomplete_value": true,
      "site": "00bcb8fc",
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
    "new": null,
    "old": {
      "definition_site": "00bcb920",
      "incomplete_value": true,
      "site": "00bcb924",
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
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb8dc.md#insn-00bcb8fc) · [`00bcb924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb8dc.md#insn-00bcb924) · [`00bcb908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb8dc.md#insn-00bcb908)
- 新版 `00bcbd24`（命令位置の公開資料なし） · `00bcbd4c`（命令位置の公開資料なし） · `00bcbd30`（命令位置の公開資料なし）

~~~diff
- 00bcb8fc ["INT_ADD", "register:40f0:8", ["const:bcb8fc:8", "const:4:8"]]
- 00bcb8fc ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcbd24 ["INT_ADD", "register:40f0:8", ["const:bcbd24:8", "const:4:8"]]
+ 00bcbd24 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bcb8fc bytes 413b0294
+ 00bcbd24 bytes 373b0294
- 00bcb924 ["INT_ADD", "register:40f0:8", ["const:bcb924:8", "const:4:8"]]
- 00bcb924 ["CALL", null, ["callee:00c5ae10:8"]]
+ 00bcbd4c ["INT_ADD", "register:40f0:8", ["const:bcbd4c:8", "const:4:8"]]
+ 00bcbd4c ["CALL", null, ["callee:00c5ae10:8"]]
- 00bcb924 bytes 3b3c0294
+ 00bcbd4c bytes 313c0294
- 00bcb908 ["INT_ADD", "register:40f0:8", ["const:bcb908:8", "const:4:8"]]
- 00bcb908 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bcbd30 ["INT_ADD", "register:40f0:8", ["const:bcbd30:8", "const:4:8"]]
+ 00bcbd30 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bcb908 bytes 423b0294
+ 00bcbd30 bytes 383b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5923f121c960db3dea897a3304495711"></a>

### [`00bcb984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md) → [`00bcbdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbdac.md) FUN_00bcbdac

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bca368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md) · 呼出先 2件 [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5d630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d630.md)
- 新版 呼出元 1件 [`00bca790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca790.md) · 呼出先 2件 [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5da30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da30.md)

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
    "old": {
      "definition_site": "00bcb99c",
      "incomplete_value": false,
      "site": "00bcb9a8",
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
            "const:b8f:8"
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
      "00bcbdc4",
      "PARAM",
      [
        "storage",
        "002a3b8f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcbdc4",
      "PARAM",
      [
        "storage",
        "002a3c5c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md#insn-00bcb9a8) · [`00bcb99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md#insn-00bcb99c)
- 新版 `00bcbdd0`（命令位置の公開資料なし） · `00bcbdc4`（命令位置の公開資料なし）

~~~diff
- 00bcb9a8 ["INT_ADD", "register:40f0:8", ["const:bcb9a8:8", "const:4:8"]]
- 00bcb9a8 ["CALL", null, ["callee:00c5ade0:8"]]
+ 00bcbdd0 ["INT_ADD", "register:40f0:8", ["const:bcbdd0:8", "const:4:8"]]
+ 00bcbdd0 ["CALL", null, ["callee:00c5ade0:8"]]
- 00bcb9a8 bytes 0e3c0294
+ 00bcbdd0 bytes 043c0294
- 00bcb99c ["COPY", "tmp:0:8", ["const:b8f:8"]]
- 00bcb99c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcb99c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcb99c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcbdc4 ["COPY", "tmp:0:8", ["const:c5c:8"]]
+ 00bcbdc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcbdc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcbdc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcb99c bytes 003c2e91
+ 00bcbdc4 bytes 00703191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c767a083e76b5ee6c0fa601c32945be0"></a>

### [`00bcb9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9bc.md) → [`00bcbde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbde4.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6c0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6c0.md)
- 新版 呼出元 1件 [`00c5dac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dac0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5dac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dac0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcbdf8",
      "incomplete_value": true,
      "site": "00bcbe00",
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
            "register:4008:8"
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


#### 変更候補の命令位置

- 旧版 [`00bcb9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9bc.md#insn-00bcb9d8) · [`00bcb9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9bc.md#insn-00bcb9bc) · [`00bcb9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9bc.md#insn-00bcb9e4)
- 新版 `00bcbe00`（命令位置の公開資料なし） · `00bcbde4`（命令位置の公開資料なし） · `00bcbe0c`（命令位置の公開資料なし）

~~~diff
- 00bcb9d8 ["INT_ADD", "register:40f0:8", ["const:bcb9d8:8", "const:4:8"]]
- 00bcb9d8 ["CALL", null, ["callee:00c5dac0:8"]]
+ 00bcbe00 ["INT_ADD", "register:40f0:8", ["const:bcbe00:8", "const:4:8"]]
+ 00bcbe00 ["CALL", null, ["callee:00c5dac0:8"]]
- 00bcb9d8 bytes 3a470294
+ 00bcbe00 bytes 30470294
- 00bcb9bc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcb9bc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bcbde4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bcbde4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcb9bc bytes e10100b4
+ 00bcbde4 bytes e10100b4
- 00bcb9e4 ["INT_ADD", "register:40f0:8", ["const:bcb9e4:8", "const:4:8"]]
- 00bcb9e4 ["CALL", null, ["callee:00c5dac0:8"]]
+ 00bcbe0c ["INT_ADD", "register:40f0:8", ["const:bcbe0c:8", "const:4:8"]]
+ 00bcbe0c ["CALL", null, ["callee:00c5dac0:8"]]
- 00bcb9e4 bytes 37470294
+ 00bcbe0c bytes 2d470294
~~~


<a id="compare-cf481b0f2940fa11b79ad596c81950a9"></a>

### [`00bcb9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9fc.md) → [`00bcbe24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbe24.md) _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6f0.md) · 呼出先 5件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5daf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5daf0.md) · 呼出先 5件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 61.11% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcba50"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcba54"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcbe78"
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
      "unmatched:00bcba54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbf0c"
      ]
    ],
    [
      "00bcbe8c",
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcbad8",
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
      "00bcbe7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbf0c"
      ]
    ],
    [
      "00bcbe8c",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ],
    [
      "00bcbf00",
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

- 旧版 [`00bcba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9fc.md#insn-00bcba50) · [`00bcba54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9fc.md#insn-00bcba54) · [`00bcba68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9fc.md#insn-00bcba68)
- 新版 `00bcbe90`（命令位置の公開資料なし）

~~~diff
- 00bcba50 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcba50 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bcba50 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bcba50 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bcba50 bytes 1931899a
- 00bcba54 ["INT_EQUAL", "tmp:0:1", ["register:40c8:8", "const:0:8"]]
- 00bcba54 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00bcba54 bytes 990400b4
- 00bcba68 ["INT_ADD", "register:40f0:8", ["const:bcba68:8", "const:4:8"]]
- 00bcba68 ["CALL", null, ["callee:00b402c0:8"]]
+ 00bcbe90 ["INT_ADD", "register:40f0:8", ["const:bcbe90:8", "const:4:8"]]
+ 00bcbe90 ["CALL", null, ["callee:00b402c0:8"]]
- 00bcba68 bytes 0cd1fd97
+ 00bcbe90 bytes 0cd1fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c141c6bcdaeecfd9ce6be8b2429f3873"></a>

### [`00bcbaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbaf4.md) → [`00bcbf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbf1c.md) _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d710.md) · 呼出先 5件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5db10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db10.md) · 呼出先 5件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.71% / 新版 88.71%

CFGの説明率　旧版 27.78% / 新版 26.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbb04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbb04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcbf2c"
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
      "unmatched:00bcbb04",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcbb5c",
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcbb88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbfc4"
      ]
    ]
  ],
  "added": [
    [
      "00bcbf2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcbf84",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ],
    [
      "00bcbfb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbfc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbaf4.md#insn-00bcbb04) · [`00bcbb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbaf4.md#insn-00bcbb60) · [`00bcbb88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbaf4.md#insn-00bcbb88)
- 新版 `00bcbf88`（命令位置の公開資料なし）

~~~diff
- 00bcbb04 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcbb04 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcbb04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bcbb04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcbb04 bytes fd7b04a9
- 00bcbb60 ["INT_ADD", "register:40f0:8", ["const:bcbb60:8", "const:4:8"]]
- 00bcbb60 ["CALL", null, ["callee:00b402c0:8"]]
+ 00bcbf88 ["INT_ADD", "register:40f0:8", ["const:bcbf88:8", "const:4:8"]]
+ 00bcbf88 ["CALL", null, ["callee:00b402c0:8"]]
- 00bcbb60 bytes ced0fd97
+ 00bcbf88 bytes ced0fd97
- 00bcbb88 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bcbb88 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00bcbb88 bytes ab000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08dbdc62423536205ad0a9e6e0ee1fc6"></a>

### [`00bcbbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbbec.md) → [`00bcc014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc014.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6d0.md) · 呼出先 5件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5dad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dad0.md) · 呼出先 5件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 70.59% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbc7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc0a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbc80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcc07c",
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcbc80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc0bc"
      ]
    ]
  ],
  "added": [
    [
      "00bcc07c",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ],
    [
      "00bcc0a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc0bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbbec.md#insn-00bcbc58) · [`00bcbc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbbec.md#insn-00bcbc7c) · [`00bcbc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbbec.md#insn-00bcbc80)
- 新版 `00bcc080`（命令位置の公開資料なし）

~~~diff
- 00bcbc58 ["INT_ADD", "register:40f0:8", ["const:bcbc58:8", "const:4:8"]]
- 00bcbc58 ["CALL", null, ["callee:00b402c0:8"]]
+ 00bcc080 ["INT_ADD", "register:40f0:8", ["const:bcc080:8", "const:4:8"]]
+ 00bcc080 ["CALL", null, ["callee:00b402c0:8"]]
- 00bcbc58 bytes 90d0fd97
+ 00bcc080 bytes 90d0fd97
- 00bcbc7c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bcbc7c ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 00bcbc7c ["INT_ADD", "register:40c0:8", ["register:40c0:8", "const:8:8"]]
- 00bcbc7c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bcbc7c bytes 088700f8
- 00bcbc80 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bcbc80 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00bcbc80 bytes ab000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e757f7c31a200ff682680ebd2597b42"></a>

### [`00bcbce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbce4.md) → [`00bcc10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc10c.md) _INIT_290

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bca0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0a8.md) [`00bca0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0b0.md) [`00bca0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0b4.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bca4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4d0.md) [`00bca4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4d8.md) [`00bca4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4dc.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 64.86% / 新版 64.86%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbd10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbd10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbd14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcbd00",
      "PARAM",
      [
        "storage",
        "011262e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcbd10",
      "WRITE",
      [
        "storage",
        "011262e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcbd10",
      "DATA",
      [
        "storage",
        "002bc0ca",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcc128",
      "PARAM",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc138",
      "WRITE",
      [
        "storage",
        "011266e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc138",
      "DATA",
      [
        "storage",
        "002bc10a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbce4.md#insn-00bcbd10) · [`00bcbd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbce4.md#insn-00bcbd14) · [`00bcbd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbce4.md#insn-00bcbd18)

~~~diff
- 00bcbd10 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bcbd10 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bcbd10 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00bcbd10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcbd10 bytes 082400a9
- 00bcbd14 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00bcbd14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bcbd14 bytes 0a0800f9
- 00bcbd18 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bcbd18 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bcbd18 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:18:8"]]
- 00bcbd18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bcbd18 bytes 1f600039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19f352c0c3f4cd80b2d6559d6109df89"></a>

### [`00bcbee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbee4.md) → [`00bcc30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc30c.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

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
    "old": {
      "definition_site": "00bcbf10",
      "incomplete_value": true,
      "site": "00bcbf10",
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
            "const:328:8"
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
    "old": {
      "definition_site": "00bcbef8",
      "incomplete_value": true,
      "site": "00bcbef8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bcbf04",
      "incomplete_value": false,
      "site": "00bcbf08",
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
            "const:1fc:8"
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
      "00bcc31c",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc32c",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bcc338",
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc31c",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc32c",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      "00bcc338",
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbf08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbee4.md#insn-00bcbf08) · [`00bcbf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbee4.md#insn-00bcbf10) · [`00bcbef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbee4.md#insn-00bcbef4)
- 新版 `00bcc330`（命令位置の公開資料なし） · `00bcc338`（命令位置の公開資料なし） · `00bcc31c`（命令位置の公開資料なし）

~~~diff
- 00bcbf08 ["INT_ADD", "register:40f0:8", ["const:bcbf08:8", "const:4:8"]]
- 00bcbf08 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcc330 ["INT_ADD", "register:40f0:8", ["const:bcc330:8", "const:4:8"]]
+ 00bcc330 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcbf08 bytes 023b0294
+ 00bcc330 bytes f83a0294
- 00bcbf10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00bcbf10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc338 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00bcc338 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcbf10 bytes 609601f9
+ 00bcc338 bytes 609603f9
- 00bcbef4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00bcbef4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcc31c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00bcc31c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcbef4 bytes 689641f9
+ 00bcc31c bytes 689643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d40904bff33b1784ff8d8e8d59ca7dc"></a>

### [`00bcbf24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf24.md) → [`00bcc34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc34c.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bcc378",
      "incomplete_value": true,
      "site": "00bcc378",
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
    "old": {
      "definition_site": "00bcbf50",
      "incomplete_value": true,
      "site": "00bcbf50",
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
            "const:328:8"
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
    "old": {
      "definition_site": "00bcbf38",
      "incomplete_value": true,
      "site": "00bcbf38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc368",
      "incomplete_value": false,
      "site": "00bcc370",
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
    "old": {
      "definition_site": "00bcbf40",
      "incomplete_value": false,
      "site": "00bcbf48",
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
            "const:1fc:8"
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
      "00bcc35c",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc368",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bcc378",
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc35c",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc368",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      "00bcc378",
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf24.md#insn-00bcbf48) · [`00bcbf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf24.md#insn-00bcbf50) · [`00bcbf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf24.md#insn-00bcbf34)
- 新版 `00bcc370`（命令位置の公開資料なし） · `00bcc378`（命令位置の公開資料なし） · `00bcc35c`（命令位置の公開資料なし）

~~~diff
- 00bcbf48 ["INT_ADD", "register:40f0:8", ["const:bcbf48:8", "const:4:8"]]
- 00bcbf48 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcc370 ["INT_ADD", "register:40f0:8", ["const:bcc370:8", "const:4:8"]]
+ 00bcc370 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcbf48 bytes f23a0294
+ 00bcc370 bytes e83a0294
- 00bcbf50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00bcbf50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00bcc378 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcbf50 bytes 609601f9
+ 00bcc378 bytes 609603f9
- 00bcbf34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00bcbf34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcc35c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00bcc35c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcbf34 bytes 689641f9
+ 00bcc35c bytes 689643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5358c39eaae882f127565391be1db76"></a>

### [`00bcbf64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf64.md) → [`00bcc38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc38c.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00bcbf64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbf68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbf68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcbf64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcbf68",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcc39c",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc38c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcc390",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcc39c",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbf64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf64.md#insn-00bcbf64) · [`00bcbf68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf64.md#insn-00bcbf68) · [`00bcbf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf64.md#insn-00bcbf78)
- 新版 `00bcc3a0`（命令位置の公開資料なし）

~~~diff
- 00bcbf64 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bcbf64 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bcbf64 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcbf64 bytes f30f1ef8
- 00bcbf68 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcbf68 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcbf68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcbf68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcbf68 bytes fd7b01a9
- 00bcbf78 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcbf78 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcc3a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcc3a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcbf78 bytes 080100b5
+ 00bcc3a0 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a2bd508e3b7be7a9537149be081f117"></a>

### [`00bcbfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfa8.md) → [`00bcc3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc3d0.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bcc400",
      "incomplete_value": true,
      "site": "00bcc400",
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
    "old": {
      "definition_site": "00bcbfd8",
      "incomplete_value": true,
      "site": "00bcbfd8",
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
            "const:328:8"
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
    "old": {
      "definition_site": "00bcbfbc",
      "incomplete_value": true,
      "site": "00bcbfbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc3ec",
      "incomplete_value": false,
      "site": "00bcc3f8",
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
    "old": {
      "definition_site": "00bcbfc4",
      "incomplete_value": false,
      "site": "00bcbfd0",
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
            "const:1fc:8"
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
      "00bcc3e0",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc3ec",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bcc400",
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc3e0",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc3ec",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ],
    [
      "00bcc400",
      "WRITE",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfa8.md#insn-00bcbfd0) · [`00bcbfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfa8.md#insn-00bcbfd8) · [`00bcbfb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfa8.md#insn-00bcbfb8)
- 新版 `00bcc3f8`（命令位置の公開資料なし） · `00bcc400`（命令位置の公開資料なし） · `00bcc3e0`（命令位置の公開資料なし）

~~~diff
- 00bcbfd0 ["INT_ADD", "register:40f0:8", ["const:bcbfd0:8", "const:4:8"]]
- 00bcbfd0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcc3f8 ["INT_ADD", "register:40f0:8", ["const:bcc3f8:8", "const:4:8"]]
+ 00bcc3f8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcbfd0 bytes d03a0294
+ 00bcc3f8 bytes c63a0294
- 00bcbfd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00bcbfd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc400 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00bcc400 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcbfd8 bytes 609601f9
+ 00bcc400 bytes 609603f9
- 00bcbfb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00bcbfb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcc3e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00bcc3e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcbfb8 bytes 689641f9
+ 00bcc3e0 bytes 689643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bc29e9b53687bb22d253a9c967370f2"></a>

### [`00bcbff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbff8.md) → [`00bcc420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc420.md) _ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc050"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc478"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bcc02c",
      "incomplete_value": true,
      "site": "00bcc038",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:328:8"
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
      "00bcc434",
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bcc02c",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc050",
      "WRITE",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc434",
      "READ",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc454",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc478",
      "WRITE",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbff8.md#insn-00bcc038) · [`00bcc044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbff8.md#insn-00bcc044) · [`00bcc050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbff8.md#insn-00bcc050)
- 新版 `00bcc460`（命令位置の公開資料なし） · `00bcc46c`（命令位置の公開資料なし）

~~~diff
- 00bcc038 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc038 ["INT_ADD", "register:40f0:8", ["const:bcc038:8", "const:4:8"]]
- 00bcc038 ["CALLIND", null, ["register:0:8"]]
+ 00bcc460 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc460 ["INT_ADD", "register:40f0:8", ["const:bcc460:8", "const:4:8"]]
+ 00bcc460 ["CALLIND", null, ["register:0:8"]]
- 00bcc038 bytes 00013fd6
+ 00bcc460 bytes 00013fd6
- 00bcc044 ["INT_ADD", "register:40f0:8", ["const:bcc044:8", "const:4:8"]]
- 00bcc044 ["CALL", null, ["callee:00c5af60:8"]]
+ 00bcc46c ["INT_ADD", "register:40f0:8", ["const:bcc46c:8", "const:4:8"]]
+ 00bcc46c ["CALL", null, ["callee:00c5af60:8"]]
- 00bcc044 bytes c73a0294
+ 00bcc46c bytes bd3a0294
- 00bcc050 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bcc050 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:330:8"]]
- 00bcc050 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bcc050 bytes a0c20c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f5455aa669cae8755006ca91ea91a15"></a>

### [`00bcc064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc064.md) → [`00bcc48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc48c.md) _ZN8firebase4auth4auth12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bcc4c8",
      "incomplete_value": true,
      "site": "00bcc4c8",
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
    "old": {
      "definition_site": "00bcc0a0",
      "incomplete_value": true,
      "site": "00bcc0a0",
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
            "const:330:8"
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
      "definition_site": "00bcc4e8",
      "incomplete_value": true,
      "site": "00bcc4e8",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc0c0",
      "incomplete_value": true,
      "site": "00bcc0c0",
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
            "const:328:8"
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
      "definition_site": "00bcc4a4",
      "incomplete_value": true,
      "site": "00bcc4a4",
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
      "definition_site": "00bcc07c",
      "incomplete_value": true,
      "site": "00bcc07c",
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
      "00bcc4a0",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc4ac",
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc4c8",
      "WRITE",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc4a0",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc4ac",
      "READ",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc4c8",
      "WRITE",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc064.md#insn-00bcc0a0) · [`00bcc0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc064.md#insn-00bcc0bc) · [`00bcc0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc064.md#insn-00bcc0c0)
- 新版 `00bcc4c8`（命令位置の公開資料なし） · `00bcc4e4`（命令位置の公開資料なし） · `00bcc4e8`（命令位置の公開資料なし）

~~~diff
- 00bcc0a0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bcc0a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bcc0a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:330:8"]]
- 00bcc0a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bcc4c8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bcc4c8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bcc4c8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:730:8"]]
+ 00bcc4c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bcc0a0 bytes bfc20c39
+ 00bcc4c8 bytes bfc21c39
- 00bcc0bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc0bc ["INT_ADD", "register:40f0:8", ["const:bcc0bc:8", "const:4:8"]]
- 00bcc0bc ["CALLIND", null, ["register:0:8"]]
+ 00bcc4e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc4e4 ["INT_ADD", "register:40f0:8", ["const:bcc4e4:8", "const:4:8"]]
+ 00bcc4e4 ["CALLIND", null, ["register:0:8"]]
- 00bcc0bc bytes 00013fd6
+ 00bcc4e4 bytes 00013fd6
- 00bcc0c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00bcc0c0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bcc0c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bcc4e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
+ 00bcc4e8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bcc4e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bcc0c0 bytes 9f9601f9
+ 00bcc4e8 bytes 9f9603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f4d995c5cfcb36e46637ed0d637d79b"></a>

### [`00bcc0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc0d4.md) → [`00bcc4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc4fc.md) _ZN8firebase4auth4auth14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bcc0d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc0d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc0d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc0d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc0d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc0e8",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc4fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcc500",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcc510",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc0d4.md#insn-00bcc0d4) · [`00bcc0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc0d4.md#insn-00bcc0d8) · [`00bcc0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc0d4.md#insn-00bcc0f0)

~~~diff
- 00bcc0d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcc0d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcc0d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bcc0d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc0d4 bytes f44fbea9
- 00bcc0d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc0d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc0d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcc0d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc0d8 bytes fd7b01a9
- 00bcc0f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc0f0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcc0f0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecc3864c7bac34adf3cd874f6fa27a2a"></a>

### [`00bcc144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc144.md) → [`00bcc56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc56c.md) _ZN8firebase4auth4auth11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bcc588",
      "incomplete_value": false,
      "site": "00bcc58c",
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
      "definition_site": "00bcc160",
      "incomplete_value": false,
      "site": "00bcc164",
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
      "definition_site": "00bcc598",
      "incomplete_value": true,
      "site": "00bcc5a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bcc170",
      "incomplete_value": true,
      "site": "00bcc17c",
      "value": [
        "LOAD",
        "8",
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
      "00bcc588",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bcc598",
      "DATA",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc588",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bcc598",
      "DATA",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc144.md#insn-00bcc164) · [`00bcc160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc144.md#insn-00bcc160) · [`00bcc16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc144.md#insn-00bcc16c)
- 新版 `00bcc58c`（命令位置の公開資料なし） · `00bcc588`（命令位置の公開資料なし） · `00bcc594`（命令位置の公開資料なし）

~~~diff
- 00bcc164 ["INT_ADD", "register:40f0:8", ["const:bcc164:8", "const:4:8"]]
- 00bcc164 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcc58c ["INT_ADD", "register:40f0:8", ["const:bcc58c:8", "const:4:8"]]
+ 00bcc58c ["CALL", null, ["callee:00c5b000:8"]]
- 00bcc164 bytes a73a0294
+ 00bcc58c bytes 9d3a0294
- 00bcc160 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bcc160 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc160 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc160 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcc588 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bcc588 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc588 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc588 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcc160 bytes 00680a91
+ 00bcc588 bytes 009c0d91
- 00bcc16c ["COPY", "tmp:0:8", ["const:338:8"]]
- 00bcc16c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc16c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc16c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcc594 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 00bcc594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcc16c bytes 08e10c91
+ 00bcc594 bytes 08e11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-858c73a224213f80042e9e467b13d508"></a>

### [`00bcc180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc180.md) → [`00bcc5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc5a8.md) _ZN8firebase4auth4auth13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00bcc1c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc5e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc19c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc194",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc19c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc5ec"
      ]
    ],
    [
      "unmatched:00bcc1a4",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc5bc",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc5c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc5ec"
      ]
    ],
    [
      "00bcc5cc",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc180.md#insn-00bcc19c) · [`00bcc1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc180.md#insn-00bcc1b8) · [`00bcc1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc180.md#insn-00bcc1c0)
- 新版 `00bcc5e0`（命令位置の公開資料なし）

~~~diff
- 00bcc19c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc19c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc19c bytes 410100b5
- 00bcc1b8 ["INT_ADD", "register:40f0:8", ["const:bcc1b8:8", "const:4:8"]]
- 00bcc1b8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcc5e0 ["INT_ADD", "register:40f0:8", ["const:bcc5e0:8", "const:4:8"]]
+ 00bcc5e0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc1b8 bytes 563a0294
+ 00bcc5e0 bytes 4c3a0294
- 00bcc1c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00bcc1c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc1c0 bytes 809601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea4c1b381591eb58a5dc699ddc041f8a"></a>

### [`00bcc22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc22c.md) → [`00bcc654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc654.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
    "old": {
      "definition_site": "00bcc258",
      "incomplete_value": true,
      "site": "00bcc258",
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
            "const:3d0:8"
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
    "old": {
      "definition_site": "00bcc240",
      "incomplete_value": true,
      "site": "00bcc240",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bcc24c",
      "incomplete_value": false,
      "site": "00bcc250",
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
            "const:bf5:8"
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
      "00bcc664",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc674",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      "00bcc680",
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc664",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc674",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      "00bcc680",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc22c.md#insn-00bcc250) · [`00bcc258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc22c.md#insn-00bcc258) · [`00bcc23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc22c.md#insn-00bcc23c)
- 新版 `00bcc678`（命令位置の公開資料なし） · `00bcc680`（命令位置の公開資料なし） · `00bcc664`（命令位置の公開資料なし）

~~~diff
- 00bcc250 ["INT_ADD", "register:40f0:8", ["const:bcc250:8", "const:4:8"]]
- 00bcc250 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcc678 ["INT_ADD", "register:40f0:8", ["const:bcc678:8", "const:4:8"]]
+ 00bcc678 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc250 bytes 303a0294
+ 00bcc678 bytes 263a0294
- 00bcc258 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
- 00bcc258 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc680 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00bcc680 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc258 bytes 60ea01f9
+ 00bcc680 bytes 60ea03f9
- 00bcc23c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
- 00bcc23c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcc664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00bcc664 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcc23c bytes 68ea41f9
+ 00bcc664 bytes 68ea43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09631dfb78730e6ede461f3abf959db2"></a>

### [`00bcc26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc26c.md) → [`00bcc694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc694.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
    "old": {
      "definition_site": "00bcc298",
      "incomplete_value": true,
      "site": "00bcc298",
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
            "const:3d0:8"
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
    "old": {
      "definition_site": "00bcc280",
      "incomplete_value": true,
      "site": "00bcc280",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bcc288",
      "incomplete_value": false,
      "site": "00bcc290",
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
            "const:bf5:8"
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
      "00bcc6a4",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc6b0",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      "00bcc6c0",
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc6a4",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc6b0",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      "00bcc6c0",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc26c.md#insn-00bcc290) · [`00bcc298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc26c.md#insn-00bcc298) · [`00bcc27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc26c.md#insn-00bcc27c)
- 新版 `00bcc6b8`（命令位置の公開資料なし） · `00bcc6c0`（命令位置の公開資料なし） · `00bcc6a4`（命令位置の公開資料なし）

~~~diff
- 00bcc290 ["INT_ADD", "register:40f0:8", ["const:bcc290:8", "const:4:8"]]
- 00bcc290 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcc6b8 ["INT_ADD", "register:40f0:8", ["const:bcc6b8:8", "const:4:8"]]
+ 00bcc6b8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc290 bytes 203a0294
+ 00bcc6b8 bytes 163a0294
- 00bcc298 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
- 00bcc298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc6c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00bcc6c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc298 bytes 60ea01f9
+ 00bcc6c0 bytes 60ea03f9
- 00bcc27c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
- 00bcc27c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcc6a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00bcc6a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcc27c bytes 68ea41f9
+ 00bcc6a4 bytes 68ea43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d74b7059076d959bee03ba395b50581c"></a>

### [`00bcc2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2ac.md) → [`00bcc6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc6d4.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bcc704",
      "incomplete_value": true,
      "site": "00bcc704",
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
    "old": {
      "definition_site": "00bcc2dc",
      "incomplete_value": true,
      "site": "00bcc2dc",
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
            "const:3d0:8"
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
    "old": {
      "definition_site": "00bcc2c0",
      "incomplete_value": true,
      "site": "00bcc2c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc6f4",
      "incomplete_value": false,
      "site": "00bcc6fc",
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
    "old": {
      "definition_site": "00bcc2cc",
      "incomplete_value": false,
      "site": "00bcc2d4",
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
            "const:bf5:8"
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
      "00bcc6e4",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc6f4",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      "00bcc704",
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc6e4",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc6f4",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ],
    [
      "00bcc704",
      "WRITE",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2ac.md#insn-00bcc2d4) · [`00bcc2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2ac.md#insn-00bcc2dc) · [`00bcc2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2ac.md#insn-00bcc2bc)
- 新版 `00bcc6fc`（命令位置の公開資料なし） · `00bcc704`（命令位置の公開資料なし） · `00bcc6e4`（命令位置の公開資料なし）

~~~diff
- 00bcc2d4 ["INT_ADD", "register:40f0:8", ["const:bcc2d4:8", "const:4:8"]]
- 00bcc2d4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcc6fc ["INT_ADD", "register:40f0:8", ["const:bcc6fc:8", "const:4:8"]]
+ 00bcc6fc ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc2d4 bytes 0f3a0294
+ 00bcc6fc bytes 053a0294
- 00bcc2dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
- 00bcc2dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc704 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00bcc704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc2dc bytes 60ea01f9
+ 00bcc704 bytes 60ea03f9
- 00bcc2bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
- 00bcc2bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcc6e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
+ 00bcc6e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcc2bc bytes 68ea41f9
+ 00bcc6e4 bytes 68ea43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86f797466eaebe29023707934fa425bc"></a>

### [`00bcc2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2f0.md) → [`00bcc718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc718.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

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
      "site": "00bcc320"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc748"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc304"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcc728",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc74c"
      ]
    ],
    [
      "unmatched:00bcc30c",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc728",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc72c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc74c"
      ]
    ],
    [
      "00bcc734",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2f0.md#insn-00bcc304) · [`00bcc318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2f0.md#insn-00bcc318) · [`00bcc320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2f0.md#insn-00bcc320)
- 新版 `00bcc740`（命令位置の公開資料なし）

~~~diff
- 00bcc304 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcc304 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc304 bytes 080100b5
- 00bcc318 ["INT_ADD", "register:40f0:8", ["const:bcc318:8", "const:4:8"]]
- 00bcc318 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcc740 ["INT_ADD", "register:40f0:8", ["const:bcc740:8", "const:4:8"]]
+ 00bcc740 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc318 bytes fe390294
+ 00bcc740 bytes f4390294
- 00bcc320 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
- 00bcc320 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc320 bytes 60ea01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdcd142037506504e535573474f22c38"></a>

### [`00bcc340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc340.md) → [`00bcc768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc768.md) _ZN8firebase4auth17signinmethodquery15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc398"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc7c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc79c",
      "incomplete_value": true,
      "site": "00bcc7a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc374",
      "incomplete_value": true,
      "site": "00bcc380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3d0:8"
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
      "00bcc77c",
      "READ",
      [
        "storage",
        "011263d8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bcc374",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc398",
      "WRITE",
      [
        "storage",
        "011263d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc77c",
      "READ",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc79c",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc7c0",
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc340.md#insn-00bcc380) · [`00bcc398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc340.md#insn-00bcc398)
- 新版 `00bcc7a8`（命令位置の公開資料なし） · `00bcc7c0`（命令位置の公開資料なし）

~~~diff
- 00bcc380 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc380 ["INT_ADD", "register:40f0:8", ["const:bcc380:8", "const:4:8"]]
- 00bcc380 ["CALLIND", null, ["register:0:8"]]
+ 00bcc7a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc7a8 ["INT_ADD", "register:40f0:8", ["const:bcc7a8:8", "const:4:8"]]
+ 00bcc7a8 ["CALLIND", null, ["register:0:8"]]
- 00bcc380 bytes 00013fd6
+ 00bcc7a8 bytes 00013fd6
- 00bcc398 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bcc398 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3d8:8"]]
- 00bcc398 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bcc398 bytes a0620f39
+ 00bcc7c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bcc7c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7d8:8"]]
+ 00bcc7c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bcc7c0 bytes a0621f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e38805e7ab86e2192b78cfab68df2d0"></a>

### [`00bcc3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc3ac.md) → [`00bcc7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc7d4.md) _ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 28.57% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc3e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00bcc408",
      "incomplete_value": true,
      "site": "00bcc408",
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
            "const:3d0:8"
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
      "site": "00bcc810"
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
      "00bcc7e8",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc7f4",
      "READ",
      [
        "storage",
        "011263d8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bcc3e8",
      "WRITE",
      [
        "storage",
        "011263d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc7e8",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc7f4",
      "READ",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc810",
      "WRITE",
      [
        "storage",
        "011267d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc3ac.md#insn-00bcc3c4) · [`00bcc3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc3ac.md#insn-00bcc3e8) · [`00bcc404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc3ac.md#insn-00bcc404)
- 新版 `00bcc7ec`（命令位置の公開資料なし） · `00bcc82c`（命令位置の公開資料なし）

~~~diff
- 00bcc3c4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc3c4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bcc7ec ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bcc7ec ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bcc3c4 bytes 410200b4
+ 00bcc7ec bytes 410200b4
- 00bcc3e8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bcc3e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bcc3e8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3d8:8"]]
- 00bcc3e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bcc3e8 bytes bf620f39
- 00bcc404 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc404 ["INT_ADD", "register:40f0:8", ["const:bcc404:8", "const:4:8"]]
- 00bcc404 ["CALLIND", null, ["register:0:8"]]
+ 00bcc82c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc82c ["INT_ADD", "register:40f0:8", ["const:bcc82c:8", "const:4:8"]]
+ 00bcc82c ["CALLIND", null, ["register:0:8"]]
- 00bcc404 bytes 00013fd6
+ 00bcc82c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ba44428fafd337e7444583c31dd8a09"></a>

### [`00bcc41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc41c.md) → [`00bcc844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc844.md) _ZN8firebase4auth17signinmethodquery14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00bcc45c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc884"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc438"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc430",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc438",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc888"
      ]
    ],
    [
      "unmatched:00bcc440",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc858",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc860",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc888"
      ]
    ],
    [
      "00bcc868",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc41c.md#insn-00bcc438) · [`00bcc454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc41c.md#insn-00bcc454) · [`00bcc45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc41c.md#insn-00bcc45c)
- 新版 `00bcc87c`（命令位置の公開資料なし）

~~~diff
- 00bcc438 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc438 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcc438 bytes 410100b5
- 00bcc454 ["INT_ADD", "register:40f0:8", ["const:bcc454:8", "const:4:8"]]
- 00bcc454 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcc87c ["INT_ADD", "register:40f0:8", ["const:bcc87c:8", "const:4:8"]]
+ 00bcc87c ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc454 bytes af390294
+ 00bcc87c bytes a5390294
- 00bcc45c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d0:8"]]
- 00bcc45c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc45c bytes 80ea01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-903327197b84bfc74f192c8a6a7330a3"></a>

### [`00bcc48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc48c.md) → [`00bcc8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8b4.md) _ZN8firebase4auth17signinmethodquery11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00bcc4a8",
      "incomplete_value": false,
      "site": "00bcc4ac",
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
    "old": {
      "definition_site": "00bcc4b8",
      "incomplete_value": true,
      "site": "00bcc4c4",
      "value": [
        "LOAD",
        "8",
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
      "00bcc8d0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bcc8e0",
      "DATA",
      [
        "storage",
        "011263e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc8d0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bcc8e0",
      "DATA",
      [
        "storage",
        "011267e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc48c.md#insn-00bcc4ac) · [`00bcc4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc48c.md#insn-00bcc4a8) · [`00bcc4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc48c.md#insn-00bcc4b4)
- 新版 `00bcc8d4`（命令位置の公開資料なし） · `00bcc8d0`（命令位置の公開資料なし） · `00bcc8dc`（命令位置の公開資料なし）

~~~diff
- 00bcc4ac ["INT_ADD", "register:40f0:8", ["const:bcc4ac:8", "const:4:8"]]
- 00bcc4ac ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcc8d4 ["INT_ADD", "register:40f0:8", ["const:bcc8d4:8", "const:4:8"]]
+ 00bcc8d4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcc4ac bytes d5390294
+ 00bcc8d4 bytes cb390294
- 00bcc4a8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bcc4a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc4a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc4a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcc8d0 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bcc8d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc8d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc8d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcc4a8 bytes 00680a91
+ 00bcc8d0 bytes 009c0d91
- 00bcc4b4 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 00bcc4b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc4b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc4b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcc8dc ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 00bcc8dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc8dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc8dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcc4b4 bytes 08810f91
+ 00bcc8dc bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d39bc4850979873cb086c1ad5abaf919"></a>

### [`00bcc4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc4c8.md) → [`00bcc8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc8f0.md) _ZN8firebase4auth17signinmethodquery13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00bcc508"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc930"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc4e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc4dc",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc4e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc934"
      ]
    ],
    [
      "unmatched:00bcc4ec",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc904",
      "READ",
      [
        "storage",
        "011267d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc90c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc934"
      ]
    ],
    [
      "00bcc914",
      "PARAM",
      [
        "storage",
        "002a2cc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc4c8.md#insn-00bcc4e4) · [`00bcc500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc4c8.md#insn-00bcc500) · [`00bcc508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc4c8.md#insn-00bcc508)
- 新版 `00bcc928`（命令位置の公開資料なし）

~~~diff
- 00bcc4e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc4e4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcc4e4 bytes 410100b5
- 00bcc500 ["INT_ADD", "register:40f0:8", ["const:bcc500:8", "const:4:8"]]
- 00bcc500 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcc928 ["INT_ADD", "register:40f0:8", ["const:bcc928:8", "const:4:8"]]
+ 00bcc928 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc500 bytes 84390294
+ 00bcc928 bytes 7a390294
- 00bcc508 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d0:8"]]
- 00bcc508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc508 bytes 80ea01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e308ca7d3667735c8799601927fe7ea1"></a>

### [`00bcc574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc574.md) → [`00bcc99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc99c.md) _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00bcc5a0",
      "incomplete_value": true,
      "site": "00bcc5a0",
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
            "const:3f0:8"
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
    "old": {
      "definition_site": "00bcc588",
      "incomplete_value": true,
      "site": "00bcc588",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bcc594",
      "incomplete_value": false,
      "site": "00bcc598",
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
            "const:b9a:8"
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
      "00bcc9ac",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc9bc",
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ],
    [
      "00bcc9c8",
      "WRITE",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc9ac",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc9bc",
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ],
    [
      "00bcc9c8",
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc574.md#insn-00bcc598) · [`00bcc5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc574.md#insn-00bcc5a0) · [`00bcc584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc574.md#insn-00bcc584)
- 新版 `00bcc9c0`（命令位置の公開資料なし） · `00bcc9c8`（命令位置の公開資料なし） · `00bcc9ac`（命令位置の公開資料なし）

~~~diff
- 00bcc598 ["INT_ADD", "register:40f0:8", ["const:bcc598:8", "const:4:8"]]
- 00bcc598 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcc9c0 ["INT_ADD", "register:40f0:8", ["const:bcc9c0:8", "const:4:8"]]
+ 00bcc9c0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc598 bytes 5e390294
+ 00bcc9c0 bytes 54390294
- 00bcc5a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
- 00bcc5a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc9c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
+ 00bcc9c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc5a0 bytes 60fa01f9
+ 00bcc9c8 bytes 60fa03f9
- 00bcc584 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
- 00bcc584 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcc9ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
+ 00bcc9ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcc584 bytes 68fa41f9
+ 00bcc9ac bytes 68fa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-384d015984c70cb56358b95c49d2c7b1"></a>

### [`00bcc5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5f4.md) → [`00bcca1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca1c.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00bcc5f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc5f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc5f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc5f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc5f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcca2c",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcca1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcca20",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcca2c",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5f4.md#insn-00bcc5f4) · [`00bcc5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5f4.md#insn-00bcc5f8) · [`00bcc608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5f4.md#insn-00bcc608)
- 新版 `00bcca30`（命令位置の公開資料なし）

~~~diff
- 00bcc5f4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bcc5f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bcc5f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc5f4 bytes f30f1ef8
- 00bcc5f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc5f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc5f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcc5f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc5f8 bytes fd7b01a9
- 00bcc608 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcc608 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcca30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcca30 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bcc608 bytes 080100b5
+ 00bcca30 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb44fea2bc0e5aa07c007d7f38a327f6"></a>

### [`00bcc638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc638.md) → [`00bcca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcca60.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bcc668",
      "incomplete_value": true,
      "site": "00bcc668",
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
            "const:3f0:8"
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
    "old": {
      "definition_site": "00bcc64c",
      "incomplete_value": true,
      "site": "00bcc64c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bcc654",
      "incomplete_value": false,
      "site": "00bcc660",
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
            "const:b9a:8"
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
      "00bcca70",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcca7c",
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ],
    [
      "00bcca90",
      "WRITE",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcca70",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcca7c",
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ],
    [
      "00bcca90",
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc638.md#insn-00bcc660) · [`00bcc668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc638.md#insn-00bcc668) · [`00bcc648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc638.md#insn-00bcc648)
- 新版 `00bcca88`（命令位置の公開資料なし） · `00bcca90`（命令位置の公開資料なし） · `00bcca70`（命令位置の公開資料なし）

~~~diff
- 00bcc660 ["INT_ADD", "register:40f0:8", ["const:bcc660:8", "const:4:8"]]
- 00bcc660 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bcca88 ["INT_ADD", "register:40f0:8", ["const:bcca88:8", "const:4:8"]]
+ 00bcca88 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc660 bytes 2c390294
+ 00bcca88 bytes 22390294
- 00bcc668 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
- 00bcc668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcca90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
+ 00bcca90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc668 bytes 60fa01f9
+ 00bcca90 bytes 60fa03f9
- 00bcc648 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
- 00bcc648 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcca70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f0:8"]]
+ 00bcca70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcc648 bytes 68fa41f9
+ 00bcca70 bytes 68fa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff846be4bd572ad3eb11cb0a0d9b59a3"></a>

### [`00bcc6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc6f4.md) → [`00bccb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb1c.md) _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 14.29% / 新版 16.67%

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
      "site": "00bcc730"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc750"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccb58"
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
      "00bccb30",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccb34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcc754"
      ]
    ],
    [
      "00bccb3c",
      "READ",
      [
        "storage",
        "011263f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bccb30",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccb34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccb7c"
      ]
    ],
    [
      "00bccb3c",
      "READ",
      [
        "storage",
        "011267f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc6f4.md#insn-00bcc730) · [`00bcc738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc6f4.md#insn-00bcc738) · [`00bcc74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc6f4.md#insn-00bcc74c)

~~~diff
- 00bcc730 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bcc730 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bcc730 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3f8:8"]]
- 00bcc730 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bcc730 bytes bfe20f39
- 00bcc738 ["INT_ADD", "register:40f0:8", ["const:bcc738:8", "const:4:8"]]
- 00bcc738 ["CALL", null, ["callee:00c5af60:8"]]
- 00bcc738 bytes 0a390294
- 00bcc74c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc74c ["INT_ADD", "register:40f0:8", ["const:bcc74c:8", "const:4:8"]]
- 00bcc74c ["CALLIND", null, ["register:0:8"]]
- 00bcc74c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edc92816fa3c1ef1daa35ef7391ab502"></a>

### [`00bcc764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc764.md) → [`00bccb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccb8c.md) _ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bcc7a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccbcc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc780"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc778",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc780",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccbd0"
      ]
    ],
    [
      "unmatched:00bcc788",
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bccba0",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccba8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccbd0"
      ]
    ],
    [
      "00bccbb0",
      "PARAM",
      [
        "storage",
        "002b5bda",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc764.md#insn-00bcc780) · [`00bcc79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc764.md#insn-00bcc79c) · [`00bcc7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc764.md#insn-00bcc7a4)
- 新版 `00bccbc4`（命令位置の公開資料なし）

~~~diff
- 00bcc780 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc780 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc780 bytes 410100b5
- 00bcc79c ["INT_ADD", "register:40f0:8", ["const:bcc79c:8", "const:4:8"]]
- 00bcc79c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bccbc4 ["INT_ADD", "register:40f0:8", ["const:bccbc4:8", "const:4:8"]]
+ 00bccbc4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc79c bytes dd380294
+ 00bccbc4 bytes d3380294
- 00bcc7a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f0:8"]]
- 00bcc7a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc7a4 bytes 80fa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbcbcb47d4c61cba9fbe29a84419f8fe"></a>

### [`00bcc810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc810.md) → [`00bccc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccc38.md) _ZN8firebase4auth11jnilistener13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bcc810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc814"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc810",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc814",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc824",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bccc38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bccc3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bccc4c",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc810.md#insn-00bcc810) · [`00bcc814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc810.md#insn-00bcc814) · [`00bcc82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc810.md#insn-00bcc82c)

~~~diff
- 00bcc810 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcc810 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcc810 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bcc810 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc810 bytes f44fbea9
- 00bcc814 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc814 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc814 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcc814 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc814 bytes fd7b01a9
- 00bcc82c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcc82c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bcc82c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6ac84776358b58f654a98d765ad5d30"></a>

### [`00bcc880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc880.md) → [`00bccca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccca8.md) _ZN8firebase4auth11jnilistener10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bcccc4",
      "incomplete_value": false,
      "site": "00bcccc8",
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
      "definition_site": "00bcc89c",
      "incomplete_value": false,
      "site": "00bcc8a0",
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
      "definition_site": "00bcccd4",
      "incomplete_value": true,
      "site": "00bccce0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bcc8ac",
      "incomplete_value": true,
      "site": "00bcc8b8",
      "value": [
        "LOAD",
        "8",
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
      "00bcccc4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bcccd4",
      "DATA",
      [
        "storage",
        "01126410",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcccc4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bcccd4",
      "DATA",
      [
        "storage",
        "01126810",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc880.md#insn-00bcc8a0) · [`00bcc89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc880.md#insn-00bcc89c) · [`00bcc8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc880.md#insn-00bcc8a8)
- 新版 `00bcccc8`（命令位置の公開資料なし） · `00bcccc4`（命令位置の公開資料なし） · `00bcccd0`（命令位置の公開資料なし）

~~~diff
- 00bcc8a0 ["INT_ADD", "register:40f0:8", ["const:bcc8a0:8", "const:4:8"]]
- 00bcc8a0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcccc8 ["INT_ADD", "register:40f0:8", ["const:bcccc8:8", "const:4:8"]]
+ 00bcccc8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcc8a0 bytes d8380294
+ 00bcccc8 bytes ce380294
- 00bcc89c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bcc89c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc89c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcc89c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcccc4 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bcccc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcccc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcccc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcc89c bytes 00441191
+ 00bcccc4 bytes 00781491
- 00bcc8a8 ["COPY", "tmp:0:8", ["const:410:8"]]
- 00bcc8a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc8a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc8a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcccd0 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 00bcccd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcccd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcccd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcc8a8 bytes 08411091
+ 00bcccd0 bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c221feea69953019f3d4b21a8099eefb"></a>

### [`00bcc8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8bc.md) → [`00bccce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccce4.md) _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc8e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccd10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcccf8",
      "incomplete_value": true,
      "site": "00bcccf8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc8d0",
      "incomplete_value": true,
      "site": "00bcc8d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bcccf4",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc8dc",
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcc8e0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bcccf4",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccd04",
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      "00bccd08",
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

- 旧版 [`00bcc8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8bc.md#insn-00bcc8d0) · [`00bcc8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8bc.md#insn-00bcc8e0) · [`00bcc8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8bc.md#insn-00bcc8e8)
- 新版 `00bcccf8`（命令位置の公開資料なし）

~~~diff
- 00bcc8d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcc8d0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcccf8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcccf8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc8d0 bytes e80000b5
+ 00bcccf8 bytes e80000b5
- 00bcc8e0 ["INT_ADD", "register:40f0:8", ["const:bcc8e0:8", "const:4:8"]]
- 00bcc8e0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc8e0 bytes 8c380294
- 00bcc8e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00bcc8e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc8e8 bytes 600e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa1ced00ef9aff7a0c24c343c86c3db4"></a>

### [`00bcc93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc93c.md) → [`00bccd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd64.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bccd94",
      "incomplete_value": true,
      "site": "00bccd94",
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
    "old": {
      "definition_site": "00bcc96c",
      "incomplete_value": true,
      "site": "00bcc96c",
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
            "const:418:8"
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
    "old": {
      "definition_site": "00bcc950",
      "incomplete_value": true,
      "site": "00bcc950",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bccd84",
      "incomplete_value": false,
      "site": "00bccd8c",
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
    "old": {
      "definition_site": "00bcc95c",
      "incomplete_value": false,
      "site": "00bcc964",
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
            "const:8bd:8"
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
      "00bccd74",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccd84",
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ],
    [
      "00bccd94",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bccd74",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccd84",
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      "00bccd94",
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc93c.md#insn-00bcc964) · [`00bcc96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc93c.md#insn-00bcc96c) · [`00bcc94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc93c.md#insn-00bcc94c)
- 新版 `00bccd8c`（命令位置の公開資料なし） · `00bccd94`（命令位置の公開資料なし） · `00bccd74`（命令位置の公開資料なし）

~~~diff
- 00bcc964 ["INT_ADD", "register:40f0:8", ["const:bcc964:8", "const:4:8"]]
- 00bcc964 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bccd8c ["INT_ADD", "register:40f0:8", ["const:bccd8c:8", "const:4:8"]]
+ 00bccd8c ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc964 bytes 6b380294
+ 00bccd8c bytes 61380294
- 00bcc96c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00bcc96c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bccd94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:818:8"]]
+ 00bccd94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc96c bytes 600e02f9
+ 00bccd94 bytes 600e04f9
- 00bcc94c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00bcc94c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bccd74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:818:8"]]
+ 00bccd74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcc94c bytes 680e42f9
+ 00bccd74 bytes 680e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af9f9fa5e88d0c36bcbfd70d856cc030"></a>

### [`00bcc980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc980.md) → [`00bccda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccda8.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc9b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccdd8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bccdbc",
      "incomplete_value": true,
      "site": "00bccdbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc994",
      "incomplete_value": true,
      "site": "00bcc994",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bccdb8",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc99c",
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcc9b0",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bccdb8",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccdc4",
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      "00bccdd8",
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc980.md#insn-00bcc994) · [`00bcc9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc980.md#insn-00bcc9a8) · [`00bcc9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc980.md#insn-00bcc9b0)
- 新版 `00bccdbc`（命令位置の公開資料なし） · `00bccdd0`（命令位置の公開資料なし）

~~~diff
- 00bcc994 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcc994 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bccdbc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bccdbc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc994 bytes 080100b5
+ 00bccdbc bytes 080100b5
- 00bcc9a8 ["INT_ADD", "register:40f0:8", ["const:bcc9a8:8", "const:4:8"]]
- 00bcc9a8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bccdd0 ["INT_ADD", "register:40f0:8", ["const:bccdd0:8", "const:4:8"]]
+ 00bccdd0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc9a8 bytes 5a380294
+ 00bccdd0 bytes 50380294
- 00bcc9b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00bcc9b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc9b0 bytes 600e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c56080276f183e22f787facff72cdbd"></a>

### [`00bcc9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc9d0.md) → [`00bccdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccdf8.md) _ZN8firebase4auth21jni_id_token_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "site": "00bcc9d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc9d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc9d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc9d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc9d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc9d8",
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
      "00bccdf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bccdfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcce00",
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

- 旧版 [`00bcc9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc9d0.md#insn-00bcc9d0) · [`00bcc9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc9d0.md#insn-00bcc9d4) · [`00bcc9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc9d0.md#insn-00bcc9d8)

~~~diff
- 00bcc9d0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bcc9d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcc9d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc9d0 bytes f50f1df8
- 00bcc9d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcc9d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcc9d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcc9d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc9d4 bytes f44f01a9
- 00bcc9d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc9d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc9d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcc9d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc9d8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-674ad46d78d250bf33d5db7efe5ae280"></a>

### [`00bcca3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcca3c.md) → [`00bcce64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcce64.md) _ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00bcca3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcca40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcca40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcca3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcca40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcca44",
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
      "00bcce64",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcce68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcce6c",
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

- 旧版 [`00bcca3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcca3c.md#insn-00bcca3c) · [`00bcca40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcca3c.md#insn-00bcca40) · [`00bcca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcca3c.md#insn-00bcca44)

~~~diff
- 00bcca3c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bcca3c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcca3c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcca3c bytes f50f1df8
- 00bcca40 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcca40 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcca40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcca40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcca40 bytes f44f01a9
- 00bcca44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcca44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcca44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcca44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcca44 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34bafbd4e25f16cae3d2f8358ec8872c"></a>

### [`00bccaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccaac.md) → [`00bcced4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcced4.md) _ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00bccaec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccf14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccac8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bccac0",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bccac8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccf18"
      ]
    ],
    [
      "unmatched:00bccad0",
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bccee8",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccf18"
      ]
    ],
    [
      "00bccef8",
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccaac.md#insn-00bccac8) · [`00bccae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccaac.md#insn-00bccae4) · [`00bccaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccaac.md#insn-00bccaec)
- 新版 `00bccf0c`（命令位置の公開資料なし）

~~~diff
- 00bccac8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bccac8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bccac8 bytes 410100b5
- 00bccae4 ["INT_ADD", "register:40f0:8", ["const:bccae4:8", "const:4:8"]]
- 00bccae4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bccf0c ["INT_ADD", "register:40f0:8", ["const:bccf0c:8", "const:4:8"]]
+ 00bccf0c ["CALL", null, ["callee:00c5af10:8"]]
- 00bccae4 bytes 0b380294
+ 00bccf0c bytes 01380294
- 00bccaec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
- 00bccaec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bccaec bytes 800e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-445f9153e085b9b9d3e2b5e4718f68d2"></a>

### [`00bccb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb58.md) → [`00bccf80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf80.md) _ZN8firebase4auth21jni_id_token_listener13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bccb98",
      "incomplete_value": true,
      "site": "00bccb98",
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
            "const:418:8"
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
    "old": {
      "definition_site": "00bccb74",
      "incomplete_value": true,
      "site": "00bccb74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bccb7c",
      "incomplete_value": false,
      "site": "00bccb90",
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
            "const:8bd:8"
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
      "00bccf94",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccfa4",
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ],
    [
      "00bccfc0",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bccf94",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccfa4",
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ],
    [
      "00bccfc0",
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb58.md#insn-00bccb90) · [`00bccb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb58.md#insn-00bccb98) · [`00bccb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb58.md#insn-00bccb6c)
- 新版 `00bccfb8`（命令位置の公開資料なし） · `00bccfc0`（命令位置の公開資料なし） · `00bccf94`（命令位置の公開資料なし）

~~~diff
- 00bccb90 ["INT_ADD", "register:40f0:8", ["const:bccb90:8", "const:4:8"]]
- 00bccb90 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bccfb8 ["INT_ADD", "register:40f0:8", ["const:bccfb8:8", "const:4:8"]]
+ 00bccfb8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bccb90 bytes e0370294
+ 00bccfb8 bytes d6370294
- 00bccb98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
- 00bccb98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bccfc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:818:8"]]
+ 00bccfc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bccb98 bytes 800e02f9
+ 00bccfc0 bytes 800e04f9
- 00bccb6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
- 00bccb6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bccf94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:818:8"]]
+ 00bccf94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bccb6c bytes 810e42f9
+ 00bccf94 bytes 810e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-805d0361c6f410332b41c2a49d8d0187"></a>

### [`00bccc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccc04.md) → [`00bcd02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd02c.md) _ZN8firebase4auth18CacheAuthMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d840.md) · 呼出先 3件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5dc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc40.md) · 呼出先 3件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 37.86% / 新版 37.86%

CFGの説明率　旧版 18.75% / 新版 17.14%

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
      "site": "00bccc50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccd00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bccc20",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bccc2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bccc54"
      ]
    ],
    [
      "unmatched:00bccc34",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcd048",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd054",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcd07c"
      ]
    ],
    [
      "00bcd05c",
      "PARAM",
      [
        "storage",
        "002ac23c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccc04.md#insn-00bccc2c) · [`00bccc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccc04.md#insn-00bccc48) · [`00bccc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccc04.md#insn-00bccc50)

~~~diff
- 00bccc2c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bccc2c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bccc2c bytes 410100b5
- 00bccc48 ["INT_ADD", "register:40f0:8", ["const:bccc48:8", "const:4:8"]]
- 00bccc48 ["CALL", null, ["callee:00c5af10:8"]]
- 00bccc48 bytes b2370294
- 00bccc50 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:328:8"]]
- 00bccc50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bccc50 bytes c09601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaea8de7406fff1da81f53ae879ab1ce"></a>

### [`00bcce34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcce34.md) → [`00bcd25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd25c.md) _ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d860.md) · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5dc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc60.md) · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 28.24% / 新版 28.24%

CFGの説明率　旧版 7.14% / 新版 7.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcce70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcce90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccebc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcd270",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd278",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcce94"
      ]
    ],
    [
      "00bcd280",
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcd270",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd278",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcd2bc"
      ]
    ],
    [
      "00bcd280",
      "READ",
      [
        "storage",
        "01126730",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcce5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcce34.md#insn-00bcce5c) · [`00bcce6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcce34.md#insn-00bcce6c) · [`00bcce70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcce34.md#insn-00bcce70)

~~~diff
- 00bcce5c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00bcce5c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcce5c bytes c8000034
- 00bcce6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcce6c ["INT_ADD", "register:40f0:8", ["const:bcce6c:8", "const:4:8"]]
- 00bcce6c ["CALLIND", null, ["register:0:8"]]
- 00bcce6c bytes 00013fd6
- 00bcce70 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bcce70 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bcce70 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:330:8"]]
- 00bcce70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bcce70 bytes bfc20c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-930c4eb44c5f1e21467367c79c9056c4"></a>

### [`00bccf88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccf88.md) → [`00bcd3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd3b0.md) _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d830.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 1件 [`00c5dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc30.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "site": "00bccfe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcd408"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bccfb8",
      "incomplete_value": true,
      "site": "00bccfc8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "unmatched:00bccfc0",
      "READ",
      [
        "storage",
        "01126340",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcd000",
      "PARAM",
      [
        "storage",
        "002b8c49",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcd3e8",
      "READ",
      [
        "storage",
        "01126740",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd428",
      "PARAM",
      [
        "storage",
        "002b8c89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccf88.md#insn-00bccfc8) · [`00bccfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccf88.md#insn-00bccfe0) · [`00bcd008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccf88.md#insn-00bcd008)
- 新版 `00bcd3f0`（命令位置の公開資料なし） · `00bcd430`（命令位置の公開資料なし）

~~~diff
- 00bccfc8 ["INT_ADD", "register:40f0:8", ["const:bccfc8:8", "const:4:8"]]
- 00bccfc8 ["CALL", null, ["callee:00497834:8"]]
+ 00bcd3f0 ["INT_ADD", "register:40f0:8", ["const:bcd3f0:8", "const:4:8"]]
+ 00bcd3f0 ["CALL", null, ["callee:00497834:8"]]
- 00bccfc8 bytes 0b2ae397
+ 00bcd3f0 bytes 1129e397
- 00bccfe0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bccfe0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bccfe0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00bccfe0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bccfe0 bytes e113979a
- 00bcd008 ["INT_ADD", "register:40f0:8", ["const:bcd008:8", "const:4:8"]]
- 00bcd008 ["CALL", null, ["callee:00c5b130:8"]]
+ 00bcd430 ["INT_ADD", "register:40f0:8", ["const:bcd430:8", "const:4:8"]]
+ 00bcd430 ["CALL", null, ["callee:00c5b130:8"]]
- 00bcd008 bytes 4a370294
+ 00bcd430 bytes 40370294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b10e5c7126d0b3c44ec329e3c57ccc6a"></a>

### [`00bcd044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd044.md) → [`00bcd46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd46c.md) _ZN8firebase4auth14SetEmulatorJniEPNS0_8AuthDataEPKcj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bcd084",
      "incomplete_value": true,
      "site": "00bcd098",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:388:8"
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
      "unmatched:00bcd084",
      "READ",
      [
        "storage",
        "01126388",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcd4ac",
      "READ",
      [
        "storage",
        "01126788",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd044.md#insn-00bcd098) · [`00bcd064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd044.md#insn-00bcd064) · [`00bcd078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd044.md#insn-00bcd078)
- 新版 `00bcd4c0`（命令位置の公開資料なし） · `00bcd48c`（命令位置の公開資料なし） · `00bcd4a0`（命令位置の公開資料なし）

~~~diff
- 00bcd098 ["INT_ADD", "register:40f0:8", ["const:bcd098:8", "const:4:8"]]
- 00bcd098 ["CALL", null, ["callee:00574cec:8"]]
+ 00bcd4c0 ["INT_ADD", "register:40f0:8", ["const:bcd4c0:8", "const:4:8"]]
+ 00bcd4c0 ["CALL", null, ["callee:00574cec:8"]]
- 00bcd098 bytes 059fe697
+ 00bcd4c0 bytes 0b9ee697
- 00bcd064 ["INT_ADD", "register:40f0:8", ["const:bcd064:8", "const:4:8"]]
- 00bcd064 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bcd48c ["INT_ADD", "register:40f0:8", ["const:bcd48c:8", "const:4:8"]]
+ 00bcd48c ["CALL", null, ["callee:00c5b080:8"]]
- 00bcd064 bytes 07370294
+ 00bcd48c bytes fd360294
- 00bcd078 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd078 ["INT_ADD", "register:40f0:8", ["const:bcd078:8", "const:4:8"]]
- 00bcd078 ["CALLIND", null, ["register:0:8"]]
+ 00bcd4a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd4a0 ["INT_ADD", "register:40f0:8", ["const:bcd4a0:8", "const:4:8"]]
+ 00bcd4a0 ["CALLIND", null, ["register:0:8"]]
- 00bcd078 bytes 00013fd6
+ 00bcd4a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1ba4bd0e55e291e64dfb104f4b3484a"></a>

### [`00bcd0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd0c4.md) → [`00bcd4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd4ec.md) _ZN8firebase4auth13CheckEmulatorEPNS0_8AuthDataE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d820.md) · 呼出先 9件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c60.md) [`00c594a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c594a0.md)
- 新版 呼出元 1件 [`00c5dc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc20.md) · 呼出先 9件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58060.md) [`00c598a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c598a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.07% / 新版 67.07%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd0ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcd514"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd0f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcd0e8",
      "PARAM",
      [
        "storage",
        "002baed3",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcd0ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd0f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c598a0"
      ]
    ]
  ],
  "added": [
    [
      "00bcd510",
      "PARAM",
      [
        "storage",
        "002baf13",
        null,
        "string"
      ]
    ],
    [
      "00bcd514",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00bcd518",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c598a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd0c4.md#insn-00bcd0ec) · [`00bcd0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd0c4.md#insn-00bcd0f0) · [`00bcd0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd0c4.md#insn-00bcd0f4)

~~~diff
- 00bcd0ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00bcd0ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bcd0ec bytes e80f00f9
- 00bcd0f0 ["INT_ADD", "register:40f0:8", ["const:bcd0f0:8", "const:4:8"]]
- 00bcd0f0 ["CALL", null, ["callee:00c598a0:8"]]
- 00bcd0f0 bytes ec300294
- 00bcd0f4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bcd0f4 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00bcd0f4 bytes 200700b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ab4b7115708a8ac26d99aa5d557978b"></a>

### [`00bcd22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd22c.md) → [`00bcd654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd654.md) _ZN8firebase4auth18CreatePlatformAuthEPNS_3AppE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5d0.md) · 呼出先 21件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5aaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaa0.md)
- 新版 呼出元 1件 [`00c5d9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9d0.md) · 呼出先 21件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aea0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 80.65% / 新版 86.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00bcd270",
      "incomplete_value": true,
      "site": "00bcd270",
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
            "const:440:8"
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
    "old": {
      "definition_site": "00bcd280",
      "incomplete_value": true,
      "site": "00bcd294",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:328:8"
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
    "old": {
      "definition_site": "00bcd284",
      "incomplete_value": true,
      "site": "00bcd294",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:338:8"
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
      "00bcd684",
      "READ",
      [
        "storage",
        "01126440",
        null,
        "undefined4"
      ]
    ],
    [
      "00bcd698",
      "WRITE",
      [
        "storage",
        "01126440",
        null,
        "undefined4"
      ]
    ],
    [
      "00bcd6a8",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcd684",
      "READ",
      [
        "storage",
        "01126840",
        null,
        "undefined4"
      ]
    ],
    [
      "00bcd698",
      "WRITE",
      [
        "storage",
        "01126840",
        null,
        "undefined4"
      ]
    ],
    [
      "00bcd6a8",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd22c.md#insn-00bcd270) · [`00bcd294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd22c.md#insn-00bcd294) · [`00bcd2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd22c.md#insn-00bcd2b0)
- 新版 `00bcd698`（命令位置の公開資料なし） · `00bcd6bc`（命令位置の公開資料なし） · `00bcd6d8`（命令位置の公開資料なし）

~~~diff
- 00bcd270 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:440:8"]]
- 00bcd270 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00bcd698 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:840:8"]]
+ 00bcd698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00bcd270 bytes e84204b9
+ 00bcd698 bytes e84208b9
- 00bcd294 ["INT_ADD", "register:40f0:8", ["const:bcd294:8", "const:4:8"]]
- 00bcd294 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00bcd6bc ["INT_ADD", "register:40f0:8", ["const:bcd6bc:8", "const:4:8"]]
+ 00bcd6bc ["CALL", null, ["callee:00c5aba0:8"]]
- 00bcd294 bytes 43350294
+ 00bcd6bc bytes 39350294
- 00bcd2b0 ["INT_ADD", "register:40f0:8", ["const:bcd2b0:8", "const:4:8"]]
- 00bcd2b0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcd6d8 ["INT_ADD", "register:40f0:8", ["const:bcd6d8:8", "const:4:8"]]
+ 00bcd6d8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcd2b0 bytes 54360294
+ 00bcd6d8 bytes 4a360294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a22cd170155f7525752d7ba837b29581"></a>

### [`00bcd468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd468.md) → [`00bcd890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd890.md) _ZN8firebase4auth4Auth16InitPlatformAuthEPNS0_8AuthDataE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d640.md) · 呼出先 6件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d820.md) [`00c5d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d830.md)
- 新版 呼出元 1件 [`00c5da40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da40.md) · 呼出先 6件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5dc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc20.md) [`00c5dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bcd48c",
      "incomplete_value": true,
      "site": "00bcd49c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f0:8"
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
    "old": {
      "definition_site": "00bcd490",
      "incomplete_value": true,
      "site": "00bcd49c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:400:8"
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
    "old": {
      "definition_site": "00bcd4ac",
      "incomplete_value": true,
      "site": "00bcd4bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:360:8"
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
      "unmatched:00bcd48c",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcd490",
      "READ",
      [
        "storage",
        "01126400",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcd4ac",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcd8b4",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd8b8",
      "READ",
      [
        "storage",
        "01126800",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd8d4",
      "READ",
      [
        "storage",
        "01126760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd468.md#insn-00bcd49c) · [`00bcd4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd468.md#insn-00bcd4bc) · [`00bcd4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd468.md#insn-00bcd4e8)
- 新版 `00bcd8c4`（命令位置の公開資料なし） · `00bcd8e4`（命令位置の公開資料なし） · `00bcd910`（命令位置の公開資料なし）

~~~diff
- 00bcd49c ["INT_ADD", "register:40f0:8", ["const:bcd49c:8", "const:4:8"]]
- 00bcd49c ["CALL", null, ["callee:005896f4:8"]]
+ 00bcd8c4 ["INT_ADD", "register:40f0:8", ["const:bcd8c4:8", "const:4:8"]]
+ 00bcd8c4 ["CALL", null, ["callee:005896f4:8"]]
- 00bcd49c bytes 86f0e697
+ 00bcd8c4 bytes 8cefe697
- 00bcd4bc ["INT_ADD", "register:40f0:8", ["const:bcd4bc:8", "const:4:8"]]
- 00bcd4bc ["CALL", null, ["callee:00574cec:8"]]
+ 00bcd8e4 ["INT_ADD", "register:40f0:8", ["const:bcd8e4:8", "const:4:8"]]
+ 00bcd8e4 ["CALL", null, ["callee:00574cec:8"]]
- 00bcd4bc bytes fc9de697
+ 00bcd8e4 bytes 029de697
- 00bcd4e8 ["INT_ADD", "register:40f0:8", ["const:bcd4e8:8", "const:4:8"]]
- 00bcd4e8 ["CALL", null, ["callee:005896f4:8"]]
+ 00bcd910 ["INT_ADD", "register:40f0:8", ["const:bcd910:8", "const:4:8"]]
+ 00bcd910 ["CALL", null, ["callee:005896f4:8"]]
- 00bcd4e8 bytes 73f0e697
+ 00bcd910 bytes 79efe697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-148e9e8871d0ec5c4e5b29c0a03375a3"></a>

### [`00bcd530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd530.md) → [`00bcd958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcd958.md) _ZN8firebase4auth4Auth19DestroyPlatformAuthEPNS0_8AuthDataE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d650.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab00.md) [`00c5abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abd0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 1件 [`00c5da50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da50.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af00.md) [`00c5afd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afd0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 44.44% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00bcd638",
      "incomplete_value": true,
      "site": "00bcd638",
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
            "const:440:8"
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
    "old": {
      "definition_site": "00bcd57c",
      "incomplete_value": true,
      "site": "00bcd588",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:408:8"
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
    "old": {
      "definition_site": "00bcd598",
      "incomplete_value": true,
      "site": "00bcd5a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:368:8"
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
      "unmatched:00bcd57c",
      "READ",
      [
        "storage",
        "01126408",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcd598",
      "READ",
      [
        "storage",
        "01126368",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcd5b4",
      "READ",
      [
        "storage",
        "01126430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcd9a4",
      "READ",
      [
        "storage",
        "01126808",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd9c0",
      "READ",
      [
        "storage",
        "01126768",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd9dc",
      "READ",
      [
        "storage",
        "01126830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd530.md#insn-00bcd588) · [`00bcd5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd530.md#insn-00bcd5a8) · [`00bcd5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd530.md#insn-00bcd5c0)
- 新版 `00bcd9b0`（命令位置の公開資料なし） · `00bcd9d0`（命令位置の公開資料なし） · `00bcd9e8`（命令位置の公開資料なし）

~~~diff
- 00bcd588 ["INT_ADD", "register:40f0:8", ["const:bcd588:8", "const:4:8"]]
- 00bcd588 ["CALL", null, ["callee:00574cec:8"]]
+ 00bcd9b0 ["INT_ADD", "register:40f0:8", ["const:bcd9b0:8", "const:4:8"]]
+ 00bcd9b0 ["CALL", null, ["callee:00574cec:8"]]
- 00bcd588 bytes c99de697
+ 00bcd9b0 bytes cf9ce697
- 00bcd5a8 ["INT_ADD", "register:40f0:8", ["const:bcd5a8:8", "const:4:8"]]
- 00bcd5a8 ["CALL", null, ["callee:00574cec:8"]]
+ 00bcd9d0 ["INT_ADD", "register:40f0:8", ["const:bcd9d0:8", "const:4:8"]]
+ 00bcd9d0 ["CALL", null, ["callee:00574cec:8"]]
- 00bcd5a8 bytes c19de697
+ 00bcd9d0 bytes c79ce697
- 00bcd5c0 ["INT_ADD", "register:40f0:8", ["const:bcd5c0:8", "const:4:8"]]
- 00bcd5c0 ["CALL", null, ["callee:00574cec:8"]]
+ 00bcd9e8 ["INT_ADD", "register:40f0:8", ["const:bcd9e8:8", "const:4:8"]]
+ 00bcd9e8 ["CALL", null, ["callee:00574cec:8"]]
- 00bcd5c0 bytes bb9de697
+ 00bcd9e8 bytes c19ce697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12326505fba73c50a54de551d678ead8"></a>

### [`00bcd68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd68c.md) → [`00bcdab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdab4.md) _ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d590.md) · 呼出先 5件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5baf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5baf0.md) [`00c5d680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d680.md)
- 新版 呼出元 1件 [`00c5d990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d990.md) · 呼出先 5件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5bef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bef0.md) [`00c5da80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da80.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd68c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd690"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd690"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcd68c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd690",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd694",
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
      "00bcdab4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcdab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcdabc",
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

- 旧版 [`00bcd68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd68c.md#insn-00bcd68c) · [`00bcd690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd68c.md#insn-00bcd690) · [`00bcd694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd68c.md#insn-00bcd694)

~~~diff
- 00bcd68c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bcd68c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcd68c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcd68c bytes f50f1df8
- 00bcd690 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcd690 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcd690 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcd690 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcd690 bytes f44f01a9
- 00bcd694 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcd694 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcd694 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcd694 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcd694 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04c5f724635221baca9344d254840dc5"></a>

### [`00bcd71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd71c.md) → [`00bcdb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb44.md) _ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5d610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d610.md) [`00c5d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d830.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5da10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da10.md) [`00c5dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc30.md)

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
      "definition_site": "00bcd728",
      "incomplete_value": true,
      "site": "00bcd730",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd71c.md#insn-00bcd730)
- 新版 `00bcdb58`（命令位置の公開資料なし）

~~~diff
- 00bcd730 ["INT_ADD", "register:40f0:8", ["const:bcd730:8", "const:4:8"]]
- 00bcd730 ["CALL", null, ["callee:00c5dc30:8"]]
+ 00bcdb58 ["INT_ADD", "register:40f0:8", ["const:bcdb58:8", "const:4:8"]]
+ 00bcdb58 ["CALL", null, ["callee:00c5dc30:8"]]
- 00bcd730 bytes 40400294
+ 00bcdb58 bytes 36400294
~~~


<a id="compare-599bc100b9f085b74d76cb7e133ea150"></a>

### [`00bcd788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md) → [`00bcdbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) _ZN8firebase4auth4Auth22FetchProvidersForEmailEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcda8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcda8c.md) [`00bcf478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf478.md) [`00bcf604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf604.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcdeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdeb4.md) [`00bcf8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf8a0.md) [`00bcfa2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfa2c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 15.38% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd78c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd78c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd790"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcd78c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd790",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd794",
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
      "00bcdbb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bcdbb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bcdbbc",
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

- 旧版 [`00bcd78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md#insn-00bcd78c) · [`00bcd790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md#insn-00bcd790) · [`00bcd794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md#insn-00bcd794)

~~~diff
- 00bcd78c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bcd78c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bcd78c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bcd78c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcd78c bytes fa6704a9
- 00bcd790 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bcd790 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bcd790 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bcd790 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcd790 bytes f85f05a9
- 00bcd794 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bcd794 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bcd794 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bcd794 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcd794 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e3424f4c433cb5bbf8f8710bd0184c1"></a>

### [`00bcd988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd988.md) → [`00bcddb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcddb0.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFut

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8e0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7d0.md)
- 新版 呼出元 1件 [`00c5dce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dce0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 41.67% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcdde0",
      "incomplete_value": true,
      "site": "00bcdde4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:70:8"
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
    "old": {
      "definition_site": "00bcd9b8",
      "incomplete_value": true,
      "site": "00bcd9bc",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bcd9c8",
      "incomplete_value": true,
      "site": "00bcd9d0",
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
            "const:8:8"
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
      "definition_site": "00bcd9cc",
      "incomplete_value": true,
      "site": "00bcd9d0",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd988.md#insn-00bcd9bc) · [`00bcd9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd988.md#insn-00bcd9d0) · [`00bcda40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd988.md#insn-00bcda40)
- 新版 `00bcdde4`（命令位置の公開資料なし） · `00bcddf8`（命令位置の公開資料なし）

~~~diff
- 00bcd9bc ["INT_ADD", "register:40f0:8", ["const:bcd9bc:8", "const:4:8"]]
- 00bcd9bc ["CALL", null, ["callee:00c5dd10:8"]]
+ 00bcdde4 ["INT_ADD", "register:40f0:8", ["const:bcdde4:8", "const:4:8"]]
+ 00bcdde4 ["CALL", null, ["callee:00c5dd10:8"]]
- 00bcd9bc bytes d53f0294
+ 00bcdde4 bytes cb3f0294
- 00bcd9d0 ["INT_ADD", "register:40f0:8", ["const:bcd9d0:8", "const:4:8"]]
- 00bcd9d0 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bcddf8 ["INT_ADD", "register:40f0:8", ["const:bcddf8:8", "const:4:8"]]
+ 00bcddf8 ["CALL", null, ["callee:00c5ae00:8"]]
- 00bcd9d0 bytes 0c340294
+ 00bcddf8 bytes 02340294
- 00bcda40 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcda40 ["RETURN", null, ["register:0:8"]]
- 00bcda40 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87739202910b90951405e2749b1fed9f"></a>

### [`00bcda8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcda8c.md) → [`00bcdeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdeb4.md) FUN_00bcdeb4

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bcd788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md) · 呼出先 10件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00bcdbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) · 呼出先 10件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.24% / 新版 96.24%

CFGの説明率　旧版 55.32% / 新版 54.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdc38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bce060"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdb50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcdf0c",
      "PARAM",
      [
        "storage",
        "002a0c58",
        null,
        "string"
      ]
    ],
    [
      "00bcdf1c",
      "READ",
      [
        "storage",
        "011263e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcdb50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcdfa0"
      ]
    ]
  ],
  "added": [
    [
      "00bcdf0c",
      "PARAM",
      [
        "storage",
        "002a0d25",
        null,
        "string"
      ]
    ],
    [
      "00bcdf1c",
      "READ",
      [
        "storage",
        "011267e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcdf78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcdfa0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcdae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcda8c.md#insn-00bcdae8) · [`00bcdb00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcda8c.md#insn-00bcdb00) · [`00bcdb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcda8c.md#insn-00bcdb50)
- 新版 `00bcdf10`（命令位置の公開資料なし） · `00bcdf28`（命令位置の公開資料なし）

~~~diff
- 00bcdae8 ["INT_ADD", "register:40f0:8", ["const:bcdae8:8", "const:4:8"]]
- 00bcdae8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcdf10 ["INT_ADD", "register:40f0:8", ["const:bcdf10:8", "const:4:8"]]
+ 00bcdf10 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcdae8 bytes 46340294
+ 00bcdf10 bytes 3c340294
- 00bcdb00 ["INT_ADD", "register:40f0:8", ["const:bcdb00:8", "const:4:8"]]
- 00bcdb00 ["CALL", null, ["callee:00497834:8"]]
+ 00bcdf28 ["INT_ADD", "register:40f0:8", ["const:bcdf28:8", "const:4:8"]]
+ 00bcdf28 ["CALL", null, ["callee:00497834:8"]]
- 00bcdb00 bytes 3d27e397
+ 00bcdf28 bytes 4326e397
- 00bcdb50 ["CBRANCH", null, ["local:b11:8", "register:102:1"]]
- 00bcdb50 bytes 42010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fd60fa9520c978cd1f8804fa4da8ef2"></a>

### [`00bcdca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdca0.md) → [`00bce0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce0c8.md) _ZN8firebase4auth4Auth21SignInWithCustomTokenEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.82% / 新版 90.82%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdcd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdd90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdd90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcdcd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bce13c",
      "READ",
      [
        "storage",
        "01126398",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcdd8c",
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bce0fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bce13c",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00bce1b4",
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcdcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdca0.md#insn-00bcdcd4) · [`00bcdd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdca0.md#insn-00bcdd28) · [`00bcdd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdca0.md#insn-00bcdd50)
- 新版 `00bce150`（命令位置の公開資料なし） · `00bce178`（命令位置の公開資料なし）

~~~diff
- 00bcdcd4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00bcdcd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bcdcd4 bytes e81700f9
- 00bcdd28 ["INT_ADD", "register:40f0:8", ["const:bcdd28:8", "const:4:8"]]
- 00bcdd28 ["CALL", null, ["callee:00497834:8"]]
+ 00bce150 ["INT_ADD", "register:40f0:8", ["const:bce150:8", "const:4:8"]]
+ 00bce150 ["CALL", null, ["callee:00497834:8"]]
- 00bcdd28 bytes b326e397
+ 00bce150 bytes b925e397
- 00bcdd50 ["INT_ADD", "register:40f0:8", ["const:bcdd50:8", "const:4:8"]]
- 00bcdd50 ["CALL", null, ["callee:00c5dcd0:8"]]
+ 00bce178 ["INT_ADD", "register:40f0:8", ["const:bce178:8", "const:4:8"]]
+ 00bce178 ["CALL", null, ["callee:00c5dcd0:8"]]
- 00bcdd50 bytes e03e0294
+ 00bce178 bytes d63e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fe71dbca46316abff5fd7127a9d678c"></a>

### [`00bcde64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcde64.md) → [`00bce28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce28c.md) _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d800.md) · 呼出先 7件 [`00bcf8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5dc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc00.md) · 呼出先 7件 [`00bcfcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.69% / 新版 70.69%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 15件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcde98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdeac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdeb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcde98",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bce318",
      "READ",
      [
        "storage",
        "00c9b5e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bce318",
      "PARAM",
      [
        "storage",
        "00bcf8b0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bce2c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bce318",
      "READ",
      [
        "storage",
        "00c9b9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bce318",
      "PARAM",
      [
        "storage",
        "00bcfcd8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcde98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcde64.md#insn-00bcde98) · [`00bcdeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcde64.md#insn-00bcdeac) · [`00bcdeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcde64.md#insn-00bcdeb8)

~~~diff
- 00bcde98 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00bcde98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bcde98 bytes e80f00f9
- 00bcdeac ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bcdeac ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00bcdeac ["INT_ADD", "register:4040:8", ["register:4040:8", "const:38:8"]]
- 00bcdeac ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00bcdeac bytes 1f8d03f8
- 00bcdeb8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bcdeb8 ["INT_ADD", "register:40b8:8", ["register:40b8:8", "const:30:8"]]
- 00bcdeb8 ["STORE", null, ["const:1b1:8", "register:40b8:8", "tmp:0:8"]]
- 00bcdeb8 bytes e80e03f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4df7074f01ea3a1d698474672c5ffdc"></a>

### [`00bcdfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdfb0.md) → [`00bce3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce3d8.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8d0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7c0.md)
- 新版 呼出元 1件 [`00c5dcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dcd0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dbc0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.69% / 新版 82.69%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdfb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdfb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcdfb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcdfb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcdfb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcdfbc",
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
      "00bce3dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bce3e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bce3e4",
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

- 旧版 [`00bcdfb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdfb0.md#insn-00bcdfb4) · [`00bcdfb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdfb0.md#insn-00bcdfb8) · [`00bcdfbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdfb0.md#insn-00bcdfbc)

~~~diff
- 00bcdfb4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bcdfb4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bcdfb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bcdfb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcdfb4 bytes f65704a9
- 00bcdfb8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcdfb8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcdfb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bcdfb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcdfb8 bytes f44f05a9
- 00bcdfbc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcdfbc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcdfbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bcdfbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcdfbc bytes fd7b06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b98373a765b48b35b47b5b086723a5e3"></a>

### [`00bce468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce468.md) → [`00bce890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce890.md) _ZN8firebase4auth4Auth35SignInAndRetrieveDataWithCredentialERKNS0_10CredentialE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5e0.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5a9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a9e0.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.24% / 新版 75.24%

CFGの説明率　旧版 16.67% / 新版 4.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce46c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce46c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce470"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bce46c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bce470",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bce474",
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
      "00bce894",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bce898",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bce89c",
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

- 旧版 [`00bce46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce468.md#insn-00bce46c) · [`00bce470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce468.md#insn-00bce470) · [`00bce474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce468.md#insn-00bce474)

~~~diff
- 00bce46c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bce46c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bce46c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bce46c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bce46c bytes fa6704a9
- 00bce470 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bce470 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bce470 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bce470 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bce470 bytes f85f05a9
- 00bce474 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bce474 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bce474 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bce474 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bce474 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9f940aca01c9481fe6c1535ce994521"></a>

### [`00bce654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce654.md) → [`00bcea7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcea7c.md) _ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a790.md) · 呼出先 3件 [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5ab90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab90.md) · 呼出先 3件 [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bceac0",
      "incomplete_value": true,
      "site": "00bceac8",
      "value": [
        "live",
        "register:4098:8"
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
      "definition_site": "00bceacc",
      "incomplete_value": true,
      "site": "00bceadc",
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
      "unmatched:00bce690",
      "PARAM",
      [
        "storage",
        "002b5b82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bceab8",
      "PARAM",
      [
        "storage",
        "002b5bc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bce694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce654.md#insn-00bce694) · [`00bce6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce654.md#insn-00bce6a0) · [`00bce6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce654.md#insn-00bce6b4)
- 新版 `00bceabc`（命令位置の公開資料なし） · `00bceac8`（命令位置の公開資料なし） · `00bceadc`（命令位置の公開資料なし）

~~~diff
- 00bce694 ["INT_ADD", "register:40f0:8", ["const:bce694:8", "const:4:8"]]
- 00bce694 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bceabc ["INT_ADD", "register:40f0:8", ["const:bceabc:8", "const:4:8"]]
+ 00bceabc ["CALL", null, ["callee:00c5b000:8"]]
- 00bce694 bytes 5b310294
+ 00bceabc bytes 51310294
- 00bce6a0 ["INT_ADD", "register:40f0:8", ["const:bce6a0:8", "const:4:8"]]
- 00bce6a0 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bceac8 ["INT_ADD", "register:40f0:8", ["const:bceac8:8", "const:4:8"]]
+ 00bceac8 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bce6a0 bytes 74300294
+ 00bceac8 bytes 6a300294
- 00bce6b4 ["INT_ADD", "register:40f0:8", ["const:bce6b4:8", "const:4:8"]]
- 00bce6b4 ["CALL", null, ["callee:00c5abe0:8"]]
+ 00bceadc ["INT_ADD", "register:40f0:8", ["const:bceadc:8", "const:4:8"]]
+ 00bceadc ["CALL", null, ["callee:00c5abe0:8"]]
- 00bce6b4 bytes 4b300294
+ 00bceadc bytes 41300294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82114054f29de5b8867524670d3f1e93"></a>

### [`00bce6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce6d8.md) → [`00bceb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bceb00.md) _ZN8firebase4auth4Auth17SignInAnonymouslyEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.82% / 新版 78.82%

CFGの説明率　旧版 2.94% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce6dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce6dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce6e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bce6dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bce6e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bce6e4",
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
      "00bceb04",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bceb08",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bceb0c",
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

- 旧版 [`00bce6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce6d8.md#insn-00bce6dc) · [`00bce6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce6d8.md#insn-00bce6e0) · [`00bce6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce6d8.md#insn-00bce6e4)

~~~diff
- 00bce6dc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bce6dc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bce6dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bce6dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bce6dc bytes fa6703a9
- 00bce6e0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bce6e0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bce6e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bce6e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bce6e0 bytes f85f04a9
- 00bce6e4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bce6e4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bce6e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bce6e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bce6e4 bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a80b2849c7579847628e9fa2c805ed3"></a>

### [`00bce864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce864.md) → [`00bcec8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcec8c.md) _ZN8firebase4auth4Auth26SignInWithEmailAndPasswordEPKcS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 37.50% / 新版 36.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce898"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00bce9a8",
      "incomplete_value": true,
      "site": "00bce9a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:620:8"
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcecc0"
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
      "unmatched:00bce898",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bced3c",
      "READ",
      [
        "storage",
        "011263b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcedcc",
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bcecc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bced3c",
      "READ",
      [
        "storage",
        "011267b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcedcc",
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bce898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce864.md#insn-00bce898) · [`00bce92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce864.md#insn-00bce92c) · [`00bce9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce864.md#insn-00bce9c8)
- 新版 `00bced54`（命令位置の公開資料なし） · `00bcedf0`（命令位置の公開資料なし）

~~~diff
- 00bce898 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00bce898 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bce898 bytes e81f00f9
- 00bce92c ["INT_ADD", "register:40f0:8", ["const:bce92c:8", "const:4:8"]]
- 00bce92c ["CALL", null, ["callee:00497834:8"]]
+ 00bced54 ["INT_ADD", "register:40f0:8", ["const:bced54:8", "const:4:8"]]
+ 00bced54 ["CALL", null, ["callee:00497834:8"]]
- 00bce92c bytes b223e397
+ 00bced54 bytes b822e397
- 00bce9c8 ["INT_ADD", "register:40f0:8", ["const:bce9c8:8", "const:4:8"]]
- 00bce9c8 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bcedf0 ["INT_ADD", "register:40f0:8", ["const:bcedf0:8", "const:4:8"]]
+ 00bcedf0 ["CALL", null, ["callee:00c5ae00:8"]]
- 00bce9c8 bytes 0e300294
+ 00bcedf0 bytes 04300294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a05831e70b75c7c93c6d4273d973e92"></a>

### [`00bceaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceaf0.md) → [`00bcef18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcef18.md) _ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 99.30% / 新版 99.30%

CFGの説明率　旧版 68.00% / 新版 77.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00bcec34",
      "incomplete_value": true,
      "site": "00bcec34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:620:8"
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
    "old": {
      "definition_site": "00bceba0",
      "incomplete_value": true,
      "site": "00bcebb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
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
      "definition_site": "00bcf014",
      "incomplete_value": true,
      "site": "00bcf01c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
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
      "00bcefc8",
      "READ",
      [
        "storage",
        "011263b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcf058",
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ],
    [
      "00bcf05c",
      "DATA",
      [
        "storage",
        "00bd4404",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcefc8",
      "READ",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcf058",
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      "00bcf05c",
      "DATA",
      [
        "storage",
        "00bd482c",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcebb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceaf0.md#insn-00bcebb8) · [`00bcebf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceaf0.md#insn-00bcebf4) · [`00bcec88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceaf0.md#insn-00bcec88)
- 新版 `00bcefe0`（命令位置の公開資料なし） · `00bcf01c`（命令位置の公開資料なし） · `00bcf0b0`（命令位置の公開資料なし）

~~~diff
- 00bcebb8 ["INT_ADD", "register:40f0:8", ["const:bcebb8:8", "const:4:8"]]
- 00bcebb8 ["CALL", null, ["callee:00497834:8"]]
+ 00bcefe0 ["INT_ADD", "register:40f0:8", ["const:bcefe0:8", "const:4:8"]]
+ 00bcefe0 ["CALL", null, ["callee:00497834:8"]]
- 00bcebb8 bytes 0f23e397
+ 00bcefe0 bytes 1522e397
- 00bcebf4 ["INT_ADD", "register:40f0:8", ["const:bcebf4:8", "const:4:8"]]
- 00bcebf4 ["CALL", null, ["callee:00c5dcd0:8"]]
+ 00bcf01c ["INT_ADD", "register:40f0:8", ["const:bcf01c:8", "const:4:8"]]
+ 00bcf01c ["CALL", null, ["callee:00c5dcd0:8"]]
- 00bcebf4 bytes 373b0294
+ 00bcf01c bytes 2d3b0294
- 00bcec88 ["INT_ADD", "register:40f0:8", ["const:bcec88:8", "const:4:8"]]
- 00bcec88 ["CALL", null, ["callee:00c5dbc0:8"]]
+ 00bcf0b0 ["INT_ADD", "register:40f0:8", ["const:bcf0b0:8", "const:4:8"]]
+ 00bcf0b0 ["CALL", null, ["callee:00c5dbc0:8"]]
- 00bcec88 bytes ce3a0294
+ 00bcf0b0 bytes c43a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-611e80d7873d8a31284460540e9f9319"></a>

### [`00bced7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bced7c.md) → [`00bcf1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf1a4.md) _ZN8firebase4auth4Auth12current_userEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a630.md) · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a640.md)
- 新版 呼出元 1件 [`00c5aa30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa30.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 75.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 11件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00bcedd8",
      "incomplete_value": true,
      "site": "00bcedf8",
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
    "old": {
      "definition_site": "00bcee18",
      "incomplete_value": true,
      "site": "00bcee38",
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
      "site": "00bced94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bced94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcf1ec"
      ]
    ],
    [
      "00bcf1f0",
      "READ",
      [
        "storage",
        "00c9b5c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcf220",
      "DATA",
      [
        "storage",
        "00c924a8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00bcf1bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcf1ec"
      ]
    ],
    [
      "00bcf1f0",
      "READ",
      [
        "storage",
        "00c9b9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcf220",
      "DATA",
      [
        "storage",
        "00c928a8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bced94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bced7c.md#insn-00bced94) · [`00bceda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bced7c.md#insn-00bceda4)
- 新版 `00bcf1bc`（命令位置の公開資料なし） · `00bcf1cc`（命令位置の公開資料なし）

~~~diff
- 00bced94 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bced94 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bced94 bytes 890100b4
+ 00bcf1bc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bcf1bc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bcf1bc bytes 890100b4
- 00bceda4 ["INT_ADD", "register:40f0:8", ["const:bceda4:8", "const:4:8"]]
- 00bceda4 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcf1cc ["INT_ADD", "register:40f0:8", ["const:bcf1cc:8", "const:4:8"]]
+ 00bcf1cc ["CALL", null, ["callee:00c5aa00:8"]]
- 00bceda4 bytes 172e0294
+ 00bcf1cc bytes 0d2e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ac0b05a9b25ea0d1101fdc1c1dd0d27"></a>

### [`00bceefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceefc.md) → [`00bcf324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf324.md) _ZN8firebase4auth4Auth17set_language_codeEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 66.67% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf374",
      "incomplete_value": true,
      "site": "00bcf384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:750:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcef4c",
      "incomplete_value": true,
      "site": "00bcef5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:350:8"
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
      "00bcf374",
      "READ",
      [
        "storage",
        "01126350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcf374",
      "READ",
      [
        "storage",
        "01126750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcef5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceefc.md#insn-00bcef5c) · [`00bcef10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceefc.md#insn-00bcef10) · [`00bcef20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceefc.md#insn-00bcef20)
- 新版 `00bcf384`（命令位置の公開資料なし） · `00bcf338`（命令位置の公開資料なし） · `00bcf348`（命令位置の公開資料なし）

~~~diff
- 00bcef5c ["INT_ADD", "register:40f0:8", ["const:bcef5c:8", "const:4:8"]]
- 00bcef5c ["CALL", null, ["callee:00574cec:8"]]
+ 00bcf384 ["INT_ADD", "register:40f0:8", ["const:bcf384:8", "const:4:8"]]
+ 00bcf384 ["CALL", null, ["callee:00574cec:8"]]
- 00bcef5c bytes 5497e697
+ 00bcf384 bytes 5a96e697
- 00bcef10 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcef10 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bcf338 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcf338 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bcef10 bytes e80300b4
+ 00bcf338 bytes e80300b4
- 00bcef20 ["INT_ADD", "register:40f0:8", ["const:bcef20:8", "const:4:8"]]
- 00bcef20 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bcf348 ["INT_ADD", "register:40f0:8", ["const:bcf348:8", "const:4:8"]]
+ 00bcf348 ["CALL", null, ["callee:00c5b080:8"]]
- 00bcef20 bytes 582f0294
+ 00bcf348 bytes 4e2f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a5a4b45c96dec9ed8b0b919ab91d43e"></a>

### [`00bcef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bcef9c.md) → [`00bcf3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf3c4.md) _ZN8firebase4auth4Auth14UseAppLanguageEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf3ec",
      "incomplete_value": true,
      "site": "00bcf3f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00bcefc4",
      "incomplete_value": true,
      "site": "00bcefd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:358:8"
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
      "00bcf3ec",
      "READ",
      [
        "storage",
        "01126358",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcf3ec",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcefd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bcef9c.md#insn-00bcefd0) · [`00bcefac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bcef9c.md#insn-00bcefac) · [`00bcefb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bcef9c.md#insn-00bcefb8)
- 新版 `00bcf3f8`（命令位置の公開資料なし） · `00bcf3d4`（命令位置の公開資料なし） · `00bcf3e0`（命令位置の公開資料なし）

~~~diff
- 00bcefd0 ["INT_ADD", "register:40f0:8", ["const:bcefd0:8", "const:4:8"]]
- 00bcefd0 ["CALL", null, ["callee:00574cec:8"]]
+ 00bcf3f8 ["INT_ADD", "register:40f0:8", ["const:bcf3f8:8", "const:4:8"]]
+ 00bcf3f8 ["CALL", null, ["callee:00574cec:8"]]
- 00bcefd0 bytes 3797e697
+ 00bcf3f8 bytes 3d96e697
- 00bcefac ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcefac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bcf3d4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcf3d4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcefac bytes c80100b4
+ 00bcf3d4 bytes c80100b4
- 00bcefb8 ["INT_ADD", "register:40f0:8", ["const:bcefb8:8", "const:4:8"]]
- 00bcefb8 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bcf3e0 ["INT_ADD", "register:40f0:8", ["const:bcf3e0:8", "const:4:8"]]
+ 00bcf3e0 ["CALL", null, ["callee:00c5b080:8"]]
- 00bcefb8 bytes 322f0294
+ 00bcf3e0 bytes 282f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-292dd17e7999051b74d54ef18be09347"></a>

### [`00bceff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceff0.md) → [`00bcf418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf418.md) _ZN8firebase4auth4Auth7SignOutEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a620.md) · 呼出先 6件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 1件 [`00c5aa20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa20.md) · 呼出先 6件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.77% / 新版 96.77%

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
      "definition_site": "00bcf020",
      "incomplete_value": true,
      "site": "00bcf024",
      "value": [
        "LOAD",
        "8",
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
                "const:1f8:8"
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
      "definition_site": "00bcf018",
      "incomplete_value": true,
      "site": "00bcf024",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:380:8"
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
      "00bcf440",
      "READ",
      [
        "storage",
        "01126380",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcf440",
      "READ",
      [
        "storage",
        "01126780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceff0.md#insn-00bcf024) · [`00bcf00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceff0.md#insn-00bcf00c) · [`00bcf018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceff0.md#insn-00bcf018)
- 新版 `00bcf44c`（命令位置の公開資料なし） · `00bcf434`（命令位置の公開資料なし） · `00bcf440`（命令位置の公開資料なし）

~~~diff
- 00bcf024 ["INT_ADD", "register:40f0:8", ["const:bcf024:8", "const:4:8"]]
- 00bcf024 ["CALL", null, ["callee:00574cec:8"]]
+ 00bcf44c ["INT_ADD", "register:40f0:8", ["const:bcf44c:8", "const:4:8"]]
+ 00bcf44c ["CALL", null, ["callee:00574cec:8"]]
- 00bcf024 bytes 2297e697
+ 00bcf44c bytes 2896e697
- 00bcf00c ["INT_ADD", "register:40f0:8", ["const:bcf00c:8", "const:4:8"]]
- 00bcf00c ["CALL", null, ["callee:00c5b080:8"]]
+ 00bcf434 ["INT_ADD", "register:40f0:8", ["const:bcf434:8", "const:4:8"]]
+ 00bcf434 ["CALL", null, ["callee:00c5b080:8"]]
- 00bcf00c bytes 1d2f0294
+ 00bcf434 bytes 132f0294
- 00bcf018 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:380:8"]]
- 00bcf018 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcf440 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:780:8"]]
+ 00bcf440 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcf018 bytes 22c141f9
+ 00bcf440 bytes 22c143f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

