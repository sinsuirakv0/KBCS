# v15.7.3 → v15.7.4 · 最優先の変更候補 (12)

[一覧の目次](README.md)

<a id="compare-113aecdc4358f171d6c3a718996a2866"></a>

### [`004fa888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa888.md) → [`004fa888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fa/004fa888.md) _ZNK5Botan14Cert_Extension10CRL_Number4copyEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa8d0",
      "incomplete_value": true,
      "site": "004fa8d8",
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
      "definition_site": "004fa8d0",
      "incomplete_value": true,
      "site": "004fa8d8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fa914",
      "incomplete_value": false,
      "site": "004fa91c",
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
            "const:69e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa914",
      "incomplete_value": false,
      "site": "004fa91c",
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
            "const:604:8"
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
      "definition_site": "004fa950",
      "incomplete_value": true,
      "site": "004fa95c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa950",
      "incomplete_value": true,
      "site": "004fa95c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f08:8"
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
      "004fa8c4",
      "READ",
      [
        "storage",
        "00c1b360",
        null,
        "pointer"
      ]
    ],
    [
      "004fa8d8",
      "DATA",
      [
        "storage",
        "00bebcb0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "004fa914",
      "PARAM",
      [
        "storage",
        "002a7604",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fa8c4",
      "READ",
      [
        "storage",
        "00c1b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "004fa8d8",
      "DATA",
      [
        "storage",
        "00bebd00",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "004fa914",
      "PARAM",
      [
        "storage",
        "002a769e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa888.md#insn-004fa8c4) · [`004fa914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa888.md#insn-004fa914) · [`004fa950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa888.md#insn-004fa950)
- 新版 `004fa8c4`（命令位置の公開資料なし） · `004fa914`（命令位置の公開資料なし） · `004fa950`（命令位置の公開資料なし）

~~~diff
- 004fa8c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:360:8"]]
- 004fa8c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa8c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3b0:8"]]
+ 004fa8c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fa8c4 bytes 08b141f9
+ 004fa8c4 bytes 08d941f9
- 004fa914 ["COPY", "tmp:0:8", ["const:604:8"]]
- 004fa914 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004fa914 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004fa914 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fa914 ["COPY", "tmp:0:8", ["const:69e:8"]]
+ 004fa914 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa914 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa914 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004fa914 bytes 21101891
+ 004fa914 bytes 21781a91
- 004fa950 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004fa950 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa950 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004fa950 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004fa950 bytes 218447f9
+ 004fa950 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f1f75ee29d1bf5d2c528b8926ce87ed"></a>

### [`004fa9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa9b0.md) → [`004fa9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fa/004fa9b0.md) _ZNK5Botan14Cert_Extension10CRL_Number12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004faa28",
      "incomplete_value": true,
      "site": "004faa28",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004faa28",
      "incomplete_value": true,
      "site": "004faa28",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004faaa0",
      "incomplete_value": true,
      "site": "004faaa0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004faaa0",
      "incomplete_value": true,
      "site": "004faaa0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004faa18",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004faa90",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004faa18",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004faa90",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004faa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa9b0.md#insn-004faa18) · [`004faa90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa9b0.md#insn-004faa90)
- 新版 `004faa18`（命令位置の公開資料なし） · `004faa90`（命令位置の公開資料なし）

~~~diff
- 004faa18 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004faa18 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004faa18 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004faa18 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004faa18 bytes c99643f9
+ 004faa18 bytes c9be43f9
- 004faa90 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004faa90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004faa90 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004faa90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004faa90 bytes c99643f9
+ 004faa90 bytes c9be43f9
~~~


<a id="compare-3b2d00448ecc8ec48e9ead4a33ed2a66"></a>

### [`004fabf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fabf4.md) → [`004fabf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fa/004fabf4.md) _ZNK5Botan14Cert_Extension10CRL_Number11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb940.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fac14",
      "incomplete_value": true,
      "site": "004fac30",
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
                "const:29b000:8"
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
    "old": {
      "definition_site": "004fac14",
      "incomplete_value": true,
      "site": "004fac30",
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
                "const:29b000:8"
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
      "004fac14",
      "READ",
      [
        "storage",
        "0029b350",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fac14",
      "READ",
      [
        "storage",
        "0029b34e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fac0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fabf4.md#insn-004fac0c)
- 新版 `004fac0c`（命令位置の公開資料なし）

~~~diff
- 004fac0c ["COPY", "tmp:0:8", ["const:350:8"]]
- 004fac0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004fac0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004fac0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004fac0c ["COPY", "tmp:0:8", ["const:34e:8"]]
+ 004fac0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004fac0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004fac0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004fac0c bytes 29410d91
+ 004fac0c bytes 29390d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-653e73168383d26fb2afc0798ff7e956"></a>

### [`004faccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faccc.md) → [`004faccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fa/004faccc.md) _ZNK5Botan14Cert_Extension14CRL_ReasonCode12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fad44",
      "incomplete_value": true,
      "site": "004fad44",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fad44",
      "incomplete_value": true,
      "site": "004fad44",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fadbc",
      "incomplete_value": true,
      "site": "004fadbc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fadbc",
      "incomplete_value": true,
      "site": "004fadbc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fad34",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004fadac",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fad34",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004fadac",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fad34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faccc.md#insn-004fad34) · [`004fadac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faccc.md#insn-004fadac)
- 新版 `004fad34`（命令位置の公開資料なし） · `004fadac`（命令位置の公開資料なし）

~~~diff
- 004fad34 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004fad34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fad34 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004fad34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fad34 bytes c99643f9
+ 004fad34 bytes c9be43f9
- 004fadac ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004fadac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fadac ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004fadac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fadac bytes c99643f9
+ 004fadac bytes c9be43f9
~~~


<a id="compare-a5a0695f4298a28e0f0a65768499480c"></a>

### [`004faf14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faf14.md) → [`004faf14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fa/004faf14.md) _ZNK5Botan14Cert_Extension14CRL_ReasonCode11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb940.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004faf34",
      "incomplete_value": true,
      "site": "004faf5c",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:6b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004faf34",
      "incomplete_value": true,
      "site": "004faf5c",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:61e:8"
              ]
            ]
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
      "004faf34",
      "READ",
      [
        "storage",
        "002a761e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004faf34",
      "READ",
      [
        "storage",
        "002a76b8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004faf2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faf14.md#insn-004faf2c)
- 新版 `004faf2c`（命令位置の公開資料なし）

~~~diff
- 004faf2c ["COPY", "tmp:0:8", ["const:61e:8"]]
- 004faf2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004faf2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004faf2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004faf2c ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 004faf2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004faf2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004faf2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004faf2c bytes 4a791891
+ 004faf2c bytes 4ae11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d528e1cd878941cbc41ce9f651b679e9"></a>

### [`004faff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faff8.md) → [`004faff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fa/004faff8.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points12encode_innerEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb038",
      "incomplete_value": true,
      "site": "004fb04c",
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
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:49d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fb038",
      "incomplete_value": true,
      "site": "004fb04c",
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
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:49f:8"
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
      "definition_site": "004fb038",
      "incomplete_value": true,
      "site": "004fb04c",
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
      "definition_site": "004fb038",
      "incomplete_value": true,
      "site": "004fb04c",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fb07c",
      "incomplete_value": true,
      "site": "004fb088",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fb07c",
      "incomplete_value": true,
      "site": "004fb088",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
      "004fb038",
      "READ",
      [
        "storage",
        "0029b49f",
        null,
        "string"
      ]
    ],
    [
      "004fb038",
      "READ",
      [
        "storage",
        "0029b4af",
        null,
        "string"
      ]
    ],
    [
      "004fb07c",
      "READ",
      [
        "storage",
        "00c1b190",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fb038",
      "READ",
      [
        "storage",
        "0029b49d",
        null,
        "string"
      ]
    ],
    [
      "004fb038",
      "READ",
      [
        "storage",
        "0029b4ad",
        null,
        "string"
      ]
    ],
    [
      "004fb07c",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faff8.md#insn-004fb030) · [`004fb034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faff8.md#insn-004fb034)
- 新版 `004fb030`（命令位置の公開資料なし） · `004fb034`（命令位置の公開資料なし）

~~~diff
- 004fb030 ["COPY", "tmp:0:8", ["const:49f:8"]]
- 004fb030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fb030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fb030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fb030 ["COPY", "tmp:0:8", ["const:49d:8"]]
+ 004fb030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fb030 bytes 087d1291
+ 004fb030 bytes 08751291
- 004fb034 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004fb034 bytes a9edffd0
+ 004fb034 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004fb034 bytes a9edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08cb9cfce9eee81cf17b71a0e3ad7693"></a>

### [`004fb0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb0d8.md) → [`004fb0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fb0d8.md) _ZN5Botan14Cert_Extension23CRL_Distribution_Points12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md)

変更の種類 call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.41% / 新版 96.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb3a4",
      "incomplete_value": true,
      "site": "004fb3ac",
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
      "definition_site": "004fb3a4",
      "incomplete_value": true,
      "site": "004fb3ac",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004fb3b4",
      "incomplete_value": true,
      "site": "004fb3b4",
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
                "const:20:8"
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
      "definition_site": "004fb3b4",
      "incomplete_value": true,
      "site": "004fb3b4",
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
                "const:20:8"
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
    "ordinal": 27,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb3b4",
      "incomplete_value": true,
      "site": "004fb3b4",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fb3b4",
      "incomplete_value": true,
      "site": "004fb3b4",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fb154",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004fb244",
      "PARAM",
      [
        "storage",
        "0029196e",
        null,
        null
      ]
    ],
    [
      "004fb3a0",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fb154",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004fb244",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        null
      ]
    ],
    [
      "004fb3a0",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb0d8.md#insn-004fb154) · [`004fb1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb0d8.md#insn-004fb1a0) · [`004fb3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb0d8.md#insn-004fb3a0)
- 新版 `004fb154`（命令位置の公開資料なし） · `004fb1a0`（命令位置の公開資料なし） · `004fb3a0`（命令位置の公開資料なし）

~~~diff
- 004fb154 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004fb154 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb154 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004fb154 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb154 bytes 299543f9
+ 004fb154 bytes 29bd43f9
- 004fb1a0 ["COPY", "tmp:0:8", ["const:96e:8"]]
- 004fb1a0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 004fb1a0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 004fb1a0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 004fb1a0 ["COPY", "tmp:0:8", ["const:8e1:8"]]
+ 004fb1a0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 004fb1a0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 004fb1a0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 004fb1a0 bytes b5ba2591
+ 004fb1a0 bytes b5862391
- 004fb3a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
- 004fb3a0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb3a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 004fb3a0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb3a0 bytes 73ea46f9
+ 004fb3a0 bytes 731247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db4e461a22843cf5c221a6cf09ae76a3"></a>

### [`004fb4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb4c0.md) → [`004fb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fb4c0.md) _ZN5Botan11BER_Decoder11decode_listINS_14Cert_Extension23CRL_Distribution_Points18Distribution_PointEEERS0_RNSt6__ndk16vectorIT_NS6_9allocat

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfc0.md) · 呼出先 11件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00517bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00517/00517bcc.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`00519bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519bb0.md) [`0051a694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051a/0051a694.md)
- 新版 呼出元 1件 [`00bdd010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd010.md) · 呼出先 11件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00517bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517bcc.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00519bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519bb0.md) [`0051a694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a694.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb524",
      "incomplete_value": true,
      "site": "004fb52c",
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
      "definition_site": "004fb524",
      "incomplete_value": true,
      "site": "004fb52c",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fb6dc",
      "incomplete_value": true,
      "site": "004fb6dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      "definition_site": "004fb6dc",
      "incomplete_value": true,
      "site": "004fb6dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fb514",
      "READ",
      [
        "storage",
        "00c1b3a8",
        null,
        "pointer"
      ]
    ],
    [
      "004fb518",
      "READ",
      [
        "storage",
        "00c1b288",
        null,
        "pointer"
      ]
    ],
    [
      "004fb52c",
      "DATA",
      [
        "storage",
        "00bebe18",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004fb514",
      "READ",
      [
        "storage",
        "00c1b3f8",
        null,
        "pointer"
      ]
    ],
    [
      "004fb518",
      "READ",
      [
        "storage",
        "00c1b2d8",
        null,
        "pointer"
      ]
    ],
    [
      "004fb52c",
      "DATA",
      [
        "storage",
        "00bebe68",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb4c0.md#insn-004fb514) · [`004fb518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb4c0.md#insn-004fb518) · [`004fb6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb4c0.md#insn-004fb6cc)
- 新版 `004fb514`（命令位置の公開資料なし） · `004fb518`（命令位置の公開資料なし） · `004fb6cc`（命令位置の公開資料なし）

~~~diff
- 004fb514 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a8:8"]]
- 004fb514 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb514 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f8:8"]]
+ 004fb514 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb514 bytes 08d541f9
+ 004fb514 bytes 08fd41f9
- 004fb518 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:288:8"]]
- 004fb518 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb518 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2d8:8"]]
+ 004fb518 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb518 bytes 294541f9
+ 004fb518 bytes 296d41f9
- 004fb6cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004fb6cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb6cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004fb6cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb6cc bytes 299543f9
+ 004fb6cc bytes 29bd43f9
~~~


<a id="compare-a1ebbc3dc333d337ebd1aaa359a9fa9b"></a>

### [`004fb79c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb79c.md) → [`004fb79c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fb79c.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb7dc",
      "incomplete_value": true,
      "site": "004fb7f0",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:70f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fb7dc",
      "incomplete_value": true,
      "site": "004fb7f0",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:675:8"
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
      "004fb7dc",
      "READ",
      [
        "storage",
        "002a9675",
        null,
        "string"
      ]
    ],
    [
      "004fb7e0",
      "READ",
      [
        "storage",
        "002a9682",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fb7dc",
      "READ",
      [
        "storage",
        "002a970f",
        null,
        "string"
      ]
    ],
    [
      "004fb7e0",
      "READ",
      [
        "storage",
        "002a971c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb79c.md#insn-004fb7d4)
- 新版 `004fb7d4`（命令位置の公開資料なし）

~~~diff
- 004fb7d4 ["COPY", "tmp:0:8", ["const:675:8"]]
- 004fb7d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fb7d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fb7d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fb7d4 ["COPY", "tmp:0:8", ["const:70f:8"]]
+ 004fb7d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb7d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb7d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fb7d4 bytes 08d51991
+ 004fb7d4 bytes 083d1c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b668d4abfd5482fad8186c19933dcd1f"></a>

### [`004fb898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb898.md) → [`004fb898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fb898.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points18Distribution_Point11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb8d8",
      "incomplete_value": true,
      "site": "004fb8ec",
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
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:49d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fb8d8",
      "incomplete_value": true,
      "site": "004fb8ec",
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
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:49f:8"
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
      "definition_site": "004fb8d8",
      "incomplete_value": true,
      "site": "004fb8ec",
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
      "definition_site": "004fb8d8",
      "incomplete_value": true,
      "site": "004fb8ec",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fb91c",
      "incomplete_value": true,
      "site": "004fb928",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fb91c",
      "incomplete_value": true,
      "site": "004fb928",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
      "004fb8d8",
      "READ",
      [
        "storage",
        "0029b49f",
        null,
        "string"
      ]
    ],
    [
      "004fb8d8",
      "READ",
      [
        "storage",
        "0029b4af",
        null,
        "string"
      ]
    ],
    [
      "004fb91c",
      "READ",
      [
        "storage",
        "00c1b190",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fb8d8",
      "READ",
      [
        "storage",
        "0029b49d",
        null,
        "string"
      ]
    ],
    [
      "004fb8d8",
      "READ",
      [
        "storage",
        "0029b4ad",
        null,
        "string"
      ]
    ],
    [
      "004fb91c",
      "READ",
      [
        "storage",
        "00c1b1e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb898.md#insn-004fb8d0) · [`004fb8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb898.md#insn-004fb8d4)
- 新版 `004fb8d0`（命令位置の公開資料なし） · `004fb8d4`（命令位置の公開資料なし）

~~~diff
- 004fb8d0 ["COPY", "tmp:0:8", ["const:49f:8"]]
- 004fb8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fb8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fb8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fb8d0 ["COPY", "tmp:0:8", ["const:49d:8"]]
+ 004fb8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fb8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fb8d0 bytes 087d1291
+ 004fb8d0 bytes 08751291
- 004fb8d4 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 004fb8d4 bytes a9edffd0
+ 004fb8d4 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004fb8d4 bytes a9edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18535b8221bbef456a2241d743491442"></a>

### [`004fb978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb978.md) → [`004fb978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fb978.md) _ZN5Botan14Cert_Extension23CRL_Distribution_Points18Distribution_Point11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fba94",
      "incomplete_value": true,
      "site": "004fba94",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fba94",
      "incomplete_value": true,
      "site": "004fba94",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fbad8",
      "incomplete_value": true,
      "site": "004fbad8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fbad8",
      "incomplete_value": true,
      "site": "004fbad8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fba84",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004fbac8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fba84",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004fbac8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fba84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb978.md#insn-004fba84) · [`004fbac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb978.md#insn-004fbac8)
- 新版 `004fba84`（命令位置の公開資料なし） · `004fbac8`（命令位置の公開資料なし）

~~~diff
- 004fba84 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004fba84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fba84 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004fba84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fba84 bytes a99643f9
+ 004fba84 bytes a9be43f9
- 004fbac8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004fbac8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fbac8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004fbac8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fbac8 bytes a99643f9
+ 004fbac8 bytes a9be43f9
~~~


<a id="compare-c20be7394b2b01186ac0badc9fc28375"></a>

### [`004fbd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbd34.md) → [`004fbd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fbd34.md) FUN_004fbd34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbd74",
      "incomplete_value": true,
      "site": "004fbd8c",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:50b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fbd74",
      "incomplete_value": true,
      "site": "004fbd8c",
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
                "const:2a2000:8"
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbd74",
      "incomplete_value": true,
      "site": "004fbd8c",
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
      "definition_site": "004fbd74",
      "incomplete_value": true,
      "site": "004fbd8c",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbd90",
      "incomplete_value": true,
      "site": "004fbd90",
      "value": [
        "LOAD",
        "8",
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
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fbd90",
      "incomplete_value": true,
      "site": "004fbd90",
      "value": [
        "LOAD",
        "8",
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
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fbd74",
      "READ",
      [
        "storage",
        "002a2480",
        null,
        "string"
      ]
    ],
    [
      "004fbd74",
      "READ",
      [
        "storage",
        "002a2490",
        null,
        "string"
      ]
    ],
    [
      "004fbd7c",
      "READ",
      [
        "storage",
        "002a249f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fbd74",
      "READ",
      [
        "storage",
        "002a250b",
        null,
        "string"
      ]
    ],
    [
      "004fbd74",
      "READ",
      [
        "storage",
        "002a251b",
        null,
        "string"
      ]
    ],
    [
      "004fbd7c",
      "READ",
      [
        "storage",
        "002a252a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fbd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbd34.md#insn-004fbd6c) · [`004fbd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbd34.md#insn-004fbd70)
- 新版 `004fbd6c`（命令位置の公開資料なし） · `004fbd70`（命令位置の公開資料なし）

~~~diff
- 004fbd6c ["COPY", "tmp:0:8", ["const:480:8"]]
- 004fbd6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fbd6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fbd6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fbd6c ["COPY", "tmp:0:8", ["const:50b:8"]]
+ 004fbd6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fbd6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fbd6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fbd6c bytes 08011291
+ 004fbd6c bytes 082d1491
- 004fbd70 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 004fbd70 bytes a9edffb0
+ 004fbd70 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 004fbd70 bytes a9edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f01f76a5b4758216e17441fe63e2d903"></a>

### [`004fbef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbef4.md) → [`004fbef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fbef4.md) FUN_004fbef4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`004dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc2c8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`004dc2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc2c8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fc078",
      "incomplete_value": true,
      "site": "004fc080",
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
      "definition_site": "004fc078",
      "incomplete_value": true,
      "site": "004fc080",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004fc088",
      "incomplete_value": true,
      "site": "004fc088",
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
                "const:50:8"
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
      "definition_site": "004fc088",
      "incomplete_value": true,
      "site": "004fc088",
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
                "const:50:8"
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
    "ordinal": 18,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fc088",
      "incomplete_value": true,
      "site": "004fc088",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc088",
      "incomplete_value": true,
      "site": "004fc088",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
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
      "004fbfbc",
      "PARAM",
      [
        "storage",
        "0029196e",
        null,
        null
      ]
    ],
    [
      "004fc074",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "004fc078",
      "READ",
      [
        "storage",
        "00c132f0",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004fbfbc",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        null
      ]
    ],
    [
      "004fc074",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "004fc078",
      "READ",
      [
        "storage",
        "00c13340",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fbf58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbef4.md#insn-004fbf58) · [`004fc074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbef4.md#insn-004fc074) · [`004fc090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbef4.md#insn-004fc090)
- 新版 `004fbf58`（命令位置の公開資料なし） · `004fc074`（命令位置の公開資料なし） · `004fc090`（命令位置の公開資料なし）

~~~diff
- 004fbf58 ["COPY", "tmp:0:8", ["const:96e:8"]]
- 004fbf58 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 004fbf58 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 004fbf58 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 004fbf58 ["COPY", "tmp:0:8", ["const:8e1:8"]]
+ 004fbf58 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 004fbf58 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 004fbf58 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 004fbf58 bytes b5ba2591
+ 004fbf58 bytes b5862391
- 004fc074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd0:8"]]
- 004fc074 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fc074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 004fc074 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 004fc074 bytes 73ea46f9
+ 004fc074 bytes 731247f9
- 004fc090 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 004fc090 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fc090 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004fc090 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fc090 bytes 08c146f9
+ 004fc090 bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b59ce1fbd76017e64ccf84fb2554a108"></a>

### [`004fc31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc31c.md) → [`004fc31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc31c.md) _ZN5Botan11X509_Object11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00482aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482aa8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md) [`00bdb870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb870.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00482aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482aa8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) [`00bdb8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8c0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fc3ec",
      "incomplete_value": true,
      "site": "004fc3ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc3ec",
      "incomplete_value": true,
      "site": "004fc3ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fc430",
      "incomplete_value": true,
      "site": "004fc430",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc430",
      "incomplete_value": true,
      "site": "004fc430",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fc3dc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004fc420",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fc3dc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004fc420",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fc3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc31c.md#insn-004fc3dc) · [`004fc420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc31c.md#insn-004fc420)
- 新版 `004fc3dc`（命令位置の公開資料なし） · `004fc420`（命令位置の公開資料なし）

~~~diff
- 004fc3dc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004fc3dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fc3dc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004fc3dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fc3dc bytes c99643f9
+ 004fc3dc bytes c9be43f9
- 004fc420 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 004fc420 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fc420 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 004fc420 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fc420 bytes c99643f9
+ 004fc420 bytes c9be43f9
~~~


<a id="compare-31d2afd50a99fecfd7cfac028a67e175"></a>

### [`004fc6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md) → [`004fc6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc6ac.md) _ZNK5Botan11X509_Object23hash_used_for_signatureEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcff0.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004fcb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c98.md)
- 新版 呼出元 1件 [`00bdd040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd040.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004fcb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fcb38.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c98.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004fc6e8",
      "incomplete_value": false,
      "site": "004fc6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc6e8",
      "incomplete_value": false,
      "site": "004fc6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "004fc94c",
      "incomplete_value": false,
      "site": "004fc958",
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
            "const:533:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc94c",
      "incomplete_value": false,
      "site": "004fc958",
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
            "const:4a8:8"
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
      "definition_site": "004fc9a0",
      "incomplete_value": true,
      "site": "004fc9ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
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
      "definition_site": "004fc9a0",
      "incomplete_value": true,
      "site": "004fc9ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:fb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fc6f0",
      "DATA",
      [
        "storage",
        "00bed6a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004fc734",
      "READ",
      [
        "storage",
        "00bed6c0",
        null,
        "pointer"
      ]
    ],
    [
      "004fc734",
      "READ",
      [
        "storage",
        "00bed6c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004fc6f0",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004fc734",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      "004fc734",
      "READ",
      [
        "storage",
        "00bed718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fc6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md#insn-004fc6e8) · [`004fc94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md#insn-004fc94c) · [`004fc994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md#insn-004fc994)
- 新版 `004fc6e8`（命令位置の公開資料なし） · `004fc94c`（命令位置の公開資料なし） · `004fc994`（命令位置の公開資料なし）

~~~diff
- 004fc6e8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 004fc6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fc6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fc6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fc6e8 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 004fc6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fc6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fc6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fc6e8 bytes 08811a91
+ 004fc6e8 bytes 08c11b91
- 004fc94c ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 004fc94c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004fc94c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004fc94c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004fc94c ["COPY", "tmp:0:8", ["const:533:8"]]
+ 004fc94c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004fc94c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004fc94c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004fc94c bytes 42a01291
+ 004fc94c bytes 42cc1491
- 004fc994 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004fc994 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004fc994 bytes e13800d0
+ 004fc994 bytes e13800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-255c4722579c756662bde44e02def368"></a>

### [`004fcb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md) → [`004fcb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fcb38.md) FUN_004fcb38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004fc6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md) [`004fd178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fd178.md) · 呼出先 15件 [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`004fc6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fc6ac.md) [`004fd178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fd178.md) · 呼出先 15件 [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.01% / 新版 96.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fcb78",
      "incomplete_value": true,
      "site": "004fcb78",
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
      "definition_site": "004fcb78",
      "incomplete_value": true,
      "site": "004fcb78",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fce20",
      "incomplete_value": true,
      "site": "004fce20",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
      "definition_site": "004fce20",
      "incomplete_value": true,
      "site": "004fce20",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 26,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fcea4",
      "incomplete_value": true,
      "site": "004fcea4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
      "definition_site": "004fcea4",
      "incomplete_value": true,
      "site": "004fcea4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
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
    "ordinal": 33,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fcb60",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004fcb78",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004fcba4",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004fcb60",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004fcb78",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004fcba4",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fcb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md#insn-004fcb60) · [`004fce10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md#insn-004fce10) · [`004fce94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md#insn-004fce94)
- 新版 `004fcb60`（命令位置の公開資料なし） · `004fce10`（命令位置の公開資料なし） · `004fce94`（命令位置の公開資料なし）

~~~diff
- 004fcb60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ef8:8"]]
- 004fcb60 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fcb60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f48:8"]]
+ 004fcb60 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 004fcb60 bytes 947e47f9
+ 004fcb60 bytes 94a647f9
- 004fce10 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 004fce10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fce10 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 004fce10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fce10 bytes e99643f9
+ 004fce10 bytes e9be43f9
- 004fce94 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 004fce94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fce94 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 004fce94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fce94 bytes e99643f9
+ 004fce94 bytes e9be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34148bdefc71b25de90ca74d1a728991"></a>

### [`004fd178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fd178.md) → [`004fd178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fd178.md) _ZNK5Botan11X509_Object16verify_signatureERKNS_10Public_KeyE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdce10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce10.md) · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00483d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483d44.md) [`00489d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489d4c.md) [`004fcb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md) [`00524c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c3c.md)
- 新版 呼出元 1件 [`00bdce60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce60.md) · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00483d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483d44.md) [`00489d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489d4c.md) [`004fcb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fc/004fcb38.md) [`00524c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c3c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.47% / 新版 98.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004fd1c0",
      "incomplete_value": false,
      "site": "004fd1c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fd1c0",
      "incomplete_value": false,
      "site": "004fd1c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "004fd554",
      "incomplete_value": false,
      "site": "004fd55c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:d14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fd554",
      "incomplete_value": false,
      "site": "004fd55c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:da1:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fd620",
      "incomplete_value": false,
      "site": "004fd62c",
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
            "const:5cf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fd620",
      "incomplete_value": false,
      "site": "004fd62c",
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
            "const:544:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fd1c0",
      "DATA",
      [
        "storage",
        "00bed6a0",
        null,
        "undefined *"
      ]
    ],
    [
      "004fd204",
      "READ",
      [
        "storage",
        "00bed6c0",
        null,
        "pointer"
      ]
    ],
    [
      "004fd204",
      "READ",
      [
        "storage",
        "00bed6c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004fd1c0",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004fd204",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      "004fd204",
      "READ",
      [
        "storage",
        "00bed718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fd1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fd178.md#insn-004fd1b8) · [`004fd554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fd178.md#insn-004fd554) · [`004fd620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fd178.md#insn-004fd620)
- 新版 `004fd1b8`（命令位置の公開資料なし） · `004fd554`（命令位置の公開資料なし） · `004fd620`（命令位置の公開資料なし）

~~~diff
- 004fd1b8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 004fd1b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004fd1b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004fd1b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004fd1b8 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 004fd1b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004fd1b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004fd1b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004fd1b8 bytes 08811a91
+ 004fd1b8 bytes 08c11b91
- 004fd554 ["COPY", "tmp:0:8", ["const:da1:8"]]
- 004fd554 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004fd554 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004fd554 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fd554 ["COPY", "tmp:0:8", ["const:d14:8"]]
+ 004fd554 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fd554 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fd554 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004fd554 bytes 21843691
+ 004fd554 bytes 21503491
- 004fd620 ["COPY", "tmp:0:8", ["const:544:8"]]
- 004fd620 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004fd620 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004fd620 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fd620 ["COPY", "tmp:0:8", ["const:5cf:8"]]
+ 004fd620 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fd620 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fd620 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004fd620 bytes 00101591
+ 004fd620 bytes 003c1791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-012a754f8d42263b921afa84090883b3"></a>

### [`004fdb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdb0c.md) → [`004fdb0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdb0c.md) _ZNK5Botan16X509_Certificate9PEM_labelEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "004fdb30",
      "incomplete_value": true,
      "site": "004fdb30",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:725:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fdb30",
      "incomplete_value": true,
      "site": "004fdb30",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:68b:8"
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
      "004fdb20",
      "READ",
      [
        "storage",
        "002a968b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fdb20",
      "READ",
      [
        "storage",
        "002a9725",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fdb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdb0c.md#insn-004fdb14)
- 新版 `004fdb14`（命令位置の公開資料なし）

~~~diff
- 004fdb14 ["COPY", "tmp:0:8", ["const:68b:8"]]
- 004fdb14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004fdb14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004fdb14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004fdb14 ["COPY", "tmp:0:8", ["const:725:8"]]
+ 004fdb14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004fdb14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004fdb14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004fdb14 bytes 4a2d1a91
+ 004fdb14 bytes 4a951c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1ff88e80262ca738dcf7bd2afadc9a6"></a>

### [`004fdb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdb38.md) → [`004fdb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdb38.md) _ZNK5Botan16X509_Certificate20alternate_PEM_labelsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fdb5c",
      "incomplete_value": true,
      "site": "004fdb6c",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:6db:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fdb5c",
      "incomplete_value": true,
      "site": "004fdb6c",
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
                "const:2a1000:8"
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
      "004fdb5c",
      "READ",
      [
        "storage",
        "002a1650",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fdb5c",
      "READ",
      [
        "storage",
        "002a16db",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fdb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdb38.md#insn-004fdb50)
- 新版 `004fdb50`（命令位置の公開資料なし）

~~~diff
- 004fdb50 ["COPY", "tmp:0:8", ["const:650:8"]]
- 004fdb50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004fdb50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004fdb50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004fdb50 ["COPY", "tmp:0:8", ["const:6db:8"]]
+ 004fdb50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004fdb50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004fdb50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004fdb50 bytes 29411991
+ 004fdb50 bytes 296d1b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6372619d99722bf16882e25a8f261bfd"></a>

### [`004fdbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdbe0.md) → [`004fdbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdbe0.md) _ZN5Botan16X509_CertificateC2ERNS_10DataSourceE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdcde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcde0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) [`00bdce30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fdc20",
      "incomplete_value": true,
      "site": "004fdc20",
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
      "definition_site": "004fdc20",
      "incomplete_value": true,
      "site": "004fdc20",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fdc20",
      "incomplete_value": true,
      "site": "004fdc20",
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
      "definition_site": "004fdc20",
      "incomplete_value": true,
      "site": "004fdc20",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fdc60",
      "incomplete_value": true,
      "site": "004fdc68",
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
      "definition_site": "004fdc60",
      "incomplete_value": true,
      "site": "004fdc68",
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
      "004fdc00",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004fdc08",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004fdc20",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004fdc00",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "004fdc08",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004fdc20",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fdc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdbe0.md#insn-004fdc00) · [`004fdc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdbe0.md#insn-004fdc08) · [`004fdc54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdbe0.md#insn-004fdc54)
- 新版 `004fdc00`（命令位置の公開資料なし） · `004fdc08`（命令位置の公開資料なし） · `004fdc54`（命令位置の公開資料なし）

~~~diff
- 004fdc00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004fdc00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdc00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 004fdc00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdc00 bytes 088d41f9
+ 004fdc00 bytes 08b541f9
- 004fdc08 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
- 004fdc08 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdc08 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:f48:8"]]
+ 004fdc08 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdc08 bytes 4a7d47f9
+ 004fdc08 bytes 4aa547f9
- 004fdc54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 004fdc54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdc54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
+ 004fdc54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdc54 bytes 085141f9
+ 004fdc54 bytes 087941f9
~~~


<a id="compare-417ba61e8e37facd292ce21daf8290c5"></a>

### [`004fdd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdd34.md) → [`004fdd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdd34.md) _ZN5Botan16X509_CertificateC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd20.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d4f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 1件 [`00bdcd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd70.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fdd74",
      "incomplete_value": true,
      "site": "004fdd74",
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
      "definition_site": "004fdd74",
      "incomplete_value": true,
      "site": "004fdd74",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fdd74",
      "incomplete_value": true,
      "site": "004fdd74",
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
      "definition_site": "004fdd74",
      "incomplete_value": true,
      "site": "004fdd74",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fddbc",
      "incomplete_value": true,
      "site": "004fddc8",
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
      "definition_site": "004fddbc",
      "incomplete_value": true,
      "site": "004fddc8",
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
      "004fdd54",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004fdd5c",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004fdd74",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004fdd54",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "004fdd5c",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004fdd74",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fdd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdd34.md#insn-004fdd54) · [`004fdd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdd34.md#insn-004fdd5c) · [`004fddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdd34.md#insn-004fddb0)
- 新版 `004fdd54`（命令位置の公開資料なし） · `004fdd5c`（命令位置の公開資料なし） · `004fddb0`（命令位置の公開資料なし）

~~~diff
- 004fdd54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004fdd54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdd54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 004fdd54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdd54 bytes 088d41f9
+ 004fdd54 bytes 08b541f9
- 004fdd5c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
- 004fdd5c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdd5c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:f48:8"]]
+ 004fdd5c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdd5c bytes 4a7d47f9
+ 004fdd5c bytes 4aa547f9
- 004fddb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 004fddb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fddb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
+ 004fddb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fddb0 bytes 085141f9
+ 004fddb0 bytes 087941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-736f05f663b81279dbb9d2c86f7f8279"></a>

### [`004fdeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdeac.md) → [`004fdeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdeac.md) _ZN5Botan16X509_CertificateC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcbc0.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) [`00bdc7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7c0.md) [`00bdc7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc7d0.md)
- 新版 呼出元 1件 [`00bdcc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc10.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) [`00bdc810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md) [`00bdc820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fdeec",
      "incomplete_value": true,
      "site": "004fdeec",
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
      "definition_site": "004fdeec",
      "incomplete_value": true,
      "site": "004fdeec",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fdeec",
      "incomplete_value": true,
      "site": "004fdeec",
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
      "definition_site": "004fdeec",
      "incomplete_value": true,
      "site": "004fdeec",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fdf2c",
      "incomplete_value": true,
      "site": "004fdf34",
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
      "definition_site": "004fdf2c",
      "incomplete_value": true,
      "site": "004fdf34",
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
      "004fdecc",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "004fded4",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004fdeec",
      "DATA",
      [
        "storage",
        "00beca10",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "004fdecc",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "004fded4",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004fdeec",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fdecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdeac.md#insn-004fdecc) · [`004fded4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdeac.md#insn-004fded4) · [`004fdf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdeac.md#insn-004fdf20)
- 新版 `004fdecc`（命令位置の公開資料なし） · `004fded4`（命令位置の公開資料なし） · `004fdf20`（命令位置の公開資料なし）

~~~diff
- 004fdecc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004fdecc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdecc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 004fdecc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdecc bytes 088d41f9
+ 004fdecc bytes 08b541f9
- 004fded4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ef8:8"]]
- 004fded4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fded4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:f48:8"]]
+ 004fded4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 004fded4 bytes 4a7d47f9
+ 004fded4 bytes 4aa547f9
- 004fdf20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 004fdf20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fdf20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
+ 004fdf20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fdf20 bytes 085141f9
+ 004fdf20 bytes 087941f9
~~~


<a id="compare-d28ce8286445cdc6cf4ac8be911c6f10"></a>

### [`004fdfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdfd8.md) → [`004fdfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdfd8.md) _ZN5Botan16X509_Certificate12force_decodeEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 68件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md)
- 新版 呼出元 0件  · 呼出先 68件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `call_target` 8件, `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fe27c",
      "incomplete_value": true,
      "site": "004fe280",
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
      "definition_site": "004fe27c",
      "incomplete_value": true,
      "site": "004fe280",
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
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004fe348",
      "incomplete_value": false,
      "site": "004fe348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fe348",
      "incomplete_value": false,
      "site": "004fe348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fe790",
      "incomplete_value": true,
      "site": "004fe790",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:418:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fe790",
      "incomplete_value": true,
      "site": "004fe790",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:38d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 71,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fe150",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004fe274",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "004fe280",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004fe150",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004fe274",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004fe280",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fe150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdfd8.md#insn-004fe150) · [`004fe274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdfd8.md#insn-004fe274) · [`004fe314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdfd8.md#insn-004fe314)
- 新版 `004fe150`（命令位置の公開資料なし） · `004fe274`（命令位置の公開資料なし） · `004fe314`（命令位置の公開資料なし）

~~~diff
- 004fe150 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004fe150 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fe150 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004fe150 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fe150 bytes 299743f9
+ 004fe150 bytes 29bf43f9
- 004fe274 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
- 004fe274 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fe274 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 004fe274 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fe274 bytes 087d47f9
+ 004fe274 bytes 08a547f9
- 004fe314 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 004fe314 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fe314 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 004fe314 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fe314 bytes 299743f9
+ 004fe314 bytes 29bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a16378ce93f27e1ef635eace4828d805"></a>

### [`004ff98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ff98c.md) → [`004ff98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ff98c.md) _ZNK5Botan16X509_Certificate4dataEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb50.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

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
      "definition_site": "004ff9ec",
      "incomplete_value": false,
      "site": "004ff9f4",
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
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ff9ec",
      "incomplete_value": false,
      "site": "004ff9f4",
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
            "const:66a:8"
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
      "definition_site": "004ffa28",
      "incomplete_value": true,
      "site": "004ffa34",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ffa28",
      "incomplete_value": true,
      "site": "004ffa34",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f08:8"
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
      "004ff9ec",
      "PARAM",
      [
        "storage",
        "002a066a",
        null,
        "string"
      ]
    ],
    [
      "004ffa28",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "004ffa28",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ff9ec",
      "PARAM",
      [
        "storage",
        "002a06f5",
        null,
        "string"
      ]
    ],
    [
      "004ffa28",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004ffa28",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ff9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ff98c.md#insn-004ff9ec) · [`004ffa28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ff98c.md#insn-004ffa28)
- 新版 `004ff9ec`（命令位置の公開資料なし） · `004ffa28`（命令位置の公開資料なし）

~~~diff
- 004ff9ec ["COPY", "tmp:0:8", ["const:66a:8"]]
- 004ff9ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004ff9ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004ff9ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004ff9ec ["COPY", "tmp:0:8", ["const:6f5:8"]]
+ 004ff9ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004ff9ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004ff9ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004ff9ec bytes 21a81991
+ 004ff9ec bytes 21d41b91
- 004ffa28 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 004ffa28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ffa28 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 004ffa28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ffa28 bytes 218447f9
+ 004ffa28 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6337d1abd443037568c6772540bc232"></a>

### [`004ffc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ffc88.md) → [`004ffc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ffc88.md) _ZNK5Botan16X509_Certificate13allowed_usageENS_10Usage_TypeE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd000.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdcb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb50.md) [`00bdcda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcda0.md)
- 新版 呼出元 1件 [`00bdd050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd050.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md) [`00bdcdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdf0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffd14",
      "incomplete_value": true,
      "site": "004ffd20",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:40d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ffd14",
      "incomplete_value": true,
      "site": "004ffd20",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:382:8"
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
      "definition_site": "004ffe50",
      "incomplete_value": true,
      "site": "004ffe50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:4aa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ffe50",
      "incomplete_value": true,
      "site": "004ffe50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:410:8"
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
      "definition_site": "004ffe44",
      "incomplete_value": true,
      "site": "004ffe54",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ffe44",
      "incomplete_value": true,
      "site": "004ffe54",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
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
      "004ffd14",
      "READ",
      [
        "storage",
        "002a4382",
        null,
        "string"
      ]
    ],
    [
      "004ffe40",
      "READ",
      [
        "storage",
        "002a9410",
        null,
        "string"
      ]
    ],
    [
      "004ffe44",
      "READ",
      [
        "storage",
        "002a9417",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ffd14",
      "READ",
      [
        "storage",
        "002a440d",
        null,
        "string"
      ]
    ],
    [
      "004ffe40",
      "READ",
      [
        "storage",
        "002a94aa",
        null,
        "string"
      ]
    ],
    [
      "004ffe44",
      "READ",
      [
        "storage",
        "002a94b1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ffd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ffc88.md#insn-004ffd0c) · [`004ffe38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ff/004ffc88.md#insn-004ffe38)
- 新版 `004ffd0c`（命令位置の公開資料なし） · `004ffe38`（命令位置の公開資料なし）

~~~diff
- 004ffd0c ["COPY", "tmp:0:8", ["const:382:8"]]
- 004ffd0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ffd0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ffd0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ffd0c ["COPY", "tmp:0:8", ["const:40d:8"]]
+ 004ffd0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ffd0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ffd0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ffd0c bytes 29090e91
+ 004ffd0c bytes 29351091
- 004ffe38 ["COPY", "tmp:0:8", ["const:410:8"]]
- 004ffe38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ffe38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ffe38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ffe38 ["COPY", "tmp:0:8", ["const:4aa:8"]]
+ 004ffe38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ffe38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ffe38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ffe38 bytes 29411091
+ 004ffe38 bytes 29a91291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94bbc319eab46f79af88a3860ac0a53a"></a>

### [`005001f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00500/005001f4.md) → [`005001f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00500/005001f4.md) _ZNK5Botan16X509_Certificate12subject_infoERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd010.md) · 呼出先 16件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`005251c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/005251c0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdd060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd060.md) · 呼出先 16件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`005251c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005251c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.32% / 新版 99.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00500528",
      "incomplete_value": false,
      "site": "00500530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:4be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00500528",
      "incomplete_value": false,
      "site": "00500530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
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
      "definition_site": "00500564",
      "incomplete_value": false,
      "site": "0050056c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00500564",
      "incomplete_value": false,
      "site": "0050056c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:56d:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005005a0",
      "incomplete_value": false,
      "site": "005005a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:b23:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005005a0",
      "incomplete_value": false,
      "site": "005005a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "00500528",
      "PARAM",
      [
        "storage",
        "0029b4c0",
        null,
        "string"
      ]
    ],
    [
      "00500564",
      "PARAM",
      [
        "storage",
        "002a456d",
        null,
        "string"
      ]
    ],
    [
      "005005a0",
      "PARAM",
      [
        "storage",
        "00291bb0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00500528",
      "PARAM",
      [
        "storage",
        "0029b4be",
        null,
        "string"
      ]
    ],
    [
      "00500564",
      "PARAM",
      [
        "storage",
        "002a45f8",
        null,
        "string"
      ]
    ],
    [
      "005005a0",
      "PARAM",
      [
        "storage",
        "00291b23",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00500528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00500/005001f4.md#insn-00500528) · [`00500564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00500/005001f4.md#insn-00500564) · [`005005a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00500/005001f4.md#insn-005005a0)
- 新版 `00500528`（命令位置の公開資料なし） · `00500564`（命令位置の公開資料なし） · `005005a0`（命令位置の公開資料なし）

~~~diff
- 00500528 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00500528 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00500528 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00500528 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00500528 ["COPY", "tmp:0:8", ["const:4be:8"]]
+ 00500528 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00500528 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00500528 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00500528 bytes 21001391
+ 00500528 bytes 21f81291
- 00500564 ["COPY", "tmp:0:8", ["const:56d:8"]]
- 00500564 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00500564 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00500564 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00500564 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00500564 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00500564 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00500564 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00500564 bytes 21b41591
+ 00500564 bytes 21e01791
- 005005a0 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 005005a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005005a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005005a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005005a0 ["COPY", "tmp:0:8", ["const:b23:8"]]
+ 005005a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005005a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005005a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005005a0 bytes 21c02e91
+ 005005a0 bytes 218c2c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51d6c2c3785e9221c59664cf7d41c705"></a>

### [`00501b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/00501b08.md) → [`00501b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00501/00501b08.md) _ZNK5Botan16X509_Certificate9to_stringEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 27件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`0051bf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051b/0051bf98.md)
- 新版 呼出元 0件  · 呼出先 27件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`0051bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bf98.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.37% / 新版 93.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 43件, `store_destination` 2件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00501b4c",
      "incomplete_value": true,
      "site": "00501b60",
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
      "definition_site": "00501b4c",
      "incomplete_value": true,
      "site": "00501b60",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00501b58",
      "incomplete_value": true,
      "site": "00501b64",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00501b58",
      "incomplete_value": true,
      "site": "00501b64",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00501b6c",
      "incomplete_value": true,
      "site": "00501b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:e0:8"
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
      "definition_site": "00501b6c",
      "incomplete_value": true,
      "site": "00501b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:e0:8"
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
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00501b34",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "00501b44",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00501b58",
      "READ",
      [
        "storage",
        "00c13410",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00501b34",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "00501b44",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00501b58",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00501b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/00501b08.md#insn-00501b34) · [`00501b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/00501b08.md#insn-00501b44) · [`00501bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/00501b08.md#insn-00501bb0)
- 新版 `00501b34`（命令位置の公開資料なし） · `00501b44`（命令位置の公開資料なし） · `00501bb0`（命令位置の公開資料なし）

~~~diff
- 00501b34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
- 00501b34 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00501b34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
+ 00501b34 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00501b34 bytes 732647f9
+ 00501b34 bytes 734e47f9
- 00501b44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d78:8"]]
- 00501b44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00501b44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dc8:8"]]
+ 00501b44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00501b44 bytes 29bd46f9
+ 00501b44 bytes 29e546f9
- 00501bb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 00501bb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00501bb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00501bb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00501bb0 bytes 08c146f9
+ 00501bb0 bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12a5413f7757e332cb1c0a212db9929a"></a>

### [`00503408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503408.md) → [`00503408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503408.md) _ZN5Botan17X509_Cert_Options17add_ex_constraintERKNS_3OIDE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00528a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00528/00528a6c.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00528a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a6c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503448",
      "incomplete_value": true,
      "site": "0050344c",
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
      "definition_site": "00503448",
      "incomplete_value": true,
      "site": "0050344c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050343c",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "0050344c",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050343c",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "0050344c",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050343c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503408.md#insn-0050343c)
- 新版 `0050343c`（命令位置の公開資料なし）

~~~diff
- 0050343c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 0050343c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050343c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 0050343c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050343c bytes 088147f9
+ 0050343c bytes 08a947f9
~~~


<a id="compare-d0127fd2e2f57c4896a388c9d41e7d1d"></a>

### [`005034d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005034d8.md) → [`005034d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/005034d8.md) _ZN5Botan17X509_Cert_Options17add_ex_constraintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0052a96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052a/0052a96c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0052a96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a96c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503528",
      "incomplete_value": true,
      "site": "00503530",
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
      "definition_site": "00503528",
      "incomplete_value": true,
      "site": "00503530",
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
      "00503520",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "00503530",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00503520",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "00503530",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005034d8.md#insn-00503520)
- 新版 `00503520`（命令位置の公開資料なし）

~~~diff
- 00503520 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f00:8"]]
- 00503520 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00503520 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f50:8"]]
+ 00503520 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00503520 bytes 298147f9
+ 00503520 bytes 29a947f9
~~~


<a id="compare-161498c676707e6a207fe1352f6ab80f"></a>

### [`005035d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005035d4.md) → [`005035d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/005035d4.md) _ZN5Botan17X509_Cert_OptionsC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00524/00524c98.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c98.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503650",
      "incomplete_value": true,
      "site": "00503650",
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
      "definition_site": "00503650",
      "incomplete_value": true,
      "site": "00503650",
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
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503658",
      "incomplete_value": true,
      "site": "00503658",
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
      "definition_site": "00503658",
      "incomplete_value": true,
      "site": "00503658",
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
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503680",
      "incomplete_value": true,
      "site": "00503680",
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
      "definition_site": "00503680",
      "incomplete_value": true,
      "site": "00503680",
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
    "ordinal": 48,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050363c",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ],
    [
      "00503650",
      "DATA",
      [
        "storage",
        "00be9368",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00503658",
      "DATA",
      [
        "storage",
        "00be9368",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050363c",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "00503650",
      "DATA",
      [
        "storage",
        "00be93b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00503658",
      "DATA",
      [
        "storage",
        "00be93b8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050363c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005035d4.md#insn-0050363c) · [`0050366c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005035d4.md#insn-0050366c) · [`0050369c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/005035d4.md#insn-0050369c)
- 新版 `0050363c`（命令位置の公開資料なし） · `0050366c`（命令位置の公開資料なし） · `0050369c`（命令位置の公開資料なし）

~~~diff
- 0050363c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
- 0050363c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050363c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc0:8"]]
+ 0050363c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050363c bytes 08b947f9
+ 0050363c bytes 08e147f9
- 0050366c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2d0:8"]]
- 0050366c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050366c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
+ 0050366c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050366c bytes 086941f9
+ 0050366c bytes 089141f9
- 0050369c ["COPY", "tmp:0:8", ["const:866:8"]]
- 0050369c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0050369c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0050369c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0050369c ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 0050369c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0050369c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0050369c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0050369c bytes 21982191
+ 0050369c bytes 21641f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f73d82b532b8f8fa24743310ead836b3"></a>

### [`00503af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md) → [`00503af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503af8.md) _ZN5Botan4PKIX11check_chainERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEENS1_6chrono10time_pointINSC_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdd040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd040.md) · 呼出先 29件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004ee34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee34c.md) [`00504ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504ee4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)
- 新版 呼出元 1件 [`00bdd090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd090.md) · 呼出先 29件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004ee34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee34c.md) [`00504ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504ee4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.42% / 新版 99.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00504090",
      "incomplete_value": true,
      "site": "00504094",
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
                "register:4050:8"
              ],
              "INT_ADD"
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
      "definition_site": "00504090",
      "incomplete_value": true,
      "site": "00504094",
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
                "register:4050:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504d24",
      "incomplete_value": false,
      "site": "00504d2c",
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
            "const:32d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00504d24",
      "incomplete_value": false,
      "site": "00504d2c",
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
            "const:293:8"
          ]
        ]
      ]
    },
    "ordinal": 86,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504d60",
      "incomplete_value": true,
      "site": "00504d6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00504d60",
      "incomplete_value": true,
      "site": "00504d6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 88,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00503fec",
      "READ",
      [
        "storage",
        "00c254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00504194",
      "READ",
      [
        "storage",
        "00c254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00504d24",
      "PARAM",
      [
        "storage",
        "002a8293",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00503fec",
      "READ",
      [
        "storage",
        "00c254e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00504194",
      "READ",
      [
        "storage",
        "00c254e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00504d24",
      "PARAM",
      [
        "storage",
        "002a832d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md#insn-00503fec) · [`0050401c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md#insn-0050401c) · [`0050408c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md#insn-0050408c)
- 新版 `00503fec`（命令位置の公開資料なし） · `0050401c`（命令位置の公開資料なし） · `0050408c`（命令位置の公開資料なし）

~~~diff
- 00503fec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4a8:8"]]
- 00503fec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00503fec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e8:8"]]
+ 00503fec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00503fec bytes 085542f9
+ 00503fec bytes 087542f9
- 0050401c ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 0050401c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050401c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050401c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050401c ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 0050401c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050401c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050401c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050401c bytes 4aa11291
+ 0050401c bytes 4aa11391
- 0050408c ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 0050408c ["INT_CARRY", "register:105:1", ["register:4068:8", "tmp:0:8"]]
- 0050408c ["INT_SCARRY", "register:106:1", ["register:4068:8", "tmp:0:8"]]
- 0050408c ["INT_ADD", "tmp:1:8", ["register:4068:8", "tmp:0:8"]]
+ 0050408c ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 0050408c ["INT_CARRY", "register:105:1", ["register:4068:8", "tmp:0:8"]]
+ 0050408c ["INT_SCARRY", "register:106:1", ["register:4068:8", "tmp:0:8"]]
+ 0050408c ["INT_ADD", "tmp:1:8", ["register:4068:8", "tmp:0:8"]]
- 0050408c bytes ada11291
+ 0050408c bytes ada11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65e7879ffb82ede42b442d13fa28d33e"></a>

### [`00504f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504f50.md) → [`00504f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504f50.md) _ZN5Botan4PKIX10check_ocspERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_4OCSP8Respons

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdd050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd050.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004de718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de718.md) [`00504ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504ee4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)
- 新版 呼出元 1件 [`00bdd0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0a0.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004de718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de718.md) [`00504ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504ee4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.36% / 新版 99.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005053bc",
      "incomplete_value": false,
      "site": "005053c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005053bc",
      "incomplete_value": false,
      "site": "005053c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:52d:8"
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
      "definition_site": "005053f8",
      "incomplete_value": true,
      "site": "00505404",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005053f8",
      "incomplete_value": true,
      "site": "00505404",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:ef0:8"
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
      "005053bc",
      "PARAM",
      [
        "storage",
        "0029e52d",
        null,
        "string"
      ]
    ],
    [
      "005053f8",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "005053f8",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005053bc",
      "PARAM",
      [
        "storage",
        "0029e5b8",
        null,
        "string"
      ]
    ],
    [
      "005053f8",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "005053f8",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005053bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504f50.md#insn-005053bc) · [`005053f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504f50.md#insn-005053f8)
- 新版 `005053bc`（命令位置の公開資料なし） · `005053f8`（命令位置の公開資料なし）

~~~diff
- 005053bc ["COPY", "tmp:0:8", ["const:52d:8"]]
- 005053bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005053bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005053bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005053bc ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 005053bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005053bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005053bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005053bc bytes 21b41491
+ 005053bc bytes 21e01691
- 005053f8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 005053f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005053f8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 005053f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005053f8 bytes 217847f9
+ 005053f8 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d585c91ffb277bc5964e2f8499f3ce67"></a>

### [`005054cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md) → [`005054cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00505/005054cc.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdd060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd060.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051c938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c938.md)
- 新版 呼出元 1件 [`00bdd0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0b0.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051c938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c938.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.72% / 新版 99.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00505f24",
      "incomplete_value": false,
      "site": "00505f2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:894:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00505f24",
      "incomplete_value": false,
      "site": "00505f2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:921:8"
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00505f60",
      "incomplete_value": true,
      "site": "00505f6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00505f60",
      "incomplete_value": true,
      "site": "00505f6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00505f24",
      "PARAM",
      [
        "storage",
        "00294921",
        null,
        "string"
      ]
    ],
    [
      "00505f60",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00505f60",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00505f24",
      "PARAM",
      [
        "storage",
        "00294894",
        null,
        "string"
      ]
    ],
    [
      "00505f60",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "00505f60",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00505f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md#insn-00505f24) · [`00505f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md#insn-00505f60)
- 新版 `00505f24`（命令位置の公開資料なし） · `00505f60`（命令位置の公開資料なし）

~~~diff
- 00505f24 ["COPY", "tmp:0:8", ["const:921:8"]]
- 00505f24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00505f24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00505f24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00505f24 ["COPY", "tmp:0:8", ["const:894:8"]]
+ 00505f24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00505f24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00505f24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00505f24 bytes 21842491
+ 00505f24 bytes 21502291
- 00505f60 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 00505f60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00505f60 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 00505f60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00505f60 bytes 217847f9
+ 00505f60 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a3f136221651393c079299391e43830"></a>

### [`005060a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md) → [`005060a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/005060a8.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certificate_StoreE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdd070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd070.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00525e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525e44.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)
- 新版 呼出元 1件 [`00bdd0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0c0.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00525e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525e44.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.44% / 新版 96.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005062f0",
      "incomplete_value": false,
      "site": "00506310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:b57:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005062f0",
      "incomplete_value": false,
      "site": "00506310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:be4:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005062f8",
      "incomplete_value": false,
      "site": "00506310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005062f8",
      "incomplete_value": false,
      "site": "00506310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:866:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00506300",
      "incomplete_value": false,
      "site": "00506310",
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
            "const:71d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00506300",
      "incomplete_value": false,
      "site": "00506310",
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
            "const:692:8"
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
      "005062f0",
      "PARAM",
      [
        "storage",
        "00296be4",
        null,
        "string"
      ]
    ],
    [
      "005062f8",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00506300",
      "PARAM",
      [
        "storage",
        "002a5692",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005062f0",
      "PARAM",
      [
        "storage",
        "00296b57",
        null,
        "string"
      ]
    ],
    [
      "005062f8",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "00506300",
      "PARAM",
      [
        "storage",
        "002a571d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005062f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md#insn-005062f0) · [`005062f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md#insn-005062f8) · [`00506300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md#insn-00506300)
- 新版 `005062f0`（命令位置の公開資料なし） · `005062f8`（命令位置の公開資料なし） · `00506300`（命令位置の公開資料なし）

~~~diff
- 005062f0 ["COPY", "tmp:0:8", ["const:be4:8"]]
- 005062f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005062f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005062f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005062f0 ["COPY", "tmp:0:8", ["const:b57:8"]]
+ 005062f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005062f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005062f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005062f0 bytes 00902f91
+ 005062f0 bytes 005c2d91
- 005062f8 ["COPY", "tmp:0:8", ["const:866:8"]]
- 005062f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005062f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005062f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005062f8 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 005062f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005062f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005062f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005062f8 bytes 21982191
+ 005062f8 bytes 21641f91
- 00506300 ["COPY", "tmp:0:8", ["const:692:8"]]
- 00506300 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00506300 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00506300 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00506300 ["COPY", "tmp:0:8", ["const:71d:8"]]
+ 00506300 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00506300 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00506300 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00506300 bytes 42481a91
+ 00506300 bytes 42741c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b45268f88a93c8f4fcd91447107164a7"></a>

### [`0050645c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/0050645c.md) → [`0050645c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/0050645c.md) _ZN5Botan4PKIX22build_certificate_pathERNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certi

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 20件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`004df920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004df920.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`0051d9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d9f8.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`004df920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df920.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`0051d9f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d9f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.43% / 新版 99.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005066c4",
      "incomplete_value": true,
      "site": "005066c4",
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
      "definition_site": "005066c4",
      "incomplete_value": true,
      "site": "005066c4",
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
      "005066b8",
      "READ",
      [
        "storage",
        "00c1b2b8",
        null,
        "pointer"
      ]
    ],
    [
      "005066c4",
      "DATA",
      [
        "storage",
        "00bea788",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "005066b8",
      "READ",
      [
        "storage",
        "00c1b308",
        null,
        "pointer"
      ]
    ],
    [
      "005066c4",
      "DATA",
      [
        "storage",
        "00bea7d8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005066b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/0050645c.md#insn-005066b8)
- 新版 `005066b8`（命令位置の公開資料なし）

~~~diff
- 005066b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b8:8"]]
- 005066b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005066b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:308:8"]]
+ 005066b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005066b8 bytes 085d41f9
+ 005066b8 bytes 088541f9
~~~


<a id="compare-a1fdeca61e93193b21fe396e75b1e5cb"></a>

### [`00508250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508250.md) → [`00508250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508250.md) _ZN5Botan4PKIX23merge_revocation_statusERNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd080.md) · 呼出先 8件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdd0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0d0.md) · 呼出先 8件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.29% / 新版 99.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00508660",
      "incomplete_value": false,
      "site": "00508668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:8b4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00508660",
      "incomplete_value": false,
      "site": "00508668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:941:8"
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
      "definition_site": "0050869c",
      "incomplete_value": true,
      "site": "005086a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050869c",
      "incomplete_value": true,
      "site": "005086a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:ef0:8"
              ]
            ]
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
      "00508660",
      "PARAM",
      [
        "storage",
        "00294941",
        null,
        "string"
      ]
    ],
    [
      "0050869c",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "0050869c",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00508660",
      "PARAM",
      [
        "storage",
        "002948b4",
        null,
        "string"
      ]
    ],
    [
      "0050869c",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "0050869c",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00508660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508250.md#insn-00508660) · [`0050869c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508250.md#insn-0050869c)
- 新版 `00508660`（命令位置の公開資料なし） · `0050869c`（命令位置の公開資料なし）

~~~diff
- 00508660 ["COPY", "tmp:0:8", ["const:941:8"]]
- 00508660 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00508660 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00508660 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00508660 ["COPY", "tmp:0:8", ["const:8b4:8"]]
+ 00508660 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00508660 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00508660 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00508660 bytes 21042591
+ 00508660 bytes 21d02291
- 0050869c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 0050869c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050869c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 0050869c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0050869c bytes 217847f9
+ 0050869c bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a80423fccc6e83c2a41e09c5724ce93"></a>

### [`005086fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/005086fc.md) → [`005086fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/005086fc.md) _ZN5Botan4PKIX14overall_statusERKNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd090.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdd0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0e0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005087c4",
      "incomplete_value": false,
      "site": "005087cc",
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
            "const:58c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005087c4",
      "incomplete_value": false,
      "site": "005087cc",
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
            "const:501:8"
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
      "definition_site": "00508800",
      "incomplete_value": true,
      "site": "0050880c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00508800",
      "incomplete_value": true,
      "site": "0050880c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:ef0:8"
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
      "005087c4",
      "PARAM",
      [
        "storage",
        "002a2501",
        null,
        "string"
      ]
    ],
    [
      "00508800",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00508800",
      "PARAM",
      [
        "storage",
        "00be9298",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005087c4",
      "PARAM",
      [
        "storage",
        "002a258c",
        null,
        "string"
      ]
    ],
    [
      "00508800",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "00508800",
      "PARAM",
      [
        "storage",
        "00be92e8",
        "_ZTIN5Botan16Invalid_ArgumentE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005087c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/005086fc.md#insn-005087c4) · [`00508800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/005086fc.md#insn-00508800)
- 新版 `005087c4`（命令位置の公開資料なし） · `00508800`（命令位置の公開資料なし）

~~~diff
- 005087c4 ["COPY", "tmp:0:8", ["const:501:8"]]
- 005087c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005087c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005087c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005087c4 ["COPY", "tmp:0:8", ["const:58c:8"]]
+ 005087c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005087c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005087c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005087c4 bytes 21041491
+ 005087c4 bytes 21301691
- 00508800 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 00508800 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00508800 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 00508800 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00508800 bytes 217847f9
+ 00508800 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c1f5abf1005610d810d8a2713f3178e"></a>

### [`00508860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508860.md) → [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) _ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS1_IPNS

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdd0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd0a0.md) · 呼出先 28件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00506ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/00506ee0.md) [`0050936c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00509/0050936c.md) [`0050947c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00509/0050947c.md)
- 新版 呼出元 1件 [`00bdd0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd0f0.md) · 呼出先 28件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00506ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) [`0050936c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050936c.md) [`0050947c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050947c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005088d8",
      "incomplete_value": true,
      "site": "005088dc",
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
      "definition_site": "005088d8",
      "incomplete_value": true,
      "site": "005088dc",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005088fc",
      "incomplete_value": true,
      "site": "00508900",
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
      "definition_site": "005088fc",
      "incomplete_value": true,
      "site": "00508900",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005091c4",
      "incomplete_value": false,
      "site": "005091cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:5d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005091c4",
      "incomplete_value": false,
      "site": "005091cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:54e:8"
          ]
        ]
      ]
    },
    "ordinal": 65,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005088d0",
      "READ",
      [
        "storage",
        "00c1b298",
        null,
        "pointer"
      ]
    ],
    [
      "005088dc",
      "DATA",
      [
        "storage",
        "00bed730",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005088f8",
      "READ",
      [
        "storage",
        "00c1b2a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005088d0",
      "READ",
      [
        "storage",
        "00c1b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "005088dc",
      "DATA",
      [
        "storage",
        "00bed780",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005088f8",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005088d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508860.md#insn-005088d0) · [`005088f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508860.md#insn-005088f8) · [`005091c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508860.md#insn-005091c4)
- 新版 `005088d0`（命令位置の公開資料なし） · `005088f8`（命令位置の公開資料なし） · `005091c4`（命令位置の公開資料なし）

~~~diff
- 005088d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:298:8"]]
- 005088d0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005088d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2e8:8"]]
+ 005088d0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 005088d0 bytes 944e41f9
+ 005088d0 bytes 947641f9
- 005088f8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:2a0:8"]]
- 005088f8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005088f8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:2f0:8"]]
+ 005088f8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 005088f8 bytes d65241f9
+ 005088f8 bytes d67a41f9
- 005091c4 ["COPY", "tmp:0:8", ["const:54e:8"]]
- 005091c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005091c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005091c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005091c4 ["COPY", "tmp:0:8", ["const:5d9:8"]]
+ 005091c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005091c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005091c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005091c4 bytes 21381591
+ 005091c4 bytes 21641791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd54cd98126e613c765228f22dffdecd"></a>

### [`0050a23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a23c.md) → [`0050a23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a23c.md) _ZNK5Botan22Path_Validation_Result10trust_rootEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050a2e8",
      "incomplete_value": true,
      "site": "0050a2f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050a2e8",
      "incomplete_value": true,
      "site": "0050a2f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f48:8"
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
      "definition_site": "0050a34c",
      "incomplete_value": true,
      "site": "0050a358",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050a34c",
      "incomplete_value": true,
      "site": "0050a358",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f48:8"
              ]
            ]
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
      "0050a2e8",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0050a2e8",
      "PARAM",
      [
        "storage",
        "00be9238",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0050a34c",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050a2e8",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ],
    [
      "0050a2e8",
      "PARAM",
      [
        "storage",
        "00be9288",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0050a34c",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050a2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a23c.md#insn-0050a2e8) · [`0050a34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a23c.md#insn-0050a34c)
- 新版 `0050a2e8`（命令位置の公開資料なし） · `0050a34c`（命令位置の公開資料なし）

~~~diff
- 0050a2e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
- 0050a2e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050a2e8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f98:8"]]
+ 0050a2e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0050a2e8 bytes 21a447f9
+ 0050a2e8 bytes 21cc47f9
- 0050a34c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
- 0050a34c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050a34c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f98:8"]]
+ 0050a34c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0050a34c bytes 21a447f9
+ 0050a34c bytes 21cc47f9
~~~


<a id="compare-77eebfdb30cf6293648121db6c221fea"></a>

### [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) → [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) _ZN5Botan4X50923create_self_signed_certERKNS_17X509_Cert_OptionsERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9al

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 27件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0049dba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dba0.md) [`004de034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de034.md) [`004e23fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e23fc.md) [`004ed188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ed188.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0049dba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dba0.md) [`004de034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de034.md) [`004e23fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e23fc.md) [`004ed188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed188.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.23% / 新版 95.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050a68c",
      "incomplete_value": true,
      "site": "0050a68c",
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
      "definition_site": "0050a68c",
      "incomplete_value": true,
      "site": "0050a68c",
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
      "definition_site": "0050a6d8",
      "incomplete_value": true,
      "site": "0050a6d8",
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
      "definition_site": "0050a6d8",
      "incomplete_value": true,
      "site": "0050a6d8",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050a840",
      "incomplete_value": true,
      "site": "0050a848",
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
      "definition_site": "0050a840",
      "incomplete_value": true,
      "site": "0050a848",
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
    "ordinal": 33,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050a674",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "0050a68c",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050a6c4",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050a674",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0050a68c",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050a6c4",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050a674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md#insn-0050a674) · [`0050a6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md#insn-0050a6c4) · [`0050a730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md#insn-0050a730)
- 新版 `0050a674`（命令位置の公開資料なし） · `0050a6c4`（命令位置の公開資料なし） · `0050a730`（命令位置の公開資料なし）

~~~diff
- 0050a674 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
- 0050a674 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050a674 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f48:8"]]
+ 0050a674 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050a674 bytes 297d47f9
+ 0050a674 bytes 29a547f9
- 0050a6c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 0050a6c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050a6c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
+ 0050a6c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050a6c4 bytes 084941f9
+ 0050a6c4 bytes 087141f9
- 0050a730 ["COPY", "tmp:0:8", ["const:607:8"]]
- 0050a730 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0050a730 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0050a730 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0050a730 ["COPY", "tmp:0:8", ["const:692:8"]]
+ 0050a730 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0050a730 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0050a730 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0050a730 bytes 211c1891
+ 0050a730 bytes 21481a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-955276bb2600c506c6d894ddc08a5b3f"></a>

### [`0050af44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050af44.md) → [`0050af44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050af44.md) FUN_0050af44

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) · 呼出先 10件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`004dc4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004dc/004dc4a4.md) [`005180b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005180b8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 10件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`004dc4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc4a4.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.24% / 新版 93.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050af8c",
      "incomplete_value": true,
      "site": "0050af8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:96d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050af8c",
      "incomplete_value": true,
      "site": "0050af8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:9fa:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050af84",
      "incomplete_value": true,
      "site": "0050af90",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050af84",
      "incomplete_value": true,
      "site": "0050af90",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050b054",
      "incomplete_value": true,
      "site": "0050b054",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:97d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050b054",
      "incomplete_value": true,
      "site": "0050b054",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:a0a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050af6c",
      "READ",
      [
        "storage",
        "002969fa",
        null,
        "string"
      ]
    ],
    [
      "0050af84",
      "READ",
      [
        "storage",
        "00296a01",
        null,
        "string"
      ]
    ],
    [
      "0050b044",
      "READ",
      [
        "storage",
        "00296a0a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050af6c",
      "READ",
      [
        "storage",
        "0029696d",
        null,
        "string"
      ]
    ],
    [
      "0050af84",
      "READ",
      [
        "storage",
        "00296974",
        null,
        "string"
      ]
    ],
    [
      "0050b044",
      "READ",
      [
        "storage",
        "0029697d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050af64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050af44.md#insn-0050af64) · [`0050b03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050af44.md#insn-0050b03c) · [`0050b09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050af44.md#insn-0050b09c)
- 新版 `0050af64`（命令位置の公開資料なし） · `0050b03c`（命令位置の公開資料なし） · `0050b09c`（命令位置の公開資料なし）

~~~diff
- 0050af64 ["COPY", "tmp:0:8", ["const:9fa:8"]]
- 0050af64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050af64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050af64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050af64 ["COPY", "tmp:0:8", ["const:96d:8"]]
+ 0050af64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050af64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050af64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050af64 bytes 29e92791
+ 0050af64 bytes 29b52591
- 0050b03c ["COPY", "tmp:0:8", ["const:a0a:8"]]
- 0050b03c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050b03c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050b03c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050b03c ["COPY", "tmp:0:8", ["const:97d:8"]]
+ 0050b03c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050b03c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050b03c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050b03c bytes 29292891
+ 0050b03c bytes 29f52591
- 0050b09c ["COPY", "tmp:0:8", ["const:46d:8"]]
- 0050b09c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050b09c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050b09c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050b09c ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 0050b09c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050b09c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050b09c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050b09c bytes 29b51191
+ 0050b09c bytes 29e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d51f93655979a361dab6ae4bd16499c"></a>

### [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) → [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) _ZN5Botan4X50915create_cert_reqERKNS_17X509_Cert_OptionsERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorI

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 42件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`0049dba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dba0.md) [`004de034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004de/004de034.md) [`004e23fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e23fc.md)
- 新版 呼出元 0件  · 呼出先 42件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`0049dba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dba0.md) [`004de034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de034.md) [`004e23fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e23fc.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.95% / 新版 94.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 5件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050b4b0",
      "incomplete_value": true,
      "site": "0050b4b0",
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
      "definition_site": "0050b4b0",
      "incomplete_value": true,
      "site": "0050b4b0",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050b4fc",
      "incomplete_value": true,
      "site": "0050b4fc",
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
      "definition_site": "0050b4fc",
      "incomplete_value": true,
      "site": "0050b4fc",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050b660",
      "incomplete_value": true,
      "site": "0050b668",
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
      "definition_site": "0050b660",
      "incomplete_value": true,
      "site": "0050b668",
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
    "ordinal": 33,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050b498",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "0050b4b0",
      "DATA",
      [
        "storage",
        "00be9198",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050b4e8",
      "READ",
      [
        "storage",
        "00c1b290",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050b498",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0050b4b0",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050b4e8",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050b498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md#insn-0050b498) · [`0050b4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md#insn-0050b4e8) · [`0050b554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md#insn-0050b554)
- 新版 `0050b498`（命令位置の公開資料なし） · `0050b4e8`（命令位置の公開資料なし） · `0050b554`（命令位置の公開資料なし）

~~~diff
- 0050b498 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef8:8"]]
- 0050b498 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050b498 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f48:8"]]
+ 0050b498 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050b498 bytes 297d47f9
+ 0050b498 bytes 29a547f9
- 0050b4e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 0050b4e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050b4e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
+ 0050b4e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050b4e8 bytes 084941f9
+ 0050b4e8 bytes 087141f9
- 0050b554 ["COPY", "tmp:0:8", ["const:607:8"]]
- 0050b554 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0050b554 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0050b554 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0050b554 ["COPY", "tmp:0:8", ["const:692:8"]]
+ 0050b554 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0050b554 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0050b554 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0050b554 bytes 211c1891
+ 0050b554 bytes 21481a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef1e1fbd49787dca269a90e97b991242"></a>

### [`0050c0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c0e8.md) → [`0050c0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c0e8.md) FUN_0050c0e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c1dc.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`0050c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c1dc.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050c120",
      "incomplete_value": true,
      "site": "0050c120",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050c120",
      "incomplete_value": true,
      "site": "0050c120",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050c14c",
      "incomplete_value": true,
      "site": "0050c14c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050c14c",
      "incomplete_value": true,
      "site": "0050c14c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050c178",
      "incomplete_value": true,
      "site": "0050c178",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050c178",
      "incomplete_value": true,
      "site": "0050c178",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050c110",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050c13c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050c168",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050c110",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050c13c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050c168",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c0e8.md#insn-0050c110) · [`0050c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c0e8.md#insn-0050c13c) · [`0050c168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c0e8.md#insn-0050c168)
- 新版 `0050c110`（命令位置の公開資料なし） · `0050c13c`（命令位置の公開資料なし） · `0050c168`（命令位置の公開資料なし）

~~~diff
- 0050c110 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050c110 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c110 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050c110 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c110 bytes a99643f9
+ 0050c110 bytes a9be43f9
- 0050c13c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050c13c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c13c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050c13c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c13c bytes a99643f9
+ 0050c13c bytes a9be43f9
- 0050c168 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050c168 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c168 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050c168 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c168 bytes a99643f9
+ 0050c168 bytes a9be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fdc66451250c31d12e803e893d6ea7d"></a>

### [`0050c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c390.md) → [`0050c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c390.md) FUN_0050c390

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0050c3ac",
      "incomplete_value": true,
      "site": "0050c3b0",
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
      "definition_site": "0050c3ac",
      "incomplete_value": true,
      "site": "0050c3b0",
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
      "0050c3a8",
      "READ",
      [
        "storage",
        "00c1afd0",
        null,
        "pointer"
      ]
    ],
    [
      "0050c3b0",
      "DATA",
      [
        "storage",
        "00beaac0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0050c3a8",
      "READ",
      [
        "storage",
        "00c1b020",
        null,
        "pointer"
      ]
    ],
    [
      "0050c3b0",
      "DATA",
      [
        "storage",
        "00beab10",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c390.md#insn-0050c3a0) · [`0050c3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c390.md#insn-0050c3a8)
- 新版 `0050c3a0`（命令位置の公開資料なし） · `0050c3a8`（命令位置の公開資料なし）

~~~diff
- 0050c3a0 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050c3a0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050c3a0 bytes 683800d0
+ 0050c3a0 bytes 683800f0
- 0050c3a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd0:8"]]
- 0050c3a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c3a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
+ 0050c3a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c3a8 bytes 08e947f9
+ 0050c3a8 bytes 081140f9
~~~


<a id="compare-7f8cbea87abf756c02ba632097ad57eb"></a>

### [`0050c3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c3d4.md) → [`0050c3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c3d4.md) FUN_0050c3d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050c4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c4c8.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`0050c4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c4c8.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050c40c",
      "incomplete_value": true,
      "site": "0050c40c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050c40c",
      "incomplete_value": true,
      "site": "0050c40c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050c438",
      "incomplete_value": true,
      "site": "0050c438",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050c438",
      "incomplete_value": true,
      "site": "0050c438",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050c464",
      "incomplete_value": true,
      "site": "0050c464",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050c464",
      "incomplete_value": true,
      "site": "0050c464",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050c3fc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050c428",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050c454",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050c3fc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050c428",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050c454",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c3d4.md#insn-0050c3fc) · [`0050c428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c3d4.md#insn-0050c428) · [`0050c454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c3d4.md#insn-0050c454)
- 新版 `0050c3fc`（命令位置の公開資料なし） · `0050c428`（命令位置の公開資料なし） · `0050c454`（命令位置の公開資料なし）

~~~diff
- 0050c3fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050c3fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c3fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050c3fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c3fc bytes a99643f9
+ 0050c3fc bytes a9be43f9
- 0050c428 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050c428 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c428 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050c428 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c428 bytes a99643f9
+ 0050c428 bytes a9be43f9
- 0050c454 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050c454 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c454 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050c454 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c454 bytes a99643f9
+ 0050c454 bytes a9be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-175d72deba463db491efd8cf988f62aa"></a>

### [`0050c67c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c67c.md) → [`0050c67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c67c.md) FUN_0050c67c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0050c698",
      "incomplete_value": true,
      "site": "0050c69c",
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
      "definition_site": "0050c698",
      "incomplete_value": true,
      "site": "0050c69c",
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
      "0050c694",
      "READ",
      [
        "storage",
        "00c1afd8",
        null,
        "pointer"
      ]
    ],
    [
      "0050c69c",
      "DATA",
      [
        "storage",
        "00beab98",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0050c694",
      "READ",
      [
        "storage",
        "00c1b028",
        null,
        "pointer"
      ]
    ],
    [
      "0050c69c",
      "DATA",
      [
        "storage",
        "00beabe8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c67c.md#insn-0050c68c) · [`0050c694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c67c.md#insn-0050c694)
- 新版 `0050c68c`（命令位置の公開資料なし） · `0050c694`（命令位置の公開資料なし）

~~~diff
- 0050c68c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050c68c ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050c68c bytes 683800d0
+ 0050c68c bytes 683800f0
- 0050c694 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd8:8"]]
- 0050c694 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c694 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:28:8"]]
+ 0050c694 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c694 bytes 08ed47f9
+ 0050c694 bytes 081540f9
~~~


<a id="compare-d29e83b838c449d2ac9cfd05e8405e02"></a>

### [`0050c6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c6c0.md) → [`0050c6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c6c0.md) FUN_0050c6c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050c7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c7b4.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`0050c7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c7b4.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050c6f8",
      "incomplete_value": true,
      "site": "0050c6f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050c6f8",
      "incomplete_value": true,
      "site": "0050c6f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050c724",
      "incomplete_value": true,
      "site": "0050c724",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050c724",
      "incomplete_value": true,
      "site": "0050c724",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050c750",
      "incomplete_value": true,
      "site": "0050c750",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050c750",
      "incomplete_value": true,
      "site": "0050c750",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050c6e8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050c714",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050c740",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050c6e8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050c714",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050c740",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c6c0.md#insn-0050c6e8) · [`0050c714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c6c0.md#insn-0050c714) · [`0050c740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c6c0.md#insn-0050c740)
- 新版 `0050c6e8`（命令位置の公開資料なし） · `0050c714`（命令位置の公開資料なし） · `0050c740`（命令位置の公開資料なし）

~~~diff
- 0050c6e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050c6e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c6e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050c6e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c6e8 bytes a99643f9
+ 0050c6e8 bytes a9be43f9
- 0050c714 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050c714 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c714 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050c714 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c714 bytes a99643f9
+ 0050c714 bytes a9be43f9
- 0050c740 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050c740 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c740 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050c740 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c740 bytes a99643f9
+ 0050c740 bytes a9be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d561632e4862c26f6d987def2e4ad6bd"></a>

### [`0050c968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c968.md) → [`0050c968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c968.md) FUN_0050c968

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0050c984",
      "incomplete_value": true,
      "site": "0050c988",
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
      "definition_site": "0050c984",
      "incomplete_value": true,
      "site": "0050c988",
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
      "0050c980",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "0050c988",
      "DATA",
      [
        "storage",
        "00beac48",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0050c980",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "0050c988",
      "DATA",
      [
        "storage",
        "00beac98",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c968.md#insn-0050c978) · [`0050c980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c968.md#insn-0050c980)
- 新版 `0050c978`（命令位置の公開資料なし） · `0050c980`（命令位置の公開資料なし）

~~~diff
- 0050c978 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050c978 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050c978 bytes 683800d0
+ 0050c978 bytes 683800f0
- 0050c980 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 0050c980 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c980 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
+ 0050c980 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c980 bytes 08f147f9
+ 0050c980 bytes 081940f9
~~~


<a id="compare-314134f69845590a168bf4b6ea4b0383"></a>

### [`0050c9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c9c4.md) → [`0050c9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050c9c4.md) FUN_0050c9c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050c9f8",
      "incomplete_value": true,
      "site": "0050c9f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      "definition_site": "0050c9f8",
      "incomplete_value": true,
      "site": "0050c9f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050c9e8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050c9e8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050c9c4.md#insn-0050c9e8)
- 新版 `0050c9e8`（命令位置の公開資料なし）

~~~diff
- 0050c9e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0050c9e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c9e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0050c9e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c9e8 bytes 299543f9
+ 0050c9e8 bytes 29bd43f9
~~~


<a id="compare-bcb39e15a459c8c095a52a09d3240695"></a>

### [`0050ca48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050ca48.md) → [`0050ca48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050ca48.md) FUN_0050ca48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050ca64",
      "incomplete_value": true,
      "site": "0050ca68",
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
      "definition_site": "0050ca64",
      "incomplete_value": true,
      "site": "0050ca68",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050ca8c",
      "incomplete_value": true,
      "site": "0050ca8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      "definition_site": "0050ca8c",
      "incomplete_value": true,
      "site": "0050ca8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050ca5c",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "0050ca68",
      "DATA",
      [
        "storage",
        "00be9410",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050ca7c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050ca5c",
      "READ",
      [
        "storage",
        "00c1b040",
        null,
        "pointer"
      ]
    ],
    [
      "0050ca68",
      "DATA",
      [
        "storage",
        "00be9460",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050ca7c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ca54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050ca48.md#insn-0050ca54) · [`0050ca5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050ca48.md#insn-0050ca5c) · [`0050ca7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050ca48.md#insn-0050ca7c)
- 新版 `0050ca54`（命令位置の公開資料なし） · `0050ca5c`（命令位置の公開資料なし） · `0050ca7c`（命令位置の公開資料なし）

~~~diff
- 0050ca54 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050ca54 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050ca54 bytes 683800d0
+ 0050ca54 bytes 683800f0
- 0050ca5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
- 0050ca5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ca5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:40:8"]]
+ 0050ca5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ca5c bytes 08f947f9
+ 0050ca5c bytes 082140f9
- 0050ca7c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0050ca7c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ca7c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0050ca7c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ca7c bytes 299543f9
+ 0050ca7c bytes 29bd43f9
~~~


<a id="compare-c923012cf3ab7388318dddaf54835043"></a>

### [`0050cadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cadc.md) → [`0050cadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cadc.md) FUN_0050cadc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050caf8",
      "incomplete_value": true,
      "site": "0050cafc",
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
      "definition_site": "0050caf8",
      "incomplete_value": true,
      "site": "0050cafc",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050cb20",
      "incomplete_value": true,
      "site": "0050cb20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      "definition_site": "0050cb20",
      "incomplete_value": true,
      "site": "0050cb20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050caf0",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "0050cafc",
      "DATA",
      [
        "storage",
        "00be9410",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cb10",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050caf0",
      "READ",
      [
        "storage",
        "00c1b040",
        null,
        "pointer"
      ]
    ],
    [
      "0050cafc",
      "DATA",
      [
        "storage",
        "00be9460",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cb10",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cadc.md#insn-0050cae8) · [`0050caf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cadc.md#insn-0050caf0) · [`0050cb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cadc.md#insn-0050cb10)
- 新版 `0050cae8`（命令位置の公開資料なし） · `0050caf0`（命令位置の公開資料なし） · `0050cb10`（命令位置の公開資料なし）

~~~diff
- 0050cae8 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050cae8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050cae8 bytes 683800d0
+ 0050cae8 bytes 683800f0
- 0050caf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
- 0050caf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050caf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:40:8"]]
+ 0050caf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050caf0 bytes 08f947f9
+ 0050caf0 bytes 082140f9
- 0050cb10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0050cb10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cb10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0050cb10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cb10 bytes 299543f9
+ 0050cb10 bytes 29bd43f9
~~~


<a id="compare-b8b92734bf49f46b76deab03e5e7579b"></a>

### [`0050cb74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cb74.md) → [`0050cb74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cb74.md) FUN_0050cb74

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050cb90",
      "incomplete_value": true,
      "site": "0050cb94",
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
      "definition_site": "0050cb90",
      "incomplete_value": true,
      "site": "0050cb94",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050cbb8",
      "incomplete_value": true,
      "site": "0050cbb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
      "definition_site": "0050cbb8",
      "incomplete_value": true,
      "site": "0050cbb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050cb88",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "0050cb94",
      "DATA",
      [
        "storage",
        "00be9410",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cba8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050cb88",
      "READ",
      [
        "storage",
        "00c1b040",
        null,
        "pointer"
      ]
    ],
    [
      "0050cb94",
      "DATA",
      [
        "storage",
        "00be9460",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cba8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cb74.md#insn-0050cb80) · [`0050cb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cb74.md#insn-0050cb88) · [`0050cba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cb74.md#insn-0050cba8)
- 新版 `0050cb80`（命令位置の公開資料なし） · `0050cb88`（命令位置の公開資料なし） · `0050cba8`（命令位置の公開資料なし）

~~~diff
- 0050cb80 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050cb80 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050cb80 bytes 683800d0
+ 0050cb80 bytes 683800f0
- 0050cb88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
- 0050cb88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cb88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:40:8"]]
+ 0050cb88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cb88 bytes 08f947f9
+ 0050cb88 bytes 082140f9
- 0050cba8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0050cba8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cba8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0050cba8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cba8 bytes 299543f9
+ 0050cba8 bytes 29bd43f9
~~~


<a id="compare-f5bd4b4a8cac8e2d5b32d16fb425c6bc"></a>

### [`0050cc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cc08.md) → [`0050cc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cc08.md) FUN_0050cc08

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050cc2c",
      "incomplete_value": true,
      "site": "0050cc30",
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
      "definition_site": "0050cc2c",
      "incomplete_value": true,
      "site": "0050cc30",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050cc68",
      "incomplete_value": true,
      "site": "0050cc6c",
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
      "definition_site": "0050cc68",
      "incomplete_value": true,
      "site": "0050cc6c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050cc50",
      "incomplete_value": true,
      "site": "0050cc50",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050cc50",
      "incomplete_value": true,
      "site": "0050cc50",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
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
      "0050cc24",
      "READ",
      [
        "storage",
        "00c1b158",
        null,
        "pointer"
      ]
    ],
    [
      "0050cc30",
      "DATA",
      [
        "storage",
        "00beaf10",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cc40",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050cc24",
      "READ",
      [
        "storage",
        "00c1b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "0050cc30",
      "DATA",
      [
        "storage",
        "00beaf60",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cc40",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cc08.md#insn-0050cc24) · [`0050cc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cc08.md#insn-0050cc40) · [`0050cc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cc08.md#insn-0050cc5c)
- 新版 `0050cc24`（命令位置の公開資料なし） · `0050cc40`（命令位置の公開資料なし） · `0050cc5c`（命令位置の公開資料なし）

~~~diff
- 0050cc24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 0050cc24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cc24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a8:8"]]
+ 0050cc24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cc24 bytes 08ad40f9
+ 0050cc24 bytes 08d540f9
- 0050cc40 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050cc40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cc40 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050cc40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cc40 bytes a99643f9
+ 0050cc40 bytes a9be43f9
- 0050cc5c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050cc5c ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050cc5c bytes 683800d0
+ 0050cc5c bytes 683800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baf1c372c6f342a8c1b913aaae8238e1"></a>

### [`0050cce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cce4.md) → [`0050cce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cce4.md) FUN_0050cce4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.27% / 新版 87.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050cd08",
      "incomplete_value": true,
      "site": "0050cd0c",
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
      "definition_site": "0050cd08",
      "incomplete_value": true,
      "site": "0050cd0c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050cd44",
      "incomplete_value": true,
      "site": "0050cd48",
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
      "definition_site": "0050cd44",
      "incomplete_value": true,
      "site": "0050cd48",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050cd2c",
      "incomplete_value": true,
      "site": "0050cd2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050cd2c",
      "incomplete_value": true,
      "site": "0050cd2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
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
      "0050cd00",
      "READ",
      [
        "storage",
        "00c1b158",
        null,
        "pointer"
      ]
    ],
    [
      "0050cd0c",
      "DATA",
      [
        "storage",
        "00beaf10",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cd1c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050cd00",
      "READ",
      [
        "storage",
        "00c1b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "0050cd0c",
      "DATA",
      [
        "storage",
        "00beaf60",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050cd1c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cce4.md#insn-0050cd00) · [`0050cd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cce4.md#insn-0050cd1c) · [`0050cd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cce4.md#insn-0050cd38)
- 新版 `0050cd00`（命令位置の公開資料なし） · `0050cd1c`（命令位置の公開資料なし） · `0050cd38`（命令位置の公開資料なし）

~~~diff
- 0050cd00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 0050cd00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cd00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a8:8"]]
+ 0050cd00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cd00 bytes 08ad40f9
+ 0050cd00 bytes 08d540f9
- 0050cd1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050cd1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cd1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050cd1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cd1c bytes a99643f9
+ 0050cd1c bytes a9be43f9
- 0050cd38 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050cd38 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050cd38 bytes 683800d0
+ 0050cd38 bytes 683800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b116103504c33cb32c1644cc71151447"></a>

### [`0050cdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cdc8.md) → [`0050cdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cdc8.md) FUN_0050cdc8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050cdec",
      "incomplete_value": true,
      "site": "0050cdf0",
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
      "definition_site": "0050cdec",
      "incomplete_value": true,
      "site": "0050cdf0",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050ce28",
      "incomplete_value": true,
      "site": "0050ce2c",
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
      "definition_site": "0050ce28",
      "incomplete_value": true,
      "site": "0050ce2c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050ce10",
      "incomplete_value": true,
      "site": "0050ce10",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ce10",
      "incomplete_value": true,
      "site": "0050ce10",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
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
      "0050cde4",
      "READ",
      [
        "storage",
        "00c1b158",
        null,
        "pointer"
      ]
    ],
    [
      "0050cdf0",
      "DATA",
      [
        "storage",
        "00beaf10",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050ce00",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050cde4",
      "READ",
      [
        "storage",
        "00c1b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "0050cdf0",
      "DATA",
      [
        "storage",
        "00beaf60",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0050ce00",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cdc8.md#insn-0050cde4) · [`0050ce00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cdc8.md#insn-0050ce00) · [`0050ce1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cdc8.md#insn-0050ce1c)
- 新版 `0050cde4`（命令位置の公開資料なし） · `0050ce00`（命令位置の公開資料なし） · `0050ce1c`（命令位置の公開資料なし）

~~~diff
- 0050cde4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 0050cde4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cde4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a8:8"]]
+ 0050cde4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cde4 bytes 08ad40f9
+ 0050cde4 bytes 08d540f9
- 0050ce00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050ce00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ce00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050ce00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ce00 bytes a99643f9
+ 0050ce00 bytes a9be43f9
- 0050ce1c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050ce1c ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 0050ce1c bytes 683800d0
+ 0050ce1c bytes 683800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2250c37b3fccc2d235ffe4a3b46c8993"></a>

### [`0050cf9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cf9c.md) → [`0050cf9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cf9c.md) FUN_0050cf9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050cfbc",
      "incomplete_value": true,
      "site": "0050cfc0",
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
      "definition_site": "0050cfbc",
      "incomplete_value": true,
      "site": "0050cfc0",
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
      "0050cfb0",
      "READ",
      [
        "storage",
        "00c1b008",
        null,
        "pointer"
      ]
    ],
    [
      "0050cfc0",
      "DATA",
      [
        "storage",
        "00be94c8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "0050cfb0",
      "READ",
      [
        "storage",
        "00c1b058",
        null,
        "pointer"
      ]
    ],
    [
      "0050cfc0",
      "DATA",
      [
        "storage",
        "00be9518",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cf9c.md#insn-0050cfb0)
- 新版 `0050cfb0`（命令位置の公開資料なし）

~~~diff
- 0050cfb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
- 0050cfb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050cfb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:58:8"]]
+ 0050cfb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050cfb0 bytes 080540f9
+ 0050cfb0 bytes 082d40f9
~~~


<a id="compare-ba7e3abe2579a3528fa73f1bb91d558b"></a>

### [`0050cffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cffc.md) → [`0050cffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050c/0050cffc.md) FUN_0050cffc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d01c",
      "incomplete_value": true,
      "site": "0050d020",
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
      "definition_site": "0050d01c",
      "incomplete_value": true,
      "site": "0050d020",
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
      "0050d010",
      "READ",
      [
        "storage",
        "00c1b008",
        null,
        "pointer"
      ]
    ],
    [
      "0050d020",
      "DATA",
      [
        "storage",
        "00be94c8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "0050d010",
      "READ",
      [
        "storage",
        "00c1b058",
        null,
        "pointer"
      ]
    ],
    [
      "0050d020",
      "DATA",
      [
        "storage",
        "00be9518",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050c/0050cffc.md#insn-0050d010)
- 新版 `0050d010`（命令位置の公開資料なし）

~~~diff
- 0050d010 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
- 0050d010 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d010 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:58:8"]]
+ 0050d010 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d010 bytes 080540f9
+ 0050d010 bytes 082d40f9
~~~


<a id="compare-77bd18776f8dfc970d4b93d052e82a50"></a>

### [`0050d060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d060.md) → [`0050d060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d060.md) FUN_0050d060

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d080",
      "incomplete_value": true,
      "site": "0050d084",
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
      "definition_site": "0050d080",
      "incomplete_value": true,
      "site": "0050d084",
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
      "0050d074",
      "READ",
      [
        "storage",
        "00c1b008",
        null,
        "pointer"
      ]
    ],
    [
      "0050d084",
      "DATA",
      [
        "storage",
        "00be94c8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "0050d074",
      "READ",
      [
        "storage",
        "00c1b058",
        null,
        "pointer"
      ]
    ],
    [
      "0050d084",
      "DATA",
      [
        "storage",
        "00be9518",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d060.md#insn-0050d074)
- 新版 `0050d074`（命令位置の公開資料なし）

~~~diff
- 0050d074 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
- 0050d074 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d074 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:58:8"]]
+ 0050d074 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d074 bytes 080540f9
+ 0050d074 bytes 082d40f9
~~~


<a id="compare-d8b592e50c85b2063a1f7062e40f757f"></a>

### [`0050d410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d410.md) → [`0050d410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d410.md) FUN_0050d410

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050d4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d4e4.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`0050d4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d4e4.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d48c",
      "incomplete_value": true,
      "site": "0050d490",
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
      "definition_site": "0050d48c",
      "incomplete_value": true,
      "site": "0050d490",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d448",
      "incomplete_value": true,
      "site": "0050d448",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d448",
      "incomplete_value": true,
      "site": "0050d448",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d474",
      "incomplete_value": true,
      "site": "0050d474",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d474",
      "incomplete_value": true,
      "site": "0050d474",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
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
      "0050d438",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050d464",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050d484",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050d438",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050d464",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050d484",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d410.md#insn-0050d438) · [`0050d464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d410.md#insn-0050d464) · [`0050d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d410.md#insn-0050d484)
- 新版 `0050d438`（命令位置の公開資料なし） · `0050d464`（命令位置の公開資料なし） · `0050d484`（命令位置の公開資料なし）

~~~diff
- 0050d438 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050d438 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d438 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050d438 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d438 bytes a99643f9
+ 0050d438 bytes a9be43f9
- 0050d464 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050d464 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d464 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050d464 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d464 bytes a99643f9
+ 0050d464 bytes a9be43f9
- 0050d484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 0050d484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 0050d484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d484 bytes 087d40f9
+ 0050d484 bytes 08a540f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-834c02b92ce2c12cf0b9d9444492d626"></a>

### [`0050d5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d5a0.md) → [`0050d5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d5a0.md) FUN_0050d5a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0050d5e4",
      "incomplete_value": true,
      "site": "0050d5e4",
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
      "definition_site": "0050d5e4",
      "incomplete_value": true,
      "site": "0050d5e4",
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
      "0050d5dc",
      "READ",
      [
        "storage",
        "00c1b188",
        null,
        "pointer"
      ]
    ],
    [
      "0050d5e4",
      "DATA",
      [
        "storage",
        "00beb520",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "0050d5dc",
      "READ",
      [
        "storage",
        "00c1b1d8",
        null,
        "pointer"
      ]
    ],
    [
      "0050d5e4",
      "DATA",
      [
        "storage",
        "00beb570",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d5dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d5a0.md#insn-0050d5dc)
- 新版 `0050d5dc`（命令位置の公開資料なし）

~~~diff
- 0050d5dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:188:8"]]
- 0050d5dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d5dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1d8:8"]]
+ 0050d5dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d5dc bytes 29c540f9
+ 0050d5dc bytes 29ed40f9
~~~


<a id="compare-7b7f661a9fdcd1534ae3e9490dba2f22"></a>

### [`0050d608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d608.md) → [`0050d608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d608.md) FUN_0050d608

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050d640",
      "incomplete_value": false,
      "site": "0050d64c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:def:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d640",
      "incomplete_value": false,
      "site": "0050d64c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:e7c:8"
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
      "definition_site": "0050d66c",
      "incomplete_value": false,
      "site": "0050d674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:284:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d66c",
      "incomplete_value": false,
      "site": "0050d674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:286:8"
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
      "0050d640",
      "PARAM",
      [
        "storage",
        "00298e7c",
        null,
        "string"
      ]
    ],
    [
      "0050d66c",
      "PARAM",
      [
        "storage",
        "0029b286",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050d640",
      "PARAM",
      [
        "storage",
        "00298def",
        null,
        "string"
      ]
    ],
    [
      "0050d66c",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d608.md#insn-0050d640) · [`0050d66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d608.md#insn-0050d66c)
- 新版 `0050d640`（命令位置の公開資料なし） · `0050d66c`（命令位置の公開資料なし）

~~~diff
- 0050d640 ["COPY", "tmp:0:8", ["const:e7c:8"]]
- 0050d640 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0050d640 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0050d640 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0050d640 ["COPY", "tmp:0:8", ["const:def:8"]]
+ 0050d640 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0050d640 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0050d640 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0050d640 bytes 42f03991
+ 0050d640 bytes 42bc3791
- 0050d66c ["COPY", "tmp:0:8", ["const:286:8"]]
- 0050d66c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0050d66c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0050d66c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0050d66c ["COPY", "tmp:0:8", ["const:284:8"]]
+ 0050d66c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0050d66c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0050d66c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0050d66c bytes 21180a91
+ 0050d66c bytes 21100a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5229d7aa0e10db2e61b1519c0ab2517"></a>

### [`0050d78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d78c.md) → [`0050d78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d78c.md) FUN_0050d78c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d7b0",
      "incomplete_value": true,
      "site": "0050d7b4",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d7b0",
      "incomplete_value": true,
      "site": "0050d7b4",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d7d4",
      "incomplete_value": true,
      "site": "0050d7d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d7d4",
      "incomplete_value": true,
      "site": "0050d7d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d800",
      "incomplete_value": true,
      "site": "0050d800",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d800",
      "incomplete_value": true,
      "site": "0050d800",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
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
      "0050d7a8",
      "READ",
      [
        "storage",
        "00c1b198",
        null,
        "pointer"
      ]
    ],
    [
      "0050d7b4",
      "DATA",
      [
        "storage",
        "00bea098",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "0050d7c4",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050d7a8",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "0050d7b4",
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "0050d7c4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d78c.md#insn-0050d7a8) · [`0050d7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d78c.md#insn-0050d7c4) · [`0050d7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d78c.md#insn-0050d7f0)
- 新版 `0050d7a8`（命令位置の公開資料なし） · `0050d7c4`（命令位置の公開資料なし） · `0050d7f0`（命令位置の公開資料なし）

~~~diff
- 0050d7a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
- 0050d7a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d7a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 0050d7a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d7a8 bytes 08cd40f9
+ 0050d7a8 bytes 08f540f9
- 0050d7c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050d7c4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d7c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050d7c4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d7c4 bytes a99643f9
+ 0050d7c4 bytes a9be43f9
- 0050d7f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050d7f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d7f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050d7f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d7f0 bytes a99643f9
+ 0050d7f0 bytes a9be43f9
~~~


<a id="compare-4dbeee5a9b17732b560c9c9564188155"></a>

### [`0050d830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d830.md) → [`0050d830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d830.md) FUN_0050d830

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d854",
      "incomplete_value": true,
      "site": "0050d858",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d854",
      "incomplete_value": true,
      "site": "0050d858",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d878",
      "incomplete_value": true,
      "site": "0050d878",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d878",
      "incomplete_value": true,
      "site": "0050d878",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d8a4",
      "incomplete_value": true,
      "site": "0050d8a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d8a4",
      "incomplete_value": true,
      "site": "0050d8a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
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
      "0050d84c",
      "READ",
      [
        "storage",
        "00c1b198",
        null,
        "pointer"
      ]
    ],
    [
      "0050d858",
      "DATA",
      [
        "storage",
        "00bea098",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "0050d868",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050d84c",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "0050d858",
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "0050d868",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d830.md#insn-0050d84c) · [`0050d868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d830.md#insn-0050d868) · [`0050d894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d830.md#insn-0050d894)
- 新版 `0050d84c`（命令位置の公開資料なし） · `0050d868`（命令位置の公開資料なし） · `0050d894`（命令位置の公開資料なし）

~~~diff
- 0050d84c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
- 0050d84c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d84c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 0050d84c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d84c bytes 08cd40f9
+ 0050d84c bytes 08f540f9
- 0050d868 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050d868 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d868 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050d868 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d868 bytes a99643f9
+ 0050d868 bytes a9be43f9
- 0050d894 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050d894 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d894 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050d894 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d894 bytes a99643f9
+ 0050d894 bytes a9be43f9
~~~


<a id="compare-89d255a98bd15f96e33134025bf4ab5b"></a>

### [`0050d8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d8f4.md) → [`0050d8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md) FUN_0050d8f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`004a4d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4d4c.md) [`004a4d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a4/004a4d88.md) [`0050d9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d9e0.md) [`0050da6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da6c.md) [`0050da74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da74.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 6件 [`004a4d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d4c.md) [`004a4d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d88.md) [`0050d9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d9e0.md) [`0050da6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da6c.md) [`0050da74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da74.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.98% / 新版 92.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d92c",
      "incomplete_value": true,
      "site": "0050d930",
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
      "definition_site": "0050d92c",
      "incomplete_value": true,
      "site": "0050d930",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050d960",
      "incomplete_value": true,
      "site": "0050d960",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d960",
      "incomplete_value": true,
      "site": "0050d960",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d9b4",
      "incomplete_value": true,
      "site": "0050d9b4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d9b4",
      "incomplete_value": true,
      "site": "0050d9b4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
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
      "0050d920",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "0050d930",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050d950",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050d920",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "0050d930",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050d950",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d8f4.md#insn-0050d920) · [`0050d950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d8f4.md#insn-0050d950) · [`0050d9a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050d8f4.md#insn-0050d9a4)
- 新版 `0050d920`（命令位置の公開資料なし） · `0050d950`（命令位置の公開資料なし） · `0050d9a4`（命令位置の公開資料なし）

~~~diff
- 0050d920 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 0050d920 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d920 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 0050d920 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d920 bytes 081940f9
+ 0050d920 bytes 084140f9
- 0050d950 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 0050d950 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d950 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 0050d950 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d950 bytes c99643f9
+ 0050d950 bytes c9be43f9
- 0050d9a4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 0050d9a4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d9a4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 0050d9a4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d9a4 bytes c99643f9
+ 0050d9a4 bytes c9be43f9
~~~


<a id="compare-618ebd361164e028afb694fb685e1cb3"></a>

### [`0050da9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da9c.md) → [`0050da9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da9c.md) FUN_0050da9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050db70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050db70.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`0050db70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050db70.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050db18",
      "incomplete_value": true,
      "site": "0050db1c",
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
      "definition_site": "0050db18",
      "incomplete_value": true,
      "site": "0050db1c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050dad4",
      "incomplete_value": true,
      "site": "0050dad4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dad4",
      "incomplete_value": true,
      "site": "0050dad4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050db00",
      "incomplete_value": true,
      "site": "0050db00",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050db00",
      "incomplete_value": true,
      "site": "0050db00",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
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
      "0050dac4",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050daf0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050db10",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050dac4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050daf0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050db10",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da9c.md#insn-0050dac4) · [`0050daf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da9c.md#insn-0050daf0) · [`0050db10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050da9c.md#insn-0050db10)
- 新版 `0050dac4`（命令位置の公開資料なし） · `0050daf0`（命令位置の公開資料なし） · `0050db10`（命令位置の公開資料なし）

~~~diff
- 0050dac4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050dac4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dac4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050dac4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dac4 bytes a99643f9
+ 0050dac4 bytes a9be43f9
- 0050daf0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050daf0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050daf0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050daf0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050daf0 bytes a99643f9
+ 0050daf0 bytes a9be43f9
- 0050db10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 0050db10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050db10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 0050db10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050db10 bytes 087d40f9
+ 0050db10 bytes 08a540f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64ac16f01f9efa860ebd57959039d53f"></a>

### [`0050dbfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dbfc.md) → [`0050dbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dbfc.md) FUN_0050dbfc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050dc4c",
      "incomplete_value": true,
      "site": "0050dc50",
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
      "definition_site": "0050dc4c",
      "incomplete_value": true,
      "site": "0050dc50",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050dc34",
      "incomplete_value": true,
      "site": "0050dc34",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dc34",
      "incomplete_value": true,
      "site": "0050dc34",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050dc70",
      "incomplete_value": true,
      "site": "0050dc70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dc70",
      "incomplete_value": true,
      "site": "0050dc70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
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
      "0050dc24",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050dc44",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "0050dc50",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0050dc24",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050dc44",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "0050dc50",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dbfc.md#insn-0050dc24) · [`0050dc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dbfc.md#insn-0050dc44) · [`0050dc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dbfc.md#insn-0050dc60)
- 新版 `0050dc24`（命令位置の公開資料なし） · `0050dc44`（命令位置の公開資料なし） · `0050dc60`（命令位置の公開資料なし）

~~~diff
- 0050dc24 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050dc24 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dc24 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050dc24 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dc24 bytes a99643f9
+ 0050dc24 bytes a9be43f9
- 0050dc44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 0050dc44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dc44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 0050dc44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dc44 bytes 087d40f9
+ 0050dc44 bytes 08a540f9
- 0050dc60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050dc60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dc60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050dc60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dc60 bytes a99643f9
+ 0050dc60 bytes a9be43f9
~~~


<a id="compare-6192825a2a279e69ee7c8fc07870a8cd"></a>

### [`0050dca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dca0.md) → [`0050dca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dca0.md) FUN_0050dca0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050dcf0",
      "incomplete_value": true,
      "site": "0050dcf4",
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
      "definition_site": "0050dcf0",
      "incomplete_value": true,
      "site": "0050dcf4",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050dcd8",
      "incomplete_value": true,
      "site": "0050dcd8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dcd8",
      "incomplete_value": true,
      "site": "0050dcd8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050dd14",
      "incomplete_value": true,
      "site": "0050dd14",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dd14",
      "incomplete_value": true,
      "site": "0050dd14",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
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
      "0050dcc8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050dce8",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "0050dcf4",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0050dcc8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050dce8",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "0050dcf4",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dca0.md#insn-0050dcc8) · [`0050dce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dca0.md#insn-0050dce8) · [`0050dd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dca0.md#insn-0050dd04)
- 新版 `0050dcc8`（命令位置の公開資料なし） · `0050dce8`（命令位置の公開資料なし） · `0050dd04`（命令位置の公開資料なし）

~~~diff
- 0050dcc8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050dcc8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dcc8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050dcc8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dcc8 bytes a99643f9
+ 0050dcc8 bytes a9be43f9
- 0050dce8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 0050dce8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dce8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 0050dce8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dce8 bytes 087d40f9
+ 0050dce8 bytes 08a540f9
- 0050dd04 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050dd04 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050dd04 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050dd04 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dd04 bytes a99643f9
+ 0050dd04 bytes a9be43f9
~~~


<a id="compare-61e62f36014b9f071487f02a63f961da"></a>

### [`0050dda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dda4.md) → [`0050dda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dda4.md) FUN_0050dda4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050ddf4",
      "incomplete_value": true,
      "site": "0050ddf8",
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
      "definition_site": "0050ddf4",
      "incomplete_value": true,
      "site": "0050ddf8",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050dddc",
      "incomplete_value": true,
      "site": "0050dddc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050dddc",
      "incomplete_value": true,
      "site": "0050dddc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050de18",
      "incomplete_value": true,
      "site": "0050de18",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050de18",
      "incomplete_value": true,
      "site": "0050de18",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
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
      "0050ddcc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050ddec",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "0050ddf8",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0050ddcc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050ddec",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "0050ddf8",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ddcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dda4.md#insn-0050ddcc) · [`0050ddec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dda4.md#insn-0050ddec) · [`0050de08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dda4.md#insn-0050de08)
- 新版 `0050ddcc`（命令位置の公開資料なし） · `0050ddec`（命令位置の公開資料なし） · `0050de08`（命令位置の公開資料なし）

~~~diff
- 0050ddcc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050ddcc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ddcc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050ddcc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ddcc bytes a99643f9
+ 0050ddcc bytes a9be43f9
- 0050ddec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 0050ddec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ddec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 0050ddec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ddec bytes 087d40f9
+ 0050ddec bytes 08a540f9
- 0050de08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050de08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050de08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050de08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050de08 bytes a99643f9
+ 0050de08 bytes a9be43f9
~~~


<a id="compare-fbf8574e91b9eb4debae2f376d28e76b"></a>

### [`0050de48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050de48.md) → [`0050de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050de48.md) FUN_0050de48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050de98",
      "incomplete_value": true,
      "site": "0050de9c",
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
      "definition_site": "0050de98",
      "incomplete_value": true,
      "site": "0050de9c",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050de80",
      "incomplete_value": true,
      "site": "0050de80",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050de80",
      "incomplete_value": true,
      "site": "0050de80",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050debc",
      "incomplete_value": true,
      "site": "0050debc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050debc",
      "incomplete_value": true,
      "site": "0050debc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
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
      "0050de70",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0050de90",
      "READ",
      [
        "storage",
        "00c1b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "0050de9c",
      "DATA",
      [
        "storage",
        "00be9cc8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0050de70",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050de90",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "0050de9c",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050de70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050de48.md#insn-0050de70) · [`0050de90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050de48.md#insn-0050de90) · [`0050deac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050de48.md#insn-0050deac)
- 新版 `0050de70`（命令位置の公開資料なし） · `0050de90`（命令位置の公開資料なし） · `0050deac`（命令位置の公開資料なし）

~~~diff
- 0050de70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050de70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050de70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050de70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050de70 bytes a99643f9
+ 0050de70 bytes a9be43f9
- 0050de90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 0050de90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050de90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 0050de90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050de90 bytes 087d40f9
+ 0050de90 bytes 08a540f9
- 0050deac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050deac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050deac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050deac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050deac bytes a99643f9
+ 0050deac bytes a9be43f9
~~~


<a id="compare-783e9d4fe97c6e0f4be9224e1ee28c71"></a>

### [`0050dfd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dfd4.md) → [`0050dfd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dfd4.md) FUN_0050dfd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e00c",
      "incomplete_value": true,
      "site": "0050e00c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:786:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e00c",
      "incomplete_value": true,
      "site": "0050e00c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:6ec:8"
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
      "0050dffc",
      "READ",
      [
        "storage",
        "002a66ec",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050dffc",
      "READ",
      [
        "storage",
        "002a6786",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050d/0050dfd4.md#insn-0050dff0)
- 新版 `0050dff0`（命令位置の公開資料なし）

~~~diff
- 0050dff0 ["COPY", "tmp:0:8", ["const:6ec:8"]]
- 0050dff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050dff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050dff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050dff0 ["COPY", "tmp:0:8", ["const:786:8"]]
+ 0050dff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050dff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050dff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050dff0 bytes 29b11b91
+ 0050dff0 bytes 29191e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69f7b93253de9b2909d37a489ba465ce"></a>

### [`0050e07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e07c.md) → [`0050e07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e07c.md) FUN_0050e07c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e0a0",
      "incomplete_value": true,
      "site": "0050e0b0",
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
                "const:9c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e0a0",
      "incomplete_value": true,
      "site": "0050e0b0",
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
                "const:a57:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050e0b4",
      "incomplete_value": true,
      "site": "0050e0b4",
      "value": [
        "LOAD",
        "8",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e0b4",
      "incomplete_value": true,
      "site": "0050e0b4",
      "value": [
        "LOAD",
        "8",
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
                "const:f:8"
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
      "0050e0a0",
      "READ",
      [
        "storage",
        "002afa57",
        null,
        "string"
      ]
    ],
    [
      "0050e0a4",
      "READ",
      [
        "storage",
        "002afa66",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050e0a0",
      "READ",
      [
        "storage",
        "002af9c3",
        null,
        "string"
      ]
    ],
    [
      "0050e0a4",
      "READ",
      [
        "storage",
        "002af9d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e07c.md#insn-0050e098) · [`0050e09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e07c.md#insn-0050e09c)
- 新版 `0050e098`（命令位置の公開資料なし） · `0050e09c`（命令位置の公開資料なし）

~~~diff
- 0050e098 ["COPY", "tmp:0:8", ["const:a57:8"]]
- 0050e098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050e098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050e098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050e098 ["COPY", "tmp:0:8", ["const:9c3:8"]]
+ 0050e098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050e098 bytes 085d2991
+ 0050e098 bytes 080d2791
- 0050e09c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0050e09c bytes 09edffd0
+ 0050e09c ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0050e09c bytes 09edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43e2e950ecb13e991a0f155b1c302f79"></a>

### [`0050e0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e0cc.md) → [`0050e0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e0cc.md) FUN_0050e0cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0050e0f8",
      "incomplete_value": true,
      "site": "0050e0fc",
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
      "definition_site": "0050e0f8",
      "incomplete_value": true,
      "site": "0050e0fc",
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
      "0050e0ec",
      "READ",
      [
        "storage",
        "00c1b348",
        null,
        "pointer"
      ]
    ],
    [
      "0050e0fc",
      "DATA",
      [
        "storage",
        "00bea940",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0050e0ec",
      "READ",
      [
        "storage",
        "00c1b398",
        null,
        "pointer"
      ]
    ],
    [
      "0050e0fc",
      "DATA",
      [
        "storage",
        "00bea990",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e0cc.md#insn-0050e0ec)
- 新版 `0050e0ec`（命令位置の公開資料なし）

~~~diff
- 0050e0ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:348:8"]]
- 0050e0ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050e0ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:398:8"]]
+ 0050e0ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e0ec bytes 29a541f9
+ 0050e0ec bytes 29cd41f9
~~~


<a id="compare-058309ef5ac43ce107c59477215b78bd"></a>

### [`0050e114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e114.md) → [`0050e114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e114.md) FUN_0050e114

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e14c",
      "incomplete_value": true,
      "site": "0050e14c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:418:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e14c",
      "incomplete_value": true,
      "site": "0050e14c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:38d:8"
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
      "0050e13c",
      "READ",
      [
        "storage",
        "0029e38d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050e13c",
      "READ",
      [
        "storage",
        "0029e418",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e114.md#insn-0050e130)
- 新版 `0050e130`（命令位置の公開資料なし）

~~~diff
- 0050e130 ["COPY", "tmp:0:8", ["const:38d:8"]]
- 0050e130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050e130 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 0050e130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e130 bytes 29350e91
+ 0050e130 bytes 29611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e113920f533b8a988c72f9f7f7f9d71"></a>

### [`0050e1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e1bc.md) → [`0050e1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e1bc.md) FUN_0050e1bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e1d8",
      "incomplete_value": true,
      "site": "0050e1d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:bb4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e1d8",
      "incomplete_value": true,
      "site": "0050e1d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:c41:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050e1d0",
      "incomplete_value": true,
      "site": "0050e1dc",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e1d0",
      "incomplete_value": true,
      "site": "0050e1dc",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
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
      "0050e1c8",
      "READ",
      [
        "storage",
        "00299c41",
        null,
        "string"
      ]
    ],
    [
      "0050e1d0",
      "READ",
      [
        "storage",
        "00299c48",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050e1c8",
      "READ",
      [
        "storage",
        "00299bb4",
        null,
        "string"
      ]
    ],
    [
      "0050e1d0",
      "READ",
      [
        "storage",
        "00299bbb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e1bc.md#insn-0050e1c4)
- 新版 `0050e1c4`（命令位置の公開資料なし）

~~~diff
- 0050e1c4 ["COPY", "tmp:0:8", ["const:c41:8"]]
- 0050e1c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050e1c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050e1c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050e1c4 ["COPY", "tmp:0:8", ["const:bb4:8"]]
+ 0050e1c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050e1c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050e1c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050e1c4 bytes 4a053191
+ 0050e1c4 bytes 4ad12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82b8d79a8f28f91bf60ff2535fa52700"></a>

### [`0050e234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e234.md) → [`0050e234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e234.md) FUN_0050e234

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e26c",
      "incomplete_value": true,
      "site": "0050e26c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:45e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e26c",
      "incomplete_value": true,
      "site": "0050e26c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:3d3:8"
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
      "0050e25c",
      "READ",
      [
        "storage",
        "002a43d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050e25c",
      "READ",
      [
        "storage",
        "002a445e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e234.md#insn-0050e250)
- 新版 `0050e250`（命令位置の公開資料なし）

~~~diff
- 0050e250 ["COPY", "tmp:0:8", ["const:3d3:8"]]
- 0050e250 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e250 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e250 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050e250 ["COPY", "tmp:0:8", ["const:45e:8"]]
+ 0050e250 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e250 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e250 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e250 bytes 294d0f91
+ 0050e250 bytes 29791191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94f724f8fa23ab658212a8a05600b6a7"></a>

### [`0050e2dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e2dc.md) → [`0050e2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e2dc.md) FUN_0050e2dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e300",
      "incomplete_value": true,
      "site": "0050e310",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:334:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e300",
      "incomplete_value": true,
      "site": "0050e310",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:2a9:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050e304",
      "incomplete_value": true,
      "site": "0050e314",
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
                "const:b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e304",
      "incomplete_value": true,
      "site": "0050e314",
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
                "const:b:8"
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
      "0050e300",
      "READ",
      [
        "storage",
        "002a22a9",
        null,
        "string"
      ]
    ],
    [
      "0050e304",
      "READ",
      [
        "storage",
        "002a22b4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050e300",
      "READ",
      [
        "storage",
        "002a2334",
        null,
        "string"
      ]
    ],
    [
      "0050e304",
      "READ",
      [
        "storage",
        "002a233f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e2dc.md#insn-0050e2f8) · [`0050e2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e2dc.md#insn-0050e2fc)
- 新版 `0050e2f8`（命令位置の公開資料なし） · `0050e2fc`（命令位置の公開資料なし）

~~~diff
- 0050e2f8 ["COPY", "tmp:0:8", ["const:2a9:8"]]
- 0050e2f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050e2f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050e2f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050e2f8 ["COPY", "tmp:0:8", ["const:334:8"]]
+ 0050e2f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e2f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e2f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050e2f8 bytes 08a50a91
+ 0050e2f8 bytes 08d10c91
- 0050e2fc ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0050e2fc bytes 09edfff0
+ 0050e2fc ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0050e2fc bytes 09edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b377e1a7e3f2d4228e28aeaeb28bedc4"></a>

### [`0050e32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e32c.md) → [`0050e32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e32c.md) FUN_0050e32c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e360",
      "incomplete_value": true,
      "site": "0050e36c",
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
      "definition_site": "0050e360",
      "incomplete_value": true,
      "site": "0050e36c",
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
      "0050e350",
      "READ",
      [
        "storage",
        "00c1b370",
        null,
        "pointer"
      ]
    ],
    [
      "0050e36c",
      "DATA",
      [
        "storage",
        "00beaa18",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0050e350",
      "READ",
      [
        "storage",
        "00c1b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "0050e36c",
      "DATA",
      [
        "storage",
        "00beaa68",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e32c.md#insn-0050e350)
- 新版 `0050e350`（命令位置の公開資料なし）

~~~diff
- 0050e350 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
- 0050e350 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050e350 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3c0:8"]]
+ 0050e350 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e350 bytes 08b941f9
+ 0050e350 bytes 08e141f9
~~~


<a id="compare-9a77d4d437878ffa5475725902580d1d"></a>

### [`0050e43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e43c.md) → [`0050e43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e43c.md) FUN_0050e43c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e474",
      "incomplete_value": true,
      "site": "0050e474",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:720:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e474",
      "incomplete_value": true,
      "site": "0050e474",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:7ad:8"
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
      "0050e464",
      "READ",
      [
        "storage",
        "002947ad",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050e464",
      "READ",
      [
        "storage",
        "00294720",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e43c.md#insn-0050e458)
- 新版 `0050e458`（命令位置の公開資料なし）

~~~diff
- 0050e458 ["COPY", "tmp:0:8", ["const:7ad:8"]]
- 0050e458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050e458 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 0050e458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e458 bytes 29b51e91
+ 0050e458 bytes 29811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd82d4ce032ed1c518a541b2b54c5da4"></a>

### [`0050e534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e534.md) → [`0050e534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e534.md) FUN_0050e534

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e568",
      "incomplete_value": true,
      "site": "0050e574",
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
      "definition_site": "0050e568",
      "incomplete_value": true,
      "site": "0050e574",
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
      "0050e558",
      "READ",
      [
        "storage",
        "00c1b350",
        null,
        "pointer"
      ]
    ],
    [
      "0050e574",
      "DATA",
      [
        "storage",
        "00beb9b0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0050e558",
      "READ",
      [
        "storage",
        "00c1b3a0",
        null,
        "pointer"
      ]
    ],
    [
      "0050e574",
      "DATA",
      [
        "storage",
        "00beba00",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e534.md#insn-0050e558)
- 新版 `0050e558`（命令位置の公開資料なし）

~~~diff
- 0050e558 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
- 0050e558 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050e558 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
+ 0050e558 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e558 bytes 08a941f9
+ 0050e558 bytes 08d141f9
~~~


<a id="compare-b868be557c6384cfc27850c7b931b5c1"></a>

### [`0050e724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e724.md) → [`0050e724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e724.md) FUN_0050e724

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e748",
      "incomplete_value": true,
      "site": "0050e758",
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
                "const:294000:8"
              ],
              [
                "leaf",
                "const:702:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e748",
      "incomplete_value": true,
      "site": "0050e758",
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
                "const:294000:8"
              ],
              [
                "leaf",
                "const:78f:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050e74c",
      "incomplete_value": true,
      "site": "0050e75c",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e74c",
      "incomplete_value": true,
      "site": "0050e75c",
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
                "const:d:8"
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
      "0050e748",
      "READ",
      [
        "storage",
        "0029478f",
        null,
        "string"
      ]
    ],
    [
      "0050e74c",
      "READ",
      [
        "storage",
        "0029479c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050e748",
      "READ",
      [
        "storage",
        "00294702",
        null,
        "string"
      ]
    ],
    [
      "0050e74c",
      "READ",
      [
        "storage",
        "0029470f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e724.md#insn-0050e740) · [`0050e744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e724.md#insn-0050e744)
- 新版 `0050e740`（命令位置の公開資料なし） · `0050e744`（命令位置の公開資料なし）

~~~diff
- 0050e740 ["COPY", "tmp:0:8", ["const:78f:8"]]
- 0050e740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050e740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050e740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050e740 ["COPY", "tmp:0:8", ["const:702:8"]]
+ 0050e740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050e740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050e740 bytes 083d1e91
+ 0050e740 bytes 08091c91
- 0050e744 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0050e744 bytes 09edfff0
+ 0050e744 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0050e744 bytes 09edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80b258adc7cbf81a2ee6bd325cf6fbb8"></a>

### [`0050e774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e774.md) → [`0050e774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e774.md) FUN_0050e774

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519a68.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0050e79c",
      "incomplete_value": true,
      "site": "0050e79c",
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
      "definition_site": "0050e79c",
      "incomplete_value": true,
      "site": "0050e79c",
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
      "0050e794",
      "READ",
      [
        "storage",
        "00c1b358",
        null,
        "pointer"
      ]
    ],
    [
      "0050e79c",
      "DATA",
      [
        "storage",
        "00beba40",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0050e794",
      "READ",
      [
        "storage",
        "00c1b3a8",
        null,
        "pointer"
      ]
    ],
    [
      "0050e79c",
      "DATA",
      [
        "storage",
        "00beba90",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e774.md#insn-0050e794)
- 新版 `0050e794`（命令位置の公開資料なし）

~~~diff
- 0050e794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:358:8"]]
- 0050e794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050e794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a8:8"]]
+ 0050e794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e794 bytes 08ad41f9
+ 0050e794 bytes 08d541f9
~~~


<a id="compare-dca50a232fa78682e34fd2f50a651e51"></a>

### [`0050e84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e84c.md) → [`0050e84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e84c.md) FUN_0050e84c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e884",
      "incomplete_value": true,
      "site": "0050e884",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:292000:8"
              ],
              [
                "leaf",
                "const:77f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e884",
      "incomplete_value": true,
      "site": "0050e884",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:292000:8"
              ],
              [
                "leaf",
                "const:80c:8"
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
      "0050e874",
      "READ",
      [
        "storage",
        "0029280c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050e874",
      "READ",
      [
        "storage",
        "0029277f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e84c.md#insn-0050e868)
- 新版 `0050e868`（命令位置の公開資料なし）

~~~diff
- 0050e868 ["COPY", "tmp:0:8", ["const:80c:8"]]
- 0050e868 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e868 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e868 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050e868 ["COPY", "tmp:0:8", ["const:77f:8"]]
+ 0050e868 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e868 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050e868 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e868 bytes 29312091
+ 0050e868 bytes 29fd1d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a091962210393f51eb3a27d18cd3f45"></a>

### [`0050e944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e944.md) → [`0050e944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e944.md) FUN_0050e944

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519a68.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0050e96c",
      "incomplete_value": true,
      "site": "0050e96c",
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
      "definition_site": "0050e96c",
      "incomplete_value": true,
      "site": "0050e96c",
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
      "0050e964",
      "READ",
      [
        "storage",
        "00c1b378",
        null,
        "pointer"
      ]
    ],
    [
      "0050e96c",
      "DATA",
      [
        "storage",
        "00bebab8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0050e964",
      "READ",
      [
        "storage",
        "00c1b3c8",
        null,
        "pointer"
      ]
    ],
    [
      "0050e96c",
      "DATA",
      [
        "storage",
        "00bebb08",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050e944.md#insn-0050e964)
- 新版 `0050e964`（命令位置の公開資料なし）

~~~diff
- 0050e964 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
- 0050e964 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050e964 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3c8:8"]]
+ 0050e964 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e964 bytes 08bd41f9
+ 0050e964 bytes 08e541f9
~~~


<a id="compare-bb2c4022d50d3f31aff710783f495fb8"></a>

### [`0050ea1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ea1c.md) → [`0050ea1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ea1c.md) FUN_0050ea1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050ea54",
      "incomplete_value": true,
      "site": "0050ea54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:369:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ea54",
      "incomplete_value": true,
      "site": "0050ea54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:36b:8"
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
      "0050ea44",
      "READ",
      [
        "storage",
        "0029b36b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050ea44",
      "READ",
      [
        "storage",
        "0029b369",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ea38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ea1c.md#insn-0050ea38)
- 新版 `0050ea38`（命令位置の公開資料なし）

~~~diff
- 0050ea38 ["COPY", "tmp:0:8", ["const:36b:8"]]
- 0050ea38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050ea38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050ea38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050ea38 ["COPY", "tmp:0:8", ["const:369:8"]]
+ 0050ea38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050ea38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050ea38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050ea38 bytes 29ad0d91
+ 0050ea38 bytes 29a50d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14cd3355b5721fa85da241ca85a4e2b6"></a>

### [`0050eac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050eac4.md) → [`0050eac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050eac4.md) FUN_0050eac4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050eae8",
      "incomplete_value": true,
      "site": "0050eaf8",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:516:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050eae8",
      "incomplete_value": true,
      "site": "0050eaf8",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:47c:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050eafc",
      "incomplete_value": true,
      "site": "0050eafc",
      "value": [
        "LOAD",
        "8",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050eafc",
      "incomplete_value": true,
      "site": "0050eafc",
      "value": [
        "LOAD",
        "8",
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
                "const:f:8"
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
      "0050eae8",
      "READ",
      [
        "storage",
        "002a947c",
        null,
        "string"
      ]
    ],
    [
      "0050eaec",
      "READ",
      [
        "storage",
        "002a948b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050eae8",
      "READ",
      [
        "storage",
        "002a9516",
        null,
        "string"
      ]
    ],
    [
      "0050eaec",
      "READ",
      [
        "storage",
        "002a9525",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050eae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050eac4.md#insn-0050eae0) · [`0050eae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050eac4.md#insn-0050eae4)
- 新版 `0050eae0`（命令位置の公開資料なし） · `0050eae4`（命令位置の公開資料なし）

~~~diff
- 0050eae0 ["COPY", "tmp:0:8", ["const:47c:8"]]
- 0050eae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050eae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050eae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050eae0 ["COPY", "tmp:0:8", ["const:516:8"]]
+ 0050eae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050eae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050eae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050eae0 bytes 08f11191
+ 0050eae0 bytes 08591491
- 0050eae4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0050eae4 bytes 09edffd0
+ 0050eae4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0050eae4 bytes 09edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-992ab1ca1ee68f4b5b4bba67e35c28c1"></a>

### [`0050eb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050eb14.md) → [`0050eb14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050eb14.md) FUN_0050eb14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0051bf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d7fc.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0051bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050eb60",
      "incomplete_value": true,
      "site": "0050eb6c",
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
      "definition_site": "0050eb60",
      "incomplete_value": true,
      "site": "0050eb6c",
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
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050eb54",
      "READ",
      [
        "storage",
        "00c1b340",
        null,
        "pointer"
      ]
    ],
    [
      "0050eb6c",
      "DATA",
      [
        "storage",
        "00bea8e0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0050eb54",
      "READ",
      [
        "storage",
        "00c1b390",
        null,
        "pointer"
      ]
    ],
    [
      "0050eb6c",
      "DATA",
      [
        "storage",
        "00bea930",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050eb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050eb14.md#insn-0050eb54)
- 新版 `0050eb54`（命令位置の公開資料なし）

~~~diff
- 0050eb54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:340:8"]]
- 0050eb54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050eb54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
+ 0050eb54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050eb54 bytes 08a141f9
+ 0050eb54 bytes 08c941f9
~~~


<a id="compare-bf397007b0a45fb82c2607fe3800c20e"></a>

### [`0050edd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050edd4.md) → [`0050edd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050edd4.md) FUN_0050edd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050ede0",
      "incomplete_value": true,
      "site": "0050edf0",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:97a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ede0",
      "incomplete_value": true,
      "site": "0050edf0",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:a07:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050edf4",
      "incomplete_value": true,
      "site": "0050edf4",
      "value": [
        "LOAD",
        "8",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050edf4",
      "incomplete_value": true,
      "site": "0050edf4",
      "value": [
        "LOAD",
        "8",
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
                "const:e:8"
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
      "0050ede0",
      "READ",
      [
        "storage",
        "00295a07",
        null,
        "string"
      ]
    ],
    [
      "0050ede8",
      "READ",
      [
        "storage",
        "00295a15",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050ede0",
      "READ",
      [
        "storage",
        "0029597a",
        null,
        "string"
      ]
    ],
    [
      "0050ede8",
      "READ",
      [
        "storage",
        "00295988",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050eddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050edd4.md#insn-0050eddc)
- 新版 `0050eddc`（命令位置の公開資料なし）

~~~diff
- 0050eddc ["COPY", "tmp:0:8", ["const:a07:8"]]
- 0050eddc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050eddc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050eddc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050eddc ["COPY", "tmp:0:8", ["const:97a:8"]]
+ 0050eddc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050eddc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050eddc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050eddc bytes 4a1d2891
+ 0050eddc bytes 4ae92591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3e3e65133293365c7afbf9e6676a0bc"></a>

### [`0050edfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050edfc.md) → [`0050edfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050edfc.md) FUN_0050edfc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051ca38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051ca38.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0051ca38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051ca38.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0050ee24",
      "incomplete_value": true,
      "site": "0050ee24",
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
      "definition_site": "0050ee24",
      "incomplete_value": true,
      "site": "0050ee24",
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
      "0050ee1c",
      "READ",
      [
        "storage",
        "00c1b380",
        null,
        "pointer"
      ]
    ],
    [
      "0050ee24",
      "DATA",
      [
        "storage",
        "00bebb48",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0050ee1c",
      "READ",
      [
        "storage",
        "00c1b3d0",
        null,
        "pointer"
      ]
    ],
    [
      "0050ee24",
      "DATA",
      [
        "storage",
        "00bebb98",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ee1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050edfc.md#insn-0050ee1c)
- 新版 `0050ee1c`（命令位置の公開資料なし）

~~~diff
- 0050ee1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:380:8"]]
- 0050ee1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ee1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3d0:8"]]
+ 0050ee1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ee1c bytes 08c141f9
+ 0050ee1c bytes 08e941f9
~~~


<a id="compare-f32c87b4647e9092793b31750e2dabb2"></a>

### [`0050ee8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ee8c.md) → [`0050ee8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee8c.md) FUN_0050ee8c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050eec4",
      "incomplete_value": true,
      "site": "0050eec4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:477:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050eec4",
      "incomplete_value": true,
      "site": "0050eec4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:3ec:8"
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
      "0050eeb4",
      "READ",
      [
        "storage",
        "0029d3ec",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050eeb4",
      "READ",
      [
        "storage",
        "0029d477",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050eea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ee8c.md#insn-0050eea8)
- 新版 `0050eea8`（命令位置の公開資料なし）

~~~diff
- 0050eea8 ["COPY", "tmp:0:8", ["const:3ec:8"]]
- 0050eea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050eea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050eea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050eea8 ["COPY", "tmp:0:8", ["const:477:8"]]
+ 0050eea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050eea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050eea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050eea8 bytes 29b10f91
+ 0050eea8 bytes 29dd1191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a6bda119cab665a057d8a03e82d3b1d"></a>

### [`0050ef34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ef34.md) → [`0050ef34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ef34.md) FUN_0050ef34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050ef58",
      "incomplete_value": true,
      "site": "0050ef68",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:422:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ef58",
      "incomplete_value": true,
      "site": "0050ef68",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:397:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050ef5c",
      "incomplete_value": true,
      "site": "0050ef6c",
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
      "definition_site": "0050ef5c",
      "incomplete_value": true,
      "site": "0050ef6c",
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
      "0050ef58",
      "READ",
      [
        "storage",
        "0029e397",
        null,
        "string"
      ]
    ],
    [
      "0050ef5c",
      "READ",
      [
        "storage",
        "0029e3a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050ef58",
      "READ",
      [
        "storage",
        "0029e422",
        null,
        "string"
      ]
    ],
    [
      "0050ef5c",
      "READ",
      [
        "storage",
        "0029e42c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ef50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ef34.md#insn-0050ef50) · [`0050ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ef34.md#insn-0050ef54)
- 新版 `0050ef50`（命令位置の公開資料なし） · `0050ef54`（命令位置の公開資料なし）

~~~diff
- 0050ef50 ["COPY", "tmp:0:8", ["const:397:8"]]
- 0050ef50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050ef50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050ef50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050ef50 ["COPY", "tmp:0:8", ["const:422:8"]]
+ 0050ef50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050ef50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050ef50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050ef50 bytes 085d0e91
+ 0050ef50 bytes 08891091
- 0050ef54 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0050ef54 bytes 09edfff0
+ 0050ef54 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0050ef54 bytes 09edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4953f00a370af5ad8f3d732c1aaef08"></a>

### [`0050ef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ef84.md) → [`0050ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ef84.md) FUN_0050ef84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0051bf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d7fc.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0051bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050efd0",
      "incomplete_value": true,
      "site": "0050efdc",
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
      "definition_site": "0050efd0",
      "incomplete_value": true,
      "site": "0050efdc",
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
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050efc4",
      "READ",
      [
        "storage",
        "00c1b390",
        null,
        "pointer"
      ]
    ],
    [
      "0050efdc",
      "DATA",
      [
        "storage",
        "00bebbc0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0050efc4",
      "READ",
      [
        "storage",
        "00c1b3e0",
        null,
        "pointer"
      ]
    ],
    [
      "0050efdc",
      "DATA",
      [
        "storage",
        "00bebc10",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050efc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050e/0050ef84.md#insn-0050efc4)
- 新版 `0050efc4`（命令位置の公開資料なし）

~~~diff
- 0050efc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
- 0050efc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050efc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3e0:8"]]
+ 0050efc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050efc4 bytes 08c941f9
+ 0050efc4 bytes 08f141f9
~~~


<a id="compare-d0827ffaf3b5a24248b6cc205c9f61a6"></a>

### [`0050f19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f19c.md) → [`0050f19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f19c.md) FUN_0050f19c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f1c4",
      "incomplete_value": true,
      "site": "0050f1d4",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:49d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f1c4",
      "incomplete_value": true,
      "site": "0050f1d4",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:412:8"
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
      "0050f1c4",
      "READ",
      [
        "storage",
        "002a0412",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050f1c4",
      "READ",
      [
        "storage",
        "002a049d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f19c.md#insn-0050f1b8)
- 新版 `0050f1b8`（命令位置の公開資料なし）

~~~diff
- 0050f1b8 ["COPY", "tmp:0:8", ["const:412:8"]]
- 0050f1b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050f1b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050f1b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050f1b8 ["COPY", "tmp:0:8", ["const:49d:8"]]
+ 0050f1b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050f1b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050f1b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050f1b8 bytes 29491091
+ 0050f1b8 bytes 29751291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5b24fa8cba7f14fc30f02d155ebcfdf"></a>

### [`0050f294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f294.md) → [`0050f294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f294.md) FUN_0050f294

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0051d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d884.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f2cc",
      "incomplete_value": true,
      "site": "0050f2cc",
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
      "definition_site": "0050f2cc",
      "incomplete_value": true,
      "site": "0050f2cc",
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
      "0050f2bc",
      "READ",
      [
        "storage",
        "00c1b398",
        null,
        "pointer"
      ]
    ],
    [
      "0050f2cc",
      "DATA",
      [
        "storage",
        "00bebc38",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0050f2bc",
      "READ",
      [
        "storage",
        "00c1b3e8",
        null,
        "pointer"
      ]
    ],
    [
      "0050f2cc",
      "DATA",
      [
        "storage",
        "00bebc88",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f294.md#insn-0050f2bc) · [`0050f2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f294.md#insn-0050f2c4)
- 新版 `0050f2bc`（命令位置の公開資料なし） · `0050f2c4`（命令位置の公開資料なし）

~~~diff
- 0050f2bc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:398:8"]]
- 0050f2bc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050f2bc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3e8:8"]]
+ 0050f2bc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050f2bc bytes 29cd41f9
+ 0050f2bc bytes 29f541f9
- 0050f2c4 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0050f2c4 bytes f40300aa
+ 0050f2c4 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 0050f2c4 bytes f40300aa
~~~


<a id="compare-3818097ec18ef4d76b04fcb9c3ee8e75"></a>

### [`0050f534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f534.md) → [`0050f534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f534.md) FUN_0050f534

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f540",
      "incomplete_value": true,
      "site": "0050f54c",
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
                "const:29b000:8"
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
    "old": {
      "definition_site": "0050f540",
      "incomplete_value": true,
      "site": "0050f54c",
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
                "const:29b000:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050f540",
      "READ",
      [
        "storage",
        "0029b350",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050f540",
      "READ",
      [
        "storage",
        "0029b34e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f534.md#insn-0050f538)
- 新版 `0050f538`（命令位置の公開資料なし）

~~~diff
- 0050f538 ["COPY", "tmp:0:8", ["const:350:8"]]
- 0050f538 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050f538 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050f538 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050f538 ["COPY", "tmp:0:8", ["const:34e:8"]]
+ 0050f538 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050f538 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050f538 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050f538 bytes 4a410d91
+ 0050f538 bytes 4a390d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-917d63a8bf068c586f8f31e7c8de2a9b"></a>

### [`0050f560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f560.md) → [`0050f560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f560.md) FUN_0050f560

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f598",
      "incomplete_value": true,
      "site": "0050f598",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:963:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f598",
      "incomplete_value": true,
      "site": "0050f598",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:9f0:8"
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
      "0050f588",
      "READ",
      [
        "storage",
        "002969f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050f588",
      "READ",
      [
        "storage",
        "00296963",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f560.md#insn-0050f57c)
- 新版 `0050f57c`（命令位置の公開資料なし）

~~~diff
- 0050f57c ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0050f57c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050f57c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050f57c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050f57c ["COPY", "tmp:0:8", ["const:963:8"]]
+ 0050f57c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050f57c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050f57c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050f57c bytes 29c12791
+ 0050f57c bytes 298d2591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58136c7924362aae191d25e7ee4530b3"></a>

### [`0050f608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f608.md) → [`0050f608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f608.md) FUN_0050f608

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "0050f614",
      "incomplete_value": true,
      "site": "0050f624",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:26b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f614",
      "incomplete_value": true,
      "site": "0050f624",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:1d1:8"
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
      "0050f614",
      "READ",
      [
        "storage",
        "002a81d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050f614",
      "READ",
      [
        "storage",
        "002a826b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f608.md#insn-0050f60c)
- 新版 `0050f60c`（命令位置の公開資料なし）

~~~diff
- 0050f60c ["COPY", "tmp:0:8", ["const:1d1:8"]]
- 0050f60c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050f60c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050f60c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050f60c ["COPY", "tmp:0:8", ["const:26b:8"]]
+ 0050f60c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050f60c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050f60c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050f60c bytes 4a450791
+ 0050f60c bytes 4aad0991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00ea05e5776d9ad5f3fdcb6e02a8198c"></a>

### [`0050f680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f680.md) → [`0050f680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f680.md) FUN_0050f680

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f6b8",
      "incomplete_value": true,
      "site": "0050f6b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:a54:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f6b8",
      "incomplete_value": true,
      "site": "0050f6b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:ae1:8"
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
      "0050f6a8",
      "READ",
      [
        "storage",
        "00297ae1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050f6a8",
      "READ",
      [
        "storage",
        "00297a54",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f69c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f680.md#insn-0050f69c)
- 新版 `0050f69c`（命令位置の公開資料なし）

~~~diff
- 0050f69c ["COPY", "tmp:0:8", ["const:ae1:8"]]
- 0050f69c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050f69c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050f69c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050f69c ["COPY", "tmp:0:8", ["const:a54:8"]]
+ 0050f69c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050f69c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050f69c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050f69c bytes 29852b91
+ 0050f69c bytes 29512991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b51df6f1c9cf97cb4fb3cde5799c3ec"></a>

### [`0050f728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f728.md) → [`0050f728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f728.md) FUN_0050f728

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f74c",
      "incomplete_value": true,
      "site": "0050f75c",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:523:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f74c",
      "incomplete_value": true,
      "site": "0050f75c",
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
                "const:29c000:8"
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f750",
      "incomplete_value": true,
      "site": "0050f760",
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
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f750",
      "incomplete_value": true,
      "site": "0050f760",
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
                "const:c:8"
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
      "0050f74c",
      "READ",
      [
        "storage",
        "0029c498",
        null,
        "string"
      ]
    ],
    [
      "0050f750",
      "READ",
      [
        "storage",
        "0029c4a4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050f74c",
      "READ",
      [
        "storage",
        "0029c523",
        null,
        "string"
      ]
    ],
    [
      "0050f750",
      "READ",
      [
        "storage",
        "0029c52f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f728.md#insn-0050f744) · [`0050f748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f728.md#insn-0050f748)
- 新版 `0050f744`（命令位置の公開資料なし） · `0050f748`（命令位置の公開資料なし）

~~~diff
- 0050f744 ["COPY", "tmp:0:8", ["const:498:8"]]
- 0050f744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050f744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050f744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050f744 ["COPY", "tmp:0:8", ["const:523:8"]]
+ 0050f744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050f744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050f744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050f744 bytes 08611291
+ 0050f744 bytes 088d1491
- 0050f748 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0050f748 bytes 09edffd0
+ 0050f748 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0050f748 bytes 09edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc94cfa430ca949fd36a4a373f0efaa8"></a>

### [`0050f778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f778.md) → [`0050f778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f778.md) FUN_0050f778

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051cc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051cc00.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0051cc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cc00.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0050f7a4",
      "incomplete_value": true,
      "site": "0050f7a8",
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
      "definition_site": "0050f7a4",
      "incomplete_value": true,
      "site": "0050f7a8",
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
      "0050f798",
      "READ",
      [
        "storage",
        "00c1b388",
        null,
        "pointer"
      ]
    ],
    [
      "0050f7a8",
      "DATA",
      [
        "storage",
        "00bebda0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0050f798",
      "READ",
      [
        "storage",
        "00c1b3d8",
        null,
        "pointer"
      ]
    ],
    [
      "0050f7a8",
      "DATA",
      [
        "storage",
        "00bebdf0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050f778.md#insn-0050f798)
- 新版 `0050f798`（命令位置の公開資料なし）

~~~diff
- 0050f798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:388:8"]]
- 0050f798 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050f798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3d8:8"]]
+ 0050f798 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050f798 bytes 08c541f9
+ 0050f798 bytes 08ed41f9
~~~


<a id="compare-64baf2f2cef0543ad16af690d9efdee1"></a>

### [`0050fae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fae8.md) → [`0050fae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fae8.md) FUN_0050fae8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00519/00519a68.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0050fb18",
      "incomplete_value": false,
      "site": "0050fb18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:beb000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050fb18",
      "incomplete_value": false,
      "site": "0050fb18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:beb000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "definition_site": "0050fb18",
      "incomplete_value": true,
      "site": "0050fb18",
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
      "definition_site": "0050fb18",
      "incomplete_value": true,
      "site": "0050fb18",
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
      "0050fb10",
      "READ",
      [
        "storage",
        "00c1b3a8",
        null,
        "pointer"
      ]
    ],
    [
      "0050fb18",
      "DATA",
      [
        "storage",
        "00bebe60",
        null,
        "undefined *"
      ]
    ],
    [
      "0050fb18",
      "DATA",
      [
        "storage",
        "00bebe18",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050fb10",
      "READ",
      [
        "storage",
        "00c1b3f8",
        null,
        "pointer"
      ]
    ],
    [
      "0050fb18",
      "DATA",
      [
        "storage",
        "00bebeb0",
        null,
        "undefined *"
      ]
    ],
    [
      "0050fb18",
      "DATA",
      [
        "storage",
        "00bebe68",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050fb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fae8.md#insn-0050fb0c) · [`0050fb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fae8.md#insn-0050fb10)
- 新版 `0050fb0c`（命令位置の公開資料なし） · `0050fb10`（命令位置の公開資料なし）

~~~diff
- 0050fb0c ["COPY", "tmp:0:8", ["const:e60:8"]]
- 0050fb0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050fb0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050fb0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050fb0c ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0050fb0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050fb0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050fb0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050fb0c bytes 29813991
+ 0050fb0c bytes 29c13a91
- 0050fb10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a8:8"]]
- 0050fb10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050fb10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f8:8"]]
+ 0050fb10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050fb10 bytes 08d541f9
+ 0050fb10 bytes 08fd41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

