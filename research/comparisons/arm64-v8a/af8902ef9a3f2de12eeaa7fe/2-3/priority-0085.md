# v16.0.0 → v16.0.1 · 最優先の変更候補 (85)

[一覧の目次](README.md)

<a id="compare-63244d0201a71872669890319b2c32a8"></a>

### [`00bd9fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9fe8.md) → [`00bda410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda410.md) _ZN8firebase4auth22GameCenterAuthProvider13GetCredentialEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00bdc000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc000.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00bdc428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc428.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bda030",
      "incomplete_value": true,
      "site": "00bda044",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:630:8"
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
      "definition_site": "00bda054",
      "incomplete_value": true,
      "site": "00bda058",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bda070",
      "incomplete_value": true,
      "site": "00bda080",
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
      "00bda458",
      "READ",
      [
        "storage",
        "00c9b630",
        null,
        "pointer"
      ]
    ],
    [
      "00bda458",
      "PARAM",
      [
        "storage",
        "00bdc000",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      "unmatched:00bda06c",
      "PARAM",
      [
        "storage",
        "002b9cb0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda458",
      "READ",
      [
        "storage",
        "00c9ba30",
        null,
        "pointer"
      ]
    ],
    [
      "00bda458",
      "PARAM",
      [
        "storage",
        "00bdc428",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      "00bda494",
      "PARAM",
      [
        "storage",
        "002b9cf0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9fe8.md#insn-00bda044) · [`00bda058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9fe8.md#insn-00bda058) · [`00bda080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9fe8.md#insn-00bda080)
- 新版 `00bda46c`（命令位置の公開資料なし） · `00bda480`（命令位置の公開資料なし） · `00bda4a8`（命令位置の公開資料なし）

~~~diff
- 00bda044 ["INT_ADD", "register:40f0:8", ["const:bda044:8", "const:4:8"]]
- 00bda044 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00bda46c ["INT_ADD", "register:40f0:8", ["const:bda46c:8", "const:4:8"]]
+ 00bda46c ["CALL", null, ["callee:00c5ae40:8"]]
- 00bda044 bytes 7f020294
+ 00bda46c bytes 75020294
- 00bda058 ["INT_ADD", "register:40f0:8", ["const:bda058:8", "const:4:8"]]
- 00bda058 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00bda480 ["INT_ADD", "register:40f0:8", ["const:bda480:8", "const:4:8"]]
+ 00bda480 ["CALL", null, ["callee:00c5aa90:8"]]
- 00bda058 bytes 8e010294
+ 00bda480 bytes 84010294
- 00bda080 ["INT_ADD", "register:40f0:8", ["const:bda080:8", "const:4:8"]]
- 00bda080 ["CALL", null, ["callee:00c5ddd0:8"]]
+ 00bda4a8 ["INT_ADD", "register:40f0:8", ["const:bda4a8:8", "const:4:8"]]
+ 00bda4a8 ["CALL", null, ["callee:00c5ddd0:8"]]
- 00bda080 bytes 540e0294
+ 00bda4a8 bytes 4a0e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdf3eb8a81cffd997018d27b54a50b58"></a>

### [`00bda230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda230.md) → [`00bda658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda658.md) _ZN8firebase4auth22GameCenterAuthProvider21IsPlayerAuthenticatedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
    "old": {
      "definition_site": "00bda23c",
      "incomplete_value": false,
      "site": "00bda240",
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
            "const:8e7:8"
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
      "00bda664",
      "PARAM",
      [
        "storage",
        "002b48e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda664",
      "PARAM",
      [
        "storage",
        "002b4927",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda230.md#insn-00bda240) · [`00bda23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda230.md#insn-00bda23c)
- 新版 `00bda668`（命令位置の公開資料なし） · `00bda664`（命令位置の公開資料なし）

~~~diff
- 00bda240 ["INT_ADD", "register:40f0:8", ["const:bda240:8", "const:4:8"]]
- 00bda240 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bda668 ["INT_ADD", "register:40f0:8", ["const:bda668:8", "const:4:8"]]
+ 00bda668 ["CALL", null, ["callee:00c5b000:8"]]
- 00bda240 bytes 70020294
+ 00bda668 bytes 66020294
- 00bda23c ["COPY", "tmp:0:8", ["const:8e7:8"]]
- 00bda23c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bda23c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bda23c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bda664 ["COPY", "tmp:0:8", ["const:927:8"]]
+ 00bda664 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda664 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda664 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bda23c bytes 009c2391
+ 00bda664 bytes 009c2491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9da7ba317ae066cb8255cc4376bb6e3"></a>

### [`00bda27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda27c.md) → [`00bda6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda6a4.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda27c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda27c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda280"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bda27c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bda280",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bda2a8",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda6a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bda6a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bda6d0",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda27c.md#insn-00bda27c) · [`00bda280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda27c.md#insn-00bda280) · [`00bda2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda27c.md#insn-00bda2ac)
- 新版 `00bda6d4`（命令位置の公開資料なし）

~~~diff
- 00bda27c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bda27c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bda27c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bda27c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bda27c bytes f44fbea9
- 00bda280 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bda280 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bda280 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bda280 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bda280 bytes fd7b01a9
- 00bda2ac ["INT_ADD", "register:40f0:8", ["const:bda2ac:8", "const:4:8"]]
- 00bda2ac ["CALL", null, ["callee:00c5b000:8"]]
+ 00bda6d4 ["INT_ADD", "register:40f0:8", ["const:bda6d4:8", "const:4:8"]]
+ 00bda6d4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bda2ac bytes 55020294
+ 00bda6d4 bytes 4b020294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe5b06da4382fd2aa846f86ecefdc3f5"></a>

### [`00bda320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda320.md) → [`00bda748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda748.md) _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5da40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da40.md) · 呼出先 3件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5de40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de40.md) · 呼出先 3件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

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
    "old": {
      "definition_site": "00bda350",
      "incomplete_value": false,
      "site": "00bda354",
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
            "const:598:8"
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
    "old": {
      "definition_site": "00bda384",
      "incomplete_value": false,
      "site": "00bda388",
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
            "const:598:8"
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
      "00bda778",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "00bda7ac",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda778",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ],
    [
      "00bda7ac",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda320.md#insn-00bda354) · [`00bda388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda320.md#insn-00bda388) · [`00bda340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda320.md#insn-00bda340)
- 新版 `00bda77c`（命令位置の公開資料なし） · `00bda7b0`（命令位置の公開資料なし） · `00bda768`（命令位置の公開資料なし）

~~~diff
- 00bda354 ["INT_ADD", "register:40f0:8", ["const:bda354:8", "const:4:8"]]
- 00bda354 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bda77c ["INT_ADD", "register:40f0:8", ["const:bda77c:8", "const:4:8"]]
+ 00bda77c ["CALL", null, ["callee:00c5b000:8"]]
- 00bda354 bytes 2b020294
+ 00bda77c bytes 21020294
- 00bda388 ["INT_ADD", "register:40f0:8", ["const:bda388:8", "const:4:8"]]
- 00bda388 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bda7b0 ["INT_ADD", "register:40f0:8", ["const:bda7b0:8", "const:4:8"]]
+ 00bda7b0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bda388 bytes 1e020294
+ 00bda7b0 bytes 14020294
- 00bda340 ["INT_ADD", "register:40f0:8", ["const:bda340:8", "const:4:8"]]
- 00bda340 ["CALL", null, ["callee:00c5b260:8"]]
+ 00bda768 ["INT_ADD", "register:40f0:8", ["const:bda768:8", "const:4:8"]]
+ 00bda768 ["CALL", null, ["callee:00c5b260:8"]]
- 00bda340 bytes c8020294
+ 00bda768 bytes be020294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91fe3edf5f33a6f8c7212c331cacc19a"></a>

### [`00bda3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda3f4.md) → [`00bda81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda81c.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokeneqERKS2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

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
    "old": {
      "definition_site": "00bda41c",
      "incomplete_value": false,
      "site": "00bda420",
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
            "const:598:8"
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
      "00bda844",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda844",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda3f4.md#insn-00bda420) · [`00bda40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda3f4.md#insn-00bda40c) · [`00bda41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda3f4.md#insn-00bda41c)
- 新版 `00bda848`（命令位置の公開資料なし） · `00bda834`（命令位置の公開資料なし） · `00bda844`（命令位置の公開資料なし）

~~~diff
- 00bda420 ["INT_ADD", "register:40f0:8", ["const:bda420:8", "const:4:8"]]
- 00bda420 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bda848 ["INT_ADD", "register:40f0:8", ["const:bda848:8", "const:4:8"]]
+ 00bda848 ["CALL", null, ["callee:00c5b000:8"]]
- 00bda420 bytes f8010294
+ 00bda848 bytes ee010294
- 00bda40c ["INT_ADD", "register:40f0:8", ["const:bda40c:8", "const:4:8"]]
- 00bda40c ["CALL", null, ["callee:00c5b260:8"]]
+ 00bda834 ["INT_ADD", "register:40f0:8", ["const:bda834:8", "const:4:8"]]
+ 00bda834 ["CALL", null, ["callee:00c5b260:8"]]
- 00bda40c bytes 95020294
+ 00bda834 bytes 8b020294
- 00bda41c ["COPY", "tmp:0:8", ["const:598:8"]]
- 00bda41c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bda41c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bda41c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bda844 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00bda844 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda844 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda844 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bda41c bytes 00601691
+ 00bda844 bytes 00601791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02d20df425da114af06f74b6c9eee403"></a>

### [`00bda460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda460.md) → [`00bda888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda888.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokenneERKS2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

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
    "old": {
      "definition_site": "00bda488",
      "incomplete_value": false,
      "site": "00bda48c",
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
            "const:598:8"
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
      "00bda8b0",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda8b0",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda460.md#insn-00bda48c) · [`00bda478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda460.md#insn-00bda478) · [`00bda488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda460.md#insn-00bda488)
- 新版 `00bda8b4`（命令位置の公開資料なし） · `00bda8a0`（命令位置の公開資料なし） · `00bda8b0`（命令位置の公開資料なし）

~~~diff
- 00bda48c ["INT_ADD", "register:40f0:8", ["const:bda48c:8", "const:4:8"]]
- 00bda48c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bda8b4 ["INT_ADD", "register:40f0:8", ["const:bda8b4:8", "const:4:8"]]
+ 00bda8b4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bda48c bytes dd010294
+ 00bda8b4 bytes d3010294
- 00bda478 ["INT_ADD", "register:40f0:8", ["const:bda478:8", "const:4:8"]]
- 00bda478 ["CALL", null, ["callee:00c5b260:8"]]
+ 00bda8a0 ["INT_ADD", "register:40f0:8", ["const:bda8a0:8", "const:4:8"]]
+ 00bda8a0 ["CALL", null, ["callee:00c5b260:8"]]
- 00bda478 bytes 7a020294
+ 00bda8a0 bytes 70020294
- 00bda488 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00bda488 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bda488 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bda488 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bda8b0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00bda8b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda8b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda8b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bda488 bytes 00601691
+ 00bda8b0 bytes 00601791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e72bdb790d5df05a5cee57af4c5f114"></a>

### [`00bda4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda4d4.md) → [`00bda8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda8fc.md) _ZN8firebase4auth17PhoneAuthProviderD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5c0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5d9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9c0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

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
    "old": {
      "definition_site": "00bda4fc",
      "incomplete_value": false,
      "site": "00bda500",
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
            "const:598:8"
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
      "00bda924",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda924",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda4d4.md#insn-00bda500) · [`00bda4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda4d4.md#insn-00bda4ec) · [`00bda4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda4d4.md#insn-00bda4fc)
- 新版 `00bda928`（命令位置の公開資料なし） · `00bda914`（命令位置の公開資料なし） · `00bda924`（命令位置の公開資料なし）

~~~diff
- 00bda500 ["INT_ADD", "register:40f0:8", ["const:bda500:8", "const:4:8"]]
- 00bda500 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bda928 ["INT_ADD", "register:40f0:8", ["const:bda928:8", "const:4:8"]]
+ 00bda928 ["CALL", null, ["callee:00c5b000:8"]]
- 00bda500 bytes c0010294
+ 00bda928 bytes b6010294
- 00bda4ec ["INT_ADD", "register:40f0:8", ["const:bda4ec:8", "const:4:8"]]
- 00bda4ec ["CALL", null, ["callee:00c5b260:8"]]
+ 00bda914 ["INT_ADD", "register:40f0:8", ["const:bda914:8", "const:4:8"]]
+ 00bda914 ["CALL", null, ["callee:00c5b260:8"]]
- 00bda4ec bytes 5d020294
+ 00bda914 bytes 53020294
- 00bda4fc ["COPY", "tmp:0:8", ["const:598:8"]]
- 00bda4fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bda4fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bda4fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bda924 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00bda924 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda924 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bda924 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bda4fc bytes 00601691
+ 00bda924 bytes 00601791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-312ae1525237e2b8a775cd2244c2eb2c"></a>

### [`00bda544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda544.md) → [`00bda96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda96c.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerC2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

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
    "old": {
      "definition_site": "00bda55c",
      "incomplete_value": true,
      "site": "00bda560",
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
    "old": {
      "definition_site": "00bda584",
      "incomplete_value": false,
      "site": "00bda588",
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
            "const:598:8"
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
    "old": {
      "definition_site": "00bda59c",
      "incomplete_value": true,
      "site": "00bda5ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bda97c",
      "READ",
      [
        "storage",
        "00c9b640",
        null,
        "pointer"
      ]
    ],
    [
      "00bda988",
      "DATA",
      [
        "storage",
        "00c92140",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bda9ac",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bda97c",
      "READ",
      [
        "storage",
        "00c9ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00bda988",
      "DATA",
      [
        "storage",
        "00c92540",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bda9ac",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda544.md#insn-00bda588) · [`00bda5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda544.md#insn-00bda5ac) · [`00bda554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda544.md#insn-00bda554)
- 新版 `00bda9b0`（命令位置の公開資料なし） · `00bda9d4`（命令位置の公開資料なし） · `00bda97c`（命令位置の公開資料なし）

~~~diff
- 00bda588 ["INT_ADD", "register:40f0:8", ["const:bda588:8", "const:4:8"]]
- 00bda588 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bda9b0 ["INT_ADD", "register:40f0:8", ["const:bda9b0:8", "const:4:8"]]
+ 00bda9b0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bda588 bytes 9e010294
+ 00bda9b0 bytes 94010294
- 00bda5ac ["INT_ADD", "register:40f0:8", ["const:bda5ac:8", "const:4:8"]]
- 00bda5ac ["CALL", null, ["callee:005896f4:8"]]
+ 00bda9d4 ["INT_ADD", "register:40f0:8", ["const:bda9d4:8", "const:4:8"]]
+ 00bda9d4 ["CALL", null, ["callee:005896f4:8"]]
- 00bda5ac bytes 42bce697
+ 00bda9d4 bytes 48bbe697
- 00bda554 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:640:8"]]
- 00bda554 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bda97c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a40:8"]]
+ 00bda97c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bda554 bytes 082143f9
+ 00bda97c bytes 082145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c4087f6e26e356481d2ec0d469fce0f"></a>

### [`00bda5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda5d8.md) → [`00bdaa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa00.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

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
    "old": {
      "definition_site": "00bda5f0",
      "incomplete_value": true,
      "site": "00bda5f4",
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
    "old": {
      "definition_site": "00bda608",
      "incomplete_value": false,
      "site": "00bda60c",
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
            "const:598:8"
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
    "old": {
      "definition_site": "00bda620",
      "incomplete_value": true,
      "site": "00bda62c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c8:8"
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
      "00bdaa10",
      "READ",
      [
        "storage",
        "00c9b640",
        null,
        "pointer"
      ]
    ],
    [
      "00bdaa1c",
      "DATA",
      [
        "storage",
        "00c92140",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bdaa30",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdaa10",
      "READ",
      [
        "storage",
        "00c9ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00bdaa1c",
      "DATA",
      [
        "storage",
        "00c92540",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00bdaa30",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda5d8.md#insn-00bda60c) · [`00bda62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda5d8.md#insn-00bda62c) · [`00bda5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda5d8.md#insn-00bda5e8)
- 新版 `00bdaa34`（命令位置の公開資料なし） · `00bdaa54`（命令位置の公開資料なし） · `00bdaa10`（命令位置の公開資料なし）

~~~diff
- 00bda60c ["INT_ADD", "register:40f0:8", ["const:bda60c:8", "const:4:8"]]
- 00bda60c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdaa34 ["INT_ADD", "register:40f0:8", ["const:bdaa34:8", "const:4:8"]]
+ 00bdaa34 ["CALL", null, ["callee:00c5b000:8"]]
- 00bda60c bytes 7d010294
+ 00bdaa34 bytes 73010294
- 00bda62c ["INT_ADD", "register:40f0:8", ["const:bda62c:8", "const:4:8"]]
- 00bda62c ["CALL", null, ["callee:00574cec:8"]]
+ 00bdaa54 ["INT_ADD", "register:40f0:8", ["const:bdaa54:8", "const:4:8"]]
+ 00bdaa54 ["CALL", null, ["callee:00574cec:8"]]
- 00bda62c bytes a069e697
+ 00bdaa54 bytes a668e697
- 00bda5e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:640:8"]]
- 00bda5e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdaa10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a40:8"]]
+ 00bdaa10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bda5e8 bytes 082143f9
+ 00bdaa10 bytes 082145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fba7bcb14f104fcdb25e9abc213e31dd"></a>

### [`00bda670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda670.md) → [`00bdaa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa98.md) _ZN8firebase4auth17PhoneAuthProvider17VerifyPhoneNumberERKNS0_16PhoneAuthOptionsEPNS1_8ListenerE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
    "old": {
      "definition_site": "00bda6dc",
      "incomplete_value": true,
      "site": "00bda6f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:778:8"
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
    "old": {
      "definition_site": "00bda6e8",
      "incomplete_value": true,
      "site": "00bda6f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bda70c",
      "incomplete_value": false,
      "site": "00bda714",
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
            "const:8dd:8"
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
      "00bdab04",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdab10",
      "READ",
      [
        "storage",
        "01126788",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdab34",
      "PARAM",
      [
        "storage",
        "002be8dd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdab04",
      "READ",
      [
        "storage",
        "01126b78",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdab10",
      "READ",
      [
        "storage",
        "01126b88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdab34",
      "PARAM",
      [
        "storage",
        "002be91d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda670.md#insn-00bda6e8) · [`00bda6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda670.md#insn-00bda6f4) · [`00bda714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda670.md#insn-00bda714)
- 新版 `00bdab10`（命令位置の公開資料なし） · `00bdab1c`（命令位置の公開資料なし） · `00bdab3c`（命令位置の公開資料なし）

~~~diff
- 00bda6e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:788:8"]]
- 00bda6e8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdab10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b88:8"]]
+ 00bdab10 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00bda6e8 bytes 22c543f9
+ 00bdab10 bytes 22c545f9
- 00bda6f4 ["INT_ADD", "register:40f0:8", ["const:bda6f4:8", "const:4:8"]]
- 00bda6f4 ["CALL", null, ["callee:005896f4:8"]]
+ 00bdab1c ["INT_ADD", "register:40f0:8", ["const:bdab1c:8", "const:4:8"]]
+ 00bdab1c ["CALL", null, ["callee:005896f4:8"]]
- 00bda6f4 bytes f0bbe697
+ 00bdab1c bytes f6bae697
- 00bda714 ["INT_ADD", "register:40f0:8", ["const:bda714:8", "const:4:8"]]
- 00bda714 ["CALL", null, ["callee:00c5b5c0:8"]]
+ 00bdab3c ["INT_ADD", "register:40f0:8", ["const:bdab3c:8", "const:4:8"]]
+ 00bdab3c ["CALL", null, ["callee:00c5b5c0:8"]]
- 00bda714 bytes ab020294
+ 00bdab3c bytes a1020294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caab69e68c2adabf0245ede7255c22ae"></a>

### [`00bdab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdab90.md) → [`00bdafb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdafb8.md) _ZN8firebase4auth17PhoneAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

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
    "old": {
      "definition_site": "00bdac08",
      "incomplete_value": true,
      "site": "00bdac20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bdac0c",
      "incomplete_value": true,
      "site": "00bdac20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e8:8"
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
    "old": {
      "definition_site": "00bdac78",
      "incomplete_value": false,
      "site": "00bdac7c",
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
            "const:598:8"
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
      "00bdafe0",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdafe4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bdacdc"
      ]
    ],
    [
      "00bdb030",
      "READ",
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
      "00bdafe0",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdafe4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdb104"
      ]
    ],
    [
      "00bdb030",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdac20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdab90.md#insn-00bdac20) · [`00bdac7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdab90.md#insn-00bdac7c) · [`00bdace4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdab90.md#insn-00bdace4)
- 新版 `00bdb048`（命令位置の公開資料なし） · `00bdb0a4`（命令位置の公開資料なし） · `00bdb10c`（命令位置の公開資料なし）

~~~diff
- 00bdac20 ["INT_ADD", "register:40f0:8", ["const:bdac20:8", "const:4:8"]]
- 00bdac20 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00bdb048 ["INT_ADD", "register:40f0:8", ["const:bdb048:8", "const:4:8"]]
+ 00bdb048 ["CALL", null, ["callee:00c5aba0:8"]]
- 00bdac20 bytes e0fe0194
+ 00bdb048 bytes d6fe0194
- 00bdac7c ["INT_ADD", "register:40f0:8", ["const:bdac7c:8", "const:4:8"]]
- 00bdac7c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdb0a4 ["INT_ADD", "register:40f0:8", ["const:bdb0a4:8", "const:4:8"]]
+ 00bdb0a4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bdac7c bytes e1ff0194
+ 00bdb0a4 bytes d7ff0194
- 00bdace4 ["INT_ADD", "register:40f0:8", ["const:bdace4:8", "const:4:8"]]
- 00bdace4 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bdb10c ["INT_ADD", "register:40f0:8", ["const:bdb10c:8", "const:4:8"]]
+ 00bdb10c ["CALL", null, ["callee:00c5aca0:8"]]
- 00bdace4 bytes effe0194
+ 00bdb10c bytes e5fe0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e758c4212576f5f5edd02076714f551e"></a>

### [`00bdadac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdadac.md) → [`00bdb1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb1d4.md) _ZN8firebase4auth20JniAuthPhoneListener29nativeOnVerificationCompletedEP7_JNIEnvP8_jobjectlS5_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b260.md)

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
    "old": {
      "definition_site": "00bdadec",
      "incomplete_value": false,
      "site": "00bdadf0",
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
            "const:598:8"
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
      "00bdb214",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdb214",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdadf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdadac.md#insn-00bdadf0) · [`00bdaddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdadac.md#insn-00bdaddc) · [`00bdadec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdadac.md#insn-00bdadec)
- 新版 `00bdb218`（命令位置の公開資料なし） · `00bdb204`（命令位置の公開資料なし） · `00bdb214`（命令位置の公開資料なし）

~~~diff
- 00bdadf0 ["INT_ADD", "register:40f0:8", ["const:bdadf0:8", "const:4:8"]]
- 00bdadf0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdb218 ["INT_ADD", "register:40f0:8", ["const:bdb218:8", "const:4:8"]]
+ 00bdb218 ["CALL", null, ["callee:00c5b000:8"]]
- 00bdadf0 bytes 84ff0194
+ 00bdb218 bytes 7aff0194
- 00bdaddc ["INT_ADD", "register:40f0:8", ["const:bdaddc:8", "const:4:8"]]
- 00bdaddc ["CALL", null, ["callee:00c5b260:8"]]
+ 00bdb204 ["INT_ADD", "register:40f0:8", ["const:bdb204:8", "const:4:8"]]
+ 00bdb204 ["CALL", null, ["callee:00c5b260:8"]]
- 00bdaddc bytes 21000294
+ 00bdb204 bytes 17000294
- 00bdadec ["COPY", "tmp:0:8", ["const:598:8"]]
- 00bdadec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdadec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdadec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdb214 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00bdb214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdb214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdb214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdadec bytes 00601691
+ 00bdb214 bytes 00601791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eea2febce5d1980cb30493c71429a7db"></a>

### [`00bdaf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaf48.md) → [`00bdb370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb370.md) _ZN8firebase4auth20JniAuthPhoneListener16nativeOnCodeSentEP7_JNIEnvP8_jobjectlP8_jstringS5_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

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
    "old": {
      "definition_site": "00bdaff0",
      "incomplete_value": false,
      "site": "00bdaff4",
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
            "const:598:8"
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
      "00bdb418",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdb418",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaf48.md#insn-00bdaff4) · [`00bdaf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaf48.md#insn-00bdaf80) · [`00bdaf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdaf48.md#insn-00bdaf94)
- 新版 `00bdb41c`（命令位置の公開資料なし） · `00bdb3a8`（命令位置の公開資料なし） · `00bdb3bc`（命令位置の公開資料なし）

~~~diff
- 00bdaff4 ["INT_ADD", "register:40f0:8", ["const:bdaff4:8", "const:4:8"]]
- 00bdaff4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdb41c ["INT_ADD", "register:40f0:8", ["const:bdb41c:8", "const:4:8"]]
+ 00bdb41c ["CALL", null, ["callee:00c5b000:8"]]
- 00bdaff4 bytes 03ff0194
+ 00bdb41c bytes f9fe0194
- 00bdaf80 ["INT_ADD", "register:40f0:8", ["const:bdaf80:8", "const:4:8"]]
- 00bdaf80 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bdb3a8 ["INT_ADD", "register:40f0:8", ["const:bdb3a8:8", "const:4:8"]]
+ 00bdb3a8 ["CALL", null, ["callee:00c57e90:8"]]
- 00bdaf80 bytes c4f20194
+ 00bdb3a8 bytes baf20194
- 00bdaf94 ["INT_ADD", "register:40f0:8", ["const:bdaf94:8", "const:4:8"]]
- 00bdaf94 ["CALL", null, ["callee:00c5de40:8"]]
+ 00bdb3bc ["INT_ADD", "register:40f0:8", ["const:bdb3bc:8", "const:4:8"]]
+ 00bdb3bc ["CALL", null, ["callee:00c5de40:8"]]
- 00bdaf94 bytes ab0a0294
+ 00bdb3bc bytes a10a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43ea9d582d8a1702bff8a9821e36b697"></a>

### [`00bdb2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb2b0.md) → [`00bdb6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb6d8.md) _ZN8firebase4auth22FederatedOAuthProviderD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 87.50% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb2d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdb6fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bdb2c8",
      "incomplete_value": true,
      "site": "00bdb2d8",
      "value": [
        "LOAD",
        "8",
        [
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
      "00bdb6ec",
      "READ",
      [
        "storage",
        "00c9b648",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb2d4",
      "DATA",
      [
        "storage",
        "00c92180",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00bdb6ec",
      "READ",
      [
        "storage",
        "00c9ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb6fc",
      "DATA",
      [
        "storage",
        "00c92580",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb2b0.md#insn-00bdb2d4) · [`00bdb2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb2b0.md#insn-00bdb2d8)
- 新版 `00bdb700`（命令位置の公開資料なし） · `00bdb6fc`（命令位置の公開資料なし）

~~~diff
- 00bdb2d4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bdb2d4 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00bdb2d4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:38:8"]]
- 00bdb2d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bdb2d4 bytes 088403f8
- 00bdb2d8 ["INT_ADD", "register:40f0:8", ["const:bdb2d8:8", "const:4:8"]]
- 00bdb2d8 ["CALL", null, ["callee:0046d490:8"]]
+ 00bdb700 ["INT_ADD", "register:40f0:8", ["const:bdb700:8", "const:4:8"]]
+ 00bdb700 ["CALL", null, ["callee:0046d490:8"]]
- 00bdb2d8 bytes 5e48e297
+ 00bdb700 bytes 6447e297
+ 00bdb6fc ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00bdb6fc ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00bdb6fc ["INT_ADD", "register:4000:8", ["register:4000:8", "const:38:8"]]
+ 00bdb6fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00bdb6fc bytes 088403f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15849ef54f4708194e542e8015fd0fb9"></a>

### [`00bdb400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb400.md) → [`00bdb828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb828.md) _ZN8firebase4auth22FederatedOAuthProvider15SetProviderDataERKNS0_26FederatedOAuthProviderDataE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b73c.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5cc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053b77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b77c.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d030.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 50.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb430"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb434"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bdb858"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb400.md#insn-00bdb430) · [`00bdb434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb400.md#insn-00bdb434) · [`00bdb444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb400.md#insn-00bdb444)
- 新版 `00bdb86c`（命令位置の公開資料なし）

~~~diff
- 00bdb430 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdb430 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bdb430 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bdb430 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00bdb430 bytes 2115819a
- 00bdb434 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00bdb434 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bdb434 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bdb434 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00bdb434 bytes 62018a9a
- 00bdb444 ["INT_ADD", "register:40f0:8", ["const:bdb444:8", "const:4:8"]]
- 00bdb444 ["CALL", null, ["callee:00c5d030:8"]]
+ 00bdb86c ["INT_ADD", "register:40f0:8", ["const:bdb86c:8", "const:4:8"]]
+ 00bdb86c ["CALL", null, ["callee:00c5d030:8"]]
- 00bdb444 bytes fb050294
+ 00bdb86c bytes f1050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d6ca6412b388b9118f71742a1c228de"></a>

### [`00bdb46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb46c.md) → [`00bdb894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb894.md) _ZN8firebase4auth22FederatedOAuthProvider6SignInEPNS0_8AuthDataE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00bdb810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb810.md) [`00bdc754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc754.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00bdbc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbc38.md) [`00bdcb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcb7c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 95.21% / 新版 95.21%

CFGの説明率　旧版 57.14% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb4a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb500"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdb504"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb4a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdb500",
      "WRITE",
      [
        "storage",
        "Stack[-0x190]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdb504",
      "WRITE",
      [
        "storage",
        "Stack[-0x168]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdb8c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00bdb928",
      "WRITE",
      [
        "storage",
        "Stack[-0x190]",
        null,
        null
      ]
    ],
    [
      "00bdb92c",
      "WRITE",
      [
        "storage",
        "Stack[-0x168]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb46c.md#insn-00bdb4a0) · [`00bdb4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb46c.md#insn-00bdb4ac) · [`00bdb500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb46c.md#insn-00bdb500)
- 新版 `00bdb8d4`（命令位置の公開資料なし）

~~~diff
- 00bdb4a0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bdb4a0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00bdb4a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bdb4a0 bytes a9031af8
- 00bdb4ac ["INT_ADD", "register:40f0:8", ["const:bdb4ac:8", "const:4:8"]]
- 00bdb4ac ["CALL", null, ["callee:00c5b080:8"]]
+ 00bdb8d4 ["INT_ADD", "register:40f0:8", ["const:bdb8d4:8", "const:4:8"]]
+ 00bdb8d4 ["CALL", null, ["callee:00c5b080:8"]]
- 00bdb4ac bytes f5fd0194
+ 00bdb8d4 bytes ebfd0194
- 00bdb500 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00bdb500 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bdb500 bytes e82300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8080cf5283f1710bd8775104cc6fbdc0"></a>

### [`00bdb744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb744.md) → [`00bdbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbb6c.md) _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEiRKS5_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d9e0.md) · 呼出先 7件 [`00bcf8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5dde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dde0.md) · 呼出先 7件 [`00bcfcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfcd8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00bdb7c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bdbbf0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdbbb8",
      "incomplete_value": true,
      "site": "00bdbbcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdb790",
      "incomplete_value": true,
      "site": "00bdb7a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdbbb8",
      "READ",
      [
        "storage",
        "00c9b5e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdbbb8",
      "PARAM",
      [
        "storage",
        "00bcf8b0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ],
    [
      "unmatched:00bdb7c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdbc0c"
      ]
    ]
  ],
  "added": [
    [
      "00bdbbb8",
      "READ",
      [
        "storage",
        "00c9b9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdbbb8",
      "PARAM",
      [
        "storage",
        "00bcfcd8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
        null
      ]
    ],
    [
      "00bdbbf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdbc0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb744.md#insn-00bdb7a4) · [`00bdb7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb744.md#insn-00bdb7c8) · [`00bdb7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb744.md#insn-00bdb7e0)
- 新版 `00bdbbcc`（命令位置の公開資料なし）

~~~diff
- 00bdb7a4 ["INT_ADD", "register:40f0:8", ["const:bdb7a4:8", "const:4:8"]]
- 00bdb7a4 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00bdbbcc ["INT_ADD", "register:40f0:8", ["const:bdbbcc:8", "const:4:8"]]
+ 00bdbbcc ["CALL", null, ["callee:00c5ae40:8"]]
- 00bdb7a4 bytes a7fc0194
+ 00bdbbcc bytes 9dfc0194
- 00bdb7c8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdb7c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bdb7c8 bytes e1000054
- 00bdb7e0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bdb7e0 ["RETURN", null, ["register:0:8"]]
- 00bdb7e0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-300bee88ef1a28741505129eec170432"></a>

### [`00bdb810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb810.md) → [`00bdbc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbc38.md) FUN_00bdbc38

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bdb46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb46c.md) [`00bdba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdba50.md) [`00bdbd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdbd28.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5abb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abb0.md)
- 新版 呼出元 3件 [`00bdb894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb894.md) [`00bdbe78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbe78.md) [`00bdc150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc150.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5afb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 89.58% / 新版 89.58%

CFGの説明率　旧版 30.00% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bdb86c",
      "incomplete_value": true,
      "site": "00bdb884",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00bdb870",
      "incomplete_value": true,
      "site": "00bdb884",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
    "old": {
      "definition_site": "00bdb8e4",
      "incomplete_value": true,
      "site": "00bdb8f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bdbc94",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdbc98",
      "READ",
      [
        "storage",
        "01126740",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdbd0c",
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
      "00bdbc94",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdbc98",
      "READ",
      [
        "storage",
        "01126b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdbd0c",
      "READ",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb810.md#insn-00bdb884) · [`00bdb8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb810.md#insn-00bdb8f4) · [`00bdb90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb810.md#insn-00bdb90c)
- 新版 `00bdbcac`（命令位置の公開資料なし） · `00bdbd1c`（命令位置の公開資料なし）

~~~diff
- 00bdb884 ["INT_ADD", "register:40f0:8", ["const:bdb884:8", "const:4:8"]]
- 00bdb884 ["CALL", null, ["callee:00c5aba0:8"]]
+ 00bdbcac ["INT_ADD", "register:40f0:8", ["const:bdbcac:8", "const:4:8"]]
+ 00bdbcac ["CALL", null, ["callee:00c5aba0:8"]]
- 00bdb884 bytes c7fb0194
+ 00bdbcac bytes bdfb0194
- 00bdb8f4 ["INT_ADD", "register:40f0:8", ["const:bdb8f4:8", "const:4:8"]]
- 00bdb8f4 ["CALL", null, ["callee:00497834:8"]]
+ 00bdbd1c ["INT_ADD", "register:40f0:8", ["const:bdbd1c:8", "const:4:8"]]
+ 00bdbd1c ["CALL", null, ["callee:00497834:8"]]
- 00bdb8f4 bytes c0efe297
+ 00bdbd1c bytes c6eee297
- 00bdb90c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdb90c ["INT_ADD", "register:40f0:8", ["const:bdb90c:8", "const:4:8"]]
- 00bdb90c ["CALLIND", null, ["register:0:8"]]
- 00bdb90c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2eac45b1ca9ca5041432a4a83ac3dbb"></a>

### [`00bdbd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdbd28.md) → [`00bdc150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc150.md) _ZN8firebase4auth22FederatedOAuthProvider14ReauthenticateEPNS0_8AuthDataE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00bdb810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb810.md) [`00bdc754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc754.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00bdbc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbc38.md) [`00bdcb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcb7c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 77.78% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00bdbec0",
      "incomplete_value": true,
      "site": "00bdbec0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdbf48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bdc370"
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
      "00bdc288",
      "READ",
      [
        "storage",
        "011268a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdc2e4",
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc2e8",
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
      "00bdc288",
      "READ",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdc2e4",
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc2e8",
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

- 旧版 [`00bdbe70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdbd28.md#insn-00bdbe70) · [`00bdbef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdbd28.md#insn-00bdbef0) · [`00bdbf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdbd28.md#insn-00bdbf48)
- 新版 `00bdc298`（命令位置の公開資料なし） · `00bdc318`（命令位置の公開資料なし）

~~~diff
- 00bdbe70 ["INT_ADD", "register:40f0:8", ["const:bdbe70:8", "const:4:8"]]
- 00bdbe70 ["CALL", null, ["callee:00497834:8"]]
+ 00bdc298 ["INT_ADD", "register:40f0:8", ["const:bdc298:8", "const:4:8"]]
+ 00bdc298 ["CALL", null, ["callee:00497834:8"]]
- 00bdbe70 bytes 61eee297
+ 00bdc298 bytes 67ede297
- 00bdbef0 ["INT_ADD", "register:40f0:8", ["const:bdbef0:8", "const:4:8"]]
- 00bdbef0 ["CALL", null, ["callee:00c5af40:8"]]
+ 00bdc318 ["INT_ADD", "register:40f0:8", ["const:bdc318:8", "const:4:8"]]
+ 00bdc318 ["CALL", null, ["callee:00c5af40:8"]]
- 00bdbef0 bytes 14fb0194
+ 00bdc318 bytes 0afb0194
- 00bdbf48 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdbf48 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00bdbf48 bytes 21010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2252ea819b54189a624ade1aa085f9dc"></a>

### [`00bdc02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc02c.md) → [`00bdc454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc454.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10CredentialEEEvRKNS_12FutureHandleEiPKcEUlPvE_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d9d0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5ddd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5ddd0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 75.00% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bdc090",
      "incomplete_value": false,
      "site": "00bdc094",
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
      "site": "00bdc130"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bdc558"
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
      "00bdc4b8",
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
      "00bdc4b8",
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

- 旧版 [`00bdc094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc02c.md#insn-00bdc094) · [`00bdc130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc02c.md#insn-00bdc130)
- 新版 `00bdc4bc`（命令位置の公開資料なし） · `00bdc558`（命令位置の公開資料なし）

~~~diff
- 00bdc094 ["INT_ADD", "register:40f0:8", ["const:bdc094:8", "const:4:8"]]
- 00bdc094 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdc4bc ["INT_ADD", "register:40f0:8", ["const:bdc4bc:8", "const:4:8"]]
+ 00bdc4bc ["CALL", null, ["callee:00c5b000:8"]]
- 00bdc094 bytes dbfa0194
+ 00bdc4bc bytes d1fa0194
- 00bdc130 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bdc130 ["RETURN", null, ["register:0:8"]]
- 00bdc130 bytes c0035fd6
+ 00bdc558 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bdc558 ["RETURN", null, ["register:0:8"]]
+ 00bdc558 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39c6e231873aeafecc570b0a76fb0c55"></a>

### [`00bdc134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc134.md) → [`00bdc55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc55c.md) _ZN8firebase6FutureINS_4auth10CredentialEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5da50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da50.md) · 呼出先 3件 [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9f0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5de50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de50.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 20.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdc570",
      "incomplete_value": false,
      "site": "00bdc57c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc17c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bdc5a4"
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
      "unmatched:00bdc17c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdc5a4",
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

- 旧版 [`00bdc154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc134.md#insn-00bdc154) · [`00bdc17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc134.md#insn-00bdc17c)
- 新版 `00bdc57c`（命令位置の公開資料なし） · `00bdc5a4`（命令位置の公開資料なし）

~~~diff
- 00bdc154 ["INT_ADD", "register:40f0:8", ["const:bdc154:8", "const:4:8"]]
- 00bdc154 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bdc57c ["INT_ADD", "register:40f0:8", ["const:bdc57c:8", "const:4:8"]]
+ 00bdc57c ["CALL", null, ["callee:00c5ac70:8"]]
- 00bdc154 bytes c7f90194
+ 00bdc57c bytes bdf90194
- 00bdc17c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdc17c ["INT_ADD", "register:40f0:8", ["const:bdc17c:8", "const:4:8"]]
- 00bdc17c ["CALLIND", null, ["register:0:8"]]
- 00bdc17c bytes 00013fd6
+ 00bdc5a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdc5a4 ["INT_ADD", "register:40f0:8", ["const:bdc5a4:8", "const:4:8"]]
+ 00bdc5a4 ["CALLIND", null, ["register:0:8"]]
+ 00bdc5a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcb19dcd85359e1b5b817709b5af940a"></a>

### [`00bdc1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc1d4.md) → [`00bdc5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc5fc.md) _ZN8firebase4auth10AuthResultC2ERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d9f0.md) · 呼出先 3件 [`00c5a640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a640.md) [`00c5d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d960.md) [`00c5da20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da20.md)
- 新版 呼出元 1件 [`00c5ddf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5ddf0.md) · 呼出先 3件 [`00c5aa40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa40.md) [`00c5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd60.md) [`00c5de20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de20.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bdc214",
      "incomplete_value": true,
      "site": "00bdc21c",
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
            "const:98:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc22c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bdc654"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc1d4.md#insn-00bdc21c) · [`00bdc22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc1d4.md#insn-00bdc22c)
- 新版 `00bdc644`（命令位置の公開資料なし） · `00bdc654`（命令位置の公開資料なし）

~~~diff
- 00bdc21c ["INT_ADD", "register:40f0:8", ["const:bdc21c:8", "const:4:8"]]
- 00bdc21c ["CALL", null, ["callee:00c5aa40:8"]]
+ 00bdc644 ["INT_ADD", "register:40f0:8", ["const:bdc644:8", "const:4:8"]]
+ 00bdc644 ["CALL", null, ["callee:00c5aa40:8"]]
- 00bdc21c bytes 09f90194
+ 00bdc644 bytes fff80194
- 00bdc22c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bdc22c ["RETURN", null, ["register:0:8"]]
- 00bdc22c bytes c0035fd6
+ 00bdc654 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bdc654 ["RETURN", null, ["register:0:8"]]
+ 00bdc654 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcd6de7be73f87f66e25f908b7c3a8c5"></a>

### [`00bdc2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc2a4.md) → [`00bdc6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc6cc.md) _ZN8firebase4auth18AdditionalUserInfoC2ERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5da20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da20.md) · 呼出先 3件 [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d960.md) [`00c5da70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da70.md)
- 新版 呼出元 1件 [`00c5de20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de20.md) · 呼出先 3件 [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md) [`00c5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd60.md) [`00c5de70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.30% / 新版 87.30%

CFGの説明率　旧版 68.75% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc378"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc37c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc380"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc360",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc774"
      ]
    ]
  ],
  "added": [
    [
      "00bdc788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc774"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc2a4.md#insn-00bdc360) · [`00bdc378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc2a4.md#insn-00bdc378) · [`00bdc37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc2a4.md#insn-00bdc37c)

~~~diff
- 00bdc360 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdc360 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00bdc360 bytes 61ffff54
- 00bdc378 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00bdc378 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00bdc378 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00bdc378 bytes 1f0800b9
- 00bdc37c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bdc37c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00bdc37c ["INT_ADD", "register:40b8:8", ["register:40b8:8", "const:10:8"]]
- 00bdc37c ["STORE", null, ["const:1b1:8", "register:40b8:8", "tmp:1:8"]]
- 00bdc37c bytes ff0e01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15fb10839c08679553dab5ada50eed0c"></a>

### [`00bdc414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc414.md) → [`00bdc83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc83c.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emp

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5da70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da70.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) [`00c5da60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da60.md)
- 新版 呼出元 1件 [`00c5de70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de70.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5de60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de60.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.38% / 新版 91.38%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件, `store_condition` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc484"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdc870"
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
      "unmatched:00bdc448",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdc44c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5de60"
      ]
    ],
    [
      "unmatched:00bdc454",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc8f4"
      ]
    ]
  ],
  "added": [
    [
      "00bdc870",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bdc874",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5de60"
      ]
    ],
    [
      "00bdc87c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc8f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc414.md#insn-00bdc448) · [`00bdc44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc414.md#insn-00bdc44c) · [`00bdc454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc414.md#insn-00bdc454)

~~~diff
- 00bdc448 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00bdc448 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bdc448 bytes e80f00f9
- 00bdc44c ["INT_ADD", "register:40f0:8", ["const:bdc44c:8", "const:4:8"]]
- 00bdc44c ["CALL", null, ["callee:00c5de60:8"]]
- 00bdc44c bytes 85050294
- 00bdc454 ["INT_NOTEQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00bdc454 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00bdc454 bytes d30300b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e9a49b7f8fbfa77c8eb6e12aa6c44b3"></a>

### [`00bdc528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc528.md) → [`00bdc950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc950.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__fin

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5da60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da60.md) · 呼出先 1件 [`00c5b1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1a0.md)
- 新版 呼出元 1件 [`00c5de60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de60.md) · 呼出先 1件 [`00c5b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 70.50% / 新版 70.50%

CFGの説明率　旧版 29.33% / 新版 30.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc558"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc580"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc588"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc558",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc99c"
      ]
    ],
    [
      "unmatched:00bdc580",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdca18"
      ]
    ],
    [
      "unmatched:00bdc588",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc9f0"
      ]
    ]
  ],
  "added": [
    [
      "00bdc980",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc99c"
      ]
    ],
    [
      "00bdc9a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdca18"
      ]
    ],
    [
      "00bdc9b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdc9f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc528.md#insn-00bdc558) · [`00bdc580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc528.md#insn-00bdc580) · [`00bdc588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc528.md#insn-00bdc588)

~~~diff
- 00bdc558 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00bdc558 bytes e0000054
- 00bdc580 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00bdc580 bytes 80030054
- 00bdc588 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bdc588 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00bdc588 bytes 080200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60f6eb35501d1decb2b9824c8df3841c"></a>

### [`00bdc754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc754.md) → [`00bdcb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcb7c.md) _ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bdb46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb46c.md) [`00bdba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdba50.md) [`00bdbd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdbd28.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d920.md)
- 新版 呼出元 3件 [`00bdb894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb894.md) [`00bdbe78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbe78.md) [`00bdc150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc150.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5dd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc784"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc788"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdcbac"
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
      "unmatched:00bdc784",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdc788",
      "WRITE",
      [
        "storage",
        "Stack[-0x4c]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdcbac",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bdcbb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x4c]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc754.md#insn-00bdc784) · [`00bdc788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc754.md#insn-00bdc788) · [`00bdc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc754.md#insn-00bdc78c)
- 新版 `00bdcbb4`（命令位置の公開資料なし）

~~~diff
- 00bdc784 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00bdc784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bdc784 bytes e81f00f9
- 00bdc788 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bdc788 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bdc788 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:34:8"]]
- 00bdc788 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bdc788 bytes ffd30039
- 00bdc78c ["INT_ADD", "register:40f0:8", ["const:bdc78c:8", "const:4:8"]]
- 00bdc78c ["CALL", null, ["callee:00c5dd20:8"]]
+ 00bdcbb4 ["INT_ADD", "register:40f0:8", ["const:bdcbb4:8", "const:4:8"]]
+ 00bdcbb4 ["CALL", null, ["callee:00c5dd20:8"]]
- 00bdc78c bytes 65040294
+ 00bdcbb4 bytes 5b040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb3977f758bfabf074ed7bf83babad45"></a>

### [`00bdc830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc830.md) → [`00bdcc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcc58.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d9c0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5ddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5ddc0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc894"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bdccbc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bdc868",
      "incomplete_value": true,
      "site": "00bdc870",
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
            "register:40a0:8"
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
      "unmatched:00bdc894",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdcccc"
      ]
    ],
    [
      "unmatched:00bdc89c",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bdc88c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdccbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdcccc"
      ]
    ],
    [
      "00bdccc4",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "00bdccb4",
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

- 旧版 [`00bdc870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc830.md#insn-00bdc870) · [`00bdc88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc830.md#insn-00bdc88c) · [`00bdc894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc830.md#insn-00bdc894)
- 新版 `00bdcc98`（命令位置の公開資料なし）

~~~diff
- 00bdc870 ["INT_ADD", "register:40f0:8", ["const:bdc870:8", "const:4:8"]]
- 00bdc870 ["CALL", null, ["callee:00c5ae80:8"]]
+ 00bdcc98 ["INT_ADD", "register:40f0:8", ["const:bdcc98:8", "const:4:8"]]
+ 00bdcc98 ["CALL", null, ["callee:00c5ae80:8"]]
- 00bdc870 bytes 84f80194
+ 00bdcc98 bytes 7af80194
- 00bdc88c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdc88c ["INT_ADD", "register:40f0:8", ["const:bdc88c:8", "const:4:8"]]
- 00bdc88c ["CALLIND", null, ["register:0:8"]]
- 00bdc88c bytes 00013fd6
- 00bdc894 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00bdc894 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a359226388eeb9f95ad5bf1e526f76a"></a>

### [`00bdc9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc9f0.md) → [`00bdce18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce18.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00bdca1c",
      "incomplete_value": true,
      "site": "00bdca1c",
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
            "const:900:8"
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
    "old": {
      "definition_site": "00bdca04",
      "incomplete_value": true,
      "site": "00bdca04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdca10",
      "incomplete_value": false,
      "site": "00bdca14",
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
            "const:210:8"
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
      "00bdce28",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdce38",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ],
    [
      "00bdce44",
      "WRITE",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdce28",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdce38",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdce44",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdca14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc9f0.md#insn-00bdca14) · [`00bdca1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc9f0.md#insn-00bdca1c) · [`00bdca00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc9f0.md#insn-00bdca00)
- 新版 `00bdce3c`（命令位置の公開資料なし） · `00bdce44`（命令位置の公開資料なし） · `00bdce28`（命令位置の公開資料なし）

~~~diff
- 00bdca14 ["INT_ADD", "register:40f0:8", ["const:bdca14:8", "const:4:8"]]
- 00bdca14 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdce3c ["INT_ADD", "register:40f0:8", ["const:bdce3c:8", "const:4:8"]]
+ 00bdce3c ["CALL", null, ["callee:00c5af10:8"]]
- 00bdca14 bytes 3ff80194
+ 00bdce3c bytes 35f80194
- 00bdca1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:900:8"]]
- 00bdca1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdce44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
+ 00bdce44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdca1c bytes 608204f9
+ 00bdce44 bytes 608206f9
- 00bdca00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:900:8"]]
- 00bdca00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdce28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
+ 00bdce28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdca00 bytes 688244f9
+ 00bdce28 bytes 688246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75542afb1bbede31fa12c5cd1d385726"></a>

### [`00bdca30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdca30.md) → [`00bdce58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce58.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00bdca5c",
      "incomplete_value": true,
      "site": "00bdca5c",
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
            "const:900:8"
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
    "old": {
      "definition_site": "00bdca44",
      "incomplete_value": true,
      "site": "00bdca44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdca4c",
      "incomplete_value": false,
      "site": "00bdca54",
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
            "const:210:8"
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
      "00bdce68",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdce74",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ],
    [
      "00bdce84",
      "WRITE",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdce68",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdce74",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdce84",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdca54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdca30.md#insn-00bdca54) · [`00bdca5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdca30.md#insn-00bdca5c) · [`00bdca40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdca30.md#insn-00bdca40)
- 新版 `00bdce7c`（命令位置の公開資料なし） · `00bdce84`（命令位置の公開資料なし） · `00bdce68`（命令位置の公開資料なし）

~~~diff
- 00bdca54 ["INT_ADD", "register:40f0:8", ["const:bdca54:8", "const:4:8"]]
- 00bdca54 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdce7c ["INT_ADD", "register:40f0:8", ["const:bdce7c:8", "const:4:8"]]
+ 00bdce7c ["CALL", null, ["callee:00c5af10:8"]]
- 00bdca54 bytes 2ff80194
+ 00bdce7c bytes 25f80194
- 00bdca5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:900:8"]]
- 00bdca5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdce84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
+ 00bdce84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdca5c bytes 608204f9
+ 00bdce84 bytes 608206f9
- 00bdca40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:900:8"]]
- 00bdca40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdce68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
+ 00bdce68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdca40 bytes 688244f9
+ 00bdce68 bytes 688246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c04357f820e619e7cd9f14e0ddc49cd4"></a>

### [`00bdca70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdca70.md) → [`00bdce98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdce98.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

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
      "site": "00bdcaa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdcec8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00bdca84",
      "incomplete_value": true,
      "site": "00bdca84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bdcea8",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdca90",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bdca98",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bdcea8",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdceb8",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdcec0",
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

- 旧版 [`00bdca84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdca70.md#insn-00bdca84) · [`00bdca98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdca70.md#insn-00bdca98) · [`00bdcaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdca70.md#insn-00bdcaa0)
- 新版 `00bdceac`（命令位置の公開資料なし）

~~~diff
- 00bdca84 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bdca84 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bdceac ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bdceac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bdca84 bytes 080100b5
+ 00bdceac bytes 080100b5
- 00bdca98 ["INT_ADD", "register:40f0:8", ["const:bdca98:8", "const:4:8"]]
- 00bdca98 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdca98 bytes 1ef80194
- 00bdcaa0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:900:8"]]
- 00bdcaa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdcaa0 bytes 608204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-685dcfe59129378f2fd3ae8701bad053"></a>

### [`00bdcab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcab4.md) → [`00bdcedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcedc.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00bdcae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdcf0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00bdcac8",
      "incomplete_value": true,
      "site": "00bdcac8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bdceec",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdcad0",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bdcae4",
      "WRITE",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdceec",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcef8",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdcf0c",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcab4.md#insn-00bdcac8) · [`00bdcadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcab4.md#insn-00bdcadc) · [`00bdcae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcab4.md#insn-00bdcae4)
- 新版 `00bdcef0`（命令位置の公開資料なし） · `00bdcf04`（命令位置の公開資料なし）

~~~diff
- 00bdcac8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bdcac8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bdcef0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bdcef0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bdcac8 bytes 080100b5
+ 00bdcef0 bytes 080100b5
- 00bdcadc ["INT_ADD", "register:40f0:8", ["const:bdcadc:8", "const:4:8"]]
- 00bdcadc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdcf04 ["INT_ADD", "register:40f0:8", ["const:bdcf04:8", "const:4:8"]]
+ 00bdcf04 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdcadc bytes 0df80194
+ 00bdcf04 bytes 03f80194
- 00bdcae4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:900:8"]]
- 00bdcae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdcae4 bytes 608204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a053efbf17efd8301c130d4691ee63a9"></a>

### [`00bdcb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcb04.md) → [`00bdcf2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcf2c.md) _ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00bdcb5c",
      "incomplete_value": true,
      "site": "00bdcb5c",
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
            "const:908:8"
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
    "old": {
      "definition_site": "00bdcb38",
      "incomplete_value": true,
      "site": "00bdcb44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bdcf40",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdcf60",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcf84",
      "WRITE",
      [
        "storage",
        "01126908",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdcf40",
      "READ",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdcf60",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcf84",
      "WRITE",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcb44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcb04.md#insn-00bdcb44) · [`00bdcb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcb04.md#insn-00bdcb5c) · [`00bdcb18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcb04.md#insn-00bdcb18)
- 新版 `00bdcf6c`（命令位置の公開資料なし） · `00bdcf84`（命令位置の公開資料なし） · `00bdcf40`（命令位置の公開資料なし）

~~~diff
- 00bdcb44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdcb44 ["INT_ADD", "register:40f0:8", ["const:bdcb44:8", "const:4:8"]]
- 00bdcb44 ["CALLIND", null, ["register:0:8"]]
+ 00bdcf6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdcf6c ["INT_ADD", "register:40f0:8", ["const:bdcf6c:8", "const:4:8"]]
+ 00bdcf6c ["CALLIND", null, ["register:0:8"]]
- 00bdcb44 bytes 00013fd6
+ 00bdcf6c bytes 00013fd6
- 00bdcb5c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bdcb5c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:908:8"]]
- 00bdcb5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bdcf84 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bdcf84 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d08:8"]]
+ 00bdcf84 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bdcb5c bytes a0222439
+ 00bdcf84 bytes a0223439
- 00bdcb18 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:908:8"]]
- 00bdcb18 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bdcb18 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bdcf40 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d08:8"]]
+ 00bdcf40 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bdcf40 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bdcb18 bytes a8226439
+ 00bdcf40 bytes a8227439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a20a7408638242a65f0bc8790c5f71b"></a>

### [`00bdcb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcb70.md) → [`00bdcf98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcf98.md) _ZN8firebase4auth11tokenresult12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00bdcbac",
      "incomplete_value": true,
      "site": "00bdcbac",
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
            "const:908:8"
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
    "old": {
      "definition_site": "00bdcbcc",
      "incomplete_value": true,
      "site": "00bdcbcc",
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
            "const:900:8"
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
    "old": {
      "definition_site": "00bdcb88",
      "incomplete_value": true,
      "site": "00bdcb88",
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
      "00bdcfac",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcfb8",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdcfd4",
      "WRITE",
      [
        "storage",
        "01126908",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdcfac",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdcfb8",
      "READ",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdcfd4",
      "WRITE",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcb70.md#insn-00bdcbac) · [`00bdcbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcb70.md#insn-00bdcbc8) · [`00bdcbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcb70.md#insn-00bdcbcc)
- 新版 `00bdcfd4`（命令位置の公開資料なし） · `00bdcff0`（命令位置の公開資料なし） · `00bdcff4`（命令位置の公開資料なし）

~~~diff
- 00bdcbac ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bdcbac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bdcbac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:908:8"]]
- 00bdcbac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdcfd4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdcfd4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdcfd4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d08:8"]]
+ 00bdcfd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bdcbac bytes bf222439
+ 00bdcfd4 bytes bf223439
- 00bdcbc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdcbc8 ["INT_ADD", "register:40f0:8", ["const:bdcbc8:8", "const:4:8"]]
- 00bdcbc8 ["CALLIND", null, ["register:0:8"]]
+ 00bdcff0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdcff0 ["INT_ADD", "register:40f0:8", ["const:bdcff0:8", "const:4:8"]]
+ 00bdcff0 ["CALLIND", null, ["register:0:8"]]
- 00bdcbc8 bytes 00013fd6
+ 00bdcff0 bytes 00013fd6
- 00bdcbcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:900:8"]]
- 00bdcbcc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bdcbcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdcff4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
+ 00bdcff4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdcff4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bdcbcc bytes 9f8204f9
+ 00bdcff4 bytes 9f8206f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6a707d822b8f94b4c562756f77bd1b0"></a>

### [`00bdcbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcbe0.md) → [`00bdd008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd008.md) _ZN8firebase4auth11tokenresult14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bdcc20",
      "incomplete_value": true,
      "site": "00bdcc20",
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
            "const:900:8"
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
    "old": {
      "definition_site": "00bdcbfc",
      "incomplete_value": true,
      "site": "00bdcbfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdcc04",
      "incomplete_value": false,
      "site": "00bdcc18",
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
            "const:210:8"
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
      "00bdd01c",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd02c",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ],
    [
      "00bdd048",
      "WRITE",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd01c",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd02c",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdd048",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcbe0.md#insn-00bdcc18) · [`00bdcc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcbe0.md#insn-00bdcc20) · [`00bdcbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcbe0.md#insn-00bdcbf4)
- 新版 `00bdd040`（命令位置の公開資料なし） · `00bdd048`（命令位置の公開資料なし） · `00bdd01c`（命令位置の公開資料なし）

~~~diff
- 00bdcc18 ["INT_ADD", "register:40f0:8", ["const:bdcc18:8", "const:4:8"]]
- 00bdcc18 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd040 ["INT_ADD", "register:40f0:8", ["const:bdd040:8", "const:4:8"]]
+ 00bdd040 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdcc18 bytes bef70194
+ 00bdd040 bytes b4f70194
- 00bdcc20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:900:8"]]
- 00bdcc20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd048 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
+ 00bdd048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdcc20 bytes 808204f9
+ 00bdd048 bytes 808206f9
- 00bdcbf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:900:8"]]
- 00bdcbf4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd01c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
+ 00bdd01c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcbf4 bytes 818244f9
+ 00bdd01c bytes 818246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c2ccf9f3e36c205e9a4941e553144d1"></a>

### [`00bdcc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcc50.md) → [`00bdd078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd078.md) _ZN8firebase4auth11tokenresult11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00bdcc6c",
      "incomplete_value": false,
      "site": "00bdcc70",
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
    "old": {
      "definition_site": "00bdcc7c",
      "incomplete_value": true,
      "site": "00bdcc88",
      "value": [
        "LOAD",
        "8",
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
      "00bdd094",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bdd0a4",
      "DATA",
      [
        "storage",
        "01126910",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd094",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bdd0a4",
      "DATA",
      [
        "storage",
        "01126d10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcc50.md#insn-00bdcc70) · [`00bdcc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcc50.md#insn-00bdcc6c) · [`00bdcc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcc50.md#insn-00bdcc78)
- 新版 `00bdd098`（命令位置の公開資料なし） · `00bdd094`（命令位置の公開資料なし） · `00bdd0a0`（命令位置の公開資料なし）

~~~diff
- 00bdcc70 ["INT_ADD", "register:40f0:8", ["const:bdcc70:8", "const:4:8"]]
- 00bdcc70 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdd098 ["INT_ADD", "register:40f0:8", ["const:bdd098:8", "const:4:8"]]
+ 00bdd098 ["CALL", null, ["callee:00c5b000:8"]]
- 00bdcc70 bytes e4f70194
+ 00bdd098 bytes daf70194
- 00bdcc6c ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bdcc6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdcc6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdcc6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd094 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bdd094 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd094 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd094 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdcc6c bytes 00680a91
+ 00bdd094 bytes 009c0d91
- 00bdcc78 ["COPY", "tmp:0:8", ["const:910:8"]]
- 00bdcc78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdcc78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdcc78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdd0a0 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00bdd0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdcc78 bytes 08412491
+ 00bdd0a0 bytes 08413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60077a673d52c638e66fb4a8b730090b"></a>

### [`00bdcc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcc8c.md) → [`00bdd0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd0b4.md) _ZN8firebase4auth11tokenresult13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bdcccc",
      "incomplete_value": true,
      "site": "00bdcccc",
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
            "const:900:8"
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
    "old": {
      "definition_site": "00bdcca8",
      "incomplete_value": true,
      "site": "00bdcca8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdccb0",
      "incomplete_value": false,
      "site": "00bdccc4",
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
            "const:210:8"
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
      "00bdd0c8",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd0d8",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ],
    [
      "00bdd0f4",
      "WRITE",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd0c8",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd0d8",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ],
    [
      "00bdd0f4",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdccc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcc8c.md#insn-00bdccc4) · [`00bdcccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcc8c.md#insn-00bdcccc) · [`00bdcca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcc8c.md#insn-00bdcca0)
- 新版 `00bdd0ec`（命令位置の公開資料なし） · `00bdd0f4`（命令位置の公開資料なし） · `00bdd0c8`（命令位置の公開資料なし）

~~~diff
- 00bdccc4 ["INT_ADD", "register:40f0:8", ["const:bdccc4:8", "const:4:8"]]
- 00bdccc4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd0ec ["INT_ADD", "register:40f0:8", ["const:bdd0ec:8", "const:4:8"]]
+ 00bdd0ec ["CALL", null, ["callee:00c5af10:8"]]
- 00bdccc4 bytes 93f70194
+ 00bdd0ec bytes 89f70194
- 00bdcccc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:900:8"]]
- 00bdcccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd0f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
+ 00bdd0f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdcccc bytes 808204f9
+ 00bdd0f4 bytes 808206f9
- 00bdcca0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:900:8"]]
- 00bdcca0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd0c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
+ 00bdd0c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcca0 bytes 818244f9
+ 00bdd0c8 bytes 818246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b56787f738c0024deedc614968469a7"></a>

### [`00bdccfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdccfc.md) → [`00bdd124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd124.md) _ZN8firebase4auth11tokenresult10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00bdcd18",
      "incomplete_value": false,
      "site": "00bdcd1c",
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
    "old": {
      "definition_site": "00bdcd28",
      "incomplete_value": true,
      "site": "00bdcd34",
      "value": [
        "LOAD",
        "8",
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
      "00bdd140",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bdd150",
      "DATA",
      [
        "storage",
        "01126918",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdd140",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bdd150",
      "DATA",
      [
        "storage",
        "01126d18",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdccfc.md#insn-00bdcd1c) · [`00bdcd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdccfc.md#insn-00bdcd18) · [`00bdcd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdccfc.md#insn-00bdcd24)
- 新版 `00bdd144`（命令位置の公開資料なし） · `00bdd140`（命令位置の公開資料なし） · `00bdd14c`（命令位置の公開資料なし）

~~~diff
- 00bdcd1c ["INT_ADD", "register:40f0:8", ["const:bdcd1c:8", "const:4:8"]]
- 00bdcd1c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdd144 ["INT_ADD", "register:40f0:8", ["const:bdd144:8", "const:4:8"]]
+ 00bdd144 ["CALL", null, ["callee:00c5b000:8"]]
- 00bdcd1c bytes b9f70194
+ 00bdd144 bytes aff70194
- 00bdcd18 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bdcd18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdcd18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdcd18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd140 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bdd140 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd140 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd140 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdcd18 bytes 00441191
+ 00bdd140 bytes 00781491
- 00bdcd24 ["COPY", "tmp:0:8", ["const:918:8"]]
- 00bdcd24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdcd24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdcd24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdd14c ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00bdd14c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd14c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd14c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdcd24 bytes 08612491
+ 00bdd14c bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94a0c158486b6aeeaabbc723a2b5fb78"></a>

### [`00bdcd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcd38.md) → [`00bdd160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd160.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

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
    "old": {
      "definition_site": "00bdcd64",
      "incomplete_value": true,
      "site": "00bdcd64",
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
            "const:920:8"
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
    "old": {
      "definition_site": "00bdcd4c",
      "incomplete_value": true,
      "site": "00bdcd4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdcd58",
      "incomplete_value": false,
      "site": "00bdcd5c",
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
            "const:7ba:8"
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
      "00bdd170",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd180",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bdd18c",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd170",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd180",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd18c",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcd38.md#insn-00bdcd5c) · [`00bdcd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcd38.md#insn-00bdcd64) · [`00bdcd48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcd38.md#insn-00bdcd48)
- 新版 `00bdd184`（命令位置の公開資料なし） · `00bdd18c`（命令位置の公開資料なし） · `00bdd170`（命令位置の公開資料なし）

~~~diff
- 00bdcd5c ["INT_ADD", "register:40f0:8", ["const:bdcd5c:8", "const:4:8"]]
- 00bdcd5c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd184 ["INT_ADD", "register:40f0:8", ["const:bdd184:8", "const:4:8"]]
+ 00bdd184 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdcd5c bytes 6df70194
+ 00bdd184 bytes 63f70194
- 00bdcd64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00bdcd64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd18c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00bdd18c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdcd64 bytes 609204f9
+ 00bdd18c bytes 609206f9
- 00bdcd48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00bdcd48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd170 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00bdd170 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcd48 bytes 689244f9
+ 00bdd170 bytes 689246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70355f93fca9765317e649a411011010"></a>

### [`00bdcd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcd78.md) → [`00bdd1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd1a0.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00bdcda4",
      "incomplete_value": true,
      "site": "00bdcda4",
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
            "const:920:8"
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
    "old": {
      "definition_site": "00bdcd8c",
      "incomplete_value": true,
      "site": "00bdcd8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdcd94",
      "incomplete_value": false,
      "site": "00bdcd9c",
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
            "const:7ba:8"
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
      "00bdd1b0",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd1bc",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bdd1cc",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd1b0",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd1bc",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd1cc",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcd78.md#insn-00bdcd9c) · [`00bdcda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcd78.md#insn-00bdcda4) · [`00bdcd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcd78.md#insn-00bdcd88)
- 新版 `00bdd1c4`（命令位置の公開資料なし） · `00bdd1cc`（命令位置の公開資料なし） · `00bdd1b0`（命令位置の公開資料なし）

~~~diff
- 00bdcd9c ["INT_ADD", "register:40f0:8", ["const:bdcd9c:8", "const:4:8"]]
- 00bdcd9c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd1c4 ["INT_ADD", "register:40f0:8", ["const:bdd1c4:8", "const:4:8"]]
+ 00bdd1c4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdcd9c bytes 5df70194
+ 00bdd1c4 bytes 53f70194
- 00bdcda4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00bdcda4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd1cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00bdd1cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdcda4 bytes 609204f9
+ 00bdd1cc bytes 609206f9
- 00bdcd88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00bdcd88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd1b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00bdd1b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcd88 bytes 689244f9
+ 00bdd1b0 bytes 689246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69e16874243fbd745abbe0b70da2b540"></a>

### [`00bdcdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcdb8.md) → [`00bdd1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd1e0.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
    "old": {
      "definition_site": "00bdcde8",
      "incomplete_value": true,
      "site": "00bdcde8",
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
            "const:920:8"
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
    "old": {
      "definition_site": "00bdcdcc",
      "incomplete_value": true,
      "site": "00bdcdcc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdcdd8",
      "incomplete_value": false,
      "site": "00bdcde0",
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
            "const:7ba:8"
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
      "00bdd1f0",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd200",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bdd210",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd1f0",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd200",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd210",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcdb8.md#insn-00bdcde0) · [`00bdcde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcdb8.md#insn-00bdcde8) · [`00bdcdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcdb8.md#insn-00bdcdc8)
- 新版 `00bdd208`（命令位置の公開資料なし） · `00bdd210`（命令位置の公開資料なし） · `00bdd1f0`（命令位置の公開資料なし）

~~~diff
- 00bdcde0 ["INT_ADD", "register:40f0:8", ["const:bdcde0:8", "const:4:8"]]
- 00bdcde0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd208 ["INT_ADD", "register:40f0:8", ["const:bdd208:8", "const:4:8"]]
+ 00bdd208 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdcde0 bytes 4cf70194
+ 00bdd208 bytes 42f70194
- 00bdcde8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00bdcde8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd210 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00bdd210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdcde8 bytes 609204f9
+ 00bdd210 bytes 609206f9
- 00bdcdc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00bdcdc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd1f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00bdd1f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcdc8 bytes 689244f9
+ 00bdd1f0 bytes 689246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ee807ffe6e67536518e8cc13643a08b"></a>

### [`00bdcdfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcdfc.md) → [`00bdd224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd224.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bdce2c",
      "incomplete_value": true,
      "site": "00bdce2c",
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
            "const:920:8"
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
    "old": {
      "definition_site": "00bdce10",
      "incomplete_value": true,
      "site": "00bdce10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdce18",
      "incomplete_value": false,
      "site": "00bdce24",
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
            "const:7ba:8"
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
      "00bdd234",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd240",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bdd254",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd234",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd240",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd254",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdce24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcdfc.md#insn-00bdce24) · [`00bdce2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcdfc.md#insn-00bdce2c) · [`00bdce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcdfc.md#insn-00bdce0c)
- 新版 `00bdd24c`（命令位置の公開資料なし） · `00bdd254`（命令位置の公開資料なし） · `00bdd234`（命令位置の公開資料なし）

~~~diff
- 00bdce24 ["INT_ADD", "register:40f0:8", ["const:bdce24:8", "const:4:8"]]
- 00bdce24 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd24c ["INT_ADD", "register:40f0:8", ["const:bdd24c:8", "const:4:8"]]
+ 00bdd24c ["CALL", null, ["callee:00c5af10:8"]]
- 00bdce24 bytes 3bf70194
+ 00bdd24c bytes 31f70194
- 00bdce2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00bdce2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd254 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00bdd254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdce2c bytes 609204f9
+ 00bdd254 bytes 609206f9
- 00bdce0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00bdce0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd234 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00bdd234 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdce0c bytes 689244f9
+ 00bdd234 bytes 689246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-118291f13241dc6e0155566ce69ce2c5"></a>

### [`00bdce4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdce4c.md) → [`00bdd274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd274.md) _ZN8firebase4auth4user15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00bdcea4",
      "incomplete_value": true,
      "site": "00bdcea4",
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
            "const:928:8"
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
    "old": {
      "definition_site": "00bdce80",
      "incomplete_value": true,
      "site": "00bdce8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
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
      "00bdd288",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd2a8",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd2cc",
      "WRITE",
      [
        "storage",
        "01126928",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd288",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd2a8",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd2cc",
      "WRITE",
      [
        "storage",
        "01126d28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdce8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdce4c.md#insn-00bdce8c) · [`00bdcea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdce4c.md#insn-00bdcea4) · [`00bdce60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdce4c.md#insn-00bdce60)
- 新版 `00bdd2b4`（命令位置の公開資料なし） · `00bdd2cc`（命令位置の公開資料なし） · `00bdd288`（命令位置の公開資料なし）

~~~diff
- 00bdce8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdce8c ["INT_ADD", "register:40f0:8", ["const:bdce8c:8", "const:4:8"]]
- 00bdce8c ["CALLIND", null, ["register:0:8"]]
+ 00bdd2b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd2b4 ["INT_ADD", "register:40f0:8", ["const:bdd2b4:8", "const:4:8"]]
+ 00bdd2b4 ["CALLIND", null, ["register:0:8"]]
- 00bdce8c bytes 00013fd6
+ 00bdd2b4 bytes 00013fd6
- 00bdcea4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bdcea4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:928:8"]]
- 00bdcea4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bdd2cc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bdd2cc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d28:8"]]
+ 00bdd2cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bdcea4 bytes a0a22439
+ 00bdd2cc bytes a0a23439
- 00bdce60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:928:8"]]
- 00bdce60 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bdce60 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bdd288 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d28:8"]]
+ 00bdd288 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd288 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bdce60 bytes a8a26439
+ 00bdd288 bytes a8a27439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd9b5320f3245e9f7f93b8a1f9ebdff4"></a>

### [`00bdceb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdceb8.md) → [`00bdd2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd2e0.md) _ZN8firebase4auth4user12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00bdcef4",
      "incomplete_value": true,
      "site": "00bdcef4",
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
            "const:928:8"
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
    "old": {
      "definition_site": "00bdcf14",
      "incomplete_value": true,
      "site": "00bdcf14",
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
            "const:920:8"
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
    "old": {
      "definition_site": "00bdced0",
      "incomplete_value": true,
      "site": "00bdced0",
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
      "00bdd2f4",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd300",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd31c",
      "WRITE",
      [
        "storage",
        "01126928",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd2f4",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd300",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd31c",
      "WRITE",
      [
        "storage",
        "01126d28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdceb8.md#insn-00bdcef4) · [`00bdcf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdceb8.md#insn-00bdcf10) · [`00bdcf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdceb8.md#insn-00bdcf14)
- 新版 `00bdd31c`（命令位置の公開資料なし） · `00bdd338`（命令位置の公開資料なし） · `00bdd33c`（命令位置の公開資料なし）

~~~diff
- 00bdcef4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bdcef4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bdcef4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:928:8"]]
- 00bdcef4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdd31c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdd31c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdd31c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d28:8"]]
+ 00bdd31c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bdcef4 bytes bfa22439
+ 00bdd31c bytes bfa23439
- 00bdcf10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdcf10 ["INT_ADD", "register:40f0:8", ["const:bdcf10:8", "const:4:8"]]
- 00bdcf10 ["CALLIND", null, ["register:0:8"]]
+ 00bdd338 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd338 ["INT_ADD", "register:40f0:8", ["const:bdd338:8", "const:4:8"]]
+ 00bdd338 ["CALLIND", null, ["register:0:8"]]
- 00bdcf10 bytes 00013fd6
+ 00bdd338 bytes 00013fd6
- 00bdcf14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00bdcf14 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bdcf14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdd33c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00bdd33c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdd33c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bdcf14 bytes 9f9204f9
+ 00bdd33c bytes 9f9206f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af5033aa9c71e251214ac932c6b7580e"></a>

### [`00bdcf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcf28.md) → [`00bdd350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd350.md) _ZN8firebase4auth4user14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bdcf68",
      "incomplete_value": true,
      "site": "00bdcf68",
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
            "const:920:8"
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
    "old": {
      "definition_site": "00bdcf44",
      "incomplete_value": true,
      "site": "00bdcf44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdcf4c",
      "incomplete_value": false,
      "site": "00bdcf60",
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
            "const:7ba:8"
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
      "00bdd364",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd374",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bdd390",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd364",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd374",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd390",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcf60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcf28.md#insn-00bdcf60) · [`00bdcf68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcf28.md#insn-00bdcf68) · [`00bdcf3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcf28.md#insn-00bdcf3c)
- 新版 `00bdd388`（命令位置の公開資料なし） · `00bdd390`（命令位置の公開資料なし） · `00bdd364`（命令位置の公開資料なし）

~~~diff
- 00bdcf60 ["INT_ADD", "register:40f0:8", ["const:bdcf60:8", "const:4:8"]]
- 00bdcf60 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd388 ["INT_ADD", "register:40f0:8", ["const:bdd388:8", "const:4:8"]]
+ 00bdd388 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdcf60 bytes ecf60194
+ 00bdd388 bytes e2f60194
- 00bdcf68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00bdcf68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd390 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00bdd390 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdcf68 bytes 809204f9
+ 00bdd390 bytes 809206f9
- 00bdcf3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00bdcf3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd364 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00bdd364 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcf3c bytes 819244f9
+ 00bdd364 bytes 819246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b8b150bf0637e3b414c4533a865e478"></a>

### [`00bdcf98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcf98.md) → [`00bdd3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd3c0.md) _ZN8firebase4auth4user11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00bdcfb4",
      "incomplete_value": false,
      "site": "00bdcfb8",
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
    "old": {
      "definition_site": "00bdcfc4",
      "incomplete_value": true,
      "site": "00bdcfd0",
      "value": [
        "LOAD",
        "8",
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
      "00bdd3dc",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bdd3ec",
      "DATA",
      [
        "storage",
        "01126930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd3dc",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bdd3ec",
      "DATA",
      [
        "storage",
        "01126d30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcfb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcf98.md#insn-00bdcfb8) · [`00bdcfb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcf98.md#insn-00bdcfb4) · [`00bdcfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcf98.md#insn-00bdcfc0)
- 新版 `00bdd3e0`（命令位置の公開資料なし） · `00bdd3dc`（命令位置の公開資料なし） · `00bdd3e8`（命令位置の公開資料なし）

~~~diff
- 00bdcfb8 ["INT_ADD", "register:40f0:8", ["const:bdcfb8:8", "const:4:8"]]
- 00bdcfb8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdd3e0 ["INT_ADD", "register:40f0:8", ["const:bdd3e0:8", "const:4:8"]]
+ 00bdd3e0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bdcfb8 bytes 12f70194
+ 00bdd3e0 bytes 08f70194
- 00bdcfb4 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bdcfb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdcfb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdcfb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd3dc ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bdd3dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd3dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd3dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdcfb4 bytes 00680a91
+ 00bdd3dc bytes 009c0d91
- 00bdcfc0 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00bdcfc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdcfc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdcfc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdd3e8 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00bdd3e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd3e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd3e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdcfc0 bytes 08c12491
+ 00bdd3e8 bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1720f937dbe70fd872111a6dda27fb51"></a>

### [`00bdcfd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcfd4.md) → [`00bdd3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd3fc.md) _ZN8firebase4auth4user13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bdd014",
      "incomplete_value": true,
      "site": "00bdd014",
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
            "const:920:8"
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
    "old": {
      "definition_site": "00bdcff0",
      "incomplete_value": true,
      "site": "00bdcff0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdcff8",
      "incomplete_value": false,
      "site": "00bdd00c",
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
            "const:7ba:8"
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
      "00bdd410",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd420",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ],
    [
      "00bdd43c",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd410",
      "READ",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd420",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ],
    [
      "00bdd43c",
      "WRITE",
      [
        "storage",
        "01126d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcfd4.md#insn-00bdd00c) · [`00bdd014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcfd4.md#insn-00bdd014) · [`00bdcfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdcfd4.md#insn-00bdcfe8)
- 新版 `00bdd434`（命令位置の公開資料なし） · `00bdd43c`（命令位置の公開資料なし） · `00bdd410`（命令位置の公開資料なし）

~~~diff
- 00bdd00c ["INT_ADD", "register:40f0:8", ["const:bdd00c:8", "const:4:8"]]
- 00bdd00c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd434 ["INT_ADD", "register:40f0:8", ["const:bdd434:8", "const:4:8"]]
+ 00bdd434 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd00c bytes c1f60194
+ 00bdd434 bytes b7f60194
- 00bdd014 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00bdd014 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd43c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00bdd43c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd014 bytes 809204f9
+ 00bdd43c bytes 809206f9
- 00bdcfe8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00bdcfe8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd410 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00bdd410 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcfe8 bytes 819244f9
+ 00bdd410 bytes 819246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-934471451d888e8a61d8515c76bf91ca"></a>

### [`00bdd044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd044.md) → [`00bdd46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd46c.md) _ZN8firebase4auth4user10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00bdd060",
      "incomplete_value": false,
      "site": "00bdd064",
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
    "old": {
      "definition_site": "00bdd070",
      "incomplete_value": true,
      "site": "00bdd07c",
      "value": [
        "LOAD",
        "8",
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
      "00bdd488",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bdd498",
      "DATA",
      [
        "storage",
        "011269a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdd488",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bdd498",
      "DATA",
      [
        "storage",
        "01126da8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd044.md#insn-00bdd064) · [`00bdd060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd044.md#insn-00bdd060) · [`00bdd06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd044.md#insn-00bdd06c)
- 新版 `00bdd48c`（命令位置の公開資料なし） · `00bdd488`（命令位置の公開資料なし） · `00bdd494`（命令位置の公開資料なし）

~~~diff
- 00bdd064 ["INT_ADD", "register:40f0:8", ["const:bdd064:8", "const:4:8"]]
- 00bdd064 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdd48c ["INT_ADD", "register:40f0:8", ["const:bdd48c:8", "const:4:8"]]
+ 00bdd48c ["CALL", null, ["callee:00c5b000:8"]]
- 00bdd064 bytes e7f60194
+ 00bdd48c bytes ddf60194
- 00bdd060 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bdd060 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd060 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd060 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd488 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bdd488 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd488 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd488 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdd060 bytes 00441191
+ 00bdd488 bytes 00781491
- 00bdd06c ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 00bdd06c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd06c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd06c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdd494 ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 00bdd494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdd06c bytes 08a12691
+ 00bdd494 bytes 08a13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-274a54b8158aeba2b44f217cec38afba"></a>

### [`00bdd080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd080.md) → [`00bdd4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd4a8.md) _ZN8firebase4auth8userinfo19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
    "old": {
      "definition_site": "00bdd0ac",
      "incomplete_value": true,
      "site": "00bdd0ac",
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
            "const:9b0:8"
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
    "old": {
      "definition_site": "00bdd094",
      "incomplete_value": true,
      "site": "00bdd094",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd0a0",
      "incomplete_value": false,
      "site": "00bdd0a4",
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
            "const:73c:8"
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
      "00bdd4b8",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd4c8",
      "PARAM",
      [
        "storage",
        "002b173c",
        null,
        "string"
      ]
    ],
    [
      "00bdd4d4",
      "WRITE",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd4b8",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd4c8",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ],
    [
      "00bdd4d4",
      "WRITE",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd080.md#insn-00bdd0a4) · [`00bdd0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd080.md#insn-00bdd0ac) · [`00bdd090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd080.md#insn-00bdd090)
- 新版 `00bdd4cc`（命令位置の公開資料なし） · `00bdd4d4`（命令位置の公開資料なし） · `00bdd4b8`（命令位置の公開資料なし）

~~~diff
- 00bdd0a4 ["INT_ADD", "register:40f0:8", ["const:bdd0a4:8", "const:4:8"]]
- 00bdd0a4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd4cc ["INT_ADD", "register:40f0:8", ["const:bdd4cc:8", "const:4:8"]]
+ 00bdd4cc ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd0a4 bytes 9bf60194
+ 00bdd4cc bytes 91f60194
- 00bdd0ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b0:8"]]
- 00bdd0ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd4d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bdd4d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd0ac bytes 60da04f9
+ 00bdd4d4 bytes 60da06f9
- 00bdd090 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b0:8"]]
- 00bdd090 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd4b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bdd4b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd090 bytes 68da44f9
+ 00bdd4b8 bytes 68da46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cbce24b7c9740554476fdf1e1808016"></a>

### [`00bdd0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd0c0.md) → [`00bdd4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd4e8.md) _ZN8firebase4auth8userinfo19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00bdd0ec",
      "incomplete_value": true,
      "site": "00bdd0ec",
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
            "const:9b0:8"
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
    "old": {
      "definition_site": "00bdd0d4",
      "incomplete_value": true,
      "site": "00bdd0d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd0dc",
      "incomplete_value": false,
      "site": "00bdd0e4",
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
            "const:73c:8"
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
      "00bdd4f8",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd504",
      "PARAM",
      [
        "storage",
        "002b173c",
        null,
        "string"
      ]
    ],
    [
      "00bdd514",
      "WRITE",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd4f8",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd504",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ],
    [
      "00bdd514",
      "WRITE",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd0c0.md#insn-00bdd0e4) · [`00bdd0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd0c0.md#insn-00bdd0ec) · [`00bdd0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd0c0.md#insn-00bdd0d0)
- 新版 `00bdd50c`（命令位置の公開資料なし） · `00bdd514`（命令位置の公開資料なし） · `00bdd4f8`（命令位置の公開資料なし）

~~~diff
- 00bdd0e4 ["INT_ADD", "register:40f0:8", ["const:bdd0e4:8", "const:4:8"]]
- 00bdd0e4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd50c ["INT_ADD", "register:40f0:8", ["const:bdd50c:8", "const:4:8"]]
+ 00bdd50c ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd0e4 bytes 8bf60194
+ 00bdd50c bytes 81f60194
- 00bdd0ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b0:8"]]
- 00bdd0ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd514 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bdd514 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd0ec bytes 60da04f9
+ 00bdd514 bytes 60da06f9
- 00bdd0d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b0:8"]]
- 00bdd0d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd4f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bdd4f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd0d0 bytes 68da44f9
+ 00bdd4f8 bytes 68da46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01bce531d0b140ff4bc55e1ec5d2d9e9"></a>

### [`00bdd100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd100.md) → [`00bdd528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd528.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
    "old": {
      "definition_site": "00bdd130",
      "incomplete_value": true,
      "site": "00bdd130",
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
            "const:9b0:8"
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
    "old": {
      "definition_site": "00bdd114",
      "incomplete_value": true,
      "site": "00bdd114",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd120",
      "incomplete_value": false,
      "site": "00bdd128",
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
            "const:73c:8"
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
      "00bdd538",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd548",
      "PARAM",
      [
        "storage",
        "002b173c",
        null,
        "string"
      ]
    ],
    [
      "00bdd558",
      "WRITE",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd538",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd548",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ],
    [
      "00bdd558",
      "WRITE",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd100.md#insn-00bdd128) · [`00bdd130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd100.md#insn-00bdd130) · [`00bdd110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd100.md#insn-00bdd110)
- 新版 `00bdd550`（命令位置の公開資料なし） · `00bdd558`（命令位置の公開資料なし） · `00bdd538`（命令位置の公開資料なし）

~~~diff
- 00bdd128 ["INT_ADD", "register:40f0:8", ["const:bdd128:8", "const:4:8"]]
- 00bdd128 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd550 ["INT_ADD", "register:40f0:8", ["const:bdd550:8", "const:4:8"]]
+ 00bdd550 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd128 bytes 7af60194
+ 00bdd550 bytes 70f60194
- 00bdd130 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b0:8"]]
- 00bdd130 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd558 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bdd558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd130 bytes 60da04f9
+ 00bdd558 bytes 60da06f9
- 00bdd110 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b0:8"]]
- 00bdd110 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bdd538 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd110 bytes 68da44f9
+ 00bdd538 bytes 68da46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c82d3156985ee04965830dd99a3bc7b"></a>

### [`00bdd144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd144.md) → [`00bdd56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd56c.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bdd174",
      "incomplete_value": true,
      "site": "00bdd174",
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
            "const:9b0:8"
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
    "old": {
      "definition_site": "00bdd158",
      "incomplete_value": true,
      "site": "00bdd158",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd160",
      "incomplete_value": false,
      "site": "00bdd16c",
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
            "const:73c:8"
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
      "00bdd57c",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd588",
      "PARAM",
      [
        "storage",
        "002b173c",
        null,
        "string"
      ]
    ],
    [
      "00bdd59c",
      "WRITE",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd57c",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd588",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ],
    [
      "00bdd59c",
      "WRITE",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd144.md#insn-00bdd16c) · [`00bdd174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd144.md#insn-00bdd174) · [`00bdd154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd144.md#insn-00bdd154)
- 新版 `00bdd594`（命令位置の公開資料なし） · `00bdd59c`（命令位置の公開資料なし） · `00bdd57c`（命令位置の公開資料なし）

~~~diff
- 00bdd16c ["INT_ADD", "register:40f0:8", ["const:bdd16c:8", "const:4:8"]]
- 00bdd16c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd594 ["INT_ADD", "register:40f0:8", ["const:bdd594:8", "const:4:8"]]
+ 00bdd594 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd16c bytes 69f60194
+ 00bdd594 bytes 5ff60194
- 00bdd174 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b0:8"]]
- 00bdd174 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd59c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bdd59c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd174 bytes 60da04f9
+ 00bdd59c bytes 60da06f9
- 00bdd154 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b0:8"]]
- 00bdd154 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd57c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bdd57c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd154 bytes 68da44f9
+ 00bdd57c bytes 68da46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4aa626d08391f719f0c5196a0a0d9306"></a>

### [`00bdd194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd194.md) → [`00bdd5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd5bc.md) _ZN8firebase4auth8userinfo15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00bdd1ec",
      "incomplete_value": true,
      "site": "00bdd1ec",
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
            "const:9b8:8"
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
    "old": {
      "definition_site": "00bdd1c8",
      "incomplete_value": true,
      "site": "00bdd1d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9b0:8"
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
      "00bdd5d0",
      "READ",
      [
        "storage",
        "011269b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd5f0",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd614",
      "WRITE",
      [
        "storage",
        "011269b8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd5d0",
      "READ",
      [
        "storage",
        "01126db8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd5f0",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd614",
      "WRITE",
      [
        "storage",
        "01126db8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd194.md#insn-00bdd1d4) · [`00bdd1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd194.md#insn-00bdd1ec) · [`00bdd1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd194.md#insn-00bdd1a8)
- 新版 `00bdd5fc`（命令位置の公開資料なし） · `00bdd614`（命令位置の公開資料なし） · `00bdd5d0`（命令位置の公開資料なし）

~~~diff
- 00bdd1d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdd1d4 ["INT_ADD", "register:40f0:8", ["const:bdd1d4:8", "const:4:8"]]
- 00bdd1d4 ["CALLIND", null, ["register:0:8"]]
+ 00bdd5fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd5fc ["INT_ADD", "register:40f0:8", ["const:bdd5fc:8", "const:4:8"]]
+ 00bdd5fc ["CALLIND", null, ["register:0:8"]]
- 00bdd1d4 bytes 00013fd6
+ 00bdd5fc bytes 00013fd6
- 00bdd1ec ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bdd1ec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b8:8"]]
- 00bdd1ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bdd614 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bdd614 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:db8:8"]]
+ 00bdd614 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bdd1ec bytes a0e22639
+ 00bdd614 bytes a0e23639
- 00bdd1a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b8:8"]]
- 00bdd1a8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bdd1a8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bdd5d0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:db8:8"]]
+ 00bdd5d0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd5d0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bdd1a8 bytes a8e26639
+ 00bdd5d0 bytes a8e27639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1673b26932359f75c387b8357310d070"></a>

### [`00bdd200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd200.md) → [`00bdd628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd628.md) _ZN8firebase4auth8userinfo12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00bdd23c",
      "incomplete_value": true,
      "site": "00bdd23c",
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
            "const:9b8:8"
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
    "old": {
      "definition_site": "00bdd25c",
      "incomplete_value": true,
      "site": "00bdd25c",
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
            "const:9b0:8"
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
    "old": {
      "definition_site": "00bdd218",
      "incomplete_value": true,
      "site": "00bdd218",
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
      "00bdd63c",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd648",
      "READ",
      [
        "storage",
        "011269b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd664",
      "WRITE",
      [
        "storage",
        "011269b8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd63c",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd648",
      "READ",
      [
        "storage",
        "01126db8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd664",
      "WRITE",
      [
        "storage",
        "01126db8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd200.md#insn-00bdd23c) · [`00bdd258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd200.md#insn-00bdd258) · [`00bdd25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd200.md#insn-00bdd25c)
- 新版 `00bdd664`（命令位置の公開資料なし） · `00bdd680`（命令位置の公開資料なし） · `00bdd684`（命令位置の公開資料なし）

~~~diff
- 00bdd23c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bdd23c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bdd23c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b8:8"]]
- 00bdd23c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdd664 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdd664 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdd664 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:db8:8"]]
+ 00bdd664 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bdd23c bytes bfe22639
+ 00bdd664 bytes bfe23639
- 00bdd258 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdd258 ["INT_ADD", "register:40f0:8", ["const:bdd258:8", "const:4:8"]]
- 00bdd258 ["CALLIND", null, ["register:0:8"]]
+ 00bdd680 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd680 ["INT_ADD", "register:40f0:8", ["const:bdd680:8", "const:4:8"]]
+ 00bdd680 ["CALLIND", null, ["register:0:8"]]
- 00bdd258 bytes 00013fd6
+ 00bdd680 bytes 00013fd6
- 00bdd25c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b0:8"]]
- 00bdd25c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bdd25c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdd684 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
+ 00bdd684 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdd684 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bdd25c bytes 9fda04f9
+ 00bdd684 bytes 9fda06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1310675a337b72feec7572d83cba34c6"></a>

### [`00bdd270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd270.md) → [`00bdd698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd698.md) _ZN8firebase4auth8userinfo14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00bdd2b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd6d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdd28c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd284",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdd28c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd6dc"
      ]
    ],
    [
      "unmatched:00bdd294",
      "PARAM",
      [
        "storage",
        "002b173c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdd6ac",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd6b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd6dc"
      ]
    ],
    [
      "00bdd6bc",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd270.md#insn-00bdd28c) · [`00bdd2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd270.md#insn-00bdd2a8) · [`00bdd2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd270.md#insn-00bdd2b0)
- 新版 `00bdd6d0`（命令位置の公開資料なし）

~~~diff
- 00bdd28c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bdd28c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bdd28c bytes 410100b5
- 00bdd2a8 ["INT_ADD", "register:40f0:8", ["const:bdd2a8:8", "const:4:8"]]
- 00bdd2a8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd6d0 ["INT_ADD", "register:40f0:8", ["const:bdd6d0:8", "const:4:8"]]
+ 00bdd6d0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd2a8 bytes 1af60194
+ 00bdd6d0 bytes 10f60194
- 00bdd2b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b0:8"]]
- 00bdd2b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd2b0 bytes 80da04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c024a8c20c95b1dead07ab0b7a766b79"></a>

### [`00bdd31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd31c.md) → [`00bdd744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd744.md) _ZN8firebase4auth8userinfo13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bdd35c",
      "incomplete_value": true,
      "site": "00bdd35c",
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
            "const:9b0:8"
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
    "old": {
      "definition_site": "00bdd338",
      "incomplete_value": true,
      "site": "00bdd338",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd340",
      "incomplete_value": false,
      "site": "00bdd354",
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
            "const:73c:8"
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
      "00bdd758",
      "READ",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd768",
      "PARAM",
      [
        "storage",
        "002b173c",
        null,
        "string"
      ]
    ],
    [
      "00bdd784",
      "WRITE",
      [
        "storage",
        "011269b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd758",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd768",
      "PARAM",
      [
        "storage",
        "002b177c",
        null,
        "string"
      ]
    ],
    [
      "00bdd784",
      "WRITE",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd31c.md#insn-00bdd354) · [`00bdd35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd31c.md#insn-00bdd35c) · [`00bdd330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd31c.md#insn-00bdd330)
- 新版 `00bdd77c`（命令位置の公開資料なし） · `00bdd784`（命令位置の公開資料なし） · `00bdd758`（命令位置の公開資料なし）

~~~diff
- 00bdd354 ["INT_ADD", "register:40f0:8", ["const:bdd354:8", "const:4:8"]]
- 00bdd354 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd77c ["INT_ADD", "register:40f0:8", ["const:bdd77c:8", "const:4:8"]]
+ 00bdd77c ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd354 bytes eff50194
+ 00bdd77c bytes e5f50194
- 00bdd35c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b0:8"]]
- 00bdd35c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd784 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
+ 00bdd784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd35c bytes 80da04f9
+ 00bdd784 bytes 80da06f9
- 00bdd330 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b0:8"]]
- 00bdd330 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd758 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
+ 00bdd758 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd330 bytes 81da44f9
+ 00bdd758 bytes 81da46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-211f840cfbe0107f24b3f50abca7f0cd"></a>

### [`00bdd38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd38c.md) → [`00bdd7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd7b4.md) _ZN8firebase4auth8userinfo10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00bdd3a8",
      "incomplete_value": false,
      "site": "00bdd3ac",
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
    "old": {
      "definition_site": "00bdd3b8",
      "incomplete_value": true,
      "site": "00bdd3c4",
      "value": [
        "LOAD",
        "8",
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
      "00bdd7d0",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bdd7e0",
      "DATA",
      [
        "storage",
        "011269f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdd7d0",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bdd7e0",
      "DATA",
      [
        "storage",
        "01126df8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd38c.md#insn-00bdd3ac) · [`00bdd3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd38c.md#insn-00bdd3a8) · [`00bdd3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd38c.md#insn-00bdd3b4)
- 新版 `00bdd7d4`（命令位置の公開資料なし） · `00bdd7d0`（命令位置の公開資料なし） · `00bdd7dc`（命令位置の公開資料なし）

~~~diff
- 00bdd3ac ["INT_ADD", "register:40f0:8", ["const:bdd3ac:8", "const:4:8"]]
- 00bdd3ac ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdd7d4 ["INT_ADD", "register:40f0:8", ["const:bdd7d4:8", "const:4:8"]]
+ 00bdd7d4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bdd3ac bytes 15f60194
+ 00bdd7d4 bytes 0bf60194
- 00bdd3a8 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bdd3a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd3a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd3a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdd7d0 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bdd7d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd7d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdd7d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdd3a8 bytes 00441191
+ 00bdd7d0 bytes 00781491
- 00bdd3b4 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00bdd3b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd3b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd3b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdd7dc ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00bdd7dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd7dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdd7dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdd3b4 bytes 08e12791
+ 00bdd7dc bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03195945a05e110dd0510ec7b8db9ded"></a>

### [`00bdd3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd3c8.md) → [`00bdd7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd7f0.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
    "old": {
      "definition_site": "00bdd3f4",
      "incomplete_value": true,
      "site": "00bdd3f4",
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
            "const:a00:8"
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
    "old": {
      "definition_site": "00bdd3dc",
      "incomplete_value": true,
      "site": "00bdd3dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd3e8",
      "incomplete_value": false,
      "site": "00bdd3ec",
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
            "const:96d:8"
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
      "00bdd800",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd810",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bdd81c",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd800",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd810",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ],
    [
      "00bdd81c",
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

- 旧版 [`00bdd3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd3c8.md#insn-00bdd3ec) · [`00bdd3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd3c8.md#insn-00bdd3f4) · [`00bdd3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd3c8.md#insn-00bdd3d8)
- 新版 `00bdd814`（命令位置の公開資料なし） · `00bdd81c`（命令位置の公開資料なし） · `00bdd800`（命令位置の公開資料なし）

~~~diff
- 00bdd3ec ["INT_ADD", "register:40f0:8", ["const:bdd3ec:8", "const:4:8"]]
- 00bdd3ec ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd814 ["INT_ADD", "register:40f0:8", ["const:bdd814:8", "const:4:8"]]
+ 00bdd814 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd3ec bytes c9f50194
+ 00bdd814 bytes bff50194
- 00bdd3f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
- 00bdd3f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd81c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdd81c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd3f4 bytes 600205f9
+ 00bdd81c bytes 600207f9
- 00bdd3d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
- 00bdd3d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd800 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdd800 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd3d8 bytes 680245f9
+ 00bdd800 bytes 680247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47fccb6af27fa3f519e5e0c3258a465e"></a>

### [`00bdd408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd408.md) → [`00bdd830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd830.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00bdd434",
      "incomplete_value": true,
      "site": "00bdd434",
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
            "const:a00:8"
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
    "old": {
      "definition_site": "00bdd41c",
      "incomplete_value": true,
      "site": "00bdd41c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd424",
      "incomplete_value": false,
      "site": "00bdd42c",
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
            "const:96d:8"
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
      "00bdd840",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd84c",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bdd85c",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd840",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd84c",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ],
    [
      "00bdd85c",
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

- 旧版 [`00bdd42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd408.md#insn-00bdd42c) · [`00bdd434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd408.md#insn-00bdd434) · [`00bdd418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd408.md#insn-00bdd418)
- 新版 `00bdd854`（命令位置の公開資料なし） · `00bdd85c`（命令位置の公開資料なし） · `00bdd840`（命令位置の公開資料なし）

~~~diff
- 00bdd42c ["INT_ADD", "register:40f0:8", ["const:bdd42c:8", "const:4:8"]]
- 00bdd42c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd854 ["INT_ADD", "register:40f0:8", ["const:bdd854:8", "const:4:8"]]
+ 00bdd854 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd42c bytes b9f50194
+ 00bdd854 bytes aff50194
- 00bdd434 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
- 00bdd434 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd85c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdd85c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd434 bytes 600205f9
+ 00bdd85c bytes 600207f9
- 00bdd418 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
- 00bdd418 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd840 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdd840 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd418 bytes 680245f9
+ 00bdd840 bytes 680247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a95bb1716268d08dd17f101119bdb66"></a>

### [`00bdd448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd448.md) → [`00bdd870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd870.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
    "old": {
      "definition_site": "00bdd478",
      "incomplete_value": true,
      "site": "00bdd478",
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
            "const:a00:8"
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
    "old": {
      "definition_site": "00bdd45c",
      "incomplete_value": true,
      "site": "00bdd45c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd468",
      "incomplete_value": false,
      "site": "00bdd470",
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
            "const:96d:8"
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
      "00bdd880",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd890",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bdd8a0",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd880",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd890",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ],
    [
      "00bdd8a0",
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

- 旧版 [`00bdd470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd448.md#insn-00bdd470) · [`00bdd478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd448.md#insn-00bdd478) · [`00bdd458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd448.md#insn-00bdd458)
- 新版 `00bdd898`（命令位置の公開資料なし） · `00bdd8a0`（命令位置の公開資料なし） · `00bdd880`（命令位置の公開資料なし）

~~~diff
- 00bdd470 ["INT_ADD", "register:40f0:8", ["const:bdd470:8", "const:4:8"]]
- 00bdd470 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd898 ["INT_ADD", "register:40f0:8", ["const:bdd898:8", "const:4:8"]]
+ 00bdd898 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd470 bytes a8f50194
+ 00bdd898 bytes 9ef50194
- 00bdd478 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
- 00bdd478 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd8a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdd8a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd478 bytes 600205f9
+ 00bdd8a0 bytes 600207f9
- 00bdd458 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
- 00bdd458 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd880 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdd880 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd458 bytes 680245f9
+ 00bdd880 bytes 680247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f797c17c53b88716a2796e257a2a460"></a>

### [`00bdd48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd48c.md) → [`00bdd8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd8b4.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdd8e4",
      "incomplete_value": true,
      "site": "00bdd8e4",
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
      "definition_site": "00bdd4bc",
      "incomplete_value": true,
      "site": "00bdd4bc",
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
            "const:a00:8"
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
    "old": {
      "definition_site": "00bdd4a0",
      "incomplete_value": true,
      "site": "00bdd4a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bdd8d0",
      "incomplete_value": false,
      "site": "00bdd8dc",
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
    "old": {
      "definition_site": "00bdd4a8",
      "incomplete_value": false,
      "site": "00bdd4b4",
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
            "const:96d:8"
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
      "00bdd8c4",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd8d0",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bdd8e4",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd8c4",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd8d0",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ],
    [
      "00bdd8e4",
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

- 旧版 [`00bdd4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd48c.md#insn-00bdd4b4) · [`00bdd4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd48c.md#insn-00bdd4bc) · [`00bdd49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd48c.md#insn-00bdd49c)
- 新版 `00bdd8dc`（命令位置の公開資料なし） · `00bdd8e4`（命令位置の公開資料なし） · `00bdd8c4`（命令位置の公開資料なし）

~~~diff
- 00bdd4b4 ["INT_ADD", "register:40f0:8", ["const:bdd4b4:8", "const:4:8"]]
- 00bdd4b4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdd8dc ["INT_ADD", "register:40f0:8", ["const:bdd8dc:8", "const:4:8"]]
+ 00bdd8dc ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd4b4 bytes 97f50194
+ 00bdd8dc bytes 8df50194
- 00bdd4bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
- 00bdd4bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdd8e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdd8e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd4bc bytes 600205f9
+ 00bdd8e4 bytes 600207f9
- 00bdd49c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a00:8"]]
- 00bdd49c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd8c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bdd8c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd49c bytes 680245f9
+ 00bdd8c4 bytes 680247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22cb3b4a2bb3f7c08dd00ced2d2e3438"></a>

### [`00bdd548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd548.md) → [`00bdd970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd970.md) _ZN8firebase4auth8metadata12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00bdd584",
      "incomplete_value": true,
      "site": "00bdd584",
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
            "const:a08:8"
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
    "old": {
      "definition_site": "00bdd5a4",
      "incomplete_value": true,
      "site": "00bdd5a4",
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
            "const:a00:8"
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
    "old": {
      "definition_site": "00bdd560",
      "incomplete_value": true,
      "site": "00bdd560",
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
      "00bdd984",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd990",
      "READ",
      [
        "storage",
        "01126a08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd9ac",
      "WRITE",
      [
        "storage",
        "01126a08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd984",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd990",
      "READ",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd9ac",
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

- 旧版 [`00bdd584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd548.md#insn-00bdd584) · [`00bdd5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd548.md#insn-00bdd5a0) · [`00bdd5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd548.md#insn-00bdd5a4)
- 新版 `00bdd9ac`（命令位置の公開資料なし） · `00bdd9c8`（命令位置の公開資料なし） · `00bdd9cc`（命令位置の公開資料なし）

~~~diff
- 00bdd584 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bdd584 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bdd584 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a08:8"]]
- 00bdd584 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bdd9ac ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bdd9ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bdd9ac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e08:8"]]
+ 00bdd9ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bdd584 bytes bf222839
+ 00bdd9ac bytes bf223839
- 00bdd5a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdd5a0 ["INT_ADD", "register:40f0:8", ["const:bdd5a0:8", "const:4:8"]]
- 00bdd5a0 ["CALLIND", null, ["register:0:8"]]
+ 00bdd9c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd9c8 ["INT_ADD", "register:40f0:8", ["const:bdd9c8:8", "const:4:8"]]
+ 00bdd9c8 ["CALLIND", null, ["register:0:8"]]
- 00bdd5a0 bytes 00013fd6
+ 00bdd9c8 bytes 00013fd6
- 00bdd5a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a00:8"]]
- 00bdd5a4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bdd5a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bdd9cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bdd9cc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bdd9cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bdd5a4 bytes 9f0205f9
+ 00bdd9cc bytes 9f0207f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4c352c937fb6d0c5f391d5b46ac4b66"></a>

### [`00bdd5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd5b8.md) → [`00bdd9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd9e0.md) _ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bdd5f8",
      "incomplete_value": true,
      "site": "00bdd5f8",
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
            "const:a00:8"
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
    "old": {
      "definition_site": "00bdd5d4",
      "incomplete_value": true,
      "site": "00bdd5d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd5dc",
      "incomplete_value": false,
      "site": "00bdd5f0",
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
            "const:96d:8"
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
      "00bdd9f4",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdda04",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bdda20",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd9f4",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdda04",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ],
    [
      "00bdda20",
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

- 旧版 [`00bdd5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd5b8.md#insn-00bdd5f0) · [`00bdd5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd5b8.md#insn-00bdd5f8) · [`00bdd5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd5b8.md#insn-00bdd5cc)
- 新版 `00bdda18`（命令位置の公開資料なし） · `00bdda20`（命令位置の公開資料なし） · `00bdd9f4`（命令位置の公開資料なし）

~~~diff
- 00bdd5f0 ["INT_ADD", "register:40f0:8", ["const:bdd5f0:8", "const:4:8"]]
- 00bdd5f0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdda18 ["INT_ADD", "register:40f0:8", ["const:bdda18:8", "const:4:8"]]
+ 00bdda18 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd5f0 bytes 48f50194
+ 00bdda18 bytes 3ef50194
- 00bdd5f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a00:8"]]
- 00bdd5f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bdda20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bdda20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd5f8 bytes 800205f9
+ 00bdda20 bytes 800207f9
- 00bdd5cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a00:8"]]
- 00bdd5cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdd9f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bdd9f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd5cc bytes 810245f9
+ 00bdd9f4 bytes 810247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b1b84a271d1c4911140710bfed32aff"></a>

### [`00bdd628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd628.md) → [`00bdda50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdda50.md) _ZN8firebase4auth8metadata11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00bdd644",
      "incomplete_value": false,
      "site": "00bdd648",
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
    "old": {
      "definition_site": "00bdd654",
      "incomplete_value": true,
      "site": "00bdd660",
      "value": [
        "LOAD",
        "8",
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
      "00bdda6c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bdda7c",
      "DATA",
      [
        "storage",
        "01126a10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdda6c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bdda7c",
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

- 旧版 [`00bdd648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd628.md#insn-00bdd648) · [`00bdd644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd628.md#insn-00bdd644) · [`00bdd650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd628.md#insn-00bdd650)
- 新版 `00bdda70`（命令位置の公開資料なし） · `00bdda6c`（命令位置の公開資料なし） · `00bdda78`（命令位置の公開資料なし）

~~~diff
- 00bdd648 ["INT_ADD", "register:40f0:8", ["const:bdd648:8", "const:4:8"]]
- 00bdd648 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdda70 ["INT_ADD", "register:40f0:8", ["const:bdda70:8", "const:4:8"]]
+ 00bdda70 ["CALL", null, ["callee:00c5b000:8"]]
- 00bdd648 bytes 6ef50194
+ 00bdda70 bytes 64f50194
- 00bdd644 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bdd644 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd644 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd644 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdda6c ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bdda6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdda6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdda6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdd644 bytes 00680a91
+ 00bdda6c bytes 009c0d91
- 00bdd650 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 00bdd650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdda78 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 00bdda78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdda78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdda78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdd650 bytes 08412891
+ 00bdda78 bytes 08413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f37491ae1bff5982d7c9c762552c8687"></a>

### [`00bdd664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd664.md) → [`00bdda8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdda8c.md) _ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bdd6a4",
      "incomplete_value": true,
      "site": "00bdd6a4",
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
            "const:a00:8"
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
    "old": {
      "definition_site": "00bdd680",
      "incomplete_value": true,
      "site": "00bdd680",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd688",
      "incomplete_value": false,
      "site": "00bdd69c",
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
            "const:96d:8"
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
      "00bddaa0",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddab0",
      "PARAM",
      [
        "storage",
        "002be96d",
        null,
        "string"
      ]
    ],
    [
      "00bddacc",
      "WRITE",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bddaa0",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddab0",
      "PARAM",
      [
        "storage",
        "002be9ad",
        null,
        "string"
      ]
    ],
    [
      "00bddacc",
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

- 旧版 [`00bdd69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd664.md#insn-00bdd69c) · [`00bdd6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd664.md#insn-00bdd6a4) · [`00bdd678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd664.md#insn-00bdd678)
- 新版 `00bddac4`（命令位置の公開資料なし） · `00bddacc`（命令位置の公開資料なし） · `00bddaa0`（命令位置の公開資料なし）

~~~diff
- 00bdd69c ["INT_ADD", "register:40f0:8", ["const:bdd69c:8", "const:4:8"]]
- 00bdd69c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bddac4 ["INT_ADD", "register:40f0:8", ["const:bddac4:8", "const:4:8"]]
+ 00bddac4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd69c bytes 1df50194
+ 00bddac4 bytes 13f50194
- 00bdd6a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a00:8"]]
- 00bdd6a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bddacc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bddacc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd6a4 bytes 800205f9
+ 00bddacc bytes 800207f9
- 00bdd678 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a00:8"]]
- 00bdd678 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bddaa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bddaa0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd678 bytes 810245f9
+ 00bddaa0 bytes 810247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3910e9decfe44d11b920ed41444a29c6"></a>

### [`00bdd6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd6d4.md) → [`00bddafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddafc.md) _ZN8firebase4auth8metadata10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00bdd6f0",
      "incomplete_value": false,
      "site": "00bdd6f4",
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
    "old": {
      "definition_site": "00bdd700",
      "incomplete_value": true,
      "site": "00bdd70c",
      "value": [
        "LOAD",
        "8",
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
      "00bddb18",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bddb28",
      "DATA",
      [
        "storage",
        "01126a20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bddb18",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bddb28",
      "DATA",
      [
        "storage",
        "01126e20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd6d4.md#insn-00bdd6f4) · [`00bdd6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd6d4.md#insn-00bdd6f0) · [`00bdd6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd6d4.md#insn-00bdd6fc)
- 新版 `00bddb1c`（命令位置の公開資料なし） · `00bddb18`（命令位置の公開資料なし） · `00bddb24`（命令位置の公開資料なし）

~~~diff
- 00bdd6f4 ["INT_ADD", "register:40f0:8", ["const:bdd6f4:8", "const:4:8"]]
- 00bdd6f4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bddb1c ["INT_ADD", "register:40f0:8", ["const:bddb1c:8", "const:4:8"]]
+ 00bddb1c ["CALL", null, ["callee:00c5b000:8"]]
- 00bdd6f4 bytes 43f50194
+ 00bddb1c bytes 39f50194
- 00bdd6f0 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bdd6f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd6f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd6f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bddb18 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bddb18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bddb18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bddb18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdd6f0 bytes 00441191
+ 00bddb18 bytes 00781491
- 00bdd6fc ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00bdd6fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd6fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd6fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bddb24 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 00bddb24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bddb24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bddb24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdd6fc bytes 08812891
+ 00bddb24 bytes 08813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35c082b2a0c0f4f0ec3c11b0a6823911"></a>

### [`00bdd750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd750.md) → [`00bddb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddb78.md) _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "site": "00bdd77c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bddba4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00bdd764",
      "incomplete_value": true,
      "site": "00bdd764",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bddb88",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdd76c",
      "PARAM",
      [
        "storage",
        "002ad448",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bdd774",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00bddb88",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddb94",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ],
    [
      "00bddb9c",
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

- 旧版 [`00bdd764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd750.md#insn-00bdd764) · [`00bdd774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd750.md#insn-00bdd774) · [`00bdd77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd750.md#insn-00bdd77c)
- 新版 `00bddb8c`（命令位置の公開資料なし）

~~~diff
- 00bdd764 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bdd764 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bddb8c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bddb8c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bdd764 bytes e80000b5
+ 00bddb8c bytes e80000b5
- 00bdd774 ["INT_ADD", "register:40f0:8", ["const:bdd774:8", "const:4:8"]]
- 00bdd774 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd774 bytes e7f40194
- 00bdd77c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
- 00bdd77c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd77c bytes 601605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-273fcca2c70e3f6882810040cc3dc0a7"></a>

### [`00bdd790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd790.md) → [`00bddbb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddbb8.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
    "old": {
      "definition_site": "00bdd7c0",
      "incomplete_value": true,
      "site": "00bdd7c0",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00bdd7a4",
      "incomplete_value": true,
      "site": "00bdd7a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd7b0",
      "incomplete_value": false,
      "site": "00bdd7b8",
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
            "const:448:8"
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
      "00bddbc8",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddbd8",
      "PARAM",
      [
        "storage",
        "002ad448",
        null,
        "string"
      ]
    ],
    [
      "00bddbe8",
      "WRITE",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bddbc8",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddbd8",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ],
    [
      "00bddbe8",
      "WRITE",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd790.md#insn-00bdd7b8) · [`00bdd7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd790.md#insn-00bdd7c0) · [`00bdd7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd790.md#insn-00bdd7a0)
- 新版 `00bddbe0`（命令位置の公開資料なし） · `00bddbe8`（命令位置の公開資料なし） · `00bddbc8`（命令位置の公開資料なし）

~~~diff
- 00bdd7b8 ["INT_ADD", "register:40f0:8", ["const:bdd7b8:8", "const:4:8"]]
- 00bdd7b8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bddbe0 ["INT_ADD", "register:40f0:8", ["const:bddbe0:8", "const:4:8"]]
+ 00bddbe0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd7b8 bytes d6f40194
+ 00bddbe0 bytes ccf40194
- 00bdd7c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
- 00bdd7c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bddbe8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
+ 00bddbe8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd7c0 bytes 601605f9
+ 00bddbe8 bytes 601607f9
- 00bdd7a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
- 00bdd7a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bddbc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
+ 00bddbc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd7a0 bytes 681645f9
+ 00bddbc8 bytes 681647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2102a80591588720a13980da81211f01"></a>

### [`00bdd7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd7d4.md) → [`00bddbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddbfc.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bdd804",
      "incomplete_value": true,
      "site": "00bdd804",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00bdd7e8",
      "incomplete_value": true,
      "site": "00bdd7e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd7f0",
      "incomplete_value": false,
      "site": "00bdd7fc",
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
            "const:448:8"
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
      "00bddc0c",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddc18",
      "PARAM",
      [
        "storage",
        "002ad448",
        null,
        "string"
      ]
    ],
    [
      "00bddc2c",
      "WRITE",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bddc0c",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddc18",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ],
    [
      "00bddc2c",
      "WRITE",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd7d4.md#insn-00bdd7fc) · [`00bdd804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd7d4.md#insn-00bdd804) · [`00bdd7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd7d4.md#insn-00bdd7e4)
- 新版 `00bddc24`（命令位置の公開資料なし） · `00bddc2c`（命令位置の公開資料なし） · `00bddc0c`（命令位置の公開資料なし）

~~~diff
- 00bdd7fc ["INT_ADD", "register:40f0:8", ["const:bdd7fc:8", "const:4:8"]]
- 00bdd7fc ["CALL", null, ["callee:00c5af10:8"]]
+ 00bddc24 ["INT_ADD", "register:40f0:8", ["const:bddc24:8", "const:4:8"]]
+ 00bddc24 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd7fc bytes c5f40194
+ 00bddc24 bytes bbf40194
- 00bdd804 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
- 00bdd804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bddc2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
+ 00bddc2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd804 bytes 601605f9
+ 00bddc2c bytes 601607f9
- 00bdd7e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
- 00bdd7e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bddc0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e28:8"]]
+ 00bddc0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd7e4 bytes 681645f9
+ 00bddc0c bytes 681647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35cacdd2bd9c57d2a468a19acf537870"></a>

### [`00bdd824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd824.md) → [`00bddc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddc4c.md) _ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00bdd87c",
      "incomplete_value": true,
      "site": "00bdd87c",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bdd858",
      "incomplete_value": true,
      "site": "00bdd864",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bddc60",
      "READ",
      [
        "storage",
        "01126a30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bddc80",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddca4",
      "WRITE",
      [
        "storage",
        "01126a30",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bddc60",
      "READ",
      [
        "storage",
        "01126e30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bddc80",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddca4",
      "WRITE",
      [
        "storage",
        "01126e30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd824.md#insn-00bdd864) · [`00bdd87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd824.md#insn-00bdd87c) · [`00bdd838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd824.md#insn-00bdd838)
- 新版 `00bddc8c`（命令位置の公開資料なし） · `00bddca4`（命令位置の公開資料なし） · `00bddc60`（命令位置の公開資料なし）

~~~diff
- 00bdd864 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdd864 ["INT_ADD", "register:40f0:8", ["const:bdd864:8", "const:4:8"]]
- 00bdd864 ["CALLIND", null, ["register:0:8"]]
+ 00bddc8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bddc8c ["INT_ADD", "register:40f0:8", ["const:bddc8c:8", "const:4:8"]]
+ 00bddc8c ["CALLIND", null, ["register:0:8"]]
- 00bdd864 bytes 00013fd6
+ 00bddc8c bytes 00013fd6
- 00bdd87c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bdd87c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a30:8"]]
- 00bdd87c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bddca4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bddca4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e30:8"]]
+ 00bddca4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bdd87c bytes a0c22839
+ 00bddca4 bytes a0c23839
- 00bdd838 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a30:8"]]
- 00bdd838 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bdd838 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bddc60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e30:8"]]
+ 00bddc60 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bddc60 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bdd838 bytes a8c26839
+ 00bddc60 bytes a8c27839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54b02a49ee2c33f1b7498c96487767bd"></a>

### [`00bdd890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd890.md) → [`00bddcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddcb8.md) _ZN8firebase4auth18userprofilebuilder12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00bdd8cc",
      "incomplete_value": true,
      "site": "00bdd8cc",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00bdd8ec",
      "incomplete_value": true,
      "site": "00bdd8ec",
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
            "const:a28:8"
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
    "old": {
      "definition_site": "00bdd8a8",
      "incomplete_value": true,
      "site": "00bdd8a8",
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
      "00bddccc",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddcd8",
      "READ",
      [
        "storage",
        "01126a30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bddcf4",
      "WRITE",
      [
        "storage",
        "01126a30",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bddccc",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddcd8",
      "READ",
      [
        "storage",
        "01126e30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bddcf4",
      "WRITE",
      [
        "storage",
        "01126e30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd890.md#insn-00bdd8cc) · [`00bdd8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd890.md#insn-00bdd8e8) · [`00bdd8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd890.md#insn-00bdd8ec)
- 新版 `00bddcf4`（命令位置の公開資料なし） · `00bddd10`（命令位置の公開資料なし） · `00bddd14`（命令位置の公開資料なし）

~~~diff
- 00bdd8cc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bdd8cc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bdd8cc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a30:8"]]
- 00bdd8cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bddcf4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bddcf4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bddcf4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e30:8"]]
+ 00bddcf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bdd8cc bytes bfc22839
+ 00bddcf4 bytes bfc23839
- 00bdd8e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdd8e8 ["INT_ADD", "register:40f0:8", ["const:bdd8e8:8", "const:4:8"]]
- 00bdd8e8 ["CALLIND", null, ["register:0:8"]]
+ 00bddd10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bddd10 ["INT_ADD", "register:40f0:8", ["const:bddd10:8", "const:4:8"]]
+ 00bddd10 ["CALLIND", null, ["register:0:8"]]
- 00bdd8e8 bytes 00013fd6
+ 00bddd10 bytes 00013fd6
- 00bdd8ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a28:8"]]
- 00bdd8ec ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bdd8ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bddd14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e28:8"]]
+ 00bddd14 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bddd14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bdd8ec bytes 9f1605f9
+ 00bddd14 bytes 9f1607f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0567c8622206c1ac61857e9c9c6bd3eb"></a>

### [`00bdd900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd900.md) → [`00bddd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddd28.md) _ZN8firebase4auth18userprofilebuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00bdd940",
      "incomplete_value": true,
      "site": "00bdd940",
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
            "const:a28:8"
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
    "old": {
      "definition_site": "00bdd91c",
      "incomplete_value": true,
      "site": "00bdd91c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00bdd924",
      "incomplete_value": false,
      "site": "00bdd938",
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
            "const:448:8"
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
      "00bddd3c",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddd4c",
      "PARAM",
      [
        "storage",
        "002ad448",
        null,
        "string"
      ]
    ],
    [
      "00bddd68",
      "WRITE",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bddd3c",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddd4c",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ],
    [
      "00bddd68",
      "WRITE",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd900.md#insn-00bdd938) · [`00bdd940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd900.md#insn-00bdd940) · [`00bdd914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd900.md#insn-00bdd914)
- 新版 `00bddd60`（命令位置の公開資料なし） · `00bddd68`（命令位置の公開資料なし） · `00bddd3c`（命令位置の公開資料なし）

~~~diff
- 00bdd938 ["INT_ADD", "register:40f0:8", ["const:bdd938:8", "const:4:8"]]
- 00bdd938 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bddd60 ["INT_ADD", "register:40f0:8", ["const:bddd60:8", "const:4:8"]]
+ 00bddd60 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd938 bytes 76f40194
+ 00bddd60 bytes 6cf40194
- 00bdd940 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a28:8"]]
- 00bdd940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bddd68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e28:8"]]
+ 00bddd68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd940 bytes 801605f9
+ 00bddd68 bytes 801607f9
- 00bdd914 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a28:8"]]
- 00bdd914 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bddd3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e28:8"]]
+ 00bddd3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd914 bytes 811645f9
+ 00bddd3c bytes 811647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a21048a45c5003ed0f7bbd84b5eb5307"></a>

### [`00bdd970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd970.md) → [`00bddd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddd98.md) _ZN8firebase4auth18userprofilebuilder11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00bdd98c",
      "incomplete_value": false,
      "site": "00bdd990",
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
    "old": {
      "definition_site": "00bdd99c",
      "incomplete_value": true,
      "site": "00bdd9a8",
      "value": [
        "LOAD",
        "8",
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
      "00bdddb4",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bdddc4",
      "DATA",
      [
        "storage",
        "01126a38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdddb4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bdddc4",
      "DATA",
      [
        "storage",
        "01126e38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd970.md#insn-00bdd990) · [`00bdd98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd970.md#insn-00bdd98c) · [`00bdd998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd970.md#insn-00bdd998)
- 新版 `00bdddb8`（命令位置の公開資料なし） · `00bdddb4`（命令位置の公開資料なし） · `00bdddc0`（命令位置の公開資料なし）

~~~diff
- 00bdd990 ["INT_ADD", "register:40f0:8", ["const:bdd990:8", "const:4:8"]]
- 00bdd990 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdddb8 ["INT_ADD", "register:40f0:8", ["const:bdddb8:8", "const:4:8"]]
+ 00bdddb8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bdd990 bytes 9cf40194
+ 00bdddb8 bytes 92f40194
- 00bdd98c ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bdd98c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd98c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdd98c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdddb4 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bdddb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdddb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdddb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdd98c bytes 00680a91
+ 00bdddb4 bytes 009c0d91
- 00bdd998 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 00bdd998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdd998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdddc0 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 00bdddc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdddc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdddc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdd998 bytes 08e12891
+ 00bdddc0 bytes 08e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10f86b6bdaf455e240684731e466ca0b"></a>

### [`00bdd9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd9ac.md) → [`00bdddd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdddd4.md) _ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00bdd9ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdde14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdd9c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd9c0",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdd9c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdde18"
      ]
    ],
    [
      "unmatched:00bdd9d0",
      "PARAM",
      [
        "storage",
        "002ad448",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bddde8",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdddf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdde18"
      ]
    ],
    [
      "00bdddf8",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd9ac.md#insn-00bdd9c8) · [`00bdd9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd9ac.md#insn-00bdd9e4) · [`00bdd9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd9ac.md#insn-00bdd9ec)
- 新版 `00bdde0c`（命令位置の公開資料なし）

~~~diff
- 00bdd9c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bdd9c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bdd9c8 bytes 410100b5
- 00bdd9e4 ["INT_ADD", "register:40f0:8", ["const:bdd9e4:8", "const:4:8"]]
- 00bdd9e4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bdde0c ["INT_ADD", "register:40f0:8", ["const:bdde0c:8", "const:4:8"]]
+ 00bdde0c ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd9e4 bytes 4bf40194
+ 00bdde0c bytes 41f40194
- 00bdd9ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a28:8"]]
- 00bdd9ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd9ec bytes 801605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4acc31fe3d71d7a569afa22748957778"></a>

### [`00bdda1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdda1c.md) → [`00bdde44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde44.md) _ZN8firebase4auth18userprofilebuilder10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00bdda38",
      "incomplete_value": false,
      "site": "00bdda3c",
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
    "old": {
      "definition_site": "00bdda48",
      "incomplete_value": true,
      "site": "00bdda54",
      "value": [
        "LOAD",
        "8",
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
      "00bdde60",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bdde70",
      "DATA",
      [
        "storage",
        "01126a58",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdde60",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bdde70",
      "DATA",
      [
        "storage",
        "01126e58",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdda1c.md#insn-00bdda3c) · [`00bdda38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdda1c.md#insn-00bdda38) · [`00bdda44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdda1c.md#insn-00bdda44)
- 新版 `00bdde64`（命令位置の公開資料なし） · `00bdde60`（命令位置の公開資料なし） · `00bdde6c`（命令位置の公開資料なし）

~~~diff
- 00bdda3c ["INT_ADD", "register:40f0:8", ["const:bdda3c:8", "const:4:8"]]
- 00bdda3c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdde64 ["INT_ADD", "register:40f0:8", ["const:bdde64:8", "const:4:8"]]
+ 00bdde64 ["CALL", null, ["callee:00c5b000:8"]]
- 00bdda3c bytes 71f40194
+ 00bdde64 bytes 67f40194
- 00bdda38 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bdda38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bdda38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bdda38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bdde60 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bdde60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdde60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bdde60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bdda38 bytes 00441191
+ 00bdde60 bytes 00781491
- 00bdda44 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00bdda44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bdda44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bdda44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bdde6c ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00bdde6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdde6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bdde6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bdda44 bytes 08612991
+ 00bdde6c bytes 08613991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26a8503ea05c5293975919dc3b5ceae2"></a>

### [`00bdda58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdda58.md) → [`00bdde80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde80.md) _ZN8firebase4auth18CacheUserMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d850.md) · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 1件 [`00c5dc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc50.md) · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 29.27% / 新版 29.27%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdda9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bddaf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bddb4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdda70",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdda78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bddaa0"
      ]
    ],
    [
      "unmatched:00bdda80",
      "PARAM",
      [
        "storage",
        "002bc210",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdde98",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bddec8"
      ]
    ],
    [
      "00bddea8",
      "PARAM",
      [
        "storage",
        "002bc250",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdda78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdda58.md#insn-00bdda78) · [`00bdda94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdda58.md#insn-00bdda94) · [`00bdda9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdda58.md#insn-00bdda9c)

~~~diff
- 00bdda78 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bdda78 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bdda78 bytes 410100b5
- 00bdda94 ["INT_ADD", "register:40f0:8", ["const:bdda94:8", "const:4:8"]]
- 00bdda94 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdda94 bytes 1ff40194
- 00bdda9c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:900:8"]]
- 00bdda9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdda9c bytes a08204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a9da0a69be86516240b90fa3b370ab7"></a>

### [`00bddc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bddc44.md) → [`00bde06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde06c.md) _ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d870.md) · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5dc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc70.md) · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.58% / 新版 85.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 10件

アドレスに依存する影響 `branch_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bde0a8",
      "incomplete_value": true,
      "site": "00bde0a8",
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
    "old": {
      "definition_site": "00bddc80",
      "incomplete_value": true,
      "site": "00bddc80",
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
            "const:908:8"
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
      "definition_site": "00bde0c8",
      "incomplete_value": true,
      "site": "00bde0c8",
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
    "old": {
      "definition_site": "00bddca0",
      "incomplete_value": true,
      "site": "00bddca0",
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
            "const:900:8"
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
      "definition_site": "00bde0f4",
      "incomplete_value": true,
      "site": "00bde0f4",
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
    "old": {
      "definition_site": "00bddccc",
      "incomplete_value": true,
      "site": "00bddccc",
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
            "const:928:8"
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
      "00bde080",
      "READ",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ],
    [
      "00bde090",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined1"
      ]
    ],
    [
      "00bde0a8",
      "WRITE",
      [
        "storage",
        "01126908",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bde080",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bde090",
      "READ",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bde0a8",
      "WRITE",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bddc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bddc44.md#insn-00bddc80) · [`00bddc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bddc44.md#insn-00bddc9c) · [`00bddca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bddc44.md#insn-00bddca0)
- 新版 `00bde0a8`（命令位置の公開資料なし） · `00bde0c4`（命令位置の公開資料なし） · `00bde0c8`（命令位置の公開資料なし）

~~~diff
- 00bddc80 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bddc80 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bddc80 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:908:8"]]
- 00bddc80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bde0a8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bde0a8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bde0a8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d08:8"]]
+ 00bde0a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bddc80 bytes bf222439
+ 00bde0a8 bytes bf223439
- 00bddc9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bddc9c ["INT_ADD", "register:40f0:8", ["const:bddc9c:8", "const:4:8"]]
- 00bddc9c ["CALLIND", null, ["register:0:8"]]
+ 00bde0c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bde0c4 ["INT_ADD", "register:40f0:8", ["const:bde0c4:8", "const:4:8"]]
+ 00bde0c4 ["CALLIND", null, ["register:0:8"]]
- 00bddc9c bytes 00013fd6
+ 00bde0c4 bytes 00013fd6
- 00bddca0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:900:8"]]
- 00bddca0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bddca0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bde0c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
+ 00bde0c8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bde0c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bddca0 bytes 9f8204f9
+ 00bde0c8 bytes 9f8206f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d18b97cd4c72c5856147261cbcb747b6"></a>

### [`00bde27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde27c.md) → [`00bde6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde6a4.md) _ZN8firebase4auth15ReadTokenResultEP8_jobjectPNS0_18FutureCallbackDataINSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde3f0.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00bde818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde818.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

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
    "old": {
      "definition_site": "00bde300",
      "incomplete_value": false,
      "site": "00bde304",
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
            "const:eaf:8"
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
    "old": {
      "definition_site": "00bde30c",
      "incomplete_value": true,
      "site": "00bde318",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
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
      "00bde728",
      "PARAM",
      [
        "storage",
        "002b6eaf",
        null,
        "string"
      ]
    ],
    [
      "00bde734",
      "READ",
      [
        "storage",
        "01126910",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bde728",
      "PARAM",
      [
        "storage",
        "002b6eef",
        null,
        "string"
      ]
    ],
    [
      "00bde734",
      "READ",
      [
        "storage",
        "01126d10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde27c.md#insn-00bde304) · [`00bde318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde27c.md#insn-00bde318) · [`00bde2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde27c.md#insn-00bde2c0)
- 新版 `00bde72c`（命令位置の公開資料なし） · `00bde740`（命令位置の公開資料なし） · `00bde6e8`（命令位置の公開資料なし）

~~~diff
- 00bde304 ["INT_ADD", "register:40f0:8", ["const:bde304:8", "const:4:8"]]
- 00bde304 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bde72c ["INT_ADD", "register:40f0:8", ["const:bde72c:8", "const:4:8"]]
+ 00bde72c ["CALL", null, ["callee:00c5b000:8"]]
- 00bde304 bytes 3ff20194
+ 00bde72c bytes 35f20194
- 00bde318 ["INT_ADD", "register:40f0:8", ["const:bde318:8", "const:4:8"]]
- 00bde318 ["CALL", null, ["callee:00497834:8"]]
+ 00bde740 ["INT_ADD", "register:40f0:8", ["const:bde740:8", "const:4:8"]]
+ 00bde740 ["CALL", null, ["callee:00497834:8"]]
- 00bde318 bytes 37e5e297
+ 00bde740 bytes 3de4e297
- 00bde2c0 ["INT_ADD", "register:40f0:8", ["const:bde2c0:8", "const:4:8"]]
- 00bde2c0 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bde6e8 ["INT_ADD", "register:40f0:8", ["const:bde6e8:8", "const:4:8"]]
+ 00bde6e8 ["CALL", null, ["callee:00c5b080:8"]]
- 00bde2c0 bytes 70f20194
+ 00bde6e8 bytes 66f20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac67ab9dccc68c670e3a1753917b701d"></a>

### [`00bde754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde754.md) → [`00bdeb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bdeb7c.md) _ZNK8firebase4auth4User13provider_dataEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6b0.md) · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5aab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aab0.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.33% / 新版 66.33%

CFGの説明率　旧版 13.19% / 新版 11.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_condition` 2件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 15件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 37件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bde754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bde754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bde758"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde754",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bde758",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bde75c",
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
      "00bdeb7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bdeb80",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bdeb84",
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

- 旧版 [`00bde754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde754.md#insn-00bde754) · [`00bde758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde754.md#insn-00bde758) · [`00bde75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde754.md#insn-00bde75c)

~~~diff
- 00bde754 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bde754 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bde754 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00bde754 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bde754 bytes fc6fbaa9
- 00bde758 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bde758 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bde758 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bde758 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bde758 bytes fa6701a9
- 00bde75c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bde75c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bde75c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bde75c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bde75c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e649ea4d648271986cf16ba84ba0df37"></a>

### [`00bdee60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bdee60.md) → [`00bdf288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf288.md) _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE7reserveEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5dad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dad0.md) · 呼出先 4件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5daa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5daa0.md)
- 新版 呼出元 1件 [`00c5ded0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5ded0.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5dea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dea0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.43% / 新版 81.43%

CFGの説明率　旧版 81.25% / 新版 72.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdee60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdee64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdee64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdee60",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdee64",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdee68",
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
      "00bdf288",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bdf28c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bdf290",
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

- 旧版 [`00bdee60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bdee60.md#insn-00bdee60) · [`00bdee64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bdee60.md#insn-00bdee64) · [`00bdee68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bdee60.md#insn-00bdee68)

~~~diff
- 00bdee60 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00bdee60 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00bdee60 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bdee60 bytes f90f1bf8
- 00bdee64 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bdee64 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bdee64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bdee64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdee64 bytes f85f01a9
- 00bdee68 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bdee68 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bdee68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bdee68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdee68 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b264ef7d15a96ecdfa96f351d3cb5a7f"></a>

### [`00bdefac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bdefac.md) → [`00bdf3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf3d4.md) _ZNK8firebase4auth22AndroidWrappedUserInfo3uidEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdf400",
      "incomplete_value": true,
      "site": "00bdf40c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdefd8",
      "incomplete_value": true,
      "site": "00bdefe4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9c0:8"
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
      "00bdf400",
      "READ",
      [
        "storage",
        "011269c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf400",
      "READ",
      [
        "storage",
        "01126dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdefe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bdefac.md#insn-00bdefe4) · [`00bdefc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bdefac.md#insn-00bdefc8) · [`00bdefd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bdefac.md#insn-00bdefd8)
- 新版 `00bdf40c`（命令位置の公開資料なし） · `00bdf3f0`（命令位置の公開資料なし） · `00bdf400`（命令位置の公開資料なし）

~~~diff
- 00bdefe4 ["INT_ADD", "register:40f0:8", ["const:bdefe4:8", "const:4:8"]]
- 00bdefe4 ["CALL", null, ["callee:00497834:8"]]
+ 00bdf40c ["INT_ADD", "register:40f0:8", ["const:bdf40c:8", "const:4:8"]]
+ 00bdf40c ["CALL", null, ["callee:00497834:8"]]
- 00bdefe4 bytes 04e2e297
+ 00bdf40c bytes 0ae1e297
- 00bdefc8 ["INT_ADD", "register:40f0:8", ["const:bdefc8:8", "const:4:8"]]
- 00bdefc8 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bdf3f0 ["INT_ADD", "register:40f0:8", ["const:bdf3f0:8", "const:4:8"]]
+ 00bdf3f0 ["CALL", null, ["callee:00c5b080:8"]]
- 00bdefc8 bytes 2eef0194
+ 00bdf3f0 bytes 24ef0194
- 00bdefd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9c0:8"]]
- 00bdefd8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdf400 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00bdf400 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdefd8 bytes 02e144f9
+ 00bdf400 bytes 02e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-242560924349cbb1326cb73bb7084275"></a>

### [`00bdf030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf030.md) → [`00bdf458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf458.md) _ZNK8firebase4auth22AndroidWrappedUserInfo5emailEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 37.50% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf030"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf034"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf030",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdf034",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdf038",
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
      "00bdf458",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bdf45c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bdf460",
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

- 旧版 [`00bdf030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf030.md#insn-00bdf030) · [`00bdf034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf030.md#insn-00bdf034) · [`00bdf038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf030.md#insn-00bdf038)

~~~diff
- 00bdf030 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bdf030 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bdf030 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bdf030 bytes f50f1df8
- 00bdf034 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bdf034 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bdf034 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bdf034 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdf034 bytes f44f01a9
- 00bdf038 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bdf038 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bdf038 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bdf038 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdf038 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6250dc506d099154ee6c20927eec39b"></a>

### [`00bdf0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf0b4.md) → [`00bdf4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf4dc.md) _ZNK8firebase4auth22AndroidWrappedUserInfo12display_nameEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 10.00% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf0b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf0b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf0b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf0b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdf0b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdf0bc",
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
      "00bdf4dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bdf4e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bdf4e4",
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

- 旧版 [`00bdf0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf0b4.md#insn-00bdf0b4) · [`00bdf0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf0b4.md#insn-00bdf0b8) · [`00bdf0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf0b4.md#insn-00bdf0bc)

~~~diff
- 00bdf0b4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bdf0b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bdf0b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bdf0b4 bytes f50f1df8
- 00bdf0b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bdf0b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bdf0b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bdf0b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdf0b8 bytes f44f01a9
- 00bdf0bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bdf0bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bdf0bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bdf0bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdf0bc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4675b770192548ab460b8987fa4b1a79"></a>

### [`00bdf1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf1bc.md) → [`00bdf5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf5e4.md) _ZNK8firebase4auth22AndroidWrappedUserInfo11provider_idEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 57.14% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bdf1d4",
      "incomplete_value": true,
      "site": "00bdf1d8",
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
    "old": {
      "definition_site": "00bdf1e8",
      "incomplete_value": true,
      "site": "00bdf1f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00bdf610",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf610",
      "READ",
      [
        "storage",
        "01126dc8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf1bc.md#insn-00bdf1d8) · [`00bdf1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf1bc.md#insn-00bdf1f4) · [`00bdf1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf1bc.md#insn-00bdf1d4)
- 新版 `00bdf600`（命令位置の公開資料なし） · `00bdf61c`（命令位置の公開資料なし）

~~~diff
- 00bdf1d8 ["INT_ADD", "register:40f0:8", ["const:bdf1d8:8", "const:4:8"]]
- 00bdf1d8 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bdf600 ["INT_ADD", "register:40f0:8", ["const:bdf600:8", "const:4:8"]]
+ 00bdf600 ["CALL", null, ["callee:00c5b080:8"]]
- 00bdf1d8 bytes aaee0194
+ 00bdf600 bytes a0ee0194
- 00bdf1f4 ["INT_ADD", "register:40f0:8", ["const:bdf1f4:8", "const:4:8"]]
- 00bdf1f4 ["CALL", null, ["callee:00497834:8"]]
+ 00bdf61c ["INT_ADD", "register:40f0:8", ["const:bdf61c:8", "const:4:8"]]
+ 00bdf61c ["CALL", null, ["callee:00497834:8"]]
- 00bdf1f4 bytes 80e1e297
+ 00bdf61c bytes 86e0e297
- 00bdf1d4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bdf1d4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf1d4 bytes 200140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a340774bf73d19d0cd32088191281158"></a>

### [`00bdf240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf240.md) → [`00bdf668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf668.md) _ZNK8firebase4auth22AndroidWrappedUserInfo12phone_numberEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 42.86% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bdf26c",
      "incomplete_value": true,
      "site": "00bdf278",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d8:8"
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
      "definition_site": "00bdf280",
      "incomplete_value": true,
      "site": "00bdf284",
      "value": [
        "live",
        "register:40a0:8"
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
      "00bdf694",
      "READ",
      [
        "storage",
        "011269d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf694",
      "READ",
      [
        "storage",
        "01126dd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf240.md#insn-00bdf278) · [`00bdf284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf240.md#insn-00bdf284) · [`00bdf25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf240.md#insn-00bdf25c)
- 新版 `00bdf6a0`（命令位置の公開資料なし） · `00bdf6ac`（命令位置の公開資料なし） · `00bdf684`（命令位置の公開資料なし）

~~~diff
- 00bdf278 ["INT_ADD", "register:40f0:8", ["const:bdf278:8", "const:4:8"]]
- 00bdf278 ["CALL", null, ["callee:00497834:8"]]
+ 00bdf6a0 ["INT_ADD", "register:40f0:8", ["const:bdf6a0:8", "const:4:8"]]
+ 00bdf6a0 ["CALL", null, ["callee:00497834:8"]]
- 00bdf278 bytes 5fe1e297
+ 00bdf6a0 bytes 65e0e297
- 00bdf284 ["INT_ADD", "register:40f0:8", ["const:bdf284:8", "const:4:8"]]
- 00bdf284 ["CALL", null, ["callee:00c5af60:8"]]
+ 00bdf6ac ["INT_ADD", "register:40f0:8", ["const:bdf6ac:8", "const:4:8"]]
+ 00bdf6ac ["CALL", null, ["callee:00c5af60:8"]]
- 00bdf284 bytes 37ee0194
+ 00bdf6ac bytes 2dee0194
- 00bdf25c ["INT_ADD", "register:40f0:8", ["const:bdf25c:8", "const:4:8"]]
- 00bdf25c ["CALL", null, ["callee:00c5b080:8"]]
+ 00bdf684 ["INT_ADD", "register:40f0:8", ["const:bdf684:8", "const:4:8"]]
+ 00bdf684 ["CALL", null, ["callee:00c5b080:8"]]
- 00bdf25c bytes 89ee0194
+ 00bdf684 bytes 7fee0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcc5ddfdf3dd8b819a0fd3fbb6c016a5"></a>

### [`00bdf2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf2c4.md) → [`00bdf6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf6ec.md) _ZN8firebase4auth22AndroidWrappedUserInfoD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d780.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5db80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bdf708",
      "incomplete_value": true,
      "site": "00bdf70c",
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
      "definition_site": "00bdf2e0",
      "incomplete_value": true,
      "site": "00bdf2e4",
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
      "00bdf700",
      "READ",
      [
        "storage",
        "00c9b660",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf70c",
      "DATA",
      [
        "storage",
        "00c92510",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00bdf700",
      "READ",
      [
        "storage",
        "00c9ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf70c",
      "DATA",
      [
        "storage",
        "00c92910",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf2c4.md#insn-00bdf2d8) · [`00bdf2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf2c4.md#insn-00bdf2ec) · [`00bdf2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf2c4.md#insn-00bdf2fc)
- 新版 `00bdf700`（命令位置の公開資料なし） · `00bdf714`（命令位置の公開資料なし） · `00bdf724`（命令位置の公開資料なし）

~~~diff
- 00bdf2d8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:660:8"]]
- 00bdf2d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdf700 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a60:8"]]
+ 00bdf700 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf2d8 bytes 293143f9
+ 00bdf700 bytes 293145f9
- 00bdf2ec ["INT_ADD", "register:40f0:8", ["const:bdf2ec:8", "const:4:8"]]
- 00bdf2ec ["CALL", null, ["callee:00c5b080:8"]]
+ 00bdf714 ["INT_ADD", "register:40f0:8", ["const:bdf714:8", "const:4:8"]]
+ 00bdf714 ["CALL", null, ["callee:00c5b080:8"]]
- 00bdf2ec bytes 65ee0194
+ 00bdf714 bytes 5bee0194
- 00bdf2fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdf2fc ["INT_ADD", "register:40f0:8", ["const:bdf2fc:8", "const:4:8"]]
- 00bdf2fc ["CALLIND", null, ["register:0:8"]]
+ 00bdf724 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdf724 ["INT_ADD", "register:40f0:8", ["const:bdf724:8", "const:4:8"]]
+ 00bdf724 ["CALLIND", null, ["register:0:8"]]
- 00bdf2fc bytes 00013fd6
+ 00bdf724 bytes 00013fd6
~~~


<a id="compare-631877a4bcb2905f732d081c56b863fd"></a>

### [`00bdf328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf328.md) → [`00bdf750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf750.md) _ZN8firebase4auth4User14UpdatePasswordEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bd0098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 93.04% / 新版 93.04%

CFGの説明率　旧版 30.00% / 新版 31.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdf7a0",
      "incomplete_value": true,
      "site": "00bdf7ac",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdf79c",
      "incomplete_value": false,
      "site": "00bdf7ac",
      "value": [
        "leaf",
        "const:b:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdf7a4",
      "incomplete_value": false,
      "site": "00bdf7ac",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "old": null,
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
      "00bdf7ec",
      "READ",
      [
        "storage",
        "01126950",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdf47c",
      "READ",
      [
        "storage",
        "00c9b618",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf47c",
      "PARAM",
      [
        "storage",
        "00bd0098",
        "_ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bdf7ec",
      "READ",
      [
        "storage",
        "01126d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdf8a4",
      "READ",
      [
        "storage",
        "00c9ba18",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf8a4",
      "PARAM",
      [
        "storage",
        "00bd04c0",
        "_ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf328.md#insn-00bdf384) · [`00bdf3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf328.md#insn-00bdf3b8) · [`00bdf3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf328.md#insn-00bdf3d8)
- 新版 `00bdf7ac`（命令位置の公開資料なし） · `00bdf800`（命令位置の公開資料なし）

~~~diff
- 00bdf384 ["INT_ADD", "register:40f0:8", ["const:bdf384:8", "const:4:8"]]
- 00bdf384 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00bdf7ac ["INT_ADD", "register:40f0:8", ["const:bdf7ac:8", "const:4:8"]]
+ 00bdf7ac ["CALL", null, ["callee:00c5ae40:8"]]
- 00bdf384 bytes afed0194
+ 00bdf7ac bytes a5ed0194
- 00bdf3b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdf3b8 ["INT_ADD", "register:40f0:8", ["const:bdf3b8:8", "const:4:8"]]
- 00bdf3b8 ["CALLIND", null, ["register:0:8"]]
- 00bdf3b8 bytes 00013fd6
- 00bdf3d8 ["INT_ADD", "register:40f0:8", ["const:bdf3d8:8", "const:4:8"]]
- 00bdf3d8 ["CALL", null, ["callee:00497834:8"]]
+ 00bdf800 ["INT_ADD", "register:40f0:8", ["const:bdf800:8", "const:4:8"]]
+ 00bdf800 ["CALL", null, ["callee:00497834:8"]]
- 00bdf3d8 bytes 07e1e297
+ 00bdf800 bytes 0de0e297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d410b2520c36f8cbb3987a5b7b9a2f1"></a>

### [`00bdf550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf550.md) → [`00bdf978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf978.md) _ZN8firebase4auth4User17UpdateUserProfileERKNS1_11UserProfileE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00bd0098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00bd04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 33.96% / 新版 31.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_call_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bdf5a4",
      "incomplete_value": true,
      "site": "00bdf5b0",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bdf5a0",
      "incomplete_value": false,
      "site": "00bdf5b0",
      "value": [
        "leaf",
        "const:11:8"
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
      "definition_site": "00bdf5a8",
      "incomplete_value": false,
      "site": "00bdf5b0",
      "value": [
        "leaf",
        "const:0:8"
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
      "unmatched:00bdf5dc",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdf5e0",
      "READ",
      [
        "storage",
        "01126a38",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdfa3c",
      "READ",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdfa04",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdfa08",
      "READ",
      [
        "storage",
        "01126e38",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdfa3c",
      "READ",
      [
        "storage",
        "01126e40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf550.md#insn-00bdf5b0) · [`00bdf5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf550.md#insn-00bdf5f0) · [`00bdf628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf550.md#insn-00bdf628)
- 新版 `00bdf9d8`（命令位置の公開資料なし） · `00bdfa18`（命令位置の公開資料なし） · `00bdfa50`（命令位置の公開資料なし）

~~~diff
- 00bdf5b0 ["INT_ADD", "register:40f0:8", ["const:bdf5b0:8", "const:4:8"]]
- 00bdf5b0 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00bdf9d8 ["INT_ADD", "register:40f0:8", ["const:bdf9d8:8", "const:4:8"]]
+ 00bdf9d8 ["CALL", null, ["callee:00c5ae40:8"]]
- 00bdf5b0 bytes 24ed0194
+ 00bdf9d8 bytes 1aed0194
- 00bdf5f0 ["INT_ADD", "register:40f0:8", ["const:bdf5f0:8", "const:4:8"]]
- 00bdf5f0 ["CALL", null, ["callee:005896f4:8"]]
+ 00bdfa18 ["INT_ADD", "register:40f0:8", ["const:bdfa18:8", "const:4:8"]]
+ 00bdfa18 ["CALL", null, ["callee:005896f4:8"]]
- 00bdf5f0 bytes 31a8e697
+ 00bdfa18 bytes 37a7e697
- 00bdf628 ["INT_ADD", "register:40f0:8", ["const:bdf628:8", "const:4:8"]]
- 00bdf628 ["CALL", null, ["callee:00497834:8"]]
+ 00bdfa50 ["INT_ADD", "register:40f0:8", ["const:bdfa50:8", "const:4:8"]]
+ 00bdfa50 ["CALL", null, ["callee:00497834:8"]]
- 00bdf628 bytes 73e0e297
+ 00bdfa50 bytes 79dfe297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c0a0a307a88f1dbffe957ca95ef7eac"></a>

### [`00bdf978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf978.md) → [`00bdfda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfda0.md) _ZN8firebase4auth4User18LinkWithCredentialERKNS0_10CredentialE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.87% / 新版 86.87%

CFGの説明率　旧版 5.00% / 新版 3.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf97c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf97c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf980"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf97c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdf980",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdf984",
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
      "00bdfda4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bdfda8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bdfdac",
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

- 旧版 [`00bdf97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf978.md#insn-00bdf97c) · [`00bdf980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf978.md#insn-00bdf980) · [`00bdf984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf978.md#insn-00bdf984)

~~~diff
- 00bdf97c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bdf97c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bdf97c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bdf97c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdf97c bytes fa6703a9
- 00bdf980 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bdf980 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bdf980 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bdf980 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdf980 bytes f85f04a9
- 00bdf984 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bdf984 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bdf984 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bdf984 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdf984 bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d467bcfe83c87a194473993c37794b7b"></a>

### [`00bdfb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfb50.md) → [`00bdff78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdff78.md) _ZNK8firebase4auth4User16LinkWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00bdfb8c",
      "incomplete_value": false,
      "site": "00bdfb90",
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
            "const:b82:8"
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
      "00bdff88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bdfb88"
      ]
    ],
    [
      "unmatched:00bdfb8c",
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
      "00bdff88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdffb0"
      ]
    ],
    [
      "00bdffb4",
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

- 旧版 [`00bdfb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfb50.md#insn-00bdfb90) · [`00bdfb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfb50.md#insn-00bdfb84) · [`00bdfb88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfb50.md#insn-00bdfb88)
- 新版 `00bdffb8`（命令位置の公開資料なし）

~~~diff
- 00bdfb90 ["INT_ADD", "register:40f0:8", ["const:bdfb90:8", "const:4:8"]]
- 00bdfb90 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bdffb8 ["INT_ADD", "register:40f0:8", ["const:bdffb8:8", "const:4:8"]]
+ 00bdffb8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bdfb90 bytes 1cec0194
+ 00bdffb8 bytes 12ec0194
- 00bdfb84 ["COPY", "register:0:8", ["register:4010:8"]]
- 00bdfb84 ["BRANCHIND", null, ["register:0:8"]]
- 00bdfb84 bytes 40001fd6
- 00bdfb88 ["COPY", "register:4000:8", ["const:2b5000:8"]]
- 00bdfb88 bytes a0b6ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5081d77257dae35f12dbba92d775797a"></a>

### [`00bdfbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfbd4.md) → [`00bdfffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfffc.md) _ZN8firebase4auth4User6UnlinkEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bcfd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfd44.md) [`00bd482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd482c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.82% / 新版 91.82%

CFGの説明率　旧版 15.79% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdfbd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdfbd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdfbfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfbd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdfbfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdfc54",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00be0000",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00be0024",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00be007c",
      "READ",
      [
        "storage",
        "01126d68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfbd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfbd4.md#insn-00bdfbd8) · [`00bdfbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfbd4.md#insn-00bdfbfc) · [`00bdfc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfbd4.md#insn-00bdfc28)
- 新版 `00be0050`（命令位置の公開資料なし）

~~~diff
- 00bdfbd8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bdfbd8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bdfbd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bdfbd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdfbd8 bytes fa6703a9
- 00bdfbfc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00bdfbfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bdfbfc bytes e91700f9
- 00bdfc28 ["INT_ADD", "register:40f0:8", ["const:bdfc28:8", "const:4:8"]]
- 00bdfc28 ["CALL", null, ["callee:00c5dc00:8"]]
+ 00be0050 ["INT_ADD", "register:40f0:8", ["const:be0050:8", "const:4:8"]]
+ 00be0050 ["CALL", null, ["callee:00c5dc00:8"]]
- 00bdfc28 bytes f6f60194
+ 00be0050 bytes ecf60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf8457bfe448bae331e2f6f60d62c558"></a>

### [`00bdfddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfddc.md) → [`00be0204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0204.md) _ZN8firebase4auth4User27UpdatePhoneNumberCredentialERKNS0_19PhoneAuthCredentialE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcfce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfce4.md) [`00bd4814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4814.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd010c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd010c.md) [`00bd4c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4c3c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.62% / 新版 88.62%

CFGの説明率　旧版 3.85% / 新版 3.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdfdf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdfdf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdfe04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfdf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdfe04",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdfe74",
      "READ",
      [
        "storage",
        "01126970",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00be0218",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00be022c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00be029c",
      "READ",
      [
        "storage",
        "01126d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfddc.md#insn-00bdfdf0) · [`00bdfe04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfddc.md#insn-00bdfe04) · [`00bdfe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfddc.md#insn-00bdfe84)
- 新版 `00be02ac`（命令位置の公開資料なし）

~~~diff
- 00bdfdf0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bdfdf0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bdfdf0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00bdfdf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdfdf0 bytes fd7b08a9
- 00bdfe04 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00bdfe04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bdfe04 bytes e91f00f9
- 00bdfe84 ["INT_ADD", "register:40f0:8", ["const:bdfe84:8", "const:4:8"]]
- 00bdfe84 ["CALL", null, ["callee:00497834:8"]]
+ 00be02ac ["INT_ADD", "register:40f0:8", ["const:be02ac:8", "const:4:8"]]
+ 00be02ac ["CALL", null, ["callee:00497834:8"]]
- 00bdfe84 bytes 5cdee297
+ 00be02ac bytes 62dde297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-518745ed52b6725b38b5de355e8a310f"></a>

### [`00be0028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0028.md) → [`00be0450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0450.md) _ZN8firebase4auth4User6ReloadEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bd0098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be002c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be002c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00be0454"
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
      "unmatched:00be002c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00be04d4",
      "READ",
      [
        "storage",
        "01126978",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00be0148",
      "READ",
      [
        "storage",
        "00c9b618",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00be0454",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00be04d4",
      "READ",
      [
        "storage",
        "01126d78",
        null,
        "undefined8"
      ]
    ],
    [
      "00be0570",
      "READ",
      [
        "storage",
        "00c9ba18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be002c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0028.md#insn-00be002c) · [`00be0080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0028.md#insn-00be0080) · [`00be00b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0028.md#insn-00be00b8)
- 新版 `00be04a8`（命令位置の公開資料なし） · `00be04e0`（命令位置の公開資料なし）

~~~diff
- 00be002c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00be002c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00be002c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00be002c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be002c bytes fa6704a9
- 00be0080 ["INT_ADD", "register:40f0:8", ["const:be0080:8", "const:4:8"]]
- 00be0080 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00be04a8 ["INT_ADD", "register:40f0:8", ["const:be04a8:8", "const:4:8"]]
+ 00be04a8 ["CALL", null, ["callee:00c5ae40:8"]]
- 00be0080 bytes 70ea0194
+ 00be04a8 bytes 66ea0194
- 00be00b8 ["INT_ADD", "register:40f0:8", ["const:be00b8:8", "const:4:8"]]
- 00be00b8 ["CALL", null, ["callee:00497834:8"]]
+ 00be04e0 ["INT_ADD", "register:40f0:8", ["const:be04e0:8", "const:4:8"]]
+ 00be04e0 ["CALL", null, ["callee:00497834:8"]]
- 00be00b8 bytes cfdde297
+ 00be04e0 bytes d5dce297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-668777b747bf527f566672f7837ab28f"></a>

### [`00be0218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0218.md) → [`00be0640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0640.md) _ZN8firebase4auth4User14ReauthenticateERKNS0_10CredentialE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bd0098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bd04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd04c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 26.67% / 新版 26.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be0228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00be022c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0228",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00be022c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00be0240",
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
      "00be0650",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00be0654",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00be0668",
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

- 旧版 [`00be0228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0218.md#insn-00be0228) · [`00be022c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0218.md#insn-00be022c) · [`00be0240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0218.md#insn-00be0240)

~~~diff
- 00be0228 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00be0228 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00be0228 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00be0228 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be0228 bytes f44f07a9
- 00be022c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00be022c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00be022c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00be022c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00be022c bytes fd7b08a9
- 00be0240 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00be0240 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00be0240 bytes e91f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ab8e0ce91b7b720af188b73cd3461fe"></a>

### [`00be05e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be05e8.md) → [`00be0a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be0/00be0a10.md) _ZNK8firebase4auth4User26ReauthenticateWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
    "old": {
      "definition_site": "00be0624",
      "incomplete_value": false,
      "site": "00be0628",
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
            "const:b82:8"
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
      "00be0a4c",
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
      "00be0a4c",
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

- 旧版 [`00be0628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be05e8.md#insn-00be0628) · [`00be0624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be05e8.md#insn-00be0624) · [`00be0634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be05e8.md#insn-00be0634)
- 新版 `00be0a50`（命令位置の公開資料なし） · `00be0a4c`（命令位置の公開資料なし） · `00be0a5c`（命令位置の公開資料なし）

~~~diff
- 00be0628 ["INT_ADD", "register:40f0:8", ["const:be0628:8", "const:4:8"]]
- 00be0628 ["CALL", null, ["callee:00c5b000:8"]]
+ 00be0a50 ["INT_ADD", "register:40f0:8", ["const:be0a50:8", "const:4:8"]]
+ 00be0a50 ["CALL", null, ["callee:00c5b000:8"]]
- 00be0628 bytes 76e90194
+ 00be0a50 bytes 6ce90194
- 00be0624 ["COPY", "tmp:0:8", ["const:b82:8"]]
- 00be0624 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00be0624 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00be0624 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00be0a4c ["COPY", "tmp:0:8", ["const:bc2:8"]]
+ 00be0a4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00be0a4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00be0a4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00be0624 bytes 00082e91
+ 00be0a4c bytes 00082f91
- 00be0634 ["INT_ADD", "register:40f0:8", ["const:be0634:8", "const:4:8"]]
- 00be0634 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00be0a5c ["INT_ADD", "register:40f0:8", ["const:be0a5c:8", "const:4:8"]]
+ 00be0a5c ["CALL", null, ["callee:00c5ac70:8"]]
- 00be0634 bytes 8fe80194
+ 00be0a5c bytes 85e80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bf4c7afaa24c00c251d3c62d43ed667"></a>

### [`00be0c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0c7c.md) → [`00be10a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be10a4.md) _ZNK8firebase4auth4User8metadataEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

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
    "old": {
      "definition_site": "00be0cb0",
      "incomplete_value": true,
      "site": "00be0cbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a0:8"
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
    "old": {
      "definition_site": "00be0cd8",
      "incomplete_value": true,
      "site": "00be0ce4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a10:8"
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
      "00be10d8",
      "READ",
      [
        "storage",
        "011269a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00be1100",
      "READ",
      [
        "storage",
        "01126a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00be1110",
      "READ",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00be10d8",
      "READ",
      [
        "storage",
        "01126da0",
        null,
        "undefined8"
      ]
    ],
    [
      "00be1100",
      "READ",
      [
        "storage",
        "01126e10",
        null,
        "undefined8"
      ]
    ],
    [
      "00be1110",
      "READ",
      [
        "storage",
        "01126e18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0c7c.md#insn-00be0cbc) · [`00be0ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0c7c.md#insn-00be0ce4) · [`00be0ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0c7c.md#insn-00be0ca4)
- 新版 `00be10e4`（命令位置の公開資料なし） · `00be110c`（命令位置の公開資料なし） · `00be10cc`（命令位置の公開資料なし）

~~~diff
- 00be0cbc ["INT_ADD", "register:40f0:8", ["const:be0cbc:8", "const:4:8"]]
- 00be0cbc ["CALL", null, ["callee:00497834:8"]]
+ 00be10e4 ["INT_ADD", "register:40f0:8", ["const:be10e4:8", "const:4:8"]]
+ 00be10e4 ["CALL", null, ["callee:00497834:8"]]
- 00be0cbc bytes cedae297
+ 00be10e4 bytes d4d9e297
- 00be0ce4 ["INT_ADD", "register:40f0:8", ["const:be0ce4:8", "const:4:8"]]
- 00be0ce4 ["CALL", null, ["callee:0058f59c:8"]]
+ 00be110c ["INT_ADD", "register:40f0:8", ["const:be110c:8", "const:4:8"]]
+ 00be110c ["CALL", null, ["callee:0058f59c:8"]]
- 00be0ce4 bytes 1ebae697
+ 00be110c bytes 24b9e697
- 00be0ca4 ["INT_ADD", "register:40f0:8", ["const:be0ca4:8", "const:4:8"]]
- 00be0ca4 ["CALL", null, ["callee:00c5b080:8"]]
+ 00be10cc ["INT_ADD", "register:40f0:8", ["const:be10cc:8", "const:4:8"]]
+ 00be10cc ["CALL", null, ["callee:00c5b080:8"]]
- 00be0ca4 bytes f7e70194
+ 00be10cc bytes ede70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea8ff7cb6342f7d149d8ca2926e9dbcc"></a>

### [`00be0e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0e08.md) → [`00be1230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1230.md) _ZN8firebase4auth22AndroidWrappedUserInfoD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d780.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5db80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db80.md)

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
    "old": {
      "definition_site": "00be0e24",
      "incomplete_value": true,
      "site": "00be0e28",
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
      "00be1244",
      "READ",
      [
        "storage",
        "00c9b660",
        null,
        "pointer"
      ]
    ],
    [
      "00be1250",
      "DATA",
      [
        "storage",
        "00c92510",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00be1244",
      "READ",
      [
        "storage",
        "00c9ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00be1250",
      "DATA",
      [
        "storage",
        "00c92910",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0e08.md#insn-00be0e1c) · [`00be0e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0e08.md#insn-00be0e30) · [`00be0e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0e08.md#insn-00be0e40)
- 新版 `00be1244`（命令位置の公開資料なし） · `00be1258`（命令位置の公開資料なし） · `00be1268`（命令位置の公開資料なし）

~~~diff
- 00be0e1c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:660:8"]]
- 00be0e1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00be1244 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a60:8"]]
+ 00be1244 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0e1c bytes 293143f9
+ 00be1244 bytes 293145f9
- 00be0e30 ["INT_ADD", "register:40f0:8", ["const:be0e30:8", "const:4:8"]]
- 00be0e30 ["CALL", null, ["callee:00c5b080:8"]]
+ 00be1258 ["INT_ADD", "register:40f0:8", ["const:be1258:8", "const:4:8"]]
+ 00be1258 ["CALL", null, ["callee:00c5b080:8"]]
- 00be0e30 bytes 94e70194
+ 00be1258 bytes 8ae70194
- 00be0e40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00be0e40 ["INT_ADD", "register:40f0:8", ["const:be0e40:8", "const:4:8"]]
- 00be0e40 ["CALLIND", null, ["register:0:8"]]
+ 00be1268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00be1268 ["INT_ADD", "register:40f0:8", ["const:be1268:8", "const:4:8"]]
+ 00be1268 ["CALLIND", null, ["register:0:8"]]
- 00be0e40 bytes 00013fd6
+ 00be1268 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-999910e3b0e65bb5de8337234b802f4d"></a>

### [`00be0e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0e84.md) → [`00be12ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be12ac.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allo

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5da90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da90.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5de90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de90.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

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
    "old": {
      "definition_site": "00be0ee8",
      "incomplete_value": false,
      "site": "00be0eec",
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
      "00be1310",
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
      "00be1310",
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

- 旧版 [`00be0eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0e84.md#insn-00be0eec) · [`00be0eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0e84.md#insn-00be0eb0) · [`00be0ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0e84.md#insn-00be0ebc)
- 新版 `00be1314`（命令位置の公開資料なし） · `00be12d8`（命令位置の公開資料なし） · `00be12e4`（命令位置の公開資料なし）

~~~diff
- 00be0eec ["INT_ADD", "register:40f0:8", ["const:be0eec:8", "const:4:8"]]
- 00be0eec ["CALL", null, ["callee:00c5b000:8"]]
+ 00be1314 ["INT_ADD", "register:40f0:8", ["const:be1314:8", "const:4:8"]]
+ 00be1314 ["CALL", null, ["callee:00c5b000:8"]]
- 00be0eec bytes 45e70194
+ 00be1314 bytes 3be70194
- 00be0eb0 ["INT_ADD", "register:40f0:8", ["const:be0eb0:8", "const:4:8"]]
- 00be0eb0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be12d8 ["INT_ADD", "register:40f0:8", ["const:be12d8:8", "const:4:8"]]
+ 00be12d8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00be0eb0 bytes d4e50194
+ 00be12d8 bytes cae50194
- 00be0ebc ["INT_ADD", "register:40f0:8", ["const:be0ebc:8", "const:4:8"]]
- 00be0ebc ["CALL", null, ["callee:00c5ae80:8"]]
+ 00be12e4 ["INT_ADD", "register:40f0:8", ["const:be12e4:8", "const:4:8"]]
+ 00be12e4 ["CALL", null, ["callee:00c5ae80:8"]]
- 00be0ebc bytes f1e60194
+ 00be12e4 bytes e7e60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72295788fdab358bcb966d2390f76bbb"></a>

### [`00be1060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1060.md) → [`00be1488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1488.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS_4auth14Fut

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5da80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5da80.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)
- 新版 呼出元 1件 [`00c5de80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de80.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)

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
    "old": {
      "definition_site": "00be10cc",
      "incomplete_value": false,
      "site": "00be10d0",
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
      "00be14f4",
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
      "00be14f4",
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

- 旧版 [`00be10d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1060.md#insn-00be10d0) · [`00be1094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1060.md#insn-00be1094) · [`00be10a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1060.md#insn-00be10a0)
- 新版 `00be14f8`（命令位置の公開資料なし） · `00be14bc`（命令位置の公開資料なし） · `00be14c8`（命令位置の公開資料なし）

~~~diff
- 00be10d0 ["INT_ADD", "register:40f0:8", ["const:be10d0:8", "const:4:8"]]
- 00be10d0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00be14f8 ["INT_ADD", "register:40f0:8", ["const:be14f8:8", "const:4:8"]]
+ 00be14f8 ["CALL", null, ["callee:00c5b000:8"]]
- 00be10d0 bytes cce60194
+ 00be14f8 bytes c2e60194
- 00be1094 ["INT_ADD", "register:40f0:8", ["const:be1094:8", "const:4:8"]]
- 00be1094 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00be14bc ["INT_ADD", "register:40f0:8", ["const:be14bc:8", "const:4:8"]]
+ 00be14bc ["CALL", null, ["callee:00c5aa00:8"]]
- 00be1094 bytes 5be50194
+ 00be14bc bytes 51e50194
- 00be10a0 ["INT_ADD", "register:40f0:8", ["const:be10a0:8", "const:4:8"]]
- 00be10a0 ["CALL", null, ["callee:00c5ae80:8"]]
+ 00be14c8 ["INT_ADD", "register:40f0:8", ["const:be14c8:8", "const:4:8"]]
+ 00be14c8 ["CALL", null, ["callee:00c5ae80:8"]]
- 00be10a0 bytes 78e60194
+ 00be14c8 bytes 6ee60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00e0829caf4190bffaa3ba833882cc62"></a>

### [`00be1cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1cfc.md) → [`00be2124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be2124.md) _ZN8firebase4auth17UserInfoInterfaceD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d770.md) [`00c5d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d780.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00c5db70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db70.md) [`00c5db80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db80.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "00be1d18",
      "incomplete_value": true,
      "site": "00be1d1c",
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
      "00be2138",
      "READ",
      [
        "storage",
        "00c9b5c8",
        null,
        "pointer"
      ]
    ],
    [
      "00be2144",
      "DATA",
      [
        "storage",
        "00c92578",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00be2138",
      "READ",
      [
        "storage",
        "00c9b9c8",
        null,
        "pointer"
      ]
    ],
    [
      "00be2144",
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

- 旧版 [`00be1d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1cfc.md#insn-00be1d10) · [`00be1d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1cfc.md#insn-00be1d5c) · [`00be1d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1cfc.md#insn-00be1d6c)
- 新版 `00be2138`（命令位置の公開資料なし） · `00be2184`（命令位置の公開資料なし） · `00be2194`（命令位置の公開資料なし）

~~~diff
- 00be1d10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5c8:8"]]
- 00be1d10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00be2138 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9c8:8"]]
+ 00be2138 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00be1d10 bytes 29e542f9
+ 00be2138 bytes 29e544f9
- 00be1d5c ["INT_ADD", "register:40f0:8", ["const:be1d5c:8", "const:4:8"]]
- 00be1d5c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00be2184 ["INT_ADD", "register:40f0:8", ["const:be2184:8", "const:4:8"]]
+ 00be2184 ["CALL", null, ["callee:00c57eb0:8"]]
- 00be1d5c bytes 55d70194
+ 00be2184 bytes 4bd70194
- 00be1d6c ["INT_ADD", "register:40f0:8", ["const:be1d6c:8", "const:4:8"]]
- 00be1d6c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00be2194 ["INT_ADD", "register:40f0:8", ["const:be2194:8", "const:4:8"]]
+ 00be2194 ["CALL", null, ["callee:00c57eb0:8"]]
- 00be1d6c bytes 51d70194
+ 00be2194 bytes 47d70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69b2d4c9a32022d1e7a32c9bf8a209cd"></a>

### [`00be2c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md) → [`00be30b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be30b4.md) FUN_00be30b4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be2c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c70.md) [`00be2c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md) · 呼出先 4件 [`00be2c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md) [`00be99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be99a0.md) [`00be9c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be9c60.md) [`00be9d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be9/00be9d88.md)
- 新版 呼出元 2件 [`00be3098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3098.md) [`00be30b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be30b4.md) · 呼出先 4件 [`00be30b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be30b4.md) [`00be9dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be9/00be9dc8.md) [`00bea088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea088.md) [`00bea1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00bea1b0.md)

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
      "site": "00be3440",
      "value": [
        "leaf",
        "ram:be9dc8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be3018",
      "value": [
        "leaf",
        "ram:be99a0:8"
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
      "site": "00be3454",
      "value": [
        "leaf",
        "ram:be9dc8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be302c",
      "value": [
        "leaf",
        "ram:be99a0:8"
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
      "00be3440",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be99a0"
      ]
    ],
    [
      "00be3454",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be99a0"
      ]
    ]
  ],
  "added": [
    [
      "00be3440",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be9dc8"
      ]
    ],
    [
      "00be3454",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be9dc8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be3018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md#insn-00be3018) · [`00be302c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md#insn-00be302c) · [`00be3048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be2/00be2c8c.md#insn-00be3048)
- 新版 `00be3440`（命令位置の公開資料なし） · `00be3454`（命令位置の公開資料なし） · `00be3470`（命令位置の公開資料なし）

~~~diff
- 00be3018 ["INT_ADD", "register:40f0:8", ["const:be3018:8", "const:4:8"]]
- 00be3018 ["CALL", null, ["ram:be99a0:8"]]
+ 00be3440 ["INT_ADD", "register:40f0:8", ["const:be3440:8", "const:4:8"]]
+ 00be3440 ["CALL", null, ["ram:be9dc8:8"]]
- 00be3018 bytes 621a0094
+ 00be3440 bytes 621a0094
- 00be302c ["INT_ADD", "register:40f0:8", ["const:be302c:8", "const:4:8"]]
- 00be302c ["CALL", null, ["ram:be99a0:8"]]
+ 00be3454 ["INT_ADD", "register:40f0:8", ["const:be3454:8", "const:4:8"]]
+ 00be3454 ["CALL", null, ["ram:be9dc8:8"]]
- 00be302c bytes 5d1a0094
+ 00be3454 bytes 5d1a0094
- 00be3048 ["INT_ADD", "register:40f0:8", ["const:be3048:8", "const:4:8"]]
- 00be3048 ["CALL", null, ["local:b0:8"]]
+ 00be3470 ["INT_ADD", "register:40f0:8", ["const:be3470:8", "const:4:8"]]
+ 00be3470 ["CALL", null, ["local:b0:8"]]
- 00be3048 bytes 11ffff97
+ 00be3470 bytes 11ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

