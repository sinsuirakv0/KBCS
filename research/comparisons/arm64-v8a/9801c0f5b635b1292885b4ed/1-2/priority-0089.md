# v16.0.0 → v16.0.1 · 最優先の変更候補 (89)

[一覧の目次](README.md)

<a id="compare-216358b4bd5e0387aae89b2f463e7eeb"></a>

### [`00c26d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26d70.md) → [`00c27198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27198.md) _ZNSt6__ndk112ctype_bynameIcEC1EPKcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5c0.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 1件 [`00c5e9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9c0.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c271d0",
      "incomplete_value": false,
      "site": "00c271d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26da8",
      "incomplete_value": false,
      "site": "00c26da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "definition_site": "00c27210",
      "incomplete_value": false,
      "site": "00c27220",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26de8",
      "incomplete_value": false,
      "site": "00c26df8",
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
            "const:9e0:8"
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
      "00c271b8",
      "READ",
      [
        "storage",
        "00c9b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c271d0",
      "DATA",
      [
        "storage",
        "00310f58",
        null,
        null
      ]
    ],
    [
      "00c271d4",
      "DATA",
      [
        "storage",
        "00c933d0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c271b8",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c271d0",
      "DATA",
      [
        "storage",
        "00310f98",
        null,
        null
      ]
    ],
    [
      "00c271d4",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26d70.md#insn-00c26df8) · [`00c26d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26d70.md#insn-00c26d90) · [`00c26da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26d70.md#insn-00c26da0)
- 新版 [`00c27220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27198.md#insn-00c27220) · [`00c271b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27198.md#insn-00c271b8) · [`00c271c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27198.md#insn-00c271c8)

~~~diff
- 00c26df8 ["INT_ADD", "register:40f0:8", ["const:c26df8:8", "const:4:8"]]
- 00c26df8 ["CALL", null, ["callee:00c25934:8"]]
+ 00c27220 ["INT_ADD", "register:40f0:8", ["const:c27220:8", "const:4:8"]]
+ 00c27220 ["CALL", null, ["callee:00c25934:8"]]
- 00c26df8 bytes c5f9ff97
+ 00c27220 bytes c5f9ff97
- 00c26d90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9d0:8"]]
- 00c26d90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c271b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
+ 00c271b8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c26d90 bytes 29e944f9
+ 00c271b8 bytes 29e946f9
- 00c26da0 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00c26da0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c26da0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c26da0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c271c8 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00c271c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c271c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c271c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c26da0 bytes 4a613d91
+ 00c271c8 bytes 4a613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-604984b61e5aa98a3e4e723b686cb54c"></a>

### [`00c26e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26e58.md) → [`00c27280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27280.md) _ZNSt6__ndk112ctype_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5e440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e440.md) [`00c5e5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5d0.md) · 呼出先 6件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md)
- 新版 呼出元 2件 [`00c5e840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e840.md) [`00c5e9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9d0.md) · 呼出先 6件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c27298",
      "incomplete_value": true,
      "site": "00c272a0",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26e70",
      "incomplete_value": true,
      "site": "00c26e78",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c272bc",
      "incomplete_value": true,
      "site": "00c272bc",
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
      "definition_site": "00c26e94",
      "incomplete_value": true,
      "site": "00c26e94",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c272fc",
      "incomplete_value": false,
      "site": "00c2730c",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26ed4",
      "incomplete_value": false,
      "site": "00c26ee4",
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
            "const:9e0:8"
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
      "00c272a0",
      "DATA",
      [
        "storage",
        "00310f58",
        null,
        null
      ]
    ],
    [
      "00c272ac",
      "READ",
      [
        "storage",
        "00c9b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c272bc",
      "DATA",
      [
        "storage",
        "00c933d0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c272a0",
      "DATA",
      [
        "storage",
        "00310f98",
        null,
        null
      ]
    ],
    [
      "00c272ac",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c272bc",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26e58.md#insn-00c26ee4) · [`00c26e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26e58.md#insn-00c26e70) · [`00c26e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26e58.md#insn-00c26e84)
- 新版 [`00c2730c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27280.md#insn-00c2730c) · [`00c27298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27280.md#insn-00c27298) · [`00c272ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27280.md#insn-00c272ac)

~~~diff
- 00c26ee4 ["INT_ADD", "register:40f0:8", ["const:c26ee4:8", "const:4:8"]]
- 00c26ee4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00c2730c ["INT_ADD", "register:40f0:8", ["const:c2730c:8", "const:4:8"]]
+ 00c2730c ["CALL", null, ["callee:00c580b0:8"]]
- 00c26ee4 bytes 73c30094
+ 00c2730c bytes 69c30094
- 00c26e70 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00c26e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c26e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c26e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c27298 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00c27298 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c27298 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c27298 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c26e70 bytes 08613d91
+ 00c27298 bytes 08613e91
- 00c26e84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00c26e84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c272ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00c272ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c26e84 bytes 08e944f9
+ 00c272ac bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06a48b9cd00c8c47a94b23845d2c2351"></a>

### [`00c272e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c272e8.md) → [`00c27710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27710.md) _ZNSt6__ndk112ctype_bynameIwEC2EPKcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5f0.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 1件 [`00c5e9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9f0.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2773c",
      "incomplete_value": true,
      "site": "00c2773c",
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
      "definition_site": "00c27314",
      "incomplete_value": true,
      "site": "00c27314",
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
      "definition_site": "00c27778",
      "incomplete_value": false,
      "site": "00c27788",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c27350",
      "incomplete_value": false,
      "site": "00c27360",
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
            "const:aa0:8"
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
      "00c27730",
      "READ",
      [
        "storage",
        "00c9b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2773c",
      "DATA",
      [
        "storage",
        "00c93438",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c27778",
      "PARAM",
      [
        "storage",
        "002bfaa0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c27730",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2773c",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c27778",
      "PARAM",
      [
        "storage",
        "002bfae0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c27360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c272e8.md#insn-00c27360) · [`00c27308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c272e8.md#insn-00c27308) · [`00c27320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c272e8.md#insn-00c27320)
- 新版 [`00c27788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27710.md#insn-00c27788) · [`00c27730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27710.md#insn-00c27730) · [`00c27748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c27710.md#insn-00c27748)

~~~diff
- 00c27360 ["INT_ADD", "register:40f0:8", ["const:c27360:8", "const:4:8"]]
- 00c27360 ["CALL", null, ["callee:00c25934:8"]]
+ 00c27788 ["INT_ADD", "register:40f0:8", ["const:c27788:8", "const:4:8"]]
+ 00c27788 ["CALL", null, ["callee:00c25934:8"]]
- 00c27360 bytes 6bf8ff97
+ 00c27788 bytes 6bf8ff97
- 00c27308 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d8:8"]]
- 00c27308 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c27730 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
+ 00c27730 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c27308 bytes 08ed44f9
+ 00c27730 bytes 08ed46f9
- 00c27320 ["INT_ADD", "register:40f0:8", ["const:c27320:8", "const:4:8"]]
- 00c27320 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c27748 ["INT_ADD", "register:40f0:8", ["const:c27748:8", "const:4:8"]]
+ 00c27748 ["CALL", null, ["callee:00c5d220:8"]]
- 00c27320 bytes c0d60094
+ 00c27748 bytes b6d60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4373729a45519fe853c345f29dfc8ef"></a>

### [`00c273c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c273c0.md) → [`00c277e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c277e8.md) _ZNSt6__ndk112ctype_bynameIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5e450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e450.md) [`00c5e610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e610.md) · 呼出先 6件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md)
- 新版 呼出元 2件 [`00c5e850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e850.md) [`00c5ea10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea10.md) · 呼出先 6件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c27814",
      "incomplete_value": true,
      "site": "00c27814",
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
      "definition_site": "00c273ec",
      "incomplete_value": true,
      "site": "00c273ec",
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
      "definition_site": "00c27854",
      "incomplete_value": false,
      "site": "00c27864",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2742c",
      "incomplete_value": false,
      "site": "00c2743c",
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
            "const:aa0:8"
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
      "00c27808",
      "READ",
      [
        "storage",
        "00c9b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c27814",
      "DATA",
      [
        "storage",
        "00c93438",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c27854",
      "PARAM",
      [
        "storage",
        "002bfaa0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c27808",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c27814",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c27854",
      "PARAM",
      [
        "storage",
        "002bfae0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2743c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c273c0.md#insn-00c2743c) · [`00c273e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c273c0.md#insn-00c273e0) · [`00c27408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c273c0.md#insn-00c27408)
- 新版 [`00c27864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c277e8.md#insn-00c27864) · [`00c27808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c277e8.md#insn-00c27808) · [`00c27830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c27/00c277e8.md#insn-00c27830)

~~~diff
- 00c2743c ["INT_ADD", "register:40f0:8", ["const:c2743c:8", "const:4:8"]]
- 00c2743c ["CALL", null, ["callee:00c580b0:8"]]
+ 00c27864 ["INT_ADD", "register:40f0:8", ["const:c27864:8", "const:4:8"]]
+ 00c27864 ["CALL", null, ["callee:00c580b0:8"]]
- 00c2743c bytes 1dc20094
+ 00c27864 bytes 13c20094
- 00c273e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d8:8"]]
- 00c273e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c27808 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
+ 00c27808 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c273e0 bytes 08ed44f9
+ 00c27808 bytes 08ed46f9
- 00c27408 ["INT_ADD", "register:40f0:8", ["const:c27408:8", "const:4:8"]]
- 00c27408 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c27830 ["INT_ADD", "register:40f0:8", ["const:c27830:8", "const:4:8"]]
+ 00c27830 ["CALL", null, ["callee:00c5d220:8"]]
- 00c27408 bytes 86d60094
+ 00c27830 bytes 7cd60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc22c994fa39b70a785923c90a9631ee"></a>

### [`00c27dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27dd8.md) → [`00c28200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28200.md) _ZNSt6__ndk17codecvtIwc9mbstate_tEC1Em

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5a470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a470.md) [`00c5e3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e3f0.md) · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 2件 [`00c5a870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a870.md) [`00c5e7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e7f0.md) · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 74.29% / 新版 74.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2823c",
      "incomplete_value": true,
      "site": "00c28240",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
    "old": {
      "definition_site": "00c27e14",
      "incomplete_value": true,
      "site": "00c27e18",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:898:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00c28278",
      "incomplete_value": true,
      "site": "00c28278",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c27e50",
      "incomplete_value": true,
      "site": "00c27e50",
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
            "const:898:8"
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
      "definition_site": "00c28258",
      "incomplete_value": false,
      "site": "00c2825c",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c27e30",
      "incomplete_value": false,
      "site": "00c27e34",
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
            "const:8a0:8"
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
      "00c2821c",
      "READ",
      [
        "storage",
        "00c9b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00c28228",
      "DATA",
      [
        "storage",
        "00c934c0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c28234",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2821c",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00c28228",
      "DATA",
      [
        "storage",
        "00c938c0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c28234",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c27e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27dd8.md#insn-00c27e34) · [`00c27e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27dd8.md#insn-00c27e50) · [`00c27df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27dd8.md#insn-00c27df4)
- 新版 [`00c2825c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28200.md#insn-00c2825c) · [`00c28278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28200.md#insn-00c28278) · [`00c2821c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28200.md#insn-00c2821c)

~~~diff
- 00c27e34 ["INT_ADD", "register:40f0:8", ["const:c27e34:8", "const:4:8"]]
- 00c27e34 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2825c ["INT_ADD", "register:40f0:8", ["const:c2825c:8", "const:4:8"]]
+ 00c2825c ["CALL", null, ["callee:00c57e50:8"]]
- 00c27e34 bytes 07bf0094
+ 00c2825c bytes fdbe0094
- 00c27e50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
- 00c27e50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c28278 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
+ 00c28278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c27e50 bytes 804e04f9
+ 00c28278 bytes 804e06f9
- 00c27df4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9e0:8"]]
- 00c27df4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2821c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 00c2821c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c27df4 bytes 08f144f9
+ 00c2821c bytes 08f146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74654a1b6c3ba1cef6d64289275457d4"></a>

### [`00c2ba44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2ba44.md) → [`00c2be6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be6c.md) _ZNSt6__ndk18numpunctIcEC2Em

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e400.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e800.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2be90",
      "incomplete_value": true,
      "site": "00c2be90",
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
      "definition_site": "00c2ba68",
      "incomplete_value": true,
      "site": "00c2ba68",
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
      "00c2be78",
      "READ",
      [
        "storage",
        "00c9b9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2be90",
      "DATA",
      [
        "storage",
        "00c93520",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2be78",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2be90",
      "DATA",
      [
        "storage",
        "00c93920",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2ba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2ba44.md#insn-00c2ba50)
- 新版 [`00c2be78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be6c.md#insn-00c2be78)

~~~diff
- 00c2ba50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9e8:8"]]
- 00c2ba50 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2be78 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:de8:8"]]
+ 00c2be78 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2ba50 bytes 29f544f9
+ 00c2be78 bytes 29f546f9
~~~


<a id="compare-1fedfef280a2977726d75dd3b7fd22a3"></a>

### [`00c2ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2ba70.md) → [`00c2be98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be98.md) _ZNSt6__ndk18numpunctIwEC1Em

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e410.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e810.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 58.33% / 新版 58.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2beac",
      "incomplete_value": true,
      "site": "00c2bebc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2ba84",
      "incomplete_value": true,
      "site": "00c2ba94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2a8:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00c2bec0",
      "incomplete_value": true,
      "site": "00c2bec0",
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
      "definition_site": "00c2ba98",
      "incomplete_value": true,
      "site": "00c2ba98",
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
      "00c2bea8",
      "READ",
      [
        "storage",
        "00c9b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2beac",
      "READ",
      [
        "storage",
        "002c42a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2bec0",
      "DATA",
      [
        "storage",
        "00c93570",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2bea8",
      "READ",
      [
        "storage",
        "00c9bdf0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2beac",
      "READ",
      [
        "storage",
        "002c42e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2bec0",
      "DATA",
      [
        "storage",
        "00c93970",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2ba80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2ba70.md#insn-00c2ba80) · [`00c2ba84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2ba70.md#insn-00c2ba84)
- 新版 [`00c2bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be98.md#insn-00c2bea8) · [`00c2beac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be98.md#insn-00c2beac)

~~~diff
- 00c2ba80 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9f0:8"]]
- 00c2ba80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2bea8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:df0:8"]]
+ 00c2bea8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2ba80 bytes 29f944f9
+ 00c2bea8 bytes 29f946f9
- 00c2ba84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a8:8"]]
- 00c2ba84 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2ba84 ["COPY", "register:5008:8", ["const:0:8"]]
- 00c2ba84 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2beac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
+ 00c2beac ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2beac ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c2beac ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2ba84 bytes 005541fd
+ 00c2beac bytes 007541fd
~~~


<a id="compare-cc80c995aa2e083e6d698a452df8ca09"></a>

### [`00c2bc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bc48.md) → [`00c2c070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c070.md) _ZNKSt6__ndk18numpunctIwE11do_truenameEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c080",
      "incomplete_value": true,
      "site": "00c2c08c",
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
                "const:310000:8"
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
      "definition_site": "00c2bc58",
      "incomplete_value": true,
      "site": "00c2bc64",
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
                "const:310000:8"
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
      "00c2c080",
      "READ",
      [
        "storage",
        "003106f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2c080",
      "READ",
      [
        "storage",
        "00310738",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2bc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bc48.md#insn-00c2bc50)
- 新版 [`00c2c078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c070.md#insn-00c2c078)

~~~diff
- 00c2bc50 ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00c2bc50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c2bc50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c2bc50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c2c078 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 00c2c078 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c2c078 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c2c078 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c2bc50 bytes 4ae11b91
+ 00c2c078 bytes 4ae11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1d47bc9b261e897f2041fb468a9508b"></a>

### [`00c2bd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bd4c.md) → [`00c2c174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c174.md) _ZNKSt6__ndk18numpunctIwE12do_falsenameEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c19c",
      "incomplete_value": true,
      "site": "00c2c1b0",
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
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2bd74",
      "incomplete_value": true,
      "site": "00c2bd88",
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
                "const:4f0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c1a8",
      "incomplete_value": true,
      "site": "00c2c1b4",
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
                "const:310000:8"
              ],
              [
                "leaf",
                "const:7b4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2bd80",
      "incomplete_value": true,
      "site": "00c2bd8c",
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
                "const:310000:8"
              ],
              [
                "leaf",
                "const:774:8"
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
      "00c2c19c",
      "READ",
      [
        "storage",
        "002c24f0",
        null,
        null
      ]
    ],
    [
      "00c2c1a8",
      "READ",
      [
        "storage",
        "00310774",
        null,
        "unicode32"
      ]
    ]
  ],
  "added": [
    [
      "00c2c19c",
      "READ",
      [
        "storage",
        "002c2530",
        null,
        null
      ]
    ],
    [
      "00c2c1a8",
      "READ",
      [
        "storage",
        "003107b4",
        null,
        "unicode32"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2bd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bd4c.md#insn-00c2bd64) · [`00c2bd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bd4c.md#insn-00c2bd74) · [`00c2bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bd4c.md#insn-00c2bd78)
- 新版 [`00c2c18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c174.md#insn-00c2c18c) · [`00c2c19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c174.md#insn-00c2c19c)

~~~diff
- 00c2bd64 ["INT_ADD", "register:40f0:8", ["const:c2bd64:8", "const:4:8"]]
- 00c2bd64 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c2c18c ["INT_ADD", "register:40f0:8", ["const:c2c18c:8", "const:4:8"]]
+ 00c2c18c ["CALL", null, ["callee:00c57e90:8"]]
- 00c2bd64 bytes 4baf0094
+ 00c2c18c bytes 41af0094
- 00c2bd74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4f0:8"]]
- 00c2bd74 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2bd74 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2bd74 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c2c19c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
+ 00c2c19c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c19c ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2c19c ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2bd74 bytes 003dc13d
+ 00c2c19c bytes 004dc13d
- 00c2bd78 ["COPY", "register:4040:8", ["const:310000:8"]]
- 00c2bd78 bytes 28b7ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eef9e7e09b38f9afffc913a51a4d34b"></a>

### [`00c2bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bda0.md) → [`00c2c1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c1c8.md) _ZNSt6__ndk115numpunct_bynameIcEC1EPKcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e850.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ec50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c1fc",
      "incomplete_value": true,
      "site": "00c2c1fc",
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
      "definition_site": "00c2bdd4",
      "incomplete_value": true,
      "site": "00c2bdd4",
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
      "00c2c1f0",
      "READ",
      [
        "storage",
        "00c9b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c1fc",
      "DATA",
      [
        "storage",
        "00c935c0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2c1f0",
      "READ",
      [
        "storage",
        "00c9bdf8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c1fc",
      "DATA",
      [
        "storage",
        "00c939c0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2bdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bda0.md#insn-00c2bdc8) · [`00c2bdd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bda0.md#insn-00c2bdd8)
- 新版 [`00c2c1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c1c8.md#insn-00c2c1f0) · [`00c2c200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c1c8.md#insn-00c2c200)

~~~diff
- 00c2bdc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9f8:8"]]
- 00c2bdc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c1f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
+ 00c2c1f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2bdc8 bytes 08fd44f9
+ 00c2c1f0 bytes 08fd46f9
- 00c2bdd8 ["INT_ADD", "register:40f0:8", ["const:c2bdd8:8", "const:4:8"]]
- 00c2bdd8 ["CALL", null, ["callee:00c5ec50:8"]]
+ 00c2c200 ["INT_ADD", "register:40f0:8", ["const:c2c200:8", "const:4:8"]]
+ 00c2c200 ["CALL", null, ["callee:00c5ec50:8"]]
- 00c2bdd8 bytes 9eca0094
+ 00c2c200 bytes 94ca0094
~~~


<a id="compare-2afc116e84777914aad4ce3192819cf7"></a>

### [`00c2be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2be00.md) → [`00c2c228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c228.md) _ZNSt6__ndk115numpunct_bynameIcE6__initEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e850.md) · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00bf1b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md) [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`00c5ec50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec50.md) · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2c454",
      "incomplete_value": false,
      "site": "00c2c464",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c02c",
      "incomplete_value": false,
      "site": "00c2c03c",
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
            "const:873:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2c250",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ],
    [
      "00c2c454",
      "PARAM",
      [
        "storage",
        "002a9873",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2c250",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ],
    [
      "00c2c454",
      "PARAM",
      [
        "storage",
        "002a9940",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2be00.md#insn-00c2c03c) · [`00c2be28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2be00.md#insn-00c2be28) · [`00c2be30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2be00.md#insn-00c2be30)
- 新版 [`00c2c464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c228.md#insn-00c2c464) · [`00c2c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c228.md#insn-00c2c250) · [`00c2c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c228.md#insn-00c2c258)

~~~diff
- 00c2c03c ["INT_ADD", "register:40f0:8", ["const:c2c03c:8", "const:4:8"]]
- 00c2c03c ["CALL", null, ["callee:00c25934:8"]]
+ 00c2c464 ["INT_ADD", "register:40f0:8", ["const:c2c464:8", "const:4:8"]]
+ 00c2c464 ["CALL", null, ["callee:00c25934:8"]]
- 00c2c03c bytes 34e5ff97
+ 00c2c464 bytes 34e5ff97
- 00c2be28 ["COPY", "tmp:0:8", ["const:13c:8"]]
- 00c2be28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c2be28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c2be28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c2c250 ["COPY", "tmp:0:8", ["const:17c:8"]]
+ 00c2c250 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c2c250 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c2c250 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c2be28 bytes 21f00491
+ 00c2c250 bytes 21f00591
- 00c2be30 ["INT_ADD", "register:40f0:8", ["const:c2be30:8", "const:4:8"]]
- 00c2be30 ["CALL", null, ["callee:00c5b850:8"]]
+ 00c2c258 ["INT_ADD", "register:40f0:8", ["const:c2c258:8", "const:4:8"]]
+ 00c2c258 ["CALL", null, ["callee:00c5b850:8"]]
- 00c2be30 bytes 88bd0094
+ 00c2c258 bytes 7ebd0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-607eab3186126c7a0dcc54a92f5238de"></a>

### [`00c2c0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c0d4.md) → [`00c2c4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c4fc.md) _ZNSt6__ndk115numpunct_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e470.md) · 呼出先 1件 [`00c5e850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e850.md)
- 新版 呼出元 1件 [`00c5e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e870.md) · 呼出先 1件 [`00c5ec50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec50.md)

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
      "definition_site": "00c2c530",
      "incomplete_value": true,
      "site": "00c2c530",
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
      "definition_site": "00c2c108",
      "incomplete_value": true,
      "site": "00c2c108",
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
      "00c2c524",
      "READ",
      [
        "storage",
        "00c9b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c530",
      "DATA",
      [
        "storage",
        "00c935c0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2c524",
      "READ",
      [
        "storage",
        "00c9bdf8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c530",
      "DATA",
      [
        "storage",
        "00c939c0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c0d4.md#insn-00c2c0fc) · [`00c2c11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c0d4.md#insn-00c2c11c)
- 新版 [`00c2c524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c4fc.md#insn-00c2c524) · [`00c2c544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c4fc.md#insn-00c2c544)

~~~diff
- 00c2c0fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9f8:8"]]
- 00c2c0fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c524 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
+ 00c2c524 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c0fc bytes 08fd44f9
+ 00c2c524 bytes 08fd46f9
- 00c2c11c ["INT_ADD", "register:40f0:8", ["const:c2c11c:8", "const:4:8"]]
- 00c2c11c ["CALL", null, ["callee:00c5ec50:8"]]
+ 00c2c544 ["INT_ADD", "register:40f0:8", ["const:c2c544:8", "const:4:8"]]
+ 00c2c544 ["CALL", null, ["callee:00c5ec50:8"]]
- 00c2c11c bytes cdc90094
+ 00c2c544 bytes c3c90094
~~~


<a id="compare-2483ca8ab62b357b1dff4c60bda39627"></a>

### [`00c2c198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c198.md) → [`00c2c5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c5c0.md) _ZNSt6__ndk115numpunct_bynameIwEC1EPKcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e880.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c5dc",
      "incomplete_value": true,
      "site": "00c2c5f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c1b4",
      "incomplete_value": true,
      "site": "00c2c1c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2a8:8"
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
      "definition_site": "00c2c5f8",
      "incomplete_value": true,
      "site": "00c2c5f8",
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
      "definition_site": "00c2c1d0",
      "incomplete_value": true,
      "site": "00c2c1d0",
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
      "00c2c5dc",
      "READ",
      [
        "storage",
        "002c42a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2c5e8",
      "READ",
      [
        "storage",
        "00c9ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c5f8",
      "DATA",
      [
        "storage",
        "00c93610",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2c5dc",
      "READ",
      [
        "storage",
        "002c42e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2c5e8",
      "READ",
      [
        "storage",
        "00c9be00",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c5f8",
      "DATA",
      [
        "storage",
        "00c93a10",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c198.md#insn-00c2c1b4) · [`00c2c1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c198.md#insn-00c2c1c0) · [`00c2c1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c198.md#insn-00c2c1d4)
- 新版 [`00c2c5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c5c0.md#insn-00c2c5dc) · [`00c2c5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c5c0.md#insn-00c2c5e8) · [`00c2c5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c5c0.md#insn-00c2c5fc)

~~~diff
- 00c2c1b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a8:8"]]
- 00c2c1b4 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c1b4 ["COPY", "register:5008:8", ["const:0:8"]]
- 00c2c1b4 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2c5dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
+ 00c2c5dc ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c5dc ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c2c5dc ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2c1b4 bytes 005541fd
+ 00c2c5dc bytes 007541fd
- 00c2c1c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a00:8"]]
- 00c2c1c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c5e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e00:8"]]
+ 00c2c5e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c1c0 bytes 080145f9
+ 00c2c5e8 bytes 080147f9
- 00c2c1d4 ["INT_ADD", "register:40f0:8", ["const:c2c1d4:8", "const:4:8"]]
- 00c2c1d4 ["CALL", null, ["callee:00c5ec80:8"]]
+ 00c2c5fc ["INT_ADD", "register:40f0:8", ["const:c2c5fc:8", "const:4:8"]]
+ 00c2c5fc ["CALL", null, ["callee:00c5ec80:8"]]
- 00c2c1d4 bytes abc90094
+ 00c2c5fc bytes a1c90094
~~~


<a id="compare-50ca7b1546191780e561230b78250d3b"></a>

### [`00c2c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c1fc.md) → [`00c2c624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md) _ZNSt6__ndk115numpunct_bynameIwE6__initEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e880.md) · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00bf1b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md) [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md) [`00c2c170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c170.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`00c5ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec80.md) · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c2c598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c598.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2c64c",
      "incomplete_value": false,
      "site": "00c2c654",
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
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c224",
      "incomplete_value": false,
      "site": "00c2c22c",
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
            "const:13c:8"
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
      "definition_site": "00c2c798",
      "incomplete_value": false,
      "site": "00c2c7a8",
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
            "const:7b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c370",
      "incomplete_value": false,
      "site": "00c2c380",
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
            "const:776:8"
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
      "00c2c64c",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ],
    [
      "00c2c798",
      "PARAM",
      [
        "storage",
        "002b1776",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2c64c",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ],
    [
      "00c2c798",
      "PARAM",
      [
        "storage",
        "002b17b6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c1fc.md#insn-00c2c22c) · [`00c2c380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c1fc.md#insn-00c2c380) · [`00c2c224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c1fc.md#insn-00c2c224)
- 新版 [`00c2c654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md#insn-00c2c654) · [`00c2c7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md#insn-00c2c7a8) · [`00c2c64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md#insn-00c2c64c)

~~~diff
- 00c2c22c ["INT_ADD", "register:40f0:8", ["const:c2c22c:8", "const:4:8"]]
- 00c2c22c ["CALL", null, ["callee:00c5b850:8"]]
+ 00c2c654 ["INT_ADD", "register:40f0:8", ["const:c2c654:8", "const:4:8"]]
+ 00c2c654 ["CALL", null, ["callee:00c5b850:8"]]
- 00c2c22c bytes 89bc0094
+ 00c2c654 bytes 7fbc0094
- 00c2c380 ["INT_ADD", "register:40f0:8", ["const:c2c380:8", "const:4:8"]]
- 00c2c380 ["CALL", null, ["callee:00c25934:8"]]
+ 00c2c7a8 ["INT_ADD", "register:40f0:8", ["const:c2c7a8:8", "const:4:8"]]
+ 00c2c7a8 ["CALL", null, ["callee:00c25934:8"]]
- 00c2c380 bytes 63e4ff97
+ 00c2c7a8 bytes 63e4ff97
- 00c2c224 ["COPY", "tmp:0:8", ["const:13c:8"]]
- 00c2c224 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c2c224 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c2c224 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c2c64c ["COPY", "tmp:0:8", ["const:17c:8"]]
+ 00c2c64c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c2c64c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c2c64c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c2c224 bytes 21f00491
+ 00c2c64c bytes 21f00591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff6b377d4afc7c3d9383de89e0f12540"></a>

### [`00c2c408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c408.md) → [`00c2c830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c830.md) _ZNSt6__ndk115numpunct_bynameIwEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e480.md) · 呼出先 1件 [`00c5e880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e880.md)
- 新版 呼出元 1件 [`00c5e880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e880.md) · 呼出先 1件 [`00c5ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2c84c",
      "incomplete_value": true,
      "site": "00c2c860",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c424",
      "incomplete_value": true,
      "site": "00c2c438",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2a8:8"
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
      "definition_site": "00c2c868",
      "incomplete_value": true,
      "site": "00c2c868",
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
      "definition_site": "00c2c440",
      "incomplete_value": true,
      "site": "00c2c440",
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
      "00c2c84c",
      "READ",
      [
        "storage",
        "002c42a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2c858",
      "READ",
      [
        "storage",
        "00c9ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c868",
      "DATA",
      [
        "storage",
        "00c93610",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2c84c",
      "READ",
      [
        "storage",
        "002c42e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2c858",
      "READ",
      [
        "storage",
        "00c9be00",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c868",
      "DATA",
      [
        "storage",
        "00c93a10",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c408.md#insn-00c2c424) · [`00c2c430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c408.md#insn-00c2c430) · [`00c2c454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c408.md#insn-00c2c454)
- 新版 [`00c2c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c830.md#insn-00c2c84c) · [`00c2c858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c830.md#insn-00c2c858) · [`00c2c87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c830.md#insn-00c2c87c)

~~~diff
- 00c2c424 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a8:8"]]
- 00c2c424 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c424 ["COPY", "register:5008:8", ["const:0:8"]]
- 00c2c424 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2c84c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e8:8"]]
+ 00c2c84c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c84c ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c2c84c ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2c424 bytes 005541fd
+ 00c2c84c bytes 007541fd
- 00c2c430 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a00:8"]]
- 00c2c430 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2c858 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e00:8"]]
+ 00c2c858 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c430 bytes 080145f9
+ 00c2c858 bytes 080147f9
- 00c2c454 ["INT_ADD", "register:40f0:8", ["const:c2c454:8", "const:4:8"]]
- 00c2c454 ["CALL", null, ["callee:00c5ec80:8"]]
+ 00c2c87c ["INT_ADD", "register:40f0:8", ["const:c2c87c:8", "const:4:8"]]
+ 00c2c87c ["CALL", null, ["callee:00c5ec80:8"]]
- 00c2c454 bytes 0bc90094
+ 00c2c87c bytes 01c90094
~~~


<a id="compare-c6800c6e800e158b69ea51d0dc77100f"></a>

### [`00c2c648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c648.md) → [`00c2ca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2ca70.md) _ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2c6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c6b4.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2cacc",
      "incomplete_value": false,
      "site": "00c2cacc",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c6a4",
      "incomplete_value": false,
      "site": "00c2c6a4",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2cabc",
      "incomplete_value": false,
      "site": "00c2cacc",
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
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c694",
      "incomplete_value": false,
      "site": "00c2c6a4",
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
            "const:ba8:8"
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
      "definition_site": "00c2caa4",
      "incomplete_value": false,
      "site": "00c2caa8",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c67c",
      "incomplete_value": false,
      "site": "00c2c680",
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
            "const:ab0:8"
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
      "00c2ca84",
      "READ",
      [
        "storage",
        "01127ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2ca90",
      "READ",
      [
        "storage",
        "01127aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2ca90",
      "DATA",
      [
        "storage",
        "01127ba8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2ca84",
      "READ",
      [
        "storage",
        "01127eb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2ca90",
      "READ",
      [
        "storage",
        "01127ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2ca90",
      "DATA",
      [
        "storage",
        "01127fa8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c648.md#insn-00c2c680) · [`00c2c6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c648.md#insn-00c2c6a4) · [`00c2c6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c648.md#insn-00c2c6a8)
- 新版 [`00c2caa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2ca70.md#insn-00c2caa8) · [`00c2cacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2ca70.md#insn-00c2cacc) · [`00c2cad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2ca70.md#insn-00c2cad0)

~~~diff
- 00c2c680 ["INT_ADD", "register:40f0:8", ["const:c2c680:8", "const:4:8"]]
- 00c2c680 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2caa8 ["INT_ADD", "register:40f0:8", ["const:c2caa8:8", "const:4:8"]]
+ 00c2caa8 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2c680 bytes f4ac0094
+ 00c2caa8 bytes eaac0094
- 00c2c6a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
- 00c2c6a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2cacc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
+ 00c2cacc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2c6a4 bytes 095505f9
+ 00c2cacc bytes 095507f9
- 00c2c6a8 ["INT_ADD", "register:40f0:8", ["const:c2c6a8:8", "const:4:8"]]
- 00c2c6a8 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c2cad0 ["INT_ADD", "register:40f0:8", ["const:c2cad0:8", "const:4:8"]]
+ 00c2cad0 ["CALL", null, ["callee:00c57e70:8"]]
- 00c2c6a8 bytes f2ac0094
+ 00c2cad0 bytes e8ac0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53d30ff1d8e6869f55ec869c5f048a3c"></a>

### [`00c2c6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c6b4.md) → [`00c2cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md) FUN_00c2cadc

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2c648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c648.md) · 呼出先 4件 [`00c35778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35778.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c2ca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2ca70.md) · 呼出先 4件 [`00c35ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ba0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 71.48% / 新版 71.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 21件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2cb10",
      "incomplete_value": false,
      "site": "00c2cb10",
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
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c6e8",
      "incomplete_value": false,
      "site": "00c2c6e8",
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
            "const:ba8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2cb28",
      "incomplete_value": false,
      "site": "00c2cb28",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c700",
      "incomplete_value": false,
      "site": "00c2c700",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2cb5c",
      "incomplete_value": false,
      "site": "00c2cb5c",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c734",
      "incomplete_value": false,
      "site": "00c2c734",
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
            "const:bc0:8"
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
      "00c2caf0",
      "READ",
      [
        "storage",
        "01127cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cafc",
      "READ",
      [
        "storage",
        "01127ba8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cb10",
      "WRITE",
      [
        "storage",
        "01127ba8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2caf0",
      "READ",
      [
        "storage",
        "011280f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cafc",
      "READ",
      [
        "storage",
        "01127fa8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cb10",
      "WRITE",
      [
        "storage",
        "01127fa8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2cabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c6b4.md#insn-00c2cabc) · [`00c2cad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c6b4.md#insn-00c2cad8) · [`00c2cae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c6b4.md#insn-00c2cae4)
- 新版 [`00c2cee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md#insn-00c2cee4) · [`00c2cf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md#insn-00c2cf00) · [`00c2cf0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md#insn-00c2cf0c)

~~~diff
- 00c2cabc ["INT_ADD", "register:40f0:8", ["const:c2cabc:8", "const:4:8"]]
- 00c2cabc ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2cee4 ["INT_ADD", "register:40f0:8", ["const:c2cee4:8", "const:4:8"]]
+ 00c2cee4 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2cabc bytes e5ab0094
+ 00c2cee4 bytes dbab0094
- 00c2cad8 ["INT_ADD", "register:40f0:8", ["const:c2cad8:8", "const:4:8"]]
- 00c2cad8 ["CALL", null, ["callee:00c57e30:8"]]
+ 00c2cf00 ["INT_ADD", "register:40f0:8", ["const:c2cf00:8", "const:4:8"]]
+ 00c2cf00 ["CALL", null, ["callee:00c57e30:8"]]
- 00c2cad8 bytes d6ab0094
+ 00c2cf00 bytes ccab0094
- 00c2cae4 ["INT_ADD", "register:40f0:8", ["const:c2cae4:8", "const:4:8"]]
- 00c2cae4 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c2cf0c ["INT_ADD", "register:40f0:8", ["const:c2cf0c:8", "const:4:8"]]
+ 00c2cf0c ["CALL", null, ["callee:00c57e70:8"]]
- 00c2cae4 bytes e3ab0094
+ 00c2cf0c bytes d9ab0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f41b4eee6dd6e20a4c4e356eb40f806"></a>

### [`00c2caec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2caec.md) → [`00c2cf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf14.md) _ZNKSt6__ndk120__time_get_c_storageIwE7__weeksEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2cb6c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2cf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf94.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2cf70",
      "incomplete_value": true,
      "site": "00c2cf70",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cb48",
      "incomplete_value": true,
      "site": "00c2cb48",
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
            "const:ab8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2cf64",
      "incomplete_value": false,
      "site": "00c2cf70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cb3c",
      "incomplete_value": false,
      "site": "00c2cb48",
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
            "const:d00:8"
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
      "definition_site": "00c2cf50",
      "incomplete_value": false,
      "site": "00c2cf54",
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
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cb28",
      "incomplete_value": false,
      "site": "00c2cb2c",
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
            "const:ac0:8"
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
      "00c2cf30",
      "READ",
      [
        "storage",
        "01127ac0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cf38",
      "READ",
      [
        "storage",
        "01127ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2cf38",
      "DATA",
      [
        "storage",
        "01127d00",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2cf30",
      "READ",
      [
        "storage",
        "01127ec0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2cf38",
      "READ",
      [
        "storage",
        "01127eb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2cf38",
      "DATA",
      [
        "storage",
        "01128100",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2cb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2caec.md#insn-00c2cb2c) · [`00c2cb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2caec.md#insn-00c2cb34) · [`00c2cb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2caec.md#insn-00c2cb48)
- 新版 [`00c2cf54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf14.md#insn-00c2cf54) · [`00c2cf5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf14.md#insn-00c2cf5c) · [`00c2cf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf14.md#insn-00c2cf70)

~~~diff
- 00c2cb2c ["INT_ADD", "register:40f0:8", ["const:c2cb2c:8", "const:4:8"]]
- 00c2cb2c ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2cf54 ["INT_ADD", "register:40f0:8", ["const:c2cf54:8", "const:4:8"]]
+ 00c2cf54 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2cb2c bytes c9ab0094
+ 00c2cf54 bytes bfab0094
- 00c2cb34 ["INT_ADD", "register:40f0:8", ["const:c2cb34:8", "const:4:8"]]
- 00c2cb34 ["CALL", null, ["ram:c2cb6c:8"]]
+ 00c2cf5c ["INT_ADD", "register:40f0:8", ["const:c2cf5c:8", "const:4:8"]]
+ 00c2cf5c ["CALL", null, ["ram:c2cf94:8"]]
- 00c2cb34 bytes 0e000094
+ 00c2cf5c bytes 0e000094
- 00c2cb48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
- 00c2cb48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c2cf70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb8:8"]]
+ 00c2cf70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00c2cb48 bytes 685e05f9
+ 00c2cf70 bytes 685e07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbf1c5c52b4a054596b5551c5c0f4f1b"></a>

### [`00c2ce40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ce40.md) → [`00c2d268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d268.md) _ZNKSt6__ndk120__time_get_c_storageIcE8__monthsEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2ceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ceac.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2d2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d2d4.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2d2c4",
      "incomplete_value": false,
      "site": "00c2d2c4",
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
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2ce9c",
      "incomplete_value": false,
      "site": "00c2ce9c",
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
            "const:ac8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2d2b4",
      "incomplete_value": false,
      "site": "00c2d2c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2ce8c",
      "incomplete_value": false,
      "site": "00c2ce9c",
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
            "const:e58:8"
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
      "definition_site": "00c2d29c",
      "incomplete_value": false,
      "site": "00c2d2a0",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2ce74",
      "incomplete_value": false,
      "site": "00c2ce78",
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
            "const:ad0:8"
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
      "00c2d27c",
      "READ",
      [
        "storage",
        "01127ad0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d288",
      "READ",
      [
        "storage",
        "01127ac8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2d288",
      "DATA",
      [
        "storage",
        "01127e58",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2d27c",
      "READ",
      [
        "storage",
        "01127ed0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d288",
      "READ",
      [
        "storage",
        "01127ec8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2d288",
      "DATA",
      [
        "storage",
        "01128258",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ce40.md#insn-00c2ce78) · [`00c2ce9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ce40.md#insn-00c2ce9c) · [`00c2cea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ce40.md#insn-00c2cea0)
- 新版 [`00c2d2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d268.md#insn-00c2d2a0) · [`00c2d2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d268.md#insn-00c2d2c4) · [`00c2d2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d268.md#insn-00c2d2c8)

~~~diff
- 00c2ce78 ["INT_ADD", "register:40f0:8", ["const:c2ce78:8", "const:4:8"]]
- 00c2ce78 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2d2a0 ["INT_ADD", "register:40f0:8", ["const:c2d2a0:8", "const:4:8"]]
+ 00c2d2a0 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2ce78 bytes f6aa0094
+ 00c2d2a0 bytes ecaa0094
- 00c2ce9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ac8:8"]]
- 00c2ce9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2d2c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec8:8"]]
+ 00c2d2c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2ce9c bytes 096505f9
+ 00c2d2c4 bytes 096507f9
- 00c2cea0 ["INT_ADD", "register:40f0:8", ["const:c2cea0:8", "const:4:8"]]
- 00c2cea0 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c2d2c8 ["INT_ADD", "register:40f0:8", ["const:c2d2c8:8", "const:4:8"]]
+ 00c2d2c8 ["CALL", null, ["callee:00c57e70:8"]]
- 00c2cea0 bytes f4aa0094
+ 00c2d2c8 bytes eaaa0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5161d174d67eba0f76f7f1fdccd4bd2a"></a>

### [`00c2ceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ceac.md) → [`00c2d2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d2d4.md) FUN_00c2d2d4

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2ce40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ce40.md) · 呼出先 4件 [`00c35a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35a58.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c2d268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d268.md) · 呼出先 4件 [`00c35e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35e80.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 70.48% / 新版 70.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 45件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2d308",
      "incomplete_value": false,
      "site": "00c2d308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cee0",
      "incomplete_value": false,
      "site": "00c2cee0",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2d320",
      "incomplete_value": false,
      "site": "00c2d320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cef8",
      "incomplete_value": false,
      "site": "00c2cef8",
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
            "const:e60:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2d358",
      "incomplete_value": false,
      "site": "00c2d358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cf30",
      "incomplete_value": false,
      "site": "00c2cf30",
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
            "const:e70:8"
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
      "00c2d2e8",
      "READ",
      [
        "storage",
        "01128098",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d2f4",
      "READ",
      [
        "storage",
        "01127e58",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d308",
      "WRITE",
      [
        "storage",
        "01127e58",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2d2e8",
      "READ",
      [
        "storage",
        "01128498",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d2f4",
      "READ",
      [
        "storage",
        "01128258",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d308",
      "WRITE",
      [
        "storage",
        "01128258",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2ceec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ceac.md#insn-00c2ceec) · [`00c2d308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ceac.md#insn-00c2d308) · [`00c2d320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2ceac.md#insn-00c2d320)
- 新版 [`00c2d314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d2d4.md#insn-00c2d314) · [`00c2d730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d2d4.md#insn-00c2d730) · [`00c2d748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d2d4.md#insn-00c2d748)

~~~diff
- 00c2ceec ["COPY", "tmp:0:8", ["const:e60:8"]]
- 00c2ceec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c2ceec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c2ceec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c2d314 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 00c2d314 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c2d314 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c2d314 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c2ceec bytes 29813991
+ 00c2d314 bytes 29810991
- 00c2d308 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00c2d730 ["COPY", "register:4040:8", ["const:1128000:8"]]
- 00c2d308 bytes c82700d0
+ 00c2d730 bytes c82700f0
- 00c2d320 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 00c2d320 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c2d320 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c2d320 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c2d748 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 00c2d748 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c2d748 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c2d748 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c2d320 bytes 29213f91
+ 00c2d748 bytes 29210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8132ecec520003a3899c251e5c70c467"></a>

### [`00c2d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2d580.md) → [`00c2d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d9a8.md) _ZNKSt6__ndk120__time_get_c_storageIwE8__monthsEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2d600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2d600.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2da28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2da28.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2da04",
      "incomplete_value": true,
      "site": "00c2da04",
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
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d5dc",
      "incomplete_value": true,
      "site": "00c2d5dc",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2d9f8",
      "incomplete_value": false,
      "site": "00c2da04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d5d0",
      "incomplete_value": false,
      "site": "00c2d5dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "definition_site": "00c2d9e4",
      "incomplete_value": true,
      "site": "00c2d9e8",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d5bc",
      "incomplete_value": true,
      "site": "00c2d5c0",
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
            "const:ae0:8"
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
      "00c2d9c4",
      "READ",
      [
        "storage",
        "01127ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d9cc",
      "READ",
      [
        "storage",
        "01127ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2d9cc",
      "DATA",
      [
        "storage",
        "011280a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2d9c4",
      "READ",
      [
        "storage",
        "01127ee0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2d9cc",
      "READ",
      [
        "storage",
        "01127ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2d9cc",
      "DATA",
      [
        "storage",
        "011284a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2d5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2d580.md#insn-00c2d5c0) · [`00c2d5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2d580.md#insn-00c2d5c8) · [`00c2d5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2d580.md#insn-00c2d5dc)
- 新版 [`00c2d9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d9a8.md#insn-00c2d9e8) · [`00c2d9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d9a8.md#insn-00c2d9f0) · [`00c2da04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2d9a8.md#insn-00c2da04)

~~~diff
- 00c2d5c0 ["INT_ADD", "register:40f0:8", ["const:c2d5c0:8", "const:4:8"]]
- 00c2d5c0 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2d9e8 ["INT_ADD", "register:40f0:8", ["const:c2d9e8:8", "const:4:8"]]
+ 00c2d9e8 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2d5c0 bytes 24a90094
+ 00c2d9e8 bytes 1aa90094
- 00c2d5c8 ["INT_ADD", "register:40f0:8", ["const:c2d5c8:8", "const:4:8"]]
- 00c2d5c8 ["CALL", null, ["ram:c2d600:8"]]
+ 00c2d9f0 ["INT_ADD", "register:40f0:8", ["const:c2d9f0:8", "const:4:8"]]
+ 00c2d9f0 ["CALL", null, ["ram:c2da28:8"]]
- 00c2d5c8 bytes 0e000094
+ 00c2d9f0 bytes 0e000094
- 00c2d5dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad8:8"]]
- 00c2d5dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c2da04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ed8:8"]]
+ 00c2da04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00c2d5dc bytes 686e05f9
+ 00c2da04 bytes 686e07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ae1f007ca8205243f19a2a83050ca49"></a>

### [`00c2db28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db28.md) → [`00c2df50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md) _ZNKSt6__ndk120__time_get_c_storageIcE7__am_pmEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2db94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db94.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2dfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2dfbc.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2dfac",
      "incomplete_value": true,
      "site": "00c2dfac",
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
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2db84",
      "incomplete_value": true,
      "site": "00c2db84",
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
            "const:ae8:8"
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
      "definition_site": "00c2df84",
      "incomplete_value": false,
      "site": "00c2df88",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2db5c",
      "incomplete_value": false,
      "site": "00c2db60",
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
            "const:af0:8"
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
      "definition_site": "00c2dfa8",
      "incomplete_value": true,
      "site": "00c2dfb0",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2db80",
      "incomplete_value": true,
      "site": "00c2db88",
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
            "const:af0:8"
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
      "00c2df64",
      "READ",
      [
        "storage",
        "01127af0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2df70",
      "READ",
      [
        "storage",
        "01127ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2df70",
      "DATA",
      [
        "storage",
        "011282e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2df64",
      "READ",
      [
        "storage",
        "01127ef0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2df70",
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2df70",
      "DATA",
      [
        "storage",
        "011286e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db28.md#insn-00c2db60) · [`00c2db84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db28.md#insn-00c2db84) · [`00c2db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db28.md#insn-00c2db88)
- 新版 [`00c2df88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md#insn-00c2df88) · [`00c2dfac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md#insn-00c2dfac) · [`00c2dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md#insn-00c2dfb0)

~~~diff
- 00c2db60 ["INT_ADD", "register:40f0:8", ["const:c2db60:8", "const:4:8"]]
- 00c2db60 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2df88 ["INT_ADD", "register:40f0:8", ["const:c2df88:8", "const:4:8"]]
+ 00c2df88 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2db60 bytes bca70094
+ 00c2df88 bytes b2a70094
- 00c2db84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ae8:8"]]
- 00c2db84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2dfac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee8:8"]]
+ 00c2dfac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2db84 bytes 097505f9
+ 00c2dfac bytes 097507f9
- 00c2db88 ["INT_ADD", "register:40f0:8", ["const:c2db88:8", "const:4:8"]]
- 00c2db88 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c2dfb0 ["INT_ADD", "register:40f0:8", ["const:c2dfb0:8", "const:4:8"]]
+ 00c2dfb0 ["CALL", null, ["callee:00c57e70:8"]]
- 00c2db88 bytes baa70094
+ 00c2dfb0 bytes b0a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d802cb79864bad7ad09868c8e59da00"></a>

### [`00c2db94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db94.md) → [`00c2dfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2dfbc.md) FUN_00c2dfbc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2db28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db28.md) · 呼出先 4件 [`00c35af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35af8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c2df50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md) · 呼出先 4件 [`00c35f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35f20.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2dff0",
      "incomplete_value": false,
      "site": "00c2dff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dbc8",
      "incomplete_value": false,
      "site": "00c2dbc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e008",
      "incomplete_value": false,
      "site": "00c2e008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dbe0",
      "incomplete_value": false,
      "site": "00c2dbe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e030",
      "incomplete_value": false,
      "site": "00c2e030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dc08",
      "incomplete_value": false,
      "site": "00c2dc08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:300:8"
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
      "00c2dfd0",
      "READ",
      [
        "storage",
        "01128318",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2dfdc",
      "READ",
      [
        "storage",
        "011282e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2dff0",
      "WRITE",
      [
        "storage",
        "011282e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2dfd0",
      "READ",
      [
        "storage",
        "01128718",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2dfdc",
      "READ",
      [
        "storage",
        "011286e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2dff0",
      "WRITE",
      [
        "storage",
        "011286e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2dc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db94.md#insn-00c2dc44) · [`00c2dc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db94.md#insn-00c2dc60) · [`00c2dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db94.md#insn-00c2dc6c)
- 新版 [`00c2e06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2dfbc.md#insn-00c2e06c) · [`00c2e088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2dfbc.md#insn-00c2e088) · [`00c2e094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2dfbc.md#insn-00c2e094)

~~~diff
- 00c2dc44 ["INT_ADD", "register:40f0:8", ["const:c2dc44:8", "const:4:8"]]
- 00c2dc44 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2e06c ["INT_ADD", "register:40f0:8", ["const:c2e06c:8", "const:4:8"]]
+ 00c2e06c ["CALL", null, ["callee:00c57e50:8"]]
- 00c2dc44 bytes 83a70094
+ 00c2e06c bytes 79a70094
- 00c2dc60 ["INT_ADD", "register:40f0:8", ["const:c2dc60:8", "const:4:8"]]
- 00c2dc60 ["CALL", null, ["callee:00c57e30:8"]]
+ 00c2e088 ["INT_ADD", "register:40f0:8", ["const:c2e088:8", "const:4:8"]]
+ 00c2e088 ["CALL", null, ["callee:00c57e30:8"]]
- 00c2dc60 bytes 74a70094
+ 00c2e088 bytes 6aa70094
- 00c2dc6c ["INT_ADD", "register:40f0:8", ["const:c2dc6c:8", "const:4:8"]]
- 00c2dc6c ["CALL", null, ["callee:00c57e70:8"]]
+ 00c2e094 ["INT_ADD", "register:40f0:8", ["const:c2e094:8", "const:4:8"]]
+ 00c2e094 ["CALL", null, ["callee:00c57e70:8"]]
- 00c2dc6c bytes 81a70094
+ 00c2e094 bytes 77a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c6f4d0d3e93b2a48c1b2842b6f95c84"></a>

### [`00c2dc74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dc74.md) → [`00c2e09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e09c.md) _ZNKSt6__ndk120__time_get_c_storageIwE7__am_pmEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2dce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dce0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2e108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e108.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e0f8",
      "incomplete_value": false,
      "site": "00c2e0f8",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dcd0",
      "incomplete_value": false,
      "site": "00c2dcd0",
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
            "const:af8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2e0e8",
      "incomplete_value": false,
      "site": "00c2e0f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dcc0",
      "incomplete_value": false,
      "site": "00c2dcd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "definition_site": "00c2e0d0",
      "incomplete_value": false,
      "site": "00c2e0d4",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dca8",
      "incomplete_value": false,
      "site": "00c2dcac",
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
            "const:b00:8"
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
      "00c2e0b0",
      "READ",
      [
        "storage",
        "01127b00",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e0bc",
      "READ",
      [
        "storage",
        "01127af8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2e0bc",
      "DATA",
      [
        "storage",
        "01128320",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e0b0",
      "READ",
      [
        "storage",
        "01127f00",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e0bc",
      "READ",
      [
        "storage",
        "01127ef8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2e0bc",
      "DATA",
      [
        "storage",
        "01128720",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2dcac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dc74.md#insn-00c2dcac) · [`00c2dcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dc74.md#insn-00c2dcd0) · [`00c2dcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dc74.md#insn-00c2dcd4)
- 新版 [`00c2e0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e09c.md#insn-00c2e0d4) · [`00c2e0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e09c.md#insn-00c2e0f8) · [`00c2e0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e09c.md#insn-00c2e0fc)

~~~diff
- 00c2dcac ["INT_ADD", "register:40f0:8", ["const:c2dcac:8", "const:4:8"]]
- 00c2dcac ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2e0d4 ["INT_ADD", "register:40f0:8", ["const:c2e0d4:8", "const:4:8"]]
+ 00c2e0d4 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2dcac bytes 69a70094
+ 00c2e0d4 bytes 5fa70094
- 00c2dcd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:af8:8"]]
- 00c2dcd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2e0f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
+ 00c2e0f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2dcd0 bytes 097d05f9
+ 00c2e0f8 bytes 097d07f9
- 00c2dcd4 ["INT_ADD", "register:40f0:8", ["const:c2dcd4:8", "const:4:8"]]
- 00c2dcd4 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c2e0fc ["INT_ADD", "register:40f0:8", ["const:c2e0fc:8", "const:4:8"]]
+ 00c2e0fc ["CALL", null, ["callee:00c57e70:8"]]
- 00c2dcd4 bytes 67a70094
+ 00c2e0fc bytes 5da70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02c54872b31f4960ef539223a0b8ea23"></a>

### [`00c2dce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dce0.md) → [`00c2e108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e108.md) FUN_00c2e108

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2dc74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dc74.md) · 呼出先 4件 [`00c35b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b44.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c2e09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e09c.md) · 呼出先 4件 [`00c35f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35f6c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 71.93% / 新版 71.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e13c",
      "incomplete_value": true,
      "site": "00c2e13c",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dd14",
      "incomplete_value": true,
      "site": "00c2dd14",
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
            "const:320:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e154",
      "incomplete_value": false,
      "site": "00c2e154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dd2c",
      "incomplete_value": false,
      "site": "00c2dd2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e180",
      "incomplete_value": false,
      "site": "00c2e180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2dd58",
      "incomplete_value": false,
      "site": "00c2dd58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "00c2e11c",
      "READ",
      [
        "storage",
        "01128350",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e128",
      "READ",
      [
        "storage",
        "01128320",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e13c",
      "WRITE",
      [
        "storage",
        "01128320",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e11c",
      "READ",
      [
        "storage",
        "01128750",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e128",
      "READ",
      [
        "storage",
        "01128720",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e13c",
      "WRITE",
      [
        "storage",
        "01128720",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2dd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dce0.md#insn-00c2dd94) · [`00c2ddb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dce0.md#insn-00c2ddb0) · [`00c2ddbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dce0.md#insn-00c2ddbc)
- 新版 [`00c2e1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e108.md#insn-00c2e1bc) · [`00c2e1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e108.md#insn-00c2e1d8) · [`00c2e1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e108.md#insn-00c2e1e4)

~~~diff
- 00c2dd94 ["INT_ADD", "register:40f0:8", ["const:c2dd94:8", "const:4:8"]]
- 00c2dd94 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2e1bc ["INT_ADD", "register:40f0:8", ["const:c2e1bc:8", "const:4:8"]]
+ 00c2e1bc ["CALL", null, ["callee:00c57e50:8"]]
- 00c2dd94 bytes 2fa70094
+ 00c2e1bc bytes 25a70094
- 00c2ddb0 ["INT_ADD", "register:40f0:8", ["const:c2ddb0:8", "const:4:8"]]
- 00c2ddb0 ["CALL", null, ["callee:00c57e30:8"]]
+ 00c2e1d8 ["INT_ADD", "register:40f0:8", ["const:c2e1d8:8", "const:4:8"]]
+ 00c2e1d8 ["CALL", null, ["callee:00c57e30:8"]]
- 00c2ddb0 bytes 20a70094
+ 00c2e1d8 bytes 16a70094
- 00c2ddbc ["INT_ADD", "register:40f0:8", ["const:c2ddbc:8", "const:4:8"]]
- 00c2ddbc ["CALL", null, ["callee:00c57e70:8"]]
+ 00c2e1e4 ["INT_ADD", "register:40f0:8", ["const:c2e1e4:8", "const:4:8"]]
+ 00c2e1e4 ["CALL", null, ["callee:00c57e70:8"]]
- 00c2ddbc bytes 2da70094
+ 00c2e1e4 bytes 23a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c683780d96c681797f9a91eb50513a49"></a>

### [`00c2ddc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2ddc4.md) → [`00c2e1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e1ec.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__xEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e220",
      "incomplete_value": false,
      "site": "00c2e224",
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
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2ddf8",
      "incomplete_value": false,
      "site": "00c2ddfc",
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
            "const:b08:8"
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
      "definition_site": "00c2e238",
      "incomplete_value": true,
      "site": "00c2e244",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2de10",
      "incomplete_value": true,
      "site": "00c2de1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f8:8"
              ]
            ]
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
      "definition_site": "00c2e234",
      "incomplete_value": false,
      "site": "00c2e244",
      "value": [
        "leaf",
        "const:ca4810:8"
      ]
    },
    "old": {
      "definition_site": "00c2de0c",
      "incomplete_value": false,
      "site": "00c2de1c",
      "value": [
        "leaf",
        "const:ca4410:8"
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
      "00c2e200",
      "READ",
      [
        "storage",
        "01127b08",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e20c",
      "DATA",
      [
        "storage",
        "00ca4410",
        null,
        null
      ]
    ],
    [
      "00c2e220",
      "PARAM",
      [
        "storage",
        "01127b08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e200",
      "READ",
      [
        "storage",
        "01127f08",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e20c",
      "DATA",
      [
        "storage",
        "00ca4810",
        null,
        null
      ]
    ],
    [
      "00c2e220",
      "PARAM",
      [
        "storage",
        "01127f08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2ddfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2ddc4.md#insn-00c2ddfc) · [`00c2de1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2ddc4.md#insn-00c2de1c) · [`00c2de28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2ddc4.md#insn-00c2de28)
- 新版 [`00c2e224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e1ec.md#insn-00c2e224) · [`00c2e244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e1ec.md#insn-00c2e244) · [`00c2e250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e1ec.md#insn-00c2e250)

~~~diff
- 00c2ddfc ["INT_ADD", "register:40f0:8", ["const:c2ddfc:8", "const:4:8"]]
- 00c2ddfc ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2e224 ["INT_ADD", "register:40f0:8", ["const:c2e224:8", "const:4:8"]]
+ 00c2e224 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2ddfc bytes 15a70094
+ 00c2e224 bytes 0ba70094
- 00c2de1c ["INT_ADD", "register:40f0:8", ["const:c2de1c:8", "const:4:8"]]
- 00c2de1c ["CALL", null, ["callee:00c57e30:8"]]
+ 00c2e244 ["INT_ADD", "register:40f0:8", ["const:c2e244:8", "const:4:8"]]
+ 00c2e244 ["CALL", null, ["callee:00c57e30:8"]]
- 00c2de1c bytes 05a70094
+ 00c2e244 bytes fba60094
- 00c2de28 ["INT_ADD", "register:40f0:8", ["const:c2de28:8", "const:4:8"]]
- 00c2de28 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c2e250 ["INT_ADD", "register:40f0:8", ["const:c2e250:8", "const:4:8"]]
+ 00c2e250 ["CALL", null, ["callee:00c57e70:8"]]
- 00c2de28 bytes 12a70094
+ 00c2e250 bytes 08a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c7fc6035dd54395eef18ba58dac10a1"></a>

### [`00c2de30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2de30.md) → [`00c2e258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e258.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__xEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2900.md) [`00c2bc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bc6c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf2d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d28.md) [`00c2c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e294",
      "incomplete_value": false,
      "site": "00c2e298",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2de6c",
      "incomplete_value": false,
      "site": "00c2de70",
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
            "const:b28:8"
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
      "definition_site": "00c2e2a4",
      "incomplete_value": false,
      "site": "00c2e2b0",
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
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2de7c",
      "incomplete_value": false,
      "site": "00c2de88",
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
            "const:b10:8"
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
      "definition_site": "00c2e2ac",
      "incomplete_value": false,
      "site": "00c2e2b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2de84",
      "incomplete_value": false,
      "site": "00c2de88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "00c2e270",
      "READ",
      [
        "storage",
        "01127b28",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e27c",
      "DATA",
      [
        "storage",
        "01127b10",
        null,
        null
      ]
    ],
    [
      "00c2e294",
      "PARAM",
      [
        "storage",
        "01127b28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e270",
      "READ",
      [
        "storage",
        "01127f28",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e27c",
      "DATA",
      [
        "storage",
        "01127f10",
        null,
        null
      ]
    ],
    [
      "00c2e294",
      "PARAM",
      [
        "storage",
        "01127f28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2de70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2de30.md#insn-00c2de70) · [`00c2de88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2de30.md#insn-00c2de88) · [`00c2dea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2de30.md#insn-00c2dea4)
- 新版 [`00c2e298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e258.md#insn-00c2e298) · [`00c2e2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e258.md#insn-00c2e2b0) · [`00c2e2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e258.md#insn-00c2e2cc)

~~~diff
- 00c2de70 ["INT_ADD", "register:40f0:8", ["const:c2de70:8", "const:4:8"]]
- 00c2de70 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2e298 ["INT_ADD", "register:40f0:8", ["const:c2e298:8", "const:4:8"]]
+ 00c2e298 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2de70 bytes f8a60094
+ 00c2e298 bytes eea60094
- 00c2de88 ["INT_ADD", "register:40f0:8", ["const:c2de88:8", "const:4:8"]]
- 00c2de88 ["CALL", null, ["callee:00c2c094:8"]]
+ 00c2e2b0 ["INT_ADD", "register:40f0:8", ["const:c2e2b0:8", "const:4:8"]]
+ 00c2e2b0 ["CALL", null, ["callee:00c2c094:8"]]
- 00c2de88 bytes 79f7ff97
+ 00c2e2b0 bytes 79f7ff97
- 00c2dea4 ["INT_ADD", "register:40f0:8", ["const:c2dea4:8", "const:4:8"]]
- 00c2dea4 ["CALL", null, ["callee:00c57e30:8"]]
+ 00c2e2cc ["INT_ADD", "register:40f0:8", ["const:c2e2cc:8", "const:4:8"]]
+ 00c2e2cc ["CALL", null, ["callee:00c57e30:8"]]
- 00c2dea4 bytes e3a60094
+ 00c2e2cc bytes d9a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47137d9c075f231b9c0cf5819c9766d5"></a>

### [`00c2ded0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2ded0.md) → [`00c2e2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e2f8.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__XEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e32c",
      "incomplete_value": false,
      "site": "00c2e330",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2df04",
      "incomplete_value": false,
      "site": "00c2df08",
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
            "const:b30:8"
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
      "definition_site": "00c2e344",
      "incomplete_value": true,
      "site": "00c2e350",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2df1c",
      "incomplete_value": true,
      "site": "00c2df28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f8:8"
              ]
            ]
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
      "definition_site": "00c2e340",
      "incomplete_value": false,
      "site": "00c2e350",
      "value": [
        "leaf",
        "const:ca4828:8"
      ]
    },
    "old": {
      "definition_site": "00c2df18",
      "incomplete_value": false,
      "site": "00c2df28",
      "value": [
        "leaf",
        "const:ca4428:8"
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
      "00c2e30c",
      "READ",
      [
        "storage",
        "01127b30",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e318",
      "DATA",
      [
        "storage",
        "00ca4428",
        null,
        null
      ]
    ],
    [
      "00c2e32c",
      "PARAM",
      [
        "storage",
        "01127b30",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e30c",
      "READ",
      [
        "storage",
        "01127f30",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e318",
      "DATA",
      [
        "storage",
        "00ca4828",
        null,
        null
      ]
    ],
    [
      "00c2e32c",
      "PARAM",
      [
        "storage",
        "01127f30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2df08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2ded0.md#insn-00c2df08) · [`00c2df28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2ded0.md#insn-00c2df28) · [`00c2df34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2ded0.md#insn-00c2df34)
- 新版 [`00c2e330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e2f8.md#insn-00c2e330) · [`00c2e350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e2f8.md#insn-00c2e350) · [`00c2e35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e2f8.md#insn-00c2e35c)

~~~diff
- 00c2df08 ["INT_ADD", "register:40f0:8", ["const:c2df08:8", "const:4:8"]]
- 00c2df08 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2e330 ["INT_ADD", "register:40f0:8", ["const:c2e330:8", "const:4:8"]]
+ 00c2e330 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2df08 bytes d2a60094
+ 00c2e330 bytes c8a60094
- 00c2df28 ["INT_ADD", "register:40f0:8", ["const:c2df28:8", "const:4:8"]]
- 00c2df28 ["CALL", null, ["callee:00c57e30:8"]]
+ 00c2e350 ["INT_ADD", "register:40f0:8", ["const:c2e350:8", "const:4:8"]]
+ 00c2e350 ["CALL", null, ["callee:00c57e30:8"]]
- 00c2df28 bytes c2a60094
+ 00c2e350 bytes b8a60094
- 00c2df34 ["INT_ADD", "register:40f0:8", ["const:c2df34:8", "const:4:8"]]
- 00c2df34 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c2e35c ["INT_ADD", "register:40f0:8", ["const:c2e35c:8", "const:4:8"]]
+ 00c2e35c ["CALL", null, ["callee:00c57e70:8"]]
- 00c2df34 bytes cfa60094
+ 00c2e35c bytes c5a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8579bc0fd53504a2ee02e4860c55eaca"></a>

### [`00c2df3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2df3c.md) → [`00c2e364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e364.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__XEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2900.md) [`00c2bc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bc6c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf2d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d28.md) [`00c2c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e3a0",
      "incomplete_value": false,
      "site": "00c2e3a4",
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
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2df78",
      "incomplete_value": false,
      "site": "00c2df7c",
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
            "const:b50:8"
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
      "definition_site": "00c2e3b0",
      "incomplete_value": false,
      "site": "00c2e3bc",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2df88",
      "incomplete_value": false,
      "site": "00c2df94",
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
            "const:b38:8"
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
      "definition_site": "00c2e3b8",
      "incomplete_value": false,
      "site": "00c2e3bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2df90",
      "incomplete_value": false,
      "site": "00c2df94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:598:8"
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
      "00c2e37c",
      "READ",
      [
        "storage",
        "01127b50",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e388",
      "DATA",
      [
        "storage",
        "01127b38",
        null,
        null
      ]
    ],
    [
      "00c2e3a0",
      "PARAM",
      [
        "storage",
        "01127b50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e37c",
      "READ",
      [
        "storage",
        "01127f50",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e388",
      "DATA",
      [
        "storage",
        "01127f38",
        null,
        null
      ]
    ],
    [
      "00c2e3a0",
      "PARAM",
      [
        "storage",
        "01127f50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2df7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2df3c.md#insn-00c2df7c) · [`00c2df94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2df3c.md#insn-00c2df94) · [`00c2dfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2df3c.md#insn-00c2dfb0)
- 新版 [`00c2e3a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e364.md#insn-00c2e3a4) · [`00c2e3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e364.md#insn-00c2e3bc) · [`00c2e3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e364.md#insn-00c2e3d8)

~~~diff
- 00c2df7c ["INT_ADD", "register:40f0:8", ["const:c2df7c:8", "const:4:8"]]
- 00c2df7c ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2e3a4 ["INT_ADD", "register:40f0:8", ["const:c2e3a4:8", "const:4:8"]]
+ 00c2e3a4 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2df7c bytes b5a60094
+ 00c2e3a4 bytes aba60094
- 00c2df94 ["INT_ADD", "register:40f0:8", ["const:c2df94:8", "const:4:8"]]
- 00c2df94 ["CALL", null, ["callee:00c2c094:8"]]
+ 00c2e3bc ["INT_ADD", "register:40f0:8", ["const:c2e3bc:8", "const:4:8"]]
+ 00c2e3bc ["CALL", null, ["callee:00c2c094:8"]]
- 00c2df94 bytes 36f7ff97
+ 00c2e3bc bytes 36f7ff97
- 00c2dfb0 ["INT_ADD", "register:40f0:8", ["const:c2dfb0:8", "const:4:8"]]
- 00c2dfb0 ["CALL", null, ["callee:00c57e30:8"]]
+ 00c2e3d8 ["INT_ADD", "register:40f0:8", ["const:c2e3d8:8", "const:4:8"]]
+ 00c2e3d8 ["CALL", null, ["callee:00c57e30:8"]]
- 00c2dfb0 bytes a0a60094
+ 00c2e3d8 bytes 96a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb5b718078a3a481a4f90037a5bcb434"></a>

### [`00c2dfdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dfdc.md) → [`00c2e404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e404.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__cEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e438",
      "incomplete_value": false,
      "site": "00c2e43c",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e010",
      "incomplete_value": false,
      "site": "00c2e014",
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
            "const:b58:8"
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
      "definition_site": "00c2e450",
      "incomplete_value": true,
      "site": "00c2e45c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e028",
      "incomplete_value": true,
      "site": "00c2e034",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f8:8"
              ]
            ]
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
      "definition_site": "00c2e44c",
      "incomplete_value": false,
      "site": "00c2e45c",
      "value": [
        "leaf",
        "const:ca4840:8"
      ]
    },
    "old": {
      "definition_site": "00c2e024",
      "incomplete_value": false,
      "site": "00c2e034",
      "value": [
        "leaf",
        "const:ca4440:8"
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
      "00c2e418",
      "READ",
      [
        "storage",
        "01127b58",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e424",
      "DATA",
      [
        "storage",
        "00ca4440",
        null,
        "string"
      ]
    ],
    [
      "00c2e438",
      "PARAM",
      [
        "storage",
        "01127b58",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e418",
      "READ",
      [
        "storage",
        "01127f58",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e424",
      "DATA",
      [
        "storage",
        "00ca4840",
        null,
        "string"
      ]
    ],
    [
      "00c2e438",
      "PARAM",
      [
        "storage",
        "01127f58",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dfdc.md#insn-00c2e014) · [`00c2e034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dfdc.md#insn-00c2e034) · [`00c2dfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2dfdc.md#insn-00c2dfec)
- 新版 [`00c2e43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e404.md#insn-00c2e43c) · [`00c2e45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e404.md#insn-00c2e45c) · [`00c2e414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e404.md#insn-00c2e414)

~~~diff
- 00c2e014 ["INT_ADD", "register:40f0:8", ["const:c2e014:8", "const:4:8"]]
- 00c2e014 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2e43c ["INT_ADD", "register:40f0:8", ["const:c2e43c:8", "const:4:8"]]
+ 00c2e43c ["CALL", null, ["callee:00c57e50:8"]]
- 00c2e014 bytes 8fa60094
+ 00c2e43c bytes 85a60094
- 00c2e034 ["INT_ADD", "register:40f0:8", ["const:c2e034:8", "const:4:8"]]
- 00c2e034 ["CALL", null, ["callee:00c57e30:8"]]
+ 00c2e45c ["INT_ADD", "register:40f0:8", ["const:c2e45c:8", "const:4:8"]]
+ 00c2e45c ["CALL", null, ["callee:00c57e30:8"]]
- 00c2e034 bytes 7fa60094
+ 00c2e45c bytes 75a60094
- 00c2dfec ["COPY", "tmp:0:8", ["const:b58:8"]]
- 00c2dfec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c2dfec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c2dfec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c2e414 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00c2e414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c2e414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c2e414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c2dfec bytes 08612d91
+ 00c2e414 bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01ac3213bdaa5431ee6789c1aa8f4d03"></a>

### [`00c2e048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e048.md) → [`00c2e470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e470.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__cEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2900.md) [`00c2bc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bc6c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf2d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d28.md) [`00c2c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e4ac",
      "incomplete_value": false,
      "site": "00c2e4b0",
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
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e084",
      "incomplete_value": false,
      "site": "00c2e088",
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
            "const:b78:8"
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
      "definition_site": "00c2e4bc",
      "incomplete_value": false,
      "site": "00c2e4c8",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e094",
      "incomplete_value": false,
      "site": "00c2e0a0",
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
            "const:b60:8"
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
      "definition_site": "00c2e4c4",
      "incomplete_value": false,
      "site": "00c2e4c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e09c",
      "incomplete_value": false,
      "site": "00c2e0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "00c2e488",
      "READ",
      [
        "storage",
        "01127b78",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e494",
      "DATA",
      [
        "storage",
        "01127b60",
        null,
        null
      ]
    ],
    [
      "00c2e4ac",
      "PARAM",
      [
        "storage",
        "01127b78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e488",
      "READ",
      [
        "storage",
        "01127f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e494",
      "DATA",
      [
        "storage",
        "01127f60",
        null,
        null
      ]
    ],
    [
      "00c2e4ac",
      "PARAM",
      [
        "storage",
        "01127f78",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e048.md#insn-00c2e088) · [`00c2e0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e048.md#insn-00c2e0a0) · [`00c2e0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e048.md#insn-00c2e0bc)
- 新版 [`00c2e4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e470.md#insn-00c2e4b0) · [`00c2e4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e470.md#insn-00c2e4c8) · [`00c2e4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e470.md#insn-00c2e4e4)

~~~diff
- 00c2e088 ["INT_ADD", "register:40f0:8", ["const:c2e088:8", "const:4:8"]]
- 00c2e088 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2e4b0 ["INT_ADD", "register:40f0:8", ["const:c2e4b0:8", "const:4:8"]]
+ 00c2e4b0 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2e088 bytes 72a60094
+ 00c2e4b0 bytes 68a60094
- 00c2e0a0 ["INT_ADD", "register:40f0:8", ["const:c2e0a0:8", "const:4:8"]]
- 00c2e0a0 ["CALL", null, ["callee:00c2c094:8"]]
+ 00c2e4c8 ["INT_ADD", "register:40f0:8", ["const:c2e4c8:8", "const:4:8"]]
+ 00c2e4c8 ["CALL", null, ["callee:00c2c094:8"]]
- 00c2e0a0 bytes f3f6ff97
+ 00c2e4c8 bytes f3f6ff97
- 00c2e0bc ["INT_ADD", "register:40f0:8", ["const:c2e0bc:8", "const:4:8"]]
- 00c2e0bc ["CALL", null, ["callee:00c57e30:8"]]
+ 00c2e4e4 ["INT_ADD", "register:40f0:8", ["const:c2e4e4:8", "const:4:8"]]
+ 00c2e4e4 ["CALL", null, ["callee:00c57e30:8"]]
- 00c2e0bc bytes 5da60094
+ 00c2e4e4 bytes 53a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e68362dd9245d13814c52b43ab3869c"></a>

### [`00c2e0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e0e8.md) → [`00c2e510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e510.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__rEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e544",
      "incomplete_value": false,
      "site": "00c2e548",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e11c",
      "incomplete_value": false,
      "site": "00c2e120",
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
            "const:b80:8"
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
      "definition_site": "00c2e55c",
      "incomplete_value": true,
      "site": "00c2e568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e134",
      "incomplete_value": true,
      "site": "00c2e140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f8:8"
              ]
            ]
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
      "definition_site": "00c2e558",
      "incomplete_value": false,
      "site": "00c2e568",
      "value": [
        "leaf",
        "const:ca4858:8"
      ]
    },
    "old": {
      "definition_site": "00c2e130",
      "incomplete_value": false,
      "site": "00c2e140",
      "value": [
        "leaf",
        "const:ca4458:8"
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
      "00c2e524",
      "READ",
      [
        "storage",
        "01127b80",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e530",
      "DATA",
      [
        "storage",
        "00ca4458",
        null,
        null
      ]
    ],
    [
      "00c2e544",
      "PARAM",
      [
        "storage",
        "01127b80",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e524",
      "READ",
      [
        "storage",
        "01127f80",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e530",
      "DATA",
      [
        "storage",
        "00ca4858",
        null,
        null
      ]
    ],
    [
      "00c2e544",
      "PARAM",
      [
        "storage",
        "01127f80",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e0e8.md#insn-00c2e120) · [`00c2e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e0e8.md#insn-00c2e140) · [`00c2e14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e0e8.md#insn-00c2e14c)
- 新版 [`00c2e548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e510.md#insn-00c2e548) · [`00c2e568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e510.md#insn-00c2e568) · [`00c2e574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e510.md#insn-00c2e574)

~~~diff
- 00c2e120 ["INT_ADD", "register:40f0:8", ["const:c2e120:8", "const:4:8"]]
- 00c2e120 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2e548 ["INT_ADD", "register:40f0:8", ["const:c2e548:8", "const:4:8"]]
+ 00c2e548 ["CALL", null, ["callee:00c57e50:8"]]
- 00c2e120 bytes 4ca60094
+ 00c2e548 bytes 42a60094
- 00c2e140 ["INT_ADD", "register:40f0:8", ["const:c2e140:8", "const:4:8"]]
- 00c2e140 ["CALL", null, ["callee:00c57e30:8"]]
+ 00c2e568 ["INT_ADD", "register:40f0:8", ["const:c2e568:8", "const:4:8"]]
+ 00c2e568 ["CALL", null, ["callee:00c57e30:8"]]
- 00c2e140 bytes 3ca60094
+ 00c2e568 bytes 32a60094
- 00c2e14c ["INT_ADD", "register:40f0:8", ["const:c2e14c:8", "const:4:8"]]
- 00c2e14c ["CALL", null, ["callee:00c57e70:8"]]
+ 00c2e574 ["INT_ADD", "register:40f0:8", ["const:c2e574:8", "const:4:8"]]
+ 00c2e574 ["CALL", null, ["callee:00c57e70:8"]]
- 00c2e14c bytes 49a60094
+ 00c2e574 bytes 3fa60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cf9abcb98f4a205e828ec9dcab06c53"></a>

### [`00c2e154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e154.md) → [`00c2e57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e57c.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__rEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2900.md) [`00c2bc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bc6c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf2d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d28.md) [`00c2c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e5b8",
      "incomplete_value": false,
      "site": "00c2e5bc",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e190",
      "incomplete_value": false,
      "site": "00c2e194",
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
            "const:ba0:8"
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
      "definition_site": "00c2e5c8",
      "incomplete_value": false,
      "site": "00c2e5d4",
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
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e1a0",
      "incomplete_value": false,
      "site": "00c2e1ac",
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
            "const:b88:8"
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
      "definition_site": "00c2e5d0",
      "incomplete_value": false,
      "site": "00c2e5d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e1a8",
      "incomplete_value": false,
      "site": "00c2e1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
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
      "00c2e594",
      "READ",
      [
        "storage",
        "01127ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e5a0",
      "DATA",
      [
        "storage",
        "01127b88",
        null,
        null
      ]
    ],
    [
      "00c2e5b8",
      "PARAM",
      [
        "storage",
        "01127ba0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e594",
      "READ",
      [
        "storage",
        "01127fa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e5a0",
      "DATA",
      [
        "storage",
        "01127f88",
        null,
        null
      ]
    ],
    [
      "00c2e5b8",
      "PARAM",
      [
        "storage",
        "01127fa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e154.md#insn-00c2e194) · [`00c2e1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e154.md#insn-00c2e1ac) · [`00c2e1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e154.md#insn-00c2e1c8)
- 新版 [`00c2e5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e57c.md#insn-00c2e5bc) · [`00c2e5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e57c.md#insn-00c2e5d4) · [`00c2e5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e57c.md#insn-00c2e5f0)

~~~diff
- 00c2e194 ["INT_ADD", "register:40f0:8", ["const:c2e194:8", "const:4:8"]]
- 00c2e194 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2e5bc ["INT_ADD", "register:40f0:8", ["const:c2e5bc:8", "const:4:8"]]
+ 00c2e5bc ["CALL", null, ["callee:00c57e50:8"]]
- 00c2e194 bytes 2fa60094
+ 00c2e5bc bytes 25a60094
- 00c2e1ac ["INT_ADD", "register:40f0:8", ["const:c2e1ac:8", "const:4:8"]]
- 00c2e1ac ["CALL", null, ["callee:00c2c094:8"]]
+ 00c2e5d4 ["INT_ADD", "register:40f0:8", ["const:c2e5d4:8", "const:4:8"]]
+ 00c2e5d4 ["CALL", null, ["callee:00c2c094:8"]]
- 00c2e1ac bytes b0f6ff97
+ 00c2e5d4 bytes b0f6ff97
- 00c2e1c8 ["INT_ADD", "register:40f0:8", ["const:c2e1c8:8", "const:4:8"]]
- 00c2e1c8 ["CALL", null, ["callee:00c57e30:8"]]
+ 00c2e5f0 ["INT_ADD", "register:40f0:8", ["const:c2e5f0:8", "const:4:8"]]
+ 00c2e5f0 ["CALL", null, ["callee:00c57e30:8"]]
- 00c2e1c8 bytes 1aa60094
+ 00c2e5f0 bytes 10a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c8440ef8bfdc0c77d014faccd3e5f6d"></a>

### [`00c2e1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e1f4.md) → [`00c2e61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e61c.md) _ZNSt6__ndk110__time_getC1EPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8a0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 1件 [`00c5eca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eca0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e670",
      "incomplete_value": false,
      "site": "00c2e680",
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
            "const:fd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e248",
      "incomplete_value": false,
      "site": "00c2e258",
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
            "const:f92:8"
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
      "00c2e670",
      "PARAM",
      [
        "storage",
        "002b6f92",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2e670",
      "PARAM",
      [
        "storage",
        "002b6fd2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e1f4.md#insn-00c2e258) · [`00c2e218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e1f4.md#insn-00c2e218) · [`00c2e240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e1f4.md#insn-00c2e240)
- 新版 [`00c2e680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e61c.md#insn-00c2e680) · [`00c2e640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e61c.md#insn-00c2e640) · [`00c2e668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e61c.md#insn-00c2e668)

~~~diff
- 00c2e258 ["INT_ADD", "register:40f0:8", ["const:c2e258:8", "const:4:8"]]
- 00c2e258 ["CALL", null, ["callee:00c25934:8"]]
+ 00c2e680 ["INT_ADD", "register:40f0:8", ["const:c2e680:8", "const:4:8"]]
+ 00c2e680 ["CALL", null, ["callee:00c25934:8"]]
- 00c2e258 bytes addcff97
+ 00c2e680 bytes addcff97
- 00c2e218 ["INT_ADD", "register:40f0:8", ["const:c2e218:8", "const:4:8"]]
- 00c2e218 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c2e640 ["INT_ADD", "register:40f0:8", ["const:c2e640:8", "const:4:8"]]
+ 00c2e640 ["CALL", null, ["callee:00c5d220:8"]]
- 00c2e218 bytes 02bb0094
+ 00c2e640 bytes f8ba0094
- 00c2e240 ["INT_ADD", "register:40f0:8", ["const:c2e240:8", "const:4:8"]]
- 00c2e240 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00c2e668 ["INT_ADD", "register:40f0:8", ["const:c2e668:8", "const:4:8"]]
+ 00c2e668 ["CALL", null, ["callee:0043ddd8:8"]]
- 00c2e240 bytes d63ee097
+ 00c2e668 bytes dc3de097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e20fb9c55c2b2b7af9028194eb7818ca"></a>

### [`00c2e2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e2bc.md) → [`00c2e6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e6e4.md) _ZNSt6__ndk110__time_getC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8b0.md) · 呼出先 5件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md)
- 新版 呼出元 1件 [`00c5ecb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecb0.md) · 呼出先 5件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2e73c",
      "incomplete_value": false,
      "site": "00c2e74c",
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
            "const:fd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e314",
      "incomplete_value": false,
      "site": "00c2e324",
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
            "const:f92:8"
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
      "00c2e73c",
      "PARAM",
      [
        "storage",
        "002b6f92",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2e73c",
      "PARAM",
      [
        "storage",
        "002b6fd2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e2bc.md#insn-00c2e324) · [`00c2e2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e2bc.md#insn-00c2e2f0) · [`00c2e314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e2bc.md#insn-00c2e314)
- 新版 [`00c2e74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e6e4.md#insn-00c2e74c) · [`00c2e718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e6e4.md#insn-00c2e718) · [`00c2e73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e6e4.md#insn-00c2e73c)

~~~diff
- 00c2e324 ["INT_ADD", "register:40f0:8", ["const:c2e324:8", "const:4:8"]]
- 00c2e324 ["CALL", null, ["callee:00c580b0:8"]]
+ 00c2e74c ["INT_ADD", "register:40f0:8", ["const:c2e74c:8", "const:4:8"]]
+ 00c2e74c ["CALL", null, ["callee:00c580b0:8"]]
- 00c2e324 bytes 63a60094
+ 00c2e74c bytes 59a60094
- 00c2e2f0 ["INT_ADD", "register:40f0:8", ["const:c2e2f0:8", "const:4:8"]]
- 00c2e2f0 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c2e718 ["INT_ADD", "register:40f0:8", ["const:c2e718:8", "const:4:8"]]
+ 00c2e718 ["CALL", null, ["callee:00c5d220:8"]]
- 00c2e2f0 bytes ccba0094
+ 00c2e718 bytes c2ba0094
- 00c2e314 ["COPY", "tmp:0:8", ["const:f92:8"]]
- 00c2e314 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c2e314 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c2e314 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c2e73c ["COPY", "tmp:0:8", ["const:fd2:8"]]
+ 00c2e73c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c2e73c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c2e73c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c2e314 bytes 00483e91
+ 00c2e73c bytes 00483f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b245fee0f66d516d535d6d2dddfce378"></a>

### [`00c2e37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e37c.md) → [`00c2e7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e7a4.md) _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8d0.md) · 呼出先 3件 [`00c2e964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e964.md) [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md) [`00c5e260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e260.md)
- 新版 呼出元 1件 [`00c5ecd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecd0.md) · 呼出先 3件 [`00c2ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2ed8c.md) [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md) [`00c5e660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e660.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2e7d4",
      "incomplete_value": true,
      "site": "00c2e7ec",
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
                "const:6d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e3ac",
      "incomplete_value": true,
      "site": "00c2e3c4",
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
                "const:690:8"
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
      "definition_site": "00c2e7f0",
      "incomplete_value": true,
      "site": "00c2e804",
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e3c8",
      "incomplete_value": true,
      "site": "00c2e3dc",
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
                "const:ba0:8"
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
      "00c2e7d4",
      "READ",
      [
        "storage",
        "002c2690",
        null,
        null
      ]
    ],
    [
      "00c2e7f0",
      "READ",
      [
        "storage",
        "002c2ba0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2e7d4",
      "READ",
      [
        "storage",
        "002c26d0",
        null,
        null
      ]
    ],
    [
      "00c2e7f0",
      "READ",
      [
        "storage",
        "002c2be0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e37c.md#insn-00c2e3ac) · [`00c2e3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e37c.md#insn-00c2e3c8) · [`00c2e404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2e37c.md#insn-00c2e404)
- 新版 [`00c2e7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e7a4.md#insn-00c2e7d4) · [`00c2e7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e7a4.md#insn-00c2e7f0) · [`00c2e82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e7a4.md#insn-00c2e82c)

~~~diff
- 00c2e3ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:690:8"]]
- 00c2e3ac ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2e3ac ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2e3ac ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c2e7d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d0:8"]]
+ 00c2e7d4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c2e7d4 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2e7d4 ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2e3ac bytes 20a5c13d
+ 00c2e7d4 bytes 20b5c13d
- 00c2e3c8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ba0:8"]]
- 00c2e3c8 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2e3c8 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2e3c8 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c2e7f0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:be0:8"]]
+ 00c2e7f0 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c2e7f0 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2e7f0 ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2e3c8 bytes 20e9c23d
+ 00c2e7f0 bytes 20f9c23d
- 00c2e404 ["INT_ADD", "register:40f0:8", ["const:c2e404:8", "const:4:8"]]
- 00c2e404 ["CALL", null, ["callee:00c5e660:8"]]
+ 00c2e82c ["INT_ADD", "register:40f0:8", ["const:c2e82c:8", "const:4:8"]]
+ 00c2e82c ["CALL", null, ["callee:00c5e660:8"]]
- 00c2e404 bytes 97bf0094
+ 00c2e82c bytes 8dbf0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dca24cbce3d02099c64b4f189b8a80c"></a>

### [`00c2ec74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2ec74.md) → [`00c2f09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2f/00c2f09c.md) _ZNSt6__ndk118__time_get_storageIwE9__analyzeEcRKNS_5ctypeIwEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5e8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8e0.md) · 呼出先 8件 [`00c3031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c3031c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md)
- 新版 呼出元 1件 [`00c5ece0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ece0.md) · 呼出先 8件 [`00c30744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30744.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.65% / 新版 99.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2f0cc",
      "incomplete_value": true,
      "site": "00c2f114",
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
                "const:6d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2eca4",
      "incomplete_value": true,
      "site": "00c2ecec",
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
                "const:690:8"
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
      "definition_site": "00c2f0d8",
      "incomplete_value": true,
      "site": "00c2f114",
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2ecb0",
      "incomplete_value": true,
      "site": "00c2ecec",
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
                "const:ba0:8"
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
      "definition_site": "00c306f0",
      "incomplete_value": false,
      "site": "00c306f4",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c302c8",
      "incomplete_value": false,
      "site": "00c302cc",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2f0cc",
      "READ",
      [
        "storage",
        "002c2690",
        null,
        null
      ]
    ],
    [
      "00c2f0d8",
      "READ",
      [
        "storage",
        "002c2ba0",
        null,
        null
      ]
    ],
    [
      "00c306f0",
      "PARAM",
      [
        "storage",
        "0029fd18",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2f0cc",
      "READ",
      [
        "storage",
        "002c26d0",
        null,
        null
      ]
    ],
    [
      "00c2f0d8",
      "READ",
      [
        "storage",
        "002c2be0",
        null,
        null
      ]
    ],
    [
      "00c306f0",
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c302cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2ec74.md#insn-00c302cc) · [`00c2eca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2ec74.md#insn-00c2eca4) · [`00c2eca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2e/00c2ec74.md#insn-00c2eca8)
- 新版 [`00c306f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2f/00c2f09c.md#insn-00c306f4) · [`00c2f0cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2f/00c2f09c.md#insn-00c2f0cc)

~~~diff
- 00c302cc ["INT_ADD", "register:40f0:8", ["const:c302cc:8", "const:4:8"]]
- 00c302cc ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c306f4 ["INT_ADD", "register:40f0:8", ["const:c306f4:8", "const:4:8"]]
+ 00c306f4 ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c302cc bytes 39b60094
+ 00c306f4 bytes 2fb60094
- 00c2eca4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:690:8"]]
- 00c2eca4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2eca4 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2eca4 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c2f0cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6d0:8"]]
+ 00c2f0cc ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c2f0cc ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2f0cc ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2eca4 bytes 00a5c13d
+ 00c2f0cc bytes 00b5c13d
- 00c2eca8 ["COPY", "register:4040:8", ["const:2c2000:8"]]
- 00c2eca8 bytes a8b4ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d989ae5fedc3f544b06b21a54900b2dc"></a>

### [`00c308c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c308c0.md) → [`00c30ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30ce8.md) _ZNSt6__ndk118__time_get_storageIwE4initERKNS_5ctypeIwEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e900.md) · 呼出先 8件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md) [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md)
- 新版 呼出元 1件 [`00c5ed00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed00.md) · 呼出先 8件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md) [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c30d70",
      "incomplete_value": false,
      "site": "00c30d78",
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
            "const:801:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c30948",
      "incomplete_value": false,
      "site": "00c30950",
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
            "const:7c1:8"
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
      "definition_site": "00c30ed0",
      "incomplete_value": false,
      "site": "00c30ed4",
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
            "const:51d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c30aa8",
      "incomplete_value": false,
      "site": "00c30aac",
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
            "const:4dd:8"
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
      "definition_site": "00c311b8",
      "incomplete_value": false,
      "site": "00c311bc",
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
            "const:e1a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c30d90",
      "incomplete_value": false,
      "site": "00c30d94",
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
            "const:d4d:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c30d70",
      "PARAM",
      [
        "storage",
        "002b27c1",
        null,
        null
      ]
    ],
    [
      "00c30ed0",
      "PARAM",
      [
        "storage",
        "002ac4dd",
        null,
        null
      ]
    ],
    [
      "00c31058",
      "PARAM",
      [
        "storage",
        "002af707",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c30d70",
      "PARAM",
      [
        "storage",
        "002b2801",
        null,
        null
      ]
    ],
    [
      "00c30ed0",
      "PARAM",
      [
        "storage",
        "002ac51d",
        null,
        null
      ]
    ],
    [
      "00c31058",
      "PARAM",
      [
        "storage",
        "002af747",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c30950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c308c0.md#insn-00c30950) · [`00c30aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c308c0.md#insn-00c30aac) · [`00c30d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c308c0.md#insn-00c30d94)
- 新版 [`00c30d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30ce8.md#insn-00c30d78) · [`00c30ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30ce8.md#insn-00c30ed4) · [`00c311bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30ce8.md#insn-00c311bc)

~~~diff
- 00c30950 ["INT_ADD", "register:40f0:8", ["const:c30950:8", "const:4:8"]]
- 00c30950 ["CALL", null, ["callee:00c5e660:8"]]
+ 00c30d78 ["INT_ADD", "register:40f0:8", ["const:c30d78:8", "const:4:8"]]
+ 00c30d78 ["CALL", null, ["callee:00c5e660:8"]]
- 00c30950 bytes 44b60094
+ 00c30d78 bytes 3ab60094
- 00c30aac ["INT_ADD", "register:40f0:8", ["const:c30aac:8", "const:4:8"]]
- 00c30aac ["CALL", null, ["callee:00c5e660:8"]]
+ 00c30ed4 ["INT_ADD", "register:40f0:8", ["const:c30ed4:8", "const:4:8"]]
+ 00c30ed4 ["CALL", null, ["callee:00c5e660:8"]]
- 00c30aac bytes edb50094
+ 00c30ed4 bytes e3b50094
- 00c30d94 ["INT_ADD", "register:40f0:8", ["const:c30d94:8", "const:4:8"]]
- 00c30d94 ["CALL", null, ["callee:00c5e660:8"]]
+ 00c311bc ["INT_ADD", "register:40f0:8", ["const:c311bc:8", "const:4:8"]]
+ 00c311bc ["CALL", null, ["callee:00c5e660:8"]]
- 00c30d94 bytes 33b50094
+ 00c311bc bytes 29b50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22d8a922ea55d2abf6da97fad13efd2e"></a>

### [`00c31338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31338.md) → [`00c31760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31760.md) _ZNSt6__ndk118__time_get_storageIcEC1EPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md) [`00c5e5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5e9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c317a8",
      "incomplete_value": false,
      "site": "00c317ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c31380",
      "incomplete_value": false,
      "site": "00c31384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "definition_site": "00c317c8",
      "incomplete_value": true,
      "site": "00c317cc",
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
      "definition_site": "00c313a0",
      "incomplete_value": true,
      "site": "00c313a4",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c317e0",
      "incomplete_value": true,
      "site": "00c317e4",
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
      "definition_site": "00c313b8",
      "incomplete_value": true,
      "site": "00c313bc",
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
      "00c317ac",
      "DATA",
      [
        "storage",
        "00c958a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c317c0",
      "READ",
      [
        "storage",
        "00c9b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c317cc",
      "DATA",
      [
        "storage",
        "00c933d0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c317ac",
      "DATA",
      [
        "storage",
        "00c95ca0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c317c0",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c317cc",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c31358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31338.md#insn-00c31358) · [`00c31368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31338.md#insn-00c31368) · [`00c31378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31338.md#insn-00c31378)
- 新版 [`00c31780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31760.md#insn-00c31780) · [`00c31790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31760.md#insn-00c31790) · [`00c317a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31760.md#insn-00c317a0)

~~~diff
- 00c31358 ["INT_ADD", "register:40f0:8", ["const:c31358:8", "const:4:8"]]
- 00c31358 ["CALL", null, ["callee:00c5eca0:8"]]
+ 00c31780 ["INT_ADD", "register:40f0:8", ["const:c31780:8", "const:4:8"]]
+ 00c31780 ["CALL", null, ["callee:00c5eca0:8"]]
- 00c31358 bytes 52b50094
+ 00c31780 bytes 48b50094
- 00c31368 ["INT_ADD", "register:40f0:8", ["const:c31368:8", "const:4:8"]]
- 00c31368 ["CALL", null, ["callee:00c58090:8"]]
+ 00c31790 ["INT_ADD", "register:40f0:8", ["const:c31790:8", "const:4:8"]]
+ 00c31790 ["CALL", null, ["callee:00c58090:8"]]
- 00c31368 bytes 4a9a0094
+ 00c31790 bytes 409a0094
- 00c31378 ["INT_ADD", "register:40f0:8", ["const:c31378:8", "const:4:8"]]
- 00c31378 ["CALL", null, ["callee:00c5e9c0:8"]]
+ 00c317a0 ["INT_ADD", "register:40f0:8", ["const:c317a0:8", "const:4:8"]]
+ 00c317a0 ["CALL", null, ["callee:00c5e9c0:8"]]
- 00c31378 bytes 92b40094
+ 00c317a0 bytes 88b40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59ab50350e0e4b01584f65d5bf34b0fa"></a>

### [`00c31618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31618.md) → [`00c31a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31a40.md) _ZNSt6__ndk112ctype_bynameIcED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5e5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5e0.md) [`00c5e910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e910.md) · 呼出先 3件 [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md)
- 新版 呼出元 2件 [`00c5e9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9e0.md) [`00c5ed10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed10.md) · 呼出先 3件 [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31a60",
      "incomplete_value": true,
      "site": "00c31a64",
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
      "definition_site": "00c31638",
      "incomplete_value": true,
      "site": "00c3163c",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31a78",
      "incomplete_value": true,
      "site": "00c31a7c",
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
      "definition_site": "00c31650",
      "incomplete_value": true,
      "site": "00c31654",
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
      "00c31a58",
      "READ",
      [
        "storage",
        "00c9b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c31a64",
      "DATA",
      [
        "storage",
        "00c933d0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c31a70",
      "READ",
      [
        "storage",
        "00c9b9c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c31a58",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c31a64",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c31a70",
      "READ",
      [
        "storage",
        "00c9bdc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c31630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31618.md#insn-00c31630) · [`00c31640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31618.md#insn-00c31640) · [`00c31648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31618.md#insn-00c31648)
- 新版 [`00c31a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31a40.md#insn-00c31a58) · [`00c31a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31a40.md#insn-00c31a68) · [`00c31a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31a40.md#insn-00c31a70)

~~~diff
- 00c31630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00c31630 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c31a58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00c31a58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c31630 bytes 08e944f9
+ 00c31a58 bytes 08e946f9
- 00c31640 ["INT_ADD", "register:40f0:8", ["const:c31640:8", "const:4:8"]]
- 00c31640 ["CALL", null, ["callee:00c5d1d0:8"]]
+ 00c31a68 ["INT_ADD", "register:40f0:8", ["const:c31a68:8", "const:4:8"]]
+ 00c31a68 ["CALL", null, ["callee:00c5d1d0:8"]]
- 00c31640 bytes e4ad0094
+ 00c31a68 bytes daad0094
- 00c31648 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9c8:8"]]
- 00c31648 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c31a70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc8:8"]]
+ 00c31a70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c31648 bytes 08e544f9
+ 00c31a70 bytes 08e546f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69eb9451bdd88b9c397e1663be0f9cc4"></a>

### [`00c31680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31680.md) → [`00c31aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31aa8.md) _ZNSt6__ndk118__time_get_storageIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e490.md) · 呼出先 7件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md) [`00c5e5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5d0.md)
- 新版 呼出元 1件 [`00c5e890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e890.md) · 呼出先 7件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5e9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31af0",
      "incomplete_value": false,
      "site": "00c31af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c316c8",
      "incomplete_value": false,
      "site": "00c316cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "definition_site": "00c31b10",
      "incomplete_value": true,
      "site": "00c31b14",
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
      "definition_site": "00c316e8",
      "incomplete_value": true,
      "site": "00c316ec",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31b28",
      "incomplete_value": true,
      "site": "00c31b2c",
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
      "definition_site": "00c31700",
      "incomplete_value": true,
      "site": "00c31704",
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
      "00c31af4",
      "DATA",
      [
        "storage",
        "00c958a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c31b08",
      "READ",
      [
        "storage",
        "00c9b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c31b14",
      "DATA",
      [
        "storage",
        "00c933d0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c31af4",
      "DATA",
      [
        "storage",
        "00c95ca0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c31b08",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c31b14",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c316a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31680.md#insn-00c316a0) · [`00c316b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31680.md#insn-00c316b0) · [`00c316c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31680.md#insn-00c316c0)
- 新版 [`00c31ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31aa8.md#insn-00c31ac8) · [`00c31ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31aa8.md#insn-00c31ad8) · [`00c31ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31aa8.md#insn-00c31ae8)

~~~diff
- 00c316a0 ["INT_ADD", "register:40f0:8", ["const:c316a0:8", "const:4:8"]]
- 00c316a0 ["CALL", null, ["callee:00c5ecb0:8"]]
+ 00c31ac8 ["INT_ADD", "register:40f0:8", ["const:c31ac8:8", "const:4:8"]]
+ 00c31ac8 ["CALL", null, ["callee:00c5ecb0:8"]]
- 00c316a0 bytes 84b40094
+ 00c31ac8 bytes 7ab40094
- 00c316b0 ["INT_ADD", "register:40f0:8", ["const:c316b0:8", "const:4:8"]]
- 00c316b0 ["CALL", null, ["callee:00c58090:8"]]
+ 00c31ad8 ["INT_ADD", "register:40f0:8", ["const:c31ad8:8", "const:4:8"]]
+ 00c31ad8 ["CALL", null, ["callee:00c58090:8"]]
- 00c316b0 bytes 78990094
+ 00c31ad8 bytes 6e990094
- 00c316c0 ["INT_ADD", "register:40f0:8", ["const:c316c0:8", "const:4:8"]]
- 00c316c0 ["CALL", null, ["callee:00c5e9d0:8"]]
+ 00c31ae8 ["INT_ADD", "register:40f0:8", ["const:c31ae8:8", "const:4:8"]]
+ 00c31ae8 ["CALL", null, ["callee:00c5e9d0:8"]]
- 00c316c0 bytes c4b30094
+ 00c31ae8 bytes bab30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fa01b8609a8d072af7a7fc12c41c838"></a>

### [`00c31960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31960.md) → [`00c31d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31d88.md) _ZNSt6__ndk118__time_get_storageIwEC1EPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md) [`00c5e5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e600.md) [`00c5e8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8a0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5e9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e9f0.md) [`00c5ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea00.md) [`00c5eca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eca0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c31dd0",
      "incomplete_value": false,
      "site": "00c31dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c319a8",
      "incomplete_value": false,
      "site": "00c319ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "definition_site": "00c31df0",
      "incomplete_value": true,
      "site": "00c31df4",
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
      "definition_site": "00c319c8",
      "incomplete_value": true,
      "site": "00c319cc",
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
      "00c31dd4",
      "DATA",
      [
        "storage",
        "00c95920",
        null,
        "undefined *"
      ]
    ],
    [
      "00c31de8",
      "READ",
      [
        "storage",
        "00c9b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c31df4",
      "DATA",
      [
        "storage",
        "00c93438",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00c31dd4",
      "DATA",
      [
        "storage",
        "00c95d20",
        null,
        "undefined *"
      ]
    ],
    [
      "00c31de8",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c31df4",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c31980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31960.md#insn-00c31980) · [`00c31990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31960.md#insn-00c31990) · [`00c319a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31960.md#insn-00c319a0)
- 新版 [`00c31da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31d88.md#insn-00c31da8) · [`00c31db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31d88.md#insn-00c31db8) · [`00c31dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c31/00c31d88.md#insn-00c31dc8)

~~~diff
- 00c31980 ["INT_ADD", "register:40f0:8", ["const:c31980:8", "const:4:8"]]
- 00c31980 ["CALL", null, ["callee:00c5eca0:8"]]
+ 00c31da8 ["INT_ADD", "register:40f0:8", ["const:c31da8:8", "const:4:8"]]
+ 00c31da8 ["CALL", null, ["callee:00c5eca0:8"]]
- 00c31980 bytes c8b30094
+ 00c31da8 bytes beb30094
- 00c31990 ["INT_ADD", "register:40f0:8", ["const:c31990:8", "const:4:8"]]
- 00c31990 ["CALL", null, ["callee:00c58090:8"]]
+ 00c31db8 ["INT_ADD", "register:40f0:8", ["const:c31db8:8", "const:4:8"]]
+ 00c31db8 ["CALL", null, ["callee:00c58090:8"]]
- 00c31990 bytes c0980094
+ 00c31db8 bytes b6980094
- 00c319a0 ["INT_ADD", "register:40f0:8", ["const:c319a0:8", "const:4:8"]]
- 00c319a0 ["CALL", null, ["callee:00c5e9f0:8"]]
+ 00c31dc8 ["INT_ADD", "register:40f0:8", ["const:c31dc8:8", "const:4:8"]]
+ 00c31dc8 ["CALL", null, ["callee:00c5e9f0:8"]]
- 00c319a0 bytes 14b30094
+ 00c31dc8 bytes 0ab30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e2a671524095e8af76c938b4d272cce"></a>

### [`00c31c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31c60.md) → [`00c32088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32088.md) _ZNSt6__ndk118__time_get_storageIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4a0.md) · 呼出先 6件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md) [`00c5e600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e600.md) [`00c5e610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e610.md) [`00c5e8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8b0.md)
- 新版 呼出元 1件 [`00c5e8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8a0.md) · 呼出先 6件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea00.md) [`00c5ea10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea10.md) [`00c5ecb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c320d0",
      "incomplete_value": false,
      "site": "00c320d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c31ca8",
      "incomplete_value": false,
      "site": "00c31cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "definition_site": "00c320f0",
      "incomplete_value": true,
      "site": "00c320f4",
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
      "definition_site": "00c31cc8",
      "incomplete_value": true,
      "site": "00c31ccc",
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
      "00c320d4",
      "DATA",
      [
        "storage",
        "00c95920",
        null,
        "undefined *"
      ]
    ],
    [
      "00c320e8",
      "READ",
      [
        "storage",
        "00c9b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c320f4",
      "DATA",
      [
        "storage",
        "00c93438",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00c320d4",
      "DATA",
      [
        "storage",
        "00c95d20",
        null,
        "undefined *"
      ]
    ],
    [
      "00c320e8",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c320f4",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c31c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31c60.md#insn-00c31c80) · [`00c31c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31c60.md#insn-00c31c90) · [`00c31ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31c60.md#insn-00c31ca0)
- 新版 [`00c320a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32088.md#insn-00c320a8) · [`00c320b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32088.md#insn-00c320b8) · [`00c320c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32088.md#insn-00c320c8)

~~~diff
- 00c31c80 ["INT_ADD", "register:40f0:8", ["const:c31c80:8", "const:4:8"]]
- 00c31c80 ["CALL", null, ["callee:00c5ecb0:8"]]
+ 00c320a8 ["INT_ADD", "register:40f0:8", ["const:c320a8:8", "const:4:8"]]
+ 00c320a8 ["CALL", null, ["callee:00c5ecb0:8"]]
- 00c31c80 bytes 0cb30094
+ 00c320a8 bytes 02b30094
- 00c31c90 ["INT_ADD", "register:40f0:8", ["const:c31c90:8", "const:4:8"]]
- 00c31c90 ["CALL", null, ["callee:00c58090:8"]]
+ 00c320b8 ["INT_ADD", "register:40f0:8", ["const:c320b8:8", "const:4:8"]]
+ 00c320b8 ["CALL", null, ["callee:00c58090:8"]]
- 00c31c90 bytes 00980094
+ 00c320b8 bytes f6970094
- 00c31ca0 ["INT_ADD", "register:40f0:8", ["const:c31ca0:8", "const:4:8"]]
- 00c31ca0 ["CALL", null, ["callee:00c5ea10:8"]]
+ 00c320c8 ["INT_ADD", "register:40f0:8", ["const:c320c8:8", "const:4:8"]]
+ 00c320c8 ["CALL", null, ["callee:00c5ea10:8"]]
- 00c31ca0 bytes 5cb20094
+ 00c320c8 bytes 52b20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32ca3e9ac2c0503f704ea9d56bb76e45"></a>

### [`00c32514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c32514.md) → [`00c3293c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c3293c.md) _ZNSt6__ndk110__time_putC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4b0.md) · 呼出先 5件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md)
- 新版 呼出元 1件 [`00c5e8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8b0.md) · 呼出先 5件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c32994",
      "incomplete_value": false,
      "site": "00c329a4",
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
            "const:804:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3256c",
      "incomplete_value": false,
      "site": "00c3257c",
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
            "const:7c4:8"
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
      "00c32994",
      "PARAM",
      [
        "storage",
        "002b27c4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c32994",
      "PARAM",
      [
        "storage",
        "002b2804",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3257c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c32514.md#insn-00c3257c) · [`00c32548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c32514.md#insn-00c32548) · [`00c3256c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c32514.md#insn-00c3256c)
- 新版 [`00c329a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c3293c.md#insn-00c329a4) · [`00c32970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c3293c.md#insn-00c32970) · [`00c32994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c3293c.md#insn-00c32994)

~~~diff
- 00c3257c ["INT_ADD", "register:40f0:8", ["const:c3257c:8", "const:4:8"]]
- 00c3257c ["CALL", null, ["callee:00c580b0:8"]]
+ 00c329a4 ["INT_ADD", "register:40f0:8", ["const:c329a4:8", "const:4:8"]]
+ 00c329a4 ["CALL", null, ["callee:00c580b0:8"]]
- 00c3257c bytes cd950094
+ 00c329a4 bytes c3950094
- 00c32548 ["INT_ADD", "register:40f0:8", ["const:c32548:8", "const:4:8"]]
- 00c32548 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c32970 ["INT_ADD", "register:40f0:8", ["const:c32970:8", "const:4:8"]]
+ 00c32970 ["CALL", null, ["callee:00c5d220:8"]]
- 00c32548 bytes 36aa0094
+ 00c32970 bytes 2caa0094
- 00c3256c ["COPY", "tmp:0:8", ["const:7c4:8"]]
- 00c3256c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c3256c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c3256c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c32994 ["COPY", "tmp:0:8", ["const:804:8"]]
+ 00c32994 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c32994 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c32994 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c3256c bytes 00101f91
+ 00c32994 bytes 00102091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5827b95c1b8317878f2b7f71f8d884b2"></a>

### [`00c325b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c325b0.md) → [`00c329d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c329d8.md) _ZNSt6__ndk110__time_putD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e950.md) · 呼出先 4件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 1件 [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md) · 呼出先 4件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c32a54",
      "incomplete_value": true,
      "site": "00c32a54",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3262c",
      "incomplete_value": true,
      "site": "00c3262c",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c32a0c",
      "incomplete_value": true,
      "site": "00c32a10",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
              ],
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
      "definition_site": "00c325e4",
      "incomplete_value": true,
      "site": "00c325e8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
              ],
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c32a34",
      "incomplete_value": false,
      "site": "00c32a38",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3260c",
      "incomplete_value": false,
      "site": "00c32610",
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
            "const:8a0:8"
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
      "00c329f8",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c32a08",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c32a34",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c329f8",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c32a08",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c32a34",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c32610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c325b0.md#insn-00c32610) · [`00c32628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c325b0.md#insn-00c32628) · [`00c3262c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c325b0.md#insn-00c3262c)
- 新版 [`00c32a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c329d8.md#insn-00c32a38) · [`00c32a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c329d8.md#insn-00c32a50) · [`00c32a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c329d8.md#insn-00c32a54)

~~~diff
- 00c32610 ["INT_ADD", "register:40f0:8", ["const:c32610:8", "const:4:8"]]
- 00c32610 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c32a38 ["INT_ADD", "register:40f0:8", ["const:c32a38:8", "const:4:8"]]
+ 00c32a38 ["CALL", null, ["callee:00c57e50:8"]]
- 00c32610 bytes 10950094
+ 00c32a38 bytes 06950094
- 00c32628 ["INT_ADD", "register:40f0:8", ["const:c32628:8", "const:4:8"]]
- 00c32628 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c32a50 ["INT_ADD", "register:40f0:8", ["const:c32a50:8", "const:4:8"]]
+ 00c32a50 ["CALL", null, ["callee:00c5d220:8"]]
- 00c32628 bytes fea90094
+ 00c32a50 bytes f4a90094
- 00c3262c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:898:8"]]
- 00c3262c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c32a54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c98:8"]]
+ 00c32a54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c3262c bytes a04e04f9
+ 00c32a54 bytes a04e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcc5be98be6bd32b773974c1577f00df"></a>

### [`00c3265c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c3265c.md) → [`00c32a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32a84.md) _ZNSt6__ndk117moneypunct_bynameIcLb0EE4initEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4d0.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00bf1b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md) [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md)
- 新版 呼出元 1件 [`00c5e8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8d0.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.53% / 新版 99.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c32dac",
      "incomplete_value": false,
      "site": "00c32dbc",
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
            "const:7f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c32984",
      "incomplete_value": false,
      "site": "00c32994",
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
            "const:7b9:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c32dac",
      "PARAM",
      [
        "storage",
        "002b17b9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c32dac",
      "PARAM",
      [
        "storage",
        "002b17f9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c32994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c3265c.md#insn-00c32994) · [`00c32688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c3265c.md#insn-00c32688) · [`00c32698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c3265c.md#insn-00c32698)
- 新版 [`00c32dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32a84.md#insn-00c32dbc) · [`00c32ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32a84.md#insn-00c32ab0) · [`00c32ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32a84.md#insn-00c32ac0)

~~~diff
- 00c32994 ["INT_ADD", "register:40f0:8", ["const:c32994:8", "const:4:8"]]
- 00c32994 ["CALL", null, ["callee:00c25934:8"]]
+ 00c32dbc ["INT_ADD", "register:40f0:8", ["const:c32dbc:8", "const:4:8"]]
+ 00c32dbc ["CALL", null, ["callee:00c25934:8"]]
- 00c32994 bytes decaff97
+ 00c32dbc bytes decaff97
- 00c32688 ["INT_ADD", "register:40f0:8", ["const:c32688:8", "const:4:8"]]
- 00c32688 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c32ab0 ["INT_ADD", "register:40f0:8", ["const:c32ab0:8", "const:4:8"]]
+ 00c32ab0 ["CALL", null, ["callee:00c5d220:8"]]
- 00c32688 bytes e6a90094
+ 00c32ab0 bytes dca90094
- 00c32698 ["INT_ADD", "register:40f0:8", ["const:c32698:8", "const:4:8"]]
- 00c32698 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c32ac0 ["INT_ADD", "register:40f0:8", ["const:c32ac0:8", "const:4:8"]]
+ 00c32ac0 ["CALL", null, ["callee:00c5e570:8"]]
- 00c32698 bytes b6ae0094
+ 00c32ac0 bytes acae0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14811bc2864e5e1372bb5e64cec081f4"></a>

### [`00c33358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c33/00c33358.md) → [`00c33780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33780.md) _ZNSt6__ndk117moneypunct_bynameIwLb0EE4initEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4f0.md) · 呼出先 17件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`006d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d76a4.md) [`00bf1b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md) [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md) [`00c2c170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c170.md)
- 新版 呼出元 1件 [`00c5e8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8f0.md) · 呼出先 17件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`006d76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76e4.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c2c598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c598.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.35% / 新版 99.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c33e38",
      "incomplete_value": false,
      "site": "00c33e3c",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c33a10",
      "incomplete_value": false,
      "site": "00c33a14",
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
            "const:d18:8"
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
      "definition_site": "00c33e50",
      "incomplete_value": true,
      "site": "00c33e60",
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
            "const:7f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c33a28",
      "incomplete_value": true,
      "site": "00c33a38",
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
            "const:7b9:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c33e7c",
      "incomplete_value": false,
      "site": "00c33e80",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c33a54",
      "incomplete_value": false,
      "site": "00c33a58",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c33e38",
      "PARAM",
      [
        "storage",
        "0029fd18",
        null,
        "string"
      ]
    ],
    [
      "00c33e50",
      "PARAM",
      [
        "storage",
        "002b17b9",
        null,
        "string"
      ]
    ],
    [
      "00c33e7c",
      "PARAM",
      [
        "storage",
        "0029fd18",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c33e38",
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ],
    [
      "00c33e50",
      "PARAM",
      [
        "storage",
        "002b17f9",
        null,
        "string"
      ]
    ],
    [
      "00c33e7c",
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c33a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c33/00c33358.md#insn-00c33a14) · [`00c33a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c33/00c33358.md#insn-00c33a38) · [`00c33a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c33/00c33358.md#insn-00c33a58)
- 新版 [`00c33e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33780.md#insn-00c33e3c) · [`00c33e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33780.md#insn-00c33e60) · [`00c33e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33780.md#insn-00c33e80)

~~~diff
- 00c33a14 ["INT_ADD", "register:40f0:8", ["const:c33a14:8", "const:4:8"]]
- 00c33a14 ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c33e3c ["INT_ADD", "register:40f0:8", ["const:c33e3c:8", "const:4:8"]]
+ 00c33e3c ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c33a14 bytes 67a80094
+ 00c33e3c bytes 5da80094
- 00c33a38 ["INT_ADD", "register:40f0:8", ["const:c33a38:8", "const:4:8"]]
- 00c33a38 ["CALL", null, ["callee:00c25934:8"]]
+ 00c33e60 ["INT_ADD", "register:40f0:8", ["const:c33e60:8", "const:4:8"]]
+ 00c33e60 ["CALL", null, ["callee:00c25934:8"]]
- 00c33a38 bytes b5c6ff97
+ 00c33e60 bytes b5c6ff97
- 00c33a58 ["INT_ADD", "register:40f0:8", ["const:c33a58:8", "const:4:8"]]
- 00c33a58 ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c33e80 ["INT_ADD", "register:40f0:8", ["const:c33e80:8", "const:4:8"]]
+ 00c33e80 ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c33a58 bytes 56a80094
+ 00c33e80 bytes 4ca80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-953a2b6a091b7266a06661a2f3824c17"></a>

### [`00c34054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34054.md) → [`00c3447c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c3447c.md) _ZNSt6__ndk117moneypunct_bynameIwLb1EE4initEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e500.md) · 呼出先 17件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`006d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d76a4.md) [`00bf1b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md) [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md) [`00c2c170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c170.md)
- 新版 呼出元 1件 [`00c5e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e900.md) · 呼出先 17件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`006d76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76e4.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c2c598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c598.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.35% / 新版 99.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c34b34",
      "incomplete_value": false,
      "site": "00c34b38",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3470c",
      "incomplete_value": false,
      "site": "00c34710",
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
            "const:d18:8"
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
      "definition_site": "00c34b4c",
      "incomplete_value": false,
      "site": "00c34b5c",
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
            "const:7f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c34724",
      "incomplete_value": false,
      "site": "00c34734",
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
            "const:7b9:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c34b78",
      "incomplete_value": false,
      "site": "00c34b7c",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c34750",
      "incomplete_value": false,
      "site": "00c34754",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c34b34",
      "PARAM",
      [
        "storage",
        "0029fd18",
        null,
        "string"
      ]
    ],
    [
      "00c34b4c",
      "PARAM",
      [
        "storage",
        "002b17b9",
        null,
        "string"
      ]
    ],
    [
      "00c34b78",
      "PARAM",
      [
        "storage",
        "0029fd18",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c34b34",
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ],
    [
      "00c34b4c",
      "PARAM",
      [
        "storage",
        "002b17f9",
        null,
        "string"
      ]
    ],
    [
      "00c34b78",
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c34710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34054.md#insn-00c34710) · [`00c34734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34054.md#insn-00c34734) · [`00c34754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34054.md#insn-00c34754)
- 新版 [`00c34b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c3447c.md#insn-00c34b38) · [`00c34b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c3447c.md#insn-00c34b5c) · [`00c34b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c3447c.md#insn-00c34b7c)

~~~diff
- 00c34710 ["INT_ADD", "register:40f0:8", ["const:c34710:8", "const:4:8"]]
- 00c34710 ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c34b38 ["INT_ADD", "register:40f0:8", ["const:c34b38:8", "const:4:8"]]
+ 00c34b38 ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c34710 bytes 28a50094
+ 00c34b38 bytes 1ea50094
- 00c34734 ["INT_ADD", "register:40f0:8", ["const:c34734:8", "const:4:8"]]
- 00c34734 ["CALL", null, ["callee:00c25934:8"]]
+ 00c34b5c ["INT_ADD", "register:40f0:8", ["const:c34b5c:8", "const:4:8"]]
+ 00c34b5c ["CALL", null, ["callee:00c25934:8"]]
- 00c34734 bytes 76c3ff97
+ 00c34b5c bytes 76c3ff97
- 00c34754 ["INT_ADD", "register:40f0:8", ["const:c34754:8", "const:4:8"]]
- 00c34754 ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c34b7c ["INT_ADD", "register:40f0:8", ["const:c34b7c:8", "const:4:8"]]
+ 00c34b7c ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c34754 bytes 17a50094
+ 00c34b7c bytes 0da50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea5d04f5dfad14d0e36880eb920e8bba"></a>

### [`00c34994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34994.md) → [`00c34dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34dbc.md) _ZNSt6__ndk17codecvtIwc9mbstate_tED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md) [`00c5e710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e710.md) · 呼出先 5件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 2件 [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md) [`00c5eb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eb10.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 68.29% / 新版 68.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c34de4",
      "incomplete_value": true,
      "site": "00c34de8",
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
      "definition_site": "00c349bc",
      "incomplete_value": true,
      "site": "00c349c0",
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
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c34e4c",
      "incomplete_value": true,
      "site": "00c34e4c",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c34a24",
      "incomplete_value": true,
      "site": "00c34a24",
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
            "const:898:8"
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
      "definition_site": "00c34e00",
      "incomplete_value": true,
      "site": "00c34e04",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
              ],
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
      "definition_site": "00c349d8",
      "incomplete_value": true,
      "site": "00c349dc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
              ],
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
      "00c34ddc",
      "READ",
      [
        "storage",
        "00c9b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00c34de8",
      "DATA",
      [
        "storage",
        "00c934c0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c34df4",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c34ddc",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00c34de8",
      "DATA",
      [
        "storage",
        "00c938c0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c34df4",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c34a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34994.md#insn-00c34a08) · [`00c34a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34994.md#insn-00c34a20) · [`00c34a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34994.md#insn-00c34a24)
- 新版 [`00c34e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34dbc.md#insn-00c34e30) · [`00c34e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34dbc.md#insn-00c34e48) · [`00c34e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34dbc.md#insn-00c34e4c)

~~~diff
- 00c34a08 ["INT_ADD", "register:40f0:8", ["const:c34a08:8", "const:4:8"]]
- 00c34a08 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c34e30 ["INT_ADD", "register:40f0:8", ["const:c34e30:8", "const:4:8"]]
+ 00c34e30 ["CALL", null, ["callee:00c57e50:8"]]
- 00c34a08 bytes 128c0094
+ 00c34e30 bytes 088c0094
- 00c34a20 ["INT_ADD", "register:40f0:8", ["const:c34a20:8", "const:4:8"]]
- 00c34a20 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c34e48 ["INT_ADD", "register:40f0:8", ["const:c34e48:8", "const:4:8"]]
+ 00c34e48 ["CALL", null, ["callee:00c5d220:8"]]
- 00c34a20 bytes 00a10094
+ 00c34e48 bytes f6a00094
- 00c34a24 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:898:8"]]
- 00c34a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c34e4c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c98:8"]]
+ 00c34e4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c34a24 bytes a04e04f9
+ 00c34e4c bytes a04e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5defb350746b7085b6d5c200c552db01"></a>

### [`00c35018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35018.md) → [`00c35440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35440.md) FUN_00c35440

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c350ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c350ac.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 1件 [`00c354d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c354d4.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c35460",
      "incomplete_value": true,
      "site": "00c35464",
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
      "definition_site": "00c35038",
      "incomplete_value": true,
      "site": "00c3503c",
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
      "00c35458",
      "READ",
      [
        "storage",
        "00c9b998",
        null,
        "pointer"
      ]
    ],
    [
      "00c35464",
      "DATA",
      [
        "storage",
        "00c95000",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c35458",
      "READ",
      [
        "storage",
        "00c9bd98",
        null,
        "pointer"
      ]
    ],
    [
      "00c35464",
      "DATA",
      [
        "storage",
        "00c95400",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c35030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35018.md#insn-00c35030) · [`00c35060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35018.md#insn-00c35060) · [`00c3507c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35018.md#insn-00c3507c)
- 新版 [`00c35458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35440.md#insn-00c35458) · [`00c35488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35440.md#insn-00c35488) · [`00c354a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35440.md#insn-00c354a4)

~~~diff
- 00c35030 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:998:8"]]
- 00c35030 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c35458 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
+ 00c35458 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c35030 bytes 08cd44f9
+ 00c35458 bytes 08cd46f9
- 00c35060 ["INT_ADD", "register:40f0:8", ["const:c35060:8", "const:4:8"]]
- 00c35060 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c35488 ["INT_ADD", "register:40f0:8", ["const:c35488:8", "const:4:8"]]
+ 00c35488 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c35060 bytes 948a0094
+ 00c35488 bytes 8a8a0094
- 00c3507c ["INT_ADD", "register:40f0:8", ["const:c3507c:8", "const:4:8"]]
- 00c3507c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c354a4 ["INT_ADD", "register:40f0:8", ["const:c354a4:8", "const:4:8"]]
+ 00c354a4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c3507c bytes 8d8a0094
+ 00c354a4 bytes 838a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c989c10a66d63337412ad175eb3e8de1"></a>

### [`00c350d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c350d8.md) → [`00c35500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35500.md) FUN_00c35500

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3516c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3516c.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 1件 [`00c35594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35594.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c35520",
      "incomplete_value": true,
      "site": "00c35524",
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
      "definition_site": "00c350f8",
      "incomplete_value": true,
      "site": "00c350fc",
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
      "00c35518",
      "READ",
      [
        "storage",
        "00c9b9a0",
        null,
        "pointer"
      ]
    ],
    [
      "00c35524",
      "DATA",
      [
        "storage",
        "00c95088",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c35518",
      "READ",
      [
        "storage",
        "00c9bda0",
        null,
        "pointer"
      ]
    ],
    [
      "00c35524",
      "DATA",
      [
        "storage",
        "00c95488",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c350f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c350d8.md#insn-00c350f0) · [`00c35120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c350d8.md#insn-00c35120) · [`00c3513c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c350d8.md#insn-00c3513c)
- 新版 [`00c35518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35500.md#insn-00c35518) · [`00c35548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35500.md#insn-00c35548) · [`00c35564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35500.md#insn-00c35564)

~~~diff
- 00c350f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a0:8"]]
- 00c350f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c35518 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
+ 00c35518 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c350f0 bytes 08d144f9
+ 00c35518 bytes 08d146f9
- 00c35120 ["INT_ADD", "register:40f0:8", ["const:c35120:8", "const:4:8"]]
- 00c35120 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c35548 ["INT_ADD", "register:40f0:8", ["const:c35548:8", "const:4:8"]]
+ 00c35548 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c35120 bytes 648a0094
+ 00c35548 bytes 5a8a0094
- 00c3513c ["INT_ADD", "register:40f0:8", ["const:c3513c:8", "const:4:8"]]
- 00c3513c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c35564 ["INT_ADD", "register:40f0:8", ["const:c35564:8", "const:4:8"]]
+ 00c35564 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c3513c bytes 5d8a0094
+ 00c35564 bytes 538a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba4611882f82683efe87542b6c1e4f66"></a>

### [`00c35198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35198.md) → [`00c355c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c355c0.md) FUN_00c355c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3522c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3522c.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 1件 [`00c35654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35654.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c355e0",
      "incomplete_value": true,
      "site": "00c355e4",
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
      "definition_site": "00c351b8",
      "incomplete_value": true,
      "site": "00c351bc",
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
      "00c355d8",
      "READ",
      [
        "storage",
        "00c9b9a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c355e4",
      "DATA",
      [
        "storage",
        "00c95110",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c355d8",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00c355e4",
      "DATA",
      [
        "storage",
        "00c95510",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c351b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35198.md#insn-00c351b0) · [`00c351e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35198.md#insn-00c351e0) · [`00c351fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35198.md#insn-00c351fc)
- 新版 [`00c355d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c355c0.md#insn-00c355d8) · [`00c35608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c355c0.md#insn-00c35608) · [`00c35624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c355c0.md#insn-00c35624)

~~~diff
- 00c351b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 00c351b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c355d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da8:8"]]
+ 00c355d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c351b0 bytes 08d544f9
+ 00c355d8 bytes 08d546f9
- 00c351e0 ["INT_ADD", "register:40f0:8", ["const:c351e0:8", "const:4:8"]]
- 00c351e0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c35608 ["INT_ADD", "register:40f0:8", ["const:c35608:8", "const:4:8"]]
+ 00c35608 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c351e0 bytes 348a0094
+ 00c35608 bytes 2a8a0094
- 00c351fc ["INT_ADD", "register:40f0:8", ["const:c351fc:8", "const:4:8"]]
- 00c351fc ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c35624 ["INT_ADD", "register:40f0:8", ["const:c35624:8", "const:4:8"]]
+ 00c35624 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c351fc bytes 2d8a0094
+ 00c35624 bytes 238a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb6df8d849775a227753bd662d2a4ce"></a>

### [`00c354a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354a8.md) → [`00c358d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358d0.md) FUN_00c358d0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c244ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c244ac.md) [`00c354c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354c0.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`00c248d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c248d4.md) [`00c358e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358e8.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00c358e0",
      "incomplete_value": false,
      "site": "00c358e4",
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
      "definition_site": "00c354b8",
      "incomplete_value": false,
      "site": "00c354bc",
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
      "00c358e0",
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
      "00c358e0",
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

- 旧版 [`00c354bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354a8.md#insn-00c354bc) · [`00c354b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354a8.md#insn-00c354b8)
- 新版 [`00c358e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358d0.md#insn-00c358e4) · [`00c358e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358d0.md#insn-00c358e0)

~~~diff
- 00c354bc ["INT_ADD", "register:40f0:8", ["const:c354bc:8", "const:4:8"]]
- 00c354bc ["CALL", null, ["callee:0043b778:8"]]
+ 00c358e4 ["INT_ADD", "register:40f0:8", ["const:c358e4:8", "const:4:8"]]
+ 00c358e4 ["CALL", null, ["callee:0043b778:8"]]
- 00c354bc bytes 9f18e097
+ 00c358e4 bytes a517e097
- 00c354b8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00c354b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c354b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c354b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c358e0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00c358e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c358e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c358e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c354b8 bytes 00303c91
+ 00c358e0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-896a239bf9bdd8fb4accc6c2166a0639"></a>

### [`00c35778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35778.md) → [`00c35ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ba0.md) FUN_00c35ba0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c2c6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c6b4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c2cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cadc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c35bbc",
      "incomplete_value": true,
      "site": "00c35bc0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1128000:8"
              ],
              [
                "leaf",
                "const:f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35794",
      "incomplete_value": true,
      "site": "00c35798",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
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
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c35bd4",
      "incomplete_value": true,
      "site": "00c35bd8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1128000:8"
              ],
              [
                "leaf",
                "const:d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c357ac",
      "incomplete_value": true,
      "site": "00c357b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:cd8:8"
              ]
            ]
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
      "definition_site": "00c35bec",
      "incomplete_value": true,
      "site": "00c35bf0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1128000:8"
              ],
              [
                "leaf",
                "const:c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c357c4",
      "incomplete_value": true,
      "site": "00c357c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
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
      "00c35bb0",
      "READ",
      [
        "storage",
        "01127ce0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c35bbc",
      "READ",
      [
        "storage",
        "01127cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c35bc8",
      "READ",
      [
        "storage",
        "01127cc8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c35bb0",
      "READ",
      [
        "storage",
        "011280e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c35bbc",
      "READ",
      [
        "storage",
        "011280f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c35bc8",
      "READ",
      [
        "storage",
        "011280c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c35798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35778.md#insn-00c35798) · [`00c357b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35778.md#insn-00c357b0) · [`00c357c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35778.md#insn-00c357c8)
- 新版 [`00c35bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ba0.md#insn-00c35bc0) · [`00c35bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ba0.md#insn-00c35bd8) · [`00c35bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ba0.md#insn-00c35bf0)

~~~diff
- 00c35798 ["INT_ADD", "register:40f0:8", ["const:c35798:8", "const:4:8"]]
- 00c35798 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c35bc0 ["INT_ADD", "register:40f0:8", ["const:c35bc0:8", "const:4:8"]]
+ 00c35bc0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c35798 bytes c6880094
+ 00c35bc0 bytes bc880094
- 00c357b0 ["INT_ADD", "register:40f0:8", ["const:c357b0:8", "const:4:8"]]
- 00c357b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c35bd8 ["INT_ADD", "register:40f0:8", ["const:c35bd8:8", "const:4:8"]]
+ 00c35bd8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c357b0 bytes c0880094
+ 00c35bd8 bytes b6880094
- 00c357c8 ["INT_ADD", "register:40f0:8", ["const:c357c8:8", "const:4:8"]]
- 00c357c8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c35bf0 ["INT_ADD", "register:40f0:8", ["const:c35bf0:8", "const:4:8"]]
+ 00c35bf0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00c357c8 bytes ba880094
+ 00c35bf0 bytes b0880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c23e7fdf70282fec29d11d44b83cd99c"></a>

### [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) → [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) FUN_00c35fb8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 96件 [`00c07464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07464.md) [`00c0a10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a10c.md) [`00c0a93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md) [`00c0d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md) [`00c0dc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0dc64.md) · 呼出先 1件 [`00c53880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53880.md)
- 新版 呼出元 96件 [`00c0788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c0788c.md) [`00c0a534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a534.md) [`00c0ad64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ad64.md) [`00c0d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d9a8.md) [`00c0e08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0e08c.md) · 呼出先 1件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c35fdc",
      "incomplete_value": true,
      "site": "00c35fe0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35bb4",
      "incomplete_value": true,
      "site": "00c35bb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a08:8"
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
      "00c35fdc",
      "READ",
      [
        "storage",
        "00c9ba08",
        null,
        "pointer"
      ]
    ],
    [
      "00c35fdc",
      "PARAM",
      [
        "storage",
        "01127a00",
        "_ZNSt6__ndk16locale2id9__next_idE",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00c35fdc",
      "READ",
      [
        "storage",
        "00c9be08",
        null,
        "pointer"
      ]
    ],
    [
      "00c35fdc",
      "PARAM",
      [
        "storage",
        "01127e00",
        "_ZNSt6__ndk16locale2id9__next_idE",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c35bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md#insn-00c35bb8) · [`00c35bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md#insn-00c35bb4)
- 新版 [`00c35fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md#insn-00c35fe0) · [`00c35fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md#insn-00c35fdc)

~~~diff
- 00c35bb8 ["INT_ADD", "register:40f0:8", ["const:c35bb8:8", "const:4:8"]]
- 00c35bb8 ["CALL", null, ["callee:00c53ca0:8"]]
+ 00c35fe0 ["INT_ADD", "register:40f0:8", ["const:c35fe0:8", "const:4:8"]]
+ 00c35fe0 ["CALL", null, ["callee:00c53ca0:8"]]
- 00c35bb8 bytes 32770094
+ 00c35fe0 bytes 30770094
- 00c35bb4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:a08:8"]]
- 00c35bb4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c35fdc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e08:8"]]
+ 00c35fdc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00c35bb4 bytes 210445f9
+ 00c35fdc bytes 210447f9
~~~


<a id="compare-9f065946533255f03f90200dfbd633ec"></a>

### [`00c35bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35bd4.md) → [`00c35ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ffc.md) FUN_00c35ffc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3601c",
      "incomplete_value": true,
      "site": "00c36020",
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
      "definition_site": "00c35bf4",
      "incomplete_value": true,
      "site": "00c35bf8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c36034",
      "incomplete_value": true,
      "site": "00c36038",
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
      "definition_site": "00c35c0c",
      "incomplete_value": true,
      "site": "00c35c10",
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
      "00c36014",
      "READ",
      [
        "storage",
        "00c9b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c36020",
      "DATA",
      [
        "storage",
        "00c933d0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c3602c",
      "READ",
      [
        "storage",
        "00c9b9c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c36014",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c36020",
      "DATA",
      [
        "storage",
        "00c937d0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c3602c",
      "READ",
      [
        "storage",
        "00c9bdc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c35bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35bd4.md#insn-00c35bec) · [`00c35bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35bd4.md#insn-00c35bfc) · [`00c35c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35bd4.md#insn-00c35c04)
- 新版 [`00c36014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ffc.md#insn-00c36014) · [`00c36024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ffc.md#insn-00c36024) · [`00c3602c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35ffc.md#insn-00c3602c)

~~~diff
- 00c35bec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00c35bec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c36014 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00c36014 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c35bec bytes 08e944f9
+ 00c36014 bytes 08e946f9
- 00c35bfc ["INT_ADD", "register:40f0:8", ["const:c35bfc:8", "const:4:8"]]
- 00c35bfc ["CALL", null, ["callee:00c5d1d0:8"]]
+ 00c36024 ["INT_ADD", "register:40f0:8", ["const:c36024:8", "const:4:8"]]
+ 00c36024 ["CALL", null, ["callee:00c5d1d0:8"]]
- 00c35bfc bytes 759c0094
+ 00c36024 bytes 6b9c0094
- 00c35c04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9c8:8"]]
- 00c35c04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c3602c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc8:8"]]
+ 00c3602c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c35c04 bytes 08e544f9
+ 00c3602c bytes 08e546f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-622a4592f974683eb8d329081c5f50ce"></a>

### [`00c35c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c44.md) → [`00c3606c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3606c.md) FUN_00c3606c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md) [`00c5e600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e600.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md) [`00c5ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ea00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3608c",
      "incomplete_value": true,
      "site": "00c36090",
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
      "definition_site": "00c35c64",
      "incomplete_value": true,
      "site": "00c35c68",
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
      "00c36084",
      "READ",
      [
        "storage",
        "00c9b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c36090",
      "DATA",
      [
        "storage",
        "00c93438",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00c36084",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c36090",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c35c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c44.md#insn-00c35c5c) · [`00c35c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c44.md#insn-00c35c6c) · [`00c35c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c44.md#insn-00c35c74)
- 新版 [`00c36084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3606c.md#insn-00c36084) · [`00c36094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3606c.md#insn-00c36094) · [`00c3609c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3606c.md#insn-00c3609c)

~~~diff
- 00c35c5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d8:8"]]
- 00c35c5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c36084 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
+ 00c36084 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c35c5c bytes 08ed44f9
+ 00c36084 bytes 08ed46f9
- 00c35c6c ["INT_ADD", "register:40f0:8", ["const:c35c6c:8", "const:4:8"]]
- 00c35c6c ["CALL", null, ["callee:00c5d1d0:8"]]
+ 00c36094 ["INT_ADD", "register:40f0:8", ["const:c36094:8", "const:4:8"]]
+ 00c36094 ["CALL", null, ["callee:00c5d1d0:8"]]
- 00c35c6c bytes 599c0094
+ 00c36094 bytes 4f9c0094
- 00c35c74 ["INT_ADD", "register:40f0:8", ["const:c35c74:8", "const:4:8"]]
- 00c35c74 ["CALL", null, ["callee:00c5ea00:8"]]
+ 00c3609c ["INT_ADD", "register:40f0:8", ["const:c3609c:8", "const:4:8"]]
+ 00c3609c ["CALL", null, ["callee:00c5ea00:8"]]
- 00c35c74 bytes 63a20094
+ 00c3609c bytes 59a20094
~~~


<a id="compare-b703d5fee45b3194ab47a2753860dec0"></a>

### [`00c35d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35d44.md) → [`00c3616c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3616c.md) FUN_00c3616c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c07b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07b64.md) [`00c0b044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0b044.md) · 呼出先 5件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5cd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd50.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 2件 [`00c07f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07f8c.md) [`00c0b46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b46c.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d150.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 86.76% / 新版 86.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36268",
      "incomplete_value": true,
      "site": "00c36268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35e40",
      "incomplete_value": true,
      "site": "00c35e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c361c4",
      "incomplete_value": true,
      "site": "00c361d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35d9c",
      "incomplete_value": true,
      "site": "00c35dac",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:898:8"
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
      "definition_site": "00c36248",
      "incomplete_value": false,
      "site": "00c3624c",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35e20",
      "incomplete_value": false,
      "site": "00c35e24",
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
            "const:8a0:8"
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
      "00c361bc",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c361c4",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36248",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c361bc",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c361c4",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36248",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c35dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35d44.md#insn-00c35dac) · [`00c35e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35d44.md#insn-00c35e24) · [`00c35e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35d44.md#insn-00c35e3c)
- 新版 [`00c361d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3616c.md#insn-00c361d4) · [`00c3624c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3616c.md#insn-00c3624c) · [`00c36264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3616c.md#insn-00c36264)

~~~diff
- 00c35dac ["INT_ADD", "register:40f0:8", ["const:c35dac:8", "const:4:8"]]
- 00c35dac ["CALL", null, ["callee:00c5d150:8"]]
+ 00c361d4 ["INT_ADD", "register:40f0:8", ["const:c361d4:8", "const:4:8"]]
+ 00c361d4 ["CALL", null, ["callee:00c5d150:8"]]
- 00c35dac bytes e99b0094
+ 00c361d4 bytes df9b0094
- 00c35e24 ["INT_ADD", "register:40f0:8", ["const:c35e24:8", "const:4:8"]]
- 00c35e24 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c3624c ["INT_ADD", "register:40f0:8", ["const:c3624c:8", "const:4:8"]]
+ 00c3624c ["CALL", null, ["callee:00c57e50:8"]]
- 00c35e24 bytes 0b870094
+ 00c3624c bytes 01870094
- 00c35e3c ["INT_ADD", "register:40f0:8", ["const:c35e3c:8", "const:4:8"]]
- 00c35e3c ["CALL", null, ["callee:00c5d220:8"]]
+ 00c36264 ["INT_ADD", "register:40f0:8", ["const:c36264:8", "const:4:8"]]
+ 00c36264 ["CALL", null, ["callee:00c5d220:8"]]
- 00c35e3c bytes f99b0094
+ 00c36264 bytes ef9b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a39b9d5fc752ba0b1fe04bbf7ecedf45"></a>

### [`00c35e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35e6c.md) → [`00c36294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36294.md) FUN_00c36294

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c07fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07fa0.md) [`00c0b474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0b474.md) · 呼出先 5件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5cd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd50.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 2件 [`00c083c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c083c8.md) [`00c0b89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b89c.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d150.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36390",
      "incomplete_value": true,
      "site": "00c36390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35f68",
      "incomplete_value": true,
      "site": "00c35f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c362ec",
      "incomplete_value": true,
      "site": "00c362fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35ec4",
      "incomplete_value": true,
      "site": "00c35ed4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:898:8"
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
      "definition_site": "00c36370",
      "incomplete_value": false,
      "site": "00c36374",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c35f48",
      "incomplete_value": false,
      "site": "00c35f4c",
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
            "const:8a0:8"
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
      "00c362e4",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c362ec",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36370",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c362e4",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c362ec",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36370",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c35ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35e6c.md#insn-00c35ed4) · [`00c35f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35e6c.md#insn-00c35f4c) · [`00c35f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35e6c.md#insn-00c35f64)
- 新版 [`00c362fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36294.md#insn-00c362fc) · [`00c36374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36294.md#insn-00c36374) · [`00c3638c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36294.md#insn-00c3638c)

~~~diff
- 00c35ed4 ["INT_ADD", "register:40f0:8", ["const:c35ed4:8", "const:4:8"]]
- 00c35ed4 ["CALL", null, ["callee:00c5d150:8"]]
+ 00c362fc ["INT_ADD", "register:40f0:8", ["const:c362fc:8", "const:4:8"]]
+ 00c362fc ["CALL", null, ["callee:00c5d150:8"]]
- 00c35ed4 bytes 9f9b0094
+ 00c362fc bytes 959b0094
- 00c35f4c ["INT_ADD", "register:40f0:8", ["const:c35f4c:8", "const:4:8"]]
- 00c35f4c ["CALL", null, ["callee:00c57e50:8"]]
+ 00c36374 ["INT_ADD", "register:40f0:8", ["const:c36374:8", "const:4:8"]]
+ 00c36374 ["CALL", null, ["callee:00c57e50:8"]]
- 00c35f4c bytes c1860094
+ 00c36374 bytes b7860094
- 00c35f64 ["INT_ADD", "register:40f0:8", ["const:c35f64:8", "const:4:8"]]
- 00c35f64 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c3638c ["INT_ADD", "register:40f0:8", ["const:c3638c:8", "const:4:8"]]
+ 00c3638c ["CALL", null, ["callee:00c5d220:8"]]
- 00c35f64 bytes af9b0094
+ 00c3638c bytes a59b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db823a1fb995bf3248f4c4b03c314732"></a>

### [`00c35f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35f94.md) → [`00c363bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c363bc.md) FUN_00c363bc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c083dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c08/00c083dc.md) [`00c0b8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0b8a4.md) · 呼出先 5件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5cd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd60.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 2件 [`00c08804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08804.md) [`00c0bccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0bccc.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d160.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c364e8",
      "incomplete_value": true,
      "site": "00c364e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c360c0",
      "incomplete_value": true,
      "site": "00c360c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36430",
      "incomplete_value": true,
      "site": "00c36440",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
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
    "old": {
      "definition_site": "00c36008",
      "incomplete_value": true,
      "site": "00c36018",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:898:8"
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
      "definition_site": "00c364c8",
      "incomplete_value": false,
      "site": "00c364cc",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c360a0",
      "incomplete_value": false,
      "site": "00c360a4",
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
            "const:8a0:8"
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
      "00c36428",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36430",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c364c8",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c36428",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36430",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c364c8",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35f94.md#insn-00c36018) · [`00c360a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35f94.md#insn-00c360a4) · [`00c360bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35f94.md#insn-00c360bc)
- 新版 [`00c36440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c363bc.md#insn-00c36440) · [`00c364cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c363bc.md#insn-00c364cc) · [`00c364e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c363bc.md#insn-00c364e4)

~~~diff
- 00c36018 ["INT_ADD", "register:40f0:8", ["const:c36018:8", "const:4:8"]]
- 00c36018 ["CALL", null, ["callee:00c5d160:8"]]
+ 00c36440 ["INT_ADD", "register:40f0:8", ["const:c36440:8", "const:4:8"]]
+ 00c36440 ["CALL", null, ["callee:00c5d160:8"]]
- 00c36018 bytes 529b0094
+ 00c36440 bytes 489b0094
- 00c360a4 ["INT_ADD", "register:40f0:8", ["const:c360a4:8", "const:4:8"]]
- 00c360a4 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c364cc ["INT_ADD", "register:40f0:8", ["const:c364cc:8", "const:4:8"]]
+ 00c364cc ["CALL", null, ["callee:00c57e50:8"]]
- 00c360a4 bytes 6b860094
+ 00c364cc bytes 61860094
- 00c360bc ["INT_ADD", "register:40f0:8", ["const:c360bc:8", "const:4:8"]]
- 00c360bc ["CALL", null, ["callee:00c5d220:8"]]
+ 00c364e4 ["INT_ADD", "register:40f0:8", ["const:c364e4:8", "const:4:8"]]
+ 00c364e4 ["CALL", null, ["callee:00c5d220:8"]]
- 00c360bc bytes 599b0094
+ 00c364e4 bytes 4f9b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7ca1ddd43bc70ed2841133d9ad34021"></a>

### [`00c360ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c360ec.md) → [`00c36514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36514.md) FUN_00c36514

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c08818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c08/00c08818.md) [`00c0bcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0bcd4.md) · 呼出先 5件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5cd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd60.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 2件 [`00c08c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08c40.md) [`00c0c0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c0fc.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d160.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c3663c",
      "incomplete_value": true,
      "site": "00c3663c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36214",
      "incomplete_value": true,
      "site": "00c36214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36588",
      "incomplete_value": true,
      "site": "00c36598",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
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
    "old": {
      "definition_site": "00c36160",
      "incomplete_value": true,
      "site": "00c36170",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:898:8"
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
      "definition_site": "00c3661c",
      "incomplete_value": false,
      "site": "00c36620",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c361f4",
      "incomplete_value": false,
      "site": "00c361f8",
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
            "const:8a0:8"
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
      "00c36580",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36588",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c3661c",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c36580",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36588",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c3661c",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c360ec.md#insn-00c36170) · [`00c361f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c360ec.md#insn-00c361f8) · [`00c36210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c360ec.md#insn-00c36210)
- 新版 [`00c36598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36514.md#insn-00c36598) · [`00c36620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36514.md#insn-00c36620) · [`00c36638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36514.md#insn-00c36638)

~~~diff
- 00c36170 ["INT_ADD", "register:40f0:8", ["const:c36170:8", "const:4:8"]]
- 00c36170 ["CALL", null, ["callee:00c5d160:8"]]
+ 00c36598 ["INT_ADD", "register:40f0:8", ["const:c36598:8", "const:4:8"]]
+ 00c36598 ["CALL", null, ["callee:00c5d160:8"]]
- 00c36170 bytes fc9a0094
+ 00c36598 bytes f29a0094
- 00c361f8 ["INT_ADD", "register:40f0:8", ["const:c361f8:8", "const:4:8"]]
- 00c361f8 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c36620 ["INT_ADD", "register:40f0:8", ["const:c36620:8", "const:4:8"]]
+ 00c36620 ["CALL", null, ["callee:00c57e50:8"]]
- 00c361f8 bytes 16860094
+ 00c36620 bytes 0c860094
- 00c36210 ["INT_ADD", "register:40f0:8", ["const:c36210:8", "const:4:8"]]
- 00c36210 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c36638 ["INT_ADD", "register:40f0:8", ["const:c36638:8", "const:4:8"]]
+ 00c36638 ["CALL", null, ["callee:00c5d220:8"]]
- 00c36210 bytes 049b0094
+ 00c36638 bytes fa9a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-116a18886912cd2ffd601ce45d8b7e09"></a>

### [`00c36240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36240.md) → [`00c36668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36668.md) FUN_00c36668

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c08c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c08/00c08c54.md) [`00c0c104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0c104.md) · 呼出先 5件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5cd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd60.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 2件 [`00c0907c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c0907c.md) [`00c0c52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c52c.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d160.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36784",
      "incomplete_value": true,
      "site": "00c36784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3635c",
      "incomplete_value": true,
      "site": "00c3635c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c366dc",
      "incomplete_value": true,
      "site": "00c366ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
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
    "old": {
      "definition_site": "00c362b4",
      "incomplete_value": true,
      "site": "00c362c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:898:8"
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
      "definition_site": "00c36764",
      "incomplete_value": false,
      "site": "00c36768",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3633c",
      "incomplete_value": false,
      "site": "00c36340",
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
            "const:8a0:8"
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
      "00c366d4",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c366dc",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36764",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c366d4",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c366dc",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36764",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c362c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36240.md#insn-00c362c4) · [`00c36340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36240.md#insn-00c36340) · [`00c36358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36240.md#insn-00c36358)
- 新版 [`00c366ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36668.md#insn-00c366ec) · [`00c36768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36668.md#insn-00c36768) · [`00c36780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36668.md#insn-00c36780)

~~~diff
- 00c362c4 ["INT_ADD", "register:40f0:8", ["const:c362c4:8", "const:4:8"]]
- 00c362c4 ["CALL", null, ["callee:00c5d160:8"]]
+ 00c366ec ["INT_ADD", "register:40f0:8", ["const:c366ec:8", "const:4:8"]]
+ 00c366ec ["CALL", null, ["callee:00c5d160:8"]]
- 00c362c4 bytes a79a0094
+ 00c366ec bytes 9d9a0094
- 00c36340 ["INT_ADD", "register:40f0:8", ["const:c36340:8", "const:4:8"]]
- 00c36340 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c36768 ["INT_ADD", "register:40f0:8", ["const:c36768:8", "const:4:8"]]
+ 00c36768 ["CALL", null, ["callee:00c57e50:8"]]
- 00c36340 bytes c4850094
+ 00c36768 bytes ba850094
- 00c36358 ["INT_ADD", "register:40f0:8", ["const:c36358:8", "const:4:8"]]
- 00c36358 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c36780 ["INT_ADD", "register:40f0:8", ["const:c36780:8", "const:4:8"]]
+ 00c36780 ["CALL", null, ["callee:00c5d220:8"]]
- 00c36358 bytes b29a0094
+ 00c36780 bytes a89a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c30dd0c6a1b50e99caafff8da7a7909"></a>

### [`00c36388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36388.md) → [`00c367b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c367b0.md) FUN_00c367b0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c09090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c09090.md) [`00c0c534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0c534.md) · 呼出先 5件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5cd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd60.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 2件 [`00c094b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c094b8.md) [`00c0c95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c95c.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d160.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c368cc",
      "incomplete_value": true,
      "site": "00c368cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c364a4",
      "incomplete_value": true,
      "site": "00c364a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36824",
      "incomplete_value": true,
      "site": "00c36834",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
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
    "old": {
      "definition_site": "00c363fc",
      "incomplete_value": true,
      "site": "00c3640c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:898:8"
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
      "definition_site": "00c368ac",
      "incomplete_value": false,
      "site": "00c368b0",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36484",
      "incomplete_value": false,
      "site": "00c36488",
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
            "const:8a0:8"
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
      "00c3681c",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36824",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c368ac",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c3681c",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36824",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c368ac",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3640c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36388.md#insn-00c3640c) · [`00c36488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36388.md#insn-00c36488) · [`00c364a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36388.md#insn-00c364a0)
- 新版 [`00c36834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c367b0.md#insn-00c36834) · [`00c368b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c367b0.md#insn-00c368b0) · [`00c368c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c367b0.md#insn-00c368c8)

~~~diff
- 00c3640c ["INT_ADD", "register:40f0:8", ["const:c3640c:8", "const:4:8"]]
- 00c3640c ["CALL", null, ["callee:00c5d160:8"]]
+ 00c36834 ["INT_ADD", "register:40f0:8", ["const:c36834:8", "const:4:8"]]
+ 00c36834 ["CALL", null, ["callee:00c5d160:8"]]
- 00c3640c bytes 559a0094
+ 00c36834 bytes 4b9a0094
- 00c36488 ["INT_ADD", "register:40f0:8", ["const:c36488:8", "const:4:8"]]
- 00c36488 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c368b0 ["INT_ADD", "register:40f0:8", ["const:c368b0:8", "const:4:8"]]
+ 00c368b0 ["CALL", null, ["callee:00c57e50:8"]]
- 00c36488 bytes 72850094
+ 00c368b0 bytes 68850094
- 00c364a0 ["INT_ADD", "register:40f0:8", ["const:c364a0:8", "const:4:8"]]
- 00c364a0 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c368c8 ["INT_ADD", "register:40f0:8", ["const:c368c8:8", "const:4:8"]]
+ 00c368c8 ["CALL", null, ["callee:00c5d220:8"]]
- 00c364a0 bytes 609a0094
+ 00c368c8 bytes 569a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ed9dc68c7c7151c0c8ac6d3a375c5c8"></a>

### [`00c364d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c364d0.md) → [`00c368f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c368f8.md) FUN_00c368f8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c094cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c094cc.md) [`00c0c964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0c964.md) · 呼出先 5件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c581b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581b0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 2件 [`00c098f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c098f4.md) [`00c0cd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0cd8c.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c585b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585b0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.19% / 新版 92.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c369e4",
      "incomplete_value": false,
      "site": "00c369e4",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c365bc",
      "incomplete_value": false,
      "site": "00c365bc",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c369c0",
      "incomplete_value": false,
      "site": "00c369c4",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36598",
      "incomplete_value": false,
      "site": "00c3659c",
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
            "const:8a0:8"
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
      "definition_site": "00c369d0",
      "incomplete_value": false,
      "site": "00c369dc",
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
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c365a8",
      "incomplete_value": false,
      "site": "00c365b4",
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
            "const:13c:8"
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
      "00c3693c",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c369c0",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c369d0",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3693c",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c369c0",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c369d0",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3659c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c364d0.md#insn-00c3659c) · [`00c365b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c364d0.md#insn-00c365b4) · [`00c365bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c364d0.md#insn-00c365bc)
- 新版 [`00c369c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c368f8.md#insn-00c369c4) · [`00c369dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c368f8.md#insn-00c369dc) · [`00c369e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c368f8.md#insn-00c369e4)

~~~diff
- 00c3659c ["INT_ADD", "register:40f0:8", ["const:c3659c:8", "const:4:8"]]
- 00c3659c ["CALL", null, ["callee:00c57e50:8"]]
+ 00c369c4 ["INT_ADD", "register:40f0:8", ["const:c369c4:8", "const:4:8"]]
+ 00c369c4 ["CALL", null, ["callee:00c57e50:8"]]
- 00c3659c bytes 2d850094
+ 00c369c4 bytes 23850094
- 00c365b4 ["INT_ADD", "register:40f0:8", ["const:c365b4:8", "const:4:8"]]
- 00c365b4 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c369dc ["INT_ADD", "register:40f0:8", ["const:c369dc:8", "const:4:8"]]
+ 00c369dc ["CALL", null, ["callee:00c5d220:8"]]
- 00c365b4 bytes 1b9a0094
+ 00c369dc bytes 119a0094
- 00c365bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:898:8"]]
- 00c365bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c369e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
+ 00c369e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c365bc bytes 004d04f9
+ 00c369e4 bytes 004d06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13aad440c66ecee3322574557d1fccb5"></a>

### [`00c365e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c365e8.md) → [`00c36a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36a10.md) FUN_00c36a10

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c098e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c098e4.md) [`00c0cd70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0cd70.md) · 呼出先 5件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c581c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581c0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 2件 [`00c09d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c09d0c.md) [`00c0d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d198.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c585c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585c0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36afc",
      "incomplete_value": false,
      "site": "00c36afc",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c366d4",
      "incomplete_value": false,
      "site": "00c366d4",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36ad8",
      "incomplete_value": false,
      "site": "00c36adc",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c366b0",
      "incomplete_value": false,
      "site": "00c366b4",
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
            "const:8a0:8"
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
      "definition_site": "00c36ae8",
      "incomplete_value": false,
      "site": "00c36af4",
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
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c366c0",
      "incomplete_value": false,
      "site": "00c366cc",
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
            "const:13c:8"
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
      "00c36a54",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36ad8",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36ae8",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c36a54",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36ad8",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36ae8",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c366b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c365e8.md#insn-00c366b4) · [`00c366cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c365e8.md#insn-00c366cc) · [`00c366d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c365e8.md#insn-00c366d4)
- 新版 [`00c36adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36a10.md#insn-00c36adc) · [`00c36af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36a10.md#insn-00c36af4) · [`00c36afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36a10.md#insn-00c36afc)

~~~diff
- 00c366b4 ["INT_ADD", "register:40f0:8", ["const:c366b4:8", "const:4:8"]]
- 00c366b4 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c36adc ["INT_ADD", "register:40f0:8", ["const:c36adc:8", "const:4:8"]]
+ 00c36adc ["CALL", null, ["callee:00c57e50:8"]]
- 00c366b4 bytes e7840094
+ 00c36adc bytes dd840094
- 00c366cc ["INT_ADD", "register:40f0:8", ["const:c366cc:8", "const:4:8"]]
- 00c366cc ["CALL", null, ["callee:00c5d220:8"]]
+ 00c36af4 ["INT_ADD", "register:40f0:8", ["const:c36af4:8", "const:4:8"]]
+ 00c36af4 ["CALL", null, ["callee:00c5d220:8"]]
- 00c366cc bytes d5990094
+ 00c36af4 bytes cb990094
- 00c366d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:898:8"]]
- 00c366d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c36afc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
+ 00c36afc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c366d4 bytes 004d04f9
+ 00c36afc bytes 004d06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8652aeb3e0fe6c6242f8553d4b98686"></a>

### [`00c36700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36700.md) → [`00c36b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36b28.md) FUN_00c36b28

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c09cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c09cfc.md) [`00c0d17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d17c.md) · 呼出先 5件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md) [`00c5e960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e960.md)
- 新版 呼出元 2件 [`00c0a124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a124.md) [`00c0d5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d5a4.md) · 呼出先 5件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5ed60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 85.07% / 新版 85.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c36c20",
      "incomplete_value": true,
      "site": "00c36c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c367f8",
      "incomplete_value": true,
      "site": "00c367f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c36c00",
      "incomplete_value": false,
      "site": "00c36c04",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c367d8",
      "incomplete_value": false,
      "site": "00c367dc",
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
            "const:8a0:8"
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
      "definition_site": "00c36c10",
      "incomplete_value": false,
      "site": "00c36c1c",
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
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c367e8",
      "incomplete_value": false,
      "site": "00c367f4",
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
            "const:13c:8"
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
      "00c36b74",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36b7c",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36bb4",
      "READ",
      [
        "storage",
        "002c2f00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c36b74",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c36b7c",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c36bb4",
      "READ",
      [
        "storage",
        "002c2f40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c367dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36700.md#insn-00c367dc) · [`00c367f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36700.md#insn-00c367f4) · [`00c367f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36700.md#insn-00c367f8)
- 新版 [`00c36c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36b28.md#insn-00c36c04) · [`00c36c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36b28.md#insn-00c36c1c) · [`00c36c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36b28.md#insn-00c36c20)

~~~diff
- 00c367dc ["INT_ADD", "register:40f0:8", ["const:c367dc:8", "const:4:8"]]
- 00c367dc ["CALL", null, ["callee:00c57e50:8"]]
+ 00c36c04 ["INT_ADD", "register:40f0:8", ["const:c36c04:8", "const:4:8"]]
+ 00c36c04 ["CALL", null, ["callee:00c57e50:8"]]
- 00c367dc bytes 9d840094
+ 00c36c04 bytes 93840094
- 00c367f4 ["INT_ADD", "register:40f0:8", ["const:c367f4:8", "const:4:8"]]
- 00c367f4 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c36c1c ["INT_ADD", "register:40f0:8", ["const:c36c1c:8", "const:4:8"]]
+ 00c36c1c ["CALL", null, ["callee:00c5d220:8"]]
- 00c367f4 bytes 8b990094
+ 00c36c1c bytes 81990094
- 00c367f8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:898:8"]]
- 00c367f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c36c20 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c98:8"]]
+ 00c36c20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c367f8 bytes 004f04f9
+ 00c36c20 bytes 004f06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2df880ca4a98f25c2a81654e883ffb08"></a>

### [`00c36c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36c84.md) → [`00c370ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c370ac.md) _ZNSt6__ndk111__call_onceERVmPvPFvS2_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md) · 呼出先 4件 [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md) [`00c5ddc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddc0.md) [`00c5ddd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddd0.md)
- 新版 呼出元 1件 [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md) · 呼出先 4件 [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1c0.md) [`00c5e1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c370d0",
      "incomplete_value": false,
      "site": "00c370dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36ca8",
      "incomplete_value": false,
      "site": "00c36cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "definition_site": "00c37154",
      "incomplete_value": false,
      "site": "00c37158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36d2c",
      "incomplete_value": false,
      "site": "00c36d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "definition_site": "00c37168",
      "incomplete_value": false,
      "site": "00c3716c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36d40",
      "incomplete_value": false,
      "site": "00c36d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "00c370d0",
      "PARAM",
      [
        "storage",
        "011285b0",
        null,
        null
      ]
    ],
    [
      "00c370fc",
      "PARAM",
      [
        "storage",
        "011285d8",
        null,
        null
      ]
    ],
    [
      "00c37100",
      "PARAM",
      [
        "storage",
        "011285b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c370d0",
      "PARAM",
      [
        "storage",
        "011289b0",
        null,
        null
      ]
    ],
    [
      "00c370fc",
      "PARAM",
      [
        "storage",
        "011289d8",
        null,
        null
      ]
    ],
    [
      "00c37100",
      "PARAM",
      [
        "storage",
        "011289b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36c84.md#insn-00c36cb4) · [`00c36d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36c84.md#insn-00c36d30) · [`00c36d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36c84.md#insn-00c36d44)
- 新版 [`00c370dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c370ac.md#insn-00c370dc) · [`00c37158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c370ac.md#insn-00c37158) · [`00c3716c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c370ac.md#insn-00c3716c)

~~~diff
- 00c36cb4 ["INT_ADD", "register:40f0:8", ["const:c36cb4:8", "const:4:8"]]
- 00c36cb4 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00c370dc ["INT_ADD", "register:40f0:8", ["const:c370dc:8", "const:4:8"]]
+ 00c370dc ["CALL", null, ["callee:00c5b6a0:8"]]
- 00c36cb4 bytes 7b910094
+ 00c370dc bytes 71910094
- 00c36d30 ["INT_ADD", "register:40f0:8", ["const:c36d30:8", "const:4:8"]]
- 00c36d30 ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00c37158 ["INT_ADD", "register:40f0:8", ["const:c37158:8", "const:4:8"]]
+ 00c37158 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00c36d30 bytes 60910094
+ 00c37158 bytes 56910094
- 00c36d44 ["INT_ADD", "register:40f0:8", ["const:c36d44:8", "const:4:8"]]
- 00c36d44 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00c3716c ["INT_ADD", "register:40f0:8", ["const:c3716c:8", "const:4:8"]]
+ 00c3716c ["CALL", null, ["callee:00c5b6a0:8"]]
- 00c36d44 bytes 57910094
+ 00c3716c bytes 4d910094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d565ffdbf70363ed61a643ef936a033"></a>

### [`00c36d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36d98.md) → [`00c371c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c371c0.md) FUN_00c371c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md) [`00c5ddc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddc0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c371e0",
      "incomplete_value": false,
      "site": "00c371e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36db8",
      "incomplete_value": false,
      "site": "00c36dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "definition_site": "00c371f4",
      "incomplete_value": false,
      "site": "00c371f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36dcc",
      "incomplete_value": false,
      "site": "00c36dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "definition_site": "00c37200",
      "incomplete_value": false,
      "site": "00c37204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36dd8",
      "incomplete_value": false,
      "site": "00c36ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c371e0",
      "PARAM",
      [
        "storage",
        "011285b0",
        null,
        null
      ]
    ],
    [
      "00c371f4",
      "PARAM",
      [
        "storage",
        "011285b0",
        null,
        null
      ]
    ],
    [
      "00c37200",
      "PARAM",
      [
        "storage",
        "011285d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c371e0",
      "PARAM",
      [
        "storage",
        "011289b0",
        null,
        null
      ]
    ],
    [
      "00c371f4",
      "PARAM",
      [
        "storage",
        "011289b0",
        null,
        null
      ]
    ],
    [
      "00c37200",
      "PARAM",
      [
        "storage",
        "011289d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36d98.md#insn-00c36dbc) · [`00c36dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36d98.md#insn-00c36dd0) · [`00c36ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36d98.md#insn-00c36ddc)
- 新版 [`00c371e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c371c0.md#insn-00c371e4) · [`00c371f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c371c0.md#insn-00c371f8) · [`00c37204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c371c0.md#insn-00c37204)

~~~diff
- 00c36dbc ["INT_ADD", "register:40f0:8", ["const:c36dbc:8", "const:4:8"]]
- 00c36dbc ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00c371e4 ["INT_ADD", "register:40f0:8", ["const:c371e4:8", "const:4:8"]]
+ 00c371e4 ["CALL", null, ["callee:00c5b6a0:8"]]
- 00c36dbc bytes 39910094
+ 00c371e4 bytes 2f910094
- 00c36dd0 ["INT_ADD", "register:40f0:8", ["const:c36dd0:8", "const:4:8"]]
- 00c36dd0 ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00c371f8 ["INT_ADD", "register:40f0:8", ["const:c371f8:8", "const:4:8"]]
+ 00c371f8 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00c36dd0 bytes 38910094
+ 00c371f8 bytes 2e910094
- 00c36ddc ["INT_ADD", "register:40f0:8", ["const:c36ddc:8", "const:4:8"]]
- 00c36ddc ["CALL", null, ["callee:00c5e1c0:8"]]
+ 00c37204 ["INT_ADD", "register:40f0:8", ["const:c37204:8", "const:4:8"]]
+ 00c37204 ["CALL", null, ["callee:00c5e1c0:8"]]
- 00c36ddc bytes f99b0094
+ 00c37204 bytes ef9b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9724343d9550eb7b7024cabc1c88e652"></a>

### [`00c36e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e94.md) → [`00c372bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c372bc.md) _ZNSt6__ndk120__get_collation_nameEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a400.md) · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)
- 新版 呼出元 1件 [`00c5a800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a800.md) · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c37320",
      "incomplete_value": true,
      "site": "00c37328",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
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
      "definition_site": "00c36ef8",
      "incomplete_value": true,
      "site": "00c36f00",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c372f4",
      "READ",
      [
        "storage",
        "00c95d48",
        null,
        "pointer"
      ]
    ],
    [
      "00c372f4",
      "PARAM",
      [
        "storage",
        "002b6fcd",
        null,
        "string"
      ]
    ],
    [
      "00c372f4",
      "READ",
      [
        "storage",
        "00c95b88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c372f4",
      "READ",
      [
        "storage",
        "00c96148",
        null,
        "pointer"
      ]
    ],
    [
      "00c372f4",
      "PARAM",
      [
        "storage",
        "002b700d",
        null,
        "string"
      ]
    ],
    [
      "00c372f4",
      "READ",
      [
        "storage",
        "00c95f88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e94.md#insn-00c36ebc) · [`00c36ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e94.md#insn-00c36ed0) · [`00c36ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e94.md#insn-00c36ef0)
- 新版 [`00c372e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c372bc.md#insn-00c372e4) · [`00c372f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c372bc.md#insn-00c372f8) · [`00c37318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c372bc.md#insn-00c37318)

~~~diff
- 00c36ebc ["COPY", "register:40a8:8", ["const:c959d8:8"]]
+ 00c372e4 ["COPY", "register:40a8:8", ["const:c95dd8:8"]]
- 00c36ebc bytes f5582f10
+ 00c372e4 bytes b5572f10
- 00c36ed0 ["INT_ADD", "register:40f0:8", ["const:c36ed0:8", "const:4:8"]]
- 00c36ed0 ["CALL", null, ["callee:00c5b850:8"]]
+ 00c372f8 ["INT_ADD", "register:40f0:8", ["const:c372f8:8", "const:4:8"]]
+ 00c372f8 ["CALL", null, ["callee:00c5b850:8"]]
- 00c36ed0 bytes 60910094
+ 00c372f8 bytes 56910094
- 00c36ef0 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 00c36ef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c36ef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c36ef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c37318 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 00c37318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c37318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c37318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c36ef0 bytes 08210391
+ 00c37318 bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23f93826b4eb612dff6bf594a3802166"></a>

### [`00c36f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36f3c.md) → [`00c37364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37364.md) _ZNSt6__ndk115__get_classnameEPKcb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a410.md) · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)
- 新版 呼出元 1件 [`00c5a810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a810.md) · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c373c4",
      "incomplete_value": true,
      "site": "00c373c8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
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
      "definition_site": "00c36f9c",
      "incomplete_value": true,
      "site": "00c36fa0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3739c",
      "READ",
      [
        "storage",
        "00c96138",
        null,
        "pointer"
      ]
    ],
    [
      "00c3739c",
      "PARAM",
      [
        "storage",
        "002b37bf",
        null,
        "string"
      ]
    ],
    [
      "00c3739c",
      "READ",
      [
        "storage",
        "00c960f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c3739c",
      "READ",
      [
        "storage",
        "00c96538",
        null,
        "pointer"
      ]
    ],
    [
      "00c3739c",
      "PARAM",
      [
        "storage",
        "002b37ff",
        null,
        "string"
      ]
    ],
    [
      "00c3739c",
      "READ",
      [
        "storage",
        "00c964f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36f3c.md#insn-00c36f64) · [`00c36f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36f3c.md#insn-00c36f78) · [`00c36f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36f3c.md#insn-00c36f98)
- 新版 [`00c3738c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37364.md#insn-00c3738c) · [`00c373a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37364.md#insn-00c373a0) · [`00c373c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37364.md#insn-00c373c0)

~~~diff
- 00c36f64 ["COPY", "register:40a8:8", ["const:c960c8:8"]]
+ 00c3738c ["COPY", "register:40a8:8", ["const:c964c8:8"]]
- 00c36f64 bytes 358b2f10
+ 00c3738c bytes f5892f10
- 00c36f78 ["INT_ADD", "register:40f0:8", ["const:c36f78:8", "const:4:8"]]
- 00c36f78 ["CALL", null, ["callee:00c5b850:8"]]
+ 00c373a0 ["INT_ADD", "register:40f0:8", ["const:c373a0:8", "const:4:8"]]
+ 00c373a0 ["CALL", null, ["callee:00c5b850:8"]]
- 00c36f78 bytes 36910094
+ 00c373a0 bytes 2c910094
- 00c36f98 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 00c36f98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c36f98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c36f98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c373c0 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00c373c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c373c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c373c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c36f98 bytes 08e10691
+ 00c373c0 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-463d7b5b83009bfbcad8e7228f9e44af"></a>

### [`00c370a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c370a0.md) → [`00c374c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c374c8.md) __cxa_bad_cast

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c598e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598e0.md) · 呼出先 4件 [`00c37b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b44.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5e080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e080.md)
- 新版 呼出元 1件 [`00c59ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ce0.md) · 呼出先 4件 [`00c37f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f6c.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5e480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e480.md)

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
      "definition_site": "00c374f4",
      "incomplete_value": true,
      "site": "00c374fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c370cc",
      "incomplete_value": true,
      "site": "00c370d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:760:8"
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
      "definition_site": "00c374f8",
      "incomplete_value": true,
      "site": "00c374fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c370d0",
      "incomplete_value": true,
      "site": "00c370d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:768:8"
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
      "00c374f4",
      "READ",
      [
        "storage",
        "00c9b760",
        null,
        "pointer"
      ]
    ],
    [
      "00c374f4",
      "PARAM",
      [
        "storage",
        "00c96588",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c374f8",
      "READ",
      [
        "storage",
        "00c9b768",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c374f4",
      "READ",
      [
        "storage",
        "00c9bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00c374f4",
      "PARAM",
      [
        "storage",
        "00c96988",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c374f8",
      "READ",
      [
        "storage",
        "00c9bb68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c370d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c370a0.md#insn-00c370d4) · [`00c370b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c370a0.md#insn-00c370b4) · [`00c370bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c370a0.md#insn-00c370bc)
- 新版 [`00c374fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c374c8.md#insn-00c374fc) · [`00c374dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c374c8.md#insn-00c374dc) · [`00c374e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c374c8.md#insn-00c374e4)

~~~diff
- 00c370d4 ["INT_ADD", "register:40f0:8", ["const:c370d4:8", "const:4:8"]]
- 00c370d4 ["CALL", null, ["callee:00c57f10:8"]]
+ 00c374fc ["INT_ADD", "register:40f0:8", ["const:c374fc:8", "const:4:8"]]
+ 00c374fc ["CALL", null, ["callee:00c57f10:8"]]
- 00c370d4 bytes 8f820094
+ 00c374fc bytes 85820094
- 00c370b4 ["INT_ADD", "register:40f0:8", ["const:c370b4:8", "const:4:8"]]
- 00c370b4 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00c374dc ["INT_ADD", "register:40f0:8", ["const:c374dc:8", "const:4:8"]]
+ 00c374dc ["CALL", null, ["callee:00c57ef0:8"]]
- 00c370b4 bytes 8f820094
+ 00c374dc bytes 85820094
- 00c370bc ["INT_ADD", "register:40f0:8", ["const:c370bc:8", "const:4:8"]]
- 00c370bc ["CALL", null, ["callee:00c5e480:8"]]
+ 00c374e4 ["INT_ADD", "register:40f0:8", ["const:c374e4:8", "const:4:8"]]
+ 00c374e4 ["CALL", null, ["callee:00c5e480:8"]]
- 00c370bc bytes f19b0094
+ 00c374e4 bytes e79b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38d8ccaa65031548182ede48435d4e3b"></a>

### [`00c370d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c370d8.md) → [`00c37500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37500.md) __cxa_bad_typeid

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c37ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ba0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5e970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e970.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c37fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37fc8.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5ed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed70.md)

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
      "definition_site": "00c3752c",
      "incomplete_value": true,
      "site": "00c37534",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37104",
      "incomplete_value": true,
      "site": "00c3710c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a18:8"
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
      "definition_site": "00c37530",
      "incomplete_value": true,
      "site": "00c37534",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37108",
      "incomplete_value": true,
      "site": "00c3710c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c3752c",
      "READ",
      [
        "storage",
        "00c9ba18",
        null,
        "pointer"
      ]
    ],
    [
      "00c3752c",
      "PARAM",
      [
        "storage",
        "00c965a0",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c37530",
      "READ",
      [
        "storage",
        "00c9ba20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c3752c",
      "READ",
      [
        "storage",
        "00c9be18",
        null,
        "pointer"
      ]
    ],
    [
      "00c3752c",
      "PARAM",
      [
        "storage",
        "00c969a0",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c37530",
      "READ",
      [
        "storage",
        "00c9be20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3710c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c370d8.md#insn-00c3710c) · [`00c370ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c370d8.md#insn-00c370ec) · [`00c370f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c370d8.md#insn-00c370f4)
- 新版 [`00c37534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37500.md#insn-00c37534) · [`00c37514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37500.md#insn-00c37514) · [`00c3751c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37500.md#insn-00c3751c)

~~~diff
- 00c3710c ["INT_ADD", "register:40f0:8", ["const:c3710c:8", "const:4:8"]]
- 00c3710c ["CALL", null, ["callee:00c57f10:8"]]
+ 00c37534 ["INT_ADD", "register:40f0:8", ["const:c37534:8", "const:4:8"]]
+ 00c37534 ["CALL", null, ["callee:00c57f10:8"]]
- 00c3710c bytes 81820094
+ 00c37534 bytes 77820094
- 00c370ec ["INT_ADD", "register:40f0:8", ["const:c370ec:8", "const:4:8"]]
- 00c370ec ["CALL", null, ["callee:00c57ef0:8"]]
+ 00c37514 ["INT_ADD", "register:40f0:8", ["const:c37514:8", "const:4:8"]]
+ 00c37514 ["CALL", null, ["callee:00c57ef0:8"]]
- 00c370ec bytes 81820094
+ 00c37514 bytes 77820094
- 00c370f4 ["INT_ADD", "register:40f0:8", ["const:c370f4:8", "const:4:8"]]
- 00c370f4 ["CALL", null, ["callee:00c5ed70:8"]]
+ 00c3751c ["INT_ADD", "register:40f0:8", ["const:c3751c:8", "const:4:8"]]
+ 00c3751c ["CALL", null, ["callee:00c5ed70:8"]]
- 00c370f4 bytes 1f9e0094
+ 00c3751c bytes 159e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ad59b4ea1c4ae5fdbe39bbd0a55b5b"></a>

### [`00c37110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37110.md) → [`00c37538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37538.md) __cxa_throw_bad_array_new_length

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58030.md)

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
      "definition_site": "00c37564",
      "incomplete_value": true,
      "site": "00c3756c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3713c",
      "incomplete_value": true,
      "site": "00c37144",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
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
      "definition_site": "00c37568",
      "incomplete_value": true,
      "site": "00c3756c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37140",
      "incomplete_value": true,
      "site": "00c37144",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
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
      "00c37564",
      "READ",
      [
        "storage",
        "00c9a7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c37564",
      "PARAM",
      [
        "storage",
        "00c962b0",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c37568",
      "READ",
      [
        "storage",
        "00c9a7d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c37564",
      "READ",
      [
        "storage",
        "00c9abd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c37564",
      "PARAM",
      [
        "storage",
        "00c966b0",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c37568",
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37110.md#insn-00c37144) · [`00c37124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37110.md#insn-00c37124) · [`00c3712c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37110.md#insn-00c3712c)
- 新版 [`00c3756c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37538.md#insn-00c3756c) · [`00c3754c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37538.md#insn-00c3754c) · [`00c37554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37538.md#insn-00c37554)

~~~diff
- 00c37144 ["INT_ADD", "register:40f0:8", ["const:c37144:8", "const:4:8"]]
- 00c37144 ["CALL", null, ["callee:00c57f10:8"]]
+ 00c3756c ["INT_ADD", "register:40f0:8", ["const:c3756c:8", "const:4:8"]]
+ 00c3756c ["CALL", null, ["callee:00c57f10:8"]]
- 00c37144 bytes 73820094
+ 00c3756c bytes 69820094
- 00c37124 ["INT_ADD", "register:40f0:8", ["const:c37124:8", "const:4:8"]]
- 00c37124 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00c3754c ["INT_ADD", "register:40f0:8", ["const:c3754c:8", "const:4:8"]]
+ 00c3754c ["CALL", null, ["callee:00c57ef0:8"]]
- 00c37124 bytes 73820094
+ 00c3754c bytes 69820094
- 00c3712c ["INT_ADD", "register:40f0:8", ["const:c3712c:8", "const:4:8"]]
- 00c3712c ["CALL", null, ["callee:00c58030:8"]]
+ 00c37554 ["INT_ADD", "register:40f0:8", ["const:c37554:8", "const:4:8"]]
+ 00c37554 ["CALL", null, ["callee:00c58030:8"]]
- 00c3712c bytes c1820094
+ 00c37554 bytes b7820094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37636279f4f21a6959a07d42d943a2bb"></a>

### [`00c37148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37148.md) → [`00c37570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37570.md) __cxa_guard_acquire

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) · 呼出先 5件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md) [`00c5ddd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddd0.md) [`00c5e9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9b0.md)
- 新版 呼出元 1件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) · 呼出先 5件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1d0.md) [`00c5edb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5edb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 83.78% / 新版 83.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c375a4",
      "incomplete_value": false,
      "site": "00c375b0",
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
            "const:e76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3717c",
      "incomplete_value": false,
      "site": "00c37188",
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
            "const:e36:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c375ac",
      "incomplete_value": false,
      "site": "00c375b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37184",
      "incomplete_value": false,
      "site": "00c3718c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00c37634",
      "incomplete_value": false,
      "site": "00c37638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3720c",
      "incomplete_value": false,
      "site": "00c37210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c375ac",
      "PARAM",
      [
        "storage",
        "01128608",
        null,
        null
      ]
    ],
    [
      "00c375b0",
      "DATA",
      [
        "storage",
        "002b7e36",
        null,
        "string"
      ]
    ],
    [
      "00c375fc",
      "PARAM",
      [
        "storage",
        "01128630",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c375ac",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c375b0",
      "DATA",
      [
        "storage",
        "002b7e76",
        null,
        "string"
      ]
    ],
    [
      "00c375fc",
      "PARAM",
      [
        "storage",
        "01128a30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3718c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37148.md#insn-00c3718c) · [`00c37210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37148.md#insn-00c37210) · [`00c37260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37148.md#insn-00c37260)
- 新版 [`00c375b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37570.md#insn-00c375b4) · [`00c37638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37570.md#insn-00c37638) · [`00c37688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37570.md#insn-00c37688)

~~~diff
- 00c3718c ["INT_ADD", "register:40f0:8", ["const:c3718c:8", "const:4:8"]]
- 00c3718c ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00c375b4 ["INT_ADD", "register:40f0:8", ["const:c375b4:8", "const:4:8"]]
+ 00c375b4 ["CALL", null, ["callee:00c5b6a0:8"]]
- 00c3718c bytes 45900094
+ 00c375b4 bytes 3b900094
- 00c37210 ["INT_ADD", "register:40f0:8", ["const:c37210:8", "const:4:8"]]
- 00c37210 ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00c37638 ["INT_ADD", "register:40f0:8", ["const:c37638:8", "const:4:8"]]
+ 00c37638 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00c37210 bytes 28900094
+ 00c37638 bytes 1e900094
- 00c37260 ["INT_ADD", "register:40f0:8", ["const:c37260:8", "const:4:8"]]
- 00c37260 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c37688 ["INT_ADD", "register:40f0:8", ["const:c37688:8", "const:4:8"]]
+ 00c37688 ["CALL", null, ["callee:00c3800c:8"]]
- 00c37260 bytes 61020094
+ 00c37688 bytes 61020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07e82f2a5f0744e6d7d35a8790feccba"></a>

### [`00c3728c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3728c.md) → [`00c376b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c376b4.md) __cxa_guard_release

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) · 呼出先 4件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md) [`00c5ddc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddc0.md)
- 新版 呼出元 1件 [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) · 呼出先 4件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.49% / 新版 80.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c376d8",
      "incomplete_value": false,
      "site": "00c376dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c372b0",
      "incomplete_value": false,
      "site": "00c372b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00c376f0",
      "incomplete_value": false,
      "site": "00c376f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c372c8",
      "incomplete_value": false,
      "site": "00c372cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00c37704",
      "incomplete_value": false,
      "site": "00c37708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c372dc",
      "incomplete_value": false,
      "site": "00c372e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "00c376d8",
      "PARAM",
      [
        "storage",
        "01128608",
        null,
        null
      ]
    ],
    [
      "00c376f0",
      "PARAM",
      [
        "storage",
        "01128608",
        null,
        null
      ]
    ],
    [
      "00c37704",
      "PARAM",
      [
        "storage",
        "01128630",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c376d8",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c376f0",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c37704",
      "PARAM",
      [
        "storage",
        "01128a30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c372b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3728c.md#insn-00c372b4) · [`00c372cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3728c.md#insn-00c372cc) · [`00c372e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3728c.md#insn-00c372e0)
- 新版 [`00c376dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c376b4.md#insn-00c376dc) · [`00c376f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c376b4.md#insn-00c376f4) · [`00c37708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c376b4.md#insn-00c37708)

~~~diff
- 00c372b4 ["INT_ADD", "register:40f0:8", ["const:c372b4:8", "const:4:8"]]
- 00c372b4 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00c376dc ["INT_ADD", "register:40f0:8", ["const:c376dc:8", "const:4:8"]]
+ 00c376dc ["CALL", null, ["callee:00c5b6a0:8"]]
- 00c372b4 bytes fb8f0094
+ 00c376dc bytes f18f0094
- 00c372cc ["INT_ADD", "register:40f0:8", ["const:c372cc:8", "const:4:8"]]
- 00c372cc ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00c376f4 ["INT_ADD", "register:40f0:8", ["const:c376f4:8", "const:4:8"]]
+ 00c376f4 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00c372cc bytes f98f0094
+ 00c376f4 bytes ef8f0094
- 00c372e0 ["INT_ADD", "register:40f0:8", ["const:c372e0:8", "const:4:8"]]
- 00c372e0 ["CALL", null, ["callee:00c5e1c0:8"]]
+ 00c37708 ["INT_ADD", "register:40f0:8", ["const:c37708:8", "const:4:8"]]
+ 00c37708 ["CALL", null, ["callee:00c5e1c0:8"]]
- 00c372e0 bytes b89a0094
+ 00c37708 bytes ae9a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a285dc1344cc89e2a1245d02d00046c8"></a>

### [`00c37334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37334.md) → [`00c3775c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c3775c.md) __cxa_guard_abort

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b90.md) · 呼出先 4件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md) [`00c5ddc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddc0.md)
- 新版 呼出元 1件 [`00c57f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f90.md) · 呼出先 4件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md) [`00c5e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37774",
      "incomplete_value": false,
      "site": "00c37778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3734c",
      "incomplete_value": false,
      "site": "00c37350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00c37790",
      "incomplete_value": false,
      "site": "00c37794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37368",
      "incomplete_value": false,
      "site": "00c3736c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00c377a4",
      "incomplete_value": false,
      "site": "00c377a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3737c",
      "incomplete_value": false,
      "site": "00c37380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "00c37774",
      "PARAM",
      [
        "storage",
        "01128608",
        null,
        null
      ]
    ],
    [
      "00c37790",
      "PARAM",
      [
        "storage",
        "01128608",
        null,
        null
      ]
    ],
    [
      "00c377a4",
      "PARAM",
      [
        "storage",
        "01128630",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c37774",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c37790",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c377a4",
      "PARAM",
      [
        "storage",
        "01128a30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37334.md#insn-00c37350) · [`00c3736c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37334.md#insn-00c3736c) · [`00c37380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37334.md#insn-00c37380)
- 新版 [`00c37778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c3775c.md#insn-00c37778) · [`00c37794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c3775c.md#insn-00c37794) · [`00c377a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c3775c.md#insn-00c377a8)

~~~diff
- 00c37350 ["INT_ADD", "register:40f0:8", ["const:c37350:8", "const:4:8"]]
- 00c37350 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00c37778 ["INT_ADD", "register:40f0:8", ["const:c37778:8", "const:4:8"]]
+ 00c37778 ["CALL", null, ["callee:00c5b6a0:8"]]
- 00c37350 bytes d48f0094
+ 00c37778 bytes ca8f0094
- 00c3736c ["INT_ADD", "register:40f0:8", ["const:c3736c:8", "const:4:8"]]
- 00c3736c ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00c37794 ["INT_ADD", "register:40f0:8", ["const:c37794:8", "const:4:8"]]
+ 00c37794 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00c3736c bytes d18f0094
+ 00c37794 bytes c78f0094
- 00c37380 ["INT_ADD", "register:40f0:8", ["const:c37380:8", "const:4:8"]]
- 00c37380 ["CALL", null, ["callee:00c5e1c0:8"]]
+ 00c377a8 ["INT_ADD", "register:40f0:8", ["const:c377a8:8", "const:4:8"]]
+ 00c377a8 ["CALL", null, ["callee:00c5e1c0:8"]]
- 00c37380 bytes 909a0094
+ 00c377a8 bytes 869a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43dd9cbe4db781f2ef30e4b865a4bcdc"></a>

### [`00c373d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c373d0.md) → [`00c377f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c377f8.md) FUN_00c377f8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37810",
      "incomplete_value": false,
      "site": "00c37814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c373e8",
      "incomplete_value": false,
      "site": "00c373ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00c37834",
      "incomplete_value": true,
      "site": "00c37838",
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
            "const:ec7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3740c",
      "incomplete_value": true,
      "site": "00c37410",
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
            "const:dfa:8"
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
      "00c37810",
      "PARAM",
      [
        "storage",
        "01128608",
        null,
        null
      ]
    ],
    [
      "00c37834",
      "PARAM",
      [
        "storage",
        "002a0dfa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37810",
      "PARAM",
      [
        "storage",
        "01128a08",
        null,
        null
      ]
    ],
    [
      "00c37834",
      "PARAM",
      [
        "storage",
        "002a0ec7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c373ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c373d0.md#insn-00c373ec) · [`00c37410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c373d0.md#insn-00c37410) · [`00c373e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c373d0.md#insn-00c373e8)
- 新版 [`00c37814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c377f8.md#insn-00c37814) · [`00c37838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c377f8.md#insn-00c37838) · [`00c37810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c377f8.md#insn-00c37810)

~~~diff
- 00c373ec ["INT_ADD", "register:40f0:8", ["const:c373ec:8", "const:4:8"]]
- 00c373ec ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00c37814 ["INT_ADD", "register:40f0:8", ["const:c37814:8", "const:4:8"]]
+ 00c37814 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00c373ec bytes b18f0094
+ 00c37814 bytes a78f0094
- 00c37410 ["INT_ADD", "register:40f0:8", ["const:c37410:8", "const:4:8"]]
- 00c37410 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c37838 ["INT_ADD", "register:40f0:8", ["const:c37838:8", "const:4:8"]]
+ 00c37838 ["CALL", null, ["callee:00c3800c:8"]]
- 00c37410 bytes f5010094
+ 00c37838 bytes f5010094
- 00c373e8 ["COPY", "tmp:0:8", ["const:608:8"]]
- 00c373e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c373e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c373e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37810 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00c37810 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37810 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37810 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c373e8 bytes 00201891
+ 00c37810 bytes 00202891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dcf216c4f266395281d09b1c50b6a0c"></a>

### [`00c3746c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md) → [`00c37894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md) FUN_00c37894

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c37488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37488.md) [`00c52abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52abc.md) · 呼出先 1件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md)
- 新版 呼出元 2件 [`00c378b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378b0.md) [`00c52ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52ee4.md) · 呼出先 1件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c378a8",
      "incomplete_value": true,
      "site": "00c378ac",
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
            "const:ec7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37480",
      "incomplete_value": true,
      "site": "00c37484",
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
            "const:dfa:8"
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
      "00c378a8",
      "PARAM",
      [
        "storage",
        "002a2dfa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c378a8",
      "PARAM",
      [
        "storage",
        "002a2ec7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md#insn-00c37484) · [`00c37478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md#insn-00c37478) · [`00c37480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md#insn-00c37480)
- 新版 [`00c378ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md#insn-00c378ac) · [`00c378a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md#insn-00c378a0) · [`00c378a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md#insn-00c378a8)

~~~diff
- 00c37484 ["INT_ADD", "register:40f0:8", ["const:c37484:8", "const:4:8"]]
- 00c37484 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c378ac ["INT_ADD", "register:40f0:8", ["const:c378ac:8", "const:4:8"]]
+ 00c378ac ["CALL", null, ["callee:00c3800c:8"]]
- 00c37484 bytes d8010094
+ 00c378ac bytes d8010094
- 00c37478 ["COPY", "register:0:8", ["register:4000:8"]]
- 00c37478 ["INT_ADD", "register:40f0:8", ["const:c37478:8", "const:4:8"]]
- 00c37478 ["CALLIND", null, ["register:0:8"]]
+ 00c378a0 ["COPY", "register:0:8", ["register:4000:8"]]
+ 00c378a0 ["INT_ADD", "register:40f0:8", ["const:c378a0:8", "const:4:8"]]
+ 00c378a0 ["CALLIND", null, ["register:0:8"]]
- 00c37478 bytes 00003fd6
+ 00c378a0 bytes 00003fd6
- 00c37480 ["COPY", "tmp:0:8", ["const:dfa:8"]]
- 00c37480 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37480 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37480 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c378a8 ["COPY", "tmp:0:8", ["const:ec7:8"]]
+ 00c378a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c378a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c378a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37480 bytes 00e83791
+ 00c378a8 bytes 001c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b90940b81dbc3676479ef0354253ef9f"></a>

### [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) → [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) FUN_00c378e0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00c3742c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3742c.md) [`00c51bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51bd0.md) [`00c51cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51cd8.md) [`00c51ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51ea0.md) [`00c52150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52150.md) · 呼出先 1件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md)
- 新版 呼出元 8件 [`00c37854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37854.md) [`00c51ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ff8.md) [`00c52100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52100.md) [`00c522c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c522c8.md) [`00c52578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52578.md) · 呼出先 1件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c378f4",
      "incomplete_value": false,
      "site": "00c378f8",
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
            "const:94f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c374cc",
      "incomplete_value": false,
      "site": "00c374d0",
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
            "const:882:8"
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
      "00c378f4",
      "PARAM",
      [
        "storage",
        "002a8882",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c378f4",
      "PARAM",
      [
        "storage",
        "002a894f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c374d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md#insn-00c374d0) · [`00c374c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md#insn-00c374c4) · [`00c374cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md#insn-00c374cc)
- 新版 [`00c378f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md#insn-00c378f8) · [`00c378ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md#insn-00c378ec) · [`00c378f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md#insn-00c378f4)

~~~diff
- 00c374d0 ["INT_ADD", "register:40f0:8", ["const:c374d0:8", "const:4:8"]]
- 00c374d0 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c378f8 ["INT_ADD", "register:40f0:8", ["const:c378f8:8", "const:4:8"]]
+ 00c378f8 ["CALL", null, ["callee:00c3800c:8"]]
- 00c374d0 bytes c5010094
+ 00c378f8 bytes c5010094
- 00c374c4 ["COPY", "register:0:8", ["register:4000:8"]]
- 00c374c4 ["INT_ADD", "register:40f0:8", ["const:c374c4:8", "const:4:8"]]
- 00c374c4 ["CALLIND", null, ["register:0:8"]]
+ 00c378ec ["COPY", "register:0:8", ["register:4000:8"]]
+ 00c378ec ["INT_ADD", "register:40f0:8", ["const:c378ec:8", "const:4:8"]]
+ 00c378ec ["CALLIND", null, ["register:0:8"]]
- 00c374c4 bytes 00003fd6
+ 00c378ec bytes 00003fd6
- 00c374cc ["COPY", "tmp:0:8", ["const:882:8"]]
- 00c374cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c374cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c374cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c378f4 ["COPY", "tmp:0:8", ["const:94f:8"]]
+ 00c378f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c378f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c378f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c374cc bytes 00082291
+ 00c378f4 bytes 003c2591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55d144f9e62c403573b6dd6b16d501e2"></a>

### [`00c374fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374fc.md) → [`00c37924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37924.md) FUN_00c37924

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00c3742c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3742c.md) [`00c374a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374a4.md) [`00c3769c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3769c.md) · 呼出先 6件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c37f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37f08.md) [`00c51a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a20.md) [`00c51a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a2c.md) [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)
- 新版 呼出元 3件 [`00c37854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37854.md) [`00c378cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378cc.md) [`00c37ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ac4.md) · 呼出先 6件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c38330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38330.md) [`00c51e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e48.md) [`00c51e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e54.md) [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3794c",
      "incomplete_value": false,
      "site": "00c37950",
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
            "const:f6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37524",
      "incomplete_value": false,
      "site": "00c37528",
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
            "const:f2a:8"
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
      "definition_site": "00c37990",
      "incomplete_value": false,
      "site": "00c37998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:8bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37568",
      "incomplete_value": false,
      "site": "00c37570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:87d:8"
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
      "definition_site": "00c37994",
      "incomplete_value": true,
      "site": "00c37998",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3756c",
      "incomplete_value": true,
      "site": "00c37570",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
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
      "00c3794c",
      "PARAM",
      [
        "storage",
        "002c1f2a",
        null,
        "string"
      ]
    ],
    [
      "00c37990",
      "PARAM",
      [
        "storage",
        "002b087d",
        null,
        "string"
      ]
    ],
    [
      "00c37994",
      "READ",
      [
        "storage",
        "00ca4480",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c3794c",
      "PARAM",
      [
        "storage",
        "002c1f6a",
        null,
        "string"
      ]
    ],
    [
      "00c37990",
      "PARAM",
      [
        "storage",
        "002b08bd",
        null,
        "string"
      ]
    ],
    [
      "00c37994",
      "READ",
      [
        "storage",
        "00ca4880",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374fc.md#insn-00c37528) · [`00c37570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374fc.md#insn-00c37570) · [`00c37604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374fc.md#insn-00c37604)
- 新版 [`00c37950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37924.md#insn-00c37950) · [`00c37998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37924.md#insn-00c37998) · [`00c37a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37924.md#insn-00c37a2c)

~~~diff
- 00c37528 ["INT_ADD", "register:40f0:8", ["const:c37528:8", "const:4:8"]]
- 00c37528 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c37950 ["INT_ADD", "register:40f0:8", ["const:c37950:8", "const:4:8"]]
+ 00c37950 ["CALL", null, ["callee:00c3800c:8"]]
- 00c37528 bytes af010094
+ 00c37950 bytes af010094
- 00c37570 ["INT_ADD", "register:40f0:8", ["const:c37570:8", "const:4:8"]]
- 00c37570 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c37998 ["INT_ADD", "register:40f0:8", ["const:c37998:8", "const:4:8"]]
+ 00c37998 ["CALL", null, ["callee:00c3800c:8"]]
- 00c37570 bytes 9d010094
+ 00c37998 bytes 9d010094
- 00c37604 ["INT_ADD", "register:40f0:8", ["const:c37604:8", "const:4:8"]]
- 00c37604 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c37a2c ["INT_ADD", "register:40f0:8", ["const:c37a2c:8", "const:4:8"]]
+ 00c37a2c ["CALL", null, ["callee:00c3800c:8"]]
- 00c37604 bytes 78010094
+ 00c37a2c bytes 78010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af2e45d0bb1168ec9f05825cdca535fb"></a>

### [`00c37648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37648.md) → [`00c37a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37a70.md) FUN_00c37a70

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00c37418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37418.md) [`00c37488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37488.md) [`00c37668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37668.md) · 呼出先 1件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)
- 新版 呼出元 3件 [`00c37840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37840.md) [`00c378b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378b0.md) [`00c37a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37a90.md) · 呼出先 1件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c37a88",
      "incomplete_value": false,
      "site": "00c37a88",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37660",
      "incomplete_value": false,
      "site": "00c37660",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c37a84",
      "incomplete_value": false,
      "site": "00c37a88",
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
            "const:8c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3765c",
      "incomplete_value": false,
      "site": "00c37660",
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
            "const:886:8"
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
      "00c37a88",
      "WRITE",
      [
        "storage",
        "00ca4480",
        null,
        "pointer"
      ]
    ],
    [
      "00c37a88",
      "DATA",
      [
        "storage",
        "002b1886",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37a88",
      "WRITE",
      [
        "storage",
        "00ca4880",
        null,
        "pointer"
      ]
    ],
    [
      "00c37a88",
      "DATA",
      [
        "storage",
        "002b18c6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37648.md#insn-00c37660) · [`00c3765c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37648.md#insn-00c3765c) · [`00c37664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37648.md#insn-00c37664)
- 新版 [`00c37a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37a70.md#insn-00c37a88) · [`00c37a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37a70.md#insn-00c37a84) · [`00c37a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37a70.md#insn-00c37a8c)

~~~diff
- 00c37660 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:480:8"]]
- 00c37660 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c37a88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:880:8"]]
+ 00c37a88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c37660 bytes 094102f9
+ 00c37a88 bytes 094104f9
- 00c3765c ["COPY", "tmp:0:8", ["const:886:8"]]
- 00c3765c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c3765c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c3765c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c37a84 ["COPY", "tmp:0:8", ["const:8c6:8"]]
+ 00c37a84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c37a84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c37a84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c3765c bytes 29192291
+ 00c37a84 bytes 29192391
- 00c37664 ["INT_ADD", "register:40f0:8", ["const:c37664:8", "const:4:8"]]
- 00c37664 ["CALL", null, ["callee:00c58020:8"]]
+ 00c37a8c ["INT_ADD", "register:40f0:8", ["const:c37a8c:8", "const:4:8"]]
+ 00c37a8c ["CALL", null, ["callee:00c58020:8"]]
- 00c37664 bytes 6f810094
+ 00c37a8c bytes 65810094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d40a23be30f9a606f673ed7909380c8"></a>

### [`00c37764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37764.md) → [`00c37b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37b8c.md) __cxa_deleted_virtual

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md)

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
      "definition_site": "00c37b9c",
      "incomplete_value": false,
      "site": "00c37ba0",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37774",
      "incomplete_value": false,
      "site": "00c37778",
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
            "const:d68:8"
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
      "00c37b9c",
      "PARAM",
      [
        "storage",
        "002b5d68",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37b9c",
      "PARAM",
      [
        "storage",
        "002b5da8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37764.md#insn-00c37778) · [`00c37774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37764.md#insn-00c37774)
- 新版 [`00c37ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37b8c.md#insn-00c37ba0) · [`00c37b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37b8c.md#insn-00c37b9c)

~~~diff
- 00c37778 ["INT_ADD", "register:40f0:8", ["const:c37778:8", "const:4:8"]]
- 00c37778 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c37ba0 ["INT_ADD", "register:40f0:8", ["const:c37ba0:8", "const:4:8"]]
+ 00c37ba0 ["CALL", null, ["callee:00c3800c:8"]]
- 00c37778 bytes 1b010094
+ 00c37ba0 bytes 1b010094
- 00c37774 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00c37774 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37774 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37774 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37b9c ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 00c37b9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37b9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37b9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37774 bytes 00a03591
+ 00c37b9c bytes 00a03691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb62ed49cea6471db5083e806e9831ed"></a>

### [`00c377b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c377b0.md) → [`00c37bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37bd8.md) _ZNKSt9exception4whatEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c37be0",
      "incomplete_value": false,
      "site": "00c37be4",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c377b8",
      "incomplete_value": false,
      "site": "00c377bc",
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
            "const:d7f:8"
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
      "00c37be0",
      "DATA",
      [
        "storage",
        "002a3d7f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37be0",
      "DATA",
      [
        "storage",
        "002a3e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c377b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c377b0.md#insn-00c377b8)
- 新版 [`00c37be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37bd8.md#insn-00c37be0)

~~~diff
- 00c377b8 ["COPY", "tmp:0:8", ["const:d7f:8"]]
- 00c377b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c377b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c377b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37be0 ["COPY", "tmp:0:8", ["const:e4c:8"]]
+ 00c37be0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37be0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37be0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c377b8 bytes 00fc3591
+ 00c37be0 bytes 00303991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f02ee3a0c855b2aa9bd7f17db3f5ab"></a>

### [`00c377ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c377ec.md) → [`00c37c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c14.md) _ZNKSt13bad_exception4whatEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c37c1c",
      "incomplete_value": false,
      "site": "00c37c20",
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
            "const:579:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c377f4",
      "incomplete_value": false,
      "site": "00c377f8",
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
            "const:539:8"
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
      "00c37c1c",
      "DATA",
      [
        "storage",
        "002ae539",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37c1c",
      "DATA",
      [
        "storage",
        "002ae579",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c377f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c377ec.md#insn-00c377f4)
- 新版 [`00c37c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c14.md#insn-00c37c1c)

~~~diff
- 00c377f4 ["COPY", "tmp:0:8", ["const:539:8"]]
- 00c377f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c377f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c377f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37c1c ["COPY", "tmp:0:8", ["const:579:8"]]
+ 00c37c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c377f4 bytes 00e41491
+ 00c37c1c bytes 00e41591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca85d6017906158a432c69535e5b152"></a>

### [`00c37840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37840.md) → [`00c37c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c68.md) _ZNKSt9bad_alloc4whatEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c37c70",
      "incomplete_value": false,
      "site": "00c37c74",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37848",
      "incomplete_value": false,
      "site": "00c3784c",
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
            "const:a93:8"
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
      "00c37c70",
      "DATA",
      [
        "storage",
        "002aaa93",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37c70",
      "DATA",
      [
        "storage",
        "002aab60",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37840.md#insn-00c37848)
- 新版 [`00c37c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c68.md#insn-00c37c70)

~~~diff
- 00c37848 ["COPY", "tmp:0:8", ["const:a93:8"]]
- 00c37848 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37848 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37848 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37c70 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 00c37c70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37c70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37c70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37848 bytes 004c2a91
+ 00c37c70 bytes 00802d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5903350ef1b8b7268f2818023c25f523"></a>

### [`00c37894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37894.md) → [`00c37cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37cbc.md) _ZNKSt20bad_array_new_length4whatEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c37cc4",
      "incomplete_value": false,
      "site": "00c37cc8",
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
            "const:21b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3789c",
      "incomplete_value": false,
      "site": "00c378a0",
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
            "const:13f:8"
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
      "00c37cc4",
      "DATA",
      [
        "storage",
        "002a513f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37cc4",
      "DATA",
      [
        "storage",
        "002a521b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3789c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37894.md#insn-00c3789c)
- 新版 [`00c37cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37cbc.md#insn-00c37cc4)

~~~diff
- 00c3789c ["COPY", "tmp:0:8", ["const:13f:8"]]
- 00c3789c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c3789c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c3789c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37cc4 ["COPY", "tmp:0:8", ["const:21b:8"]]
+ 00c37cc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37cc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37cc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c3789c bytes 00fc0491
+ 00c37cc4 bytes 006c0891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc78594ea9061b5a7a273437c4e91800"></a>

### [`00c378a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378a4.md) → [`00c37ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ccc.md) _ZNSt12out_of_rangeD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c57b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b00.md) · 呼出先 3件 [`00c53880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53880.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 10件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c57f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f00.md) · 呼出先 3件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

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
      "definition_site": "00c37cec",
      "incomplete_value": true,
      "site": "00c37cf4",
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
      "definition_site": "00c378c4",
      "incomplete_value": true,
      "site": "00c378cc",
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
      "00c37ce4",
      "READ",
      [
        "storage",
        "00c9b690",
        null,
        "pointer"
      ]
    ],
    [
      "00c37cf4",
      "DATA",
      [
        "storage",
        "00c962d8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00c37ce4",
      "READ",
      [
        "storage",
        "00c9ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00c37cf4",
      "DATA",
      [
        "storage",
        "00c966d8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c378bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378a4.md#insn-00c378bc) · [`00c378d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378a4.md#insn-00c378d4) · [`00c378e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378a4.md#insn-00c378e4)
- 新版 [`00c37ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ccc.md#insn-00c37ce4) · [`00c37cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ccc.md#insn-00c37cfc) · [`00c37d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ccc.md#insn-00c37d0c)

~~~diff
- 00c378bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:690:8"]]
- 00c378bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c37ce4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
+ 00c37ce4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c378bc bytes 084943f9
+ 00c37ce4 bytes 084945f9
- 00c378d4 ["INT_ADD", "register:40f0:8", ["const:c378d4:8", "const:4:8"]]
- 00c378d4 ["CALL", null, ["callee:00c53ca0:8"]]
+ 00c37cfc ["INT_ADD", "register:40f0:8", ["const:c37cfc:8", "const:4:8"]]
+ 00c37cfc ["CALL", null, ["callee:00c53ca0:8"]]
- 00c378d4 bytes eb6f0094
+ 00c37cfc bytes e96f0094
- 00c378e4 ["INT_ADD", "register:40f0:8", ["const:c378e4:8", "const:4:8"]]
- 00c378e4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c37d0c ["INT_ADD", "register:40f0:8", ["const:c37d0c:8", "const:4:8"]]
+ 00c37d0c ["CALL", null, ["callee:00c57eb0:8"]]
- 00c378e4 bytes 73800094
+ 00c37d0c bytes 69800094
~~~


<a id="compare-6c78ec0073842cf84510d83ae7cf8323"></a>

### [`00c37934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md) → [`00c37d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md) _ZNSt13runtime_errorD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`006d7610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md) [`00beff20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff20.md) [`00bf0688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0688.md) [`00c5a4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4c0.md) [`00c5db70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db70.md) · 呼出先 3件 [`00c53880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53880.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)
- 新版 呼出元 8件 [`006d7650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7650.md) [`00bf0348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0348.md) [`00bf0ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0ab0.md) [`00c5a8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8c0.md) [`00c5df70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df70.md) · 呼出先 3件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582e0.md)

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
      "definition_site": "00c37d7c",
      "incomplete_value": true,
      "site": "00c37d84",
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
      "definition_site": "00c37954",
      "incomplete_value": true,
      "site": "00c3795c",
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
      "00c37d74",
      "READ",
      [
        "storage",
        "00c9b698",
        null,
        "pointer"
      ]
    ],
    [
      "00c37d84",
      "DATA",
      [
        "storage",
        "00c96300",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00c37d74",
      "READ",
      [
        "storage",
        "00c9ba98",
        null,
        "pointer"
      ]
    ],
    [
      "00c37d84",
      "DATA",
      [
        "storage",
        "00c96700",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3794c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md#insn-00c3794c) · [`00c37964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md#insn-00c37964) · [`00c37974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md#insn-00c37974)
- 新版 [`00c37d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md#insn-00c37d74) · [`00c37d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md#insn-00c37d8c) · [`00c37d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md#insn-00c37d9c)

~~~diff
- 00c3794c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:698:8"]]
- 00c3794c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c37d74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a98:8"]]
+ 00c37d74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c3794c bytes 084d43f9
+ 00c37d74 bytes 084d45f9
- 00c37964 ["INT_ADD", "register:40f0:8", ["const:c37964:8", "const:4:8"]]
- 00c37964 ["CALL", null, ["callee:00c53ca0:8"]]
+ 00c37d8c ["INT_ADD", "register:40f0:8", ["const:c37d8c:8", "const:4:8"]]
+ 00c37d8c ["CALL", null, ["callee:00c53ca0:8"]]
- 00c37964 bytes c76f0094
+ 00c37d8c bytes c56f0094
- 00c37974 ["INT_ADD", "register:40f0:8", ["const:c37974:8", "const:4:8"]]
- 00c37974 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00c37d9c ["INT_ADD", "register:40f0:8", ["const:c37d9c:8", "const:4:8"]]
+ 00c37d9c ["CALL", null, ["callee:00c57eb0:8"]]
- 00c37974 bytes 4f800094
+ 00c37d9c bytes 45800094
~~~


<a id="compare-c77baadb00c2fe25b835517c1b1ca823"></a>

### [`00c37bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37bd4.md) → [`00c37ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ffc.md) _ZNKSt10bad_typeid4whatEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c38004",
      "incomplete_value": false,
      "site": "00c38008",
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
            "const:adb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37bdc",
      "incomplete_value": false,
      "site": "00c37be0",
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
            "const:a9b:8"
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
      "00c38004",
      "DATA",
      [
        "storage",
        "002bea9b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c38004",
      "DATA",
      [
        "storage",
        "002beadb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37bd4.md#insn-00c37bdc)
- 新版 [`00c38004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ffc.md#insn-00c38004)

~~~diff
- 00c37bdc ["COPY", "tmp:0:8", ["const:a9b:8"]]
- 00c37bdc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37bdc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37bdc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c38004 ["COPY", "tmp:0:8", ["const:adb:8"]]
+ 00c38004 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38004 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38004 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37bdc bytes 006c2a91
+ 00c38004 bytes 006c2b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbb565b0fe68164c0f1bf5648ab29f13"></a>

### [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) → [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) FUN_00c3800c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 22件 [`00c37148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37148.md) [`00c3728c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3728c.md) [`00c37334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37334.md) [`00c373d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c373d0.md) [`00c3746c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md) · 呼出先 10件 [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md) [`00c59e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e80.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5e300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e300.md) [`00c5ea70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea70.md)
- 新版 呼出元 22件 [`00c37570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37570.md) [`00c376b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c376b4.md) [`00c3775c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c3775c.md) [`00c377f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c377f8.md) [`00c37894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md) · 呼出先 10件 [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md) [`00c5a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a280.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5e700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e700.md) [`00c5ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38040",
      "incomplete_value": false,
      "site": "00c3806c",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37c18",
      "incomplete_value": false,
      "site": "00c37c44",
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
            "const:dc8:8"
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
      "definition_site": "00c38068",
      "incomplete_value": true,
      "site": "00c3806c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37c40",
      "incomplete_value": true,
      "site": "00c37c44",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c380e4",
      "incomplete_value": false,
      "site": "00c380f0",
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
            "const:b3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37cbc",
      "incomplete_value": false,
      "site": "00c37cc8",
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
            "const:afc:8"
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
      "00c38040",
      "PARAM",
      [
        "storage",
        "002c0dc8",
        null,
        "string"
      ]
    ],
    [
      "00c38064",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c380e4",
      "PARAM",
      [
        "storage",
        "002bfafc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c38040",
      "PARAM",
      [
        "storage",
        "002c0e08",
        null,
        "string"
      ]
    ],
    [
      "00c38064",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c380e4",
      "PARAM",
      [
        "storage",
        "002bfb3c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md#insn-00c37c44) · [`00c37cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md#insn-00c37cc8) · [`00c37cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md#insn-00c37cdc)
- 新版 [`00c3806c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md#insn-00c3806c) · [`00c380f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md#insn-00c380f0) · [`00c38104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md#insn-00c38104)

~~~diff
- 00c37c44 ["INT_ADD", "register:40f0:8", ["const:c37c44:8", "const:4:8"]]
- 00c37c44 ["CALL", null, ["callee:00c5a220:8"]]
+ 00c3806c ["INT_ADD", "register:40f0:8", ["const:c3806c:8", "const:4:8"]]
+ 00c3806c ["CALL", null, ["callee:00c5a220:8"]]
- 00c37c44 bytes 77880094
+ 00c3806c bytes 6d880094
- 00c37cc8 ["INT_ADD", "register:40f0:8", ["const:c37cc8:8", "const:4:8"]]
- 00c37cc8 ["CALL", null, ["callee:00c5ee90:8"]]
+ 00c380f0 ["INT_ADD", "register:40f0:8", ["const:c380f0:8", "const:4:8"]]
+ 00c380f0 ["CALL", null, ["callee:00c5ee90:8"]]
- 00c37cc8 bytes 729b0094
+ 00c380f0 bytes 689b0094
- 00c37cdc ["INT_ADD", "register:40f0:8", ["const:c37cdc:8", "const:4:8"]]
- 00c37cdc ["CALL", null, ["callee:00c5eea0:8"]]
+ 00c38104 ["INT_ADD", "register:40f0:8", ["const:c38104:8", "const:4:8"]]
+ 00c38104 ["CALL", null, ["callee:00c5eea0:8"]]
- 00c37cdc bytes 719b0094
+ 00c38104 bytes 679b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23b0b99de694fe073d186dc8252777fd"></a>

### [`00c37f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37f08.md) → [`00c38330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38330.md) FUN_00c38330

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c374fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374fc.md) · 呼出先 2件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)
- 新版 呼出元 1件 [`00c37924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37924.md) · 呼出先 2件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38374",
      "incomplete_value": true,
      "site": "00c38378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37f4c",
      "incomplete_value": true,
      "site": "00c37f50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38364",
      "incomplete_value": true,
      "site": "00c38378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37f3c",
      "incomplete_value": true,
      "site": "00c37f50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c38360",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38364",
      "READ",
      [
        "storage",
        "00c9ba80",
        null,
        "pointer"
      ]
    ],
    [
      "00c38364",
      "PARAM",
      [
        "storage",
        "00c965d0",
        "_ZTIN10__cxxabiv117__class_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c38360",
      "READ",
      [
        "storage",
        "00c9be78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38364",
      "READ",
      [
        "storage",
        "00c9be80",
        null,
        "pointer"
      ]
    ],
    [
      "00c38364",
      "PARAM",
      [
        "storage",
        "00c969d0",
        "_ZTIN10__cxxabiv117__class_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37f08.md#insn-00c37f50) · [`00c37f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37f08.md#insn-00c37f38) · [`00c37f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37f08.md#insn-00c37f3c)
- 新版 [`00c38378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38330.md#insn-00c38378) · [`00c38360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38330.md#insn-00c38360) · [`00c38364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38330.md#insn-00c38364)

~~~diff
- 00c37f50 ["INT_ADD", "register:40f0:8", ["const:c37f50:8", "const:4:8"]]
- 00c37f50 ["CALL", null, ["callee:00c58610:8"]]
+ 00c38378 ["INT_ADD", "register:40f0:8", ["const:c38378:8", "const:4:8"]]
+ 00c38378 ["CALL", null, ["callee:00c58610:8"]]
- 00c37f50 bytes b0800094
+ 00c38378 bytes a6800094
- 00c37f38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00c37f38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c38360 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
+ 00c38360 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c37f38 bytes 083d45f9
+ 00c38360 bytes 083d47f9
- 00c37f3c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:a80:8"]]
- 00c37f3c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c38364 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e80:8"]]
+ 00c38364 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00c37f3c bytes 424045f9
+ 00c38364 bytes 424047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fec31e854e59ca29934f66453ecabf7"></a>

### [`00c384ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c384ec.md) → [`00c38914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38914.md) FUN_00c38914

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38974",
      "incomplete_value": true,
      "site": "00c38978",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3854c",
      "incomplete_value": true,
      "site": "00c38550",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38964",
      "incomplete_value": true,
      "site": "00c38978",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3853c",
      "incomplete_value": true,
      "site": "00c38550",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a88:8"
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
      "00c38960",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38964",
      "READ",
      [
        "storage",
        "00c9ba88",
        null,
        "pointer"
      ]
    ],
    [
      "00c38964",
      "PARAM",
      [
        "storage",
        "00c965e8",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c38960",
      "READ",
      [
        "storage",
        "00c9be78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38964",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00c38964",
      "PARAM",
      [
        "storage",
        "00c969e8",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c384ec.md#insn-00c38550) · [`00c38518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c384ec.md#insn-00c38518) · [`00c38538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c384ec.md#insn-00c38538)
- 新版 [`00c38978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38914.md#insn-00c38978) · [`00c38940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38914.md#insn-00c38940) · [`00c38960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38914.md#insn-00c38960)

~~~diff
- 00c38550 ["INT_ADD", "register:40f0:8", ["const:c38550:8", "const:4:8"]]
- 00c38550 ["CALL", null, ["callee:00c58610:8"]]
+ 00c38978 ["INT_ADD", "register:40f0:8", ["const:c38978:8", "const:4:8"]]
+ 00c38978 ["CALL", null, ["callee:00c58610:8"]]
- 00c38550 bytes 307f0094
+ 00c38978 bytes 267f0094
- 00c38518 ["INT_ADD", "register:40f0:8", ["const:c38518:8", "const:4:8"]]
- 00c38518 ["CALL", null, ["callee:00c5b850:8"]]
+ 00c38940 ["INT_ADD", "register:40f0:8", ["const:c38940:8", "const:4:8"]]
+ 00c38940 ["CALL", null, ["callee:00c5b850:8"]]
- 00c38518 bytes ce8b0094
+ 00c38940 bytes c48b0094
- 00c38538 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00c38538 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c38960 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
+ 00c38960 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c38538 bytes 083d45f9
+ 00c38960 bytes 083d47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc1a673d517535b9014f30eadc9fcd94"></a>

### [`00c38598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38598.md) → [`00c389c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c389c0.md) FUN_00c389c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c38854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38854.md) [`00c38948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38948.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c38c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38c7c.md) [`00c38d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38d70.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 89.14% / 新版 89.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 11件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c389ec",
      "incomplete_value": true,
      "site": "00c389f0",
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
      "definition_site": "00c385c4",
      "incomplete_value": true,
      "site": "00c385c8",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c38b00",
      "incomplete_value": true,
      "site": "00c38b04",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4040:8"
              ],
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
      "definition_site": "00c386d8",
      "incomplete_value": true,
      "site": "00c386dc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4040:8"
              ],
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
    "ordinal": 13,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38a50",
      "incomplete_value": true,
      "site": "00c38a5c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38628",
      "incomplete_value": true,
      "site": "00c38634",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
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
      "00c389e8",
      "READ",
      [
        "storage",
        "00c9ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00c38a50",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38a50",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c389e8",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ],
    [
      "00c38a50",
      "READ",
      [
        "storage",
        "00c9be78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38a50",
      "PARAM",
      [
        "storage",
        "00c969b8",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38598.md#insn-00c38634) · [`00c3866c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38598.md#insn-00c3866c) · [`00c386f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38598.md#insn-00c386f0)
- 新版 [`00c38a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c389c0.md#insn-00c38a5c) · [`00c38a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c389c0.md#insn-00c38a94) · [`00c38b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c389c0.md#insn-00c38b18)

~~~diff
- 00c38634 ["INT_ADD", "register:40f0:8", ["const:c38634:8", "const:4:8"]]
- 00c38634 ["CALL", null, ["callee:00c58610:8"]]
+ 00c38a5c ["INT_ADD", "register:40f0:8", ["const:c38a5c:8", "const:4:8"]]
+ 00c38a5c ["CALL", null, ["callee:00c58610:8"]]
- 00c38634 bytes f77e0094
+ 00c38a5c bytes ed7e0094
- 00c3866c ["INT_ADD", "register:40f0:8", ["const:c3866c:8", "const:4:8"]]
- 00c3866c ["CALL", null, ["callee:00c58610:8"]]
+ 00c38a94 ["INT_ADD", "register:40f0:8", ["const:c38a94:8", "const:4:8"]]
+ 00c38a94 ["CALL", null, ["callee:00c58610:8"]]
- 00c3866c bytes e97e0094
+ 00c38a94 bytes df7e0094
- 00c386f0 ["INT_ADD", "register:40f0:8", ["const:c386f0:8", "const:4:8"]]
- 00c386f0 ["CALL", null, ["callee:00c58610:8"]]
+ 00c38b18 ["INT_ADD", "register:40f0:8", ["const:c38b18:8", "const:4:8"]]
+ 00c38b18 ["CALL", null, ["callee:00c58610:8"]]
- 00c386f0 bytes c87e0094
+ 00c38b18 bytes be7e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f4753ba34fe543b3004190e6e7a9512"></a>

### [`00c389e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c389e8.md) → [`00c38e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38e10.md) FUN_00c38e10

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.81% / 新版 86.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c38e34",
      "incomplete_value": true,
      "site": "00c38e38",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
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
      "definition_site": "00c38a0c",
      "incomplete_value": true,
      "site": "00c38a10",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38e80",
      "incomplete_value": true,
      "site": "00c38e90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38a58",
      "incomplete_value": true,
      "site": "00c38a68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38e8c",
      "incomplete_value": true,
      "site": "00c38e90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38a64",
      "incomplete_value": true,
      "site": "00c38a68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c38e30",
      "READ",
      [
        "storage",
        "00c9ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00c38e80",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38e80",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c38e30",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ],
    [
      "00c38e80",
      "READ",
      [
        "storage",
        "00c9be78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38e80",
      "PARAM",
      [
        "storage",
        "00c969b8",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c389e8.md#insn-00c38a68) · [`00c38a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c389e8.md#insn-00c38a98) · [`00c38ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c389e8.md#insn-00c38ad0)
- 新版 [`00c38e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38e10.md#insn-00c38e90) · [`00c38ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38e10.md#insn-00c38ec0) · [`00c38ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38e10.md#insn-00c38ef8)

~~~diff
- 00c38a68 ["INT_ADD", "register:40f0:8", ["const:c38a68:8", "const:4:8"]]
- 00c38a68 ["CALL", null, ["callee:00c58610:8"]]
+ 00c38e90 ["INT_ADD", "register:40f0:8", ["const:c38e90:8", "const:4:8"]]
+ 00c38e90 ["CALL", null, ["callee:00c58610:8"]]
- 00c38a68 bytes ea7d0094
+ 00c38e90 bytes e07d0094
- 00c38a98 ["INT_ADD", "register:40f0:8", ["const:c38a98:8", "const:4:8"]]
- 00c38a98 ["CALL", null, ["callee:00c58610:8"]]
+ 00c38ec0 ["INT_ADD", "register:40f0:8", ["const:c38ec0:8", "const:4:8"]]
+ 00c38ec0 ["CALL", null, ["callee:00c58610:8"]]
- 00c38a98 bytes de7d0094
+ 00c38ec0 bytes d47d0094
- 00c38ad0 ["INT_ADD", "register:40f0:8", ["const:c38ad0:8", "const:4:8"]]
- 00c38ad0 ["CALL", null, ["callee:00c58610:8"]]
+ 00c38ef8 ["INT_ADD", "register:40f0:8", ["const:c38ef8:8", "const:4:8"]]
+ 00c38ef8 ["CALL", null, ["callee:00c58610:8"]]
- 00c38ad0 bytes d07d0094
+ 00c38ef8 bytes c67d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07873d6bd6febb050aa202295830db6b"></a>

### [`00c39658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39658.md) → [`00c39a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md) __cxa_demangle

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9f0.md) · 呼出先 10件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a7f0.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`00c5edf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5edf0.md) · 呼出先 10件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3ac18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c39dc8",
      "incomplete_value": false,
      "site": "00c39dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c399a0",
      "incomplete_value": false,
      "site": "00c399a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "ordinal": 90,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c39f20",
      "incomplete_value": false,
      "site": "00c39f2c",
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
            "const:e53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c39af8",
      "incomplete_value": false,
      "site": "00c39b04",
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
            "const:e13:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3a008",
      "incomplete_value": false,
      "site": "00c3a020",
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
            "const:ee2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c39be0",
      "incomplete_value": false,
      "site": "00c39bf8",
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
            "const:e15:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c39dc8",
      "DATA",
      [
        "storage",
        "00c993e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c39f20",
      "PARAM",
      [
        "storage",
        "002b9e13",
        null,
        "string"
      ]
    ],
    [
      "00c3a008",
      "PARAM",
      [
        "storage",
        "002a0e15",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c39dc8",
      "DATA",
      [
        "storage",
        "00c997e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c39f20",
      "PARAM",
      [
        "storage",
        "002b9e53",
        null,
        "string"
      ]
    ],
    [
      "00c3a008",
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c39b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39658.md#insn-00c39b04) · [`00c39bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39658.md#insn-00c39bf8) · [`00c396b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39658.md#insn-00c396b4)
- 新版 [`00c39f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md#insn-00c39f2c) · [`00c3a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md#insn-00c3a020) · [`00c39adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md#insn-00c39adc)

~~~diff
- 00c39b04 ["INT_ADD", "register:40f0:8", ["const:c39b04:8", "const:4:8"]]
- 00c39b04 ["CALL", null, ["callee:00c3ac18:8"]]
+ 00c39f2c ["INT_ADD", "register:40f0:8", ["const:c39f2c:8", "const:4:8"]]
+ 00c39f2c ["CALL", null, ["callee:00c3ac18:8"]]
- 00c39b04 bytes 3b030094
+ 00c39f2c bytes 3b030094
- 00c39bf8 ["INT_ADD", "register:40f0:8", ["const:c39bf8:8", "const:4:8"]]
- 00c39bf8 ["CALL", null, ["callee:00c3800c:8"]]
+ 00c3a020 ["INT_ADD", "register:40f0:8", ["const:c3a020:8", "const:4:8"]]
+ 00c3a020 ["CALL", null, ["callee:00c3800c:8"]]
- 00c39bf8 bytes fbf7ff97
+ 00c3a020 bytes fbf7ff97
- 00c396b4 ["INT_ADD", "register:40f0:8", ["const:c396b4:8", "const:4:8"]]
- 00c396b4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c39adc ["INT_ADD", "register:40f0:8", ["const:c39adc:8", "const:4:8"]]
+ 00c39adc ["CALL", null, ["callee:00c57fe0:8"]]
- 00c396b4 bytes 4b790094
+ 00c39adc bytes 41790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46c979d57c6e6f5c499e2bc6568ec168"></a>

### [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) → [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) FUN_00c3a178

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00c39658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39658.md) [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 31件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a764.md) [`00c3a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a7f0.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md)
- 新版 呼出元 5件 [`00c39a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 31件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3ab8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ab8c.md) [`00c3ac18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.26% / 新版 98.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3a3a0",
      "incomplete_value": false,
      "site": "00c3a3a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c39f78",
      "incomplete_value": false,
      "site": "00c39f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3a7e4",
      "incomplete_value": false,
      "site": "00c3a7e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3a3bc",
      "incomplete_value": false,
      "site": "00c3a3bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3a9e8",
      "incomplete_value": false,
      "site": "00c3a9f4",
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
            "const:1f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3a5c0",
      "incomplete_value": false,
      "site": "00c3a5cc",
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
            "const:fdf:8"
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3a3a0",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3a644",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3a668",
      "DATA",
      [
        "storage",
        "002b08ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3a3a0",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3a644",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3a668",
      "DATA",
      [
        "storage",
        "002b090e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c39f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md#insn-00c39f94) · [`00c3a1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md#insn-00c3a1a4) · [`00c3a5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md#insn-00c3a5cc)
- 新版 [`00c3a3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md#insn-00c3a3bc) · [`00c3a5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md#insn-00c3a5cc) · [`00c3a9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md#insn-00c3a9f4)

~~~diff
- 00c39f94 ["COPY", "tmp:0:8", ["const:8ce:8"]]
- 00c39f94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c39f94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c39f94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3a3bc ["COPY", "tmp:0:8", ["const:90e:8"]]
+ 00c3a3bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3a3bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3a3bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c39f94 bytes 08392391
+ 00c3a3bc bytes 08392491
- 00c3a1a4 ["INT_ADD", "register:40f0:8", ["const:c3a1a4:8", "const:4:8"]]
- 00c3a1a4 ["CALL", null, ["callee:00c3da94:8"]]
+ 00c3a5cc ["INT_ADD", "register:40f0:8", ["const:c3a5cc:8", "const:4:8"]]
+ 00c3a5cc ["CALL", null, ["callee:00c3da94:8"]]
- 00c3a1a4 bytes 320d0094
+ 00c3a5cc bytes 320d0094
- 00c3a5cc ["INT_ADD", "register:40f0:8", ["const:c3a5cc:8", "const:4:8"]]
- 00c3a5cc ["CALL", null, ["callee:00c3ac18:8"]]
+ 00c3a9f4 ["INT_ADD", "register:40f0:8", ["const:c3a9f4:8", "const:4:8"]]
+ 00c3a9f4 ["CALL", null, ["callee:00c3ac18:8"]]
- 00c3a5cc bytes 89000094
+ 00c3a9f4 bytes 89000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f77014143677c273329c13c09170dc"></a>

### [`00c3a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a7f0.md) → [`00c3ac18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md) FUN_00c3ac18

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c39658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39658.md) [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 2件 [`00c39a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3ac88",
      "incomplete_value": false,
      "site": "00c3ac88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3a860",
      "incomplete_value": false,
      "site": "00c3a860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
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
      "00c3ac88",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3ac88",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3a828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a7f0.md#insn-00c3a828) · [`00c3a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a7f0.md#insn-00c3a850) · [`00c3a858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a7f0.md#insn-00c3a858)
- 新版 [`00c3ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md#insn-00c3ac50) · [`00c3ac78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md#insn-00c3ac78) · [`00c3ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md#insn-00c3ac80)

~~~diff
- 00c3a828 ["INT_ADD", "register:40f0:8", ["const:c3a828:8", "const:4:8"]]
- 00c3a828 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3ac50 ["INT_ADD", "register:40f0:8", ["const:c3ac50:8", "const:4:8"]]
+ 00c3ac50 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3a828 bytes fe7c0094
+ 00c3ac50 bytes f47c0094
- 00c3a850 ["INT_ADD", "register:40f0:8", ["const:c3a850:8", "const:4:8"]]
- 00c3a850 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c3ac78 ["INT_ADD", "register:40f0:8", ["const:c3ac78:8", "const:4:8"]]
+ 00c3ac78 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c3a850 bytes e4740094
+ 00c3ac78 bytes da740094
- 00c3a858 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00c3a858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3a858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3a858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3ac80 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3ac80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ac80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ac80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3a858 bytes 08410591
+ 00c3ac80 bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0834980e3007c74ec424d3b9de3b19a0"></a>

### [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) → [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) FUN_00c3accc

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 15件 [`00c39658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39658.md) [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 38件 [`00c3a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a764.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3c840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c840.md) [`00c3ddb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3ddb4.md)
- 新版 呼出元 15件 [`00c39a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 38件 [`00c3ab8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ab8c.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3cc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md) [`00c3e1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e1dc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.14% / 新版 93.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 21件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3aeb0",
      "incomplete_value": false,
      "site": "00c3aeb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3aa88",
      "incomplete_value": false,
      "site": "00c3aa88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3af20",
      "incomplete_value": false,
      "site": "00c3af20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3aaf8",
      "incomplete_value": false,
      "site": "00c3aaf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3af90",
      "incomplete_value": false,
      "site": "00c3af90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3ab68",
      "incomplete_value": false,
      "site": "00c3ab68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3ad18",
      "DATA",
      [
        "storage",
        "003129a0",
        "switchD_00c3a8f8::switchdataD_003129a0",
        "ushort"
      ]
    ],
    [
      "00c3ae30",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3aeb0",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3ad18",
      "DATA",
      [
        "storage",
        "003129e0",
        "switchD_00c3ad20::switchdataD_003129e0",
        "ushort"
      ]
    ],
    [
      "00c3ae30",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3aeb0",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3abb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md#insn-00c3abb8) · [`00c3ad54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md#insn-00c3ad54) · [`00c3b2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md#insn-00c3b2dc)
- 新版 [`00c3afe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md#insn-00c3afe0) · [`00c3b17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md#insn-00c3b17c) · [`00c3b704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md#insn-00c3b704)

~~~diff
- 00c3abb8 ["INT_ADD", "register:40f0:8", ["const:c3abb8:8", "const:4:8"]]
- 00c3abb8 ["CALL", null, ["callee:00c5a020:8"]]
+ 00c3afe0 ["INT_ADD", "register:40f0:8", ["const:c3afe0:8", "const:4:8"]]
+ 00c3afe0 ["CALL", null, ["callee:00c5a020:8"]]
- 00c3abb8 bytes 1a7c0094
+ 00c3afe0 bytes 107c0094
- 00c3ad54 ["COPY", "register:4048:8", ["const:2a5000:8"]]
+ 00c3b17c ["COPY", "register:4048:8", ["const:2a6000:8"]]
- 00c3ad54 bytes 49b3fff0
+ 00c3b17c bytes 49b3fff0
- 00c3b2dc ["INT_ADD", "register:40f0:8", ["const:c3b2dc:8", "const:4:8"]]
- 00c3b2dc ["CALL", null, ["callee:00c4f124:8"]]
+ 00c3b704 ["INT_ADD", "register:40f0:8", ["const:c3b704:8", "const:4:8"]]
+ 00c3b704 ["CALL", null, ["callee:00c4f124:8"]]
- 00c3b2dc bytes 884e0094
+ 00c3b704 bytes 884e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-371eec496d0f63135a9e94e05f5d1215"></a>

### [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) → [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) FUN_00c3c20c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c42598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42598.md) · 呼出先 19件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a764.md) [`00c3bc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bc3c.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3cc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cc08.md)
- 新版 呼出元 7件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c429c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c429c0.md) · 呼出先 19件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3ab8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ab8c.md) [`00c3c064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c064.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3c608",
      "incomplete_value": false,
      "site": "00c3c608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3c1e0",
      "incomplete_value": false,
      "site": "00c3c1e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3c62c",
      "incomplete_value": false,
      "site": "00c3c62c",
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
            "const:d84:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3c204",
      "incomplete_value": false,
      "site": "00c3c204",
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
            "const:d44:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3c8f4",
      "incomplete_value": false,
      "site": "00c3c8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3c4cc",
      "incomplete_value": false,
      "site": "00c3c4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "ordinal": 74,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3c36c",
      "PARAM",
      [
        "storage",
        "002b18ba",
        null,
        "string"
      ]
    ],
    [
      "00c3c4ec",
      "DATA",
      [
        "storage",
        "00c99140",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3c608",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3c36c",
      "PARAM",
      [
        "storage",
        "002b18fa",
        null,
        "string"
      ]
    ],
    [
      "00c3c4ec",
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3c608",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3bf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md#insn-00c3bf4c) · [`00c3be74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md#insn-00c3be74) · [`00c3bec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md#insn-00c3bec4)
- 新版 [`00c3c374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md#insn-00c3c374) · [`00c3c29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md#insn-00c3c29c) · [`00c3c2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md#insn-00c3c2ec)

~~~diff
- 00c3bf4c ["INT_ADD", "register:40f0:8", ["const:c3bf4c:8", "const:4:8"]]
- 00c3bf4c ["CALL", null, ["callee:00c4d0f0:8"]]
+ 00c3c374 ["INT_ADD", "register:40f0:8", ["const:c3c374:8", "const:4:8"]]
+ 00c3c374 ["CALL", null, ["callee:00c4d0f0:8"]]
- 00c3bf4c bytes 5f430094
+ 00c3c374 bytes 5f430094
- 00c3be74 ["INT_ADD", "register:40f0:8", ["const:c3be74:8", "const:4:8"]]
- 00c3be74 ["CALL", null, ["callee:00c3e454:8"]]
+ 00c3c29c ["INT_ADD", "register:40f0:8", ["const:c3c29c:8", "const:4:8"]]
+ 00c3c29c ["CALL", null, ["callee:00c3e454:8"]]
- 00c3be74 bytes 6e080094
+ 00c3c29c bytes 6e080094
- 00c3bec4 ["INT_ADD", "register:40f0:8", ["const:c3bec4:8", "const:4:8"]]
- 00c3bec4 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c3c2ec ["INT_ADD", "register:40f0:8", ["const:c3c2ec:8", "const:4:8"]]
+ 00c3c2ec ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c3bec4 bytes 77770094
+ 00c3c2ec bytes 6d770094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83cc6a73d658282d0d9a08ed68cc5e56"></a>

### [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) → [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) FUN_00c3c940

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 13件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md)
- 新版 呼出元 4件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 13件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3cbb8",
      "incomplete_value": false,
      "site": "00c3cbbc",
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
            "const:28e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3c790",
      "incomplete_value": false,
      "site": "00c3c794",
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
            "const:1b2:8"
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
      "00c3cb70",
      "DATA",
      [
        "storage",
        "00c991b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3cb70",
      "DATA",
      [
        "storage",
        "00c99220",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3cbb8",
      "PARAM",
      [
        "storage",
        "002a51b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3cb70",
      "DATA",
      [
        "storage",
        "00c995b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3cb70",
      "DATA",
      [
        "storage",
        "00c99620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3cbb8",
      "PARAM",
      [
        "storage",
        "002a528e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3c794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md#insn-00c3c794) · [`00c3c588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md#insn-00c3c588) · [`00c3c5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md#insn-00c3c5b0)
- 新版 [`00c3cbbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md#insn-00c3cbbc) · [`00c3c9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md#insn-00c3c9b0) · [`00c3c9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md#insn-00c3c9d8)

~~~diff
- 00c3c794 ["INT_ADD", "register:40f0:8", ["const:c3c794:8", "const:4:8"]]
- 00c3c794 ["CALL", null, ["callee:00c57fd0:8"]]
+ 00c3cbbc ["INT_ADD", "register:40f0:8", ["const:c3cbbc:8", "const:4:8"]]
+ 00c3cbbc ["CALL", null, ["callee:00c57fd0:8"]]
- 00c3c794 bytes 0f6d0094
+ 00c3cbbc bytes 056d0094
- 00c3c588 ["INT_ADD", "register:40f0:8", ["const:c3c588:8", "const:4:8"]]
- 00c3c588 ["CALL", null, ["callee:00c3a178:8"]]
+ 00c3c9b0 ["INT_ADD", "register:40f0:8", ["const:c3c9b0:8", "const:4:8"]]
+ 00c3c9b0 ["CALL", null, ["callee:00c3a178:8"]]
- 00c3c588 bytes f2f5ff97
+ 00c3c9b0 bytes f2f5ff97
- 00c3c5b0 ["INT_ADD", "register:40f0:8", ["const:c3c5b0:8", "const:4:8"]]
- 00c3c5b0 ["CALL", null, ["callee:00c3fd7c:8"]]
+ 00c3c9d8 ["INT_ADD", "register:40f0:8", ["const:c3c9d8:8", "const:4:8"]]
+ 00c3c9d8 ["CALL", null, ["callee:00c3fd7c:8"]]
- 00c3c5b0 bytes e90c0094
+ 00c3c9d8 bytes e90c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

