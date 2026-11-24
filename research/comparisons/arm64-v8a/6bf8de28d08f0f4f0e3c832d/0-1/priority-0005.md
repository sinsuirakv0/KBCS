# v16.0.0 → v16.0.1 · 最優先の変更候補 (5)

[一覧の目次](README.md)

<a id="compare-5bfce0d0269ac6332402650285bb574a"></a>

### [`00472d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md) → [`00472da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md) FUN_00472da4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 9件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`008532c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/008532c8.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) · 呼出先 5件 [`00472df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md) [`00472fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 9件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`00853308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853308.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) · 呼出先 5件 [`00472e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md) [`00473028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00472dd8",
      "incomplete_value": false,
      "site": "00472ddc",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00472d98",
      "incomplete_value": false,
      "site": "00472d9c",
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
            "const:9e8:8"
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
      "definition_site": "00472de8",
      "incomplete_value": false,
      "site": "00472dec",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00472da8",
      "incomplete_value": false,
      "site": "00472dac",
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
            "const:9a0:8"
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
      "definition_site": "00472df4",
      "incomplete_value": false,
      "site": "00472e08",
      "value": [
        "leaf",
        "const:473028:8"
      ]
    },
    "old": {
      "definition_site": "00472db4",
      "incomplete_value": false,
      "site": "00472dc8",
      "value": [
        "leaf",
        "const:472fe8:8"
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
      "00472db8",
      "READ",
      [
        "storage",
        "00ca49e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00472dc4",
      "DATA",
      [
        "storage",
        "00ca49a0",
        null,
        null
      ]
    ],
    [
      "00472dd8",
      "PARAM",
      [
        "storage",
        "00ca49e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00472db8",
      "READ",
      [
        "storage",
        "00ca4de8",
        null,
        "undefined1"
      ]
    ],
    [
      "00472dc4",
      "DATA",
      [
        "storage",
        "00ca4da0",
        null,
        null
      ]
    ],
    [
      "00472dd8",
      "PARAM",
      [
        "storage",
        "00ca4de8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00472d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md#insn-00472d9c) · [`00472dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md#insn-00472dac) · [`00472dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md#insn-00472dc8)
- 新版 [`00472ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md#insn-00472ddc) · [`00472dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md#insn-00472dec) · [`00472e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md#insn-00472e08)

~~~diff
- 00472d9c ["INT_ADD", "register:40f0:8", ["const:472d9c:8", "const:4:8"]]
- 00472d9c ["CALL", null, ["callee:00c57e50:8"]]
+ 00472ddc ["INT_ADD", "register:40f0:8", ["const:472ddc:8", "const:4:8"]]
+ 00472ddc ["CALL", null, ["callee:00c57e50:8"]]
- 00472d9c bytes 2d931f94
+ 00472ddc bytes 1d941f94
- 00472dac ["INT_ADD", "register:40f0:8", ["const:472dac:8", "const:4:8"]]
- 00472dac ["CALL", null, ["callee:00472e34:8"]]
+ 00472dec ["INT_ADD", "register:40f0:8", ["const:472dec:8", "const:4:8"]]
+ 00472dec ["CALL", null, ["callee:00472e34:8"]]
- 00472dac bytes 12000094
+ 00472dec bytes 12000094
- 00472dc8 ["INT_ADD", "register:40f0:8", ["const:472dc8:8", "const:4:8"]]
- 00472dc8 ["CALL", null, ["callee:00c57e30:8"]]
+ 00472e08 ["INT_ADD", "register:40f0:8", ["const:472e08:8", "const:4:8"]]
+ 00472e08 ["CALL", null, ["callee:00c57e30:8"]]
- 00472dc8 bytes 1a931f94
+ 00472e08 bytes 0a941f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e86835b00d2381dba9a8aa6d7169661"></a>

### [`00472df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md) → [`00472e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md) FUN_00472e34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00472d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md) [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`00472da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md) [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00472e78",
      "incomplete_value": false,
      "site": "00472e7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00472e38",
      "incomplete_value": false,
      "site": "00472e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00472ec0",
      "incomplete_value": false,
      "site": "00472ec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00472e80",
      "incomplete_value": false,
      "site": "00472e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "00472e7c",
      "DATA",
      [
        "storage",
        "00c649b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00472ec4",
      "DATA",
      [
        "storage",
        "00c64a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00472e7c",
      "DATA",
      [
        "storage",
        "00c64db0",
        null,
        "undefined *"
      ]
    ],
    [
      "00472ec4",
      "DATA",
      [
        "storage",
        "00c64e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00472e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md#insn-00472e2c) · [`00472e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md#insn-00472e38) · [`00472e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md#insn-00472e74)
- 新版 [`00472e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md#insn-00472e6c) · [`00472e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md#insn-00472e78) · [`00472eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md#insn-00472eb4)

~~~diff
- 00472e2c ["INT_ADD", "register:40f0:8", ["const:472e2c:8", "const:4:8"]]
- 00472e2c ["CALL", null, ["callee:00c57e90:8"]]
+ 00472e6c ["INT_ADD", "register:40f0:8", ["const:472e6c:8", "const:4:8"]]
+ 00472e6c ["CALL", null, ["callee:00c57e90:8"]]
- 00472e2c bytes 19931f94
+ 00472e6c bytes 09941f94
- 00472e38 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 00472e38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00472e38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00472e38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00472e78 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 00472e78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00472e78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00472e78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00472e38 bytes 08c12691
+ 00472e78 bytes 08c13691
- 00472e74 ["INT_ADD", "register:40f0:8", ["const:472e74:8", "const:4:8"]]
- 00472e74 ["CALL", null, ["callee:00c57e90:8"]]
+ 00472eb4 ["INT_ADD", "register:40f0:8", ["const:472eb4:8", "const:4:8"]]
+ 00472eb4 ["CALL", null, ["callee:00c57e90:8"]]
- 00472e74 bytes 07931f94
+ 00472eb4 bytes f7931f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e91e4d361281aef344a8ae97f0a89604"></a>

### [`00472fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md) → [`00473028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md) FUN_00473028

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00472d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md) [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) · 呼出先 9件 [`00474e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474e88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)
- 新版 呼出元 3件 [`00472da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md) [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) · 呼出先 9件 [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047304c",
      "incomplete_value": false,
      "site": "00473050",
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
            "const:fe5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047300c",
      "incomplete_value": false,
      "site": "00473010",
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
            "const:fa5:8"
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
      "0047304c",
      "PARAM",
      [
        "storage",
        "002b7fa5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047304c",
      "PARAM",
      [
        "storage",
        "002b7fe5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00473010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md#insn-00473010) · [`0047300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md#insn-0047300c) · [`0047301c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md#insn-0047301c)
- 新版 [`00473050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md#insn-00473050) · [`0047304c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md#insn-0047304c) · [`0047305c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md#insn-0047305c)

~~~diff
- 00473010 ["INT_ADD", "register:40f0:8", ["const:473010:8", "const:4:8"]]
- 00473010 ["CALL", null, ["callee:00c58470:8"]]
+ 00473050 ["INT_ADD", "register:40f0:8", ["const:473050:8", "const:4:8"]]
+ 00473050 ["CALL", null, ["callee:00c58470:8"]]
- 00473010 bytes 18941f94
+ 00473050 bytes 08951f94
- 0047300c ["COPY", "tmp:0:8", ["const:fa5:8"]]
- 0047300c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047300c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047300c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047304c ["COPY", "tmp:0:8", ["const:fe5:8"]]
+ 0047304c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047304c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047304c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047300c bytes 00943e91
+ 0047304c bytes 00943f91
- 0047301c ["INT_ADD", "register:40f0:8", ["const:47301c:8", "const:4:8"]]
- 0047301c ["CALL", null, ["callee:00c580e0:8"]]
+ 0047305c ["INT_ADD", "register:40f0:8", ["const:47305c:8", "const:4:8"]]
+ 0047305c ["CALL", null, ["callee:00c580e0:8"]]
- 0047301c bytes 31931f94
+ 0047305c bytes 21941f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-165186c7506ee5ec269466700debe22f"></a>

### [`00473154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473154.md) → [`00473194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473194.md) FUN_00473194

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 4件 [`00475838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475838.md) [`0047583c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/0047583c.md) [`0055096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055096c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 4件 [`00475878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475878.md) [`0047587c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047587c.md) [`005509ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509ac.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004731c0",
      "incomplete_value": false,
      "site": "004731c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473180",
      "incomplete_value": false,
      "site": "00473180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "004731c0",
      "DATA",
      [
        "storage",
        "00c64a50",
        null,
        "undefined *"
      ]
    ],
    [
      "004731f4",
      "READ",
      [
        "storage",
        "00c64a70",
        null,
        "pointer"
      ]
    ],
    [
      "004731f4",
      "READ",
      [
        "storage",
        "00c64a78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004731c0",
      "DATA",
      [
        "storage",
        "00c64e50",
        null,
        "undefined *"
      ]
    ],
    [
      "004731f4",
      "READ",
      [
        "storage",
        "00c64e70",
        null,
        "pointer"
      ]
    ],
    [
      "004731f4",
      "READ",
      [
        "storage",
        "00c64e78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00473178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473154.md#insn-00473178) · [`0047318c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473154.md#insn-0047318c) · [`004731b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473154.md#insn-004731b8)
- 新版 [`004731b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473194.md#insn-004731b8) · [`004731cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473194.md#insn-004731cc) · [`004731f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473194.md#insn-004731f8)

~~~diff
- 00473178 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 00473178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00473178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00473178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004731b8 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 004731b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004731b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004731b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00473178 bytes 08412991
+ 004731b8 bytes 08413991
- 0047318c ["INT_ADD", "register:40f0:8", ["const:47318c:8", "const:4:8"]]
- 0047318c ["CALL", null, ["callee:005509ac:8"]]
+ 004731cc ["INT_ADD", "register:40f0:8", ["const:4731cc:8", "const:4:8"]]
+ 004731cc ["CALL", null, ["callee:005509ac:8"]]
- 0047318c bytes f8750394
+ 004731cc bytes f8750394
- 004731b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004731b8 ["INT_ADD", "register:40f0:8", ["const:4731b8:8", "const:4:8"]]
- 004731b8 ["CALLIND", null, ["register:0:8"]]
+ 004731f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004731f8 ["INT_ADD", "register:40f0:8", ["const:4731f8:8", "const:4:8"]]
+ 004731f8 ["CALLIND", null, ["register:0:8"]]
- 004731b8 bytes 00013fd6
+ 004731f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b44f15daf6087a925189a1e47940058"></a>

### [`00473230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473230.md) → [`00473270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473270.md) FUN_00473270

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`008532c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/008532c8.md) [`00922c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00922/00922c2c.md) [`00a8a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) · 呼出先 10件 [`00475d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md) [`00768388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768388.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00853308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853308.md) [`00922dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00922/00922dc8.md) [`00a8a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) · 呼出先 10件 [`00475da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md) [`007683c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007683c8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00473298",
      "value": [
        "leaf",
        "ram:7683c8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00473258",
      "value": [
        "leaf",
        "ram:768388:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004732d4",
      "incomplete_value": false,
      "site": "004732e0",
      "value": [
        "leaf",
        "const:475da0:8"
      ]
    },
    "old": {
      "definition_site": "00473294",
      "incomplete_value": false,
      "site": "004732a0",
      "value": [
        "leaf",
        "const:475d60:8"
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047333c",
      "incomplete_value": false,
      "site": "00473340",
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
            "const:f27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004732fc",
      "incomplete_value": false,
      "site": "00473300",
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
            "const:e5a:8"
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
      "00473298",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768388"
      ]
    ],
    [
      "004732d4",
      "PARAM",
      [
        "storage",
        "00475d60",
        null,
        null
      ]
    ],
    [
      "0047333c",
      "PARAM",
      [
        "storage",
        "002a3e5a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00473298",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683c8"
      ]
    ],
    [
      "004732d4",
      "PARAM",
      [
        "storage",
        "00475da0",
        null,
        null
      ]
    ],
    [
      "0047333c",
      "PARAM",
      [
        "storage",
        "002a3f27",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00473258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473230.md#insn-00473258) · [`004732a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473230.md#insn-004732a0) · [`004732c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473230.md#insn-004732c0)
- 新版 [`00473298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473270.md#insn-00473298) · [`004732e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473270.md#insn-004732e0) · [`00473300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473270.md#insn-00473300)

~~~diff
- 00473258 ["INT_ADD", "register:40f0:8", ["const:473258:8", "const:4:8"]]
- 00473258 ["CALL", null, ["ram:768388:8"]]
+ 00473298 ["INT_ADD", "register:40f0:8", ["const:473298:8", "const:4:8"]]
+ 00473298 ["CALL", null, ["ram:7683c8:8"]]
- 00473258 bytes 4cd40b94
+ 00473298 bytes 4cd40b94
- 004732a0 ["INT_ADD", "register:40f0:8", ["const:4732a0:8", "const:4:8"]]
- 004732a0 ["CALL", null, ["callee:00c58110:8"]]
+ 004732e0 ["INT_ADD", "register:40f0:8", ["const:4732e0:8", "const:4:8"]]
+ 004732e0 ["CALL", null, ["callee:00c58110:8"]]
- 004732a0 bytes 9c921f94
+ 004732e0 bytes 8c931f94
- 004732c0 ["INT_ADD", "register:40f0:8", ["const:4732c0:8", "const:4:8"]]
- 004732c0 ["CALL", null, ["callee:00c58180:8"]]
+ 00473300 ["INT_ADD", "register:40f0:8", ["const:473300:8", "const:4:8"]]
+ 00473300 ["CALL", null, ["callee:00c58180:8"]]
- 004732c0 bytes b0921f94
+ 00473300 bytes a0931f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb074a0fd8a73ebf0f44ff3ac0039a06"></a>

### [`00473354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473354.md) → [`00473394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473394.md) FUN_00473394

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`0047971c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047971c.md) [`00479720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479720.md) [`00550960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550960.md)
- 新版 呼出元 1件 [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`0047975c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047975c.md) [`00479760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479760.md) [`005509a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047340c",
      "incomplete_value": false,
      "site": "0047340c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004733cc",
      "incomplete_value": false,
      "site": "004733cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047340c",
      "DATA",
      [
        "storage",
        "00c64b60",
        null,
        "undefined *"
      ]
    ],
    [
      "00473448",
      "READ",
      [
        "storage",
        "00c64b80",
        null,
        "pointer"
      ]
    ],
    [
      "00473448",
      "READ",
      [
        "storage",
        "00c64b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047340c",
      "DATA",
      [
        "storage",
        "00c64f60",
        null,
        "undefined *"
      ]
    ],
    [
      "00473448",
      "READ",
      [
        "storage",
        "00c64f80",
        null,
        "pointer"
      ]
    ],
    [
      "00473448",
      "READ",
      [
        "storage",
        "00c64f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047340c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473354.md#insn-0047340c) · [`004733b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473354.md#insn-004733b0) · [`004733c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473354.md#insn-004733c0)
- 新版 [`0047344c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473394.md#insn-0047344c) · [`004733f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473394.md#insn-004733f0) · [`00473400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473394.md#insn-00473400)

~~~diff
- 0047340c ["COPY", "register:0:8", ["register:4040:8"]]
- 0047340c ["INT_ADD", "register:40f0:8", ["const:47340c:8", "const:4:8"]]
- 0047340c ["CALLIND", null, ["register:0:8"]]
+ 0047344c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047344c ["INT_ADD", "register:40f0:8", ["const:47344c:8", "const:4:8"]]
+ 0047344c ["CALLIND", null, ["register:0:8"]]
- 0047340c bytes 00013fd6
+ 0047344c bytes 00013fd6
- 004733b0 ["INT_ADD", "register:40f0:8", ["const:4733b0:8", "const:4:8"]]
- 004733b0 ["CALL", null, ["callee:0043bb20:8"]]
+ 004733f0 ["INT_ADD", "register:40f0:8", ["const:4733f0:8", "const:4:8"]]
+ 004733f0 ["CALL", null, ["callee:0043bb20:8"]]
- 004733b0 bytes cc21ff97
+ 004733f0 bytes cc21ff97
- 004733c0 ["INT_ADD", "register:40f0:8", ["const:4733c0:8", "const:4:8"]]
- 004733c0 ["CALL", null, ["callee:00473540:8"]]
+ 00473400 ["INT_ADD", "register:40f0:8", ["const:473400:8", "const:4:8"]]
+ 00473400 ["CALL", null, ["callee:00473540:8"]]
- 004733c0 bytes 50000094
+ 00473400 bytes 50000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7606169b395d75b7ff2f3ba038157546"></a>

### [`00473650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473650.md) → [`00473690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473690.md) FUN_00473690

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 4件 [`004797d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004797d4.md) [`004797d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004797d8.md) [`00550960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550960.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 4件 [`00479814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479814.md) [`00479818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479818.md) [`005509a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004736cc",
      "incomplete_value": false,
      "site": "004736cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047368c",
      "incomplete_value": false,
      "site": "0047368c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "004736cc",
      "DATA",
      [
        "storage",
        "00c64bf0",
        null,
        "undefined *"
      ]
    ],
    [
      "00473704",
      "READ",
      [
        "storage",
        "00c64c10",
        null,
        "pointer"
      ]
    ],
    [
      "00473704",
      "READ",
      [
        "storage",
        "00c64c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004736cc",
      "DATA",
      [
        "storage",
        "00c64ff0",
        null,
        "undefined *"
      ]
    ],
    [
      "00473704",
      "READ",
      [
        "storage",
        "00c65010",
        null,
        "pointer"
      ]
    ],
    [
      "00473704",
      "READ",
      [
        "storage",
        "00c65018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00473688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473650.md#insn-00473688) · [`0047369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473650.md#insn-0047369c) · [`004736c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473650.md#insn-004736c8)
- 新版 [`004736c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473690.md#insn-004736c8) · [`004736dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473690.md#insn-004736dc) · [`00473708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473690.md#insn-00473708)

~~~diff
- 00473688 ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 00473688 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00473688 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00473688 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004736c8 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 004736c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004736c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004736c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00473688 bytes 29c12f91
+ 004736c8 bytes 29c13f91
- 0047369c ["INT_ADD", "register:40f0:8", ["const:47369c:8", "const:4:8"]]
- 0047369c ["CALL", null, ["callee:005509a0:8"]]
+ 004736dc ["INT_ADD", "register:40f0:8", ["const:4736dc:8", "const:4:8"]]
+ 004736dc ["CALL", null, ["callee:005509a0:8"]]
- 0047369c bytes b1740394
+ 004736dc bytes b1740394
- 004736c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004736c8 ["INT_ADD", "register:40f0:8", ["const:4736c8:8", "const:4:8"]]
- 004736c8 ["CALLIND", null, ["register:0:8"]]
+ 00473708 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473708 ["INT_ADD", "register:40f0:8", ["const:473708:8", "const:4:8"]]
+ 00473708 ["CALLIND", null, ["register:0:8"]]
- 004736c8 bytes 00013fd6
+ 00473708 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-482c241e08367b29cb8d1ae7b9b60569"></a>

### [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) → [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) FUN_0047377c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 20件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044b544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b544.md) [`00474158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md) [`00479aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479aa8.md) [`00479f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479f0c.md)
- 新版 呼出元 3件 [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 20件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b584.md) [`00474198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md) [`00479ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479ae8.md) [`00479f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f4c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.02% / 新版 96.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00473838",
      "incomplete_value": true,
      "site": "00473848",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:833:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004737f8",
      "incomplete_value": true,
      "site": "00473808",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047383c",
      "incomplete_value": true,
      "site": "0047384c",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004737fc",
      "incomplete_value": true,
      "site": "0047380c",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00473840",
      "incomplete_value": true,
      "site": "00473850",
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
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473800",
      "incomplete_value": true,
      "site": "00473810",
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
                "const:a50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00473838",
      "READ",
      [
        "storage",
        "002af7f3",
        null,
        "string"
      ]
    ],
    [
      "0047383c",
      "READ",
      [
        "storage",
        "002af7fd",
        null,
        "string"
      ]
    ],
    [
      "00473840",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00473838",
      "READ",
      [
        "storage",
        "002af833",
        null,
        "string"
      ]
    ],
    [
      "0047383c",
      "READ",
      [
        "storage",
        "002af83d",
        null,
        "string"
      ]
    ],
    [
      "00473840",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004737cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md#insn-004737cc) · [`0047382c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md#insn-0047382c) · [`004739f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md#insn-004739f8)
- 新版 [`0047380c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md#insn-0047380c) · [`0047386c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md#insn-0047386c) · [`00473a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md#insn-00473a38)

~~~diff
- 004737cc ["INT_ADD", "register:40f0:8", ["const:4737cc:8", "const:4:8"]]
- 004737cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047380c ["INT_ADD", "register:40f0:8", ["const:47380c:8", "const:4:8"]]
+ 0047380c ["CALL", null, ["callee:00c57eb0:8"]]
- 004737cc bytes b9901f94
+ 0047380c bytes a9911f94
- 0047382c ["INT_ADD", "register:40f0:8", ["const:47382c:8", "const:4:8"]]
- 0047382c ["CALL", null, ["callee:00474198:8"]]
+ 0047386c ["INT_ADD", "register:40f0:8", ["const:47386c:8", "const:4:8"]]
+ 0047386c ["CALL", null, ["callee:00474198:8"]]
- 0047382c bytes 4b020094
+ 0047386c bytes 4b020094
- 004739f8 ["INT_ADD", "register:40f0:8", ["const:4739f8:8", "const:4:8"]]
- 004739f8 ["CALL", null, ["callee:00c57f70:8"]]
+ 00473a38 ["INT_ADD", "register:40f0:8", ["const:473a38:8", "const:4:8"]]
+ 00473a38 ["CALL", null, ["callee:00c57f70:8"]]
- 004739f8 bytes 5e901f94
+ 00473a38 bytes 4e911f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e88bf2aca7e607140e1c00c7f1aacb24"></a>

### [`00474158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md) → [`00474198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md) FUN_00474198

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 17件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) [`00474158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md) [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) [`0048bfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md) [`00623f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623f28.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 17件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) [`00474198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md) [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) [`0048c000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048c000.md) [`00623f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623f68.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004742e8",
      "incomplete_value": false,
      "site": "004742f0",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004742a8",
      "incomplete_value": false,
      "site": "004742b0",
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
            "const:f13:8"
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
      "definition_site": "004743a4",
      "incomplete_value": false,
      "site": "004743ac",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474364",
      "incomplete_value": false,
      "site": "0047436c",
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
            "const:da7:8"
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
      "definition_site": "004743bc",
      "incomplete_value": false,
      "site": "004743c8",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047437c",
      "incomplete_value": false,
      "site": "00474388",
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
            "const:ea9:8"
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
      "004742e8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "004743a4",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "004743bc",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004742e8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "004743a4",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "004743bc",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004742b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md#insn-004742b0) · [`0047436c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md#insn-0047436c) · [`00474388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md#insn-00474388)
- 新版 [`004742f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md#insn-004742f0) · [`004743ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md#insn-004743ac) · [`004743c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md#insn-004743c8)

~~~diff
- 004742b0 ["INT_ADD", "register:40f0:8", ["const:4742b0:8", "const:4:8"]]
- 004742b0 ["CALL", null, ["callee:00441e94:8"]]
+ 004742f0 ["INT_ADD", "register:40f0:8", ["const:4742f0:8", "const:4:8"]]
+ 004742f0 ["CALL", null, ["callee:00441e94:8"]]
- 004742b0 bytes e936ff97
+ 004742f0 bytes e936ff97
- 0047436c ["INT_ADD", "register:40f0:8", ["const:47436c:8", "const:4:8"]]
- 0047436c ["CALL", null, ["callee:00441e94:8"]]
+ 004743ac ["INT_ADD", "register:40f0:8", ["const:4743ac:8", "const:4:8"]]
+ 004743ac ["CALL", null, ["callee:00441e94:8"]]
- 0047436c bytes ba36ff97
+ 004743ac bytes ba36ff97
- 00474388 ["INT_ADD", "register:40f0:8", ["const:474388:8", "const:4:8"]]
- 00474388 ["CALL", null, ["callee:004427f4:8"]]
+ 004743c8 ["INT_ADD", "register:40f0:8", ["const:4743c8:8", "const:4:8"]]
+ 004743c8 ["CALL", null, ["callee:004427f4:8"]]
- 00474388 bytes 0b39ff97
+ 004743c8 bytes 0b39ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0cfa85503bd91d51e328a129dc49d13"></a>

### [`00474a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474a78.md) → [`00474ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ab8.md) FUN_00474ab8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "00474abc",
      "incomplete_value": false,
      "site": "00474ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474a7c",
      "incomplete_value": false,
      "site": "00474a80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
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
      "00474ac0",
      "DATA",
      [
        "storage",
        "00c649b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474ac0",
      "DATA",
      [
        "storage",
        "00c64db0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474a78.md#insn-00474a7c)
- 新版 [`00474abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ab8.md#insn-00474abc)

~~~diff
- 00474a7c ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 00474a7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00474a7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00474a7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00474abc ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 00474abc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00474abc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00474abc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00474a7c bytes 08c12691
+ 00474abc bytes 08c13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98b1c55a9737c4b5a945b7305921240a"></a>

### [`00474a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474a88.md) → [`00474ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ac8.md) FUN_00474ac8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00474ad8",
      "incomplete_value": false,
      "site": "00474ae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474a98",
      "incomplete_value": false,
      "site": "00474aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
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
      "00474ae0",
      "DATA",
      [
        "storage",
        "00c649b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474ae0",
      "DATA",
      [
        "storage",
        "00c64db0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474a88.md#insn-00474a98) · [`00474aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474a88.md#insn-00474aa4)
- 新版 [`00474ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ac8.md#insn-00474ad8) · [`00474ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ac8.md#insn-00474ae4)

~~~diff
- 00474a98 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 00474a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00474a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00474a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00474ad8 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 00474ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00474ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00474ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00474a98 bytes 08c12691
+ 00474ad8 bytes 08c13691
- 00474aa4 ["INT_ADD", "register:40f0:8", ["const:474aa4:8", "const:4:8"]]
- 00474aa4 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00474ae4 ["INT_ADD", "register:40f0:8", ["const:474ae4:8", "const:4:8"]]
+ 00474ae4 ["CALL", null, ["callee:00c57ea0:8"]]
- 00474aa4 bytes ff8b1f94
+ 00474ae4 bytes ef8c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3725c6f28496fd5a51aadb53ab951979"></a>

### [`00474c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474c7c.md) → [`00474cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cbc.md) FUN_00474cbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "00474cc0",
      "incomplete_value": false,
      "site": "00474cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474c80",
      "incomplete_value": false,
      "site": "00474c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "00474cc4",
      "DATA",
      [
        "storage",
        "00c64a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474cc4",
      "DATA",
      [
        "storage",
        "00c64e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474c7c.md#insn-00474c80)
- 新版 [`00474cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cbc.md#insn-00474cc0)

~~~diff
- 00474c80 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00474c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00474c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00474c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00474cc0 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00474cc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00474cc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00474cc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00474c80 bytes 08012891
+ 00474cc0 bytes 08013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14fe783cedb96474dcdd2b3f88e6e267"></a>

### [`00474c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474c8c.md) → [`00474ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ccc.md) FUN_00474ccc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00474cdc",
      "incomplete_value": false,
      "site": "00474ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474c9c",
      "incomplete_value": false,
      "site": "00474ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "00474ce4",
      "DATA",
      [
        "storage",
        "00c64a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474ce4",
      "DATA",
      [
        "storage",
        "00c64e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474c8c.md#insn-00474c9c) · [`00474ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474c8c.md#insn-00474ca8)
- 新版 [`00474cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ccc.md#insn-00474cdc) · [`00474ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ccc.md#insn-00474ce8)

~~~diff
- 00474c9c ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00474c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00474c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00474c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00474cdc ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00474cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00474cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00474cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00474c9c bytes 08012891
+ 00474cdc bytes 08013891
- 00474ca8 ["INT_ADD", "register:40f0:8", ["const:474ca8:8", "const:4:8"]]
- 00474ca8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00474ce8 ["INT_ADD", "register:40f0:8", ["const:474ce8:8", "const:4:8"]]
+ 00474ce8 ["CALL", null, ["callee:00c57ea0:8"]]
- 00474ca8 bytes 7e8b1f94
+ 00474ce8 bytes 6e8c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673b81ad45d2611111bf9133efddc714"></a>

### [`004757f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004757f0.md) → [`00475830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475830.md) FUN_00475830

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00475854",
      "incomplete_value": false,
      "site": "00475854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475814",
      "incomplete_value": false,
      "site": "00475814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "00475854",
      "DATA",
      [
        "storage",
        "00c64a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00475854",
      "DATA",
      [
        "storage",
        "00c64e50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004757f0.md#insn-00475804) · [`00475810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/004757f0.md#insn-00475810)
- 新版 [`00475844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475830.md#insn-00475844) · [`00475850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475830.md#insn-00475850)

~~~diff
- 00475804 ["INT_ADD", "register:40f0:8", ["const:475804:8", "const:4:8"]]
- 00475804 ["CALL", null, ["callee:00c57e90:8"]]
+ 00475844 ["INT_ADD", "register:40f0:8", ["const:475844:8", "const:4:8"]]
+ 00475844 ["CALL", null, ["callee:00c57e90:8"]]
- 00475804 bytes a3881f94
+ 00475844 bytes 93891f94
- 00475810 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 00475810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00475810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00475810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00475850 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00475850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00475850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00475850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00475810 bytes 08412991
+ 00475850 bytes 08413991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae1a304b5e3018dc3b37b3369e3101b2"></a>

### [`00475824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475824.md) → [`00475864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475864.md) FUN_00475864

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00475870",
      "incomplete_value": false,
      "site": "00475870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475830",
      "incomplete_value": false,
      "site": "00475830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "00475870",
      "DATA",
      [
        "storage",
        "00c64a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00475870",
      "DATA",
      [
        "storage",
        "00c64e50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047582c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475824.md#insn-0047582c)
- 新版 [`0047586c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475864.md#insn-0047586c)

~~~diff
- 0047582c ["COPY", "tmp:0:8", ["const:a50:8"]]
- 0047582c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047582c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047582c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047586c ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 0047586c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047586c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047586c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047582c bytes 29412991
+ 0047586c bytes 29413991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad9042368a706fda22a2521c9bbb7047"></a>

### [`00475d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md) → [`00475da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md) FUN_00475da0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00473230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473230.md) · 呼出先 16件 [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) [`00476548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476548.md) [`00478c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c84.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00473270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473270.md) · 呼出先 16件 [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) [`00476588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476588.md) [`00478cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.54% / 新版 98.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00475df4",
      "incomplete_value": false,
      "site": "00475df8",
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
            "const:5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475db4",
      "incomplete_value": false,
      "site": "00475db8",
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
            "const:fc5:8"
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
      "definition_site": "00476038",
      "incomplete_value": false,
      "site": "0047603c",
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
            "const:3f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475ff8",
      "incomplete_value": false,
      "site": "00475ffc",
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
            "const:3b9:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00475df4",
      "PARAM",
      [
        "storage",
        "002b7fc5",
        null,
        "string"
      ]
    ],
    [
      "00475e08",
      "READ",
      [
        "storage",
        "002c43c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00476038",
      "PARAM",
      [
        "storage",
        "002bc3b9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00475df4",
      "PARAM",
      [
        "storage",
        "002b8005",
        null,
        "string"
      ]
    ],
    [
      "00475e08",
      "READ",
      [
        "storage",
        "002c4400",
        null,
        "undefined8"
      ]
    ],
    [
      "00476038",
      "PARAM",
      [
        "storage",
        "002bc3f9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md#insn-00475db8) · [`00475fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md#insn-00475fbc) · [`00475ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md#insn-00475ffc)
- 新版 [`00475df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md#insn-00475df8) · [`00475ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md#insn-00475ffc) · [`0047603c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md#insn-0047603c)

~~~diff
- 00475db8 ["INT_ADD", "register:40f0:8", ["const:475db8:8", "const:4:8"]]
- 00475db8 ["CALL", null, ["callee:00c58470:8"]]
+ 00475df8 ["INT_ADD", "register:40f0:8", ["const:475df8:8", "const:4:8"]]
+ 00475df8 ["CALL", null, ["callee:00c58470:8"]]
- 00475db8 bytes ae881f94
+ 00475df8 bytes 9e891f94
- 00475fbc ["INT_ADD", "register:40f0:8", ["const:475fbc:8", "const:4:8"]]
- 00475fbc ["CALL", null, ["callee:00c580f0:8"]]
+ 00475ffc ["INT_ADD", "register:40f0:8", ["const:475ffc:8", "const:4:8"]]
+ 00475ffc ["CALL", null, ["callee:00c580f0:8"]]
- 00475fbc bytes 4d871f94
+ 00475ffc bytes 3d881f94
- 00475ffc ["INT_ADD", "register:40f0:8", ["const:475ffc:8", "const:4:8"]]
- 00475ffc ["CALL", null, ["callee:00c58470:8"]]
+ 0047603c ["INT_ADD", "register:40f0:8", ["const:47603c:8", "const:4:8"]]
+ 0047603c ["CALL", null, ["callee:00c58470:8"]]
- 00475ffc bytes 1d881f94
+ 0047603c bytes 0d891f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeabb26fcfa5db34684bf796b95110ab"></a>

### [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) → [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) FUN_004761a4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00475d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00475/00475d60.md) · 呼出先 11件 [`00474158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00474/00474158.md) [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) [`00477dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md)
- 新版 呼出元 1件 [`00475da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md) · 呼出先 11件 [`00474198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md) [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) [`00477e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/00477e0c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00476204",
      "incomplete_value": true,
      "site": "00476220",
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
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004761c4",
      "incomplete_value": true,
      "site": "004761e0",
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
                "const:a50:8"
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
      "00476204",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ],
    [
      "004762e8",
      "READ",
      [
        "storage",
        "002af7f3",
        null,
        "string"
      ]
    ],
    [
      "004762f8",
      "READ",
      [
        "storage",
        "002af7fd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00476204",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ],
    [
      "004762e8",
      "READ",
      [
        "storage",
        "002af833",
        null,
        "string"
      ]
    ],
    [
      "004762f8",
      "READ",
      [
        "storage",
        "002af83d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004761b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md#insn-004761b4) · [`004761c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md#insn-004761c4) · [`004761cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md#insn-004761cc)
- 新版 [`004761f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md#insn-004761f4) · [`00476204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md#insn-00476204)

~~~diff
- 004761b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004761b4 ["INT_ADD", "register:40f0:8", ["const:4761b4:8", "const:4:8"]]
- 004761b4 ["CALLIND", null, ["register:0:8"]]
+ 004761f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004761f4 ["INT_ADD", "register:40f0:8", ["const:4761f4:8", "const:4:8"]]
+ 004761f4 ["CALLIND", null, ["register:0:8"]]
- 004761b4 bytes 20013fd6
+ 004761f4 bytes 20013fd6
- 004761c4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a50:8"]]
- 004761c4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 004761c4 ["COPY", "register:5010:8", ["const:0:8"]]
- 004761c4 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00476204 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a90:8"]]
+ 00476204 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00476204 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00476204 ["COPY", "register:5018:8", ["const:0:8"]]
- 004761c4 bytes 2095c23d
+ 00476204 bytes 20a5c23d
- 004761cc ["COPY", "register:40c8:8", ["const:2af000:8"]]
- 004761cc bytes d9f1ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edc1482b1bffee349d084b9d47e93666"></a>

### [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) → [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) FUN_004766c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) · 呼出先 23件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`0045399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md) [`00472df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md) [`00472fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md) [`00478108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md)
- 新版 呼出元 1件 [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) · 呼出先 23件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) [`00472e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md) [`00473028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md) [`00478148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.83% / 新版 93.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047673c",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004766fc",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00476700"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00476748",
      "value": [
        "leaf",
        "ram:764ee0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00476708",
      "value": [
        "leaf",
        "ram:764ea0:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047673c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ],
    [
      "unmatched:00476700",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "00476748",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ],
  "added": [
    [
      "0047673c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "00476740",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "00476748",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004766c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md#insn-004766c0) · [`004766fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md#insn-004766fc) · [`00476700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md#insn-00476700)
- 新版 [`00476700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md#insn-00476700) · [`0047673c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md#insn-0047673c)

~~~diff
- 004766c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004766c0 ["INT_ADD", "register:40f0:8", ["const:4766c0:8", "const:4:8"]]
- 004766c0 ["CALLIND", null, ["register:0:8"]]
+ 00476700 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00476700 ["INT_ADD", "register:40f0:8", ["const:476700:8", "const:4:8"]]
+ 00476700 ["CALLIND", null, ["register:0:8"]]
- 004766c0 bytes 20013fd6
+ 00476700 bytes 20013fd6
- 004766fc ["INT_ADD", "register:40f0:8", ["const:4766fc:8", "const:4:8"]]
- 004766fc ["CALL", null, ["ram:764344:8"]]
+ 0047673c ["INT_ADD", "register:40f0:8", ["const:47673c:8", "const:4:8"]]
+ 0047673c ["CALL", null, ["ram:764384:8"]]
- 004766fc bytes 12b70b94
+ 0047673c bytes 12b70b94
- 00476700 ["INT_ADD", "register:40f0:8", ["const:476700:8", "const:4:8"]]
- 00476700 ["CALL", null, ["callee:008514f8:8"]]
- 00476700 bytes 6e6b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be817cc48a3651489ed3e992a930dcc4"></a>

### [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) → [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) FUN_00476b50

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) · 呼出先 22件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0044b668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b668.md) [`004782d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md)
- 新版 呼出元 1件 [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) · 呼出先 22件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0044b6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b6a8.md) [`00478314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.95% / 新版 98.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047737c",
      "incomplete_value": true,
      "site": "0047737c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
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
      "definition_site": "0047733c",
      "incomplete_value": true,
      "site": "0047733c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 64,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00476c1c",
      "incomplete_value": false,
      "site": "00476c28",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476bdc",
      "incomplete_value": false,
      "site": "00476be8",
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
            "const:f98:8"
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
      "definition_site": "00476ce8",
      "incomplete_value": false,
      "site": "00476cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:5a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476ca8",
      "incomplete_value": false,
      "site": "00476cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:1a:8"
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
      "00476c1c",
      "PARAM",
      [
        "storage",
        "002b7f98",
        null,
        "string"
      ]
    ],
    [
      "00476ce8",
      "PARAM",
      [
        "storage",
        "002ba01a",
        null,
        "string"
      ]
    ],
    [
      "00476e40",
      "PARAM",
      [
        "storage",
        "002ad63a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00476c1c",
      "PARAM",
      [
        "storage",
        "002b7fd8",
        null,
        "string"
      ]
    ],
    [
      "00476ce8",
      "PARAM",
      [
        "storage",
        "002ba05a",
        null,
        "string"
      ]
    ],
    [
      "00476e40",
      "PARAM",
      [
        "storage",
        "002ad67a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00476be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md#insn-00476be8) · [`00476cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md#insn-00476cb4) · [`00476e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md#insn-00476e0c)
- 新版 [`00476c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md#insn-00476c28) · [`00476cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md#insn-00476cf4) · [`00476e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md#insn-00476e4c)

~~~diff
- 00476be8 ["INT_ADD", "register:40f0:8", ["const:476be8:8", "const:4:8"]]
- 00476be8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00476c28 ["INT_ADD", "register:40f0:8", ["const:476c28:8", "const:4:8"]]
+ 00476c28 ["CALL", null, ["callee:00c57f60:8"]]
- 00476be8 bytes de831f94
+ 00476c28 bytes ce841f94
- 00476cb4 ["INT_ADD", "register:40f0:8", ["const:476cb4:8", "const:4:8"]]
- 00476cb4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00476cf4 ["INT_ADD", "register:40f0:8", ["const:476cf4:8", "const:4:8"]]
+ 00476cf4 ["CALL", null, ["callee:00c57f60:8"]]
- 00476cb4 bytes ab831f94
+ 00476cf4 bytes 9b841f94
- 00476e0c ["INT_ADD", "register:40f0:8", ["const:476e0c:8", "const:4:8"]]
- 00476e0c ["CALL", null, ["callee:00c57f60:8"]]
+ 00476e4c ["INT_ADD", "register:40f0:8", ["const:476e4c:8", "const:4:8"]]
+ 00476e4c ["CALL", null, ["callee:00c57f60:8"]]
- 00476e0c bytes 55831f94
+ 00476e4c bytes 45841f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31dd8c07042a390ecebe6e5088b3d9ac"></a>

### [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) → [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) FUN_004779cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) · 呼出先 20件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`0045399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00453/0045399c.md) [`00472df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472df4.md) [`00472fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472fe8.md) [`00478108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md)
- 新版 呼出元 1件 [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) · 呼出先 20件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) [`00472e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md) [`00473028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md) [`00478148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 92.38% / 新版 92.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件, `store_value` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00477acc",
      "incomplete_value": true,
      "site": "00477ad8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:190:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477a8c",
      "incomplete_value": true,
      "site": "00477a98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00477a28",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004779e8",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "004779ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00477a28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ],
    [
      "unmatched:004779ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "00477a34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ],
  "added": [
    [
      "00477a28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "00477a2c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "00477a34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004779e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md#insn-004779e8) · [`004779ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md#insn-004779ec) · [`004779f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md#insn-004779f4)
- 新版 [`00477a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md#insn-00477a28) · [`00477a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md#insn-00477a34)

~~~diff
- 004779e8 ["INT_ADD", "register:40f0:8", ["const:4779e8:8", "const:4:8"]]
- 004779e8 ["CALL", null, ["ram:764344:8"]]
+ 00477a28 ["INT_ADD", "register:40f0:8", ["const:477a28:8", "const:4:8"]]
+ 00477a28 ["CALL", null, ["ram:764384:8"]]
- 004779e8 bytes 57b20b94
+ 00477a28 bytes 57b20b94
- 004779ec ["INT_ADD", "register:40f0:8", ["const:4779ec:8", "const:4:8"]]
- 004779ec ["CALL", null, ["callee:008514f8:8"]]
- 004779ec bytes b3660f94
- 004779f4 ["INT_ADD", "register:40f0:8", ["const:4779f4:8", "const:4:8"]]
- 004779f4 ["CALL", null, ["ram:764ea0:8"]]
+ 00477a34 ["INT_ADD", "register:40f0:8", ["const:477a34:8", "const:4:8"]]
+ 00477a34 ["CALL", null, ["ram:764ee0:8"]]
- 004779f4 bytes 2bb50b94
+ 00477a34 bytes 2bb50b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91f70c4d8e6ece86731003c43463b026"></a>

### [`00477dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md) → [`00477e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/00477e0c.md) FUN_00477e0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) · 呼出先 10件 [`0044b544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b544.md) [`00478c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c50.md) [`00478c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c54.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 2件 [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 10件 [`0044b584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b584.md) [`00478c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c90.md) [`00478c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c94.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00477f10",
      "incomplete_value": false,
      "site": "00477f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477ed0",
      "incomplete_value": false,
      "site": "00477ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00477e48",
      "incomplete_value": false,
      "site": "00477e50",
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
            "const:434:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477e08",
      "incomplete_value": false,
      "site": "00477e10",
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
            "const:358:8"
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
      "definition_site": "00477ecc",
      "incomplete_value": true,
      "site": "00477ed4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477e8c",
      "incomplete_value": true,
      "site": "00477e94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
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
      "00477e48",
      "PARAM",
      [
        "storage",
        "002a6358",
        null,
        "string"
      ]
    ],
    [
      "00477ecc",
      "READ",
      [
        "storage",
        "00c9a808",
        null,
        "pointer"
      ]
    ],
    [
      "00477ecc",
      "PARAM",
      [
        "storage",
        "00ca58e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00477e48",
      "PARAM",
      [
        "storage",
        "002a6434",
        null,
        "string"
      ]
    ],
    [
      "00477ecc",
      "READ",
      [
        "storage",
        "00c9ac08",
        null,
        "pointer"
      ]
    ],
    [
      "00477ecc",
      "PARAM",
      [
        "storage",
        "00ca5ce8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md#insn-00477e10) · [`00477e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md#insn-00477e94) · [`00477e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md#insn-00477e00)
- 新版 [`00477e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/00477e0c.md#insn-00477e50) · [`00477ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/00477e0c.md#insn-00477ed4) · [`00477e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/00477e0c.md#insn-00477e40)

~~~diff
- 00477e10 ["INT_ADD", "register:40f0:8", ["const:477e10:8", "const:4:8"]]
- 00477e10 ["CALL", null, ["callee:00c57f70:8"]]
+ 00477e50 ["INT_ADD", "register:40f0:8", ["const:477e50:8", "const:4:8"]]
+ 00477e50 ["CALL", null, ["callee:00c57f70:8"]]
- 00477e10 bytes 587f1f94
+ 00477e50 bytes 48801f94
- 00477e94 ["INT_ADD", "register:40f0:8", ["const:477e94:8", "const:4:8"]]
- 00477e94 ["CALL", null, ["callee:00561d34:8"]]
+ 00477ed4 ["INT_ADD", "register:40f0:8", ["const:477ed4:8", "const:4:8"]]
+ 00477ed4 ["CALL", null, ["callee:00561d34:8"]]
- 00477e94 bytes 98a70394
+ 00477ed4 bytes 98a70394
- 00477e00 ["INT_ADD", "register:40f0:8", ["const:477e00:8", "const:4:8"]]
- 00477e00 ["CALL", null, ["callee:0044b584:8"]]
+ 00477e40 ["INT_ADD", "register:40f0:8", ["const:477e40:8", "const:4:8"]]
+ 00477e40 ["CALL", null, ["callee:0044b584:8"]]
- 00477e00 bytes d14dff97
+ 00477e40 bytes d14dff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53107b1decf350f2f0952361ad10f3f1"></a>

### [`004782d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md) → [`00478314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md) FUN_00478314

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) [`0048ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce78.md) · 呼出先 13件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)
- 新版 呼出元 2件 [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) [`0048ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md) · 呼出先 13件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.32% / 新版 88.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00478384",
      "incomplete_value": true,
      "site": "00478388",
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
      "definition_site": "00478344",
      "incomplete_value": true,
      "site": "00478348",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00478380",
      "incomplete_value": true,
      "site": "00478390",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478340",
      "incomplete_value": true,
      "site": "00478350",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00478398",
      "incomplete_value": true,
      "site": "00478398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
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
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478358",
      "incomplete_value": true,
      "site": "00478358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
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
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00478368",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "0047836c",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00478380",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00478368",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "0047836c",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00478380",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00478370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md#insn-00478370) · [`00478390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md#insn-00478390) · [`004783e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md#insn-004783e8)
- 新版 [`004783b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md#insn-004783b0) · [`004783d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md#insn-004783d0) · [`00478428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md#insn-00478428)

~~~diff
- 00478370 ["INT_ADD", "register:40f0:8", ["const:478370:8", "const:4:8"]]
- 00478370 ["CALL", null, ["callee:00c581e0:8"]]
+ 004783b0 ["INT_ADD", "register:40f0:8", ["const:4783b0:8", "const:4:8"]]
+ 004783b0 ["CALL", null, ["callee:00c581e0:8"]]
- 00478370 bytes 9c7e1f94
+ 004783b0 bytes 8c7f1f94
- 00478390 ["INT_ADD", "register:40f0:8", ["const:478390:8", "const:4:8"]]
- 00478390 ["CALL", null, ["callee:00c581f0:8"]]
+ 004783d0 ["INT_ADD", "register:40f0:8", ["const:4783d0:8", "const:4:8"]]
+ 004783d0 ["CALL", null, ["callee:00c581f0:8"]]
- 00478390 bytes 987e1f94
+ 004783d0 bytes 887f1f94
- 004783e8 ["INT_ADD", "register:40f0:8", ["const:4783e8:8", "const:4:8"]]
- 004783e8 ["CALL", null, ["callee:00c58280:8"]]
+ 00478428 ["INT_ADD", "register:40f0:8", ["const:478428:8", "const:4:8"]]
+ 00478428 ["CALL", null, ["callee:00c58280:8"]]
- 004783e8 bytes a67e1f94
+ 00478428 bytes 967f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e111c95e308c3c30578011dbcb834bd"></a>

### [`00478650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478650.md) → [`00478690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478690.md) FUN_00478690

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) [`0048ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce78.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00478b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b50.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 2件 [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) [`0048ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00478b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478b90.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, store_destination, store_value

命令の説明率　旧版 85.62% / 新版 85.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 7件, `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_condition` 7件, `store_destination` 10件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004786dc",
      "incomplete_value": true,
      "site": "004786dc",
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
      "definition_site": "0047869c",
      "incomplete_value": true,
      "site": "0047869c",
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
            "const:9f0:8"
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
      "definition_site": "00478780",
      "incomplete_value": true,
      "site": "00478780",
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
      "definition_site": "00478740",
      "incomplete_value": true,
      "site": "00478740",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00478824",
      "incomplete_value": true,
      "site": "00478824",
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
      "definition_site": "004787e4",
      "incomplete_value": true,
      "site": "004787e4",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004786ac",
      "READ",
      [
        "storage",
        "00ca4a08",
        null,
        "undefined1"
      ]
    ],
    [
      "004786b8",
      "READ",
      [
        "storage",
        "00ca4a00",
        null,
        "undefined8"
      ]
    ],
    [
      "004786d0",
      "READ",
      [
        "storage",
        "00ca49f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004786ac",
      "READ",
      [
        "storage",
        "00ca4e08",
        null,
        "undefined1"
      ]
    ],
    [
      "004786b8",
      "READ",
      [
        "storage",
        "00ca4e00",
        null,
        "undefined8"
      ]
    ],
    [
      "004786d0",
      "READ",
      [
        "storage",
        "00ca4df8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047869c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478650.md#insn-0047869c) · [`00478740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478650.md#insn-00478740) · [`004787e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478650.md#insn-004787e4)
- 新版 [`004786dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478690.md#insn-004786dc) · [`00478780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478690.md#insn-00478780) · [`00478824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478690.md#insn-00478824)

~~~diff
- 0047869c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 0047869c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 004786dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 004786dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0047869c bytes 68fa04f9
+ 004786dc bytes 68fa06f9
- 00478740 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00478740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00478780 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00478780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00478740 bytes 68fa04f9
+ 00478780 bytes 68fa06f9
- 004787e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 004787e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00478824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00478824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 004787e4 bytes 68fa04f9
+ 00478824 bytes 68fa06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9b5e4095b4e2f5e8f1d40ce80780d67"></a>

### [`00478b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b58.md) → [`00478b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478b98.md) FUN_00478b98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 67.74% / 新版 67.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00478bbc",
      "incomplete_value": true,
      "site": "00478bc4",
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
      "definition_site": "00478b7c",
      "incomplete_value": true,
      "site": "00478b84",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00478bd0",
      "incomplete_value": true,
      "site": "00478bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478b90",
      "incomplete_value": true,
      "site": "00478b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00478bd0",
      "incomplete_value": true,
      "site": "00478bd0",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478b90",
      "incomplete_value": true,
      "site": "00478b90",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
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
      "00478bb4",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00478bbc",
      "READ",
      [
        "storage",
        "00c92e00",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00478bc0",
      "READ",
      [
        "storage",
        "00c92e18",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "00478bb4",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00478bbc",
      "READ",
      [
        "storage",
        "00c93200",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00478bc0",
      "READ",
      [
        "storage",
        "00c93218",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00478b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b58.md#insn-00478b74) · [`00478b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b58.md#insn-00478b78) · [`00478b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b58.md#insn-00478b8c)
- 新版 [`00478bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478b98.md#insn-00478bb4) · [`00478bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478b98.md#insn-00478bcc)

~~~diff
- 00478b74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7b8:8"]]
- 00478b74 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00478bb4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:bb8:8"]]
+ 00478bb4 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00478b74 bytes b5de43f9
+ 00478bb4 bytes b5de45f9
- 00478b78 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00478b78 bytes f30300aa
- 00478b8c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
- 00478b8c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00478bcc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
+ 00478bcc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00478b8c bytes 29e143f9
+ 00478bcc bytes 29e145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd97ea31bb0d405bbfcb975bf58dac6e"></a>

### [`00478c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c1c.md) → [`00478c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c5c.md) FUN_00478c5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00478c70",
      "incomplete_value": false,
      "site": "00478c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478c30",
      "incomplete_value": false,
      "site": "00478c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "00478c74",
      "DATA",
      [
        "storage",
        "00c64ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00478c74",
      "DATA",
      [
        "storage",
        "00c64ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00478c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c1c.md#insn-00478c28) · [`00478c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c1c.md#insn-00478c30)
- 新版 [`00478c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c5c.md#insn-00478c68) · [`00478c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c5c.md#insn-00478c70)

~~~diff
- 00478c28 ["INT_ADD", "register:40f0:8", ["const:478c28:8", "const:4:8"]]
- 00478c28 ["CALL", null, ["callee:00c57e90:8"]]
+ 00478c68 ["INT_ADD", "register:40f0:8", ["const:478c68:8", "const:4:8"]]
+ 00478c68 ["CALL", null, ["callee:00c57e90:8"]]
- 00478c28 bytes 9a7b1f94
+ 00478c68 bytes 8a7c1f94
- 00478c30 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00478c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00478c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00478c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00478c70 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00478c70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00478c70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00478c70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00478c30 bytes 08812b91
+ 00478c70 bytes 08813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cd8cecfe3b97db6b83ee286220bb878"></a>

### [`00478c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c40.md) → [`00478c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c80.md) FUN_00478c80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00478c84",
      "incomplete_value": false,
      "site": "00478c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478c44",
      "incomplete_value": false,
      "site": "00478c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "00478c88",
      "DATA",
      [
        "storage",
        "00c64ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00478c88",
      "DATA",
      [
        "storage",
        "00c64ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00478c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c40.md#insn-00478c44)
- 新版 [`00478c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c80.md#insn-00478c84)

~~~diff
- 00478c44 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00478c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00478c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00478c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00478c84 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00478c84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00478c84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00478c84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00478c44 bytes 08812b91
+ 00478c84 bytes 08813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4791b57f2c7d71f4b0eaabc047b30c86"></a>

### [`004796d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004796d4.md) → [`00479714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479714.md) FUN_00479714

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00479738",
      "incomplete_value": false,
      "site": "00479738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004796f8",
      "incomplete_value": false,
      "site": "004796f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "00479738",
      "DATA",
      [
        "storage",
        "00c64b60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479738",
      "DATA",
      [
        "storage",
        "00c64f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004796e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004796d4.md#insn-004796e8) · [`004796f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004796d4.md#insn-004796f4)
- 新版 [`00479728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479714.md#insn-00479728) · [`00479734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479714.md#insn-00479734)

~~~diff
- 004796e8 ["INT_ADD", "register:40f0:8", ["const:4796e8:8", "const:4:8"]]
- 004796e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00479728 ["INT_ADD", "register:40f0:8", ["const:479728:8", "const:4:8"]]
+ 00479728 ["CALL", null, ["callee:00c57e90:8"]]
- 004796e8 bytes ea781f94
+ 00479728 bytes da791f94
- 004796f4 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 004796f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004796f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004796f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479734 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00479734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004796f4 bytes 08812d91
+ 00479734 bytes 08813d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49f67adb6edf3b5f783ab8930c62a2cf"></a>

### [`00479708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479708.md) → [`00479748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479748.md) FUN_00479748

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00479754",
      "incomplete_value": false,
      "site": "00479754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479714",
      "incomplete_value": false,
      "site": "00479714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "00479754",
      "DATA",
      [
        "storage",
        "00c64b60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479754",
      "DATA",
      [
        "storage",
        "00c64f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479708.md#insn-00479710)
- 新版 [`00479750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479748.md#insn-00479750)

~~~diff
- 00479710 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 00479710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479750 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00479750 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479750 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479750 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479710 bytes 29812d91
+ 00479750 bytes 29813d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69beca0873b67c2fc8ae0fb5b6291ecf"></a>

### [`0047978c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047978c.md) → [`004797cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004797cc.md) FUN_004797cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004797f0",
      "incomplete_value": false,
      "site": "004797f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004797b0",
      "incomplete_value": false,
      "site": "004797b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "004797f0",
      "DATA",
      [
        "storage",
        "00c64bf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004797f0",
      "DATA",
      [
        "storage",
        "00c64ff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004797a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047978c.md#insn-004797a0) · [`004797ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047978c.md#insn-004797ac)
- 新版 [`004797e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004797cc.md#insn-004797e0) · [`004797ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004797cc.md#insn-004797ec)

~~~diff
- 004797a0 ["INT_ADD", "register:40f0:8", ["const:4797a0:8", "const:4:8"]]
- 004797a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 004797e0 ["INT_ADD", "register:40f0:8", ["const:4797e0:8", "const:4:8"]]
+ 004797e0 ["CALL", null, ["callee:00c57e90:8"]]
- 004797a0 bytes bc781f94
+ 004797e0 bytes ac791f94
- 004797ac ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 004797ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004797ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004797ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004797ec ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 004797ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004797ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004797ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004797ac bytes 08c12f91
+ 004797ec bytes 08c13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed13f966531edef67f2eabbbc4c988e6"></a>

### [`004797c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004797c0.md) → [`00479800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479800.md) FUN_00479800

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047980c",
      "incomplete_value": false,
      "site": "0047980c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004797cc",
      "incomplete_value": false,
      "site": "004797cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "0047980c",
      "DATA",
      [
        "storage",
        "00c64bf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047980c",
      "DATA",
      [
        "storage",
        "00c64ff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004797c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004797c0.md#insn-004797c8)
- 新版 [`00479808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479800.md#insn-00479808)

~~~diff
- 004797c8 ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 004797c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004797c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004797c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479808 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00479808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004797c8 bytes 29c12f91
+ 00479808 bytes 29c13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8f5bcabcbf8f6359cc6ab1d34416a51"></a>

### [`0047983c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047983c.md) → [`0047987c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047987c.md) FUN_0047987c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479894",
      "incomplete_value": false,
      "site": "00479898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479854",
      "incomplete_value": false,
      "site": "00479858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      "00479898",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479898",
      "DATA",
      [
        "storage",
        "00c65070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047983c.md#insn-00479898) · [`00479850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047983c.md#insn-00479850) · [`00479854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047983c.md#insn-00479854)
- 新版 [`004798d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047987c.md#insn-004798d8) · [`00479890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047987c.md#insn-00479890) · [`00479894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047987c.md#insn-00479894)

~~~diff
- 00479898 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479898 ["INT_ADD", "register:40f0:8", ["const:479898:8", "const:4:8"]]
- 00479898 ["CALLIND", null, ["register:0:8"]]
+ 004798d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004798d8 ["INT_ADD", "register:40f0:8", ["const:4798d8:8", "const:4:8"]]
+ 004798d8 ["CALLIND", null, ["register:0:8"]]
- 00479898 bytes 00013fd6
+ 004798d8 bytes 00013fd6
- 00479850 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00479890 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 00479850 bytes 493f00f0
+ 00479890 bytes 693f0090
- 00479854 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 00479854 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479854 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479854 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479894 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00479894 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479894 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479894 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479854 bytes 29c13191
+ 00479894 bytes 29c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9dadd250a2e394b77fe107bb25c1c22"></a>

### [`004798ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004798ac.md) → [`004798ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004798ec.md) FUN_004798ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479904",
      "incomplete_value": false,
      "site": "00479908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004798c4",
      "incomplete_value": false,
      "site": "004798c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      "00479908",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479908",
      "DATA",
      [
        "storage",
        "00c65070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004798c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004798ac.md#insn-004798c0) · [`004798c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004798ac.md#insn-004798c4) · [`004798d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004798ac.md#insn-004798d4)
- 新版 [`00479900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004798ec.md#insn-00479900) · [`00479904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004798ec.md#insn-00479904) · [`00479914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004798ec.md#insn-00479914)

~~~diff
- 004798c0 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00479900 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 004798c0 bytes 493f00f0
+ 00479900 bytes 693f0090
- 004798c4 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 004798c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004798c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004798c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479904 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00479904 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479904 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479904 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004798c4 bytes 29c13191
+ 00479904 bytes 29c10191
- 004798d4 ["INT_ADD", "register:40f0:8", ["const:4798d4:8", "const:4:8"]]
- 004798d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00479914 ["INT_ADD", "register:40f0:8", ["const:479914:8", "const:4:8"]]
+ 00479914 ["CALL", null, ["callee:00c57eb0:8"]]
- 004798d4 bytes 77781f94
+ 00479914 bytes 67791f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c95dbb5a263b45d9e2c7d5dbbdbcbfb"></a>

### [`00479918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479918.md) → [`00479958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479958.md) FUN_00479958

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00479980",
      "incomplete_value": false,
      "site": "00479984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479940",
      "incomplete_value": false,
      "site": "00479944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      "00479984",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479984",
      "DATA",
      [
        "storage",
        "00c65070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047992c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479918.md#insn-0047992c) · [`0047993c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479918.md#insn-0047993c) · [`00479940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479918.md#insn-00479940)
- 新版 [`0047996c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479958.md#insn-0047996c) · [`0047997c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479958.md#insn-0047997c) · [`00479980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479958.md#insn-00479980)

~~~diff
- 0047992c ["INT_ADD", "register:40f0:8", ["const:47992c:8", "const:4:8"]]
- 0047992c ["CALL", null, ["callee:00c57e90:8"]]
+ 0047996c ["INT_ADD", "register:40f0:8", ["const:47996c:8", "const:4:8"]]
+ 0047996c ["CALL", null, ["callee:00c57e90:8"]]
- 0047992c bytes 59781f94
+ 0047996c bytes 49791f94
- 0047993c ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 0047997c ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0047993c bytes 493f00f0
+ 0047997c bytes 693f0090
- 00479940 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 00479940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479980 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00479980 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479980 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479980 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479940 bytes 29c13191
+ 00479980 bytes 29c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c615dd3fa43cc26b9451043d855eceb7"></a>

### [`004799b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004799b8.md) → [`004799f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004799f8.md) FUN_004799f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479a14",
      "incomplete_value": false,
      "site": "00479a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004799d4",
      "incomplete_value": false,
      "site": "004799e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      "00479a20",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479a20",
      "DATA",
      [
        "storage",
        "00c65070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004799b8.md#insn-00479a20) · [`004799d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004799b8.md#insn-004799d0) · [`004799d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004799b8.md#insn-004799d4)
- 新版 [`00479a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004799f8.md#insn-00479a60) · [`00479a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004799f8.md#insn-00479a10) · [`00479a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004799f8.md#insn-00479a14)

~~~diff
- 00479a20 ["INT_ADD", "register:40f0:8", ["const:479a20:8", "const:4:8"]]
- 00479a20 ["CALL", null, ["callee:0043bb20:8"]]
+ 00479a60 ["INT_ADD", "register:40f0:8", ["const:479a60:8", "const:4:8"]]
+ 00479a60 ["CALL", null, ["callee:0043bb20:8"]]
- 00479a20 bytes 3008ff97
+ 00479a60 bytes 3008ff97
- 004799d0 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00479a10 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 004799d0 bytes 493f00f0
+ 00479a10 bytes 693f0090
- 004799d4 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 004799d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004799d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004799d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479a14 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00479a14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479a14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479a14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004799d4 bytes 29c13191
+ 00479a14 bytes 29c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b4161bde30abc18bfa01310f8a5b877"></a>

### [`00479b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479b08.md) → [`00479b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479b48.md) FUN_00479b48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00479d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d68.md) [`00550950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550950.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00479da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479da8.md) [`00550990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550990.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.26% / 新版 93.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479be0",
      "incomplete_value": false,
      "site": "00479be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479ba0",
      "incomplete_value": false,
      "site": "00479ba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479bf8",
      "incomplete_value": false,
      "site": "00479bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479bb8",
      "incomplete_value": false,
      "site": "00479bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00479bb4",
      "value": [
        "leaf",
        "ram:550990:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00479b74",
      "value": [
        "leaf",
        "ram:550950:8"
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
      "00479bb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00550950"
      ]
    ],
    [
      "00479be8",
      "DATA",
      [
        "storage",
        "00c64ce0",
        null,
        "pointer"
      ]
    ],
    [
      "00479bf8",
      "DATA",
      [
        "storage",
        "00c64d30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479bb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00550990"
      ]
    ],
    [
      "00479be8",
      "DATA",
      [
        "storage",
        "00c650e0",
        null,
        "pointer"
      ]
    ],
    [
      "00479bf8",
      "DATA",
      [
        "storage",
        "00c65130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479b08.md#insn-00479b74) · [`00479b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479b08.md#insn-00479b48) · [`00479b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479b08.md#insn-00479b64)
- 新版 [`00479bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479b48.md#insn-00479bb4) · [`00479b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479b48.md#insn-00479b88) · [`00479ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479b48.md#insn-00479ba4)

~~~diff
- 00479b74 ["INT_ADD", "register:40f0:8", ["const:479b74:8", "const:4:8"]]
- 00479b74 ["CALL", null, ["ram:550950:8"]]
+ 00479bb4 ["INT_ADD", "register:40f0:8", ["const:479bb4:8", "const:4:8"]]
+ 00479bb4 ["CALL", null, ["ram:550990:8"]]
- 00479b74 bytes 775b0394
+ 00479bb4 bytes 775b0394
- 00479b48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479b48 ["INT_ADD", "register:40f0:8", ["const:479b48:8", "const:4:8"]]
- 00479b48 ["CALLIND", null, ["register:0:8"]]
+ 00479b88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479b88 ["INT_ADD", "register:40f0:8", ["const:479b88:8", "const:4:8"]]
+ 00479b88 ["CALLIND", null, ["register:0:8"]]
- 00479b48 bytes 00013fd6
+ 00479b88 bytes 00013fd6
- 00479b64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00479b64 ["INT_ADD", "register:40f0:8", ["const:479b64:8", "const:4:8"]]
- 00479b64 ["CALLIND", null, ["register:0:8"]]
+ 00479ba4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00479ba4 ["INT_ADD", "register:40f0:8", ["const:479ba4:8", "const:4:8"]]
+ 00479ba4 ["CALLIND", null, ["register:0:8"]]
- 00479b64 bytes 20013fd6
+ 00479ba4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67200370b8e6030218e99da58419d3ac"></a>

### [`00479d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d28.md) → [`00479d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d68.md) FUN_00479d68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "00479d6c",
      "incomplete_value": false,
      "site": "00479d70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479d2c",
      "incomplete_value": false,
      "site": "00479d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "00479d70",
      "DATA",
      [
        "storage",
        "00c64ce0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00479d70",
      "DATA",
      [
        "storage",
        "00c650e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d28.md#insn-00479d28) · [`00479d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d28.md#insn-00479d2c)
- 新版 [`00479d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d68.md#insn-00479d68) · [`00479d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d68.md#insn-00479d6c)

~~~diff
- 00479d28 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00479d68 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00479d28 bytes 483f00f0
+ 00479d68 bytes 683f0090
- 00479d2c ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00479d2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479d2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479d2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479d6c ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00479d6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479d6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479d6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479d2c bytes 08813391
+ 00479d6c bytes 08810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2576bcb64fc3c48d802505df66223dea"></a>

### [`00479d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d38.md) → [`00479d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d78.md) FUN_00479d78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479d88",
      "incomplete_value": false,
      "site": "00479d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479d48",
      "incomplete_value": false,
      "site": "00479d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "00479d90",
      "DATA",
      [
        "storage",
        "00c64ce0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00479d90",
      "DATA",
      [
        "storage",
        "00c650e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d38.md#insn-00479d44) · [`00479d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d38.md#insn-00479d48) · [`00479d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d38.md#insn-00479d54)
- 新版 [`00479d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d78.md#insn-00479d84) · [`00479d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d78.md#insn-00479d88) · [`00479d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d78.md#insn-00479d94)

~~~diff
- 00479d44 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00479d84 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00479d44 bytes 483f00f0
+ 00479d84 bytes 683f0090
- 00479d48 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00479d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479d88 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00479d88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479d88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479d88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479d48 bytes 08813391
+ 00479d88 bytes 08810391
- 00479d54 ["INT_ADD", "register:40f0:8", ["const:479d54:8", "const:4:8"]]
- 00479d54 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00479d94 ["INT_ADD", "register:40f0:8", ["const:479d94:8", "const:4:8"]]
+ 00479d94 ["CALL", null, ["callee:00c57ea0:8"]]
- 00479d54 bytes 53771f94
+ 00479d94 bytes 43781f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce6c9cdf2a80ac61e7d5674021d2b263"></a>

### [`00479dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479dc0.md) → [`00479e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e00.md) FUN_00479e00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00479e14",
      "incomplete_value": false,
      "site": "00479e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479dd4",
      "incomplete_value": false,
      "site": "00479dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
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
      "00479e18",
      "DATA",
      [
        "storage",
        "00c64dc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479e18",
      "DATA",
      [
        "storage",
        "00c651c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479dc0.md#insn-00479dd0) · [`00479dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479dc0.md#insn-00479dd4) · [`00479de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479dc0.md#insn-00479de8)
- 新版 [`00479e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e00.md#insn-00479e10) · [`00479e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e00.md#insn-00479e14) · [`00479e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e00.md#insn-00479e28)

~~~diff
- 00479dd0 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00479e10 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00479dd0 bytes 483f00f0
+ 00479e10 bytes 683f0090
- 00479dd4 ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 00479dd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479dd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479dd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479e14 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00479e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479dd4 bytes 08213791
+ 00479e14 bytes 08210791
- 00479de8 ["INT_ADD", "register:40f0:8", ["const:479de8:8", "const:4:8"]]
- 00479de8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00479e28 ["INT_ADD", "register:40f0:8", ["const:479e28:8", "const:4:8"]]
+ 00479e28 ["CALL", null, ["callee:00c53d00:8"]]
- 00479de8 bytes be661f94
+ 00479e28 bytes b6671f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81331ca23b5e2d2724864a9d46711010"></a>

### [`00479e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e1c.md) → [`00479e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e5c.md) FUN_00479e5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00479e74",
      "incomplete_value": false,
      "site": "00479e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479e34",
      "incomplete_value": false,
      "site": "00479e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
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
      "00479e78",
      "DATA",
      [
        "storage",
        "00c64dc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479e78",
      "DATA",
      [
        "storage",
        "00c651c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e1c.md#insn-00479e30) · [`00479e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e1c.md#insn-00479e34) · [`00479e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e1c.md#insn-00479e48)
- 新版 [`00479e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e5c.md#insn-00479e70) · [`00479e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e5c.md#insn-00479e74) · [`00479e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e5c.md#insn-00479e88)

~~~diff
- 00479e30 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00479e70 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00479e30 bytes 483f00f0
+ 00479e70 bytes 683f0090
- 00479e34 ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 00479e34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479e34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479e34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479e74 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00479e74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479e74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479e74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479e34 bytes 08213791
+ 00479e74 bytes 08210791
- 00479e48 ["INT_ADD", "register:40f0:8", ["const:479e48:8", "const:4:8"]]
- 00479e48 ["CALL", null, ["callee:00c53d00:8"]]
+ 00479e88 ["INT_ADD", "register:40f0:8", ["const:479e88:8", "const:4:8"]]
+ 00479e88 ["CALL", null, ["callee:00c53d00:8"]]
- 00479e48 bytes a6661f94
+ 00479e88 bytes 9e671f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c03c97ce7033747127887271288491f6"></a>

### [`00479e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e78.md) → [`00479eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479eb8.md) FUN_00479eb8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479edc",
      "incomplete_value": false,
      "site": "00479ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479e9c",
      "incomplete_value": false,
      "site": "00479ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
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
      "00479ee0",
      "DATA",
      [
        "storage",
        "00c64dc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479ee0",
      "DATA",
      [
        "storage",
        "00c651c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e78.md#insn-00479e8c) · [`00479e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e78.md#insn-00479e98) · [`00479e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e78.md#insn-00479e9c)
- 新版 [`00479ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479eb8.md#insn-00479ecc) · [`00479ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479eb8.md#insn-00479ed8) · [`00479edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479eb8.md#insn-00479edc)

~~~diff
- 00479e8c ["INT_ADD", "register:40f0:8", ["const:479e8c:8", "const:4:8"]]
- 00479e8c ["CALL", null, ["callee:00c57e90:8"]]
+ 00479ecc ["INT_ADD", "register:40f0:8", ["const:479ecc:8", "const:4:8"]]
+ 00479ecc ["CALL", null, ["callee:00c57e90:8"]]
- 00479e8c bytes 01771f94
+ 00479ecc bytes f1771f94
- 00479e98 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00479ed8 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 00479e98 bytes 493f00f0
+ 00479ed8 bytes 693f0090
- 00479e9c ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 00479e9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479e9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479e9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479edc ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00479edc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479edc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479edc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479e9c bytes 29213791
+ 00479edc bytes 29210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57c03513d5769e2f1899334f6a302528"></a>

### [`00479ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479ed0.md) → [`00479f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f10.md) FUN_00479f10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479f18",
      "incomplete_value": false,
      "site": "00479f1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479ed8",
      "incomplete_value": false,
      "site": "00479edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
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
      "00479f1c",
      "DATA",
      [
        "storage",
        "00c64dc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479f1c",
      "DATA",
      [
        "storage",
        "00c651c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479ed0.md#insn-00479ed4) · [`00479ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479ed0.md#insn-00479ed8) · [`00479f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479ed0.md#insn-00479f00)
- 新版 [`00479f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f10.md#insn-00479f14) · [`00479f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f10.md#insn-00479f18) · [`00479f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f10.md#insn-00479f40)

~~~diff
- 00479ed4 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00479f14 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 00479ed4 bytes 493f00f0
+ 00479f14 bytes 693f0090
- 00479ed8 ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 00479ed8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479ed8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479ed8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479f18 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00479f18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479f18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479f18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479ed8 bytes 29213791
+ 00479f18 bytes 29210791
- 00479f00 ["INT_ADD", "register:40f0:8", ["const:479f00:8", "const:4:8"]]
- 00479f00 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00479f40 ["INT_ADD", "register:40f0:8", ["const:479f40:8", "const:4:8"]]
+ 00479f40 ["CALL", null, ["callee:00c53cd0:8"]]
- 00479f00 bytes 6c661f94
+ 00479f40 bytes 64671f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ffaa7828e33e7e8f0879d78672c9893"></a>

### [`00479fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479fac.md) → [`00479fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479fec.md) FUN_00479fec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047a138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a138.md) [`0047a13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a13c.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`00493894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493894.md) [`00550954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550954.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a178.md) [`0047a17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a17c.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md) [`00550994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550994.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a048",
      "incomplete_value": false,
      "site": "0047a050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a008",
      "incomplete_value": false,
      "site": "0047a010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047a020",
      "value": [
        "leaf",
        "ram:550994:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00479fe0",
      "value": [
        "leaf",
        "ram:550954:8"
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
      "site": "0047a040",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047a000",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "0047a020",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00550954"
      ]
    ],
    [
      "0047a040",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0047a050",
      "DATA",
      [
        "storage",
        "00c64e48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a020",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00550994"
      ]
    ],
    [
      "0047a040",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0047a050",
      "DATA",
      [
        "storage",
        "00c65248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479fac.md#insn-00479fe0) · [`0047a000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479fac.md#insn-0047a000) · [`0047a020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479fac.md#insn-0047a020)
- 新版 [`0047a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479fec.md#insn-0047a020) · [`0047a040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479fec.md#insn-0047a040) · [`0047a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479fec.md#insn-0047a060)

~~~diff
- 00479fe0 ["INT_ADD", "register:40f0:8", ["const:479fe0:8", "const:4:8"]]
- 00479fe0 ["CALL", null, ["ram:550954:8"]]
+ 0047a020 ["INT_ADD", "register:40f0:8", ["const:47a020:8", "const:4:8"]]
+ 0047a020 ["CALL", null, ["ram:550994:8"]]
- 00479fe0 bytes 5d5a0394
+ 0047a020 bytes 5d5a0394
- 0047a000 ["INT_ADD", "register:40f0:8", ["const:47a000:8", "const:4:8"]]
- 0047a000 ["CALL", null, ["ram:48ccb8:8"]]
+ 0047a040 ["INT_ADD", "register:40f0:8", ["const:47a040:8", "const:4:8"]]
+ 0047a040 ["CALL", null, ["ram:48ccf8:8"]]
- 0047a000 bytes 2e4b0094
+ 0047a040 bytes 2e4b0094
- 0047a020 ["INT_ADD", "register:40f0:8", ["const:47a020:8", "const:4:8"]]
- 0047a020 ["CALL", null, ["callee:004938d4:8"]]
+ 0047a060 ["INT_ADD", "register:40f0:8", ["const:47a060:8", "const:4:8"]]
+ 0047a060 ["CALL", null, ["callee:004938d4:8"]]
- 0047a020 bytes 1d660094
+ 0047a060 bytes 1d660094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-071c54eb42aae5ee335654a070931817"></a>

### [`0047a104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a104.md) → [`0047a144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a144.md) FUN_0047a144

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047a158",
      "incomplete_value": false,
      "site": "0047a15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a118",
      "incomplete_value": false,
      "site": "0047a11c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "0047a15c",
      "DATA",
      [
        "storage",
        "00c64e48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a15c",
      "DATA",
      [
        "storage",
        "00c65248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a104.md#insn-0047a110) · [`0047a114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a104.md#insn-0047a114) · [`0047a118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a104.md#insn-0047a118)
- 新版 [`0047a150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a144.md#insn-0047a150) · [`0047a154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a144.md#insn-0047a154) · [`0047a158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a144.md#insn-0047a158)

~~~diff
- 0047a110 ["INT_ADD", "register:40f0:8", ["const:47a110:8", "const:4:8"]]
- 0047a110 ["CALL", null, ["callee:00c57e90:8"]]
+ 0047a150 ["INT_ADD", "register:40f0:8", ["const:47a150:8", "const:4:8"]]
+ 0047a150 ["CALL", null, ["callee:00c57e90:8"]]
- 0047a110 bytes 60761f94
+ 0047a150 bytes 50771f94
- 0047a114 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0047a154 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0047a114 bytes 483f00d0
+ 0047a154 bytes 483f00f0
- 0047a118 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0047a118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047a118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047a118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a158 ["COPY", "tmp:0:8", ["const:248:8"]]
+ 0047a158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047a118 bytes 08213991
+ 0047a158 bytes 08210991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90b341ae24819302a9360c3aa9bf62f0"></a>

### [`0047a128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a128.md) → [`0047a168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a168.md) FUN_0047a168

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047a16c",
      "incomplete_value": false,
      "site": "0047a170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a12c",
      "incomplete_value": false,
      "site": "0047a130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "0047a170",
      "DATA",
      [
        "storage",
        "00c64e48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a170",
      "DATA",
      [
        "storage",
        "00c65248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a128.md#insn-0047a128) · [`0047a12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a128.md#insn-0047a12c)
- 新版 [`0047a168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a168.md#insn-0047a168) · [`0047a16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a168.md#insn-0047a16c)

~~~diff
- 0047a128 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0047a168 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0047a128 bytes 483f00d0
+ 0047a168 bytes 483f00f0
- 0047a12c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0047a12c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047a12c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047a12c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a16c ["COPY", "tmp:0:8", ["const:248:8"]]
+ 0047a16c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a16c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a16c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047a12c bytes 08213991
+ 0047a16c bytes 08210991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3dc2a61c84dd8403770bbc7a749210e"></a>

### [`0047a140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md) → [`0047a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md) FUN_0047a180

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0047a704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a704.md) [`0047a754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a754.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0047a744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a744.md) [`0047a794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a794.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a1a4",
      "incomplete_value": true,
      "site": "0047a1c0",
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
      "definition_site": "0047a164",
      "incomplete_value": true,
      "site": "0047a180",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a2f4",
      "incomplete_value": false,
      "site": "0047a2f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a2b4",
      "incomplete_value": false,
      "site": "0047a2b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "0047a1a4",
      "READ",
      [
        "storage",
        "002b4b6a",
        null,
        "string"
      ]
    ],
    [
      "0047a2f4",
      "DATA",
      [
        "storage",
        "00c64eb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0047a384",
      "READ",
      [
        "storage",
        "00c64ed8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047a1a4",
      "READ",
      [
        "storage",
        "002b4baa",
        null,
        "string"
      ]
    ],
    [
      "0047a2f4",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0047a384",
      "READ",
      [
        "storage",
        "00c652d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md#insn-0047a15c) · [`0047a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md#insn-0047a190) · [`0047a1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md#insn-0047a1d8)
- 新版 [`0047a19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md#insn-0047a19c) · [`0047a1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md#insn-0047a1d0) · [`0047a218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md#insn-0047a218)

~~~diff
- 0047a15c ["COPY", "tmp:0:8", ["const:b6a:8"]]
- 0047a15c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047a15c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047a15c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047a19c ["COPY", "tmp:0:8", ["const:baa:8"]]
+ 0047a19c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047a19c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047a19c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047a15c bytes 4aa92d91
+ 0047a19c bytes 4aa92e91
- 0047a190 ["INT_ADD", "register:40f0:8", ["const:47a190:8", "const:4:8"]]
- 0047a190 ["CALL", null, ["callee:0048ce54:8"]]
+ 0047a1d0 ["INT_ADD", "register:40f0:8", ["const:47a1d0:8", "const:4:8"]]
+ 0047a1d0 ["CALL", null, ["callee:0048ce54:8"]]
- 0047a190 bytes 214b0094
+ 0047a1d0 bytes 214b0094
- 0047a1d8 ["INT_ADD", "register:40f0:8", ["const:47a1d8:8", "const:4:8"]]
- 0047a1d8 ["CALL", null, ["callee:0043bb20:8"]]
+ 0047a218 ["INT_ADD", "register:40f0:8", ["const:47a218:8", "const:4:8"]]
+ 0047a218 ["CALL", null, ["callee:0043bb20:8"]]
- 0047a1d8 bytes 4206ff97
+ 0047a218 bytes 4206ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4686f754cfbe29e051f060a9c8afe3c1"></a>

### [`0047a5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a5c8.md) → [`0047a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a608.md) FUN_0047a608

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0047a61c",
      "incomplete_value": false,
      "site": "0047a620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a5dc",
      "incomplete_value": false,
      "site": "0047a5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "0047a620",
      "DATA",
      [
        "storage",
        "00c64eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a620",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a5c8.md#insn-0047a5d8) · [`0047a5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a5c8.md#insn-0047a5dc) · [`0047a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a5c8.md#insn-0047a5f0)
- 新版 [`0047a618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a608.md#insn-0047a618) · [`0047a61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a608.md#insn-0047a61c) · [`0047a630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a608.md#insn-0047a630)

~~~diff
- 0047a5d8 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0047a618 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0047a5d8 bytes 483f00d0
+ 0047a618 bytes 483f00f0
- 0047a5dc ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 0047a5dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047a5dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047a5dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a61c ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 0047a61c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a61c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a61c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047a5dc bytes 08e13a91
+ 0047a61c bytes 08e10a91
- 0047a5f0 ["INT_ADD", "register:40f0:8", ["const:47a5f0:8", "const:4:8"]]
- 0047a5f0 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047a630 ["INT_ADD", "register:40f0:8", ["const:47a630:8", "const:4:8"]]
+ 0047a630 ["CALL", null, ["callee:00c53d00:8"]]
- 0047a5f0 bytes bc641f94
+ 0047a630 bytes b4651f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-125cf98244901dd4c02f551c74885b9b"></a>

### [`0047a624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a624.md) → [`0047a664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a664.md) FUN_0047a664

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0047a67c",
      "incomplete_value": false,
      "site": "0047a680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a63c",
      "incomplete_value": false,
      "site": "0047a640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "0047a680",
      "DATA",
      [
        "storage",
        "00c64eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a680",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a624.md#insn-0047a638) · [`0047a63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a624.md#insn-0047a63c) · [`0047a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a624.md#insn-0047a650)
- 新版 [`0047a678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a664.md#insn-0047a678) · [`0047a67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a664.md#insn-0047a67c) · [`0047a690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a664.md#insn-0047a690)

~~~diff
- 0047a638 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0047a678 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0047a638 bytes 483f00d0
+ 0047a678 bytes 483f00f0
- 0047a63c ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 0047a63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047a63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047a63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a67c ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 0047a67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047a63c bytes 08e13a91
+ 0047a67c bytes 08e10a91
- 0047a650 ["INT_ADD", "register:40f0:8", ["const:47a650:8", "const:4:8"]]
- 0047a650 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047a690 ["INT_ADD", "register:40f0:8", ["const:47a690:8", "const:4:8"]]
+ 0047a690 ["CALL", null, ["callee:00c53d00:8"]]
- 0047a650 bytes a4641f94
+ 0047a690 bytes 9c651f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0950a46ea22777cf6451293c2236632"></a>

### [`0047a680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a680.md) → [`0047a6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a6c0.md) FUN_0047a6c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a6e4",
      "incomplete_value": false,
      "site": "0047a6e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a6a4",
      "incomplete_value": false,
      "site": "0047a6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "0047a6e4",
      "DATA",
      [
        "storage",
        "00c64eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a6e4",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a680.md#insn-0047a694) · [`0047a69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a680.md#insn-0047a69c) · [`0047a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a680.md#insn-0047a6a0)
- 新版 [`0047a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a6c0.md#insn-0047a6d4) · [`0047a6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a6c0.md#insn-0047a6dc) · [`0047a6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a6c0.md#insn-0047a6e0)

~~~diff
- 0047a694 ["INT_ADD", "register:40f0:8", ["const:47a694:8", "const:4:8"]]
- 0047a694 ["CALL", null, ["callee:00c57e90:8"]]
+ 0047a6d4 ["INT_ADD", "register:40f0:8", ["const:47a6d4:8", "const:4:8"]]
+ 0047a6d4 ["CALL", null, ["callee:00c57e90:8"]]
- 0047a694 bytes ff741f94
+ 0047a6d4 bytes ef751f94
- 0047a69c ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 0047a6dc ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0047a69c bytes 493f00d0
+ 0047a6dc bytes 493f00f0
- 0047a6a0 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 0047a6a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047a6a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047a6a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047a6e0 ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 0047a6e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a6e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a6e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047a6a0 bytes 29e13a91
+ 0047a6e0 bytes 29e10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88fb392ae6fec2ebbef33392570e0ad5"></a>

### [`0047a6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a6d0.md) → [`0047a710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a710.md) FUN_0047a710

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "0047a71c",
      "incomplete_value": false,
      "site": "0047a71c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a6dc",
      "incomplete_value": false,
      "site": "0047a6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "0047a71c",
      "DATA",
      [
        "storage",
        "00c64eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a71c",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a6d0.md#insn-0047a6d4) · [`0047a6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a6d0.md#insn-0047a6d8) · [`0047a6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a6d0.md#insn-0047a6f8)
- 新版 [`0047a714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a710.md#insn-0047a714) · [`0047a718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a710.md#insn-0047a718) · [`0047a738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a710.md#insn-0047a738)

~~~diff
- 0047a6d4 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 0047a714 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0047a6d4 bytes 493f00d0
+ 0047a714 bytes 493f00f0
- 0047a6d8 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 0047a6d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047a6d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047a6d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047a718 ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 0047a718 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a718 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a718 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047a6d8 bytes 29e13a91
+ 0047a718 bytes 29e10a91
- 0047a6f8 ["INT_ADD", "register:40f0:8", ["const:47a6f8:8", "const:4:8"]]
- 0047a6f8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0047a738 ["INT_ADD", "register:40f0:8", ["const:47a738:8", "const:4:8"]]
+ 0047a738 ["CALL", null, ["callee:00c53cd0:8"]]
- 0047a6f8 bytes 6e641f94
+ 0047a738 bytes 66651f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f3f25a26c14d9efa076bfe64d2e3769"></a>

### [`0047a924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a924.md) → [`0047a964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a964.md) _INIT_16

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a9a0",
      "incomplete_value": true,
      "site": "0047a9bc",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a960",
      "incomplete_value": true,
      "site": "0047a97c",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ee6:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a9c4",
      "incomplete_value": true,
      "site": "0047a9e0",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a984",
      "incomplete_value": true,
      "site": "0047a9a0",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ef9:8"
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
      "definition_site": "0047a9e4",
      "incomplete_value": true,
      "site": "0047aa00",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a9a4",
      "incomplete_value": true,
      "site": "0047a9c0",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047a9a0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0047a9c4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0047a9e4",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047a9a0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0047a9c4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0047a9e4",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a924.md#insn-0047a99c) · [`0047a9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a924.md#insn-0047a9bc) · [`0047aa84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a924.md#insn-0047aa84)
- 新版 [`0047a9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a964.md#insn-0047a9dc) · [`0047a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a964.md#insn-0047a9fc) · [`0047aac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a964.md#insn-0047aac4)

~~~diff
- 0047a99c ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0047a99c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047a99c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047a99c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047a9dc ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0047a9dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047a9dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047a9dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047a99c bytes 4a093691
+ 0047a9dc bytes 4a093791
- 0047a9bc ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0047a9bc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047a9bc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047a9bc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047a9fc ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0047a9fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047a9fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047a9fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047a9bc bytes 4a553a91
+ 0047a9fc bytes 4a893d91
- 0047aa84 ["INT_ADD", "register:40f0:8", ["const:47aa84:8", "const:4:8"]]
- 0047aa84 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0047aac4 ["INT_ADD", "register:40f0:8", ["const:47aac4:8", "const:4:8"]]
+ 0047aac4 ["CALL", null, ["callee:0043b7f8:8"]]
- 0047aa84 bytes 4d03ff97
+ 0047aac4 bytes 4d03ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa22725bd20640004551167e219b2afe"></a>

### [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) → [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) FUN_0047af10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 23件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004706d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706d4.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0047b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md) [`0047d23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d23c.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 23件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md) [`0047d27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047af58",
      "incomplete_value": false,
      "site": "0047af68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047af18",
      "incomplete_value": false,
      "site": "0047af28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:938:8"
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
      "definition_site": "0047b3b8",
      "incomplete_value": true,
      "site": "0047b3bc",
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
      "definition_site": "0047b378",
      "incomplete_value": true,
      "site": "0047b37c",
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
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047b3b4",
      "incomplete_value": true,
      "site": "0047b3c0",
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
      "definition_site": "0047b374",
      "incomplete_value": true,
      "site": "0047b380",
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
    "ordinal": 47,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047af68",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0047b3a8",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "0047b3ac",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047af68",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0047b3a8",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "0047b3ac",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047b3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md#insn-0047b3c0) · [`0047af0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md#insn-0047af0c) · [`0047af18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md#insn-0047af18)
- 新版 [`0047b400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md#insn-0047b400) · [`0047af4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md#insn-0047af4c) · [`0047af58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md#insn-0047af58)

~~~diff
- 0047b3c0 ["INT_ADD", "register:40f0:8", ["const:47b3c0:8", "const:4:8"]]
- 0047b3c0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0047b400 ["INT_ADD", "register:40f0:8", ["const:47b400:8", "const:4:8"]]
+ 0047b400 ["CALL", null, ["callee:00c57fb0:8"]]
- 0047b3c0 bytes fc711f94
+ 0047b400 bytes ec721f94
- 0047af0c ["INT_ADD", "register:40f0:8", ["const:47af0c:8", "const:4:8"]]
- 0047af0c ["CALL", null, ["callee:00487e20:8"]]
+ 0047af4c ["INT_ADD", "register:40f0:8", ["const:47af4c:8", "const:4:8"]]
+ 0047af4c ["CALL", null, ["callee:00487e20:8"]]
- 0047af0c bytes b5330094
+ 0047af4c bytes b5330094
- 0047af18 ["COPY", "tmp:0:8", ["const:938:8"]]
- 0047af18 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047af18 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047af18 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047af58 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 0047af58 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047af58 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047af58 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047af18 bytes 4ae12491
+ 0047af58 bytes 4ae13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ae5b09dcf027f4069ee3f4e48f79c87"></a>

### [`0047b80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md) → [`0047b84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b84c.md) FUN_0047b84c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0047fa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fa0c.md) [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 13件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00550be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be0.md) [`00550be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be4.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md)
- 新版 呼出元 3件 [`0047fa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fa4c.md) [`005ba798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba798.md) [`00876f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md) · 呼出先 13件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00550c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c20.md) [`00550c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c24.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047b8a4",
      "incomplete_value": true,
      "site": "0047b8a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047b864",
      "incomplete_value": true,
      "site": "0047b864",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:fe0:8"
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
      "definition_site": "0047b9c8",
      "incomplete_value": true,
      "site": "0047b9c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:84e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047b988",
      "incomplete_value": true,
      "site": "0047b988",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:80e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047bb58",
      "incomplete_value": false,
      "site": "0047bb5c",
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
      "definition_site": "0047bb18",
      "incomplete_value": false,
      "site": "0047bb1c",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047b890",
      "READ",
      [
        "storage",
        "002b7fe0",
        null,
        "string"
      ]
    ],
    [
      "0047b9b4",
      "READ",
      [
        "storage",
        "002af80e",
        null,
        "string"
      ]
    ],
    [
      "0047bb58",
      "PARAM",
      [
        "storage",
        "00ca44d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047b890",
      "READ",
      [
        "storage",
        "002b8020",
        null,
        "string"
      ]
    ],
    [
      "0047b9b4",
      "READ",
      [
        "storage",
        "002af84e",
        null,
        "string"
      ]
    ],
    [
      "0047bb58",
      "PARAM",
      [
        "storage",
        "00ca48d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047badc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md#insn-0047badc) · [`0047bb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md#insn-0047bb1c) · [`0047bba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md#insn-0047bba8)
- 新版 [`0047bb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b84c.md#insn-0047bb1c) · [`0047bb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b84c.md#insn-0047bb5c) · [`0047bbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b84c.md#insn-0047bbe8)

~~~diff
- 0047badc ["INT_ADD", "register:40f0:8", ["const:47badc:8", "const:4:8"]]
- 0047badc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047bb1c ["INT_ADD", "register:40f0:8", ["const:47bb1c:8", "const:4:8"]]
+ 0047bb1c ["CALL", null, ["callee:00c57eb0:8"]]
- 0047badc bytes f56f1f94
+ 0047bb1c bytes e5701f94
- 0047bb1c ["INT_ADD", "register:40f0:8", ["const:47bb1c:8", "const:4:8"]]
- 0047bb1c ["CALL", null, ["callee:00c580e0:8"]]
+ 0047bb5c ["INT_ADD", "register:40f0:8", ["const:47bb5c:8", "const:4:8"]]
+ 0047bb5c ["CALL", null, ["callee:00c580e0:8"]]
- 0047bb1c bytes 71701f94
+ 0047bb5c bytes 61711f94
- 0047bba8 ["INT_ADD", "register:40f0:8", ["const:47bba8:8", "const:4:8"]]
- 0047bba8 ["CALL", null, ["callee:00c580f0:8"]]
+ 0047bbe8 ["INT_ADD", "register:40f0:8", ["const:47bbe8:8", "const:4:8"]]
+ 0047bbe8 ["CALL", null, ["callee:00c580f0:8"]]
- 0047bba8 bytes 52701f94
+ 0047bbe8 bytes 42711f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0c50668772c9db9740257bb93bdf716"></a>

### [`0047bcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bcc0.md) → [`0047bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bd00.md) FUN_0047bd00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00854630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/00854630.md) · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)
- 新版 呼出元 1件 [`00854670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/00854670.md) · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)

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
      "definition_site": "0047bd18",
      "incomplete_value": false,
      "site": "0047bd20",
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
      "definition_site": "0047bcd8",
      "incomplete_value": false,
      "site": "0047bce0",
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
            "const:4d8:8"
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
      "0047bd18",
      "PARAM",
      [
        "storage",
        "00ca44d8",
        null,
        null
      ]
    ],
    [
      "0047bdcc",
      "PARAM",
      [
        "storage",
        "00ca44d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047bd18",
      "PARAM",
      [
        "storage",
        "00ca48d8",
        null,
        null
      ]
    ],
    [
      "0047bdcc",
      "PARAM",
      [
        "storage",
        "00ca48d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047bce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bcc0.md#insn-0047bce0) · [`0047bcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bcc0.md#insn-0047bcd8) · [`0047bd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bcc0.md#insn-0047bd24)
- 新版 [`0047bd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bd00.md#insn-0047bd20) · [`0047bd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bd00.md#insn-0047bd18) · [`0047bd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bd00.md#insn-0047bd64)

~~~diff
- 0047bce0 ["INT_ADD", "register:40f0:8", ["const:47bce0:8", "const:4:8"]]
- 0047bce0 ["CALL", null, ["callee:00c580e0:8"]]
+ 0047bd20 ["INT_ADD", "register:40f0:8", ["const:47bd20:8", "const:4:8"]]
+ 0047bd20 ["CALL", null, ["callee:00c580e0:8"]]
- 0047bce0 bytes 00701f94
+ 0047bd20 bytes f0701f94
- 0047bcd8 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0047bcd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047bcd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047bcd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047bd18 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 0047bd18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047bd18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047bd18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047bcd8 bytes 00601391
+ 0047bd18 bytes 00602391
- 0047bd24 ["INT_ADD", "register:40f0:8", ["const:47bd24:8", "const:4:8"]]
- 0047bd24 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047bd64 ["INT_ADD", "register:40f0:8", ["const:47bd64:8", "const:4:8"]]
+ 0047bd64 ["CALL", null, ["callee:00c53d00:8"]]
- 0047bd24 bytes ef5e1f94
+ 0047bd64 bytes e75f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20cbdcd4c4e2807696b7ec7faf212377"></a>

### [`0047bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md) → [`0047bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md) FUN_0047bde0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) · 呼出先 9件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6dc.md) [`0047d6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6e0.md) [`0047d6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6e4.md) [`0056b1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b1fc.md)
- 新版 呼出元 1件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) · 呼出先 9件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d71c.md) [`0047d720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d720.md) [`0047d724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d724.md) [`0056b23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b23c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.47% / 新版 98.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047be14",
      "incomplete_value": false,
      "site": "0047be14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bdd4",
      "incomplete_value": false,
      "site": "0047bdd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047be14",
      "DATA",
      [
        "storage",
        "00c64f58",
        null,
        "undefined *"
      ]
    ],
    [
      "0047bec4",
      "READ",
      [
        "storage",
        "00c64f88",
        null,
        "undefined *"
      ]
    ],
    [
      "0047bf38",
      "READ",
      [
        "storage",
        "00c64f78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047be14",
      "DATA",
      [
        "storage",
        "00c65358",
        null,
        "undefined *"
      ]
    ],
    [
      "0047bec4",
      "READ",
      [
        "storage",
        "00c65388",
        null,
        "undefined *"
      ]
    ],
    [
      "0047bf38",
      "READ",
      [
        "storage",
        "00c65378",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md#insn-0047bdcc) · [`0047bdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md#insn-0047bdd0) · [`0047bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md#insn-0047bde4)
- 新版 [`0047be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md#insn-0047be0c) · [`0047be10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md#insn-0047be10) · [`0047be24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md#insn-0047be24)

~~~diff
- 0047bdcc ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0047be0c ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0047bdcc bytes 483f00b0
+ 0047be0c bytes 483f00d0
- 0047bdd0 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0047bdd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047bdd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047bdd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047be10 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0047be10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047be10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047be10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047bdd0 bytes 08613d91
+ 0047be10 bytes 08610d91
- 0047bde4 ["INT_ADD", "register:40f0:8", ["const:47bde4:8", "const:4:8"]]
- 0047bde4 ["CALL", null, ["callee:0047d724:8"]]
+ 0047be24 ["INT_ADD", "register:40f0:8", ["const:47be24:8", "const:4:8"]]
+ 0047be24 ["CALL", null, ["callee:0047d724:8"]]
- 0047bde4 bytes 40060094
+ 0047be24 bytes 40060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-417be01295d3a0ca3d11e5ea5238af87"></a>

### [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) → [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) FUN_0047c048

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047cd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd9c.md) [`0047cec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cec8.md) [`0047fa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fa0c.md) · 呼出先 22件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0047bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md) [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047ca4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md)
- 新版 呼出元 4件 [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047cddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cddc.md) [`0047cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md) [`0047fa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fa4c.md) · 呼出先 22件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0047bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md) [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047c2b4",
      "incomplete_value": true,
      "site": "0047c2b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:f3b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047c274",
      "incomplete_value": true,
      "site": "0047c274",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:e6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047c718",
      "incomplete_value": false,
      "site": "0047c71c",
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
      "definition_site": "0047c6d8",
      "incomplete_value": false,
      "site": "0047c6dc",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047c754",
      "incomplete_value": false,
      "site": "0047c758",
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
      "definition_site": "0047c714",
      "incomplete_value": false,
      "site": "0047c718",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047c29c",
      "READ",
      [
        "storage",
        "0029fe6e",
        null,
        "string"
      ]
    ],
    [
      "0047c718",
      "PARAM",
      [
        "storage",
        "00ca44d8",
        null,
        null
      ]
    ],
    [
      "0047c754",
      "PARAM",
      [
        "storage",
        "00ca44d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047c29c",
      "READ",
      [
        "storage",
        "0029ff3b",
        null,
        "string"
      ]
    ],
    [
      "0047c718",
      "PARAM",
      [
        "storage",
        "00ca48d8",
        null,
        null
      ]
    ],
    [
      "0047c754",
      "PARAM",
      [
        "storage",
        "00ca48d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047c2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md#insn-0047c2b4) · [`0047c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md#insn-0047c69c) · [`0047c6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md#insn-0047c6d8)
- 新版 [`0047c2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md#insn-0047c2f4) · [`0047c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md#insn-0047c6dc) · [`0047c718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md#insn-0047c718)

~~~diff
- 0047c2b4 ["INT_ADD", "register:40f0:8", ["const:47c2b4:8", "const:4:8"]]
- 0047c2b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047c2f4 ["INT_ADD", "register:40f0:8", ["const:47c2f4:8", "const:4:8"]]
+ 0047c2f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0047c2b4 bytes ff6d1f94
+ 0047c2f4 bytes ef6e1f94
- 0047c69c ["COPY", "register:0:8", ["register:4040:8"]]
- 0047c69c ["INT_ADD", "register:40f0:8", ["const:47c69c:8", "const:4:8"]]
- 0047c69c ["CALLIND", null, ["register:0:8"]]
+ 0047c6dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047c6dc ["INT_ADD", "register:40f0:8", ["const:47c6dc:8", "const:4:8"]]
+ 0047c6dc ["CALLIND", null, ["register:0:8"]]
- 0047c69c bytes 00013fd6
+ 0047c6dc bytes 00013fd6
- 0047c6d8 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0047c6d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c6d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c6d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047c718 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 0047c718 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c718 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c718 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c6d8 bytes 00601391
+ 0047c718 bytes 00602391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49d3a7af38248736b5d38395cefbe401"></a>

### [`0047d1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d1b8.md) → [`0047d1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1f8.md) FUN_0047d1f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00853c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c38.md) · 呼出先 2件 [`0047e1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00853c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c78.md) · 呼出先 2件 [`0047e20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047d228",
      "incomplete_value": false,
      "site": "0047d234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d1e8",
      "incomplete_value": false,
      "site": "0047d1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047d234",
      "DATA",
      [
        "storage",
        "00c64fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047d234",
      "DATA",
      [
        "storage",
        "00c653e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d1b8.md#insn-0047d1dc) · [`0047d1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d1b8.md#insn-0047d1e4) · [`0047d1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d1b8.md#insn-0047d1e8)
- 新版 [`0047d21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1f8.md#insn-0047d21c) · [`0047d224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1f8.md#insn-0047d224) · [`0047d228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1f8.md#insn-0047d228)

~~~diff
- 0047d1dc ["INT_ADD", "register:40f0:8", ["const:47d1dc:8", "const:4:8"]]
- 0047d1dc ["CALL", null, ["callee:00c57e90:8"]]
+ 0047d21c ["INT_ADD", "register:40f0:8", ["const:47d21c:8", "const:4:8"]]
+ 0047d21c ["CALL", null, ["callee:00c57e90:8"]]
- 0047d1dc bytes 2d6a1f94
+ 0047d21c bytes 1d6b1f94
- 0047d1e4 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0047d224 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0047d1e4 bytes 283f00f0
+ 0047d224 bytes 483f0090
- 0047d1e8 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0047d1e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047d1e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047d1e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047d228 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 0047d228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047d1e8 bytes 08a13f91
+ 0047d228 bytes 08a10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5ad619265fb1710513d498ff97a2258"></a>

### [`0047d3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3c4.md) → [`0047d404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d404.md) FUN_0047d404

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047d23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d23c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0047d27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0047d410",
      "incomplete_value": false,
      "site": "0047d414",
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
      "definition_site": "0047d3d0",
      "incomplete_value": false,
      "site": "0047d3d4",
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
      "0047d410",
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
      "0047d410",
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

- 旧版 [`0047d3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3c4.md#insn-0047d3d4) · [`0047d3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3c4.md#insn-0047d3d0)
- 新版 [`0047d414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d404.md#insn-0047d414) · [`0047d410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d404.md#insn-0047d410)

~~~diff
- 0047d3d4 ["INT_ADD", "register:40f0:8", ["const:47d3d4:8", "const:4:8"]]
- 0047d3d4 ["CALL", null, ["callee:0043b778:8"]]
+ 0047d414 ["INT_ADD", "register:40f0:8", ["const:47d414:8", "const:4:8"]]
+ 0047d414 ["CALL", null, ["callee:0043b778:8"]]
- 0047d3d4 bytes d9f8fe97
+ 0047d414 bytes d9f8fe97
- 0047d3d0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0047d3d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047d3d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047d3d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047d410 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0047d410 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d410 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d410 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047d3d0 bytes 00303c91
+ 0047d410 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75bccc8c933a78cdc3c66fc75ade0766"></a>

### [`0047d560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d560.md) → [`0047d5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5a0.md) FUN_0047d5a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047d3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3d8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0047d418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d418.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0047d5ac",
      "incomplete_value": false,
      "site": "0047d5b0",
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
      "definition_site": "0047d56c",
      "incomplete_value": false,
      "site": "0047d570",
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
      "0047d5ac",
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
      "0047d5ac",
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

- 旧版 [`0047d570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d560.md#insn-0047d570) · [`0047d56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d560.md#insn-0047d56c)
- 新版 [`0047d5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5a0.md#insn-0047d5b0) · [`0047d5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5a0.md#insn-0047d5ac)

~~~diff
- 0047d570 ["INT_ADD", "register:40f0:8", ["const:47d570:8", "const:4:8"]]
- 0047d570 ["CALL", null, ["callee:0043b778:8"]]
+ 0047d5b0 ["INT_ADD", "register:40f0:8", ["const:47d5b0:8", "const:4:8"]]
+ 0047d5b0 ["CALL", null, ["callee:0043b778:8"]]
- 0047d570 bytes 72f8fe97
+ 0047d5b0 bytes 72f8fe97
- 0047d56c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0047d56c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047d56c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047d56c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047d5ac ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0047d5ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d5ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d5ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047d56c bytes 00303c91
+ 0047d5ac bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f54becbc34611162efbee3a06259d5e"></a>

### [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) → [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) FUN_0047d6b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`0047b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md) [`0047d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) [`0049eb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049eb60.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 8件 [`0047b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md) [`0047d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md) [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) [`0049eba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eba0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0047d6c4",
      "incomplete_value": false,
      "site": "0047d6c8",
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
      "definition_site": "0047d684",
      "incomplete_value": false,
      "site": "0047d688",
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
      "0047d6c4",
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
      "0047d6c4",
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

- 旧版 [`0047d688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md#insn-0047d688) · [`0047d684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md#insn-0047d684)
- 新版 [`0047d6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md#insn-0047d6c8) · [`0047d6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md#insn-0047d6c4)

~~~diff
- 0047d688 ["INT_ADD", "register:40f0:8", ["const:47d688:8", "const:4:8"]]
- 0047d688 ["CALL", null, ["callee:0043b778:8"]]
+ 0047d6c8 ["INT_ADD", "register:40f0:8", ["const:47d6c8:8", "const:4:8"]]
+ 0047d6c8 ["CALL", null, ["callee:0043b778:8"]]
- 0047d688 bytes 2cf8fe97
+ 0047d6c8 bytes 2cf8fe97
- 0047d684 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0047d684 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047d684 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047d684 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047d6c4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0047d6c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d6c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d6c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047d684 bytes 00303c91
+ 0047d6c4 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbb4b1ac8eac190ce43891848afe479e"></a>

### [`0047d694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d694.md) → [`0047d6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6d4.md) FUN_0047d6d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047d6f8",
      "incomplete_value": false,
      "site": "0047d6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d6b8",
      "incomplete_value": false,
      "site": "0047d6b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "0047d6f8",
      "DATA",
      [
        "storage",
        "00c64f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047d6f8",
      "DATA",
      [
        "storage",
        "00c65358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d694.md#insn-0047d6a8) · [`0047d6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d694.md#insn-0047d6b0) · [`0047d6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d694.md#insn-0047d6b4)
- 新版 [`0047d6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6d4.md#insn-0047d6e8) · [`0047d6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6d4.md#insn-0047d6f0) · [`0047d6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6d4.md#insn-0047d6f4)

~~~diff
- 0047d6a8 ["INT_ADD", "register:40f0:8", ["const:47d6a8:8", "const:4:8"]]
- 0047d6a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0047d6e8 ["INT_ADD", "register:40f0:8", ["const:47d6e8:8", "const:4:8"]]
+ 0047d6e8 ["CALL", null, ["callee:00c57e90:8"]]
- 0047d6a8 bytes fa681f94
+ 0047d6e8 bytes ea691f94
- 0047d6b0 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0047d6f0 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0047d6b0 bytes 283f00f0
+ 0047d6f0 bytes 483f0090
- 0047d6b4 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0047d6b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047d6b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047d6b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047d6f4 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0047d6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047d6b4 bytes 08613d91
+ 0047d6f4 bytes 08610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f242a539644813df37b32703b22cc5f"></a>

### [`0047d6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6c8.md) → [`0047d708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d708.md) FUN_0047d708

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047d714",
      "incomplete_value": false,
      "site": "0047d714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d6d4",
      "incomplete_value": false,
      "site": "0047d6d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "0047d714",
      "DATA",
      [
        "storage",
        "00c64f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047d714",
      "DATA",
      [
        "storage",
        "00c65358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6c8.md#insn-0047d6cc) · [`0047d6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6c8.md#insn-0047d6d0)
- 新版 [`0047d70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d708.md#insn-0047d70c) · [`0047d710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d708.md#insn-0047d710)

~~~diff
- 0047d6cc ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 0047d70c ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0047d6cc bytes 293f00f0
+ 0047d70c bytes 493f0090
- 0047d6d0 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0047d6d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047d6d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047d6d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047d710 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0047d710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047d710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047d710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047d6d0 bytes 29613d91
+ 0047d710 bytes 29610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4fdf0920957a6021acaa1604bf587a4"></a>

### [`0047d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md) → [`0047d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md) FUN_0047d860

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md) [`00656e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656e50.md) [`00781004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781004.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 4件 [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md) [`00656e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00656/00656e90.md) [`00781044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781044.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047d9bc",
      "incomplete_value": false,
      "site": "0047d9c4",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d97c",
      "incomplete_value": false,
      "site": "0047d984",
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
            "const:f13:8"
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
      "definition_site": "0047d9e0",
      "incomplete_value": false,
      "site": "0047d9ec",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d9a0",
      "incomplete_value": false,
      "site": "0047d9ac",
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
            "const:ea9:8"
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
      "definition_site": "0047db14",
      "incomplete_value": false,
      "site": "0047db1c",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047dad4",
      "incomplete_value": false,
      "site": "0047dadc",
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
            "const:da7:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047d9bc",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0047d9e0",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0047db14",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047d9bc",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0047d9e0",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0047db14",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md#insn-0047d984) · [`0047d9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md#insn-0047d9ac) · [`0047dadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md#insn-0047dadc)
- 新版 [`0047d9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md#insn-0047d9c4) · [`0047d9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md#insn-0047d9ec) · [`0047db1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md#insn-0047db1c)

~~~diff
- 0047d984 ["INT_ADD", "register:40f0:8", ["const:47d984:8", "const:4:8"]]
- 0047d984 ["CALL", null, ["callee:00441e94:8"]]
+ 0047d9c4 ["INT_ADD", "register:40f0:8", ["const:47d9c4:8", "const:4:8"]]
+ 0047d9c4 ["CALL", null, ["callee:00441e94:8"]]
- 0047d984 bytes 3411ff97
+ 0047d9c4 bytes 3411ff97
- 0047d9ac ["INT_ADD", "register:40f0:8", ["const:47d9ac:8", "const:4:8"]]
- 0047d9ac ["CALL", null, ["callee:004427f4:8"]]
+ 0047d9ec ["INT_ADD", "register:40f0:8", ["const:47d9ec:8", "const:4:8"]]
+ 0047d9ec ["CALL", null, ["callee:004427f4:8"]]
- 0047d9ac bytes 8213ff97
+ 0047d9ec bytes 8213ff97
- 0047dadc ["INT_ADD", "register:40f0:8", ["const:47dadc:8", "const:4:8"]]
- 0047dadc ["CALL", null, ["callee:00441e94:8"]]
+ 0047db1c ["INT_ADD", "register:40f0:8", ["const:47db1c:8", "const:4:8"]]
+ 0047db1c ["CALL", null, ["callee:00441e94:8"]]
- 0047dadc bytes de10ff97
+ 0047db1c bytes de10ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51d1e9adfff31e1931898e2238e8df37"></a>

### [`0047e17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e17c.md) → [`0047e1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1bc.md) FUN_0047e1bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0047e1c0",
      "incomplete_value": false,
      "site": "0047e1c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e180",
      "incomplete_value": false,
      "site": "0047e184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "0047e1c4",
      "DATA",
      [
        "storage",
        "00c64fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047e1c4",
      "DATA",
      [
        "storage",
        "00c653e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e17c.md#insn-0047e17c) · [`0047e180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e17c.md#insn-0047e180)
- 新版 [`0047e1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1bc.md#insn-0047e1bc) · [`0047e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1bc.md#insn-0047e1c0)

~~~diff
- 0047e17c ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0047e1bc ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0047e17c bytes 283f00d0
+ 0047e1bc bytes 283f00f0
- 0047e180 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0047e180 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047e180 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047e180 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047e1c0 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 0047e1c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047e1c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047e1c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047e180 bytes 08a13f91
+ 0047e1c0 bytes 08a10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e7c1dc9bbe12d19dc628b9ab7ff1ffd"></a>

### [`0047e18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e18c.md) → [`0047e1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1cc.md) FUN_0047e1cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047e1dc",
      "incomplete_value": false,
      "site": "0047e1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e19c",
      "incomplete_value": false,
      "site": "0047e1a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "0047e1e4",
      "DATA",
      [
        "storage",
        "00c64fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047e1e4",
      "DATA",
      [
        "storage",
        "00c653e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e18c.md#insn-0047e198) · [`0047e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e18c.md#insn-0047e19c) · [`0047e1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e18c.md#insn-0047e1a8)
- 新版 [`0047e1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1cc.md#insn-0047e1d8) · [`0047e1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1cc.md#insn-0047e1dc) · [`0047e1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1cc.md#insn-0047e1e8)

~~~diff
- 0047e198 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0047e1d8 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0047e198 bytes 283f00d0
+ 0047e1d8 bytes 283f00f0
- 0047e19c ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0047e19c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047e19c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047e19c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047e1dc ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 0047e1dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047e1dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047e1dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047e19c bytes 08a13f91
+ 0047e1dc bytes 08a10f91
- 0047e1a8 ["INT_ADD", "register:40f0:8", ["const:47e1a8:8", "const:4:8"]]
- 0047e1a8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0047e1e8 ["INT_ADD", "register:40f0:8", ["const:47e1e8:8", "const:4:8"]]
+ 0047e1e8 ["CALL", null, ["callee:00c57ea0:8"]]
- 0047e1a8 bytes 3e661f94
+ 0047e1e8 bytes 2e671f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-172689ca41eaeff2a222480578efb6fa"></a>

### [`0047e1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md) → [`0047e20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md) FUN_0047e20c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0047d1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d1b8.md) · 呼出先 12件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`0047d1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1f8.md) · 呼出先 12件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.86% / 新版 84.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 7件, `store_value` 6件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047e24c",
      "incomplete_value": false,
      "site": "0047e24c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e20c",
      "incomplete_value": false,
      "site": "0047e20c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047e2b4",
      "incomplete_value": true,
      "site": "0047e2b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:99a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e274",
      "incomplete_value": true,
      "site": "0047e274",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:95a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047e2cc",
      "incomplete_value": true,
      "site": "0047e2cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e28c",
      "incomplete_value": true,
      "site": "0047e28c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:fec:8"
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
      "0047e24c",
      "DATA",
      [
        "storage",
        "00c65038",
        null,
        "undefined *"
      ]
    ],
    [
      "0047e26c",
      "PARAM",
      [
        "storage",
        "002c9496",
        null,
        "string"
      ]
    ],
    [
      "0047e280",
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
      "0047e24c",
      "DATA",
      [
        "storage",
        "00c65438",
        null,
        "undefined *"
      ]
    ],
    [
      "0047e26c",
      "PARAM",
      [
        "storage",
        "002c94d6",
        null,
        "string"
      ]
    ],
    [
      "0047e280",
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

- 旧版 [`0047e234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md#insn-0047e234) · [`0047e2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md#insn-0047e2b0) · [`0047e2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md#insn-0047e2d0)
- 新版 [`0047e274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md#insn-0047e274) · [`0047e2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md#insn-0047e2f0) · [`0047e310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md#insn-0047e310)

~~~diff
- 0047e234 ["INT_ADD", "register:40f0:8", ["const:47e234:8", "const:4:8"]]
- 0047e234 ["CALL", null, ["callee:00c58190:8"]]
+ 0047e274 ["INT_ADD", "register:40f0:8", ["const:47e274:8", "const:4:8"]]
+ 0047e274 ["CALL", null, ["callee:00c58190:8"]]
- 0047e234 bytes d7661f94
+ 0047e274 bytes c7671f94
- 0047e2b0 ["INT_ADD", "register:40f0:8", ["const:47e2b0:8", "const:4:8"]]
- 0047e2b0 ["CALL", null, ["callee:0047e60c:8"]]
+ 0047e2f0 ["INT_ADD", "register:40f0:8", ["const:47e2f0:8", "const:4:8"]]
+ 0047e2f0 ["CALL", null, ["callee:0047e60c:8"]]
- 0047e2b0 bytes c7000094
+ 0047e2f0 bytes c7000094
- 0047e2d0 ["INT_ADD", "register:40f0:8", ["const:47e2d0:8", "const:4:8"]]
- 0047e2d0 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047e310 ["INT_ADD", "register:40f0:8", ["const:47e310:8", "const:4:8"]]
+ 0047e310 ["CALL", null, ["callee:00c53d00:8"]]
- 0047e2d0 bytes 84551f94
+ 0047e310 bytes 7c561f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8991d0b5572cdba0b667d620fb80dd8"></a>

### [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) → [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) FUN_0047e60c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 118件 [`0047e1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md) [`005ba2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba2d0.md) [`005c421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c421c.md) [`005cc174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc174.md) [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`0047eecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eecc.md) [`0047f010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f010.md) [`0047f10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f10c.md)
- 新版 呼出元 118件 [`0047e20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md) [`005ba310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba310.md) [`005c425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c425c.md) [`005cc1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc1b4.md) [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`0047ef0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ef0c.md) [`0047f050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f050.md) [`0047f14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f14c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047e6d4",
      "incomplete_value": false,
      "site": "0047e6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e694",
      "incomplete_value": false,
      "site": "0047e6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      "0047e6e0",
      "DATA",
      [
        "storage",
        "00c650a8",
        null,
        "pointer"
      ]
    ],
    [
      "0047e828",
      "READ",
      [
        "storage",
        "00c650b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047e6e0",
      "DATA",
      [
        "storage",
        "00c654a8",
        null,
        "pointer"
      ]
    ],
    [
      "0047e828",
      "READ",
      [
        "storage",
        "00c654b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md#insn-0047e618) · [`0047e624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md#insn-0047e624) · [`0047e638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md#insn-0047e638)
- 新版 [`0047e658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md#insn-0047e658) · [`0047e664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md#insn-0047e664) · [`0047e678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md#insn-0047e678)

~~~diff
- 0047e618 ["INT_ADD", "register:40f0:8", ["const:47e618:8", "const:4:8"]]
- 0047e618 ["CALL", null, ["callee:00440f70:8"]]
+ 0047e658 ["INT_ADD", "register:40f0:8", ["const:47e658:8", "const:4:8"]]
+ 0047e658 ["CALL", null, ["callee:00440f70:8"]]
- 0047e618 bytes 460aff97
+ 0047e658 bytes 460aff97
- 0047e624 ["INT_ADD", "register:40f0:8", ["const:47e624:8", "const:4:8"]]
- 0047e624 ["CALL", null, ["callee:0047ef0c:8"]]
+ 0047e664 ["INT_ADD", "register:40f0:8", ["const:47e664:8", "const:4:8"]]
+ 0047e664 ["CALL", null, ["callee:0047ef0c:8"]]
- 0047e624 bytes 2a020094
+ 0047e664 bytes 2a020094
- 0047e638 ["INT_ADD", "register:40f0:8", ["const:47e638:8", "const:4:8"]]
- 0047e638 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047e678 ["INT_ADD", "register:40f0:8", ["const:47e678:8", "const:4:8"]]
+ 0047e678 ["CALL", null, ["callee:00c57eb0:8"]]
- 0047e638 bytes 1e651f94
+ 0047e678 bytes 0e661f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-582ac33ba1d317d9b6bf5e0b444b0a3d"></a>

### [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) → [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) FUN_0047e8dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 92件 [`0047e1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md) [`005ba2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba2d0.md) [`005fa7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fa/005fa7e4.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`00624768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624768.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0047f210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md) [`0047f41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md) [`00489128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489128.md) [`0048a7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a7c8.md)
- 新版 呼出元 92件 [`0047e20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md) [`005ba310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba310.md) [`005fa824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fa/005fa824.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`006247a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/006247a8.md) · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0047f250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md) [`0047f45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md) [`00489168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489168.md) [`0048a808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a808.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047ea24",
      "incomplete_value": false,
      "site": "0047ea30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e9e4",
      "incomplete_value": false,
      "site": "0047e9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047eaa0",
      "incomplete_value": false,
      "site": "0047eab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ea60",
      "incomplete_value": false,
      "site": "0047ea70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047ea30",
      "DATA",
      [
        "storage",
        "00c650a8",
        null,
        "pointer"
      ]
    ],
    [
      "0047eaa0",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047ea30",
      "DATA",
      [
        "storage",
        "00c654a8",
        null,
        "pointer"
      ]
    ],
    [
      "0047eaa0",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md#insn-0047e9b0) · [`0047ea70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md#insn-0047ea70) · [`0047e910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md#insn-0047e910)
- 新版 [`0047e9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md#insn-0047e9f0) · [`0047eab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md#insn-0047eab0) · [`0047e950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md#insn-0047e950)

~~~diff
- 0047e9b0 ["INT_ADD", "register:40f0:8", ["const:47e9b0:8", "const:4:8"]]
- 0047e9b0 ["CALL", null, ["callee:00c584f0:8"]]
+ 0047e9f0 ["INT_ADD", "register:40f0:8", ["const:47e9f0:8", "const:4:8"]]
+ 0047e9f0 ["CALL", null, ["callee:00c584f0:8"]]
- 0047e9b0 bytes d0651f94
+ 0047e9f0 bytes c0661f94
- 0047ea70 ["INT_ADD", "register:40f0:8", ["const:47ea70:8", "const:4:8"]]
- 0047ea70 ["CALL", null, ["callee:0047f45c:8"]]
+ 0047eab0 ["INT_ADD", "register:40f0:8", ["const:47eab0:8", "const:4:8"]]
+ 0047eab0 ["CALL", null, ["callee:0047f45c:8"]]
- 0047ea70 bytes 6b020094
+ 0047eab0 bytes 6b020094
- 0047e910 ["INT_ADD", "register:40f0:8", ["const:47e910:8", "const:4:8"]]
- 0047e910 ["CALL", null, ["callee:0043bb20:8"]]
+ 0047e950 ["INT_ADD", "register:40f0:8", ["const:47e950:8", "const:4:8"]]
+ 0047e950 ["CALL", null, ["callee:0043bb20:8"]]
- 0047e910 bytes 74f4fe97
+ 0047e950 bytes 74f4fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7289cb748639835dc71e47609452730d"></a>

### [`0047eb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eb64.md) → [`0047eba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eba4.md) FUN_0047eba4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c580e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c584e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047ebbc",
      "incomplete_value": false,
      "site": "0047ebc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047eb7c",
      "incomplete_value": false,
      "site": "0047eb80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "0047ebc0",
      "DATA",
      [
        "storage",
        "00c65038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047ebc0",
      "DATA",
      [
        "storage",
        "00c65438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eb64.md#insn-0047eb7c) · [`0047eb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eb64.md#insn-0047eb8c) · [`0047eba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eb64.md#insn-0047eba0)
- 新版 [`0047ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eba4.md#insn-0047ebbc) · [`0047ebcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eba4.md#insn-0047ebcc) · [`0047ebe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eba4.md#insn-0047ebe0)

~~~diff
- 0047eb7c ["COPY", "tmp:0:8", ["const:38:8"]]
- 0047eb7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047eb7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047eb7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047ebbc ["COPY", "tmp:0:8", ["const:438:8"]]
+ 0047ebbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047ebbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047ebbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047eb7c bytes 29e10091
+ 0047ebbc bytes 29e11091
- 0047eb8c ["INT_ADD", "register:40f0:8", ["const:47eb8c:8", "const:4:8"]]
- 0047eb8c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047ebcc ["INT_ADD", "register:40f0:8", ["const:47ebcc:8", "const:4:8"]]
+ 0047ebcc ["CALL", null, ["callee:00c57eb0:8"]]
- 0047eb8c bytes c9631f94
+ 0047ebcc bytes b9641f94
- 0047eba0 ["INT_ADD", "register:40f0:8", ["const:47eba0:8", "const:4:8"]]
- 0047eba0 ["CALL", null, ["callee:00c53d00:8"]]
+ 0047ebe0 ["INT_ADD", "register:40f0:8", ["const:47ebe0:8", "const:4:8"]]
+ 0047ebe0 ["CALL", null, ["callee:00c53d00:8"]]
- 0047eba0 bytes 50531f94
+ 0047ebe0 bytes 48541f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cb667a7ab32d6ecfaff119046f12650"></a>

### [`0047ec00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ec00.md) → [`0047ec40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ec40.md) FUN_0047ec40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c580e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c584e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047ec58",
      "incomplete_value": false,
      "site": "0047ec5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ec18",
      "incomplete_value": false,
      "site": "0047ec1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "0047ec5c",
      "DATA",
      [
        "storage",
        "00c65038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047ec5c",
      "DATA",
      [
        "storage",
        "00c65438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ec18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ec00.md#insn-0047ec18) · [`0047ec28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ec00.md#insn-0047ec28) · [`0047ec3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ec00.md#insn-0047ec3c)
- 新版 [`0047ec58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ec40.md#insn-0047ec58) · [`0047ec68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ec40.md#insn-0047ec68) · [`0047ec7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ec40.md#insn-0047ec7c)

~~~diff
- 0047ec18 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0047ec18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047ec18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047ec18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047ec58 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 0047ec58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047ec58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047ec58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047ec18 bytes 29e10091
+ 0047ec58 bytes 29e11091
- 0047ec28 ["INT_ADD", "register:40f0:8", ["const:47ec28:8", "const:4:8"]]
- 0047ec28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0047ec68 ["INT_ADD", "register:40f0:8", ["const:47ec68:8", "const:4:8"]]
+ 0047ec68 ["CALL", null, ["callee:00c57eb0:8"]]
- 0047ec28 bytes a2631f94
+ 0047ec68 bytes 92641f94
- 0047ec3c ["INT_ADD", "register:40f0:8", ["const:47ec3c:8", "const:4:8"]]
- 0047ec3c ["CALL", null, ["callee:00c53d00:8"]]
+ 0047ec7c ["INT_ADD", "register:40f0:8", ["const:47ec7c:8", "const:4:8"]]
+ 0047ec7c ["CALL", null, ["callee:00c53d00:8"]]
- 0047ec3c bytes 29531f94
+ 0047ec7c bytes 21541f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aa3ab4d711f65f9f4793f4e31401a7f"></a>

### [`0047efd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047efd0.md) → [`0047f010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f010.md) FUN_0047f010

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0047f014",
      "incomplete_value": false,
      "site": "0047f018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047efd4",
      "incomplete_value": false,
      "site": "0047efd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      "0047f018",
      "DATA",
      [
        "storage",
        "00c650a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047f018",
      "DATA",
      [
        "storage",
        "00c654a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047efd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047efd0.md#insn-0047efd4)
- 新版 [`0047f014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f010.md#insn-0047f014)

~~~diff
- 0047efd4 ["COPY", "tmp:0:8", ["const:a8:8"]]
- 0047efd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047efd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047efd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047f014 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 0047f014 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f014 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f014 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047efd4 bytes 08a10291
+ 0047f014 bytes 08a11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b287fb7892728ef6937f1f22590ac0"></a>

### [`0047efe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047efe0.md) → [`0047f020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f020.md) FUN_0047f020

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047f030",
      "incomplete_value": false,
      "site": "0047f038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047eff0",
      "incomplete_value": false,
      "site": "0047eff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      "0047f038",
      "DATA",
      [
        "storage",
        "00c650a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047f038",
      "DATA",
      [
        "storage",
        "00c654a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047eff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047efe0.md#insn-0047eff0) · [`0047effc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047efe0.md#insn-0047effc)
- 新版 [`0047f030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f020.md#insn-0047f030) · [`0047f03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f020.md#insn-0047f03c)

~~~diff
- 0047eff0 ["COPY", "tmp:0:8", ["const:a8:8"]]
- 0047eff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047eff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047eff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047f030 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 0047f030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047eff0 bytes 08a10291
+ 0047f030 bytes 08a11291
- 0047effc ["INT_ADD", "register:40f0:8", ["const:47effc:8", "const:4:8"]]
- 0047effc ["CALL", null, ["callee:00c57ea0:8"]]
+ 0047f03c ["INT_ADD", "register:40f0:8", ["const:47f03c:8", "const:4:8"]]
+ 0047f03c ["CALL", null, ["callee:00c57ea0:8"]]
- 0047effc bytes a9621f94
+ 0047f03c bytes 99631f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f242f8dd71431ea94ce33190cc2132b8"></a>

### [`0047f694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md) → [`0047f6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md) FUN_0047f6d4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0047eca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eca4.md) · 呼出先 8件 [`0047f7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md) [`0047f93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f93c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0047ece4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ece4.md) · 呼出先 8件 [`0047f81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md) [`0047f97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f97c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047f714",
      "incomplete_value": false,
      "site": "0047f720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f6d4",
      "incomplete_value": false,
      "site": "0047f6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047f748",
      "incomplete_value": true,
      "site": "0047f750",
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f708",
      "incomplete_value": true,
      "site": "0047f710",
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047f720",
      "DATA",
      [
        "storage",
        "00c650f8",
        null,
        "pointer"
      ]
    ],
    [
      "0047f748",
      "READ",
      [
        "storage",
        "002c2d10",
        null,
        null
      ]
    ],
    [
      "0047f798",
      "READ",
      [
        "storage",
        "00c65108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047f720",
      "DATA",
      [
        "storage",
        "00c654f8",
        null,
        "pointer"
      ]
    ],
    [
      "0047f748",
      "READ",
      [
        "storage",
        "002c2d50",
        null,
        null
      ]
    ],
    [
      "0047f798",
      "READ",
      [
        "storage",
        "00c65508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md#insn-0047f720) · [`0047f6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md#insn-0047f6c4) · [`0047f6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md#insn-0047f6d4)
- 新版 [`0047f760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md#insn-0047f760) · [`0047f704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md#insn-0047f704) · [`0047f714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md#insn-0047f714)

~~~diff
- 0047f720 ["INT_ADD", "register:40f0:8", ["const:47f720:8", "const:4:8"]]
- 0047f720 ["CALL", null, ["callee:0047f81c:8"]]
+ 0047f760 ["INT_ADD", "register:40f0:8", ["const:47f760:8", "const:4:8"]]
+ 0047f760 ["CALL", null, ["callee:0047f81c:8"]]
- 0047f720 bytes 2f000094
+ 0047f760 bytes 2f000094
- 0047f6c4 ["INT_ADD", "register:40f0:8", ["const:47f6c4:8", "const:4:8"]]
- 0047f6c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0047f704 ["INT_ADD", "register:40f0:8", ["const:47f704:8", "const:4:8"]]
+ 0047f704 ["CALL", null, ["callee:00c57e90:8"]]
- 0047f6c4 bytes f3601f94
+ 0047f704 bytes e3611f94
- 0047f6d4 ["COPY", "tmp:0:8", ["const:f8:8"]]
- 0047f6d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047f6d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047f6d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047f714 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 0047f714 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f714 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f714 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047f6d4 bytes 08e10391
+ 0047f714 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de43edf4ecf1a6fe8715887310c1ce0c"></a>

### [`0047f7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md) → [`0047f81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md) FUN_0047f81c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047f694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md) · 呼出先 6件 [`0047fc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fc2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d00.md) [`00c57d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d10.md)
- 新版 呼出元 1件 [`0047f6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md) · 呼出先 6件 [`0047fc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fc6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58100.md) [`00c58110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58110.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

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
      "definition_site": "0047f888",
      "incomplete_value": false,
      "site": "0047f894",
      "value": [
        "leaf",
        "const:47fc6c:8"
      ]
    },
    "old": {
      "definition_site": "0047f848",
      "incomplete_value": false,
      "site": "0047f854",
      "value": [
        "leaf",
        "const:47fc2c:8"
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047f8d8",
      "incomplete_value": false,
      "site": "0047f8dc",
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
            "const:f27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f898",
      "incomplete_value": false,
      "site": "0047f89c",
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
            "const:e5a:8"
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
      "0047f888",
      "PARAM",
      [
        "storage",
        "0047fc2c",
        null,
        null
      ]
    ],
    [
      "0047f8d8",
      "PARAM",
      [
        "storage",
        "002a3e5a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047f888",
      "PARAM",
      [
        "storage",
        "0047fc6c",
        null,
        null
      ]
    ],
    [
      "0047f8d8",
      "PARAM",
      [
        "storage",
        "002a3f27",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md#insn-0047f854) · [`0047f89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md#insn-0047f89c) · [`0047f810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md#insn-0047f810)
- 新版 [`0047f894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md#insn-0047f894) · [`0047f8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md#insn-0047f8dc) · [`0047f850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md#insn-0047f850)

~~~diff
- 0047f854 ["INT_ADD", "register:40f0:8", ["const:47f854:8", "const:4:8"]]
- 0047f854 ["CALL", null, ["callee:00c58110:8"]]
+ 0047f894 ["INT_ADD", "register:40f0:8", ["const:47f894:8", "const:4:8"]]
+ 0047f894 ["CALL", null, ["callee:00c58110:8"]]
- 0047f854 bytes 2f611f94
+ 0047f894 bytes 1f621f94
- 0047f89c ["INT_ADD", "register:40f0:8", ["const:47f89c:8", "const:4:8"]]
- 0047f89c ["CALL", null, ["callee:00c58120:8"]]
+ 0047f8dc ["INT_ADD", "register:40f0:8", ["const:47f8dc:8", "const:4:8"]]
+ 0047f8dc ["CALL", null, ["callee:00c58120:8"]]
- 0047f89c bytes 21611f94
+ 0047f8dc bytes 11621f94
- 0047f810 ["INT_ADD", "register:40f0:8", ["const:47f810:8", "const:4:8"]]
- 0047f810 ["CALL", null, ["callee:00c57e90:8"]]
+ 0047f850 ["INT_ADD", "register:40f0:8", ["const:47f850:8", "const:4:8"]]
+ 0047f850 ["CALL", null, ["callee:00c57e90:8"]]
- 0047f810 bytes a0601f94
+ 0047f850 bytes 90611f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec13817917b498fe7915dbbeb1622b78"></a>

### [`0047f8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f8e8.md) → [`0047f928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f928.md) FUN_0047f928

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

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
      "definition_site": "0047f94c",
      "incomplete_value": true,
      "site": "0047f94c",
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
      "definition_site": "0047f90c",
      "incomplete_value": true,
      "site": "0047f90c",
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
      "0047f940",
      "READ",
      [
        "storage",
        "00c9a850",
        null,
        "pointer"
      ]
    ],
    [
      "0047f94c",
      "DATA",
      [
        "storage",
        "00c928d8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0047f940",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "0047f94c",
      "DATA",
      [
        "storage",
        "00c92cd8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f8e8.md#insn-0047f900) · [`0047f910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f8e8.md#insn-0047f910) · [`0047f918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f8e8.md#insn-0047f918)
- 新版 [`0047f940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f928.md#insn-0047f940) · [`0047f950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f928.md#insn-0047f950) · [`0047f958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f928.md#insn-0047f958)

~~~diff
- 0047f900 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:850:8"]]
- 0047f900 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047f940 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
+ 0047f940 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0047f900 bytes 082944f9
+ 0047f940 bytes 082946f9
- 0047f910 ["INT_ADD", "register:40f0:8", ["const:47f910:8", "const:4:8"]]
- 0047f910 ["CALL", null, ["callee:00c580d0:8"]]
+ 0047f950 ["INT_ADD", "register:40f0:8", ["const:47f950:8", "const:4:8"]]
+ 0047f950 ["CALL", null, ["callee:00c580d0:8"]]
- 0047f910 bytes f0601f94
+ 0047f950 bytes e0611f94
- 0047f918 ["INT_ADD", "register:40f0:8", ["const:47f918:8", "const:4:8"]]
- 0047f918 ["CALL", null, ["callee:00c57e60:8"]]
+ 0047f958 ["INT_ADD", "register:40f0:8", ["const:47f958:8", "const:4:8"]]
+ 0047f958 ["CALL", null, ["callee:00c57e60:8"]]
- 0047f918 bytes 52601f94
+ 0047f958 bytes 42611f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9818c78fe0547dc4b06bfabfae39b7e1"></a>

### [`0047f964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f964.md) → [`0047f9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f9a4.md) FUN_0047f9a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047fa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fa0c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58150.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047fa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fa4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58550.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047f9c8",
      "value": [
        "leaf",
        "ram:47fa4c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047f988",
      "value": [
        "leaf",
        "ram:47fa0c:8"
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
      "0047f9c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047fa0c"
      ]
    ]
  ],
  "added": [
    [
      "0047f9c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047fa4c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f964.md#insn-0047f988) · [`0047f990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f964.md#insn-0047f990) · [`0047fa04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f964.md#insn-0047fa04)
- 新版 [`0047f9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f9a4.md#insn-0047f9c8) · [`0047f9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f9a4.md#insn-0047f9d0) · [`0047fa44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f9a4.md#insn-0047fa44)

~~~diff
- 0047f988 ["INT_ADD", "register:40f0:8", ["const:47f988:8", "const:4:8"]]
- 0047f988 ["CALL", null, ["ram:47fa0c:8"]]
+ 0047f9c8 ["INT_ADD", "register:40f0:8", ["const:47f9c8:8", "const:4:8"]]
+ 0047f9c8 ["CALL", null, ["ram:47fa4c:8"]]
- 0047f988 bytes 21000094
+ 0047f9c8 bytes 21000094
- 0047f990 ["INT_ADD", "register:40f0:8", ["const:47f990:8", "const:4:8"]]
- 0047f990 ["CALL", null, ["callee:00c58550:8"]]
+ 0047f9d0 ["INT_ADD", "register:40f0:8", ["const:47f9d0:8", "const:4:8"]]
+ 0047f9d0 ["CALL", null, ["callee:00c58550:8"]]
- 0047f990 bytes f0611f94
+ 0047f9d0 bytes e0621f94
- 0047fa04 ["INT_ADD", "register:40f0:8", ["const:47fa04:8", "const:4:8"]]
- 0047fa04 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0047fa44 ["INT_ADD", "register:40f0:8", ["const:47fa44:8", "const:4:8"]]
+ 0047fa44 ["CALL", null, ["callee:00c57ee0:8"]]
- 0047fa04 bytes 37601f94
+ 0047fa44 bytes 27611f94
~~~


<a id="compare-5685a1bce5fb9e0a9e7be7d1d8fd7864"></a>

### [`0047fd48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fd48.md) → [`0047fd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd88.md) _INIT_17

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047fdc4",
      "incomplete_value": true,
      "site": "0047fde0",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047fd84",
      "incomplete_value": true,
      "site": "0047fda0",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ee6:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047fde8",
      "incomplete_value": true,
      "site": "0047fe04",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047fda8",
      "incomplete_value": true,
      "site": "0047fdc4",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ef9:8"
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
      "definition_site": "0047fe08",
      "incomplete_value": true,
      "site": "0047fe24",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047fdc8",
      "incomplete_value": true,
      "site": "0047fde4",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047fdc4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0047fde8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0047fe08",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047fdc4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0047fde8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0047fe08",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047fdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fd48.md#insn-0047fdc0) · [`0047fde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fd48.md#insn-0047fde0) · [`0047fea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fd48.md#insn-0047fea8)
- 新版 [`0047fe00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd88.md#insn-0047fe00) · [`0047fe20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd88.md#insn-0047fe20) · [`0047fee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd88.md#insn-0047fee8)

~~~diff
- 0047fdc0 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0047fdc0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047fdc0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047fdc0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047fe00 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0047fe00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047fe00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047fe00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047fdc0 bytes 4a093691
+ 0047fe00 bytes 4a093791
- 0047fde0 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0047fde0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047fde0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047fde0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047fe20 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0047fe20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047fe20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047fe20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047fde0 bytes 4a553a91
+ 0047fe20 bytes 4a893d91
- 0047fea8 ["INT_ADD", "register:40f0:8", ["const:47fea8:8", "const:4:8"]]
- 0047fea8 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0047fee8 ["INT_ADD", "register:40f0:8", ["const:47fee8:8", "const:4:8"]]
+ 0047fee8 ["CALL", null, ["callee:0043b7f8:8"]]
- 0047fea8 bytes 44eefe97
+ 0047fee8 bytes 44eefe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb25f41c18d79f488e9a9a2c4d850d95"></a>

### [`004813f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md) → [`00481430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md) FUN_00481430

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 18件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`00637810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/00637810.md) · 呼出先 0件 
- 新版 呼出元 18件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00637850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00637/00637850.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00481444",
      "incomplete_value": false,
      "site": "00481448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00481404",
      "incomplete_value": false,
      "site": "00481408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:140:8"
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
      "00481448",
      "DATA",
      [
        "storage",
        "00c65140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00481448",
      "DATA",
      [
        "storage",
        "00c65540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00481404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md#insn-00481404)
- 新版 [`00481444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md#insn-00481444)

~~~diff
- 00481404 ["COPY", "tmp:0:8", ["const:140:8"]]
- 00481404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00481404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00481404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00481444 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 00481444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00481444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00481444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00481404 bytes 08010591
+ 00481444 bytes 08011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aca515bf33f87d323327a4ddbdc390f0"></a>

### [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) → [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) FUN_00482b0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 17件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) · 呼出先 34件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0043de38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043de38.md) [`00440ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`00481420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md)
- 新版 呼出元 17件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) · 呼出先 34件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043de78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043de78.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`00481460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481460.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.14% / 新版 95.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 13件, `call_target` 4件, `store_destination` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048324c",
      "incomplete_value": true,
      "site": "0048324c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048320c",
      "incomplete_value": true,
      "site": "0048320c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004833bc",
      "incomplete_value": false,
      "site": "004833c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048337c",
      "incomplete_value": false,
      "site": "00483380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "ordinal": 64,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00483620",
      "incomplete_value": true,
      "site": "00483620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004835e0",
      "incomplete_value": true,
      "site": "004835e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "ordinal": 76,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00483160",
      "READ",
      [
        "storage",
        "00ca4b70",
        null,
        "undefined1"
      ]
    ],
    [
      "0048316c",
      "READ",
      [
        "storage",
        "00ca4b68",
        null,
        "undefined8"
      ]
    ],
    [
      "004831c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "00483160",
      "READ",
      [
        "storage",
        "00ca4f70",
        null,
        "undefined1"
      ]
    ],
    [
      "0048316c",
      "READ",
      [
        "storage",
        "00ca4f68",
        null,
        "undefined8"
      ]
    ],
    [
      "004831c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md#insn-00483180) · [`00483194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md#insn-00483194) · [`004831bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md#insn-004831bc)
- 新版 [`004831c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md#insn-004831c0) · [`004831d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md#insn-004831d4) · [`004831fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md#insn-004831fc)

~~~diff
- 00483180 ["INT_ADD", "register:40f0:8", ["const:483180:8", "const:4:8"]]
- 00483180 ["CALL", null, ["ram:48ccb8:8"]]
+ 004831c0 ["INT_ADD", "register:40f0:8", ["const:4831c0:8", "const:4:8"]]
+ 004831c0 ["CALL", null, ["ram:48ccf8:8"]]
- 00483180 bytes ce260094
+ 004831c0 bytes ce260094
- 00483194 ["INT_ADD", "register:40f0:8", ["const:483194:8", "const:4:8"]]
- 00483194 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004831d4 ["INT_ADD", "register:40f0:8", ["const:4831d4:8", "const:4:8"]]
+ 004831d4 ["CALL", null, ["callee:0043ddd8:8"]]
- 00483194 bytes 01ebfe97
+ 004831d4 bytes 01ebfe97
- 004831bc ["INT_ADD", "register:40f0:8", ["const:4831bc:8", "const:4:8"]]
- 004831bc ["CALL", null, ["ram:48ccb8:8"]]
+ 004831fc ["INT_ADD", "register:40f0:8", ["const:4831fc:8", "const:4:8"]]
+ 004831fc ["CALL", null, ["ram:48ccf8:8"]]
- 004831bc bytes bf260094
+ 004831fc bytes bf260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d1047325cc32465140d4829502ef032"></a>

### [`0048388c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md) → [`004838cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md) FUN_004838cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 18件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00486d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d8c.md) [`00486e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e64.md) [`004870e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004870e8.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md)
- 新版 呼出元 2件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 18件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00486dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486dcc.md) [`00486ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486ea4.md) [`00487128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487128.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.11% / 新版 97.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00483ac0",
      "incomplete_value": false,
      "site": "00483ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483a80",
      "incomplete_value": false,
      "site": "00483a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00483ae8",
      "incomplete_value": false,
      "site": "00483ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483aa8",
      "incomplete_value": false,
      "site": "00483aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00483b10",
      "incomplete_value": false,
      "site": "00483b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483ad0",
      "incomplete_value": false,
      "site": "00483ae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00483ac8",
      "DATA",
      [
        "storage",
        "00c65230",
        null,
        "pointer"
      ]
    ],
    [
      "00483ae8",
      "DATA",
      [
        "storage",
        "00c65280",
        null,
        null
      ]
    ],
    [
      "00483b20",
      "DATA",
      [
        "storage",
        "00c652c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00483ac8",
      "DATA",
      [
        "storage",
        "00c65630",
        null,
        "pointer"
      ]
    ],
    [
      "00483ae8",
      "DATA",
      [
        "storage",
        "00c65680",
        null,
        null
      ]
    ],
    [
      "00483b20",
      "DATA",
      [
        "storage",
        "00c656c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md#insn-00483a68) · [`00483ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md#insn-00483ac8) · [`00483b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md#insn-00483b40)
- 新版 [`00483aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md#insn-00483aa8) · [`00483b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md#insn-00483b08) · [`00483b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md#insn-00483b80)

~~~diff
- 00483a68 ["INT_ADD", "register:40f0:8", ["const:483a68:8", "const:4:8"]]
- 00483a68 ["CALL", null, ["callee:0055e870:8"]]
+ 00483aa8 ["INT_ADD", "register:40f0:8", ["const:483aa8:8", "const:4:8"]]
+ 00483aa8 ["CALL", null, ["callee:0055e870:8"]]
- 00483a68 bytes 726b0394
+ 00483aa8 bytes 726b0394
- 00483ac8 ["INT_ADD", "register:40f0:8", ["const:483ac8:8", "const:4:8"]]
- 00483ac8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00483b08 ["INT_ADD", "register:40f0:8", ["const:483b08:8", "const:4:8"]]
+ 00483b08 ["CALL", null, ["callee:00c57e90:8"]]
- 00483ac8 bytes f24f1f94
+ 00483b08 bytes e2501f94
- 00483b40 ["INT_ADD", "register:40f0:8", ["const:483b40:8", "const:4:8"]]
- 00483b40 ["CALL", null, ["callee:00c57e80:8"]]
+ 00483b80 ["INT_ADD", "register:40f0:8", ["const:483b80:8", "const:4:8"]]
+ 00483b80 ["CALL", null, ["callee:00c57e80:8"]]
- 00483b40 bytes d04f1f94
+ 00483b80 bytes c0501f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c5b425393b72b933147910b17ca6511"></a>

### [`00484780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md) → [`004847c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md) FUN_004847c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00872560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872560.md) [`009d5b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d5b5c.md) [`009d9790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d9/009d9790.md) [`00ab86a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab86a8.md) · 呼出先 14件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00470e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470e14.md) [`004716e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004716e4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) [`00481f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481f44.md)
- 新版 呼出元 4件 [`008725a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008725a0.md) [`009d5cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md) [`009d992c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d992c.md) [`00ab88a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab8/00ab88a4.md) · 呼出先 14件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00470e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470e54.md) [`00471724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471724.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) [`00481f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00484878",
      "incomplete_value": false,
      "site": "00484884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00484838",
      "incomplete_value": false,
      "site": "00484844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004847f0",
      "value": [
        "leaf",
        "ram:470e54:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004847b0",
      "value": [
        "leaf",
        "ram:470e14:8"
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
      "site": "00484a4c",
      "value": [
        "leaf",
        "ram:470e54:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00484a0c",
      "value": [
        "leaf",
        "ram:470e14:8"
      ]
    },
    "ordinal": 28,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004847f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e14"
      ]
    ],
    [
      "00484884",
      "DATA",
      [
        "storage",
        "00c65140",
        null,
        "undefined *"
      ]
    ],
    [
      "0048490c",
      "DATA",
      [
        "storage",
        "00c65140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004847f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "00484884",
      "DATA",
      [
        "storage",
        "00c65540",
        null,
        "undefined *"
      ]
    ],
    [
      "0048490c",
      "DATA",
      [
        "storage",
        "00c65540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004847b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md#insn-004847b0) · [`00484884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md#insn-00484884) · [`00484a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md#insn-00484a0c)
- 新版 [`004847f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md#insn-004847f0) · [`004848c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md#insn-004848c4) · [`00484a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md#insn-00484a4c)

~~~diff
- 004847b0 ["INT_ADD", "register:40f0:8", ["const:4847b0:8", "const:4:8"]]
- 004847b0 ["CALL", null, ["ram:470e14:8"]]
+ 004847f0 ["INT_ADD", "register:40f0:8", ["const:4847f0:8", "const:4:8"]]
+ 004847f0 ["CALL", null, ["ram:470e54:8"]]
- 004847b0 bytes 99b1ff97
+ 004847f0 bytes 99b1ff97
- 00484884 ["INT_ADD", "register:40f0:8", ["const:484884:8", "const:4:8"]]
- 00484884 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004848c4 ["INT_ADD", "register:40f0:8", ["const:4848c4:8", "const:4:8"]]
+ 004848c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00484884 bytes 8b4c1f94
+ 004848c4 bytes 7b4d1f94
- 00484a0c ["INT_ADD", "register:40f0:8", ["const:484a0c:8", "const:4:8"]]
- 00484a0c ["CALL", null, ["ram:470e14:8"]]
+ 00484a4c ["INT_ADD", "register:40f0:8", ["const:484a4c:8", "const:4:8"]]
+ 00484a4c ["CALL", null, ["ram:470e54:8"]]
- 00484a0c bytes 02b1ff97
+ 00484a4c bytes 02b1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07484f51ebfadcf3a5817a51710191b6"></a>

### [`00484c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484c9c.md) → [`00484cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484cdc.md) FUN_00484cdc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`00a148e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a148e4.md) · 呼出先 4件 [`005975d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`00a14a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14a80.md) · 呼出先 4件 [`00597610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00484d10",
      "incomplete_value": false,
      "site": "00484d18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00484cd0",
      "incomplete_value": false,
      "site": "00484cd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00484d18",
      "DATA",
      [
        "storage",
        "00c65198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00484d18",
      "DATA",
      [
        "storage",
        "00c65598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00484cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484c9c.md#insn-00484cd0) · [`00484cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484c9c.md#insn-00484cec) · [`00484d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484c9c.md#insn-00484d0c)
- 新版 [`00484d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484cdc.md#insn-00484d10) · [`00484d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484cdc.md#insn-00484d2c) · [`00484d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484cdc.md#insn-00484d4c)

~~~diff
- 00484cd0 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00484cd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00484cd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00484cd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00484d10 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00484d10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00484d10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00484d10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00484cd0 bytes 08610691
+ 00484d10 bytes 08611691
- 00484cec ["INT_ADD", "register:40f0:8", ["const:484cec:8", "const:4:8"]]
- 00484cec ["CALL", null, ["callee:00597610:8"]]
+ 00484d2c ["INT_ADD", "register:40f0:8", ["const:484d2c:8", "const:4:8"]]
+ 00484d2c ["CALL", null, ["callee:00597610:8"]]
- 00484cec bytes 394a0494
+ 00484d2c bytes 394a0494
- 00484d0c ["INT_ADD", "register:40f0:8", ["const:484d0c:8", "const:4:8"]]
- 00484d0c ["CALL", null, ["callee:00c53d00:8"]]
+ 00484d4c ["INT_ADD", "register:40f0:8", ["const:484d4c:8", "const:4:8"]]
+ 00484d4c ["CALL", null, ["callee:00c53d00:8"]]
- 00484d0c bytes f53a1f94
+ 00484d4c bytes ed3b1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1c925fb06e425061c0bdbdc417b8a2a"></a>

### [`00485370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485370.md) → [`004853b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004853b0.md) FUN_004853b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004855e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/004855e0.md) · 呼出先 8件 [`0055e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e830.md) [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00485620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485620.md) · 呼出先 8件 [`0055e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e870.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.24% / 新版 99.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048558c",
      "incomplete_value": false,
      "site": "00485594",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048554c",
      "incomplete_value": false,
      "site": "00485554",
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
            "const:30e:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048558c",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0048558c",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00485514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485370.md#insn-00485514) · [`00485554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485370.md#insn-00485554) · [`004853c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485370.md#insn-004853c0)
- 新版 [`00485554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004853b0.md#insn-00485554) · [`00485594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004853b0.md#insn-00485594) · [`00485400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004853b0.md#insn-00485400)

~~~diff
- 00485514 ["INT_ADD", "register:40f0:8", ["const:485514:8", "const:4:8"]]
- 00485514 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00485554 ["INT_ADD", "register:40f0:8", ["const:485554:8", "const:4:8"]]
+ 00485554 ["CALL", null, ["callee:00c57eb0:8"]]
- 00485514 bytes 67491f94
+ 00485554 bytes 574a1f94
- 00485554 ["INT_ADD", "register:40f0:8", ["const:485554:8", "const:4:8"]]
- 00485554 ["CALL", null, ["callee:00c58190:8"]]
+ 00485594 ["INT_ADD", "register:40f0:8", ["const:485594:8", "const:4:8"]]
+ 00485594 ["CALL", null, ["callee:00c58190:8"]]
- 00485554 bytes 0f4a1f94
+ 00485594 bytes ff4a1f94
- 004853c0 ["INT_ADD", "register:40f0:8", ["const:4853c0:8", "const:4:8"]]
- 004853c0 ["CALL", null, ["callee:0055e870:8"]]
+ 00485400 ["INT_ADD", "register:40f0:8", ["const:485400:8", "const:4:8"]]
+ 00485400 ["CALL", null, ["callee:0055e870:8"]]
- 004853c0 bytes 1c650394
+ 00485400 bytes 1c650394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eec28d77192c9169f750fda1d51800c2"></a>

### [`00485ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md) → [`00485b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md) FUN_00485b20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00481420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md) [`00485ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00481460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481460.md) [`00485b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00485c78",
      "incomplete_value": false,
      "site": "00485c80",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00485c38",
      "incomplete_value": false,
      "site": "00485c40",
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
            "const:f13:8"
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
      "definition_site": "00485d34",
      "incomplete_value": false,
      "site": "00485d3c",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00485cf4",
      "incomplete_value": false,
      "site": "00485cfc",
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
            "const:da7:8"
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
      "definition_site": "00485d4c",
      "incomplete_value": false,
      "site": "00485d58",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00485d0c",
      "incomplete_value": false,
      "site": "00485d18",
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
            "const:ea9:8"
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
      "00485c78",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00485d34",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "00485d4c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00485c78",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00485d34",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "00485d4c",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00485c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md#insn-00485c40) · [`00485cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md#insn-00485cfc) · [`00485d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md#insn-00485d18)
- 新版 [`00485c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md#insn-00485c80) · [`00485d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md#insn-00485d3c) · [`00485d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md#insn-00485d58)

~~~diff
- 00485c40 ["INT_ADD", "register:40f0:8", ["const:485c40:8", "const:4:8"]]
- 00485c40 ["CALL", null, ["callee:00441e94:8"]]
+ 00485c80 ["INT_ADD", "register:40f0:8", ["const:485c80:8", "const:4:8"]]
+ 00485c80 ["CALL", null, ["callee:00441e94:8"]]
- 00485c40 bytes 85f0fe97
+ 00485c80 bytes 85f0fe97
- 00485cfc ["INT_ADD", "register:40f0:8", ["const:485cfc:8", "const:4:8"]]
- 00485cfc ["CALL", null, ["callee:00441e94:8"]]
+ 00485d3c ["INT_ADD", "register:40f0:8", ["const:485d3c:8", "const:4:8"]]
+ 00485d3c ["CALL", null, ["callee:00441e94:8"]]
- 00485cfc bytes 56f0fe97
+ 00485d3c bytes 56f0fe97
- 00485d18 ["INT_ADD", "register:40f0:8", ["const:485d18:8", "const:4:8"]]
- 00485d18 ["CALL", null, ["callee:004427f4:8"]]
+ 00485d58 ["INT_ADD", "register:40f0:8", ["const:485d58:8", "const:4:8"]]
+ 00485d58 ["CALL", null, ["callee:004427f4:8"]]
- 00485d18 bytes a7f2fe97
+ 00485d58 bytes a7f2fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f03f8e13aa0b3ea3f805e2878890f4a"></a>

### [`00486418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486418.md) → [`00486458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486458.md) FUN_00486458

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00485ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md) [`00486418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486418.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00485b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md) [`00486458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486458.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004865a8",
      "incomplete_value": false,
      "site": "004865b0",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486568",
      "incomplete_value": false,
      "site": "00486570",
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
            "const:f13:8"
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
      "definition_site": "00486664",
      "incomplete_value": false,
      "site": "0048666c",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486624",
      "incomplete_value": false,
      "site": "0048662c",
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
            "const:da7:8"
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
      "definition_site": "0048667c",
      "incomplete_value": false,
      "site": "00486688",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048663c",
      "incomplete_value": false,
      "site": "00486648",
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
            "const:ea9:8"
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
      "004865a8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00486664",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0048667c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004865a8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00486664",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0048667c",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486418.md#insn-00486570) · [`0048662c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486418.md#insn-0048662c) · [`00486648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486418.md#insn-00486648)
- 新版 [`004865b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486458.md#insn-004865b0) · [`0048666c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486458.md#insn-0048666c) · [`00486688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486458.md#insn-00486688)

~~~diff
- 00486570 ["INT_ADD", "register:40f0:8", ["const:486570:8", "const:4:8"]]
- 00486570 ["CALL", null, ["callee:00441e94:8"]]
+ 004865b0 ["INT_ADD", "register:40f0:8", ["const:4865b0:8", "const:4:8"]]
+ 004865b0 ["CALL", null, ["callee:00441e94:8"]]
- 00486570 bytes 39eefe97
+ 004865b0 bytes 39eefe97
- 0048662c ["INT_ADD", "register:40f0:8", ["const:48662c:8", "const:4:8"]]
- 0048662c ["CALL", null, ["callee:00441e94:8"]]
+ 0048666c ["INT_ADD", "register:40f0:8", ["const:48666c:8", "const:4:8"]]
+ 0048666c ["CALL", null, ["callee:00441e94:8"]]
- 0048662c bytes 0aeefe97
+ 0048666c bytes 0aeefe97
- 00486648 ["INT_ADD", "register:40f0:8", ["const:486648:8", "const:4:8"]]
- 00486648 ["CALL", null, ["callee:004427f4:8"]]
+ 00486688 ["INT_ADD", "register:40f0:8", ["const:486688:8", "const:4:8"]]
+ 00486688 ["CALL", null, ["callee:004427f4:8"]]
- 00486648 bytes 5bf0fe97
+ 00486688 bytes 5bf0fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cf275bb0f76c0879bd4528b4c84eb6c"></a>

### [`00486d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d38.md) → [`00486d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d78.md) FUN_00486d78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) [`00508324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508324.md) [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) [`00a67638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67638.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 4件 [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`00508364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508364.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) [`00a67830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67830.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "00486d84",
      "incomplete_value": false,
      "site": "00486d88",
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
      "definition_site": "00486d44",
      "incomplete_value": false,
      "site": "00486d48",
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
      "00486d84",
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
      "00486d84",
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

- 旧版 [`00486d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d38.md#insn-00486d48) · [`00486d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d38.md#insn-00486d44)
- 新版 [`00486d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d78.md#insn-00486d88) · [`00486d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d78.md#insn-00486d84)

~~~diff
- 00486d48 ["INT_ADD", "register:40f0:8", ["const:486d48:8", "const:4:8"]]
- 00486d48 ["CALL", null, ["callee:00442930:8"]]
+ 00486d88 ["INT_ADD", "register:40f0:8", ["const:486d88:8", "const:4:8"]]
+ 00486d88 ["CALL", null, ["callee:00442930:8"]]
- 00486d48 bytes eaeefe97
+ 00486d88 bytes eaeefe97
- 00486d44 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00486d44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00486d44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00486d44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00486d84 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00486d84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00486d84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00486d84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00486d44 bytes 00303c91
+ 00486d84 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4d9da5d78f1cd4ecb47c465d63cc82b"></a>

### [`00486d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d4c.md) → [`00486d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d8c.md) FUN_00486d8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "00486d90",
      "incomplete_value": false,
      "site": "00486d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486d50",
      "incomplete_value": false,
      "site": "00486d54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "00486d94",
      "DATA",
      [
        "storage",
        "00c65230",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00486d94",
      "DATA",
      [
        "storage",
        "00c65630",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d4c.md#insn-00486d50)
- 新版 [`00486d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d8c.md#insn-00486d90)

~~~diff
- 00486d50 ["COPY", "tmp:0:8", ["const:230:8"]]
- 00486d50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486d50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486d50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486d90 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00486d90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486d90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486d90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486d50 bytes 08c10891
+ 00486d90 bytes 08c11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d6e100179deed394eb38dd67e5b27ee"></a>

### [`00486d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d5c.md) → [`00486d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d9c.md) FUN_00486d9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00486dac",
      "incomplete_value": false,
      "site": "00486db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486d6c",
      "incomplete_value": false,
      "site": "00486d74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "00486db4",
      "DATA",
      [
        "storage",
        "00c65230",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00486db4",
      "DATA",
      [
        "storage",
        "00c65630",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d5c.md#insn-00486d6c) · [`00486d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d5c.md#insn-00486d78)
- 新版 [`00486dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d9c.md#insn-00486dac) · [`00486db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d9c.md#insn-00486db8)

~~~diff
- 00486d6c ["COPY", "tmp:0:8", ["const:230:8"]]
- 00486d6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486d6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486d6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486dac ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00486dac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486dac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486dac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486d6c bytes 08c10891
+ 00486dac bytes 08c11891
- 00486d78 ["INT_ADD", "register:40f0:8", ["const:486d78:8", "const:4:8"]]
- 00486d78 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00486db8 ["INT_ADD", "register:40f0:8", ["const:486db8:8", "const:4:8"]]
+ 00486db8 ["CALL", null, ["callee:00c57ea0:8"]]
- 00486d78 bytes 4a431f94
+ 00486db8 bytes 3a441f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61d7bb12decc0d7e08714fb00225fae8"></a>

### [`00486d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d8c.md) → [`00486dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486dcc.md) FUN_00486dcc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0048388c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`004838cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00486de0",
      "incomplete_value": false,
      "site": "00486de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486da0",
      "incomplete_value": false,
      "site": "00486da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:280:8"
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
      "00486de4",
      "DATA",
      [
        "storage",
        "00c65280",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00486de4",
      "DATA",
      [
        "storage",
        "00c65680",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d8c.md#insn-00486da0) · [`00486db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d8c.md#insn-00486db4) · [`00486dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d8c.md#insn-00486dd4)
- 新版 [`00486de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486dcc.md#insn-00486de0) · [`00486df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486dcc.md#insn-00486df4) · [`00486e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486dcc.md#insn-00486e14)

~~~diff
- 00486da0 ["COPY", "tmp:0:8", ["const:280:8"]]
- 00486da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486de0 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 00486de0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486de0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486de0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486da0 bytes 08010a91
+ 00486de0 bytes 08011a91
- 00486db4 ["INT_ADD", "register:40f0:8", ["const:486db4:8", "const:4:8"]]
- 00486db4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00486df4 ["INT_ADD", "register:40f0:8", ["const:486df4:8", "const:4:8"]]
+ 00486df4 ["CALL", null, ["callee:00c53d00:8"]]
- 00486db4 bytes cb321f94
+ 00486df4 bytes c3331f94
- 00486dd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00486dd4 ["INT_ADD", "register:40f0:8", ["const:486dd4:8", "const:4:8"]]
- 00486dd4 ["CALLIND", null, ["register:0:8"]]
+ 00486e14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00486e14 ["INT_ADD", "register:40f0:8", ["const:486e14:8", "const:4:8"]]
+ 00486e14 ["CALLIND", null, ["register:0:8"]]
- 00486dd4 bytes 00013fd6
+ 00486e14 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e008b48aec8e0a0753f6c5715daf411a"></a>

### [`00486e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e24.md) → [`00486e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e64.md) FUN_00486e64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "00486e68",
      "incomplete_value": false,
      "site": "00486e6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486e28",
      "incomplete_value": false,
      "site": "00486e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "00486e6c",
      "DATA",
      [
        "storage",
        "00c652c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00486e6c",
      "DATA",
      [
        "storage",
        "00c656c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e24.md#insn-00486e28)
- 新版 [`00486e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e64.md#insn-00486e68)

~~~diff
- 00486e28 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00486e28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486e28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486e28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486e68 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00486e68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486e68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486e68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486e28 bytes 08010b91
+ 00486e68 bytes 08011b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b86a37299253186cfb9afdc1ae4d6e04"></a>

### [`00486e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e34.md) → [`00486e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e74.md) FUN_00486e74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00486e84",
      "incomplete_value": false,
      "site": "00486e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486e44",
      "incomplete_value": false,
      "site": "00486e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "00486e8c",
      "DATA",
      [
        "storage",
        "00c652c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00486e8c",
      "DATA",
      [
        "storage",
        "00c656c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e34.md#insn-00486e44) · [`00486e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e34.md#insn-00486e50)
- 新版 [`00486e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e74.md#insn-00486e84) · [`00486e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e74.md#insn-00486e90)

~~~diff
- 00486e44 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00486e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486e84 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00486e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486e44 bytes 08010b91
+ 00486e84 bytes 08011b91
- 00486e50 ["INT_ADD", "register:40f0:8", ["const:486e50:8", "const:4:8"]]
- 00486e50 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00486e90 ["INT_ADD", "register:40f0:8", ["const:486e90:8", "const:4:8"]]
+ 00486e90 ["CALL", null, ["callee:00c57ea0:8"]]
- 00486e50 bytes 14431f94
+ 00486e90 bytes 04441f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8403658d15802364664d4ff96ed2292"></a>

### [`00486e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e64.md) → [`00486ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486ea4.md) FUN_00486ea4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0048388c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`004838cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00486ebc",
      "incomplete_value": false,
      "site": "00486ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486e7c",
      "incomplete_value": false,
      "site": "00486e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00486ef8",
      "incomplete_value": false,
      "site": "00486efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486eb8",
      "incomplete_value": false,
      "site": "00486ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "00486ec0",
      "DATA",
      [
        "storage",
        "00c65310",
        null,
        null
      ]
    ],
    [
      "00486efc",
      "DATA",
      [
        "storage",
        "00c65358",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00486ec0",
      "DATA",
      [
        "storage",
        "00c65710",
        null,
        null
      ]
    ],
    [
      "00486efc",
      "DATA",
      [
        "storage",
        "00c65758",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e64.md#insn-00486e7c) · [`00486e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e64.md#insn-00486e90) · [`00486ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e64.md#insn-00486ea4)
- 新版 [`00486ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486ea4.md#insn-00486ebc) · [`00486ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486ea4.md#insn-00486ed0) · [`00486ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486ea4.md#insn-00486ee4)

~~~diff
- 00486e7c ["COPY", "tmp:0:8", ["const:310:8"]]
- 00486e7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486e7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486e7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486ebc ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00486ebc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486ebc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486ebc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486e7c bytes 08410c91
+ 00486ebc bytes 08411c91
- 00486e90 ["INT_ADD", "register:40f0:8", ["const:486e90:8", "const:4:8"]]
- 00486e90 ["CALL", null, ["callee:00c53d00:8"]]
+ 00486ed0 ["INT_ADD", "register:40f0:8", ["const:486ed0:8", "const:4:8"]]
+ 00486ed0 ["CALL", null, ["callee:00c53d00:8"]]
- 00486e90 bytes 94321f94
+ 00486ed0 bytes 8c331f94
- 00486ea4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00486ea4 ["INT_ADD", "register:40f0:8", ["const:486ea4:8", "const:4:8"]]
- 00486ea4 ["CALLIND", null, ["register:0:8"]]
+ 00486ee4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00486ee4 ["INT_ADD", "register:40f0:8", ["const:486ee4:8", "const:4:8"]]
+ 00486ee4 ["CALLIND", null, ["register:0:8"]]
- 00486ea4 bytes 00013fd6
+ 00486ee4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c887ef43cad8696127bc649fa82a7abf"></a>

### [`004870e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004870e8.md) → [`00487128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487128.md) FUN_00487128

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0048388c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md) · 呼出先 5件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`004838cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00487168",
      "incomplete_value": false,
      "site": "0048716c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487128",
      "incomplete_value": false,
      "site": "0048712c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0048717c",
      "incomplete_value": false,
      "site": "0048717c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048713c",
      "incomplete_value": false,
      "site": "0048713c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0048719c",
      "incomplete_value": false,
      "site": "004871a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048715c",
      "incomplete_value": false,
      "site": "00487160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
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
      "0048716c",
      "DATA",
      [
        "storage",
        "00c65370",
        null,
        "undefined *"
      ]
    ],
    [
      "0048717c",
      "DATA",
      [
        "storage",
        "00c65400",
        null,
        "pointer"
      ]
    ],
    [
      "004871a0",
      "DATA",
      [
        "storage",
        "00c653c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0048716c",
      "DATA",
      [
        "storage",
        "00c65770",
        null,
        "undefined *"
      ]
    ],
    [
      "0048717c",
      "DATA",
      [
        "storage",
        "00c65800",
        null,
        "pointer"
      ]
    ],
    [
      "004871a0",
      "DATA",
      [
        "storage",
        "00c657c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004870e8.md#insn-00487118) · [`00487128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004870e8.md#insn-00487128) · [`00487154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004870e8.md#insn-00487154)
- 新版 [`00487158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487128.md#insn-00487158) · [`00487168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487128.md#insn-00487168) · [`00487194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487128.md#insn-00487194)

~~~diff
- 00487118 ["COPY", "tmp:0:8", ["const:400:8"]]
- 00487118 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00487118 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00487118 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00487158 ["COPY", "tmp:0:8", ["const:800:8"]]
+ 00487158 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00487158 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00487158 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00487118 bytes 29011091
+ 00487158 bytes 29012091
- 00487128 ["COPY", "tmp:0:8", ["const:370:8"]]
- 00487128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00487128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00487128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00487168 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00487168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00487168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00487168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00487128 bytes 08c10d91
+ 00487168 bytes 08c11d91
- 00487154 ["INT_ADD", "register:40f0:8", ["const:487154:8", "const:4:8"]]
- 00487154 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00487194 ["INT_ADD", "register:40f0:8", ["const:487194:8", "const:4:8"]]
+ 00487194 ["CALL", null, ["callee:00c53cd0:8"]]
- 00487154 bytes d7311f94
+ 00487194 bytes cf321f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7e2f349d7282f21c618313a86c7e207"></a>

### [`00487224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487224.md) → [`00487264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487264.md) FUN_00487264

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "00487268",
      "incomplete_value": false,
      "site": "0048726c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487228",
      "incomplete_value": false,
      "site": "0048722c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "0048726c",
      "DATA",
      [
        "storage",
        "00c65370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0048726c",
      "DATA",
      [
        "storage",
        "00c65770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487224.md#insn-00487228)
- 新版 [`00487268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487264.md#insn-00487268)

~~~diff
- 00487228 ["COPY", "tmp:0:8", ["const:370:8"]]
- 00487228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00487228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00487228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00487268 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00487268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00487268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00487268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00487228 bytes 08c10d91
+ 00487268 bytes 08c11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7109711f0257aa09b4e5c519ba4500dc"></a>

### [`00487234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487234.md) → [`00487274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487274.md) FUN_00487274

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00487284",
      "incomplete_value": false,
      "site": "0048728c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487244",
      "incomplete_value": false,
      "site": "0048724c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "0048728c",
      "DATA",
      [
        "storage",
        "00c65370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0048728c",
      "DATA",
      [
        "storage",
        "00c65770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487234.md#insn-00487244) · [`00487250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487234.md#insn-00487250)
- 新版 [`00487284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487274.md#insn-00487284) · [`00487290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487274.md#insn-00487290)

~~~diff
- 00487244 ["COPY", "tmp:0:8", ["const:370:8"]]
- 00487244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00487244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00487244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00487284 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00487284 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00487284 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00487284 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00487244 bytes 08c10d91
+ 00487284 bytes 08c11d91
- 00487250 ["INT_ADD", "register:40f0:8", ["const:487250:8", "const:4:8"]]
- 00487250 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00487290 ["INT_ADD", "register:40f0:8", ["const:487290:8", "const:4:8"]]
+ 00487290 ["CALL", null, ["callee:00c57ea0:8"]]
- 00487250 bytes 14421f94
+ 00487290 bytes 04431f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea633d55fc57ed539973b2a2f24a516"></a>

### [`00487264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487264.md) → [`004872a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004872a4.md) FUN_004872a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004872bc",
      "incomplete_value": false,
      "site": "004872c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048727c",
      "incomplete_value": false,
      "site": "00487280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004872f8",
      "incomplete_value": false,
      "site": "004872fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004872b8",
      "incomplete_value": false,
      "site": "004872bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "004872c0",
      "DATA",
      [
        "storage",
        "00c653c0",
        null,
        null
      ]
    ],
    [
      "004872fc",
      "DATA",
      [
        "storage",
        "00c65400",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004872c0",
      "DATA",
      [
        "storage",
        "00c657c0",
        null,
        null
      ]
    ],
    [
      "004872fc",
      "DATA",
      [
        "storage",
        "00c65800",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048727c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487264.md#insn-0048727c) · [`00487290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487264.md#insn-00487290) · [`004872a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487264.md#insn-004872a4)
- 新版 [`004872bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004872a4.md#insn-004872bc) · [`004872d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004872a4.md#insn-004872d0) · [`004872e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004872a4.md#insn-004872e4)

~~~diff
- 0048727c ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 0048727c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0048727c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0048727c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004872bc ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 004872bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004872bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004872bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0048727c bytes 08010f91
+ 004872bc bytes 08011f91
- 00487290 ["INT_ADD", "register:40f0:8", ["const:487290:8", "const:4:8"]]
- 00487290 ["CALL", null, ["callee:00c53d00:8"]]
+ 004872d0 ["INT_ADD", "register:40f0:8", ["const:4872d0:8", "const:4:8"]]
+ 004872d0 ["CALL", null, ["callee:00c53d00:8"]]
- 00487290 bytes 94311f94
+ 004872d0 bytes 8c321f94
- 004872a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004872a4 ["INT_ADD", "register:40f0:8", ["const:4872a4:8", "const:4:8"]]
- 004872a4 ["CALLIND", null, ["register:0:8"]]
+ 004872e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004872e4 ["INT_ADD", "register:40f0:8", ["const:4872e4:8", "const:4:8"]]
+ 004872e4 ["CALLIND", null, ["register:0:8"]]
- 004872a4 bytes 00013fd6
+ 004872e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-970c53be21d2f01f24abda97daa5995d"></a>

### [`00487304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487304.md) → [`00487344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487344.md) FUN_00487344

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00487358",
      "incomplete_value": false,
      "site": "0048735c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487318",
      "incomplete_value": false,
      "site": "0048731c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "0048735c",
      "DATA",
      [
        "storage",
        "00c65400",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048735c",
      "DATA",
      [
        "storage",
        "00c65800",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487304.md#insn-00487318) · [`0048732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487304.md#insn-0048732c) · [`0048734c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487304.md#insn-0048734c)
- 新版 [`00487358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487344.md#insn-00487358) · [`0048736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487344.md#insn-0048736c) · [`0048738c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487344.md#insn-0048738c)

~~~diff
- 00487318 ["COPY", "tmp:0:8", ["const:400:8"]]
- 00487318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00487318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00487318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00487358 ["COPY", "tmp:0:8", ["const:800:8"]]
+ 00487358 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00487358 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00487358 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00487318 bytes 08011091
+ 00487358 bytes 08012091
- 0048732c ["INT_ADD", "register:40f0:8", ["const:48732c:8", "const:4:8"]]
- 0048732c ["CALL", null, ["callee:00c53d00:8"]]
+ 0048736c ["INT_ADD", "register:40f0:8", ["const:48736c:8", "const:4:8"]]
+ 0048736c ["CALL", null, ["callee:00c53d00:8"]]
- 0048732c bytes 6d311f94
+ 0048736c bytes 65321f94
- 0048734c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048734c ["INT_ADD", "register:40f0:8", ["const:48734c:8", "const:4:8"]]
- 0048734c ["CALLIND", null, ["register:0:8"]]
+ 0048738c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048738c ["INT_ADD", "register:40f0:8", ["const:48738c:8", "const:4:8"]]
+ 0048738c ["CALLIND", null, ["register:0:8"]]
- 0048734c bytes 00013fd6
+ 0048738c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a440f643767c66dd85e15ebc9304bd4e"></a>

### [`0048754c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048754c.md) → [`0048758c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048758c.md) _INIT_18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004875c8",
      "incomplete_value": true,
      "site": "004875e4",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487588",
      "incomplete_value": true,
      "site": "004875a4",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ee6:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004875ec",
      "incomplete_value": true,
      "site": "00487608",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004875ac",
      "incomplete_value": true,
      "site": "004875c8",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:ef9:8"
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
      "definition_site": "0048760c",
      "incomplete_value": true,
      "site": "00487628",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004875cc",
      "incomplete_value": true,
      "site": "004875e8",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004875c8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "004875ec",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0048760c",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004875c8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "004875ec",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0048760c",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004875c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048754c.md#insn-004875c4) · [`004875e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048754c.md#insn-004875e4) · [`004876ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048754c.md#insn-004876ac)
- 新版 [`00487604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048758c.md#insn-00487604) · [`00487624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048758c.md#insn-00487624) · [`004876ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048758c.md#insn-004876ec)

~~~diff
- 004875c4 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 004875c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004875c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004875c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00487604 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00487604 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00487604 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00487604 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004875c4 bytes 4a093691
+ 00487604 bytes 4a093791
- 004875e4 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 004875e4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004875e4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004875e4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00487624 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00487624 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00487624 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00487624 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004875e4 bytes 4a553a91
+ 00487624 bytes 4a893d91
- 004876ac ["INT_ADD", "register:40f0:8", ["const:4876ac:8", "const:4:8"]]
- 004876ac ["CALL", null, ["callee:0043b7f8:8"]]
+ 004876ec ["INT_ADD", "register:40f0:8", ["const:4876ec:8", "const:4:8"]]
+ 004876ec ["CALL", null, ["callee:0043b7f8:8"]]
- 004876ac bytes 43d0fe97
+ 004876ec bytes 43d0fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f53a6a9feadfb7a56ac475ba90509a5c"></a>

### [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) → [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) FUN_00487e20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 153件 [`0043d73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`00444b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`0046d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) · 呼出先 2件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md)
- 新版 呼出元 153件 [`0043d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d77c.md) [`00444bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444bd8.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) · 呼出先 2件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c581f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 68.33% / 新版 68.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00487e70",
      "incomplete_value": true,
      "site": "00487e70",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487e30",
      "incomplete_value": true,
      "site": "00487e30",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00487e50",
      "incomplete_value": false,
      "site": "00487e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487e10",
      "incomplete_value": false,
      "site": "00487e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00487e7c",
      "incomplete_value": true,
      "site": "00487e7c",
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
      "definition_site": "00487e3c",
      "incomplete_value": true,
      "site": "00487e3c",
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
      "00487e44",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00487e48",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "00487e5c",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00487e44",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00487e48",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00487e5c",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md#insn-00487e04) · [`00487e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md#insn-00487e08)
- 新版 [`00487e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md#insn-00487e54) · [`00487e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md#insn-00487e44) · [`00487e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md#insn-00487e48)

~~~diff
+ 00487e54 ["COPY", "register:40b8:8", ["register:4000:8"]]
+ 00487e54 bytes f70300aa
- 00487e04 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:7b8:8"]]
- 00487e04 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00487e44 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:bb8:8"]]
+ 00487e44 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00487e04 bytes 18df43f9
+ 00487e44 bytes 18df45f9
- 00487e08 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:888:8"]]
- 00487e08 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00487e48 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:c88:8"]]
+ 00487e48 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 00487e08 bytes 394744f9
+ 00487e48 bytes 394746f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d506ef0f891c2e696734ea4489e9329"></a>

### [`00488650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488650.md) → [`00488690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488690.md) FUN_00488690

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md) · 呼出先 1件 [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) · 呼出先 1件 [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

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
      "definition_site": "004886a8",
      "incomplete_value": false,
      "site": "004886b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488668",
      "incomplete_value": false,
      "site": "00488670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "004886b0",
      "DATA",
      [
        "storage",
        "00c65478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004886b0",
      "DATA",
      [
        "storage",
        "00c65878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00488660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488650.md#insn-00488660) · [`00488668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488650.md#insn-00488668)
- 新版 [`004886a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488690.md#insn-004886a0) · [`004886a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488690.md#insn-004886a8)

~~~diff
- 00488660 ["INT_ADD", "register:40f0:8", ["const:488660:8", "const:4:8"]]
- 00488660 ["CALL", null, ["callee:00487e20:8"]]
+ 004886a0 ["INT_ADD", "register:40f0:8", ["const:4886a0:8", "const:4:8"]]
+ 004886a0 ["CALL", null, ["callee:00487e20:8"]]
- 00488660 bytes e0fdff97
+ 004886a0 bytes e0fdff97
- 00488668 ["COPY", "tmp:0:8", ["const:478:8"]]
- 00488668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00488668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00488668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004886a8 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 004886a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004886a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004886a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00488668 bytes 08e11191
+ 004886a8 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b570c89c47b55786286beac1aa3ec22a"></a>

### [`00488750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md) → [`00488790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md) FUN_00488790

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00444b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) · 呼出先 14件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00470e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470e14.md) [`004716e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004716e4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) [`00488014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488014.md)
- 新版 呼出元 3件 [`00444bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444bd8.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) · 呼出先 14件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00470e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470e54.md) [`00471724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471724.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) [`00488054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00488930",
      "incomplete_value": true,
      "site": "00488930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004888f0",
      "incomplete_value": true,
      "site": "004888f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004887c0",
      "value": [
        "leaf",
        "ram:470e54:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00488780",
      "value": [
        "leaf",
        "ram:470e14:8"
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
      "site": "004888a4",
      "value": [
        "leaf",
        "ram:470e54:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00488864",
      "value": [
        "leaf",
        "ram:470e14:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004887c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e14"
      ]
    ],
    [
      "004888a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e14"
      ]
    ],
    [
      "00488910",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "004887c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "004888a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "00488910",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00488780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md#insn-00488780) · [`00488824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md#insn-00488824) · [`00488864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md#insn-00488864)
- 新版 [`004887c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md#insn-004887c0) · [`00488864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md#insn-00488864) · [`004888a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md#insn-004888a4)

~~~diff
- 00488780 ["INT_ADD", "register:40f0:8", ["const:488780:8", "const:4:8"]]
- 00488780 ["CALL", null, ["ram:470e14:8"]]
+ 004887c0 ["INT_ADD", "register:40f0:8", ["const:4887c0:8", "const:4:8"]]
+ 004887c0 ["CALL", null, ["ram:470e54:8"]]
- 00488780 bytes a5a1ff97
+ 004887c0 bytes a5a1ff97
- 00488824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00488824 ["INT_ADD", "register:40f0:8", ["const:488824:8", "const:4:8"]]
- 00488824 ["CALLIND", null, ["register:0:8"]]
+ 00488864 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00488864 ["INT_ADD", "register:40f0:8", ["const:488864:8", "const:4:8"]]
+ 00488864 ["CALLIND", null, ["register:0:8"]]
- 00488824 bytes 00013fd6
+ 00488864 bytes 00013fd6
- 00488864 ["INT_ADD", "register:40f0:8", ["const:488864:8", "const:4:8"]]
- 00488864 ["CALL", null, ["ram:470e14:8"]]
+ 004888a4 ["INT_ADD", "register:40f0:8", ["const:4888a4:8", "const:4:8"]]
+ 004888a4 ["CALL", null, ["ram:470e54:8"]]
- 00488864 bytes 6ca1ff97
+ 004888a4 bytes 6ca1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

