# v15.7.3 → v15.7.4 · 最優先の変更候補 (13)

[一覧の目次](README.md)

<a id="compare-28f5ed4b16be287067114575ea917265"></a>

### [`0050fc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fc5c.md) → [`0050fc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fc5c.md) FUN_0050fc5c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.74% / 新版 90.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050fca4",
      "incomplete_value": true,
      "site": "0050fca4",
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
      "definition_site": "0050fca4",
      "incomplete_value": true,
      "site": "0050fca4",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050fca4",
      "incomplete_value": true,
      "site": "0050fca4",
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
      "definition_site": "0050fca4",
      "incomplete_value": true,
      "site": "0050fca4",
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
      "0050fc88",
      "READ",
      [
        "storage",
        "00c1b3a0",
        null,
        "pointer"
      ]
    ],
    [
      "0050fc8c",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "0050fca4",
      "DATA",
      [
        "storage",
        "00bebed8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0050fc88",
      "READ",
      [
        "storage",
        "00c1b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "0050fc8c",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "0050fca4",
      "DATA",
      [
        "storage",
        "00bebf28",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050fc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fc5c.md#insn-0050fc88) · [`0050fc8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fc5c.md#insn-0050fc8c)
- 新版 `0050fc88`（命令位置の公開資料なし） · `0050fc8c`（命令位置の公開資料なし）

~~~diff
- 0050fc88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
- 0050fc88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050fc88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f0:8"]]
+ 0050fc88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050fc88 bytes 08d141f9
+ 0050fc88 bytes 08f941f9
- 0050fc8c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f00:8"]]
- 0050fc8c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050fc8c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f50:8"]]
+ 0050fc8c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050fc8c bytes 298147f9
+ 0050fc8c bytes 29a947f9
~~~


<a id="compare-d93238295c7b611538a4ee50de8ad2b2"></a>

### [`0050fea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fea8.md) → [`0050fea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fea8.md) FUN_0050fea8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0051ce40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051c/0051ce40.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdbca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbca0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0051ce40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051ce40.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdbcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "0050fed4",
      "incomplete_value": false,
      "site": "0050fed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050fed4",
      "incomplete_value": false,
      "site": "0050fed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "0050fed4",
      "DATA",
      [
        "storage",
        "00be9da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0050fed4",
      "DATA",
      [
        "storage",
        "00be9df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050fecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fea8.md#insn-0050fecc) · [`0050fed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050fea8.md#insn-0050fed0)
- 新版 `0050fecc`（命令位置の公開資料なし） · `0050fed0`（命令位置の公開資料なし）

~~~diff
- 0050fecc ["COPY", "tmp:0:8", ["const:da8:8"]]
- 0050fecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050fecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050fecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050fecc ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 0050fecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050fecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050fecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050fecc bytes 08a13691
+ 0050fecc bytes 08e13791
- 0050fed0 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0050fed0 bytes f40300aa
+ 0050fed0 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 0050fed0 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51c3c70deef1ea947bdca7edfb17edf0"></a>

### [`0050ffa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050ffa4.md) → [`0050ffa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050ffa4.md) FUN_0050ffa4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00510074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510074.md) · 呼出先 4件 [`004bb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb810.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00510074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510074.md) · 呼出先 4件 [`004bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051000c",
      "incomplete_value": true,
      "site": "0051000c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051000c",
      "incomplete_value": true,
      "site": "0051000c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510048",
      "incomplete_value": true,
      "site": "00510048",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510048",
      "incomplete_value": true,
      "site": "00510048",
      "value": [
        "LOAD",
        "8",
        [
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
      "0050fffc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00510038",
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
      "0050fffc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00510038",
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

- 旧版 [`0050fffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050ffa4.md#insn-0050fffc) · [`00510038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050f/0050ffa4.md#insn-00510038)
- 新版 `0050fffc`（命令位置の公開資料なし） · `00510038`（命令位置の公開資料なし）

~~~diff
- 0050fffc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0050fffc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050fffc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0050fffc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050fffc bytes a99643f9
+ 0050fffc bytes a9be43f9
- 00510038 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510038 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510038 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510038 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510038 bytes a99643f9
+ 00510038 bytes a9be43f9
~~~


<a id="compare-fb4e5590458f9691dc32c19bd9770ba7"></a>

### [`005100e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/005100e0.md) → [`005100e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005100e0.md) FUN_005100e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00510254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510254.md) · 呼出先 4件 [`004bb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb810.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00510254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510254.md) · 呼出先 4件 [`004bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00510148",
      "incomplete_value": true,
      "site": "00510148",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510148",
      "incomplete_value": true,
      "site": "00510148",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051018c",
      "incomplete_value": true,
      "site": "0051018c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051018c",
      "incomplete_value": true,
      "site": "0051018c",
      "value": [
        "LOAD",
        "8",
        [
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005101b8",
      "incomplete_value": true,
      "site": "005101b8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005101b8",
      "incomplete_value": true,
      "site": "005101b8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00510138",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0051017c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "005101a8",
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
      "00510138",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0051017c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "005101a8",
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

- 旧版 [`00510138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/005100e0.md#insn-00510138) · [`0051017c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/005100e0.md#insn-0051017c) · [`005101a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/005100e0.md#insn-005101a8)
- 新版 `00510138`（命令位置の公開資料なし） · `0051017c`（命令位置の公開資料なし） · `005101a8`（命令位置の公開資料なし）

~~~diff
- 00510138 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510138 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510138 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510138 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510138 bytes a99643f9
+ 00510138 bytes a9be43f9
- 0051017c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0051017c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051017c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0051017c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0051017c bytes a99643f9
+ 0051017c bytes a9be43f9
- 005101a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 005101a8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005101a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 005101a8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005101a8 bytes a99643f9
+ 005101a8 bytes a9be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af93526d31fa4b9283c62adf39d3267c"></a>

### [`00510588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510588.md) → [`00510588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510588.md) FUN_00510588

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051062c",
      "incomplete_value": true,
      "site": "0051062c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:eec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051062c",
      "incomplete_value": true,
      "site": "0051062c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:f79:8"
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
      "definition_site": "005105c8",
      "incomplete_value": false,
      "site": "005105d0",
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
            "const:977:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005105c8",
      "incomplete_value": false,
      "site": "005105d0",
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
            "const:a0b:8"
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
      "definition_site": "005105d8",
      "incomplete_value": false,
      "site": "005105e0",
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
      "definition_site": "005105d8",
      "incomplete_value": false,
      "site": "005105e0",
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
      "005105c8",
      "PARAM",
      [
        "storage",
        "002aea0b",
        null,
        "string"
      ]
    ],
    [
      "005105d8",
      "PARAM",
      [
        "storage",
        "0029b286",
        null,
        null
      ]
    ],
    [
      "0051061c",
      "READ",
      [
        "storage",
        "00298f79",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005105c8",
      "PARAM",
      [
        "storage",
        "002ae977",
        null,
        "string"
      ]
    ],
    [
      "005105d8",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ],
    [
      "0051061c",
      "READ",
      [
        "storage",
        "00298eec",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005105c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510588.md#insn-005105c8) · [`005105d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510588.md#insn-005105d8) · [`00510614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510588.md#insn-00510614)
- 新版 `005105c8`（命令位置の公開資料なし） · `005105d8`（命令位置の公開資料なし） · `00510614`（命令位置の公開資料なし）

~~~diff
- 005105c8 ["COPY", "tmp:0:8", ["const:a0b:8"]]
- 005105c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005105c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005105c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005105c8 ["COPY", "tmp:0:8", ["const:977:8"]]
+ 005105c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005105c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005105c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005105c8 bytes 002c2891
+ 005105c8 bytes 00dc2591
- 005105d8 ["COPY", "tmp:0:8", ["const:286:8"]]
- 005105d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005105d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005105d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005105d8 ["COPY", "tmp:0:8", ["const:284:8"]]
+ 005105d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005105d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005105d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005105d8 bytes 21180a91
+ 005105d8 bytes 21100a91
- 00510614 ["COPY", "tmp:0:8", ["const:f79:8"]]
- 00510614 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00510614 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00510614 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00510614 ["COPY", "tmp:0:8", ["const:eec:8"]]
+ 00510614 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00510614 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00510614 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00510614 bytes 29e53d91
+ 00510614 bytes 29b13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0757454a2577ccc54dfd2c84fbc92a95"></a>

### [`00510894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510894.md) → [`00510894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510894.md) FUN_00510894

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00510960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510960.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00510960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510960.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.84% / 新版 91.84%

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
      "definition_site": "005108fc",
      "incomplete_value": true,
      "site": "00510900",
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
      "definition_site": "005108fc",
      "incomplete_value": true,
      "site": "00510900",
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
      "definition_site": "005108e4",
      "incomplete_value": true,
      "site": "005108e4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005108e4",
      "incomplete_value": true,
      "site": "005108e4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00510930",
      "incomplete_value": true,
      "site": "00510930",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510930",
      "incomplete_value": true,
      "site": "00510930",
      "value": [
        "LOAD",
        "8",
        [
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
      "005108d4",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "005108f4",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "00510900",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "005108d4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "005108f4",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00510900",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005108d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510894.md#insn-005108d4) · [`005108f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510894.md#insn-005108f4) · [`00510920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510894.md#insn-00510920)
- 新版 `005108d4`（命令位置の公開資料なし） · `005108f4`（命令位置の公開資料なし） · `00510920`（命令位置の公開資料なし）

~~~diff
- 005108d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 005108d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005108d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 005108d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005108d4 bytes a99643f9
+ 005108d4 bytes a9be43f9
- 005108f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 005108f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005108f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 005108f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005108f4 bytes 081940f9
+ 005108f4 bytes 084140f9
- 00510920 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510920 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510920 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510920 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510920 bytes a99643f9
+ 00510920 bytes a9be43f9
~~~


<a id="compare-878bb8e5b243c9784b4cbd64f00ac8f4"></a>

### [`005109d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/005109d8.md) → [`005109d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005109d8.md) FUN_005109d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

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
      "definition_site": "005109f4",
      "incomplete_value": true,
      "site": "005109f8",
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
      "definition_site": "005109f4",
      "incomplete_value": true,
      "site": "005109f8",
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
      "definition_site": "00510a2c",
      "incomplete_value": true,
      "site": "00510a2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00510a2c",
      "incomplete_value": true,
      "site": "00510a2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "005109ec",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "005109f8",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00510a1c",
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
      "005109ec",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "005109f8",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00510a1c",
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

- 旧版 [`005109ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/005109d8.md#insn-005109ec) · [`00510a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/005109d8.md#insn-00510a1c)
- 新版 `005109ec`（命令位置の公開資料なし） · `00510a1c`（命令位置の公開資料なし）

~~~diff
- 005109ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 005109ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005109ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 005109ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005109ec bytes 081940f9
+ 005109ec bytes 084140f9
- 00510a1c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00510a1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510a1c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00510a1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510a1c bytes 299543f9
+ 00510a1c bytes 29bd43f9
~~~


<a id="compare-95854dbfe5477219f2191234c46a63b7"></a>

### [`00510a58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510a58.md) → [`00510a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510a58.md) FUN_00510a58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

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
      "definition_site": "00510a74",
      "incomplete_value": true,
      "site": "00510a78",
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
      "definition_site": "00510a74",
      "incomplete_value": true,
      "site": "00510a78",
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
      "definition_site": "00510aac",
      "incomplete_value": true,
      "site": "00510aac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00510aac",
      "incomplete_value": true,
      "site": "00510aac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00510a6c",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "00510a78",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00510a9c",
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
      "00510a6c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00510a78",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00510a9c",
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

- 旧版 [`00510a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510a58.md#insn-00510a6c) · [`00510a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510a58.md#insn-00510a9c)
- 新版 `00510a6c`（命令位置の公開資料なし） · `00510a9c`（命令位置の公開資料なし）

~~~diff
- 00510a6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 00510a6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510a6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 00510a6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00510a6c bytes 081940f9
+ 00510a6c bytes 084140f9
- 00510a9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00510a9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510a9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00510a9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510a9c bytes 299543f9
+ 00510a9c bytes 29bd43f9
~~~


<a id="compare-bced34d4a724192dd9493201b13dabfc"></a>

### [`00510acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510acc.md) → [`00510acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510acc.md) FUN_00510acc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00510be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510be8.md) [`00510c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510c0c.md) [`00510c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510c14.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 3件 [`00510be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510be8.md) [`00510c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c0c.md) [`00510c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c14.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00510b44",
      "incomplete_value": true,
      "site": "00510b48",
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
      "definition_site": "00510b44",
      "incomplete_value": true,
      "site": "00510b48",
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
      "definition_site": "00510b80",
      "incomplete_value": true,
      "site": "00510b84",
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
      "definition_site": "00510b80",
      "incomplete_value": true,
      "site": "00510b84",
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
      "definition_site": "00510b04",
      "incomplete_value": true,
      "site": "00510b04",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510b04",
      "incomplete_value": true,
      "site": "00510b04",
      "value": [
        "LOAD",
        "8",
        [
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
      "00510af4",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00510b3c",
      "READ",
      [
        "storage",
        "00c1b060",
        null,
        "pointer"
      ]
    ],
    [
      "00510b48",
      "DATA",
      [
        "storage",
        "00be9898",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00510af4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00510b3c",
      "READ",
      [
        "storage",
        "00c1b0b0",
        null,
        "pointer"
      ]
    ],
    [
      "00510b48",
      "DATA",
      [
        "storage",
        "00be98e8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00510af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510acc.md#insn-00510af4) · [`00510b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510acc.md#insn-00510b3c) · [`00510b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510acc.md#insn-00510b58)
- 新版 `00510af4`（命令位置の公開資料なし） · `00510b3c`（命令位置の公開資料なし） · `00510b58`（命令位置の公開資料なし）

~~~diff
- 00510af4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510af4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510af4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510af4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510af4 bytes a99643f9
+ 00510af4 bytes a9be43f9
- 00510b3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:60:8"]]
- 00510b3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510b3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b0:8"]]
+ 00510b3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00510b3c bytes 083140f9
+ 00510b3c bytes 085940f9
- 00510b58 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510b58 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510b58 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510b58 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510b58 bytes a99643f9
+ 00510b58 bytes a9be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc4bae0bcd1586e1c6c7b48dc7f0bfa1"></a>

### [`00510c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510c70.md) → [`00510c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c70.md) FUN_00510c70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00510ca8",
      "incomplete_value": true,
      "site": "00510ca8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510ca8",
      "incomplete_value": true,
      "site": "00510ca8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510cd4",
      "incomplete_value": true,
      "site": "00510cd4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510cd4",
      "incomplete_value": true,
      "site": "00510cd4",
      "value": [
        "LOAD",
        "8",
        [
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
      "00510c98",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00510cc4",
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
      "00510c98",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00510cc4",
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

- 旧版 [`00510c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510c70.md#insn-00510c98) · [`00510cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510c70.md#insn-00510cc4)
- 新版 `00510c98`（命令位置の公開資料なし） · `00510cc4`（命令位置の公開資料なし）

~~~diff
- 00510c98 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510c98 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510c98 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510c98 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510c98 bytes a99643f9
+ 00510c98 bytes a9be43f9
- 00510cc4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510cc4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510cc4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510cc4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510cc4 bytes a99643f9
+ 00510cc4 bytes a9be43f9
~~~


<a id="compare-23679417429d4e2ffc9b971faf44588c"></a>

### [`00510d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510d1c.md) → [`00510d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510d1c.md) FUN_00510d1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00510d54",
      "incomplete_value": true,
      "site": "00510d54",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510d54",
      "incomplete_value": true,
      "site": "00510d54",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510d80",
      "incomplete_value": true,
      "site": "00510d80",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510d80",
      "incomplete_value": true,
      "site": "00510d80",
      "value": [
        "LOAD",
        "8",
        [
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
      "00510d44",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00510d70",
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
      "00510d44",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00510d70",
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

- 旧版 [`00510d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510d1c.md#insn-00510d44) · [`00510d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510d1c.md#insn-00510d70)
- 新版 `00510d44`（命令位置の公開資料なし） · `00510d70`（命令位置の公開資料なし）

~~~diff
- 00510d44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510d44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510d44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510d44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510d44 bytes a99643f9
+ 00510d44 bytes a9be43f9
- 00510d70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510d70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510d70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510d70 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510d70 bytes a99643f9
+ 00510d70 bytes a9be43f9
~~~


<a id="compare-cf76c591cda2128d34843585ca583311"></a>

### [`00510dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510dc0.md) → [`00510dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510dc0.md) FUN_00510dc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbef0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

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
      "definition_site": "00510e68",
      "incomplete_value": true,
      "site": "00510e74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510e68",
      "incomplete_value": true,
      "site": "00510e74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:c1b000:8"
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
      "00510e68",
      "READ",
      [
        "storage",
        "00c1b000",
        null,
        "pointer"
      ]
    ],
    [
      "00510e68",
      "PARAM",
      [
        "storage",
        "00be94a0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00510e68",
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ],
    [
      "00510e68",
      "PARAM",
      [
        "storage",
        "00be94f0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00510e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510dc0.md#insn-00510e68)
- 新版 `00510e68`（命令位置の公開資料なし）

~~~diff
- 00510e68 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00510e68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510e68 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:50:8"]]
+ 00510e68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00510e68 bytes 210040f9
+ 00510e68 bytes 212840f9
~~~


<a id="compare-e28056aa18138cb099184ecc56314475"></a>

### [`00510f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510f14.md) → [`00510f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510f14.md) FUN_00510f14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00510f4c",
      "incomplete_value": true,
      "site": "00510f4c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510f4c",
      "incomplete_value": true,
      "site": "00510f4c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510f78",
      "incomplete_value": true,
      "site": "00510f78",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510f78",
      "incomplete_value": true,
      "site": "00510f78",
      "value": [
        "LOAD",
        "8",
        [
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
      "00510f3c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00510f68",
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
      "00510f3c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00510f68",
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

- 旧版 [`00510f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510f14.md#insn-00510f3c) · [`00510f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510f14.md#insn-00510f68)
- 新版 `00510f3c`（命令位置の公開資料なし） · `00510f68`（命令位置の公開資料なし）

~~~diff
- 00510f3c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510f3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510f3c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510f3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510f3c bytes a99643f9
+ 00510f3c bytes a9be43f9
- 00510f68 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510f68 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510f68 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510f68 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510f68 bytes a99643f9
+ 00510f68 bytes a9be43f9
~~~


<a id="compare-efc8c2afb392bc6529ffb954ff434225"></a>

### [`00510fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510fc0.md) → [`00510fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510fc0.md) FUN_00510fc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00510ff8",
      "incomplete_value": true,
      "site": "00510ff8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00510ff8",
      "incomplete_value": true,
      "site": "00510ff8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00511024",
      "incomplete_value": true,
      "site": "00511024",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00511024",
      "incomplete_value": true,
      "site": "00511024",
      "value": [
        "LOAD",
        "8",
        [
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
      "00510fe8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00511014",
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
      "00510fe8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00511014",
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

- 旧版 [`00510fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510fc0.md#insn-00510fe8) · [`00511014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510fc0.md#insn-00511014)
- 新版 `00510fe8`（命令位置の公開資料なし） · `00511014`（命令位置の公開資料なし）

~~~diff
- 00510fe8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00510fe8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510fe8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00510fe8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510fe8 bytes a99643f9
+ 00510fe8 bytes a9be43f9
- 00511014 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00511014 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511014 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00511014 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00511014 bytes a99643f9
+ 00511014 bytes a9be43f9
~~~


<a id="compare-bbceba30cf288d570cca5d851e83a1f8"></a>

### [`00511164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511164.md) → [`00511164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511164.md) FUN_00511164

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0051117c",
      "incomplete_value": false,
      "site": "00511180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051117c",
      "incomplete_value": false,
      "site": "00511180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "00511180",
      "DATA",
      [
        "storage",
        "00be9e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00511180",
      "DATA",
      [
        "storage",
        "00be9ea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051117c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511164.md#insn-0051117c)
- 新版 `0051117c`（命令位置の公開資料なし）

~~~diff
- 0051117c ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0051117c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051117c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051117c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051117c ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 0051117c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051117c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051117c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051117c bytes 29613991
+ 0051117c bytes 29a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb76a6fa34c99473cc750c9480babfc2"></a>

### [`005111c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005111c8.md) → [`005111c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005111c8.md) FUN_005111c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb920.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb970.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00511210",
      "incomplete_value": true,
      "site": "00511210",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511210",
      "incomplete_value": true,
      "site": "00511210",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:857:8"
              ]
            ]
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
      "definition_site": "0051123c",
      "incomplete_value": true,
      "site": "00511248",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0051123c",
      "incomplete_value": true,
      "site": "00511248",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "005111fc",
      "READ",
      [
        "storage",
        "002a6857",
        null,
        "string"
      ]
    ],
    [
      "0051123c",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0051123c",
      "PARAM",
      [
        "storage",
        "00be9238",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005111fc",
      "READ",
      [
        "storage",
        "002a68f1",
        null,
        "string"
      ]
    ],
    [
      "0051123c",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ],
    [
      "0051123c",
      "PARAM",
      [
        "storage",
        "00be9288",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005111f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005111c8.md#insn-005111f4) · [`0051123c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005111c8.md#insn-0051123c)
- 新版 `005111f4`（命令位置の公開資料なし） · `0051123c`（命令位置の公開資料なし）

~~~diff
- 005111f4 ["COPY", "tmp:0:8", ["const:857:8"]]
- 005111f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005111f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005111f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005111f4 ["COPY", "tmp:0:8", ["const:8f1:8"]]
+ 005111f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005111f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005111f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005111f4 bytes 295d2191
+ 005111f4 bytes 29c52391
- 0051123c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
- 0051123c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051123c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f98:8"]]
+ 0051123c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0051123c bytes 21a447f9
+ 0051123c bytes 21cc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d770a069aad5e7e5fbfd2508f0851560"></a>

### [`00511290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511290.md) → [`00511290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511290.md) FUN_00511290

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "005112a8",
      "incomplete_value": false,
      "site": "005112ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005112a8",
      "incomplete_value": false,
      "site": "005112ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "005112ac",
      "DATA",
      [
        "storage",
        "00be9ea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005112ac",
      "DATA",
      [
        "storage",
        "00be9ef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005112a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511290.md#insn-005112a8)
- 新版 `005112a8`（命令位置の公開資料なし）

~~~diff
- 005112a8 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 005112a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005112a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005112a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005112a8 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 005112a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005112a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005112a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005112a8 bytes 29a13a91
+ 005112a8 bytes 29e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afea4a7c28b02a79b3f087dd79d18250"></a>

### [`005112f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005112f4.md) → [`005112f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005112f4.md) FUN_005112f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb920.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb970.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051133c",
      "incomplete_value": true,
      "site": "0051133c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051133c",
      "incomplete_value": true,
      "site": "0051133c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:857:8"
              ]
            ]
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
      "definition_site": "00511368",
      "incomplete_value": true,
      "site": "00511374",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00511368",
      "incomplete_value": true,
      "site": "00511374",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00511328",
      "READ",
      [
        "storage",
        "002a6857",
        null,
        "string"
      ]
    ],
    [
      "00511368",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "00511368",
      "PARAM",
      [
        "storage",
        "00be9238",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00511328",
      "READ",
      [
        "storage",
        "002a68f1",
        null,
        "string"
      ]
    ],
    [
      "00511368",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ],
    [
      "00511368",
      "PARAM",
      [
        "storage",
        "00be9288",
        "_ZTIN5Botan9ExceptionE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005112f4.md#insn-00511320) · [`00511368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005112f4.md#insn-00511368)
- 新版 `00511320`（命令位置の公開資料なし） · `00511368`（命令位置の公開資料なし）

~~~diff
- 00511320 ["COPY", "tmp:0:8", ["const:857:8"]]
- 00511320 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00511320 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00511320 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00511320 ["COPY", "tmp:0:8", ["const:8f1:8"]]
+ 00511320 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00511320 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00511320 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00511320 bytes 295d2191
+ 00511320 bytes 29c52391
- 00511368 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
- 00511368 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511368 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f98:8"]]
+ 00511368 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00511368 bytes 21a447f9
+ 00511368 bytes 21cc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83556ad1ca736752e060865877694e86"></a>

### [`005113bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005113bc.md) → [`005113bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005113bc.md) FUN_005113bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005113ec",
      "incomplete_value": true,
      "site": "00511400",
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
                "const:744:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005113ec",
      "incomplete_value": true,
      "site": "00511400",
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
                "const:6b9:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005113f0",
      "incomplete_value": true,
      "site": "00511404",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005113f0",
      "incomplete_value": true,
      "site": "00511404",
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
                "const:9:8"
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
      "definition_site": "00511410",
      "incomplete_value": true,
      "site": "00511410",
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
      "definition_site": "00511410",
      "incomplete_value": true,
      "site": "00511410",
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
      "005113ec",
      "READ",
      [
        "storage",
        "002a16b9",
        null,
        "string"
      ]
    ],
    [
      "005113f0",
      "READ",
      [
        "storage",
        "002a16c2",
        null,
        "string"
      ]
    ],
    [
      "005113f8",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005113ec",
      "READ",
      [
        "storage",
        "002a1744",
        null,
        "string"
      ]
    ],
    [
      "005113f0",
      "READ",
      [
        "storage",
        "002a174d",
        null,
        "string"
      ]
    ],
    [
      "005113f8",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005113e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005113bc.md#insn-005113e4) · [`005113e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005113bc.md#insn-005113e8)
- 新版 `005113e4`（命令位置の公開資料なし） · `005113e8`（命令位置の公開資料なし）

~~~diff
- 005113e4 ["COPY", "tmp:0:8", ["const:6b9:8"]]
- 005113e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005113e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005113e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005113e4 ["COPY", "tmp:0:8", ["const:744:8"]]
+ 005113e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005113e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005113e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005113e4 bytes 08e51a91
+ 005113e4 bytes 08111d91
- 005113e8 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 005113e8 bytes f40300aa
+ 005113e8 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 005113e8 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-582d5e10c79ae18f889c9a3142bc50cd"></a>

### [`00511488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511488.md) → [`00511488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511488.md) FUN_00511488

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005114b8",
      "incomplete_value": true,
      "site": "005114cc",
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
                "const:296000:8"
              ],
              [
                "leaf",
                "const:b93:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005114b8",
      "incomplete_value": true,
      "site": "005114cc",
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
                "const:296000:8"
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005114bc",
      "incomplete_value": true,
      "site": "005114d0",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005114bc",
      "incomplete_value": true,
      "site": "005114d0",
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
                "const:e:8"
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
      "definition_site": "005114dc",
      "incomplete_value": true,
      "site": "005114dc",
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
      "definition_site": "005114dc",
      "incomplete_value": true,
      "site": "005114dc",
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
      "005114b8",
      "READ",
      [
        "storage",
        "00296c20",
        null,
        "string"
      ]
    ],
    [
      "005114bc",
      "READ",
      [
        "storage",
        "00296c2e",
        null,
        "string"
      ]
    ],
    [
      "005114c4",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005114b8",
      "READ",
      [
        "storage",
        "00296b93",
        null,
        "string"
      ]
    ],
    [
      "005114bc",
      "READ",
      [
        "storage",
        "00296ba1",
        null,
        "string"
      ]
    ],
    [
      "005114c4",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005114b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511488.md#insn-005114b0) · [`005114b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511488.md#insn-005114b4)
- 新版 `005114b0`（命令位置の公開資料なし） · `005114b4`（命令位置の公開資料なし）

~~~diff
- 005114b0 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 005114b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005114b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005114b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005114b0 ["COPY", "tmp:0:8", ["const:b93:8"]]
+ 005114b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005114b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005114b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005114b0 bytes 08813091
+ 005114b0 bytes 084d2e91
- 005114b4 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 005114b4 bytes f40300aa
+ 005114b4 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 005114b4 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31e19d507d389bca4f7020003cdbeabb"></a>

### [`00511554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511554.md) → [`00511554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511554.md) FUN_00511554

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00511564",
      "incomplete_value": false,
      "site": "00511564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511564",
      "incomplete_value": false,
      "site": "00511564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "00511564",
      "DATA",
      [
        "storage",
        "00be9f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00511564",
      "DATA",
      [
        "storage",
        "00be9f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511554.md#insn-00511560)
- 新版 `00511560`（命令位置の公開資料なし）

~~~diff
- 00511560 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00511560 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00511560 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00511560 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00511560 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00511560 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00511560 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00511560 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00511560 bytes 29213c91
+ 00511560 bytes 29613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9748dc420c6c4688608320c3830ae253"></a>

### [`00511580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511580.md) → [`00511580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511580.md) FUN_00511580

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00511590",
      "incomplete_value": false,
      "site": "00511590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511590",
      "incomplete_value": false,
      "site": "00511590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "00511590",
      "DATA",
      [
        "storage",
        "00be9f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00511590",
      "DATA",
      [
        "storage",
        "00be9f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051158c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511580.md#insn-0051158c)
- 新版 `0051158c`（命令位置の公開資料なし）

~~~diff
- 0051158c ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0051158c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051158c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051158c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051158c ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0051158c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051158c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051158c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051158c bytes 29e13c91
+ 0051158c bytes 29213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c40459ff1dc48c95a51feb7936ab2d9e"></a>

### [`005115ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005115ac.md) → [`005115ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005115ac.md) FUN_005115ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005115d0",
      "incomplete_value": true,
      "site": "005115dc",
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
      "definition_site": "005115d0",
      "incomplete_value": true,
      "site": "005115dc",
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
      "definition_site": "005115fc",
      "incomplete_value": true,
      "site": "005115fc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005115fc",
      "incomplete_value": true,
      "site": "005115fc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00511628",
      "incomplete_value": true,
      "site": "00511628",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00511628",
      "incomplete_value": true,
      "site": "00511628",
      "value": [
        "LOAD",
        "8",
        [
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
      "005115c4",
      "READ",
      [
        "storage",
        "00c1b198",
        null,
        "pointer"
      ]
    ],
    [
      "005115dc",
      "DATA",
      [
        "storage",
        "00bea098",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005115ec",
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
      "005115c4",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "005115dc",
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005115ec",
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

- 旧版 [`005115c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005115ac.md#insn-005115c4) · [`005115ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005115ac.md#insn-005115ec) · [`00511618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005115ac.md#insn-00511618)
- 新版 `005115c4`（命令位置の公開資料なし） · `005115ec`（命令位置の公開資料なし） · `00511618`（命令位置の公開資料なし）

~~~diff
- 005115c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
- 005115c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005115c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 005115c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005115c4 bytes 08cd40f9
+ 005115c4 bytes 08f540f9
- 005115ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 005115ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005115ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 005115ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005115ec bytes a99643f9
+ 005115ec bytes a9be43f9
- 00511618 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00511618 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511618 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00511618 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00511618 bytes a99643f9
+ 00511618 bytes a9be43f9
~~~


<a id="compare-1cec54cf446a4c8850b3177c7dc1091d"></a>

### [`00511658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511658.md) → [`00511658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511658.md) FUN_00511658

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

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
      "definition_site": "0051167c",
      "incomplete_value": true,
      "site": "00511688",
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
      "definition_site": "0051167c",
      "incomplete_value": true,
      "site": "00511688",
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
      "definition_site": "005116a8",
      "incomplete_value": true,
      "site": "005116a8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005116a8",
      "incomplete_value": true,
      "site": "005116a8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005116d4",
      "incomplete_value": true,
      "site": "005116d4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005116d4",
      "incomplete_value": true,
      "site": "005116d4",
      "value": [
        "LOAD",
        "8",
        [
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
      "00511670",
      "READ",
      [
        "storage",
        "00c1b198",
        null,
        "pointer"
      ]
    ],
    [
      "00511688",
      "DATA",
      [
        "storage",
        "00bea098",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00511698",
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
      "00511670",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "00511688",
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00511698",
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

- 旧版 [`00511670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511658.md#insn-00511670) · [`00511698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511658.md#insn-00511698) · [`005116c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511658.md#insn-005116c4)
- 新版 `00511670`（命令位置の公開資料なし） · `00511698`（命令位置の公開資料なし） · `005116c4`（命令位置の公開資料なし）

~~~diff
- 00511670 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
- 00511670 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511670 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 00511670 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00511670 bytes 08cd40f9
+ 00511670 bytes 08f540f9
- 00511698 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00511698 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511698 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00511698 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00511698 bytes a99643f9
+ 00511698 bytes a9be43f9
- 005116c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 005116c4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005116c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 005116c4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005116c4 bytes a99643f9
+ 005116c4 bytes a9be43f9
~~~


<a id="compare-dc0007bde8ba9676c193422063e339da"></a>

### [`00511720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511720.md) → [`00511720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511720.md) FUN_00511720

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d1fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d1fc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0051d1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d1fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00511734",
      "incomplete_value": true,
      "site": "00511738",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511734",
      "incomplete_value": true,
      "site": "00511738",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a8:8"
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
      "00511734",
      "READ",
      [
        "storage",
        "00c1b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "00511734",
      "PARAM",
      [
        "storage",
        "00bea318",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      "00511734",
      "READ",
      [
        "storage",
        "00c1b1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00511734",
      "PARAM",
      [
        "storage",
        "00bea368",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511720.md#insn-00511734)
- 新版 `00511734`（命令位置の公開資料なし）

~~~diff
- 00511734 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1a8:8"]]
- 00511734 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511734 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1f8:8"]]
+ 00511734 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00511734 bytes 21d440f9
+ 00511734 bytes 21fc40f9
~~~


<a id="compare-71a1ecd1fc0b4b88ff46a91983f522ad"></a>

### [`0051175c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/0051175c.md) → [`0051175c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051175c.md) FUN_0051175c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d1fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d1fc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0051d1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d1fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00511770",
      "incomplete_value": true,
      "site": "00511778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511770",
      "incomplete_value": true,
      "site": "00511778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a8:8"
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
      "00511770",
      "READ",
      [
        "storage",
        "00c1b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "00511770",
      "PARAM",
      [
        "storage",
        "00bea318",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      "00511770",
      "READ",
      [
        "storage",
        "00c1b1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00511770",
      "PARAM",
      [
        "storage",
        "00bea368",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/0051175c.md#insn-00511770)
- 新版 `00511770`（命令位置の公開資料なし）

~~~diff
- 00511770 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1a8:8"]]
- 00511770 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511770 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1f8:8"]]
+ 00511770 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00511770 bytes 21d440f9
+ 00511770 bytes 21fc40f9
~~~


<a id="compare-0d493e82fa0b4d23b05005a46cefaa4f"></a>

### [`00511934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511934.md) → [`00511934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511934.md) FUN_00511934

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

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
      "definition_site": "00511950",
      "incomplete_value": true,
      "site": "00511954",
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
      "definition_site": "00511950",
      "incomplete_value": true,
      "site": "00511954",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00511990",
      "incomplete_value": true,
      "site": "00511994",
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
      "definition_site": "00511990",
      "incomplete_value": true,
      "site": "00511994",
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
      "00511948",
      "READ",
      [
        "storage",
        "00c1b2a0",
        null,
        "pointer"
      ]
    ],
    [
      "00511954",
      "DATA",
      [
        "storage",
        "00beaa78",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00511988",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00511948",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "00511954",
      "DATA",
      [
        "storage",
        "00beaac8",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00511988",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511934.md#insn-00511948) · [`00511988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511934.md#insn-00511988)
- 新版 `00511948`（命令位置の公開資料なし） · `00511988`（命令位置の公開資料なし）

~~~diff
- 00511948 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 00511948 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511948 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
+ 00511948 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00511948 bytes 085141f9
+ 00511948 bytes 087941f9
- 00511988 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 00511988 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511988 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 00511988 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00511988 bytes 088d41f9
+ 00511988 bytes 08b541f9
~~~


<a id="compare-67796b8a54a5263b7548233175982021"></a>

### [`005119e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005119e4.md) → [`005119e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005119e4.md) FUN_005119e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00511a00",
      "incomplete_value": true,
      "site": "00511a04",
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
      "definition_site": "00511a00",
      "incomplete_value": true,
      "site": "00511a04",
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
      "005119f8",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "00511a04",
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
      "005119f8",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "00511a04",
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

- 旧版 [`005119f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/005119e4.md#insn-005119f8)
- 新版 `005119f8`（命令位置の公開資料なし）

~~~diff
- 005119f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 005119f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005119f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 005119f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005119f8 bytes 088d41f9
+ 005119f8 bytes 08b541f9
~~~


<a id="compare-3c21c8c1c0eb5d34e6a9d1bfea401c64"></a>

### [`00511eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511eb0.md) → [`00511eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511eb0.md) FUN_00511eb0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00511ecc",
      "incomplete_value": true,
      "site": "00511ed0",
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
      "definition_site": "00511ecc",
      "incomplete_value": true,
      "site": "00511ed0",
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
      "00511ec4",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00511ed0",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00511ec4",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00511ed0",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511eb0.md#insn-00511ec4)
- 新版 `00511ec4`（命令位置の公開資料なし）

~~~diff
- 00511ec4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00511ec4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511ec4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00511ec4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00511ec4 bytes 08c947f9
+ 00511ec4 bytes 08f147f9
~~~


<a id="compare-232a81d6f1a03b861bf4f7b335f22f02"></a>

### [`00511f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511f10.md) → [`00511f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511f10.md) FUN_00511f10

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00511f2c",
      "incomplete_value": true,
      "site": "00511f30",
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
      "definition_site": "00511f2c",
      "incomplete_value": true,
      "site": "00511f30",
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
      "00511f24",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00511f30",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00511f24",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00511f30",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511f10.md#insn-00511f24)
- 新版 `00511f24`（命令位置の公開資料なし）

~~~diff
- 00511f24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00511f24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511f24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00511f24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00511f24 bytes 08c947f9
+ 00511f24 bytes 08f147f9
~~~


<a id="compare-477c27b1870822a2f7f98b5c42f7ff92"></a>

### [`00511fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511fe0.md) → [`00511fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511fe0.md) FUN_00511fe0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

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
      "definition_site": "00511ffc",
      "incomplete_value": true,
      "site": "00512000",
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
      "definition_site": "00511ffc",
      "incomplete_value": true,
      "site": "00512000",
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
      "definition_site": "00512034",
      "incomplete_value": true,
      "site": "00512034",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00512034",
      "incomplete_value": true,
      "site": "00512034",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00511ff4",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "00512000",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00512024",
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
      "00511ff4",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00512000",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00512024",
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

- 旧版 [`00511ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511fe0.md#insn-00511ff4) · [`00512024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00511/00511fe0.md#insn-00512024)
- 新版 `00511ff4`（命令位置の公開資料なし） · `00512024`（命令位置の公開資料なし）

~~~diff
- 00511ff4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 00511ff4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511ff4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 00511ff4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00511ff4 bytes 081940f9
+ 00511ff4 bytes 084140f9
- 00512024 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00512024 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512024 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00512024 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00512024 bytes 299543f9
+ 00512024 bytes 29bd43f9
~~~


<a id="compare-f12767feea47bbe094fffa5da58d76cf"></a>

### [`00512058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512058.md) → [`00512058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512058.md) FUN_00512058

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

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
      "definition_site": "00512074",
      "incomplete_value": true,
      "site": "00512078",
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
      "definition_site": "00512074",
      "incomplete_value": true,
      "site": "00512078",
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
      "definition_site": "005120ac",
      "incomplete_value": true,
      "site": "005120ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005120ac",
      "incomplete_value": true,
      "site": "005120ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0051206c",
      "READ",
      [
        "storage",
        "00c1b030",
        null,
        "pointer"
      ]
    ],
    [
      "00512078",
      "DATA",
      [
        "storage",
        "00be99c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0051209c",
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
      "0051206c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00512078",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0051209c",
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

- 旧版 [`0051206c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512058.md#insn-0051206c) · [`0051209c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512058.md#insn-0051209c)
- 新版 `0051206c`（命令位置の公開資料なし） · `0051209c`（命令位置の公開資料なし）

~~~diff
- 0051206c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 0051206c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051206c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 0051206c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051206c bytes 081940f9
+ 0051206c bytes 084140f9
- 0051209c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0051209c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051209c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0051209c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0051209c bytes 299543f9
+ 0051209c bytes 29bd43f9
~~~


<a id="compare-4925942bd98f3ff9da3879f95c955896"></a>

### [`0051215c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/0051215c.md) → [`0051215c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/0051215c.md) FUN_0051215c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00512170",
      "incomplete_value": true,
      "site": "00512170",
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
      "definition_site": "00512170",
      "incomplete_value": true,
      "site": "00512170",
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
      "00512164",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "00512170",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00512164",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00512170",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/0051215c.md#insn-00512164)
- 新版 `00512164`（命令位置の公開資料なし）

~~~diff
- 00512164 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:170:8"]]
- 00512164 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512164 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1c0:8"]]
+ 00512164 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00512164 bytes 29b940f9
+ 00512164 bytes 29e140f9
~~~


<a id="compare-db828b3d684a996f011c26d8cf4bd574"></a>

### [`00512480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512480.md) → [`00512480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512480.md) FUN_00512480

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "0051249c",
      "incomplete_value": true,
      "site": "005124a0",
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
      "definition_site": "0051249c",
      "incomplete_value": true,
      "site": "005124a0",
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
      "00512494",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "005124a0",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00512494",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005124a0",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512480.md#insn-00512494)
- 新版 `00512494`（命令位置の公開資料なし）

~~~diff
- 00512494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00512494 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00512494 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512494 bytes 08c947f9
+ 00512494 bytes 08f147f9
~~~


<a id="compare-da2056776f2379b69ca5d013cf993839"></a>

### [`005124c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005124c8.md) → [`005124c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005124c8.md) FUN_005124c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "005124e4",
      "incomplete_value": true,
      "site": "005124e8",
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
      "definition_site": "005124e4",
      "incomplete_value": true,
      "site": "005124e8",
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
      "005124dc",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "005124e8",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005124dc",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005124e8",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005124dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005124c8.md#insn-005124dc)
- 新版 `005124dc`（命令位置の公開資料なし）

~~~diff
- 005124dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 005124dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005124dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005124dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005124dc bytes 08c947f9
+ 005124dc bytes 08f147f9
~~~


<a id="compare-43c49539451ac1e4a036c6841916707d"></a>

### [`00512510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512510.md) → [`00512510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512510.md) FUN_00512510

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "0051252c",
      "incomplete_value": true,
      "site": "00512530",
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
      "definition_site": "0051252c",
      "incomplete_value": true,
      "site": "00512530",
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
      "00512524",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512530",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00512524",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512530",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512510.md#insn-00512524)
- 新版 `00512524`（命令位置の公開資料なし）

~~~diff
- 00512524 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00512524 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512524 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00512524 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512524 bytes 08c947f9
+ 00512524 bytes 08f147f9
~~~


<a id="compare-c6a621bfe6a5d0ef09dd3a48b9296295"></a>

### [`00512558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512558.md) → [`00512558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512558.md) FUN_00512558

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00512574",
      "incomplete_value": true,
      "site": "00512578",
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
      "definition_site": "00512574",
      "incomplete_value": true,
      "site": "00512578",
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
      "0051256c",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512578",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0051256c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512578",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051256c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512558.md#insn-0051256c)
- 新版 `0051256c`（命令位置の公開資料なし）

~~~diff
- 0051256c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 0051256c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051256c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0051256c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051256c bytes 08c947f9
+ 0051256c bytes 08f147f9
~~~


<a id="compare-83ed41824a3f9894e8e75048bf7d1a39"></a>

### [`005125a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005125a0.md) → [`005125a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125a0.md) FUN_005125a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "005125bc",
      "incomplete_value": true,
      "site": "005125c0",
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
      "definition_site": "005125bc",
      "incomplete_value": true,
      "site": "005125c0",
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
      "005125b4",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "005125c0",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005125b4",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005125c0",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005125b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005125a0.md#insn-005125b4)
- 新版 `005125b4`（命令位置の公開資料なし）

~~~diff
- 005125b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 005125b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005125b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005125b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005125b4 bytes 08c947f9
+ 005125b4 bytes 08f147f9
~~~


<a id="compare-e57e5bdd10727043cfaf7a1d9bab7f0d"></a>

### [`005125e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005125e8.md) → [`005125e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125e8.md) FUN_005125e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00512604",
      "incomplete_value": true,
      "site": "00512608",
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
      "definition_site": "00512604",
      "incomplete_value": true,
      "site": "00512608",
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
      "005125fc",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512608",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005125fc",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512608",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005125fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005125e8.md#insn-005125fc)
- 新版 `005125fc`（命令位置の公開資料なし）

~~~diff
- 005125fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 005125fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005125fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005125fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005125fc bytes 08c947f9
+ 005125fc bytes 08f147f9
~~~


<a id="compare-920c1f3e7931374e58e4600f4388cedf"></a>

### [`00512630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512630.md) → [`00512630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512630.md) FUN_00512630

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "0051264c",
      "incomplete_value": true,
      "site": "00512650",
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
      "definition_site": "0051264c",
      "incomplete_value": true,
      "site": "00512650",
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
      "00512644",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512650",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00512644",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512650",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512630.md#insn-00512644)
- 新版 `00512644`（命令位置の公開資料なし）

~~~diff
- 00512644 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00512644 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512644 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00512644 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512644 bytes 08c947f9
+ 00512644 bytes 08f147f9
~~~


<a id="compare-fc80d3e67bac3127fe477942e1c579e1"></a>

### [`00512678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512678.md) → [`00512678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512678.md) FUN_00512678

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00512694",
      "incomplete_value": true,
      "site": "00512698",
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
      "definition_site": "00512694",
      "incomplete_value": true,
      "site": "00512698",
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
      "0051268c",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512698",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0051268c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512698",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051268c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512678.md#insn-0051268c)
- 新版 `0051268c`（命令位置の公開資料なし）

~~~diff
- 0051268c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 0051268c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051268c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0051268c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051268c bytes 08c947f9
+ 0051268c bytes 08f147f9
~~~


<a id="compare-b38b6b5990bd2dfe5c3eeb66753789d4"></a>

### [`005126c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005126c0.md) → [`005126c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005126c0.md) FUN_005126c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "005126dc",
      "incomplete_value": true,
      "site": "005126e0",
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
      "definition_site": "005126dc",
      "incomplete_value": true,
      "site": "005126e0",
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
      "005126d4",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "005126e0",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005126d4",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005126e0",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005126d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005126c0.md#insn-005126d4)
- 新版 `005126d4`（命令位置の公開資料なし）

~~~diff
- 005126d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 005126d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005126d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005126d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005126d4 bytes 08c947f9
+ 005126d4 bytes 08f147f9
~~~


<a id="compare-e6996305e5e91e89da10e254c8b827e9"></a>

### [`00512708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512708.md) → [`00512708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512708.md) FUN_00512708

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00512724",
      "incomplete_value": true,
      "site": "00512728",
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
      "definition_site": "00512724",
      "incomplete_value": true,
      "site": "00512728",
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
      "0051271c",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512728",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0051271c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512728",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051271c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512708.md#insn-0051271c)
- 新版 `0051271c`（命令位置の公開資料なし）

~~~diff
- 0051271c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 0051271c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051271c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0051271c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051271c bytes 08c947f9
+ 0051271c bytes 08f147f9
~~~


<a id="compare-c0ea34cd66f004d69dd5d4a194945f10"></a>

### [`00512750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512750.md) → [`00512750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512750.md) FUN_00512750

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "0051276c",
      "incomplete_value": true,
      "site": "00512770",
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
      "definition_site": "0051276c",
      "incomplete_value": true,
      "site": "00512770",
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
      "00512764",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512770",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00512764",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512770",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512750.md#insn-00512764)
- 新版 `00512764`（命令位置の公開資料なし）

~~~diff
- 00512764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00512764 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00512764 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512764 bytes 08c947f9
+ 00512764 bytes 08f147f9
~~~


<a id="compare-333637927eda958a2643ee7b22b67210"></a>

### [`00512798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512798.md) → [`00512798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512798.md) FUN_00512798

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "005127b4",
      "incomplete_value": true,
      "site": "005127b8",
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
      "definition_site": "005127b4",
      "incomplete_value": true,
      "site": "005127b8",
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
      "005127ac",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "005127b8",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005127ac",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005127b8",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005127ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512798.md#insn-005127ac)
- 新版 `005127ac`（命令位置の公開資料なし）

~~~diff
- 005127ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 005127ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005127ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005127ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005127ac bytes 08c947f9
+ 005127ac bytes 08f147f9
~~~


<a id="compare-c9e578181aff4cbad0485d12b9aedb10"></a>

### [`005127e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005127e0.md) → [`005127e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005127e0.md) FUN_005127e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "005127fc",
      "incomplete_value": true,
      "site": "00512800",
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
      "definition_site": "005127fc",
      "incomplete_value": true,
      "site": "00512800",
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
      "005127f4",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512800",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005127f4",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512800",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005127f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005127e0.md#insn-005127f4)
- 新版 `005127f4`（命令位置の公開資料なし）

~~~diff
- 005127f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 005127f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005127f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005127f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005127f4 bytes 08c947f9
+ 005127f4 bytes 08f147f9
~~~


<a id="compare-f153eaeca0562e481fc557816c74b2c7"></a>

### [`00512828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512828.md) → [`00512828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512828.md) FUN_00512828

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00512844",
      "incomplete_value": true,
      "site": "00512848",
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
      "definition_site": "00512844",
      "incomplete_value": true,
      "site": "00512848",
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
      "0051283c",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512848",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0051283c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512848",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051283c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512828.md#insn-0051283c)
- 新版 `0051283c`（命令位置の公開資料なし）

~~~diff
- 0051283c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 0051283c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051283c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0051283c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051283c bytes 08c947f9
+ 0051283c bytes 08f147f9
~~~


<a id="compare-1d69bef04d1a9d737b402939e3710094"></a>

### [`00512870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512870.md) → [`00512870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512870.md) FUN_00512870

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "0051288c",
      "incomplete_value": true,
      "site": "00512890",
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
      "definition_site": "0051288c",
      "incomplete_value": true,
      "site": "00512890",
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
      "00512884",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512890",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00512884",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512890",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512870.md#insn-00512884)
- 新版 `00512884`（命令位置の公開資料なし）

~~~diff
- 00512884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00512884 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00512884 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512884 bytes 08c947f9
+ 00512884 bytes 08f147f9
~~~


<a id="compare-1a8ce4bfb04b116635f4a57bafd11226"></a>

### [`005128b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005128b8.md) → [`005128b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005128b8.md) FUN_005128b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "005128d4",
      "incomplete_value": true,
      "site": "005128d8",
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
      "definition_site": "005128d4",
      "incomplete_value": true,
      "site": "005128d8",
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
      "005128cc",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "005128d8",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005128cc",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005128d8",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005128cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005128b8.md#insn-005128cc)
- 新版 `005128cc`（命令位置の公開資料なし）

~~~diff
- 005128cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 005128cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005128cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005128cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005128cc bytes 08c947f9
+ 005128cc bytes 08f147f9
~~~


<a id="compare-a32fd6289a127e5b37a02887401a8205"></a>

### [`00512900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512900.md) → [`00512900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512900.md) FUN_00512900

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "0051291c",
      "incomplete_value": true,
      "site": "00512920",
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
      "definition_site": "0051291c",
      "incomplete_value": true,
      "site": "00512920",
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
      "00512914",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512920",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00512914",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512920",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512900.md#insn-00512914)
- 新版 `00512914`（命令位置の公開資料なし）

~~~diff
- 00512914 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00512914 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512914 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00512914 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512914 bytes 08c947f9
+ 00512914 bytes 08f147f9
~~~


<a id="compare-3f8cbc1f205f205ea140916772482881"></a>

### [`00512948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512948.md) → [`00512948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512948.md) FUN_00512948

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00512964",
      "incomplete_value": true,
      "site": "00512968",
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
      "definition_site": "00512964",
      "incomplete_value": true,
      "site": "00512968",
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
      "0051295c",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512968",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0051295c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512968",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051295c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512948.md#insn-0051295c)
- 新版 `0051295c`（命令位置の公開資料なし）

~~~diff
- 0051295c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 0051295c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051295c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0051295c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051295c bytes 08c947f9
+ 0051295c bytes 08f147f9
~~~


<a id="compare-dc6477d042e1349f48c73ec4eb687617"></a>

### [`005129d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005129d4.md) → [`005129d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005129d4.md) FUN_005129d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "005129f0",
      "incomplete_value": true,
      "site": "005129f4",
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
      "definition_site": "005129f0",
      "incomplete_value": true,
      "site": "005129f4",
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
      "005129e8",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "005129f4",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005129e8",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005129f4",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005129e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/005129d4.md#insn-005129e8)
- 新版 `005129e8`（命令位置の公開資料なし）

~~~diff
- 005129e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 005129e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005129e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005129e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005129e8 bytes 08c947f9
+ 005129e8 bytes 08f147f9
~~~


<a id="compare-cd1fdec32c1d572ae8986a166aa0f5e1"></a>

### [`00512a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512a1c.md) → [`00512a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512a1c.md) FUN_00512a1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00512a38",
      "incomplete_value": true,
      "site": "00512a3c",
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
      "definition_site": "00512a38",
      "incomplete_value": true,
      "site": "00512a3c",
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
      "00512a30",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512a3c",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00512a30",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512a3c",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512a1c.md#insn-00512a30)
- 新版 `00512a30`（命令位置の公開資料なし）

~~~diff
- 00512a30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00512a30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512a30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00512a30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512a30 bytes 08c947f9
+ 00512a30 bytes 08f147f9
~~~


<a id="compare-bd9c649a2e558f0cf171649ba5a3d25f"></a>

### [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) → [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) FUN_00512c94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 35件 [`0047f2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f2d0.md) [`00482154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482154.md) [`00482df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482df4.md) [`00484754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484754.md) [`00484d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484d30.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 35件 [`0047f2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f2d0.md) [`00482154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482154.md) [`00482df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482df4.md) [`00484754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484754.md) [`00484d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484d30.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00512ca0",
      "incomplete_value": false,
      "site": "00512ca4",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00512ca0",
      "incomplete_value": false,
      "site": "00512ca4",
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
            "const:303:8"
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
      "00512ca0",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00512ca0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md#insn-00512ca0)
- 新版 `00512ca0`（命令位置の公開資料なし）

~~~diff
- 00512ca0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00512ca0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00512ca0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00512ca0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00512ca0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00512ca0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00512ca0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00512ca0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00512ca0 bytes 000c0c91
+ 00512ca0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-303292e786dfb003ff14976af478602e"></a>

### [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) → [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) FUN_00512ca8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 32件 [`004826c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004826c4.md) [`00483d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483d44.md) [`00484024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484024.md) [`00485f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485f54.md) [`0049f624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049f624.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 32件 [`004826c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004826c4.md) [`00483d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483d44.md) [`00484024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484024.md) [`00485f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485f54.md) [`0049f624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f624.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00512d10",
      "incomplete_value": true,
      "site": "00512d10",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00512d10",
      "incomplete_value": true,
      "site": "00512d10",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00512d4c",
      "incomplete_value": true,
      "site": "00512d4c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00512d4c",
      "incomplete_value": true,
      "site": "00512d4c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00512d00",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00512d3c",
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
      "00512d00",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00512d3c",
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

- 旧版 [`00512d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md#insn-00512d00) · [`00512d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md#insn-00512d3c)
- 新版 `00512d00`（命令位置の公開資料なし） · `00512d3c`（命令位置の公開資料なし）

~~~diff
- 00512d00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00512d00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512d00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00512d00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00512d00 bytes a99643f9
+ 00512d00 bytes a9be43f9
- 00512d3c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00512d3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512d3c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00512d3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00512d3c bytes a99643f9
+ 00512d3c bytes a9be43f9
~~~


<a id="compare-a1d924696c1eda75935cbb69c4d209f5"></a>

### [`00512d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512d84.md) → [`00512d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512d84.md) FUN_00512d84

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00512da0",
      "incomplete_value": true,
      "site": "00512da4",
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
      "definition_site": "00512da0",
      "incomplete_value": true,
      "site": "00512da4",
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
      "00512d98",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512da4",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00512d98",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512da4",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512d84.md#insn-00512d98)
- 新版 `00512d98`（命令位置の公開資料なし）

~~~diff
- 00512d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00512d98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00512d98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512d98 bytes 08c947f9
+ 00512d98 bytes 08f147f9
~~~


<a id="compare-49b44413bf8a41070d38c77e865e236a"></a>

### [`00512dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512dcc.md) → [`00512dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512dcc.md) FUN_00512dcc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0048cd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cd38.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0b0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 1件 [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb100.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.39% / 新版 92.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512e8c",
      "incomplete_value": true,
      "site": "00512e8c",
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
      "definition_site": "00512e8c",
      "incomplete_value": true,
      "site": "00512e8c",
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00512ed8",
      "incomplete_value": false,
      "site": "00512edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00512ed8",
      "incomplete_value": false,
      "site": "00512edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00512dec",
      "incomplete_value": false,
      "site": "00512e00",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00512dec",
      "incomplete_value": false,
      "site": "00512e00",
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
            "const:c7c:8"
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
      "00512dec",
      "PARAM",
      [
        "storage",
        "002afc7c",
        null,
        "string"
      ]
    ],
    [
      "00512e08",
      "PARAM",
      [
        "storage",
        "002a0342",
        null,
        null
      ]
    ],
    [
      "00512e78",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00512dec",
      "PARAM",
      [
        "storage",
        "002afbe8",
        null,
        "string"
      ]
    ],
    [
      "00512e08",
      "PARAM",
      [
        "storage",
        "002a03cd",
        null,
        null
      ]
    ],
    [
      "00512e78",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512dcc.md#insn-00512dec) · [`00512e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512dcc.md#insn-00512e08) · [`00512e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512dcc.md#insn-00512e78)
- 新版 `00512dec`（命令位置の公開資料なし） · `00512e08`（命令位置の公開資料なし） · `00512e78`（命令位置の公開資料なし）

~~~diff
- 00512dec ["COPY", "tmp:0:8", ["const:c7c:8"]]
- 00512dec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00512dec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00512dec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00512dec ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00512dec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00512dec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00512dec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00512dec bytes 00f03191
+ 00512dec bytes 00a02f91
- 00512e08 ["COPY", "tmp:0:8", ["const:342:8"]]
- 00512e08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00512e08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00512e08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00512e08 ["COPY", "tmp:0:8", ["const:3cd:8"]]
+ 00512e08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00512e08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00512e08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00512e08 bytes 21080d91
+ 00512e08 bytes 21340f91
- 00512e78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00512e78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512e78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00512e78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512e78 bytes 08c947f9
+ 00512e78 bytes 08f147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52023d7eed869d08097122deca48fceb"></a>

### [`00512fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512fd4.md) → [`00512fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512fd4.md) FUN_00512fd4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00512ff0",
      "incomplete_value": true,
      "site": "00512ff4",
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
      "definition_site": "00512ff0",
      "incomplete_value": true,
      "site": "00512ff4",
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
      "00512fe8",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00512ff4",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00512fe8",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00512ff4",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512fd4.md#insn-00512fe8)
- 新版 `00512fe8`（命令位置の公開資料なし）

~~~diff
- 00512fe8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00512fe8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512fe8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00512fe8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512fe8 bytes 08c947f9
+ 00512fe8 bytes 08f147f9
~~~


<a id="compare-b609e9c7991a33413d0f31891c78be0e"></a>

### [`0051301c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051301c.md) → [`0051301c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051301c.md) FUN_0051301c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00513038",
      "incomplete_value": true,
      "site": "0051303c",
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
      "definition_site": "00513038",
      "incomplete_value": true,
      "site": "0051303c",
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
      "00513030",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "0051303c",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00513030",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "0051303c",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00513030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051301c.md#insn-00513030)
- 新版 `00513030`（命令位置の公開資料なし）

~~~diff
- 00513030 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00513030 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00513030 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00513030 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00513030 bytes 08c947f9
+ 00513030 bytes 08f147f9
~~~


<a id="compare-02dd34dcbb991cb871c580dc2418f87c"></a>

### [`0051308c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051308c.md) → [`0051308c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051308c.md) FUN_0051308c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004d5f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d5/004d5f58.md) [`004d6094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6094.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004d5f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5f58.md) [`004d6094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6094.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005130b4",
      "incomplete_value": false,
      "site": "005130c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005130b4",
      "incomplete_value": false,
      "site": "005130c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:380:8"
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
      "definition_site": "005130dc",
      "incomplete_value": false,
      "site": "005130e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005130dc",
      "incomplete_value": false,
      "site": "005130e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005130f8",
      "incomplete_value": false,
      "site": "00513104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005130f8",
      "incomplete_value": false,
      "site": "00513104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:380:8"
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
      "005130a4",
      "READ",
      [
        "storage",
        "00c25390",
        null,
        "undefined1"
      ]
    ],
    [
      "005130b4",
      "PARAM",
      [
        "storage",
        "00c25380",
        null,
        "undefined8"
      ]
    ],
    [
      "005130dc",
      "PARAM",
      [
        "storage",
        "00c25390",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "005130a4",
      "READ",
      [
        "storage",
        "00c253d0",
        null,
        "undefined1"
      ]
    ],
    [
      "005130b4",
      "PARAM",
      [
        "storage",
        "00c253c0",
        null,
        "undefined8"
      ]
    ],
    [
      "005130dc",
      "PARAM",
      [
        "storage",
        "00c253d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051309c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051308c.md#insn-0051309c) · [`005130b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051308c.md#insn-005130b4) · [`005130dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051308c.md#insn-005130dc)
- 新版 `0051309c`（命令位置の公開資料なし） · `005130b4`（命令位置の公開資料なし） · `005130dc`（命令位置の公開資料なし）

~~~diff
- 0051309c ["COPY", "tmp:0:8", ["const:390:8"]]
- 0051309c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0051309c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0051309c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0051309c ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 0051309c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0051309c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0051309c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0051309c bytes 08410e91
+ 0051309c bytes 08410f91
- 005130b4 ["COPY", "tmp:0:8", ["const:380:8"]]
- 005130b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005130b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005130b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005130b4 ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 005130b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005130b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005130b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005130b4 bytes 21000e91
+ 005130b4 bytes 21000f91
- 005130dc ["COPY", "tmp:0:8", ["const:390:8"]]
- 005130dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005130dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005130dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005130dc ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 005130dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005130dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005130dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005130dc bytes 00400e91
+ 005130dc bytes 00400f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a89df6b742e71412b83c5d02751a7550"></a>

### [`00513138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513138.md) → [`00513138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513138.md) FUN_00513138

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004a2edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a2edc.md) [`004bf57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bf/004bf57c.md) [`004c05ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md) · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbee0.md)
- 新版 呼出元 3件 [`004a2edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2edc.md) [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`004c05ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md) · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00513230",
      "incomplete_value": true,
      "site": "0051323c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513230",
      "incomplete_value": true,
      "site": "0051323c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
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
      "00513230",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "00513230",
      "PARAM",
      [
        "storage",
        "00be9e18",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00513230",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      "00513230",
      "PARAM",
      [
        "storage",
        "00be9e68",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00513224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513138.md#insn-00513224) · [`00513230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513138.md#insn-00513230)
- 新版 `00513224`（命令位置の公開資料なし） · `00513230`（命令位置の公開資料なし）

~~~diff
- 00513224 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 00513224 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 00513224 bytes 213800f0
+ 00513224 bytes 41380090
- 00513230 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
- 00513230 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00513230 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:48:8"]]
+ 00513230 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00513230 bytes 21fc47f9
+ 00513230 bytes 212440f9
~~~


<a id="compare-1fcc7b7ae9910a96c61c7255240c0610"></a>

### [`0051328c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051328c.md) → [`0051328c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051328c.md) FUN_0051328c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "005132a8",
      "incomplete_value": true,
      "site": "005132ac",
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
      "definition_site": "005132a8",
      "incomplete_value": true,
      "site": "005132ac",
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
      "005132a0",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "005132ac",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "005132a0",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005132ac",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005132a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051328c.md#insn-005132a0)
- 新版 `005132a0`（命令位置の公開資料なし）

~~~diff
- 005132a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 005132a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005132a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 005132a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005132a0 bytes 08c947f9
+ 005132a0 bytes 08f147f9
~~~


<a id="compare-09ad944afa34bf4c573a2d814471b4fd"></a>

### [`005132d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005132d4.md) → [`005132d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) FUN_005132d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004ababc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ab/004ababc.md) [`004d2b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2b8c.md) [`004d3aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d3/004d3aec.md) [`004d3ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d3/004d3ba0.md) · 呼出先 8件 [`0051345c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051345c.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 4件 [`004ababc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ababc.md) [`004d2b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2b8c.md) [`004d3aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3aec.md) [`004d3ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3ba0.md) · 呼出先 8件 [`0051345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051345c.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005133c8",
      "incomplete_value": true,
      "site": "005133d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005133c8",
      "incomplete_value": true,
      "site": "005133d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa8:8"
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
      "definition_site": "005133cc",
      "incomplete_value": true,
      "site": "005133d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:c1b000:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005133cc",
      "incomplete_value": true,
      "site": "005133d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "005133c8",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "005133c8",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005133cc",
      "READ",
      [
        "storage",
        "00c1afb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005133c8",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "005133c8",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005133cc",
      "READ",
      [
        "storage",
        "00c1b000",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005133c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005132d4.md#insn-005133c0) · [`005133c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005132d4.md#insn-005133c8) · [`005133cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005132d4.md#insn-005133cc)
- 新版 `005133c0`（命令位置の公開資料なし） · `005133c8`（命令位置の公開資料なし） · `005133cc`（命令位置の公開資料なし）

~~~diff
- 005133c0 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 005133c0 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 005133c0 bytes 223800f0
+ 005133c0 bytes 42380090
- 005133c8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
- 005133c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005133c8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 005133c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005133c8 bytes 21d447f9
+ 005133c8 bytes 21fc47f9
- 005133cc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:fb0:8"]]
- 005133cc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005133cc ["COPY", "tmp:0:8", ["register:4010:8"]]
+ 005133cc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005133cc bytes 42d847f9
+ 005133cc bytes 420040f9
~~~


<a id="compare-63d5563ebb39ba1893018ba57585f780"></a>

### [`0051345c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051345c.md) → [`0051345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051345c.md) FUN_0051345c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00495978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495978.md) [`005132d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005132d4.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520804.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 4件 [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`005132d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00513468",
      "incomplete_value": false,
      "site": "0051346c",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513468",
      "incomplete_value": false,
      "site": "0051346c",
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
            "const:303:8"
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
      "00513468",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00513468",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00513468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051345c.md#insn-00513468)
- 新版 `00513468`（命令位置の公開資料なし）

~~~diff
- 00513468 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00513468 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00513468 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00513468 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00513468 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00513468 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00513468 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00513468 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00513468 bytes 000c0c91
+ 00513468 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bab283525c4e49b2f0b4614c5bdd0190"></a>

### [`005137dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005137dc.md) → [`005137dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005137dc.md) FUN_005137dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`004bf57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bf/004bf57c.md) [`00518128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/00518128.md) [`00526bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00526/00526bb4.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 3件 [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`00518128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518128.md) [`00526bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526bb4.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00513824",
      "incomplete_value": true,
      "site": "00513824",
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
      "definition_site": "00513824",
      "incomplete_value": true,
      "site": "00513824",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00513824",
      "incomplete_value": true,
      "site": "00513824",
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
      "definition_site": "00513824",
      "incomplete_value": true,
      "site": "00513824",
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
      "00513804",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "00513810",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "00513824",
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
      "00513804",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "00513810",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "00513824",
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

- 旧版 [`00513804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005137dc.md#insn-00513804) · [`0051380c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/005137dc.md#insn-0051380c)
- 新版 `00513804`（命令位置の公開資料なし） · `0051380c`（命令位置の公開資料なし）

~~~diff
- 00513804 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
- 00513804 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00513804 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 00513804 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00513804 bytes 087d47f9
+ 00513804 bytes 08a547f9
- 0051380c ["COPY", "register:4098:8", ["register:4000:8"]]
- 0051380c bytes f30300aa
+ 0051380c ["COPY", "register:4098:8", ["register:4000:8"]]
+ 0051380c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f1dc4155cb7e3e7505afa056c852744"></a>

### [`00513904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513904.md) → [`00513904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513904.md) FUN_00513904

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd0e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00513950",
      "incomplete_value": true,
      "site": "00513950",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513950",
      "incomplete_value": true,
      "site": "00513950",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:847:8"
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
      "definition_site": "00513940",
      "incomplete_value": true,
      "site": "00513954",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00513940",
      "incomplete_value": true,
      "site": "00513954",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0051397c",
      "incomplete_value": true,
      "site": "00513988",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:400:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051397c",
      "incomplete_value": true,
      "site": "00513988",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
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
      "00513938",
      "READ",
      [
        "storage",
        "002a6847",
        null,
        "string"
      ]
    ],
    [
      "00513940",
      "READ",
      [
        "storage",
        "002a684e",
        null,
        "string"
      ]
    ],
    [
      "0051397c",
      "READ",
      [
        "storage",
        "00c1b3b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00513938",
      "READ",
      [
        "storage",
        "002a68e1",
        null,
        "string"
      ]
    ],
    [
      "00513940",
      "READ",
      [
        "storage",
        "002a68e8",
        null,
        "string"
      ]
    ],
    [
      "0051397c",
      "READ",
      [
        "storage",
        "00c1b400",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00513934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513904.md#insn-00513934) · [`0051397c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513904.md#insn-0051397c)
- 新版 `00513934`（命令位置の公開資料なし） · `0051397c`（命令位置の公開資料なし）

~~~diff
- 00513934 ["COPY", "tmp:0:8", ["const:847:8"]]
- 00513934 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00513934 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00513934 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00513934 ["COPY", "tmp:0:8", ["const:8e1:8"]]
+ 00513934 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00513934 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00513934 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00513934 bytes 291d2191
+ 00513934 bytes 29852391
- 0051397c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:3b0:8"]]
- 0051397c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051397c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:400:8"]]
+ 0051397c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0051397c bytes 21d841f9
+ 0051397c bytes 210042f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4779edae1c556c0f85a15d68e161106a"></a>

### [`00513b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513b50.md) → [`00513b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513b50.md) FUN_00513b50

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`00522aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00522/00522aa0.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8e0.md)
- 新版 呼出元 2件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522aa0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00513bb4",
      "incomplete_value": true,
      "site": "00513bb8",
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
      "definition_site": "00513bb4",
      "incomplete_value": true,
      "site": "00513bb8",
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
      "definition_site": "00513bd4",
      "incomplete_value": true,
      "site": "00513bd8",
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
      "definition_site": "00513bd4",
      "incomplete_value": true,
      "site": "00513bd8",
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
      "definition_site": "00513bf0",
      "incomplete_value": true,
      "site": "00513bf4",
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
      "definition_site": "00513bf0",
      "incomplete_value": true,
      "site": "00513bf4",
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
      "00513b98",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ],
    [
      "00513bac",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ],
    [
      "00513bb8",
      "DATA",
      [
        "storage",
        "00bea440",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00513b98",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "00513bac",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ],
    [
      "00513bb8",
      "DATA",
      [
        "storage",
        "00bea490",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00513b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513b50.md#insn-00513b98) · [`00513bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513b50.md#insn-00513bac) · [`00513bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513b50.md#insn-00513bcc)
- 新版 `00513b98`（命令位置の公開資料なし） · `00513bac`（命令位置の公開資料なし） · `00513bcc`（命令位置の公開資料なし）

~~~diff
- 00513b98 ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 00513b98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00513b98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00513b98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00513b98 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 00513b98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00513b98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00513b98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00513b98 bytes 21282391
+ 00513b98 bytes 21f42091
- 00513bac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 00513bac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00513bac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 00513bac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00513bac bytes 089147f9
+ 00513bac bytes 08b947f9
- 00513bcc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f28:8"]]
- 00513bcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00513bcc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f78:8"]]
+ 00513bcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00513bcc bytes 089547f9
+ 00513bcc bytes 08bd47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6625c5ed7bda311da0ea4d32d31ba7e"></a>

### [`00513c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513c60.md) → [`00513c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513c60.md) FUN_00513c60

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md) [`00bdbb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb80.md) [`00bdbbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbbe0.md)
- 新版 呼出元 1件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) [`00bdbbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbd0.md) [`00bdbc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc30.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00513d20",
      "incomplete_value": true,
      "site": "00513d20",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513d20",
      "incomplete_value": true,
      "site": "00513d20",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00513d64",
      "incomplete_value": true,
      "site": "00513d64",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513d64",
      "incomplete_value": true,
      "site": "00513d64",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00513d10",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00513d54",
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
      "00513d10",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00513d54",
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

- 旧版 [`00513d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513c60.md#insn-00513d10) · [`00513d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513c60.md#insn-00513d54)
- 新版 `00513d10`（命令位置の公開資料なし） · `00513d54`（命令位置の公開資料なし）

~~~diff
- 00513d10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00513d10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00513d10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 00513d10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00513d10 bytes 899643f9
+ 00513d10 bytes 89be43f9
- 00513d54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00513d54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00513d54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 00513d54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00513d54 bytes 899643f9
+ 00513d54 bytes 89be43f9
~~~


<a id="compare-d5e4632432535b41e9595bb11d48ecee"></a>

### [`00513de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513de4.md) → [`00513de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513de4.md) FUN_00513de4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)

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
      "definition_site": "00513e00",
      "incomplete_value": true,
      "site": "00513e04",
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
      "definition_site": "00513e00",
      "incomplete_value": true,
      "site": "00513e04",
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
      "00513df8",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "00513e04",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00513df8",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00513e04",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00513df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513de4.md#insn-00513df8)
- 新版 `00513df8`（命令位置の公開資料なし）

~~~diff
- 00513df8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 00513df8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00513df8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 00513df8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00513df8 bytes 08c947f9
+ 00513df8 bytes 08f147f9
~~~


<a id="compare-80f2ce5a72c8b0793381d10dd46500cb"></a>

### [`00513e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513e2c.md) → [`00513e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513e2c.md) FUN_00513e2c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004ce6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce6fc.md) [`004ec0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec0b4.md) · 呼出先 8件 [`00513fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513fb0.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 2件 [`004ce6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce6fc.md) [`004ec0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec0b4.md) · 呼出先 8件 [`00513fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513fb0.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00513f1c",
      "incomplete_value": true,
      "site": "00513f24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513f1c",
      "incomplete_value": true,
      "site": "00513f24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa8:8"
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
      "definition_site": "00513f20",
      "incomplete_value": true,
      "site": "00513f24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:c1b000:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513f20",
      "incomplete_value": true,
      "site": "00513f24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
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
      "00513f1c",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "00513f1c",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00513f20",
      "READ",
      [
        "storage",
        "00c1afb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00513f1c",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "00513f1c",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00513f20",
      "READ",
      [
        "storage",
        "00c1b000",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00513f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513e2c.md#insn-00513f14) · [`00513f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513e2c.md#insn-00513f1c) · [`00513f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513e2c.md#insn-00513f20)
- 新版 `00513f14`（命令位置の公開資料なし） · `00513f1c`（命令位置の公開資料なし） · `00513f20`（命令位置の公開資料なし）

~~~diff
- 00513f14 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 00513f14 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 00513f14 bytes 223800f0
+ 00513f14 bytes 42380090
- 00513f1c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
- 00513f1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00513f1c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 00513f1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00513f1c bytes 21d447f9
+ 00513f1c bytes 21fc47f9
- 00513f20 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:fb0:8"]]
- 00513f20 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00513f20 ["COPY", "tmp:0:8", ["register:4010:8"]]
+ 00513f20 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00513f20 bytes 42d847f9
+ 00513f20 bytes 420040f9
~~~


<a id="compare-b8d85371e1e79ff5ffa001fa62034084"></a>

### [`00513fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513fb0.md) → [`00513fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513fb0.md) FUN_00513fb0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 12件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00513e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513e2c.md) [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md) [`0051d4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d4f0.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 12件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00513e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513e2c.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00513fbc",
      "incomplete_value": false,
      "site": "00513fc0",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513fbc",
      "incomplete_value": false,
      "site": "00513fc0",
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
            "const:303:8"
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
      "00513fbc",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00513fbc",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00513fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513fb0.md#insn-00513fbc)
- 新版 `00513fbc`（命令位置の公開資料なし）

~~~diff
- 00513fbc ["COPY", "tmp:0:8", ["const:303:8"]]
- 00513fbc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00513fbc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00513fbc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00513fbc ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00513fbc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00513fbc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00513fbc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00513fbc bytes 000c0c91
+ 00513fbc bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a494f151f9700ec9d121b2ac4a6ac7af"></a>

### [`00513fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513fc4.md) → [`00513fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513fc4.md) FUN_00513fc4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005141ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/005141ac.md) [`00514680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514680.md) · 呼出先 9件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 2件 [`005141ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/005141ac.md) [`00514680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514680.md) · 呼出先 9件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0051404c",
      "incomplete_value": false,
      "site": "00514054",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051404c",
      "incomplete_value": false,
      "site": "00514054",
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
            "const:bfd:8"
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
      "definition_site": "00514084",
      "incomplete_value": true,
      "site": "00514090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00514084",
      "incomplete_value": true,
      "site": "00514090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0051404c",
      "PARAM",
      [
        "storage",
        "00296bfd",
        null,
        "string"
      ]
    ],
    [
      "00514084",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00514084",
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
      "0051404c",
      "PARAM",
      [
        "storage",
        "00296b70",
        null,
        "string"
      ]
    ],
    [
      "00514084",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "00514084",
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

- 旧版 [`0051404c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513fc4.md#insn-0051404c) · [`00514084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513fc4.md#insn-00514084)
- 新版 `0051404c`（命令位置の公開資料なし） · `00514084`（命令位置の公開資料なし）

~~~diff
- 0051404c ["COPY", "tmp:0:8", ["const:bfd:8"]]
- 0051404c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0051404c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0051404c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0051404c ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 0051404c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0051404c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0051404c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0051404c bytes 21f42f91
+ 0051404c bytes 21c02d91
- 00514084 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 00514084 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00514084 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 00514084 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00514084 bytes 217847f9
+ 00514084 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-133a691ee472869952a5e4da24ab0e21"></a>

### [`005140e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/005140e0.md) → [`005140e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/005140e0.md) FUN_005140e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514100",
      "incomplete_value": true,
      "site": "00514100",
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
      "definition_site": "00514100",
      "incomplete_value": true,
      "site": "00514100",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00514120",
      "incomplete_value": false,
      "site": "00514120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514120",
      "incomplete_value": false,
      "site": "00514120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "005140f4",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "00514100",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00514120",
      "DATA",
      [
        "storage",
        "00be9f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005140f4",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00514100",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00514120",
      "DATA",
      [
        "storage",
        "00be9f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005140f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/005140e0.md#insn-005140f4) · [`0051411c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/005140e0.md#insn-0051411c)
- 新版 `005140f4`（命令位置の公開資料なし） · `0051411c`（命令位置の公開資料なし）

~~~diff
- 005140f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 005140f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005140f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 005140f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005140f4 bytes 08b940f9
+ 005140f4 bytes 08e140f9
- 0051411c ["COPY", "tmp:0:8", ["const:f08:8"]]
- 0051411c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0051411c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0051411c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0051411c ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 0051411c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0051411c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0051411c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0051411c bytes 08213c91
+ 0051411c bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-804f7e17b11b52a5c7df99052ad7176f"></a>

### [`00514148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514148.md) → [`00514148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514148.md) FUN_00514148

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514168",
      "incomplete_value": true,
      "site": "00514168",
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
      "definition_site": "00514168",
      "incomplete_value": true,
      "site": "00514168",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00514188",
      "incomplete_value": false,
      "site": "00514188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514188",
      "incomplete_value": false,
      "site": "00514188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "0051415c",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "00514168",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00514188",
      "DATA",
      [
        "storage",
        "00be9f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0051415c",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00514168",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00514188",
      "DATA",
      [
        "storage",
        "00be9f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051415c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514148.md#insn-0051415c) · [`00514184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514148.md#insn-00514184)
- 新版 `0051415c`（命令位置の公開資料なし） · `00514184`（命令位置の公開資料なし）

~~~diff
- 0051415c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 0051415c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051415c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 0051415c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051415c bytes 08b940f9
+ 0051415c bytes 08e140f9
- 00514184 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00514184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00514184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00514184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00514184 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00514184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00514184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00514184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00514184 bytes 08213c91
+ 00514184 bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68680a176965ab82758269df594a0999"></a>

### [`005141ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/005141ac.md) → [`005141ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/005141ac.md) FUN_005141ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00513fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513fc4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00513fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513fc4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.65% / 新版 94.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00514224",
      "incomplete_value": true,
      "site": "00514224",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "definition_site": "00514224",
      "incomplete_value": true,
      "site": "00514224",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "definition_site": "00514308",
      "incomplete_value": true,
      "site": "00514308",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "definition_site": "00514308",
      "incomplete_value": true,
      "site": "00514308",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005143f4",
      "incomplete_value": true,
      "site": "005143f4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "definition_site": "005143f4",
      "incomplete_value": true,
      "site": "005143f4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "00514214",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "005142f8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "005143e4",
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
      "00514214",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "005142f8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "005143e4",
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

- 旧版 [`00514214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/005141ac.md#insn-00514214) · [`005142f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/005141ac.md#insn-005142f8) · [`005143e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/005141ac.md#insn-005143e4)
- 新版 `00514214`（命令位置の公開資料なし） · `005142f8`（命令位置の公開資料なし） · `005143e4`（命令位置の公開資料なし）

~~~diff
- 00514214 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 00514214 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00514214 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 00514214 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00514214 bytes 099743f9
+ 00514214 bytes 09bf43f9
- 005142f8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 005142f8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005142f8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 005142f8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005142f8 bytes 099743f9
+ 005142f8 bytes 09bf43f9
- 005143e4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 005143e4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005143e4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 005143e4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005143e4 bytes 099743f9
+ 005143e4 bytes 09bf43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6963ff3de13e46c4fa66e66a1a1ec35"></a>

### [`00514504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514504.md) → [`00514504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514504.md) FUN_00514504

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514524",
      "incomplete_value": true,
      "site": "00514524",
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
      "definition_site": "00514524",
      "incomplete_value": true,
      "site": "00514524",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00514540",
      "incomplete_value": false,
      "site": "00514544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514540",
      "incomplete_value": false,
      "site": "00514544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "00514518",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "00514524",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00514544",
      "DATA",
      [
        "storage",
        "00be9ea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00514518",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00514524",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00514544",
      "DATA",
      [
        "storage",
        "00be9ef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514504.md#insn-00514518) · [`00514540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514504.md#insn-00514540)
- 新版 `00514518`（命令位置の公開資料なし） · `00514540`（命令位置の公開資料なし）

~~~diff
- 00514518 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 00514518 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00514518 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 00514518 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00514518 bytes 08b940f9
+ 00514518 bytes 08e140f9
- 00514540 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 00514540 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00514540 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00514540 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00514540 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 00514540 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00514540 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00514540 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00514540 bytes 29a13a91
+ 00514540 bytes 29e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe870d6dd3abf7fe0c7b73ffa56e1bf9"></a>

### [`00514580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514580.md) → [`00514580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514580.md) FUN_00514580

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005145a0",
      "incomplete_value": true,
      "site": "005145a0",
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
      "definition_site": "005145a0",
      "incomplete_value": true,
      "site": "005145a0",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005145bc",
      "incomplete_value": false,
      "site": "005145c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005145bc",
      "incomplete_value": false,
      "site": "005145c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "00514594",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "005145a0",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "005145c0",
      "DATA",
      [
        "storage",
        "00be9ea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00514594",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "005145a0",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "005145c0",
      "DATA",
      [
        "storage",
        "00be9ef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514580.md#insn-00514594) · [`005145bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514580.md#insn-005145bc)
- 新版 `00514594`（命令位置の公開資料なし） · `005145bc`（命令位置の公開資料なし）

~~~diff
- 00514594 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 00514594 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00514594 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 00514594 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00514594 bytes 08b940f9
+ 00514594 bytes 08e140f9
- 005145bc ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 005145bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005145bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005145bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005145bc ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 005145bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005145bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005145bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005145bc bytes 29a13a91
+ 005145bc bytes 29e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9c02abe7637564797e98f12dedbfe63"></a>

### [`00514680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514680.md) → [`00514680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514680.md) FUN_00514680

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00513fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513fc4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00513fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513fc4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbae0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00514790",
      "incomplete_value": true,
      "site": "00514790",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514790",
      "incomplete_value": true,
      "site": "00514790",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005147bc",
      "incomplete_value": true,
      "site": "005147bc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005147bc",
      "incomplete_value": true,
      "site": "005147bc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00514780",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "005147ac",
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
      "00514780",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "005147ac",
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

- 旧版 [`00514780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514680.md#insn-00514780) · [`005147ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514680.md#insn-005147ac)
- 新版 `00514780`（命令位置の公開資料なし） · `005147ac`（命令位置の公開資料なし）

~~~diff
- 00514780 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00514780 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00514780 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 00514780 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00514780 bytes 899643f9
+ 00514780 bytes 89be43f9
- 005147ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 005147ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005147ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 005147ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005147ac bytes 899643f9
+ 005147ac bytes 89be43f9
~~~


<a id="compare-d53ac179bf09cdbd2d9a64ec768bffd8"></a>

### [`0051483c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/0051483c.md) → [`0051483c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/0051483c.md) FUN_0051483c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`004d2830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d2830.md) [`004d29f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d2/004d29f8.md) · 呼出先 8件 [`00514ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514ae0.md) [`00514ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514ae4.md) [`00514b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514b90.md) [`00514b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514b94.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`004d2830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2830.md) [`004d29f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d29f8.md) · 呼出先 8件 [`00514ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514ae0.md) [`00514ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514ae4.md) [`00514b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514b90.md) [`00514b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514b94.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005148d0",
      "incomplete_value": false,
      "site": "005148d0",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005148d0",
      "incomplete_value": false,
      "site": "005148d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "definition_site": "005148f0",
      "incomplete_value": false,
      "site": "005148f0",
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
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005148f0",
      "incomplete_value": false,
      "site": "005148f0",
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
            "const:78:8"
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
      "005148d0",
      "DATA",
      [
        "storage",
        "00becfe8",
        null,
        "undefined *"
      ]
    ],
    [
      "005148f0",
      "DATA",
      [
        "storage",
        "00bed078",
        null,
        "undefined *"
      ]
    ],
    [
      "00514928",
      "READ",
      [
        "storage",
        "00bed098",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005148d0",
      "DATA",
      [
        "storage",
        "00bed038",
        null,
        "undefined *"
      ]
    ],
    [
      "005148f0",
      "DATA",
      [
        "storage",
        "00bed0c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00514928",
      "READ",
      [
        "storage",
        "00bed0e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005148c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/0051483c.md#insn-005148c4) · [`005148c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/0051483c.md#insn-005148c8) · [`005148e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/0051483c.md#insn-005148e8)
- 新版 `005148c4`（命令位置の公開資料なし） · `005148c8`（命令位置の公開資料なし） · `005148e8`（命令位置の公開資料なし）

~~~diff
- 005148c4 ["COPY", "register:4040:8", ["const:bec000:8"]]
+ 005148c4 ["COPY", "register:4040:8", ["const:bed000:8"]]
- 005148c4 bytes c8360090
+ 005148c4 bytes c83600b0
- 005148c8 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 005148c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005148c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005148c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005148c8 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 005148c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005148c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005148c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005148c8 bytes 08a13f91
+ 005148c8 bytes 08e10091
- 005148e8 ["COPY", "tmp:0:8", ["const:78:8"]]
- 005148e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005148e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005148e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005148e8 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 005148e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005148e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005148e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005148e8 bytes 08e10191
+ 005148e8 bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3dd6120d65723223a5e27980b7af294"></a>

### [`00514a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514a98.md) → [`00514a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514a98.md) FUN_00514a98

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00514abc",
      "incomplete_value": false,
      "site": "00514abc",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514abc",
      "incomplete_value": false,
      "site": "00514abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
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
      "00514abc",
      "DATA",
      [
        "storage",
        "00becfe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00514abc",
      "DATA",
      [
        "storage",
        "00bed038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514a98.md#insn-00514ab4) · [`00514ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514a98.md#insn-00514ab8)
- 新版 `00514ab4`（命令位置の公開資料なし） · `00514ab8`（命令位置の公開資料なし）

~~~diff
- 00514ab4 ["COPY", "register:4040:8", ["const:bec000:8"]]
+ 00514ab4 ["COPY", "register:4040:8", ["const:bed000:8"]]
- 00514ab4 bytes c8360090
+ 00514ab4 bytes c83600b0
- 00514ab8 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00514ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00514ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00514ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00514ab8 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00514ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00514ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00514ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00514ab8 bytes 08a13f91
+ 00514ab8 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e97f170ca044cd5dcb505021a796808d"></a>

### [`00514acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514acc.md) → [`00514acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514acc.md) FUN_00514acc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00514ad8",
      "incomplete_value": false,
      "site": "00514ad8",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514ad8",
      "incomplete_value": false,
      "site": "00514ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
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
      "00514ad8",
      "DATA",
      [
        "storage",
        "00becfe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00514ad8",
      "DATA",
      [
        "storage",
        "00bed038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514acc.md#insn-00514ad0) · [`00514ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514acc.md#insn-00514ad4)
- 新版 `00514ad0`（命令位置の公開資料なし） · `00514ad4`（命令位置の公開資料なし）

~~~diff
- 00514ad0 ["COPY", "register:4048:8", ["const:bec000:8"]]
+ 00514ad0 ["COPY", "register:4048:8", ["const:bed000:8"]]
- 00514ad0 bytes c9360090
+ 00514ad0 bytes c93600b0
- 00514ad4 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00514ad4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00514ad4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00514ad4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00514ad4 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00514ad4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00514ad4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00514ad4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00514ad4 bytes 29a13f91
+ 00514ad4 bytes 29e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eab29819eacd817e38bbddb5a5ce71e2"></a>

### [`00514b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514b48.md) → [`00514b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514b48.md) FUN_00514b48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00514b6c",
      "incomplete_value": false,
      "site": "00514b6c",
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
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514b6c",
      "incomplete_value": false,
      "site": "00514b6c",
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
            "const:78:8"
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
      "00514b6c",
      "DATA",
      [
        "storage",
        "00bed078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00514b6c",
      "DATA",
      [
        "storage",
        "00bed0c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514b48.md#insn-00514b68)
- 新版 `00514b68`（命令位置の公開資料なし）

~~~diff
- 00514b68 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00514b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00514b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00514b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00514b68 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00514b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00514b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00514b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00514b68 bytes 08e10191
+ 00514b68 bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be5ee24c24baa85965c4eb41ea4f9aaa"></a>

### [`00514b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514b7c.md) → [`00514b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514b7c.md) FUN_00514b7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00514b88",
      "incomplete_value": false,
      "site": "00514b88",
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
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514b88",
      "incomplete_value": false,
      "site": "00514b88",
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
            "const:78:8"
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
      "00514b88",
      "DATA",
      [
        "storage",
        "00bed078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00514b88",
      "DATA",
      [
        "storage",
        "00bed0c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514b7c.md#insn-00514b84)
- 新版 `00514b84`（命令位置の公開資料なし）

~~~diff
- 00514b84 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00514b84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00514b84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00514b84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00514b84 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00514b84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00514b84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00514b84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00514b84 bytes 29e10191
+ 00514b84 bytes 29210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aeb15b6e6db37e886724a45b02a78620"></a>

### [`00514bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514bd4.md) → [`00514bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514bd4.md) FUN_00514bd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005162fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005162fc.md) [`005163b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005163b4.md) [`005166c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005166c8.md) [`00516794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/00516794.md) · 呼出先 3件 [`004bb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb810.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 4件 [`005162fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005162fc.md) [`005163b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005163b4.md) [`005166c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005166c8.md) [`00516794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/00516794.md) · 呼出先 3件 [`004bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.98% / 新版 92.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00514c0c",
      "incomplete_value": true,
      "site": "00514c0c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00514c0c",
      "incomplete_value": true,
      "site": "00514c0c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00514c38",
      "incomplete_value": true,
      "site": "00514c38",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00514c38",
      "incomplete_value": true,
      "site": "00514c38",
      "value": [
        "LOAD",
        "8",
        [
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
      "00514bfc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00514c28",
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
      "00514bfc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00514c28",
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

- 旧版 [`00514bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514bd4.md#insn-00514bfc) · [`00514c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514bd4.md#insn-00514c28)
- 新版 `00514bfc`（命令位置の公開資料なし） · `00514c28`（命令位置の公開資料なし）

~~~diff
- 00514bfc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00514bfc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00514bfc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00514bfc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00514bfc bytes a99643f9
+ 00514bfc bytes a9be43f9
- 00514c28 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00514c28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00514c28 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00514c28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00514c28 bytes a99643f9
+ 00514c28 bytes a9be43f9
~~~


<a id="compare-37aeea631dfadfc6aa000c58e245b096"></a>

### [`00514cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514cc0.md) → [`00514cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514cc0.md) FUN_00514cc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00516464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/00516464.md) [`005168d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005168d8.md) · 呼出先 19件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`005150ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005150ac.md) [`005161d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005161d4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 2件 [`00516464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/00516464.md) [`005168d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005168d8.md) · 呼出先 19件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`005150ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/005150ac.md) [`005161d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005161d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00514dec",
      "incomplete_value": true,
      "site": "00514dec",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00514dec",
      "incomplete_value": true,
      "site": "00514dec",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00514e18",
      "incomplete_value": true,
      "site": "00514e18",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00514e18",
      "incomplete_value": true,
      "site": "00514e18",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00514e58",
      "incomplete_value": true,
      "site": "00514e58",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00514e58",
      "incomplete_value": true,
      "site": "00514e58",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 15,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00514de0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00514e08",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00514e48",
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
      "00514de0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00514e08",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00514e48",
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

- 旧版 [`00514de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514cc0.md#insn-00514de0) · [`00514de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514cc0.md#insn-00514de4)
- 新版 `00514de0`（命令位置の公開資料なし） · `00514de4`（命令位置の公開資料なし）

~~~diff
- 00514de0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 00514de0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00514de0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 00514de0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00514de0 bytes e99643f9
+ 00514de0 bytes e9be43f9
- 00514de4 ["COPY", "register:4000:8", ["register:40a8:8"]]
- 00514de4 bytes e00315aa
+ 00514de4 ["COPY", "register:4000:8", ["register:40a8:8"]]
+ 00514de4 bytes e00315aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ce818254433dd8fa8b1545a63758088"></a>

### [`005150ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005150ac.md) → [`005150ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/005150ac.md) FUN_005150ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00514cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514cc0.md) · 呼出先 6件 [`00515468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515468.md) [`00515718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515718.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdbca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbca0.md)
- 新版 呼出元 1件 [`00514cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514cc0.md) · 呼出先 6件 [`00515468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515468.md) [`00515718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515718.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.74% / 新版 97.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `call_target` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051512c",
      "incomplete_value": true,
      "site": "0051512c",
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
      "definition_site": "0051512c",
      "incomplete_value": true,
      "site": "0051512c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00515174",
      "incomplete_value": true,
      "site": "0051517c",
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
      "definition_site": "00515174",
      "incomplete_value": true,
      "site": "0051517c",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005152c8",
      "incomplete_value": true,
      "site": "005152c8",
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
      "definition_site": "005152c8",
      "incomplete_value": true,
      "site": "005152c8",
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
      "00515124",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "0051512c",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00515164",
      "READ",
      [
        "storage",
        "00c1b178",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00515124",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "0051512c",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00515164",
      "READ",
      [
        "storage",
        "00c1b1c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00515124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005150ac.md#insn-00515124) · [`00515164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005150ac.md#insn-00515164) · [`005151b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005150ac.md#insn-005151b8)
- 新版 `00515124`（命令位置の公開資料なし） · `00515164`（命令位置の公開資料なし） · `005151b8`（命令位置の公開資料なし）

~~~diff
- 00515124 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:170:8"]]
- 00515124 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00515124 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:1c0:8"]]
+ 00515124 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00515124 bytes 18bb40f9
+ 00515124 bytes 18e340f9
- 00515164 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:178:8"]]
- 00515164 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00515164 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c8:8"]]
+ 00515164 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00515164 bytes 08bd40f9
+ 00515164 bytes 08e540f9
- 005151b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 005151b8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005151b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 005151b8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005151b8 bytes 899643f9
+ 005151b8 bytes 89be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-686e31df9d26a6ee70cfe6bb2f63c79f"></a>

### [`00515468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515468.md) → [`00515468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515468.md) FUN_00515468

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005150ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005150ac.md) · 呼出先 11件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`005158d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005158d4.md) [`00515b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515b48.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`005150ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/005150ac.md) · 呼出先 11件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`005158d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/005158d4.md) [`00515b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515b48.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.38% / 新版 92.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005154ac",
      "incomplete_value": false,
      "site": "005154d4",
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
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005154ac",
      "incomplete_value": false,
      "site": "005154d4",
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
            "const:f8:8"
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
      "definition_site": "005154e0",
      "incomplete_value": true,
      "site": "005154e0",
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
      "definition_site": "005154e0",
      "incomplete_value": true,
      "site": "005154e0",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00515528",
      "incomplete_value": true,
      "site": "00515530",
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
      "definition_site": "00515528",
      "incomplete_value": true,
      "site": "00515530",
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
      "005154cc",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "005154d4",
      "DATA",
      [
        "storage",
        "00bed0f8",
        null,
        "pointer"
      ]
    ],
    [
      "005154e0",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "005154cc",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "005154d4",
      "DATA",
      [
        "storage",
        "00bed148",
        null,
        "pointer"
      ]
    ],
    [
      "005154e0",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005154ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515468.md#insn-005154ac) · [`005154cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515468.md#insn-005154cc) · [`00515518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515468.md#insn-00515518)
- 新版 `005154ac`（命令位置の公開資料なし） · `005154cc`（命令位置の公開資料なし） · `00515518`（命令位置の公開資料なし）

~~~diff
- 005154ac ["COPY", "tmp:0:8", ["const:f8:8"]]
- 005154ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005154ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005154ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005154ac ["COPY", "tmp:0:8", ["const:148:8"]]
+ 005154ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005154ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005154ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005154ac bytes 29e10391
+ 005154ac bytes 29210591
- 005154cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 005154cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005154cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 005154cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005154cc bytes 08b940f9
+ 005154cc bytes 08e140f9
- 00515518 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:178:8"]]
- 00515518 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00515518 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1c8:8"]]
+ 00515518 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00515518 bytes 29bd40f9
+ 00515518 bytes 29e540f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12b26bbda354a2f70f38a945714eea3b"></a>

### [`00515718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515718.md) → [`00515718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515718.md) FUN_00515718

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005150ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005150ac.md) · 呼出先 7件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00515cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515cc4.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`005150ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/005150ac.md) · 呼出先 7件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00515cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515cc4.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.36% / 新版 90.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00515748",
      "incomplete_value": false,
      "site": "00515770",
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
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00515748",
      "incomplete_value": false,
      "site": "00515770",
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
            "const:158:8"
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
      "definition_site": "0051577c",
      "incomplete_value": true,
      "site": "0051577c",
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
      "definition_site": "0051577c",
      "incomplete_value": true,
      "site": "0051577c",
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
      "definition_site": "005157c8",
      "incomplete_value": true,
      "site": "005157d0",
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
      "definition_site": "005157c8",
      "incomplete_value": true,
      "site": "005157d0",
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
    "ordinal": 19,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00515768",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "00515770",
      "DATA",
      [
        "storage",
        "00bed158",
        null,
        "pointer"
      ]
    ],
    [
      "0051577c",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00515768",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00515770",
      "DATA",
      [
        "storage",
        "00bed1a8",
        null,
        "pointer"
      ]
    ],
    [
      "0051577c",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00515748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515718.md#insn-00515748) · [`00515768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515718.md#insn-00515768) · [`005157b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515718.md#insn-005157b4)
- 新版 `00515748`（命令位置の公開資料なし） · `00515768`（命令位置の公開資料なし） · `005157b4`（命令位置の公開資料なし）

~~~diff
- 00515748 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00515748 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00515748 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00515748 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00515748 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 00515748 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00515748 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00515748 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00515748 bytes 29610591
+ 00515748 bytes 29a10691
- 00515768 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 00515768 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00515768 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 00515768 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00515768 bytes 08b940f9
+ 00515768 bytes 08e140f9
- 005157b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:178:8"]]
- 005157b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005157b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c8:8"]]
+ 005157b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005157b4 bytes 08bd40f9
+ 005157b4 bytes 08e540f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-435da8391bca5c8f61d08b2826417d99"></a>

### [`005158d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005158d4.md) → [`005158d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/005158d4.md) FUN_005158d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515468.md) · 呼出先 6件 [`00515e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515e40.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb260.md) [`00bdb270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb270.md)
- 新版 呼出元 1件 [`00515468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515468.md) · 呼出先 6件 [`00515e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515e40.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) [`00bdb2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00515990",
      "incomplete_value": false,
      "site": "00515994",
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
            "const:544:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00515990",
      "incomplete_value": false,
      "site": "00515994",
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
            "const:5d1:8"
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
      "00515990",
      "PARAM",
      [
        "storage",
        "002945d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00515990",
      "PARAM",
      [
        "storage",
        "00294544",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00515990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005158d4.md#insn-00515990)
- 新版 `00515990`（命令位置の公開資料なし）

~~~diff
- 00515990 ["COPY", "tmp:0:8", ["const:5d1:8"]]
- 00515990 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00515990 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00515990 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00515990 ["COPY", "tmp:0:8", ["const:544:8"]]
+ 00515990 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00515990 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00515990 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00515990 bytes 21441791
+ 00515990 bytes 21101591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fab109ba060630831539e8efabedde72"></a>

### [`005159e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005159e0.md) → [`005159e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/005159e0.md) FUN_005159e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005159f8",
      "incomplete_value": false,
      "site": "005159fc",
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
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005159f8",
      "incomplete_value": false,
      "site": "005159fc",
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
            "const:f8:8"
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
      "definition_site": "00515a3c",
      "incomplete_value": true,
      "site": "00515a3c",
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
      "definition_site": "00515a3c",
      "incomplete_value": true,
      "site": "00515a3c",
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
      "definition_site": "00515a64",
      "incomplete_value": true,
      "site": "00515a64",
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
      "definition_site": "00515a64",
      "incomplete_value": true,
      "site": "00515a64",
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
      "005159fc",
      "DATA",
      [
        "storage",
        "00bed0f8",
        null,
        "pointer"
      ]
    ],
    [
      "00515a10",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00515a30",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005159fc",
      "DATA",
      [
        "storage",
        "00bed148",
        null,
        "pointer"
      ]
    ],
    [
      "00515a10",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00515a30",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005159f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005159e0.md#insn-005159f8) · [`00515a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005159e0.md#insn-00515a10) · [`00515a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/005159e0.md#insn-00515a30)
- 新版 `005159f8`（命令位置の公開資料なし） · `00515a10`（命令位置の公開資料なし） · `00515a30`（命令位置の公開資料なし）

~~~diff
- 005159f8 ["COPY", "tmp:0:8", ["const:f8:8"]]
- 005159f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005159f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005159f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005159f8 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 005159f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005159f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005159f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005159f8 bytes 08e10391
+ 005159f8 bytes 08210591
- 00515a10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00515a10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00515a10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00515a10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00515a10 bytes 299543f9
+ 00515a10 bytes 29bd43f9
- 00515a30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 00515a30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00515a30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 00515a30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00515a30 bytes 08b940f9
+ 00515a30 bytes 08e140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acf21a291aedc31a98781d38f816e262"></a>

### [`00515a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515a90.md) → [`00515a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515a90.md) FUN_00515a90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00515aa8",
      "incomplete_value": false,
      "site": "00515aac",
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
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00515aa8",
      "incomplete_value": false,
      "site": "00515aac",
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
            "const:f8:8"
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
      "definition_site": "00515aec",
      "incomplete_value": true,
      "site": "00515aec",
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
      "definition_site": "00515aec",
      "incomplete_value": true,
      "site": "00515aec",
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
      "definition_site": "00515b14",
      "incomplete_value": true,
      "site": "00515b14",
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
      "definition_site": "00515b14",
      "incomplete_value": true,
      "site": "00515b14",
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
      "00515aac",
      "DATA",
      [
        "storage",
        "00bed0f8",
        null,
        "pointer"
      ]
    ],
    [
      "00515ac0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00515ae0",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00515aac",
      "DATA",
      [
        "storage",
        "00bed148",
        null,
        "pointer"
      ]
    ],
    [
      "00515ac0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00515ae0",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00515aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515a90.md#insn-00515aa8) · [`00515ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515a90.md#insn-00515ac0) · [`00515ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515a90.md#insn-00515ae0)
- 新版 `00515aa8`（命令位置の公開資料なし） · `00515ac0`（命令位置の公開資料なし） · `00515ae0`（命令位置の公開資料なし）

~~~diff
- 00515aa8 ["COPY", "tmp:0:8", ["const:f8:8"]]
- 00515aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00515aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00515aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00515aa8 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00515aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00515aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00515aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00515aa8 bytes 08e10391
+ 00515aa8 bytes 08210591
- 00515ac0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00515ac0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00515ac0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00515ac0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00515ac0 bytes 299543f9
+ 00515ac0 bytes 29bd43f9
- 00515ae0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 00515ae0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00515ae0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 00515ae0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00515ae0 bytes 08b940f9
+ 00515ae0 bytes 08e140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62315457999c1d561e9860a040449352"></a>

### [`00515cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515cc4.md) → [`00515cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515cc4.md) FUN_00515cc4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00515718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515718.md) · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00515718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515718.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00515d00",
      "incomplete_value": true,
      "site": "00515d00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00515d00",
      "incomplete_value": true,
      "site": "00515d00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00515cf0",
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
      "00515cf0",
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

- 旧版 [`00515cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515cc4.md#insn-00515cf0)
- 新版 `00515cf0`（命令位置の公開資料なし）

~~~diff
- 00515cf0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00515cf0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00515cf0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00515cf0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00515cf0 bytes 299543f9
+ 00515cf0 bytes 29bd43f9
~~~


<a id="compare-df77368217170cce1b77bfe2a06f1a89"></a>

### [`00515f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515f5c.md) → [`00515f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00515/00515f5c.md) FUN_00515f5c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00515f74",
      "incomplete_value": false,
      "site": "00515f78",
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
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00515f74",
      "incomplete_value": false,
      "site": "00515f78",
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
            "const:158:8"
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
      "definition_site": "00515fb8",
      "incomplete_value": true,
      "site": "00515fb8",
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
      "definition_site": "00515fb8",
      "incomplete_value": true,
      "site": "00515fb8",
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
      "definition_site": "00515fe0",
      "incomplete_value": true,
      "site": "00515fe0",
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
      "definition_site": "00515fe0",
      "incomplete_value": true,
      "site": "00515fe0",
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
      "00515f78",
      "DATA",
      [
        "storage",
        "00bed158",
        null,
        "pointer"
      ]
    ],
    [
      "00515f8c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00515fac",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00515f78",
      "DATA",
      [
        "storage",
        "00bed1a8",
        null,
        "pointer"
      ]
    ],
    [
      "00515f8c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00515fac",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00515f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515f5c.md#insn-00515f74) · [`00515f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515f5c.md#insn-00515f8c) · [`00515fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515f5c.md#insn-00515fac)
- 新版 `00515f74`（命令位置の公開資料なし） · `00515f8c`（命令位置の公開資料なし） · `00515fac`（命令位置の公開資料なし）

~~~diff
- 00515f74 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00515f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00515f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00515f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00515f74 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 00515f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00515f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00515f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00515f74 bytes 08610591
+ 00515f74 bytes 08a10691
- 00515f8c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00515f8c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00515f8c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00515f8c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00515f8c bytes 299543f9
+ 00515f8c bytes 29bd43f9
- 00515fac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 00515fac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00515fac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 00515fac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00515fac bytes 08b940f9
+ 00515fac bytes 08e140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39a30880c2197683795ce0cff73c3651"></a>

### [`0051600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/0051600c.md) → [`0051600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/0051600c.md) FUN_0051600c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00516024",
      "incomplete_value": false,
      "site": "00516028",
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
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516024",
      "incomplete_value": false,
      "site": "00516028",
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
            "const:158:8"
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
      "definition_site": "00516068",
      "incomplete_value": true,
      "site": "00516068",
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
      "definition_site": "00516068",
      "incomplete_value": true,
      "site": "00516068",
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
      "definition_site": "00516090",
      "incomplete_value": true,
      "site": "00516090",
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
      "definition_site": "00516090",
      "incomplete_value": true,
      "site": "00516090",
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
      "00516028",
      "DATA",
      [
        "storage",
        "00bed158",
        null,
        "pointer"
      ]
    ],
    [
      "0051603c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0051605c",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00516028",
      "DATA",
      [
        "storage",
        "00bed1a8",
        null,
        "pointer"
      ]
    ],
    [
      "0051603c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0051605c",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/0051600c.md#insn-00516024) · [`0051603c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/0051600c.md#insn-0051603c) · [`0051605c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/0051600c.md#insn-0051605c)
- 新版 `00516024`（命令位置の公開資料なし） · `0051603c`（命令位置の公開資料なし） · `0051605c`（命令位置の公開資料なし）

~~~diff
- 00516024 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00516024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00516024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00516024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00516024 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 00516024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00516024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00516024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00516024 bytes 08610591
+ 00516024 bytes 08a10691
- 0051603c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0051603c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051603c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0051603c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0051603c bytes 299543f9
+ 0051603c bytes 29bd43f9
- 0051605c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
- 0051605c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051605c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 0051605c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051605c bytes 08b940f9
+ 0051605c bytes 08e140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9256711c2facab6d7f66a129465bace6"></a>

### [`005162fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005162fc.md) → [`005162fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005162fc.md) FUN_005162fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`004bb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb810.md) [`00514bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514bd4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) [`00514bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514bd4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

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
      "definition_site": "00516330",
      "incomplete_value": true,
      "site": "00516330",
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
      "definition_site": "00516330",
      "incomplete_value": true,
      "site": "00516330",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00516384",
      "incomplete_value": false,
      "site": "00516384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516384",
      "incomplete_value": false,
      "site": "00516384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "00516324",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "00516330",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00516348",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00516324",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00516330",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00516348",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005162fc.md#insn-00516324) · [`00516380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005162fc.md#insn-00516380)
- 新版 `00516324`（命令位置の公開資料なし） · `00516380`（命令位置の公開資料なし）

~~~diff
- 00516324 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:170:8"]]
- 00516324 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00516324 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1c0:8"]]
+ 00516324 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00516324 bytes 94ba40f9
+ 00516324 bytes 94e240f9
- 00516380 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 00516380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00516380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00516380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00516380 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 00516380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00516380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00516380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00516380 bytes 08e13c91
+ 00516380 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef3c5f2407e0e4914fc7d19487c89213"></a>

### [`005163b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005163b4.md) → [`005163b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005163b4.md) FUN_005163b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`004bb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb810.md) [`00514bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514bd4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) [`00514bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514bd4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "definition_site": "005163e8",
      "incomplete_value": true,
      "site": "005163e8",
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
      "definition_site": "005163e8",
      "incomplete_value": true,
      "site": "005163e8",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0051643c",
      "incomplete_value": false,
      "site": "0051643c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051643c",
      "incomplete_value": false,
      "site": "0051643c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "005163dc",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "005163e8",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00516400",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "005163dc",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "005163e8",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00516400",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005163dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005163b4.md#insn-005163dc) · [`00516438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005163b4.md#insn-00516438)
- 新版 `005163dc`（命令位置の公開資料なし） · `00516438`（命令位置の公開資料なし）

~~~diff
- 005163dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:170:8"]]
- 005163dc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005163dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1c0:8"]]
+ 005163dc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 005163dc bytes 94ba40f9
+ 005163dc bytes 94e240f9
- 00516438 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 00516438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00516438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00516438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00516438 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 00516438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00516438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00516438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00516438 bytes 08e13c91
+ 00516438 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9e11dfebcff04c222ac9d19df5836d6"></a>

### [`00516464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/00516464.md) → [`00516464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/00516464.md) FUN_00516464

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00514cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514cc0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00514cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514cc0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.25% / 新版 92.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005165a4",
      "incomplete_value": true,
      "site": "005165a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005165a4",
      "incomplete_value": true,
      "site": "005165a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005165d0",
      "incomplete_value": true,
      "site": "005165d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005165d0",
      "incomplete_value": true,
      "site": "005165d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005165fc",
      "incomplete_value": true,
      "site": "005165fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005165fc",
      "incomplete_value": true,
      "site": "005165fc",
      "value": [
        "LOAD",
        "8",
        [
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
      "00516594",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "005165c0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "005165ec",
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
      "00516594",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "005165c0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "005165ec",
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

- 旧版 [`00516594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/00516464.md#insn-00516594) · [`005165c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/00516464.md#insn-005165c0) · [`005165ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/00516464.md#insn-005165ec)
- 新版 `00516594`（命令位置の公開資料なし） · `005165c0`（命令位置の公開資料なし） · `005165ec`（命令位置の公開資料なし）

~~~diff
- 00516594 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00516594 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00516594 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 00516594 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00516594 bytes 899643f9
+ 00516594 bytes 89be43f9
- 005165c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 005165c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005165c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 005165c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005165c0 bytes 899643f9
+ 005165c0 bytes 89be43f9
- 005165ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 005165ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005165ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 005165ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005165ec bytes 899643f9
+ 005165ec bytes 89be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a64017b624e7d2f12527c5dad5a92db"></a>

### [`005166c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005166c8.md) → [`005166c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005166c8.md) FUN_005166c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`004bb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb810.md) [`00514bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514bd4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) [`00514bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514bd4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

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
      "definition_site": "005166fc",
      "incomplete_value": true,
      "site": "005166fc",
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
      "definition_site": "005166fc",
      "incomplete_value": true,
      "site": "005166fc",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0051674c",
      "incomplete_value": false,
      "site": "00516750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051674c",
      "incomplete_value": false,
      "site": "00516750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "005166f0",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "005166fc",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00516714",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "005166f0",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "005166fc",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00516714",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005166f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005166c8.md#insn-005166f0) · [`0051674c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005166c8.md#insn-0051674c)
- 新版 `005166f0`（命令位置の公開資料なし） · `0051674c`（命令位置の公開資料なし）

~~~diff
- 005166f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:170:8"]]
- 005166f0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005166f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1c0:8"]]
+ 005166f0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 005166f0 bytes 94ba40f9
+ 005166f0 bytes 94e240f9
- 0051674c ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0051674c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051674c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051674c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051674c ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 0051674c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051674c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051674c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051674c bytes 29613991
+ 0051674c bytes 29a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5f0267d321a777c08714b4bc1a30b69"></a>

### [`00516794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/00516794.md) → [`00516794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/00516794.md) FUN_00516794

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`004bb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb810.md) [`00514bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514bd4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) [`00514bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514bd4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

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
      "definition_site": "005167c8",
      "incomplete_value": true,
      "site": "005167c8",
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
      "definition_site": "005167c8",
      "incomplete_value": true,
      "site": "005167c8",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00516818",
      "incomplete_value": false,
      "site": "0051681c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516818",
      "incomplete_value": false,
      "site": "0051681c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "005167bc",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "005167c8",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "005167e0",
      "DATA",
      [
        "storage",
        "00be9d48",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "005167bc",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "005167c8",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "005167e0",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005167bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/00516794.md#insn-005167bc) · [`00516818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/00516794.md#insn-00516818)
- 新版 `005167bc`（命令位置の公開資料なし） · `00516818`（命令位置の公開資料なし）

~~~diff
- 005167bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:170:8"]]
- 005167bc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005167bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1c0:8"]]
+ 005167bc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 005167bc bytes 94ba40f9
+ 005167bc bytes 94e240f9
- 00516818 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00516818 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00516818 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00516818 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516818 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00516818 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516818 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516818 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00516818 bytes 29613991
+ 00516818 bytes 29a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf0aafe71124f85853b03445a2c04e73"></a>

### [`005168d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005168d8.md) → [`005168d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005168d8.md) FUN_005168d8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00514cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00514/00514cc0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00514cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514cc0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00516a18",
      "incomplete_value": true,
      "site": "00516a18",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516a18",
      "incomplete_value": true,
      "site": "00516a18",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00516a44",
      "incomplete_value": true,
      "site": "00516a44",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516a44",
      "incomplete_value": true,
      "site": "00516a44",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00516a70",
      "incomplete_value": true,
      "site": "00516a70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516a70",
      "incomplete_value": true,
      "site": "00516a70",
      "value": [
        "LOAD",
        "8",
        [
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
      "00516a08",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00516a34",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00516a60",
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
      "00516a08",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00516a34",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00516a60",
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

- 旧版 [`00516a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005168d8.md#insn-00516a08) · [`00516a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005168d8.md#insn-00516a34) · [`00516a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005168d8.md#insn-00516a60)
- 新版 `00516a08`（命令位置の公開資料なし） · `00516a34`（命令位置の公開資料なし） · `00516a60`（命令位置の公開資料なし）

~~~diff
- 00516a08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00516a08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00516a08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 00516a08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00516a08 bytes 899643f9
+ 00516a08 bytes 89be43f9
- 00516a34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00516a34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00516a34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 00516a34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00516a34 bytes 899643f9
+ 00516a34 bytes 89be43f9
- 00516a60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00516a60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00516a60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:778:8"]]
+ 00516a60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00516a60 bytes 899643f9
+ 00516a60 bytes 89be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

