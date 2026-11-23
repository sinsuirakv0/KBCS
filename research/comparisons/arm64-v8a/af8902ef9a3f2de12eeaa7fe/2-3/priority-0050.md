# v16.0.0 → v16.0.1 · 最優先の変更候補 (50)

[一覧の目次](README.md)

<a id="compare-3f65a4a85e19784c4a6f839c2be0f6f0"></a>

### [`008d078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d078c.md) → [`008d0928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0928.md) _INIT_171

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.23% / 新版 80.23%

CFGの説明率　旧版 38.89% / 新版 38.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d07bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d07e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d0808"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d07bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d07c8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008d07e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008d0958",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008d0964",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "008d0980",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d07bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d078c.md#insn-008d07bc) · [`008d07e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d078c.md#insn-008d07e4) · [`008d0808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d078c.md#insn-008d0808)

~~~diff
- 008d07bc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008d07bc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008d07bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d07bc bytes a9831ff8
- 008d07e4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 008d07e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008d07e4 bytes e013813c
- 008d0808 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 008d0808 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008d0808 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf2736bba5721a1c681d1f673a41a863"></a>

### [`008d0b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d0b1c.md) → [`008d0cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0cb8.md) FUN_008d0cb8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008d1aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1aa4.md) · 呼出先 20件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 1件 [`008d1c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1c40.md) · 呼出先 20件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 84.68% / 新版 84.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 31件, `call_target` 2件, `store_destination` 7件, `store_value` 24件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d0d00",
      "incomplete_value": false,
      "site": "008d0d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0b64",
      "incomplete_value": false,
      "site": "008d0b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
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
      "definition_site": "008d0df8",
      "incomplete_value": true,
      "site": "008d0df8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:38e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0c5c",
      "incomplete_value": true,
      "site": "008d0c5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:34e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d0e10",
      "incomplete_value": true,
      "site": "008d0e10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:f16:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0c74",
      "incomplete_value": true,
      "site": "008d0c74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:ed6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d0d04",
      "DATA",
      [
        "storage",
        "00c841b8",
        null,
        "undefined *"
      ]
    ],
    [
      "008d0dc8",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "008d0de8",
      "READ",
      [
        "storage",
        "002b634e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d0d04",
      "DATA",
      [
        "storage",
        "00c845b8",
        null,
        "undefined *"
      ]
    ],
    [
      "008d0dc8",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008d0de8",
      "READ",
      [
        "storage",
        "002b638e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d0bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d0b1c.md#insn-008d0bf0) · [`008d0c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d0b1c.md#insn-008d0c98) · [`008d0ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d0b1c.md#insn-008d0ce8)
- 新版 `008d0d8c`（命令位置の公開資料なし） · `008d0e34`（命令位置の公開資料なし） · `008d0e84`（命令位置の公開資料なし）

~~~diff
- 008d0bf0 ["INT_ADD", "register:40f0:8", ["const:8d0bf0:8", "const:4:8"]]
- 008d0bf0 ["CALL", null, ["callee:00c57e80:8"]]
+ 008d0d8c ["INT_ADD", "register:40f0:8", ["const:8d0d8c:8", "const:4:8"]]
+ 008d0d8c ["CALL", null, ["callee:00c57e80:8"]]
- 008d0bf0 bytes a41b0e94
+ 008d0d8c bytes 3d1c0e94
- 008d0c98 ["INT_ADD", "register:40f0:8", ["const:8d0c98:8", "const:4:8"]]
- 008d0c98 ["CALL", null, ["callee:00633374:8"]]
+ 008d0e34 ["INT_ADD", "register:40f0:8", ["const:8d0e34:8", "const:4:8"]]
+ 008d0e34 ["CALL", null, ["callee:00633374:8"]]
- 008d0c98 bytes a789f597
+ 008d0e34 bytes 5089f597
- 008d0ce8 ["INT_ADD", "register:40f0:8", ["const:8d0ce8:8", "const:4:8"]]
- 008d0ce8 ["CALL", null, ["callee:00c53d00:8"]]
+ 008d0e84 ["INT_ADD", "register:40f0:8", ["const:8d0e84:8", "const:4:8"]]
+ 008d0e84 ["CALL", null, ["callee:00c53d00:8"]]
- 008d0ce8 bytes fe0a0e94
+ 008d0e84 bytes 9f0b0e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aead938e1f39ac18f759ddc5bdacbfa"></a>

### [`008d188c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d188c.md) → [`008d1a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1a28.md) FUN_008d1a28

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008d0b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d0b1c.md) [`00a95e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a95/00a95e04.md) · 呼出先 10件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00b3c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c6b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 2件 [`008d0cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0cb8.md) [`00a95ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a95/00a95ffc.md) · 呼出先 10件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00b3cad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3cad8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 74.78% / 新版 74.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d1a54",
      "incomplete_value": false,
      "site": "008d1a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d18b8",
      "incomplete_value": false,
      "site": "008d18c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "definition_site": "008d1aa0",
      "incomplete_value": true,
      "site": "008d1aa0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:7c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d1904",
      "incomplete_value": true,
      "site": "008d1904",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:785:8"
              ]
            ]
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
      "definition_site": "008d1ab8",
      "incomplete_value": true,
      "site": "008d1ab8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:ffc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d191c",
      "incomplete_value": true,
      "site": "008d191c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:fbc:8"
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
      "008d1a5c",
      "DATA",
      [
        "storage",
        "00c84208",
        null,
        "pointer"
      ]
    ],
    [
      "008d1a70",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "008d1a90",
      "READ",
      [
        "storage",
        "002ab785",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d1a5c",
      "DATA",
      [
        "storage",
        "00c84608",
        null,
        "pointer"
      ]
    ],
    [
      "008d1a70",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008d1a90",
      "READ",
      [
        "storage",
        "002ab7c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d18b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d188c.md#insn-008d18b0) · [`008d193c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d188c.md#insn-008d193c) · [`008d1a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d188c.md#insn-008d1a04)
- 新版 `008d1a4c`（命令位置の公開資料なし） · `008d1ad8`（命令位置の公開資料なし） · `008d1ba0`（命令位置の公開資料なし）

~~~diff
- 008d18b0 ["INT_ADD", "register:40f0:8", ["const:8d18b0:8", "const:4:8"]]
- 008d18b0 ["CALL", null, ["callee:00b3cad8:8"]]
+ 008d1a4c ["INT_ADD", "register:40f0:8", ["const:8d1a4c:8", "const:4:8"]]
+ 008d1a4c ["CALL", null, ["callee:00b3cad8:8"]]
- 008d18b0 bytes 80ab0994
+ 008d1a4c bytes 23ac0994
- 008d193c ["INT_ADD", "register:40f0:8", ["const:8d193c:8", "const:4:8"]]
- 008d193c ["CALL", null, ["callee:0047e60c:8"]]
+ 008d1ad8 ["INT_ADD", "register:40f0:8", ["const:8d1ad8:8", "const:4:8"]]
+ 008d1ad8 ["CALL", null, ["callee:0047e60c:8"]]
- 008d193c bytes 24b3ee97
+ 008d1ad8 bytes cdb2ee97
- 008d1a04 ["INT_ADD", "register:40f0:8", ["const:8d1a04:8", "const:4:8"]]
- 008d1a04 ["CALL", null, ["callee:00c57e50:8"]]
+ 008d1ba0 ["INT_ADD", "register:40f0:8", ["const:8d1ba0:8", "const:4:8"]]
+ 008d1ba0 ["CALL", null, ["callee:00c57e50:8"]]
- 008d1a04 bytes 13180e94
+ 008d1ba0 bytes ac180e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e491ae3da1fa64ad00e297841cd9094b"></a>

### [`008d1aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1aa4.md) → [`008d1c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1c40.md) FUN_008d1c40

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 16件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`0066d09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d09c.md) [`008b7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7950.md) [`008d0b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d0b1c.md) [`008d8260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8260.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 16件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`0066d0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d0dc.md) [`008b7994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7994.md) [`008d0cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0cb8.md) [`008d83fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d83fc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008d1c84",
      "incomplete_value": false,
      "site": "008d1c84",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d1ae8",
      "incomplete_value": false,
      "site": "008d1ae8",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d1c7c",
      "incomplete_value": true,
      "site": "008d1c84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
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
      "definition_site": "008d1ae0",
      "incomplete_value": true,
      "site": "008d1ae8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008d1c88",
      "incomplete_value": false,
      "site": "008d1c88",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d1aec",
      "incomplete_value": false,
      "site": "008d1aec",
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
            "const:578:8"
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
      "008d1c7c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1c80",
      "READ",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1c84",
      "WRITE",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008d1c7c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1c80",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1c84",
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d1ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1aa4.md#insn-008d1ae8) · [`008d1aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1aa4.md#insn-008d1aec) · [`008d1b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1aa4.md#insn-008d1b10)
- 新版 `008d1c84`（命令位置の公開資料なし） · `008d1c88`（命令位置の公開資料なし） · `008d1cac`（命令位置の公開資料なし）

~~~diff
- 008d1ae8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 008d1ae8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008d1c84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
+ 008d1c84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008d1ae8 bytes 09b502f9
+ 008d1c84 bytes 09b504f9
- 008d1aec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
- 008d1aec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008d1c88 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:978:8"]]
+ 008d1c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008d1aec bytes aabe02f9
+ 008d1c88 bytes aabe04f9
- 008d1b10 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
- 008d1b10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008d1cac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:978:8"]]
+ 008d1cac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008d1b10 bytes b4be02f9
+ 008d1cac bytes b4be04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-539445b3e2658835665e762341439f1c"></a>

### [`008d1d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1d14.md) → [`008d1eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1eb0.md) FUN_008d1eb0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`008ad760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad760.md) [`008d305c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d305c.md) [`008d9a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md) · 呼出先 28件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`008b6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ecc.md)
- 新版 呼出元 4件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`008ad7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad7a4.md) [`008d31f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d31f8.md) [`008d9c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9c04.md) · 呼出先 28件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008b6f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.85% / 新版 72.85%

CFGの説明率　旧版 33.33% / 新版 29.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 1件, `store_value` 3件, `unresolved_branch_alignment` 21件, `unresolved_call_alignment` 26件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 25件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d1fc0",
      "incomplete_value": false,
      "site": "008d1fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d1e24",
      "incomplete_value": false,
      "site": "008d1e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d1e98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d1eb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d1eec",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1ef8",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008d1f00",
      "PARAM",
      [
        "storage",
        "00c841e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008d1eec",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1ef8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008d1f00",
      "PARAM",
      [
        "storage",
        "00c845e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d1e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1d14.md#insn-008d1e98) · [`008d1eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1d14.md#insn-008d1eb4) · [`008d1ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1d14.md#insn-008d1ec4)

~~~diff
- 008d1e98 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d1e98 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 008d1e98 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:50:8"]]
- 008d1e98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d1e98 bytes 080405f8
- 008d1eb4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 008d1eb4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 008d1eb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 008d1eb4 bytes ff0f00f9
- 008d1ec4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008d1ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d1ec4 bytes c80200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82891042c142c6dfbc042b046993c285"></a>

### [`008d27c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d27c0.md) → [`008d295c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d295c.md) FUN_008d295c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 4件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`00732e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732e8c.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) [`008144d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/008144d4.md) · 呼出先 0件 
- 新版 呼出元 4件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`00732ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) [`00814514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814514.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-083523fc67873e6252fca6063ef64715"></a>

### [`008d2908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d2908.md) → [`008d2aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2aa4.md) FUN_008d2aa4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`008ad760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad760.md) · 呼出先 4件 [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md) [`008d299c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d299c.md) [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) [`00ac948c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac948c.md)
- 新版 呼出元 2件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`008ad7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad7a4.md) · 呼出先 4件 [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md) [`008d2b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2b38.md) [`00aa3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3e24.md) [`00ac9688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac9688.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d2ad4",
      "incomplete_value": true,
      "site": "008d2ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "live",
            "register:40a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d2938",
      "incomplete_value": true,
      "site": "008d293c",
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
            "const:2f38:8"
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
      "definition_site": "008d2930",
      "incomplete_value": false,
      "site": "008d293c",
      "value": [
        "leaf",
        "const:1:8"
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
      "008d2b00",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "008d2b00",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d293c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d2908.md#insn-008d293c) · [`008d2928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d2908.md#insn-008d2928) · [`008d2938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d2908.md#insn-008d2938)
- 新版 `008d2ad8`（命令位置の公開資料なし） · `008d2ac4`（命令位置の公開資料なし）

~~~diff
- 008d293c ["INT_ADD", "register:40f0:8", ["const:8d293c:8", "const:4:8"]]
- 008d293c ["CALL", null, ["callee:008b7a10:8"]]
+ 008d2ad8 ["INT_ADD", "register:40f0:8", ["const:8d2ad8:8", "const:4:8"]]
+ 008d2ad8 ["CALL", null, ["callee:008b7a10:8"]]
- 008d293c bytes 2494ff97
+ 008d2ad8 bytes ce93ff97
- 008d2928 ["INT_ADD", "register:40f0:8", ["const:8d2928:8", "const:4:8"]]
- 008d2928 ["CALL", null, ["callee:00ac9688:8"]]
+ 008d2ac4 ["INT_ADD", "register:40f0:8", ["const:8d2ac4:8", "const:4:8"]]
+ 008d2ac4 ["CALL", null, ["callee:00ac9688:8"]]
- 008d2928 bytes d9da0794
+ 008d2ac4 bytes f1da0794
- 008d2938 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008d2938 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008d2938 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008d2938 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008d2938 bytes 6002148b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c390d51c2e70f122403a47791e54f04"></a>

### [`008d299c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d299c.md) → [`008d2b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2b38.md) FUN_008d2b38

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`008d2908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d2908.md) [`008d8570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8570.md) [`008d98a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d98a4.md) [`008d9a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md) · 呼出先 19件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005dbcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbcd4.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`0071ebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071ebdc.md)
- 新版 呼出元 5件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`008d2aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2aa4.md) [`008d870c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d870c.md) [`008d9a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9a40.md) [`008d9c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9c04.md) · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005dbd14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005dbd14.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`0071ec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071ec1c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.12% / 新版 89.12%

CFGの説明率　旧版 54.92% / 新版 58.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件, `store_value` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d29a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d29a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d29a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d29a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d29a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d29a8",
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
      "008d2b3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d2b40",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008d2b44",
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

- 旧版 [`008d29a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d299c.md#insn-008d29a0) · [`008d29a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d299c.md#insn-008d29a4) · [`008d29a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d299c.md#insn-008d29a8)

~~~diff
- 008d29a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d29a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d29a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 008d29a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d29a0 bytes fd7b15a9
- 008d29a4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008d29a4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008d29a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 008d29a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d29a4 bytes fc6f16a9
- 008d29a8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008d29a8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008d29a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 008d29a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d29a8 bytes fa6717a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67792b50d280b7f78b624da592e5110f"></a>

### [`008d305c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d305c.md) → [`008d31f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d31f8.md) FUN_008d31f8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 17件 [`0044d9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d9f8.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`0048eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 17件 [`0044da38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044da38.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`0048eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.60% / 新版 75.60%

CFGの説明率　旧版 48.08% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 14件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d33f4",
      "incomplete_value": true,
      "site": "008d33f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:263:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d3258",
      "incomplete_value": true,
      "site": "008d3258",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:223:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d3318"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d331c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d322c",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "008d3238",
      "READ",
      [
        "storage",
        "00ca4b30",
        null,
        "undefined8"
      ]
    ],
    [
      "008d324c",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008d322c",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008d3238",
      "READ",
      [
        "storage",
        "00ca4f30",
        null,
        "undefined8"
      ]
    ],
    [
      "008d324c",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d30bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d305c.md#insn-008d30bc) · [`008d317c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d305c.md#insn-008d317c) · [`008d3190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d305c.md#insn-008d3190)
- 新版 `008d3318`（命令位置の公開資料なし） · `008d332c`（命令位置の公開資料なし）

~~~diff
- 008d30bc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008d30bc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 008d30bc bytes 600000b4
- 008d317c ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 008d3318 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 008d317c bytes 60000054
+ 008d3318 bytes 60000054
- 008d3190 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008d3190 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 008d332c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 008d332c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 008d3190 bytes 4b000054
+ 008d332c bytes 4b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71491cfe0a4b649156e0f9abd26ad753"></a>

### [`008d3410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3410.md) → [`008d35ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35ac.md) FUN_008d35ac

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 4件 [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) [`00a06374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06374.md) [`00a06440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06440.md) [`00a064d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a064d8.md) · 呼出先 0件 
- 新版 呼出元 4件 [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) [`00a06510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06510.md) [`00a065dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a065dc.md) [`00a06674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06674.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-4b4e6650e7d0f5e6f37c66c432c2ff28"></a>

### [`008d3454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3454.md) → [`008d35f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35f0.md) FUN_008d35f0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`008ad760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad760.md) [`008d305c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d305c.md) · 呼出先 4件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00865ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865ab4.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 6件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`008ad7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad7a4.md) [`008d31f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d31f8.md) · 呼出先 4件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00865af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865af4.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 29.23% / 新版 29.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 10件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d3458"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d345c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d345c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d3458",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d345c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d3460",
      "WRITE",
      [
        "storage",
        "Stack[-0x18]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008d35f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008d35f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "008d35fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x18]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d3458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3454.md#insn-008d3458) · [`008d345c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3454.md#insn-008d345c) · [`008d3460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3454.md#insn-008d3460)

~~~diff
- 008d3458 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008d3458 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 008d3458 bytes e80b00fd
- 008d345c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d345c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d345c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:18:8"]]
- 008d345c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d345c bytes fdfb01a9
- 008d3460 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 008d3460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 008d3460 bytes f51700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fe5b2f55f3187191503cdfd2da7b59a"></a>

### [`008d3700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3700.md) → [`008d389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d389c.md) FUN_008d389c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 39件 [`00467a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md) [`00467ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467ab0.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 39件 [`00467a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.15% / 新版 85.15%

CFGの説明率　旧版 24.75% / 新版 25.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 135件, `call_target` 2件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 17件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d3704"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d3708"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d3708"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d3704",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d3708",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d370c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008d38a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "008d38a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d38a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d3704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3700.md#insn-008d3704) · [`008d3708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3700.md#insn-008d3708) · [`008d370c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3700.md#insn-008d370c)

~~~diff
- 008d3704 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:a0:8"]]
- 008d3704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 008d3704 bytes e85300fd
- 008d3708 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d3708 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d3708 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 008d3708 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d3708 bytes fd7b0ba9
- 008d370c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008d370c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008d370c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 008d370c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d370c bytes fc6f0ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0587b420be66ab22841ef822c0c6dd9"></a>

### [`008d4b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d4/008d4b18.md) → [`008d4cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d4/008d4cb4.md) FUN_008d4cb4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 2件 [`00732e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732e8c.md) [`00b2f5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f5e4.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00732ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`00b2fa0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2fa0c.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-d9b2cb2a22c810dfa58f6972c9471709"></a>

### [`008d4b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d4/008d4b20.md) → [`008d4cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d4/008d4cbc.md) FUN_008d4cbc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 80.00% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d4b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d4/008d4b20.md#insn-008d4b64) · [`008d4b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d4/008d4b20.md#insn-008d4b74) · [`008d4b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d4/008d4b20.md#insn-008d4b80)
- 新版 `008d4d00`（命令位置の公開資料なし） · `008d4d10`（命令位置の公開資料なし） · `008d4d1c`（命令位置の公開資料なし）

~~~diff
- 008d4b64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d4b64 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 008d4b64 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
+ 008d4d00 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008d4d00 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 008d4d00 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 008d4b64 bytes 08020054
+ 008d4d00 bytes 08020054
- 008d4b74 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d4b74 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 008d4b74 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 008d4d10 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008d4d10 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 008d4d10 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 008d4b74 bytes 88000054
+ 008d4d10 bytes 88000054
- 008d4b80 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d4b80 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 008d4b80 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 008d4b80 ["CBRANCH", null, ["local:b6:8", "tmp:2:1"]]
+ 008d4d1c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008d4d1c ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 008d4d1c ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 008d4d1c ["CBRANCH", null, ["local:b5:8", "tmp:2:1"]]
- 008d4b80 bytes ec000054
+ 008d4d1c bytes ec000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f783491a1c2ac0877de1f46197c12bc5"></a>

### [`008d4bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d4/008d4bc0.md) → [`008d4d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d4/008d4d5c.md) FUN_008d4d5c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008d299c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d299c.md) · 呼出先 9件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005dc2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc2c0.md) [`008d809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d809c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`008d2b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2b38.md) · 呼出先 9件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005dc300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dc/005dc300.md) [`008d8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8238.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.77% / 新版 86.77%

CFGの説明率　旧版 56.18% / 新版 53.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d4bc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d4bc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d4bc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d4bc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d4bc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d4bcc",
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
      "008d4d60",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d4d64",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008d4d68",
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

- 旧版 [`008d4bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d4/008d4bc0.md#insn-008d4bc4) · [`008d4bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d4/008d4bc0.md#insn-008d4bc8) · [`008d4bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d4/008d4bc0.md#insn-008d4bcc)

~~~diff
- 008d4bc4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d4bc4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d4bc4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 008d4bc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d4bc4 bytes fd7b05a9
- 008d4bc8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008d4bc8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008d4bc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 008d4bc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d4bc8 bytes fc6f06a9
- 008d4bcc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008d4bcc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008d4bcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 008d4bcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d4bcc bytes fa6707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7eda5febb3f4afd9d7068fab85355d6"></a>

### [`008d5008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5008.md) → [`008d51a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d51a4.md) FUN_008d51a4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`008d89c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d89c0.md) · 呼出先 12件 [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008ba824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008ba824.md) [`008d52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md) [`008d9958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9958.md)
- 新版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`008d8b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b5c.md) · 呼出先 12件 [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008ba868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008ba868.md) [`008d548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md) [`008d9af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9af4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.37% / 新版 70.37%

CFGの説明率　旧版 9.30% / 新版 8.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d502c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d504c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5050"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d502c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d5030",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048ce50"
      ]
    ],
    [
      "unmatched:008d5034",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5250"
      ]
    ]
  ],
  "added": [
    [
      "008d51c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008d51cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048ce50"
      ]
    ],
    [
      "008d51d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5250"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d502c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5008.md#insn-008d502c) · [`008d5030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5008.md#insn-008d5030) · [`008d5034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5008.md#insn-008d5034)

~~~diff
- 008d502c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d502c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008d502c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d502c bytes a8831ff8
- 008d5030 ["INT_ADD", "register:40f0:8", ["const:8d5030:8", "const:4:8"]]
- 008d5030 ["CALL", null, ["callee:0048ce50:8"]]
- 008d5030 bytes 78dfee97
- 008d5034 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 008d5034 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 008d5034 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 008d5034 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 008d5034 bytes 00040036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-469a0edc1179a4b2ce3101f671f3b735"></a>

### [`008d52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md) → [`008d548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md) FUN_008d548c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`008d5008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5008.md) · 呼出先 17件 [`0044b764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b764.md) [`005618ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/005618ac.md) [`00561ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561ae4.md) [`00561cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cac.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md)
- 新版 呼出元 2件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`008d51a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d51a4.md) · 呼出先 17件 [`0044b7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b7a4.md) [`005618ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md) [`00561b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md) [`00561cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561cec.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.74% / 新版 86.74%

CFGの説明率　旧版 40.20% / 新版 42.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5314"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5364"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5370"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d5314",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "008d54cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768398"
      ]
    ],
    [
      "unmatched:008d5364",
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
      "008d54b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "008d54cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683d8"
      ]
    ],
    [
      "008d5500",
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

- 旧版 [`008d5314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md#insn-008d5314) · [`008d5330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md#insn-008d5330) · [`008d5364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md#insn-008d5364)
- 新版 `008d54cc`（命令位置の公開資料なし）

~~~diff
- 008d5314 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d5314 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008d5314 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d5314 bytes a8831ff8
- 008d5330 ["INT_ADD", "register:40f0:8", ["const:8d5330:8", "const:4:8"]]
- 008d5330 ["CALL", null, ["ram:768398:8"]]
+ 008d54cc ["INT_ADD", "register:40f0:8", ["const:8d54cc:8", "const:4:8"]]
+ 008d54cc ["CALL", null, ["ram:7683d8:8"]]
- 008d5330 bytes 1a4cfa97
+ 008d54cc bytes c34bfa97
- 008d5364 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008d5364 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 008d5364 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008d5364 bytes a8831c38
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4451664154a073054a472dedcf19b86"></a>

### [`008d58e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d58e0.md) → [`008d5a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5a7c.md) FUN_008d5a7c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 3件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00865ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865ab4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00865af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865af4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d597c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008d5b18"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "008d5908",
      "incomplete_value": true,
      "site": "008d591c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:b8:8"
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
      "unmatched:008d597c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5b30"
      ]
    ]
  ],
  "added": [
    [
      "008d5b18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5b30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d591c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d58e0.md#insn-008d591c) · [`008d597c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d58e0.md#insn-008d597c) · [`008d5990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d58e0.md#insn-008d5990)
- 新版 `008d5ab8`（命令位置の公開資料なし）

~~~diff
- 008d591c ["INT_ADD", "register:40f0:8", ["const:8d591c:8", "const:4:8"]]
- 008d591c ["CALL", null, ["callee:005c179c:8"]]
+ 008d5ab8 ["INT_ADD", "register:40f0:8", ["const:8d5ab8:8", "const:4:8"]]
+ 008d5ab8 ["CALL", null, ["callee:005c179c:8"]]
- 008d591c bytes 90aff397
+ 008d5ab8 bytes 39aff397
- 008d597c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d597c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 008d597c bytes c1000054
- 008d5990 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d5990 ["RETURN", null, ["register:0:8"]]
- 008d5990 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83bdb1d74fac4c2f71bea2321cf85eb8"></a>

### [`008d5998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5998.md) → [`008d5b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5b34.md) FUN_008d5b34

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) · 呼出先 3件 [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)
- 新版 呼出元 1件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 3件 [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 18.18% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5ad8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008d5c74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "008d59b8",
      "incomplete_value": true,
      "site": "008d59c0",
      "value": [
        "live",
        "register:4008:8"
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
      "unmatched:008d5ad8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5c64"
      ]
    ]
  ],
  "added": [
    [
      "008d5c74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5c64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d59c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5998.md#insn-008d59c0) · [`008d59e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5998.md#insn-008d59e4) · [`008d5a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5998.md#insn-008d5a20)
- 新版 `008d5b5c`（命令位置の公開資料なし） · `008d5b80`（命令位置の公開資料なし） · `008d5bbc`（命令位置の公開資料なし）

~~~diff
- 008d59c0 ["INT_ADD", "register:40f0:8", ["const:8d59c0:8", "const:4:8"]]
- 008d59c0 ["CALL", null, ["callee:00480e28:8"]]
+ 008d5b5c ["INT_ADD", "register:40f0:8", ["const:8d5b5c:8", "const:4:8"]]
+ 008d5b5c ["CALL", null, ["callee:00480e28:8"]]
- 008d59c0 bytes 0aadee97
+ 008d5b5c bytes b3acee97
- 008d59e4 ["INT_ADD", "register:40f0:8", ["const:8d59e4:8", "const:4:8"]]
- 008d59e4 ["CALL", null, ["callee:00481098:8"]]
+ 008d5b80 ["INT_ADD", "register:40f0:8", ["const:8d5b80:8", "const:4:8"]]
+ 008d5b80 ["CALL", null, ["callee:00481098:8"]]
- 008d59e4 bytes 9dadee97
+ 008d5b80 bytes 46adee97
- 008d5a20 ["INT_ADD", "register:40f0:8", ["const:8d5a20:8", "const:4:8"]]
- 008d5a20 ["CALL", null, ["callee:00481098:8"]]
+ 008d5bbc ["INT_ADD", "register:40f0:8", ["const:8d5bbc:8", "const:4:8"]]
+ 008d5bbc ["CALL", null, ["callee:00481098:8"]]
- 008d5a20 bytes 8eadee97
+ 008d5bbc bytes 37adee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6222413adb7ccca4d633315e2475f4e"></a>

### [`008d5ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5ae0.md) → [`008d5c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5c7c.md) FUN_008d5c7c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)
- 新版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 45.45% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5ae8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d5ae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d5ae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d5aec",
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
      "008d5c80",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d5c84",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008d5c88",
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

- 旧版 [`008d5ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5ae0.md#insn-008d5ae4) · [`008d5ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5ae0.md#insn-008d5ae8) · [`008d5aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5ae0.md#insn-008d5aec)

~~~diff
- 008d5ae4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d5ae4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d5ae4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008d5ae4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d5ae4 bytes fd7b01a9
- 008d5ae8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008d5ae8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008d5ae8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008d5ae8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d5ae8 bytes fc6f02a9
- 008d5aec ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008d5aec ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008d5aec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 008d5aec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d5aec bytes fa6703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67a920a05eaeab202bc2c48998d44af3"></a>

### [`008d5ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5ce8.md) → [`008d5e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5e84.md) FUN_008d5e84

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 85.51% / 新版 85.51%

CFGの説明率　旧版 25.81% / 新版 27.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 2件

アドレスに依存する影響 `unresolved_branch_alignment` 8件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5d54"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5d7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5d80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d5d54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5f00"
      ]
    ],
    [
      "unmatched:008d5d80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5f4c"
      ]
    ],
    [
      "008d5ef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5f74"
      ]
    ]
  ],
  "added": [
    [
      "008d5ef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5f00"
      ]
    ],
    [
      "008d5f1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5f4c"
      ]
    ],
    [
      "008d5f60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5f74"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5ce8.md#insn-008d5d54) · [`008d5d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5ce8.md#insn-008d5d7c) · [`008d5d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5ce8.md#insn-008d5d80)

~~~diff
- 008d5d54 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d5d54 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 008d5d54 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 008d5d54 bytes 88000054
- 008d5d7c ["COPY", "register:100:1", ["const:0:1"]]
- 008d5d7c ["COPY", "register:101:1", ["const:0:1"]]
- 008d5d7c ["COPY", "register:102:1", ["const:1:1"]]
- 008d5d7c ["COPY", "register:103:1", ["const:1:1"]]
- 008d5d7c bytes 6020601e
- 008d5d80 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d5d80 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 008d5d80 ["CBRANCH", null, ["local:b16:8", "tmp:1:1"]]
- 008d5d80 bytes 88010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a53b61ed3d1afec5b386df9f232d43c"></a>

### [`008d5e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5e04.md) → [`008d5fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5fa0.md) FUN_008d5fa0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 2件 [`00a359a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a359a0.md) [`00a389f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a389f4.md)
- 新版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 2件 [`00a35b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35b98.md) [`00a38bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38bec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.42% / 新版 93.42%

CFGの説明率　旧版 24.14% / 新版 26.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5e70"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5f18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d5e70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d6058"
      ]
    ],
    [
      "unmatched:008d5eb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d60c4"
      ]
    ],
    [
      "unmatched:008d5f18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d6060"
      ]
    ]
  ],
  "added": [
    [
      "008d600c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d6058"
      ]
    ],
    [
      "008d6054",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d60c4"
      ]
    ],
    [
      "008d60b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d6060"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5e04.md#insn-008d5e70) · [`008d5eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5e04.md#insn-008d5eb8) · [`008d5ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5e04.md#insn-008d5ee8)
- 新版 `008d6084`（命令位置の公開資料なし）

~~~diff
- 008d5e70 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d5e70 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 008d5e70 ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
- 008d5e70 bytes 68020054
- 008d5eb8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d5eb8 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 008d5eb8 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 008d5eb8 ["CBRANCH", null, ["local:b19:8", "tmp:2:1"]]
- 008d5eb8 bytes 8c030054
- 008d5ee8 ["INT_ADD", "register:40f0:8", ["const:8d5ee8:8", "const:4:8"]]
- 008d5ee8 ["CALL", null, ["callee:00a38bec:8"]]
+ 008d6084 ["INT_ADD", "register:40f0:8", ["const:8d6084:8", "const:4:8"]]
+ 008d6084 ["CALL", null, ["callee:00a38bec:8"]]
- 008d5ee8 bytes c38a0594
+ 008d6084 bytes da8a0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f6a6ac9fb975df75a05c65103ca1830"></a>

### [`008d5f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5f34.md) → [`008d60d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d60d0.md) FUN_008d60d0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`00814ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00814/00814ee8.md) · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b3dfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3dfe8.md)
- 新版 呼出元 2件 [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`00814f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814f28.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b3e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3e/00b3e410.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "008d6100",
      "incomplete_value": false,
      "site": "008d6104",
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
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008d5f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5f34.md#insn-008d5f4c)
- 新版 `008d60e8`（命令位置の公開資料なし）

~~~diff
- 008d5f4c ["INT_ADD", "register:40f0:8", ["const:8d5f4c:8", "const:4:8"]]
- 008d5f4c ["CALL", null, ["callee:008514f8:8"]]
+ 008d60e8 ["INT_ADD", "register:40f0:8", ["const:8d60e8:8", "const:4:8"]]
+ 008d60e8 ["CALL", null, ["callee:008514f8:8"]]
- 008d5f4c bytes 5bedfd97
+ 008d60e8 bytes 04edfd97
~~~


<a id="compare-58fea078db5ae7ea61145a346dd5061d"></a>

### [`008d5f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5f6c.md) → [`008d6108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6108.md) FUN_008d6108

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008da608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da608.md) [`008dad0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dad0c.md) · 呼出先 3件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`008da7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da7a4.md) [`008daea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008daea8.md) · 呼出先 3件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.58% / 新版 46.58%

CFGの説明率　旧版 8.33% / 新版 8.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 50件, `unresolved_call_alignment` 27件, `unresolved_store_alignment` 48件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5fa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5fac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5fb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d5fa0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d5fac",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d5fb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x7f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008d613c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "008d6148",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "008d6150",
      "WRITE",
      [
        "storage",
        "Stack[-0x7f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5f6c.md#insn-008d5fa0) · [`008d5fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5f6c.md#insn-008d5fac) · [`008d5fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5f6c.md#insn-008d5fb4)

~~~diff
- 008d5fa0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d5fa0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008d5fa0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d5fa0 bytes a8831ff8
- 008d5fac ["COPY", "tmp:0:4", ["register:4048:4"]]
- 008d5fac ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe0:8"]]
- 008d5fac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008d5fac bytes a9031e38
- 008d5fb4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008d5fb4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe1:8"]]
- 008d5fb4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 008d5fb4 bytes a8131eb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93a51b8696b68bcc53b7487e350abec6"></a>

### [`008d6a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6a78.md) → [`008d6c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6c14.md) FUN_008d6c14

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) · 呼出先 0件 
- 新版 呼出元 1件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 61.29% / 新版 61.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-02624d159f39d08e35996aee75a0552e"></a>

### [`008d6af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6af4.md) → [`008d6c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6c90.md) FUN_008d6c90

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6af4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6af4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6af8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d6af4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d6af8",
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
      "008d6c90",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008d6c94",
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

- 旧版 [`008d6af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6af4.md#insn-008d6af4) · [`008d6af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6af4.md#insn-008d6af8) · [`008d6b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6af4.md#insn-008d6b10)
- 新版 `008d6cac`（命令位置の公開資料なし）

~~~diff
- 008d6af4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d6af4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d6af4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008d6af4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008d6af4 bytes fd7bbea9
- 008d6af8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008d6af8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008d6af8 bytes f30b00f9
- 008d6b10 ["INT_ADD", "register:40f0:8", ["const:8d6b10:8", "const:4:8"]]
- 008d6b10 ["CALL", null, ["callee:00c53d00:8"]]
+ 008d6cac ["INT_ADD", "register:40f0:8", ["const:8d6cac:8", "const:4:8"]]
+ 008d6cac ["CALL", null, ["callee:00c53d00:8"]]
- 008d6b10 bytes 74f30d94
+ 008d6cac bytes 15f40d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cf94a227d1994adbc78fa2c67fc4e34"></a>

### [`008d6b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md) → [`008d6ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md) FUN_008d6ce0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 19件 [`0044b764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b764.md) [`005618ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/005618ac.md) [`00561ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561ae4.md) [`00561cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cac.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md)
- 新版 呼出元 1件 [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 19件 [`0044b7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b7a4.md) [`005618ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md) [`00561b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md) [`00561cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561cec.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 25.84% / 新版 29.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6b48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6b48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6b4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d6b48",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d6b4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d6b50",
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
      "008d6ce4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008d6ce8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008d6cec",
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

- 旧版 [`008d6b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md#insn-008d6b48) · [`008d6b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md#insn-008d6b4c) · [`008d6b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md#insn-008d6b50)

~~~diff
- 008d6b48 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d6b48 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d6b48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 008d6b48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d6b48 bytes fd7b0ea9
- 008d6b4c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:f0:8"]]
- 008d6b4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 008d6b4c bytes fc7b00f9
- 008d6b50 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008d6b50 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008d6b50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 008d6b50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d6b50 bytes f65710a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ebd1c7e5615ccf4f7d151aa4212c770"></a>

### [`008d7058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7058.md) → [`008d71f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d71f4.md) FUN_008d71f4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 18件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 18件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.60% / 新版 86.60%

CFGの説明率　旧版 65.00% / 新版 67.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 1件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 16件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7058"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7058"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d705c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d7058",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d705c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d7060",
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
      "008d71f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d71f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008d71fc",
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

- 旧版 [`008d7058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7058.md#insn-008d7058) · [`008d705c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7058.md#insn-008d705c) · [`008d7060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7058.md#insn-008d7060)

~~~diff
- 008d7058 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d7058 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d7058 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 008d7058 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008d7058 bytes fd7bbaa9
- 008d705c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008d705c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008d705c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008d705c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d705c bytes fc6f01a9
- 008d7060 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008d7060 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008d7060 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008d7060 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d7060 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a240d480a1ecd15a7c152016d971803"></a>

### [`008d754c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d754c.md) → [`008d76e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d76e8.md) FUN_008d76e8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007c7eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7eb0.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) · 呼出先 6件 [`008d809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d809c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 6件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007c7ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7ef0.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 6件 [`008d8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8238.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.18% / 新版 81.18%

CFGの説明率　旧版 50.00% / 新版 48.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7550"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7550"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7554"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d7550",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d7554",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d7558",
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
      "008d76ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d76f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008d76f4",
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

- 旧版 [`008d7550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d754c.md#insn-008d7550) · [`008d7554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d754c.md#insn-008d7554) · [`008d7558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d754c.md#insn-008d7558)

~~~diff
- 008d7550 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d7550 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d7550 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008d7550 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d7550 bytes fd7b04a9
- 008d7554 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008d7554 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008d7554 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 008d7554 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d7554 bytes fc6f05a9
- 008d7558 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008d7558 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008d7558 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 008d7558 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d7558 bytes fa6706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75e3e3cdbd2f0c6f77c2ae91ef52df48"></a>

### [`008d77f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d77f4.md) → [`008d7990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d7990.md) FUN_008d7990

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008d98a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d98a4.md) · 呼出先 9件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008783b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008783b0.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md)
- 新版 呼出元 1件 [`008d9a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9a40.md) · 呼出先 9件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008783f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.41% / 新版 72.41%

CFGの説明率　旧版 3.49% / 新版 3.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 2件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d780c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d7808",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d780c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d7830",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008d79a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008d79a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d79cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d7808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d77f4.md#insn-008d7808) · [`008d780c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d77f4.md#insn-008d780c) · [`008d7830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d77f4.md#insn-008d7830)

~~~diff
- 008d7808 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008d7808 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008d7808 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 008d7808 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d7808 bytes f65712a9
- 008d780c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008d780c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008d780c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 008d780c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d780c bytes f44f13a9
- 008d7830 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d7830 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 008d7830 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d7830 bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-819d15e09aaa37abb3ed95de81777a0b"></a>

### [`008d7d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7d40.md) → [`008d7edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d7edc.md) FUN_008d7edc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008d7fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7fb8.md) · 呼出先 3件 [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`008d8154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8154.md) · 呼出先 3件 [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.86% / 新版 58.86%

CFGの説明率　旧版 21.13% / 新版 22.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7d5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7f78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d7ef8"
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
      "unmatched:008d7d5c",
      "DATA",
      [
        "storage",
        "00c841b8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d7d70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7f28"
      ]
    ],
    [
      "008d7f5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008d7dec"
      ]
    ]
  ],
  "added": [
    [
      "008d7ef8",
      "DATA",
      [
        "storage",
        "00c845b8",
        null,
        "undefined *"
      ]
    ],
    [
      "008d7f0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7f28"
      ]
    ],
    [
      "008d7f5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7f88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d7d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7d40.md#insn-008d7d5c) · [`008d7d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7d40.md#insn-008d7d70) · [`008d7db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7d40.md#insn-008d7db0)

~~~diff
- 008d7d5c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008d7d5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d7d5c bytes 080000f9
- 008d7d70 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008d7d70 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008d7d70 bytes e00000b5
- 008d7db0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008d7db0 ["INT_ADD", "register:40f0:8", ["const:8d7db0:8", "const:4:8"]]
- 008d7db0 ["CALLIND", null, ["register:0:8"]]
- 008d7db0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dec3b773741c88d5a3a786d49fa6310"></a>

### [`008d7fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7fb8.md) → [`008d8154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8154.md) FUN_008d8154

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`008d7d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7d40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008d7edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d7edc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008d7fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7fb8.md#insn-008d7fc8)
- 新版 `008d8164`（命令位置の公開資料なし）

~~~diff
- 008d7fc8 ["INT_ADD", "register:40f0:8", ["const:8d7fc8:8", "const:4:8"]]
- 008d7fc8 ["CALL", null, ["callee:008d7edc:8"]]
+ 008d8164 ["INT_ADD", "register:40f0:8", ["const:8d8164:8", "const:4:8"]]
+ 008d8164 ["CALL", null, ["callee:008d7edc:8"]]
- 008d7fc8 bytes 5effff97
+ 008d8164 bytes 5effff97
~~~


<a id="compare-8fb4ae10712ce5339c3d607296fa38e2"></a>

### [`008d7fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7fdc.md) → [`008d8178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8178.md) FUN_008d8178

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8190",
      "incomplete_value": false,
      "site": "008d8194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d7ff4",
      "incomplete_value": false,
      "site": "008d7ff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008d801c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "008d81b8"
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
      "008d8194",
      "DATA",
      [
        "storage",
        "00c84208",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008d801c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008d8194",
      "DATA",
      [
        "storage",
        "00c84608",
        null,
        "pointer"
      ]
    ],
    [
      "008d81b8",
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

- 旧版 [`008d801c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7fdc.md#insn-008d801c) · [`008d7ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7fdc.md#insn-008d7ff4)
- 新版 `008d81b8`（命令位置の公開資料なし） · `008d8190`（命令位置の公開資料なし）

~~~diff
- 008d801c ["COPY", "register:0:8", ["register:4040:8"]]
- 008d801c ["INT_ADD", "register:40f0:8", ["const:8d801c:8", "const:4:8"]]
- 008d801c ["CALLIND", null, ["register:0:8"]]
- 008d801c bytes 00013fd6
+ 008d81b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008d81b8 ["INT_ADD", "register:40f0:8", ["const:8d81b8:8", "const:4:8"]]
+ 008d81b8 ["CALLIND", null, ["register:0:8"]]
+ 008d81b8 bytes 00013fd6
- 008d7ff4 ["COPY", "tmp:0:8", ["const:208:8"]]
- 008d7ff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d7ff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d7ff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8190 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 008d8190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d7ff4 bytes 08210891
+ 008d8190 bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-701685649565109e1191985f8031670b"></a>

### [`008d8038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8038.md) → [`008d81d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d81d4.md) FUN_008d81d4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 68.00% / 新版 68.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d803c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d8038",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d803c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d8054",
      "DATA",
      [
        "storage",
        "00c84208",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d81d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008d81d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d81f0",
      "DATA",
      [
        "storage",
        "00c84608",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8038.md#insn-008d8038) · [`008d803c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8038.md#insn-008d803c) · [`008d8054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8038.md#insn-008d8054)

~~~diff
- 008d8038 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d8038 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d8038 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008d8038 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008d8038 bytes fd7bbea9
- 008d803c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008d803c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008d803c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008d803c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d803c bytes f44f01a9
- 008d8054 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008d8054 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d8054 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a5293da20b685bbabe6255b8754bd7a"></a>

### [`008d809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d809c.md) → [`008d8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8238.md) FUN_008d8238

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`008d299c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d299c.md) [`008d4bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d4/008d4bc0.md) [`008d7058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7058.md) [`008d754c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d754c.md) [`008d80b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d80b0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 7件 [`008d2b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2b38.md) [`008d4d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d4/008d4d5c.md) [`008d71f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d71f4.md) [`008d76e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d76e8.md) [`008d824c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d824c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "008d8244",
      "incomplete_value": false,
      "site": "008d8248",
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
      "definition_site": "008d80a8",
      "incomplete_value": false,
      "site": "008d80ac",
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
      "008d8244",
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
      "008d8244",
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

- 旧版 [`008d80ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d809c.md#insn-008d80ac) · [`008d80a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d809c.md#insn-008d80a8)
- 新版 `008d8248`（命令位置の公開資料なし） · `008d8244`（命令位置の公開資料なし）

~~~diff
- 008d80ac ["INT_ADD", "register:40f0:8", ["const:8d80ac:8", "const:4:8"]]
- 008d80ac ["CALL", null, ["callee:0043b778:8"]]
+ 008d8248 ["INT_ADD", "register:40f0:8", ["const:8d8248:8", "const:4:8"]]
+ 008d8248 ["CALL", null, ["callee:0043b778:8"]]
- 008d80ac bytes a38ded97
+ 008d8248 bytes 4c8ded97
- 008d80a8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 008d80a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d80a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d80a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d8244 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 008d8244 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d8244 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d8244 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d80a8 bytes 00303c91
+ 008d8244 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2bfaaa6f9531a87d2ad2bda679e967a"></a>

### [`008d8218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8218.md) → [`008d83b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d83b4.md) FUN_008d83b4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008d83d8",
      "incomplete_value": false,
      "site": "008d83d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d823c",
      "incomplete_value": false,
      "site": "008d823c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "008d83d8",
      "DATA",
      [
        "storage",
        "00c84228",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d83d8",
      "DATA",
      [
        "storage",
        "00c84628",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d822c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8218.md#insn-008d822c) · [`008d8238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8218.md#insn-008d8238)
- 新版 `008d83c8`（命令位置の公開資料なし） · `008d83d4`（命令位置の公開資料なし）

~~~diff
- 008d822c ["INT_ADD", "register:40f0:8", ["const:8d822c:8", "const:4:8"]]
- 008d822c ["CALL", null, ["callee:00c57e90:8"]]
+ 008d83c8 ["INT_ADD", "register:40f0:8", ["const:8d83c8:8", "const:4:8"]]
+ 008d83c8 ["CALL", null, ["callee:00c57e90:8"]]
- 008d822c bytes 19fe0d94
+ 008d83c8 bytes b2fe0d94
- 008d8238 ["COPY", "tmp:0:8", ["const:228:8"]]
- 008d8238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d83d4 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 008d83d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d83d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d83d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8238 bytes 08a10891
+ 008d83d4 bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15d41c43805ca084a87c79d66bea0262"></a>

### [`008d824c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d824c.md) → [`008d83e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d83e8.md) FUN_008d83e8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d83f4",
      "incomplete_value": false,
      "site": "008d83f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8258",
      "incomplete_value": false,
      "site": "008d8258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "008d83f4",
      "DATA",
      [
        "storage",
        "00c84228",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d83f4",
      "DATA",
      [
        "storage",
        "00c84628",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d824c.md#insn-008d8254)
- 新版 `008d83f0`（命令位置の公開資料なし）

~~~diff
- 008d8254 ["COPY", "tmp:0:8", ["const:228:8"]]
- 008d8254 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d8254 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d8254 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d83f0 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 008d83f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d83f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d83f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d8254 bytes 29a10891
+ 008d83f0 bytes 29a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-415a5b50a198dc7d34693133c9d92f48"></a>

### [`008d8268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8268.md) → [`008d8404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8404.md) FUN_008d8404

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md) [`008d83d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d83d4.md) [`008d83d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d83d8.md) [`00aca9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca9d8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md) [`008d8570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8570.md) [`008d8574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8574.md) [`00acabd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acabd4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8438",
      "incomplete_value": false,
      "site": "008d8438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d829c",
      "incomplete_value": false,
      "site": "008d829c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "008d8438",
      "DATA",
      [
        "storage",
        "00c84298",
        null,
        "undefined *"
      ]
    ],
    [
      "008d8470",
      "READ",
      [
        "storage",
        "00c842b8",
        null,
        "pointer"
      ]
    ],
    [
      "008d8470",
      "READ",
      [
        "storage",
        "00c842c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8438",
      "DATA",
      [
        "storage",
        "00c84698",
        null,
        "undefined *"
      ]
    ],
    [
      "008d8470",
      "READ",
      [
        "storage",
        "00c846b8",
        null,
        "pointer"
      ]
    ],
    [
      "008d8470",
      "READ",
      [
        "storage",
        "00c846c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8268.md#insn-008d8290) · [`008d82ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8268.md#insn-008d82ac) · [`008d82d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8268.md#insn-008d82d8)
- 新版 `008d842c`（命令位置の公開資料なし） · `008d8448`（命令位置の公開資料なし） · `008d8474`（命令位置の公開資料なし）

~~~diff
- 008d8290 ["COPY", "tmp:0:8", ["const:298:8"]]
- 008d8290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d842c ["COPY", "tmp:0:8", ["const:698:8"]]
+ 008d842c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d842c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d842c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8290 bytes 08610a91
+ 008d842c bytes 08611a91
- 008d82ac ["INT_ADD", "register:40f0:8", ["const:8d82ac:8", "const:4:8"]]
- 008d82ac ["CALL", null, ["callee:00acabd4:8"]]
+ 008d8448 ["INT_ADD", "register:40f0:8", ["const:8d8448:8", "const:4:8"]]
+ 008d8448 ["CALL", null, ["callee:00acabd4:8"]]
- 008d82ac bytes cbc90794
+ 008d8448 bytes e3c90794
- 008d82d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008d82d8 ["INT_ADD", "register:40f0:8", ["const:8d82d8:8", "const:4:8"]]
- 008d82d8 ["CALLIND", null, ["register:0:8"]]
+ 008d8474 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008d8474 ["INT_ADD", "register:40f0:8", ["const:8d8474:8", "const:4:8"]]
+ 008d8474 ["CALLIND", null, ["register:0:8"]]
- 008d82d8 bytes 00013fd6
+ 008d8474 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-559c2430047b8c36b22b3777e1e18672"></a>

### [`008d838c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d838c.md) → [`008d8528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8528.md) FUN_008d8528

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008d854c",
      "incomplete_value": false,
      "site": "008d854c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d83b0",
      "incomplete_value": false,
      "site": "008d83b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "008d854c",
      "DATA",
      [
        "storage",
        "00c84298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d854c",
      "DATA",
      [
        "storage",
        "00c84698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d83a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d838c.md#insn-008d83a0) · [`008d83ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d838c.md#insn-008d83ac)
- 新版 `008d853c`（命令位置の公開資料なし） · `008d8548`（命令位置の公開資料なし）

~~~diff
- 008d83a0 ["INT_ADD", "register:40f0:8", ["const:8d83a0:8", "const:4:8"]]
- 008d83a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 008d853c ["INT_ADD", "register:40f0:8", ["const:8d853c:8", "const:4:8"]]
+ 008d853c ["CALL", null, ["callee:00c57e90:8"]]
- 008d83a0 bytes bcfd0d94
+ 008d853c bytes 55fe0d94
- 008d83ac ["COPY", "tmp:0:8", ["const:298:8"]]
- 008d83ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d83ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d83ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8548 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 008d8548 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8548 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8548 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d83ac bytes 08610a91
+ 008d8548 bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-349f16971454085016abe42f0d91ae82"></a>

### [`008d83c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d83c0.md) → [`008d855c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d855c.md) FUN_008d855c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d8568",
      "incomplete_value": false,
      "site": "008d8568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d83cc",
      "incomplete_value": false,
      "site": "008d83cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "008d8568",
      "DATA",
      [
        "storage",
        "00c84298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8568",
      "DATA",
      [
        "storage",
        "00c84698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d83c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d83c0.md#insn-008d83c8)
- 新版 `008d8564`（命令位置の公開資料なし）

~~~diff
- 008d83c8 ["COPY", "tmp:0:8", ["const:298:8"]]
- 008d83c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d83c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d83c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d8564 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 008d8564 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8564 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8564 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d83c8 bytes 29610a91
+ 008d8564 bytes 29611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b498cb565d56dca53021a62a8f11fe06"></a>

### [`008d83dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d83dc.md) → [`008d8578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8578.md) FUN_008d8578

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00756264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00756/00756264.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7950.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md) [`00ac8440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8440.md)
- 新版 呼出元 0件  · 呼出先 6件 [`007562a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00756/007562a4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b7994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7994.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md) [`00ac863c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac863c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.23% / 新版 89.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008d85f8",
      "incomplete_value": false,
      "site": "008d85f8",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d845c",
      "incomplete_value": false,
      "site": "008d845c",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d85ec",
      "incomplete_value": true,
      "site": "008d85f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
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
      "definition_site": "008d8450",
      "incomplete_value": true,
      "site": "008d845c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008d85fc",
      "incomplete_value": false,
      "site": "008d85fc",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8460",
      "incomplete_value": false,
      "site": "008d8460",
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
            "const:578:8"
          ]
        ]
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
      "008d85ec",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008d85f0",
      "READ",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "008d85f8",
      "WRITE",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008d85ec",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008d85f0",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "008d85f8",
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d845c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d83dc.md#insn-008d845c) · [`008d8460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d83dc.md#insn-008d8460) · [`008d847c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d83dc.md#insn-008d847c)
- 新版 `008d85f8`（命令位置の公開資料なし） · `008d85fc`（命令位置の公開資料なし） · `008d8618`（命令位置の公開資料なし）

~~~diff
- 008d845c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 008d845c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008d85f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
+ 008d85f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008d845c bytes 09b502f9
+ 008d85f8 bytes 09b504f9
- 008d8460 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:578:8"]]
- 008d8460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008d85fc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:978:8"]]
+ 008d85fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008d8460 bytes eabe02f9
+ 008d85fc bytes eabe04f9
- 008d847c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:578:8"]]
- 008d847c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008d8618 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:978:8"]]
+ 008d8618 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008d847c bytes f4be02f9
+ 008d8618 bytes f4be04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c30fa61a3dfbb0947b017126a6220e1"></a>

### [`008d8520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8520.md) → [`008d86bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d86bc.md) FUN_008d86bc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008d86e0",
      "incomplete_value": false,
      "site": "008d86e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8544",
      "incomplete_value": false,
      "site": "008d8544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "008d86e0",
      "DATA",
      [
        "storage",
        "00c84328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d86e0",
      "DATA",
      [
        "storage",
        "00c84728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8520.md#insn-008d8534) · [`008d8540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8520.md#insn-008d8540)
- 新版 `008d86d0`（命令位置の公開資料なし） · `008d86dc`（命令位置の公開資料なし）

~~~diff
- 008d8534 ["INT_ADD", "register:40f0:8", ["const:8d8534:8", "const:4:8"]]
- 008d8534 ["CALL", null, ["callee:00c57e90:8"]]
+ 008d86d0 ["INT_ADD", "register:40f0:8", ["const:8d86d0:8", "const:4:8"]]
+ 008d86d0 ["CALL", null, ["callee:00c57e90:8"]]
- 008d8534 bytes 57fd0d94
+ 008d86d0 bytes f0fd0d94
- 008d8540 ["COPY", "tmp:0:8", ["const:328:8"]]
- 008d8540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d86dc ["COPY", "tmp:0:8", ["const:728:8"]]
+ 008d86dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d86dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d86dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8540 bytes 08a10c91
+ 008d86dc bytes 08a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7173429d8dd870e6437618bb96e1b1f"></a>

### [`008d8554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8554.md) → [`008d86f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d86f0.md) FUN_008d86f0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d86fc",
      "incomplete_value": false,
      "site": "008d86fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8560",
      "incomplete_value": false,
      "site": "008d8560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "008d86fc",
      "DATA",
      [
        "storage",
        "00c84328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d86fc",
      "DATA",
      [
        "storage",
        "00c84728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d855c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8554.md#insn-008d855c)
- 新版 `008d86f8`（命令位置の公開資料なし）

~~~diff
- 008d855c ["COPY", "tmp:0:8", ["const:328:8"]]
- 008d855c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d855c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d855c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d86f8 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 008d86f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d86f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d86f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d855c bytes 29a10c91
+ 008d86f8 bytes 29a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-384141c7c794838f80499cba80c8be69"></a>

### [`008d8630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8630.md) → [`008d87cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d87cc.md) FUN_008d87cc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008d87f0",
      "incomplete_value": false,
      "site": "008d87f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8654",
      "incomplete_value": false,
      "site": "008d8654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
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
      "008d87f0",
      "DATA",
      [
        "storage",
        "00c843a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d87f0",
      "DATA",
      [
        "storage",
        "00c847a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8630.md#insn-008d8644) · [`008d8650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8630.md#insn-008d8650)
- 新版 `008d87e0`（命令位置の公開資料なし） · `008d87ec`（命令位置の公開資料なし）

~~~diff
- 008d8644 ["INT_ADD", "register:40f0:8", ["const:8d8644:8", "const:4:8"]]
- 008d8644 ["CALL", null, ["callee:00c57e90:8"]]
+ 008d87e0 ["INT_ADD", "register:40f0:8", ["const:8d87e0:8", "const:4:8"]]
+ 008d87e0 ["CALL", null, ["callee:00c57e90:8"]]
- 008d8644 bytes 13fd0d94
+ 008d87e0 bytes acfd0d94
- 008d8650 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 008d8650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d87ec ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 008d87ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d87ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d87ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8650 bytes 08a10e91
+ 008d87ec bytes 08a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99ee53dd966c7b84979dce7c1941dcdb"></a>

### [`008d8664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8664.md) → [`008d8800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8800.md) FUN_008d8800

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d880c",
      "incomplete_value": false,
      "site": "008d880c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8670",
      "incomplete_value": false,
      "site": "008d8670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
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
      "008d880c",
      "DATA",
      [
        "storage",
        "00c843a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d880c",
      "DATA",
      [
        "storage",
        "00c847a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d866c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8664.md#insn-008d866c)
- 新版 `008d8808`（命令位置の公開資料なし）

~~~diff
- 008d866c ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 008d866c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d866c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d866c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d8808 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 008d8808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d866c bytes 29a10e91
+ 008d8808 bytes 29a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1acece1872a86f82c5d0803919e786dc"></a>

### [`008d8680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8680.md) → [`008d881c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d881c.md) FUN_008d881c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8900",
      "incomplete_value": true,
      "site": "008d8914",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:baa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8764",
      "incomplete_value": true,
      "site": "008d8778",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:b6a:8"
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
      "definition_site": "008d892c",
      "incomplete_value": false,
      "site": "008d8934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8790",
      "incomplete_value": false,
      "site": "008d8798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d8854",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d86b8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "008d8854",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008d8870",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008d88c0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "008d8854",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008d8870",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008d88c0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d86b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8680.md#insn-008d86b8) · [`008d86d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8680.md#insn-008d86d4) · [`008d8708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8680.md#insn-008d8708)
- 新版 `008d8854`（命令位置の公開資料なし） · `008d8870`（命令位置の公開資料なし） · `008d88a4`（命令位置の公開資料なし）

~~~diff
- 008d86b8 ["INT_ADD", "register:40f0:8", ["const:8d86b8:8", "const:4:8"]]
- 008d86b8 ["CALL", null, ["ram:47acb4:8"]]
+ 008d8854 ["INT_ADD", "register:40f0:8", ["const:8d8854:8", "const:4:8"]]
+ 008d8854 ["CALL", null, ["ram:47acf4:8"]]
- 008d86b8 bytes 7f89ee97
+ 008d8854 bytes 2889ee97
- 008d86d4 ["INT_ADD", "register:40f0:8", ["const:8d86d4:8", "const:4:8"]]
- 008d86d4 ["CALL", null, ["ram:47acb4:8"]]
+ 008d8870 ["INT_ADD", "register:40f0:8", ["const:8d8870:8", "const:4:8"]]
+ 008d8870 ["CALL", null, ["ram:47acf4:8"]]
- 008d86d4 bytes 7889ee97
+ 008d8870 bytes 2189ee97
- 008d8708 ["INT_ADD", "register:40f0:8", ["const:8d8708:8", "const:4:8"]]
- 008d8708 ["CALL", null, ["callee:0048ce50:8"]]
+ 008d88a4 ["INT_ADD", "register:40f0:8", ["const:8d88a4:8", "const:4:8"]]
+ 008d88a4 ["CALL", null, ["callee:0048ce50:8"]]
- 008d8708 bytes c2d1ee97
+ 008d88a4 bytes 6bd1ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7408d8cbdb75945d6dec3c19ced53c13"></a>

### [`008d88f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d88f0.md) → [`008d8a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8a8c.md) FUN_008d8a8c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008d8aa0",
      "incomplete_value": false,
      "site": "008d8aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8904",
      "incomplete_value": false,
      "site": "008d8908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "008d8aa4",
      "DATA",
      [
        "storage",
        "00c84418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8aa4",
      "DATA",
      [
        "storage",
        "00c84818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d88fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d88f0.md#insn-008d88fc) · [`008d8904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d88f0.md#insn-008d8904)
- 新版 `008d8a98`（命令位置の公開資料なし） · `008d8aa0`（命令位置の公開資料なし）

~~~diff
- 008d88fc ["INT_ADD", "register:40f0:8", ["const:8d88fc:8", "const:4:8"]]
- 008d88fc ["CALL", null, ["callee:00c57e90:8"]]
+ 008d8a98 ["INT_ADD", "register:40f0:8", ["const:8d8a98:8", "const:4:8"]]
+ 008d8a98 ["CALL", null, ["callee:00c57e90:8"]]
- 008d88fc bytes 65fc0d94
+ 008d8a98 bytes fefc0d94
- 008d8904 ["COPY", "tmp:0:8", ["const:418:8"]]
- 008d8904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8aa0 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 008d8aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8904 bytes 08611091
+ 008d8aa0 bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52be4e0ccc93b152c4acacfebf12d911"></a>

### [`008d8914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8914.md) → [`008d8ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8ab0.md) FUN_008d8ab0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d8ab4",
      "incomplete_value": false,
      "site": "008d8ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8918",
      "incomplete_value": false,
      "site": "008d891c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "008d8ab8",
      "DATA",
      [
        "storage",
        "00c84418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8ab8",
      "DATA",
      [
        "storage",
        "00c84818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8914.md#insn-008d8918)
- 新版 `008d8ab4`（命令位置の公開資料なし）

~~~diff
- 008d8918 ["COPY", "tmp:0:8", ["const:418:8"]]
- 008d8918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8ab4 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 008d8ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8918 bytes 08611091
+ 008d8ab4 bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aeb1adf29758c6ac9e00cee96ed5b3f"></a>

### [`008d8970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8970.md) → [`008d8b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b0c.md) FUN_008d8b0c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008d8b30",
      "incomplete_value": false,
      "site": "008d8b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8994",
      "incomplete_value": false,
      "site": "008d8994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
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
      "008d8b30",
      "DATA",
      [
        "storage",
        "00c844a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8b30",
      "DATA",
      [
        "storage",
        "00c848a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8970.md#insn-008d8984) · [`008d8990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8970.md#insn-008d8990)
- 新版 `008d8b20`（命令位置の公開資料なし） · `008d8b2c`（命令位置の公開資料なし）

~~~diff
- 008d8984 ["INT_ADD", "register:40f0:8", ["const:8d8984:8", "const:4:8"]]
- 008d8984 ["CALL", null, ["callee:00c57e90:8"]]
+ 008d8b20 ["INT_ADD", "register:40f0:8", ["const:8d8b20:8", "const:4:8"]]
+ 008d8b20 ["CALL", null, ["callee:00c57e90:8"]]
- 008d8984 bytes 43fc0d94
+ 008d8b20 bytes dcfc0d94
- 008d8990 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 008d8990 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8990 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8990 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8b2c ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 008d8b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8990 bytes 08a11291
+ 008d8b2c bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-535c0e21aafbdd40919ec5ebfef14b36"></a>

### [`008d89a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d89a4.md) → [`008d8b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b40.md) FUN_008d8b40

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d8b4c",
      "incomplete_value": false,
      "site": "008d8b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d89b0",
      "incomplete_value": false,
      "site": "008d89b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
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
      "008d8b4c",
      "DATA",
      [
        "storage",
        "00c844a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8b4c",
      "DATA",
      [
        "storage",
        "00c848a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d89ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d89a4.md#insn-008d89ac)
- 新版 `008d8b48`（命令位置の公開資料なし）

~~~diff
- 008d89ac ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 008d89ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d89ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d89ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d8b48 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 008d8b48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8b48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8b48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d89ac bytes 29a11291
+ 008d8b48 bytes 29a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c44a0383e0dcf0cc63367a34644bdd73"></a>

### [`008d89c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d89c0.md) → [`008d8b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b5c.md) FUN_008d8b5c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008d5008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5008.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008d51a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d51a4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "008d8b7c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d89e0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "008d8b88",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d89ec",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "008d8b7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008d8b88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008d8b7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008d8b88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d89e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d89c0.md#insn-008d89e0) · [`008d89ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d89c0.md#insn-008d89ec)
- 新版 `008d8b7c`（命令位置の公開資料なし） · `008d8b88`（命令位置の公開資料なし）

~~~diff
- 008d89e0 ["INT_ADD", "register:40f0:8", ["const:8d89e0:8", "const:4:8"]]
- 008d89e0 ["CALL", null, ["ram:47acb4:8"]]
+ 008d8b7c ["INT_ADD", "register:40f0:8", ["const:8d8b7c:8", "const:4:8"]]
+ 008d8b7c ["CALL", null, ["ram:47acf4:8"]]
- 008d89e0 bytes b588ee97
+ 008d8b7c bytes 5e88ee97
- 008d89ec ["INT_ADD", "register:40f0:8", ["const:8d89ec:8", "const:4:8"]]
- 008d89ec ["CALL", null, ["ram:47acb4:8"]]
+ 008d8b88 ["INT_ADD", "register:40f0:8", ["const:8d8b88:8", "const:4:8"]]
+ 008d8b88 ["CALL", null, ["ram:47acf4:8"]]
- 008d89ec bytes b288ee97
+ 008d8b88 bytes 5b88ee97
~~~


<a id="compare-0dc5850b51781500f47a59d1e41e4f53"></a>

### [`008d8a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a44.md) → [`008d8be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8be0.md) FUN_008d8be0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008d8c04",
      "incomplete_value": false,
      "site": "008d8c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8a68",
      "incomplete_value": false,
      "site": "008d8a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "008d8c04",
      "DATA",
      [
        "storage",
        "00c84528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8c04",
      "DATA",
      [
        "storage",
        "00c84928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a44.md#insn-008d8a58) · [`008d8a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a44.md#insn-008d8a64)
- 新版 `008d8bf4`（命令位置の公開資料なし） · `008d8c00`（命令位置の公開資料なし）

~~~diff
- 008d8a58 ["INT_ADD", "register:40f0:8", ["const:8d8a58:8", "const:4:8"]]
- 008d8a58 ["CALL", null, ["callee:00c57e90:8"]]
+ 008d8bf4 ["INT_ADD", "register:40f0:8", ["const:8d8bf4:8", "const:4:8"]]
+ 008d8bf4 ["CALL", null, ["callee:00c57e90:8"]]
- 008d8a58 bytes 0efc0d94
+ 008d8bf4 bytes a7fc0d94
- 008d8a64 ["COPY", "tmp:0:8", ["const:528:8"]]
- 008d8a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8c00 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 008d8c00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8c00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8c00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8a64 bytes 08a11491
+ 008d8c00 bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b01a2508f7597284780d0c24444d3e2"></a>

### [`008d8a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a78.md) → [`008d8c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8c14.md) FUN_008d8c14

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d8c20",
      "incomplete_value": false,
      "site": "008d8c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8a84",
      "incomplete_value": false,
      "site": "008d8a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "008d8c20",
      "DATA",
      [
        "storage",
        "00c84528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8c20",
      "DATA",
      [
        "storage",
        "00c84928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a78.md#insn-008d8a80)
- 新版 `008d8c1c`（命令位置の公開資料なし）

~~~diff
- 008d8a80 ["COPY", "tmp:0:8", ["const:528:8"]]
- 008d8a80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d8a80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d8a80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d8c1c ["COPY", "tmp:0:8", ["const:928:8"]]
+ 008d8c1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8c1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8c1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d8a80 bytes 29a11491
+ 008d8c1c bytes 29a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0ff5c5fdcf4df900962aa59e23c4775"></a>

### [`008d8a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a94.md) → [`008d8c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8c30.md) FUN_008d8c30

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00597604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597604.md) [`008b6e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e14.md) [`008b6e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e1c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00597644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597644.md) [`008b6e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6e58.md) [`008b6e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6e60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.16% / 新版 78.16%

CFGの説明率　旧版 72.73% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8a98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8a98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8a9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d8a98",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d8a9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d8aa0",
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
      "008d8c34",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008d8c38",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008d8c3c",
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

- 旧版 [`008d8a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a94.md#insn-008d8a98) · [`008d8a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a94.md#insn-008d8a9c) · [`008d8aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a94.md#insn-008d8aa0)

~~~diff
- 008d8a98 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d8a98 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d8a98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008d8a98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d8a98 bytes fd7b04a9
- 008d8a9c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 008d8a9c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 008d8a9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 008d8a9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d8a9c bytes f85f05a9
- 008d8aa0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008d8aa0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008d8aa0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 008d8aa0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d8aa0 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b354ebdf8620e5fce03f670ecfd463b"></a>

### [`008d8ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8ca8.md) → [`008d8e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e44.md) FUN_008d8e44

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d8e48",
      "incomplete_value": false,
      "site": "008d8e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8cac",
      "incomplete_value": false,
      "site": "008d8cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:598:8"
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
      "008d8e4c",
      "DATA",
      [
        "storage",
        "00c84598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8e4c",
      "DATA",
      [
        "storage",
        "00c84998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8ca8.md#insn-008d8cac)
- 新版 `008d8e48`（命令位置の公開資料なし）

~~~diff
- 008d8cac ["COPY", "tmp:0:8", ["const:598:8"]]
- 008d8cac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8cac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8cac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8e48 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 008d8e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8cac bytes 08611691
+ 008d8e48 bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b09d0813066b2e56439cb3fbf922637d"></a>

### [`008d8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md) → [`008d8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e6c.md) FUN_008d8e6c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 22件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca14.md) [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca54.md) [`0046cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.34% / 新版 81.34%

CFGの説明率　旧版 46.58% / 新版 45.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8cd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8cd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8cd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d8cd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d8cd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d8cdc",
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
      "008d8e70",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d8e74",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008d8e78",
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

- 旧版 [`008d8cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md#insn-008d8cd4) · [`008d8cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md#insn-008d8cd8) · [`008d8cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md#insn-008d8cdc)

~~~diff
- 008d8cd4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d8cd4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d8cd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 008d8cd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d8cd4 bytes fd7b0ba9
- 008d8cd8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008d8cd8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008d8cd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 008d8cd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d8cd8 bytes fc6f0ca9
- 008d8cdc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008d8cdc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008d8cdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 008d8cdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d8cdc bytes fa670da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70dace2ec33ea27ed4b5a48a602cef5c"></a>

### [`008d92a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d92a8.md) → [`008d9444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9444.md) FUN_008d9444

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d9448",
      "incomplete_value": false,
      "site": "008d944c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d92ac",
      "incomplete_value": false,
      "site": "008d92b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "008d944c",
      "DATA",
      [
        "storage",
        "00c84608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d944c",
      "DATA",
      [
        "storage",
        "00c84a08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d92ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d92a8.md#insn-008d92ac)
- 新版 `008d9448`（命令位置の公開資料なし）

~~~diff
- 008d92ac ["COPY", "tmp:0:8", ["const:608:8"]]
- 008d92ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d92ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d92ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9448 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 008d9448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d92ac bytes 08211891
+ 008d9448 bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a2eb237fa4df2a419ce1718e82f2cb1"></a>

### [`008d937c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d937c.md) → [`008d9518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9518.md) FUN_008d9518

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d9524",
      "incomplete_value": false,
      "site": "008d9524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d9388",
      "incomplete_value": false,
      "site": "008d9388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "008d9524",
      "DATA",
      [
        "storage",
        "00c846a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9524",
      "DATA",
      [
        "storage",
        "00c84aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d937c.md#insn-008d9384)
- 新版 `008d9520`（命令位置の公開資料なし）

~~~diff
- 008d9384 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 008d9384 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d9384 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d9384 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d9520 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 008d9520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d9520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d9520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d9384 bytes 29a11a91
+ 008d9520 bytes 29a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e308a058974f2b0a1589f6bd0ac5c9bc"></a>

### [`008d9398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9398.md) → [`008d9534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9534.md) FUN_008d9534

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md) [`008d9568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9568.md) [`008d956c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d956c.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md) [`008d9704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9704.md) [`008d9708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9708.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.76% / 新版 86.76%

CFGの説明率　旧版 78.26% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d942c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d942c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9430"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d956c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008d9588",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:008d942c",
      "DATA",
      [
        "storage",
        "00c84718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d956c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008d9588",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008d95c8",
      "DATA",
      [
        "storage",
        "00c84b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d93d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9398.md#insn-008d93d0) · [`008d93ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9398.md#insn-008d93ec) · [`008d942c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9398.md#insn-008d942c)
- 新版 `008d956c`（命令位置の公開資料なし） · `008d9588`（命令位置の公開資料なし）

~~~diff
- 008d93d0 ["INT_ADD", "register:40f0:8", ["const:8d93d0:8", "const:4:8"]]
- 008d93d0 ["CALL", null, ["ram:47acb4:8"]]
+ 008d956c ["INT_ADD", "register:40f0:8", ["const:8d956c:8", "const:4:8"]]
+ 008d956c ["CALL", null, ["ram:47acf4:8"]]
- 008d93d0 bytes 3986ee97
+ 008d956c bytes e285ee97
- 008d93ec ["INT_ADD", "register:40f0:8", ["const:8d93ec:8", "const:4:8"]]
- 008d93ec ["CALL", null, ["ram:47acb4:8"]]
+ 008d9588 ["INT_ADD", "register:40f0:8", ["const:8d9588:8", "const:4:8"]]
+ 008d9588 ["CALL", null, ["ram:47acf4:8"]]
- 008d93ec bytes 3286ee97
+ 008d9588 bytes db85ee97
- 008d942c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d942c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008d942c ["COPY", "tmp:2:8", ["register:8:8"]]
- 008d942c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d942c bytes e84f00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07fd6fc4b848a467165e348f899e08ba"></a>

### [`008d9570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9570.md) → [`008d970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d970c.md) FUN_008d970c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7950.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b7994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7994.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.65% / 新版 80.65%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9574"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d9570",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d9574",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d9578",
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
      "008d970c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008d9710",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008d9714",
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

- 旧版 [`008d9570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9570.md#insn-008d9570) · [`008d9574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9570.md#insn-008d9574) · [`008d9578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9570.md#insn-008d9578)

~~~diff
- 008d9570 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d9570 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d9570 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 008d9570 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008d9570 bytes fd7bbda9
- 008d9574 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008d9574 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 008d9574 bytes f50b00f9
- 008d9578 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008d9578 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008d9578 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008d9578 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d9578 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de43c79f51972ad3b74ff9830a9d359e"></a>

### [`008d9614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9614.md) → [`008d97b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d97b0.md) FUN_008d97b0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9624"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d97c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9628"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d9624",
      "DATA",
      [
        "storage",
        "00c847a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d9628",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d97d0"
      ]
    ]
  ],
  "added": [
    [
      "008d97c0",
      "DATA",
      [
        "storage",
        "00c84ba8",
        null,
        "undefined *"
      ]
    ],
    [
      "008d97c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d97d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9614.md#insn-008d9624) · [`008d9628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9614.md#insn-008d9628)
- 新版 `008d97c0`（命令位置の公開資料なし）

~~~diff
- 008d9624 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d9624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008d9624 bytes 090100f9
- 008d9628 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008d9628 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 008d9628 bytes 600000b4
+ 008d97c0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008d97c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008d97c0 bytes 090100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cda7a9862a972d40e9a90b6f41370a5"></a>

### [`008d9638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9638.md) → [`008d97d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d97d4.md) FUN_008d97d4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d97e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9648"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d9644",
      "DATA",
      [
        "storage",
        "00c847a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d9648",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d9810"
      ]
    ]
  ],
  "added": [
    [
      "008d97e0",
      "DATA",
      [
        "storage",
        "00c84ba8",
        null,
        "undefined *"
      ]
    ],
    [
      "008d97e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d9810"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9638.md#insn-008d9644) · [`008d9648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9638.md#insn-008d9648)
- 新版 `008d97e0`（命令位置の公開資料なし）

~~~diff
- 008d9644 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008d9644 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008d9644 bytes 090000f9
- 008d9648 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008d9648 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008d9648 bytes 680100b4
+ 008d97e0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008d97e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008d97e0 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-635f12a9084680e2f68a3d61b3d06355"></a>

### [`008d9678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9678.md) → [`008d9814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9814.md) FUN_008d9814

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`008d809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d809c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`008d8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8238.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 88.71% / 新版 88.71%

CFGの説明率　旧版 45.45% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d96ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d96b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d96b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d96b0",
      "DATA",
      [
        "storage",
        "00c847a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d984c",
      "DATA",
      [
        "storage",
        "00c84ba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d96ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9678.md#insn-008d96ac) · [`008d96b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9678.md#insn-008d96b0) · [`008d96b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9678.md#insn-008d96b8)

~~~diff
- 008d96ac ["COPY", "tmp:0:8", ["const:0:8"]]
- 008d96ac ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 008d96ac ["INT_ADD", "register:40a8:8", ["register:40a8:8", "const:20:8"]]
- 008d96ac ["STORE", null, ["const:1b1:8", "register:40a8:8", "tmp:1:8"]]
- 008d96ac bytes bf0e02f8
- 008d96b0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d96b0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008d96b0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008d96b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d96b0 bytes 082400a9
- 008d96b8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 008d96b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008d96b8 bytes 0a0800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0df1618c2b610aba2e67811b60ae95b"></a>

### [`008d9924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9924.md) → [`008d9ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9ac0.md) FUN_008d9ac0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008d9ad4",
      "incomplete_value": false,
      "site": "008d9ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d9938",
      "incomplete_value": false,
      "site": "008d993c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "008d9ad8",
      "DATA",
      [
        "storage",
        "00c84828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9ad8",
      "DATA",
      [
        "storage",
        "00c84c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9924.md#insn-008d9930) · [`008d9938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9924.md#insn-008d9938)
- 新版 `008d9acc`（命令位置の公開資料なし） · `008d9ad4`（命令位置の公開資料なし）

~~~diff
- 008d9930 ["INT_ADD", "register:40f0:8", ["const:8d9930:8", "const:4:8"]]
- 008d9930 ["CALL", null, ["callee:00c57e90:8"]]
+ 008d9acc ["INT_ADD", "register:40f0:8", ["const:8d9acc:8", "const:4:8"]]
+ 008d9acc ["CALL", null, ["callee:00c57e90:8"]]
- 008d9930 bytes 58f80d94
+ 008d9acc bytes f1f80d94
- 008d9938 ["COPY", "tmp:0:8", ["const:828:8"]]
- 008d9938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d9938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d9938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9ad4 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 008d9ad4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9ad4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9ad4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d9938 bytes 08a12091
+ 008d9ad4 bytes 08a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-034870b2ba3b53a53d74cc004f755c30"></a>

### [`008d9948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9948.md) → [`008d9ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9ae4.md) FUN_008d9ae4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d9ae8",
      "incomplete_value": false,
      "site": "008d9aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d994c",
      "incomplete_value": false,
      "site": "008d9950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "008d9aec",
      "DATA",
      [
        "storage",
        "00c84828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9aec",
      "DATA",
      [
        "storage",
        "00c84c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d994c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9948.md#insn-008d994c)
- 新版 `008d9ae8`（命令位置の公開資料なし）

~~~diff
- 008d994c ["COPY", "tmp:0:8", ["const:828:8"]]
- 008d994c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d994c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d994c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9ae8 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 008d9ae8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9ae8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9ae8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d994c bytes 08a12091
+ 008d9ae8 bytes 08a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be7dffff35837473953af3579b296edd"></a>

### [`008d99a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d99a4.md) → [`008d9b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9b40.md) FUN_008d9b40

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008d9b54",
      "incomplete_value": false,
      "site": "008d9b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d99b8",
      "incomplete_value": false,
      "site": "008d99bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "008d9b58",
      "DATA",
      [
        "storage",
        "00c848a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9b58",
      "DATA",
      [
        "storage",
        "00c84ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d99b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d99a4.md#insn-008d99b0) · [`008d99b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d99a4.md#insn-008d99b8)
- 新版 `008d9b4c`（命令位置の公開資料なし） · `008d9b54`（命令位置の公開資料なし）

~~~diff
- 008d99b0 ["INT_ADD", "register:40f0:8", ["const:8d99b0:8", "const:4:8"]]
- 008d99b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 008d9b4c ["INT_ADD", "register:40f0:8", ["const:8d9b4c:8", "const:4:8"]]
+ 008d9b4c ["CALL", null, ["callee:00c57e90:8"]]
- 008d99b0 bytes 38f80d94
+ 008d9b4c bytes d1f80d94
- 008d99b8 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 008d99b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d99b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d99b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9b54 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 008d9b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d99b8 bytes 08a12291
+ 008d9b54 bytes 08a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-971ce9118005aee39ed7764ddf1f9e85"></a>

### [`008d99c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d99c8.md) → [`008d9b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9b64.md) FUN_008d9b64

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d9b68",
      "incomplete_value": false,
      "site": "008d9b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d99cc",
      "incomplete_value": false,
      "site": "008d99d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "008d9b6c",
      "DATA",
      [
        "storage",
        "00c848a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9b6c",
      "DATA",
      [
        "storage",
        "00c84ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d99cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d99c8.md#insn-008d99cc)
- 新版 `008d9b68`（命令位置の公開資料なし）

~~~diff
- 008d99cc ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 008d99cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d99cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d99cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9b68 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 008d9b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d99cc bytes 08a12291
+ 008d9b68 bytes 08a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-458713f978d9fde8e5407118b7c41417"></a>

### [`008d9a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a10.md) → [`008d9bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9bac.md) FUN_008d9bac

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d9bcc",
      "incomplete_value": false,
      "site": "008d9bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d9a30",
      "incomplete_value": false,
      "site": "008d9a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "008d9bd0",
      "DATA",
      [
        "storage",
        "00c84928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9bd0",
      "DATA",
      [
        "storage",
        "00c84d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a10.md#insn-008d9a24) · [`008d9a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a10.md#insn-008d9a30)
- 新版 `008d9bc0`（命令位置の公開資料なし） · `008d9bcc`（命令位置の公開資料なし）

~~~diff
- 008d9a24 ["INT_ADD", "register:40f0:8", ["const:8d9a24:8", "const:4:8"]]
- 008d9a24 ["CALL", null, ["callee:00c57e90:8"]]
+ 008d9bc0 ["INT_ADD", "register:40f0:8", ["const:8d9bc0:8", "const:4:8"]]
+ 008d9bc0 ["CALL", null, ["callee:00c57e90:8"]]
- 008d9a24 bytes 1bf80d94
+ 008d9bc0 bytes b4f80d94
- 008d9a30 ["COPY", "tmp:0:8", ["const:928:8"]]
- 008d9a30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d9a30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d9a30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9bcc ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 008d9bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d9a30 bytes 08a12491
+ 008d9bcc bytes 08a13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f4d0c6c701eb77bc5de3a7356fd499b"></a>

### [`008d9a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a48.md) → [`008d9be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9be4.md) FUN_008d9be4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d9be8",
      "incomplete_value": false,
      "site": "008d9bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d9a4c",
      "incomplete_value": false,
      "site": "008d9a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "008d9bec",
      "DATA",
      [
        "storage",
        "00c84928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9bec",
      "DATA",
      [
        "storage",
        "00c84d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a48.md#insn-008d9a4c)
- 新版 `008d9be8`（命令位置の公開資料なし）

~~~diff
- 008d9a4c ["COPY", "tmp:0:8", ["const:928:8"]]
- 008d9a4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d9a4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d9a4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9be8 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 008d9be8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9be8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9be8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d9a4c bytes 08a12491
+ 008d9be8 bytes 08a13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c40598613e8dd678ed68d9cf8b43337"></a>

### [`008d9a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md) → [`008d9c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9c04.md) FUN_008d9c04

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 28件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0044d9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044d9f8.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md)
- 新版 呼出元 0件  · 呼出先 28件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0044da38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044da38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.32% / 新版 89.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_value` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d9ce0",
      "incomplete_value": true,
      "site": "008d9cf8",
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
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:660:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d9b44",
      "incomplete_value": true,
      "site": "008d9b5c",
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
                "const:2c2000:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "008d9cec",
      "incomplete_value": true,
      "site": "008d9cfc",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:33a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d9b50",
      "incomplete_value": true,
      "site": "008d9b60",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:26d:8"
              ]
            ]
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
      "definition_site": "008d9cec",
      "incomplete_value": true,
      "site": "008d9cfc",
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
      "definition_site": "008d9b50",
      "incomplete_value": true,
      "site": "008d9b60",
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
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d9ce0",
      "READ",
      [
        "storage",
        "002c2620",
        null,
        null
      ]
    ],
    [
      "008d9cec",
      "READ",
      [
        "storage",
        "002aa26d",
        null,
        "string"
      ]
    ],
    [
      "008d9cec",
      "READ",
      [
        "storage",
        "002aa27d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d9ce0",
      "READ",
      [
        "storage",
        "002c2660",
        null,
        null
      ]
    ],
    [
      "008d9cec",
      "READ",
      [
        "storage",
        "002aa33a",
        null,
        "string"
      ]
    ],
    [
      "008d9cec",
      "READ",
      [
        "storage",
        "002aa34a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md#insn-008d9c74) · [`008d9c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md#insn-008d9c90) · [`008d9cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md#insn-008d9cfc)
- 新版 `008d9e10`（命令位置の公開資料なし） · `008d9e2c`（命令位置の公開資料なし） · `008d9e98`（命令位置の公開資料なし）

~~~diff
- 008d9c74 ["INT_ADD", "register:40f0:8", ["const:8d9c74:8", "const:4:8"]]
- 008d9c74 ["CALL", null, ["ram:48ccb8:8"]]
+ 008d9e10 ["INT_ADD", "register:40f0:8", ["const:8d9e10:8", "const:4:8"]]
+ 008d9e10 ["CALL", null, ["ram:48ccf8:8"]]
- 008d9c74 bytes 11ccee97
+ 008d9e10 bytes bacbee97
- 008d9c90 ["INT_ADD", "register:40f0:8", ["const:8d9c90:8", "const:4:8"]]
- 008d9c90 ["CALL", null, ["callee:00c57f70:8"]]
+ 008d9e2c ["INT_ADD", "register:40f0:8", ["const:8d9e2c:8", "const:4:8"]]
+ 008d9e2c ["CALL", null, ["callee:00c57f70:8"]]
- 008d9c90 bytes b8f70d94
+ 008d9e2c bytes 51f80d94
- 008d9cfc ["INT_ADD", "register:40f0:8", ["const:8d9cfc:8", "const:4:8"]]
- 008d9cfc ["CALL", null, ["callee:00c57e90:8"]]
+ 008d9e98 ["INT_ADD", "register:40f0:8", ["const:8d9e98:8", "const:4:8"]]
+ 008d9e98 ["CALL", null, ["callee:00c57e90:8"]]
- 008d9cfc bytes 65f70d94
+ 008d9e98 bytes fef70d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a86ee271a8a2fcdfd80b7badae0ae84f"></a>

### [`008da1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da1c8.md) → [`008da364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da364.md) FUN_008da364

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008da378",
      "incomplete_value": false,
      "site": "008da37c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da1dc",
      "incomplete_value": false,
      "site": "008da1e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "008da37c",
      "DATA",
      [
        "storage",
        "00c84998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da37c",
      "DATA",
      [
        "storage",
        "00c84d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da1c8.md#insn-008da1d4) · [`008da1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da1c8.md#insn-008da1dc)
- 新版 `008da370`（命令位置の公開資料なし） · `008da378`（命令位置の公開資料なし）

~~~diff
- 008da1d4 ["INT_ADD", "register:40f0:8", ["const:8da1d4:8", "const:4:8"]]
- 008da1d4 ["CALL", null, ["callee:00c57e90:8"]]
+ 008da370 ["INT_ADD", "register:40f0:8", ["const:8da370:8", "const:4:8"]]
+ 008da370 ["CALL", null, ["callee:00c57e90:8"]]
- 008da1d4 bytes 2ff60d94
+ 008da370 bytes c8f60d94
- 008da1dc ["COPY", "tmp:0:8", ["const:998:8"]]
- 008da1dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008da1dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008da1dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da378 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 008da378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008da1dc bytes 08612691
+ 008da378 bytes 08613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d463355c3b2f4bf5af44c2c722cbc0a2"></a>

### [`008da1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da1ec.md) → [`008da388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da388.md) FUN_008da388

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008da38c",
      "incomplete_value": false,
      "site": "008da390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da1f0",
      "incomplete_value": false,
      "site": "008da1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "008da390",
      "DATA",
      [
        "storage",
        "00c84998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da390",
      "DATA",
      [
        "storage",
        "00c84d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da1ec.md#insn-008da1f0)
- 新版 `008da38c`（命令位置の公開資料なし）

~~~diff
- 008da1f0 ["COPY", "tmp:0:8", ["const:998:8"]]
- 008da1f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008da1f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008da1f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da38c ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 008da38c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da38c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da38c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008da1f0 bytes 08612691
+ 008da38c bytes 08613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e4f8a31f82f8d61aab07dcaee4c5319"></a>

### [`008da248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da248.md) → [`008da3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da3e4.md) FUN_008da3e4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008da3f8",
      "incomplete_value": false,
      "site": "008da3fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da25c",
      "incomplete_value": false,
      "site": "008da260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "008da3fc",
      "DATA",
      [
        "storage",
        "00c84a18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da3fc",
      "DATA",
      [
        "storage",
        "00c84e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da248.md#insn-008da254) · [`008da25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da248.md#insn-008da25c)
- 新版 `008da3f0`（命令位置の公開資料なし） · `008da3f8`（命令位置の公開資料なし）

~~~diff
- 008da254 ["INT_ADD", "register:40f0:8", ["const:8da254:8", "const:4:8"]]
- 008da254 ["CALL", null, ["callee:00c57e90:8"]]
+ 008da3f0 ["INT_ADD", "register:40f0:8", ["const:8da3f0:8", "const:4:8"]]
+ 008da3f0 ["CALL", null, ["callee:00c57e90:8"]]
- 008da254 bytes 0ff60d94
+ 008da3f0 bytes a8f60d94
- 008da25c ["COPY", "tmp:0:8", ["const:a18:8"]]
- 008da25c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008da25c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008da25c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da3f8 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 008da3f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da3f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da3f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008da25c bytes 08612891
+ 008da3f8 bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-803943d4fd34b3481fef1f9be33fbade"></a>

### [`008da26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da26c.md) → [`008da408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da408.md) FUN_008da408

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008da40c",
      "incomplete_value": false,
      "site": "008da410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da270",
      "incomplete_value": false,
      "site": "008da274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "008da410",
      "DATA",
      [
        "storage",
        "00c84a18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da410",
      "DATA",
      [
        "storage",
        "00c84e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da26c.md#insn-008da270)
- 新版 `008da40c`（命令位置の公開資料なし）

~~~diff
- 008da270 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 008da270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008da270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008da270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da40c ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 008da40c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da40c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da40c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008da270 bytes 08612891
+ 008da40c bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f33517aa1024bf9b18914ffdd58e0b4"></a>

### [`008da2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da2c8.md) → [`008da464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da464.md) FUN_008da464

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008da478",
      "incomplete_value": false,
      "site": "008da47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da2dc",
      "incomplete_value": false,
      "site": "008da2e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "008da47c",
      "DATA",
      [
        "storage",
        "00c84a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da47c",
      "DATA",
      [
        "storage",
        "00c84e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da2c8.md#insn-008da2d4) · [`008da2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da2c8.md#insn-008da2dc)
- 新版 `008da470`（命令位置の公開資料なし） · `008da478`（命令位置の公開資料なし）

~~~diff
- 008da2d4 ["INT_ADD", "register:40f0:8", ["const:8da2d4:8", "const:4:8"]]
- 008da2d4 ["CALL", null, ["callee:00c57e90:8"]]
+ 008da470 ["INT_ADD", "register:40f0:8", ["const:8da470:8", "const:4:8"]]
+ 008da470 ["CALL", null, ["callee:00c57e90:8"]]
- 008da2d4 bytes eff50d94
+ 008da470 bytes 88f60d94
- 008da2dc ["COPY", "tmp:0:8", ["const:a98:8"]]
- 008da2dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008da2dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008da2dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da478 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008da478 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da478 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da478 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008da2dc bytes 08612a91
+ 008da478 bytes 08613a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4acfdc490d92fe4f5518370d999530a4"></a>

### [`008da2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da2ec.md) → [`008da488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da488.md) FUN_008da488

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008da48c",
      "incomplete_value": false,
      "site": "008da490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da2f0",
      "incomplete_value": false,
      "site": "008da2f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "008da490",
      "DATA",
      [
        "storage",
        "00c84a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da490",
      "DATA",
      [
        "storage",
        "00c84e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da2ec.md#insn-008da2f0)
- 新版 `008da48c`（命令位置の公開資料なし）

~~~diff
- 008da2f0 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 008da2f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008da2f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008da2f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da48c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008da48c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da48c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da48c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008da2f0 bytes 08612a91
+ 008da48c bytes 08613a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c9e0e4b3a2055100e9df88d9232b55e"></a>

### [`008da348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da348.md) → [`008da4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da4e4.md) FUN_008da4e4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "008da4f8",
      "incomplete_value": false,
      "site": "008da4fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da35c",
      "incomplete_value": false,
      "site": "008da360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "008da4fc",
      "DATA",
      [
        "storage",
        "00c84b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da4fc",
      "DATA",
      [
        "storage",
        "00c84f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da348.md#insn-008da354) · [`008da35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da348.md#insn-008da35c)
- 新版 `008da4f0`（命令位置の公開資料なし） · `008da4f8`（命令位置の公開資料なし）

~~~diff
- 008da354 ["INT_ADD", "register:40f0:8", ["const:8da354:8", "const:4:8"]]
- 008da354 ["CALL", null, ["callee:00c57e90:8"]]
+ 008da4f0 ["INT_ADD", "register:40f0:8", ["const:8da4f0:8", "const:4:8"]]
+ 008da4f0 ["CALL", null, ["callee:00c57e90:8"]]
- 008da354 bytes cff50d94
+ 008da4f0 bytes 68f60d94
- 008da35c ["COPY", "tmp:0:8", ["const:b18:8"]]
- 008da35c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008da35c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008da35c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da4f8 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 008da4f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da4f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da4f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008da35c bytes 08612c91
+ 008da4f8 bytes 08613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0d253a75cf89feff4608f962fc5b0e5"></a>

### [`008da36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da36c.md) → [`008da508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da508.md) FUN_008da508

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008da50c",
      "incomplete_value": false,
      "site": "008da510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da370",
      "incomplete_value": false,
      "site": "008da374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "008da510",
      "DATA",
      [
        "storage",
        "00c84b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da510",
      "DATA",
      [
        "storage",
        "00c84f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da36c.md#insn-008da370)
- 新版 `008da50c`（命令位置の公開資料なし）

~~~diff
- 008da370 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 008da370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008da370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008da370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da50c ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 008da50c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da50c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008da370 bytes 08612c91
+ 008da50c bytes 08613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5902574ea31613c5f01aa219855e3739"></a>

### [`008da3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da3c4.md) → [`008da560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da560.md) FUN_008da560

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008da56c",
      "incomplete_value": false,
      "site": "008da578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da3d0",
      "incomplete_value": false,
      "site": "008da3dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "008da578",
      "DATA",
      [
        "storage",
        "00c84ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da578",
      "DATA",
      [
        "storage",
        "00c84fa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da3c4.md#insn-008da3d0)
- 新版 `008da56c`（命令位置の公開資料なし）

~~~diff
- 008da3d0 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 008da3d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008da3d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008da3d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008da56c ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 008da56c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008da56c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008da56c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008da3d0 bytes 4aa12e91
+ 008da56c bytes 4aa13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91a6e8c8806c9a311498e1e2003d8ee9"></a>

### [`008da408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da408.md) → [`008da5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da5a4.md) FUN_008da5a4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008da5bc",
      "incomplete_value": false,
      "site": "008da5c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da420",
      "incomplete_value": false,
      "site": "008da42c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "008da5c8",
      "DATA",
      [
        "storage",
        "00c84ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da5c8",
      "DATA",
      [
        "storage",
        "00c84fa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da408.md#insn-008da420) · [`008da450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da408.md#insn-008da450)
- 新版 `008da5bc`（命令位置の公開資料なし） · `008da5ec`（命令位置の公開資料なし）

~~~diff
- 008da420 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 008da420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008da420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008da420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da5bc ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 008da5bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da5bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da5bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008da420 bytes 08a12e91
+ 008da5bc bytes 08a13e91
- 008da450 ["COPY", "register:0:8", ["register:4040:8"]]
- 008da450 ["INT_ADD", "register:40f0:8", ["const:8da450:8", "const:4:8"]]
- 008da450 ["CALLIND", null, ["register:0:8"]]
+ 008da5ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 008da5ec ["INT_ADD", "register:40f0:8", ["const:8da5ec:8", "const:4:8"]]
+ 008da5ec ["CALLIND", null, ["register:0:8"]]
- 008da450 bytes 00013fd6
+ 008da5ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6f59c6e569aeaf5a8628f75a1cc3023"></a>

### [`008da464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da464.md) → [`008da600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da600.md) FUN_008da600

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008da628",
      "incomplete_value": false,
      "site": "008da62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da48c",
      "incomplete_value": false,
      "site": "008da490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "008da62c",
      "DATA",
      [
        "storage",
        "00c84ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da62c",
      "DATA",
      [
        "storage",
        "00c84fa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da464.md#insn-008da478) · [`008da48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da464.md#insn-008da48c) · [`008da4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da464.md#insn-008da4b0)
- 新版 `008da614`（命令位置の公開資料なし） · `008da628`（命令位置の公開資料なし） · `008da64c`（命令位置の公開資料なし）

~~~diff
- 008da478 ["INT_ADD", "register:40f0:8", ["const:8da478:8", "const:4:8"]]
- 008da478 ["CALL", null, ["callee:00c57e90:8"]]
+ 008da614 ["INT_ADD", "register:40f0:8", ["const:8da614:8", "const:4:8"]]
+ 008da614 ["CALL", null, ["callee:00c57e90:8"]]
- 008da478 bytes 86f50d94
+ 008da614 bytes 1ff60d94
- 008da48c ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 008da48c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008da48c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008da48c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008da628 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 008da628 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008da628 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008da628 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008da48c bytes 29a12e91
+ 008da628 bytes 29a13e91
- 008da4b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008da4b0 ["INT_ADD", "register:40f0:8", ["const:8da4b0:8", "const:4:8"]]
- 008da4b0 ["CALLIND", null, ["register:0:8"]]
+ 008da64c ["COPY", "register:0:8", ["register:4040:8"]]
+ 008da64c ["INT_ADD", "register:40f0:8", ["const:8da64c:8", "const:4:8"]]
+ 008da64c ["CALLIND", null, ["register:0:8"]]
- 008da4b0 bytes 00013fd6
+ 008da64c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8d7292d3b99667c8a8e1f54d116dec4"></a>

### [`008da4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da4fc.md) → [`008da698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da698.md) FUN_008da698

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008da6b8",
      "incomplete_value": false,
      "site": "008da6bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da51c",
      "incomplete_value": false,
      "site": "008da520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "008da6bc",
      "DATA",
      [
        "storage",
        "00c84ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da6bc",
      "DATA",
      [
        "storage",
        "00c84fa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da4fc.md#insn-008da51c) · [`008da540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da4fc.md#insn-008da540) · [`008da568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da4fc.md#insn-008da568)
- 新版 `008da6b8`（命令位置の公開資料なし） · `008da6dc`（命令位置の公開資料なし） · `008da704`（命令位置の公開資料なし）

~~~diff
- 008da51c ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 008da51c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008da51c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008da51c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008da6b8 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 008da6b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008da6b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008da6b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008da51c bytes 29a12e91
+ 008da6b8 bytes 29a13e91
- 008da540 ["COPY", "register:0:8", ["register:4040:8"]]
- 008da540 ["INT_ADD", "register:40f0:8", ["const:8da540:8", "const:4:8"]]
- 008da540 ["CALLIND", null, ["register:0:8"]]
+ 008da6dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008da6dc ["INT_ADD", "register:40f0:8", ["const:8da6dc:8", "const:4:8"]]
+ 008da6dc ["CALLIND", null, ["register:0:8"]]
- 008da540 bytes 00013fd6
+ 008da6dc bytes 00013fd6
- 008da568 ["COPY", "register:0:8", ["register:4040:8"]]
- 008da568 ["INT_ADD", "register:40f0:8", ["const:8da568:8", "const:4:8"]]
- 008da568 ["CALLIND", null, ["register:0:8"]]
+ 008da704 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008da704 ["INT_ADD", "register:40f0:8", ["const:8da704:8", "const:4:8"]]
+ 008da704 ["CALLIND", null, ["register:0:8"]]
- 008da568 bytes 00013fd6
+ 008da704 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-783f2f271c5a3d8864b7e61a2afff443"></a>

### [`008da608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da608.md) → [`008da7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da7a4.md) FUN_008da7a4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`00865ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865ab4.md) [`008d5f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5f6c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) [`00865af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865af4.md) [`008d6108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6108.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.92% / 新版 98.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008da86c",
      "incomplete_value": true,
      "site": "008da86c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6f6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008da6d0",
      "incomplete_value": true,
      "site": "008da6d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:629:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008da854",
      "READ",
      [
        "storage",
        "002a0629",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008da854",
      "READ",
      [
        "storage",
        "002a06f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008da64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da608.md#insn-008da64c) · [`008da66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da608.md#insn-008da66c) · [`008da678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da608.md#insn-008da678)
- 新版 `008da7e8`（命令位置の公開資料なし） · `008da808`（命令位置の公開資料なし） · `008da814`（命令位置の公開資料なし）

~~~diff
- 008da64c ["COPY", "register:0:8", ["register:4040:8"]]
- 008da64c ["INT_ADD", "register:40f0:8", ["const:8da64c:8", "const:4:8"]]
- 008da64c ["CALLIND", null, ["register:0:8"]]
+ 008da7e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008da7e8 ["INT_ADD", "register:40f0:8", ["const:8da7e8:8", "const:4:8"]]
+ 008da7e8 ["CALLIND", null, ["register:0:8"]]
- 008da64c bytes 00013fd6
+ 008da7e8 bytes 00013fd6
- 008da66c ["INT_ADD", "register:40f0:8", ["const:8da66c:8", "const:4:8"]]
- 008da66c ["CALL", null, ["callee:00c53cd0:8"]]
+ 008da808 ["INT_ADD", "register:40f0:8", ["const:8da808:8", "const:4:8"]]
+ 008da808 ["CALL", null, ["callee:00c53cd0:8"]]
- 008da66c bytes 91e40d94
+ 008da808 bytes 32e50d94
- 008da678 ["INT_ADD", "register:40f0:8", ["const:8da678:8", "const:4:8"]]
- 008da678 ["CALL", null, ["callee:00596f2c:8"]]
+ 008da814 ["INT_ADD", "register:40f0:8", ["const:8da814:8", "const:4:8"]]
+ 008da814 ["CALL", null, ["callee:00596f2c:8"]]
- 008da678 bytes 1df2f297
+ 008da814 bytes c6f1f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a34323a7eef2ddcaa4131171c931404"></a>

### [`008daad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008daad4.md) → [`008dac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008dac70.md) FUN_008dac70

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008dac7c",
      "incomplete_value": false,
      "site": "008dac88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008daae0",
      "incomplete_value": false,
      "site": "008daaec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "008dac88",
      "DATA",
      [
        "storage",
        "00c84c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008dac88",
      "DATA",
      [
        "storage",
        "00c85028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008daadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008daad4.md#insn-008daadc) · [`008daae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008daad4.md#insn-008daae0)
- 新版 `008dac78`（命令位置の公開資料なし） · `008dac7c`（命令位置の公開資料なし）

~~~diff
- 008daadc ["COPY", "register:4050:8", ["const:c84000:8"]]
+ 008dac78 ["COPY", "register:4050:8", ["const:c85000:8"]]
- 008daadc bytes 4a1d00d0
+ 008dac78 bytes 4a1d00f0
- 008daae0 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 008daae0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008daae0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008daae0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008dac7c ["COPY", "tmp:0:8", ["const:28:8"]]
+ 008dac7c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008dac7c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008dac7c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008daae0 bytes 4aa13091
+ 008dac7c bytes 4aa10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cced4dc73d15e8455153544792eeb0a"></a>

### [`008dab18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab18.md) → [`008dacb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008dacb4.md) FUN_008dacb4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008daccc",
      "incomplete_value": false,
      "site": "008dacd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008dab30",
      "incomplete_value": false,
      "site": "008dab3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "008dacd8",
      "DATA",
      [
        "storage",
        "00c84c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008dacd8",
      "DATA",
      [
        "storage",
        "00c85028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008dab2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab18.md#insn-008dab2c) · [`008dab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab18.md#insn-008dab30) · [`008dab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab18.md#insn-008dab60)
- 新版 `008dacc8`（命令位置の公開資料なし） · `008daccc`（命令位置の公開資料なし） · `008dacfc`（命令位置の公開資料なし）

~~~diff
- 008dab2c ["COPY", "register:4040:8", ["const:c84000:8"]]
+ 008dacc8 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008dab2c bytes 481d00d0
+ 008dacc8 bytes 481d00f0
- 008dab30 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 008dab30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008dab30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008dab30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008daccc ["COPY", "tmp:0:8", ["const:28:8"]]
+ 008daccc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008daccc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008daccc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008dab30 bytes 08a13091
+ 008daccc bytes 08a10091
- 008dab60 ["COPY", "register:0:8", ["register:4040:8"]]
- 008dab60 ["INT_ADD", "register:40f0:8", ["const:8dab60:8", "const:4:8"]]
- 008dab60 ["CALLIND", null, ["register:0:8"]]
+ 008dacfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008dacfc ["INT_ADD", "register:40f0:8", ["const:8dacfc:8", "const:4:8"]]
+ 008dacfc ["CALLIND", null, ["register:0:8"]]
- 008dab60 bytes 00013fd6
+ 008dacfc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af8054a5153d3adc567a1a78c341fb77"></a>

### [`008dab74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab74.md) → [`008dad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008dad10.md) FUN_008dad10

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008dad38",
      "incomplete_value": false,
      "site": "008dad3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008dab9c",
      "incomplete_value": false,
      "site": "008daba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "008dad3c",
      "DATA",
      [
        "storage",
        "00c84c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008dad3c",
      "DATA",
      [
        "storage",
        "00c85028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008dab88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab74.md#insn-008dab88) · [`008dab98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab74.md#insn-008dab98) · [`008dab9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab74.md#insn-008dab9c)
- 新版 `008dad24`（命令位置の公開資料なし） · `008dad34`（命令位置の公開資料なし） · `008dad38`（命令位置の公開資料なし）

~~~diff
- 008dab88 ["INT_ADD", "register:40f0:8", ["const:8dab88:8", "const:4:8"]]
- 008dab88 ["CALL", null, ["callee:00c57e90:8"]]
+ 008dad24 ["INT_ADD", "register:40f0:8", ["const:8dad24:8", "const:4:8"]]
+ 008dad24 ["CALL", null, ["callee:00c57e90:8"]]
- 008dab88 bytes c2f30d94
+ 008dad24 bytes 5bf40d94
- 008dab98 ["COPY", "register:4048:8", ["const:c84000:8"]]
+ 008dad34 ["COPY", "register:4048:8", ["const:c85000:8"]]
- 008dab98 bytes 491d00d0
+ 008dad34 bytes 491d00f0
- 008dab9c ["COPY", "tmp:0:8", ["const:c28:8"]]
- 008dab9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008dab9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008dab9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008dad38 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 008dad38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008dad38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008dad38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008dab9c bytes 29a13091
+ 008dad38 bytes 29a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c2f6e6bc32259cb51c9f4cd420bba74"></a>

### [`008dac04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dac04.md) → [`008dada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008dada0.md) FUN_008dada0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008dadbc",
      "incomplete_value": false,
      "site": "008dadc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008dac20",
      "incomplete_value": false,
      "site": "008dac24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "008dadc0",
      "DATA",
      [
        "storage",
        "00c84c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008dadc0",
      "DATA",
      [
        "storage",
        "00c85028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008dac1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dac04.md#insn-008dac1c) · [`008dac20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dac04.md#insn-008dac20) · [`008dac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dac04.md#insn-008dac48)
- 新版 `008dadb8`（命令位置の公開資料なし） · `008dadbc`（命令位置の公開資料なし） · `008dade4`（命令位置の公開資料なし）

~~~diff
- 008dac1c ["COPY", "register:4050:8", ["const:c84000:8"]]
+ 008dadb8 ["COPY", "register:4050:8", ["const:c85000:8"]]
- 008dac1c bytes 4a1d00d0
+ 008dadb8 bytes 4a1d00f0
- 008dac20 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 008dac20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008dac20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008dac20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008dadbc ["COPY", "tmp:0:8", ["const:28:8"]]
+ 008dadbc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008dadbc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008dadbc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008dac20 bytes 4aa13091
+ 008dadbc bytes 4aa10091
- 008dac48 ["COPY", "register:0:8", ["register:4048:8"]]
- 008dac48 ["INT_ADD", "register:40f0:8", ["const:8dac48:8", "const:4:8"]]
- 008dac48 ["CALLIND", null, ["register:0:8"]]
+ 008dade4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008dade4 ["INT_ADD", "register:40f0:8", ["const:8dade4:8", "const:4:8"]]
+ 008dade4 ["CALLIND", null, ["register:0:8"]]
- 008dac48 bytes 20013fd6
+ 008dade4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fde9b78768b2bd92445a5d9defb98175"></a>

### [`008dafdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dafdc.md) → [`008db178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008db/008db178.md) _INIT_172

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.97% / 新版 77.97%

CFGの説明率　旧版 27.27% / 新版 18.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008db00c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008db034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008db058"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008db00c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008db018",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008db034",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008db1a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008db1b4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "008db1d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008db00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dafdc.md#insn-008db00c) · [`008db034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dafdc.md#insn-008db034) · [`008db058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dafdc.md#insn-008db058)

~~~diff
- 008db00c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008db00c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008db00c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008db00c bytes a9831ff8
- 008db034 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 008db034 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008db034 bytes e013813c
- 008db058 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 008db058 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008db058 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70180c9d5b97f898975c4c487387ee97"></a>

### [`008db36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db36c.md) → [`008db508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008db/008db508.md) FUN_008db508

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008dde04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dde04.md) · 呼出先 3件 [`008db480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db480.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`008ddfa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddfa0.md) · 呼出先 3件 [`008db61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008db/008db61c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 18.18% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008db460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008db5fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008db3a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008db52c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008db39c"
      ]
    ],
    [
      "008db534",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008db3ac"
      ]
    ],
    [
      "unmatched:008db39c",
      "READ",
      [
        "storage",
        "00ca420c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "008db52c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008db538"
      ]
    ],
    [
      "008db534",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008db548"
      ]
    ],
    [
      "008db538",
      "READ",
      [
        "storage",
        "00ca460c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008db3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db36c.md#insn-008db3a8) · [`008db3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db36c.md#insn-008db3e8) · [`008db438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db36c.md#insn-008db438)
- 新版 `008db5d4`（命令位置の公開資料なし）

~~~diff
- 008db3a8 ["CBRANCH", null, ["local:b23:8", "register:101:1"]]
- 008db3a8 bytes e0050054
- 008db3e8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 008db3e8 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 008db3e8 ["CBRANCH", null, ["local:b21:8", "tmp:1:1"]]
- 008db3e8 bytes a9030054
- 008db438 ["INT_ADD", "register:40f0:8", ["const:8db438:8", "const:4:8"]]
- 008db438 ["CALL", null, ["callee:00c53d00:8"]]
+ 008db5d4 ["INT_ADD", "register:40f0:8", ["const:8db5d4:8", "const:4:8"]]
+ 008db5d4 ["CALL", null, ["callee:00c53d00:8"]]
- 008db438 bytes 2ae10d94
+ 008db5d4 bytes cbe10d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8b2b924a3b1cd84a895f03e2ed6d1f6"></a>

### [`008db480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db480.md) → [`008db61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008db/008db61c.md) FUN_008db61c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008db36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db36c.md) [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) · 呼出先 4件 [`006662e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/006662e0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`008db508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008db/008db508.md) [`008dd0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dd0f4.md) · 呼出先 4件 [`00666320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/00666320.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 18.18% / 新版 19.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008db49c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008db638"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008db4f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008db49c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008db4f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008db6bc"
      ]
    ],
    [
      "unmatched:008db500",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c53d00"
      ]
    ]
  ],
  "added": [
    [
      "008db638",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008db690",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008db6bc"
      ]
    ],
    [
      "008db69c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c53d00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008db49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db480.md#insn-008db49c) · [`008db4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db480.md#insn-008db4e0) · [`008db4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db480.md#insn-008db4f4)
- 新版 `008db67c`（命令位置の公開資料なし）

~~~diff
- 008db49c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008db49c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008db49c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008db49c bytes a8831ff8
- 008db4e0 ["INT_ADD", "register:40f0:8", ["const:8db4e0:8", "const:4:8"]]
- 008db4e0 ["CALL", null, ["callee:00666320:8"]]
+ 008db67c ["INT_ADD", "register:40f0:8", ["const:8db67c:8", "const:4:8"]]
+ 008db67c ["CALL", null, ["callee:00666320:8"]]
- 008db4e0 bytes 802bf697
+ 008db67c bytes 292bf697
- 008db4f4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 008db4f4 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 008db4f4 bytes 730100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d57d3eeb694f912337d000cab2d8e1b2"></a>

### [`008db558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db558.md) → [`008db6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008db/008db6f4.md) FUN_008db6f4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md) [`006647f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006647f0.md) [`00665c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665c3c.md) [`00665c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665c78.md)
- 新版 呼出元 1件 [`008dd0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dd0f4.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`006647c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006647c0.md) [`00664830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664830.md) [`00665c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665c7c.md) [`00665cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665cb8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 58.97% / 新版 58.97%

CFGの説明率　旧版 7.48% / 新版 7.20%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 31件, `unresolved_branch_alignment` 26件, `unresolved_call_alignment` 12件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 46件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008db55c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008db55c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008db560"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008db55c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008db560",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008db564",
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
      "008db6f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008db6fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008db700",
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

- 旧版 [`008db55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db558.md#insn-008db55c) · [`008db560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db558.md#insn-008db560) · [`008db564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db558.md#insn-008db564)

~~~diff
- 008db55c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008db55c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008db55c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 008db55c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008db55c bytes fd7b0ca9
- 008db560 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008db560 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008db560 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 008db560 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008db560 bytes fc6f0da9
- 008db564 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008db564 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008db564 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 008db564 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008db564 bytes fa670ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-defea46e5a798b06f7027392e18c21bd"></a>

### [`008dbf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008dbf84.md) → [`008dc120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dc/008dc120.md) FUN_008dc120

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008ddabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008ddabc.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 1件 [`008ddc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddc58.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.64% / 新版 74.64%

CFGの説明率　旧版 4.80% / 新版 5.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 11件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dbfa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dc068"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dc084"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008dbfa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008dbfc4",
      "DATA",
      [
        "storage",
        "00335f3c",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "unmatched:008dc018",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008dc140",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008dc160",
      "DATA",
      [
        "storage",
        "00335f3c",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "008dc1b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008dbfa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008dbf84.md#insn-008dbfa4) · [`008dc010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008dbf84.md#insn-008dc010) · [`008dc018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008dbf84.md#insn-008dc018)
- 新版 `008dc1ac`（命令位置の公開資料なし）

~~~diff
- 008dbfa4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008dbfa4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008dbfa4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008dbfa4 bytes a8831ff8
- 008dc010 ["INT_ADD", "register:40f0:8", ["const:8dc010:8", "const:4:8"]]
- 008dc010 ["CALL", null, ["callee:009dcecc:8"]]
+ 008dc1ac ["INT_ADD", "register:40f0:8", ["const:8dc1ac:8", "const:4:8"]]
+ 008dc1ac ["CALL", null, ["callee:009dcecc:8"]]
- 008dc010 bytes 48030494
+ 008dc1ac bytes 48030494
- 008dc018 ["INT_ADD", "register:40f0:8", ["const:8dc018:8", "const:4:8"]]
- 008dc018 ["CALL", null, ["ram:47acb4:8"]]
- 008dc018 bytes 277bee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3256177d877e671bfffa65e3b54d5159"></a>

### [`008dc4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc4c8.md) → [`008dc664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dc/008dc664.md) FUN_008dc664

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008dd868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dd868.md) · 呼出先 9件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)
- 新版 呼出元 1件 [`008dda04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dda04.md) · 呼出先 9件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.22% / 新版 87.22%

CFGの説明率　旧版 6.98% / 新版 7.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dc4e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dc4e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008dc67c"
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
      "unmatched:008dc4e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008dc4f4",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008dc4fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008dc6c0"
      ]
    ]
  ],
  "added": [
    [
      "008dc67c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008dc690",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008dc698",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008dc6c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008dc4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc4c8.md#insn-008dc4e0) · [`008dc4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc4c8.md#insn-008dc4fc) · [`008dc518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc4c8.md#insn-008dc518)
- 新版 `008dc6b4`（命令位置の公開資料なし）

~~~diff
- 008dc4e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008dc4e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008dc4e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 008dc4e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008dc4e0 bytes f44f06a9
- 008dc4fc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008dc4fc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 008dc4fc bytes 480100b4
- 008dc518 ["INT_ADD", "register:40f0:8", ["const:8dc518:8", "const:4:8"]]
- 008dc518 ["CALL", null, ["callee:00c58610:8"]]
+ 008dc6b4 ["INT_ADD", "register:40f0:8", ["const:8dc6b4:8", "const:4:8"]]
+ 008dc6b4 ["CALL", null, ["callee:00c58610:8"]]
- 008dc518 bytes 3eef0d94
+ 008dc6b4 bytes d7ef0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4410210d2fdcaa446ecfb0645e8fc2a9"></a>

### [`008dc798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc798.md) → [`008dc934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dc/008dc934.md) FUN_008dc934

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) · 呼出先 12件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00615ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615ea0.md) [`0065349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/0065349c.md)
- 新版 呼出元 1件 [`008dd0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dd0f4.md) · 呼出先 12件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00615ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ee0.md) [`006534dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006534dc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.90% / 新版 71.90%

CFGの説明率　旧版 14.81% / 新版 15.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `call_target` 1件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 33件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dc79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dc7a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dc7a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008dc79c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:008dc7a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008dc7a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008dc938",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "008dc93c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008dc940",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008dc79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc798.md#insn-008dc79c) · [`008dc7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc798.md#insn-008dc7a0) · [`008dc7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc798.md#insn-008dc7a4)

~~~diff
- 008dc79c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 008dc79c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 008dc79c bytes e83b00fd
- 008dc7a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008dc7a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008dc7a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 008dc7a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008dc7a0 bytes fd7b08a9
- 008dc7a4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008dc7a4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008dc7a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 008dc7a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008dc7a4 bytes fc6f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cb96a93ba2d773bb1afe4dbbeea330f"></a>

### [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) → [`008dd0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dd0f4.md) FUN_008dd0f4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008ddb18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008ddb18.md) · 呼出先 29件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 1件 [`008ddcb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddcb4.md) · 呼出先 29件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.21% / 新版 89.21%

CFGの説明率　旧版 89.84% / 新版 88.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 11件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008dd4e0",
      "incomplete_value": false,
      "site": "008dd4e0",
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
            "const:60c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008dd344",
      "incomplete_value": false,
      "site": "008dd344",
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
            "const:20c:8"
          ]
        ]
      ]
    },
    "ordinal": 65,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dd404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dd408"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008dd1dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00665c3c"
      ]
    ],
    [
      "008dd4e0",
      "WRITE",
      [
        "storage",
        "00ca420c",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:008dd3fc",
      "READ",
      [
        "storage",
        "002b6805",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008dd1dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00665c7c"
      ]
    ],
    [
      "008dd4e0",
      "WRITE",
      [
        "storage",
        "00ca460c",
        null,
        "undefined4"
      ]
    ],
    [
      "008dd598",
      "READ",
      [
        "storage",
        "002b6845",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008dd040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md#insn-008dd040) · [`008dd1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md#insn-008dd1dc) · [`008dd268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md#insn-008dd268)
- 新版 `008dd1dc`（命令位置の公開資料なし） · `008dd378`（命令位置の公開資料なし） · `008dd404`（命令位置の公開資料なし）

~~~diff
- 008dd040 ["INT_ADD", "register:40f0:8", ["const:8dd040:8", "const:4:8"]]
- 008dd040 ["CALL", null, ["ram:665c3c:8"]]
+ 008dd1dc ["INT_ADD", "register:40f0:8", ["const:8dd1dc:8", "const:4:8"]]
+ 008dd1dc ["CALL", null, ["ram:665c7c:8"]]
- 008dd040 bytes ff22f697
+ 008dd1dc bytes a822f697
- 008dd1dc ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 008dd1dc ["CBRANCH", null, ["local:b80:8", "tmp:0:1"]]
+ 008dd378 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 008dd378 ["CBRANCH", null, ["local:b81:8", "tmp:0:1"]]
- 008dd1dc bytes 0a2b00b5
+ 008dd378 bytes 0a2b00b5
- 008dd268 ["INT_ADD", "register:40f0:8", ["const:8dd268:8", "const:4:8"]]
- 008dd268 ["CALL", null, ["callee:008dd030:8"]]
+ 008dd404 ["INT_ADD", "register:40f0:8", ["const:8dd404:8", "const:4:8"]]
+ 008dd404 ["CALL", null, ["callee:008dd030:8"]]
- 008dd268 bytes 0bffff97
+ 008dd404 bytes 0bffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0223016899896262e5df3b4459de6370"></a>

### [`008dd868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dd868.md) → [`008dda04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dda04.md) FUN_008dda04

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008de8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008de/008de8bc.md) · 呼出先 8件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008dc4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc4c8.md)
- 新版 呼出元 1件 [`008dea58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008de/008dea58.md) · 呼出先 8件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008dc664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dc/008dc664.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.93% / 新版 89.93%

CFGの説明率　旧版 37.84% / 新版 41.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 10件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008dda28",
      "incomplete_value": true,
      "site": "008dda28",
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
      "definition_site": "008dd88c",
      "incomplete_value": true,
      "site": "008dd88c",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008dd900"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008dda9c"
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
      "008dda24",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008dda30",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008dda38",
      "PARAM",
      [
        "storage",
        "00c84c98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008dda24",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008dda30",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008dda38",
      "PARAM",
      [
        "storage",
        "00c85098",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008dd8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dd868.md#insn-008dd8a8) · [`008dd8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dd868.md#insn-008dd8b8) · [`008dd900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dd868.md#insn-008dd900)
- 新版 `008dda44`（命令位置の公開資料なし） · `008dda54`（命令位置の公開資料なし）

~~~diff
- 008dd8a8 ["INT_ADD", "register:40f0:8", ["const:8dd8a8:8", "const:4:8"]]
- 008dd8a8 ["CALL", null, ["callee:00c58610:8"]]
+ 008dda44 ["INT_ADD", "register:40f0:8", ["const:8dda44:8", "const:4:8"]]
+ 008dda44 ["CALL", null, ["callee:00c58610:8"]]
- 008dd8a8 bytes 5aea0d94
+ 008dda44 bytes f3ea0d94
- 008dd8b8 ["INT_ADD", "register:40f0:8", ["const:8dd8b8:8", "const:4:8"]]
- 008dd8b8 ["CALL", null, ["callee:00467860:8"]]
+ 008dda54 ["INT_ADD", "register:40f0:8", ["const:8dda54:8", "const:4:8"]]
+ 008dda54 ["CALL", null, ["callee:00467860:8"]]
- 008dd8b8 bytes da27ee97
+ 008dda54 bytes 8327ee97
- 008dd900 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 008dd900 bytes 40010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bc069cbe99e63f788df1e6f2de11b0a"></a>

### [`008ddb18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008ddb18.md) → [`008ddcb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddcb4.md) FUN_008ddcb4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 13件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0066d09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d09c.md) [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 13件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0066d0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d0dc.md) [`008dd0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dd0f4.md)

変更の種類 branch_condition_or_target, call, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.18% / 新版 74.18%

CFGの説明率　旧版 28.57% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 41件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ddb4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ddb50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ddb98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ddb40",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008ddb44",
      "READ",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008ddb4c",
      "WRITE",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008ddcdc",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008ddce0",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "008ddce8",
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ddb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008ddb18.md#insn-008ddb4c) · [`008ddb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008ddb18.md#insn-008ddb50) · [`008ddb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008ddb18.md#insn-008ddb98)

~~~diff
- 008ddb4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 008ddb4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008ddb4c bytes 09b502f9
- 008ddb50 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:578:8"]]
- 008ddb50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008ddb50 bytes 6abf02f9
- 008ddb98 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:578:8"]]
- 008ddb98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008ddb98 bytes 74bf02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b55426a3262e3371bc4f145bb3cde72"></a>

### [`008dde04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dde04.md) → [`008ddfa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddfa0.md) FUN_008ddfa0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 24件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047d17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d17c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 24件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047d1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1bc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.17% / 新版 87.17%

CFGの説明率　旧版 56.20% / 新版 56.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 6件, `store_condition` 13件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ddec4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008de284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008de44c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008de028",
      "READ",
      [
        "storage",
        "002c4118",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008ddec4",
      "DATA",
      [
        "storage",
        "00332098",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "unmatched:008ddec8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008de0a4"
      ]
    ]
  ],
  "added": [
    [
      "008de028",
      "READ",
      [
        "storage",
        "002c4158",
        null,
        "undefined8"
      ]
    ],
    [
      "008de060",
      "DATA",
      [
        "storage",
        "00332098",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "008de064",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008de0a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ddec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dde04.md#insn-008ddec4) · [`008de284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dde04.md#insn-008de284)
- 新版 `008de060`（命令位置の公開資料なし）

~~~diff
- 008ddec4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:38:8"]]
- 008ddec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:4"]]
- 008ddec4 bytes ee3a00b9
+ 008de060 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:38:8"]]
+ 008de060 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:4"]]
+ 008de060 bytes ee3a00b9
- 008de284 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:37c:8"]]
- 008de284 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008de284 bytes 287f03b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb6ccdaa97fc3e9fc9959708fdea906"></a>

### [`008de8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008de/008de8bc.md) → [`008dea58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008de/008dea58.md) FUN_008dea58

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 25件 [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00468c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 25件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00468c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.77% / 新版 55.77%

CFGの説明率　旧版 13.56% / 新版 13.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 18件, `call_target` 1件, `unresolved_branch_alignment` 27件, `unresolved_call_alignment` 28件, `unresolved_store_alignment` 14件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008df1f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008df1f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008df200"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008de8fc",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "008deaa4",
      "READ",
      [
        "storage",
        "00ca4b30",
        null,
        "undefined8"
      ]
    ],
    [
      "008deab8",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008dea98",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008deaa4",
      "READ",
      [
        "storage",
        "00ca4f30",
        null,
        "undefined8"
      ]
    ],
    [
      "008deab8",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008de98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008de/008de8bc.md#insn-008de98c) · [`008dea84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008de/008de8bc.md#insn-008dea84) · [`008deaa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008de/008de8bc.md#insn-008deaa8)
- 新版 `008dec20`（命令位置の公開資料なし）

~~~diff
- 008de98c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008de98c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 008de98c bytes 600000b4
- 008dea84 ["INT_ADD", "register:40f0:8", ["const:8dea84:8", "const:4:8"]]
- 008dea84 ["CALL", null, ["callee:008dda04:8"]]
+ 008dec20 ["INT_ADD", "register:40f0:8", ["const:8dec20:8", "const:4:8"]]
+ 008dec20 ["CALL", null, ["callee:008dda04:8"]]
- 008dea84 bytes 79fbff97
+ 008dec20 bytes 79fbff97
- 008deaa8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c8:8"]]
- 008deaa8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 008deaa8 bytes 976640f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10c518fd33f36e0cb9d004df301857b3"></a>

### [`008e0890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0890.md) → [`008e0a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e0/008e0a2c.md) FUN_008e0a2c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008e0458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0458.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`008e05f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e0/008e05f4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "008e0a38",
      "incomplete_value": false,
      "site": "008e0a3c",
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
      "definition_site": "008e089c",
      "incomplete_value": false,
      "site": "008e08a0",
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
      "008e0a38",
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
      "008e0a38",
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

- 旧版 [`008e08a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0890.md#insn-008e08a0) · [`008e089c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0890.md#insn-008e089c)
- 新版 `008e0a3c`（命令位置の公開資料なし） · `008e0a38`（命令位置の公開資料なし）

~~~diff
- 008e08a0 ["INT_ADD", "register:40f0:8", ["const:8e08a0:8", "const:4:8"]]
- 008e08a0 ["CALL", null, ["callee:0043b778:8"]]
+ 008e0a3c ["INT_ADD", "register:40f0:8", ["const:8e0a3c:8", "const:4:8"]]
+ 008e0a3c ["CALL", null, ["callee:0043b778:8"]]
- 008e08a0 bytes a66bed97
+ 008e0a3c bytes 4f6bed97
- 008e089c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 008e089c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e089c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e089c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e0a38 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 008e0a38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e0a38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e0a38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e089c bytes 00303c91
+ 008e0a38 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

