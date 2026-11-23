# v15.7.3 → v15.7.4 · 最優先の変更候補 (23)

[一覧の目次](README.md)

<a id="compare-381fc4609340c80c055cb3dc970ad56b"></a>

### [`00595ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/00595ca0.md) → [`00595ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595ca0.md) FUN_00595ca0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.40% / 新版 84.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595cdc",
      "incomplete_value": false,
      "site": "00595ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595cdc",
      "incomplete_value": false,
      "site": "00595ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "definition_site": "00595d48",
      "incomplete_value": true,
      "site": "00595d48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595d48",
      "incomplete_value": true,
      "site": "00595d48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:315:8"
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
      "definition_site": "00595d60",
      "incomplete_value": true,
      "site": "00595d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:47d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595d60",
      "incomplete_value": true,
      "site": "00595d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e3:8"
              ]
            ]
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
      "00595ce0",
      "DATA",
      [
        "storage",
        "00bf3578",
        null,
        "undefined *"
      ]
    ],
    [
      "00595d14",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00595d34",
      "READ",
      [
        "storage",
        "002a0315",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00595ce0",
      "DATA",
      [
        "storage",
        "00bf35c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00595d14",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00595d34",
      "READ",
      [
        "storage",
        "002a03a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/00595ca0.md#insn-00595cdc) · [`00595d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/00595ca0.md#insn-00595d10) · [`00595d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/00595ca0.md#insn-00595d30)
- 新版 [`00595cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595ca0.md#insn-00595cdc) · [`00595d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595ca0.md#insn-00595d10) · [`00595d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595ca0.md#insn-00595d30)

~~~diff
- 00595cdc ["COPY", "tmp:0:8", ["const:578:8"]]
- 00595cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00595cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00595cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595cdc ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 00595cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00595cdc bytes 08e11591
+ 00595cdc bytes 08211791
- 00595d10 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00595d10 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00595d10 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00595d10 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00595d10 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00595d10 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00595d10 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00595d10 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00595d10 bytes 39e30091
+ 00595d10 bytes 39e30191
- 00595d30 ["COPY", "tmp:0:8", ["const:315:8"]]
- 00595d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00595d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00595d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595d30 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 00595d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00595d30 bytes 08550c91
+ 00595d30 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9906c0a535b1d5e655a082f697803d92"></a>

### [`00596128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596128.md) → [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) FUN_00596128

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00596784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596784.md) · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`004588e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00458/004588e8.md) [`004588f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00458/004588f0.md) [`00458974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00458/00458974.md) [`0045a030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a030.md)
- 新版 呼出元 1件 [`00596784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596784.md) · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`004588e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/004588e8.md) [`004588f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/004588f0.md) [`00458974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458974.md) [`0045a030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md)

変更の種類 call, call_target, operands_and_dependencies

命令の説明率　旧版 99.11% / 新版 99.11%

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
      "site": "0059617c",
      "value": [
        "leaf",
        "ram:abf570:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0059617c",
      "value": [
        "leaf",
        "ram:abf52c:8"
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
      "0059617c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00abf52c"
      ]
    ]
  ],
  "added": [
    [
      "0059617c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00abf570"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059617c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596128.md#insn-0059617c)
- 新版 [`0059617c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md#insn-0059617c)

~~~diff
- 0059617c ["INT_ADD", "register:40f0:8", ["const:59617c:8", "const:4:8"]]
- 0059617c ["CALL", null, ["ram:abf52c:8"]]
+ 0059617c ["INT_ADD", "register:40f0:8", ["const:59617c:8", "const:4:8"]]
+ 0059617c ["CALL", null, ["ram:abf570:8"]]
- 0059617c bytes eca41494
+ 0059617c bytes fda41494
~~~


<a id="compare-70f621ce4b3019e02eca61c8f49863d4"></a>

### [`005962e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/005962e8.md) → [`005962e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/005962e8.md) FUN_005962e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`0059675c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/0059675c.md) [`0059682c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/0059682c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0059675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/0059675c.md) [`0059682c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/0059682c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596328",
      "incomplete_value": false,
      "site": "00596330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596328",
      "incomplete_value": false,
      "site": "00596330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00596438",
      "incomplete_value": false,
      "site": "0059643c",
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
      "definition_site": "00596438",
      "incomplete_value": false,
      "site": "0059643c",
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
      "00596330",
      "DATA",
      [
        "storage",
        "00bf35d8",
        null,
        "pointer"
      ]
    ],
    [
      "005963d4",
      "READ",
      [
        "storage",
        "00bf35e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00596438",
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
      "00596330",
      "DATA",
      [
        "storage",
        "00bf3628",
        null,
        "pointer"
      ]
    ],
    [
      "005963d4",
      "READ",
      [
        "storage",
        "00bf3638",
        null,
        "undefined *"
      ]
    ],
    [
      "00596438",
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

- 旧版 [`00596328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/005962e8.md#insn-00596328) · [`00596438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/005962e8.md#insn-00596438)
- 新版 [`00596328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/005962e8.md#insn-00596328) · [`00596438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/005962e8.md#insn-00596438)

~~~diff
- 00596328 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00596328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00596328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00596328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00596328 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 00596328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00596328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00596328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00596328 bytes 08611791
+ 00596328 bytes 08a11891
- 00596438 ["COPY", "tmp:0:8", ["const:5d1:8"]]
- 00596438 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00596438 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00596438 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00596438 ["COPY", "tmp:0:8", ["const:544:8"]]
+ 00596438 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00596438 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00596438 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00596438 bytes 21441791
+ 00596438 bytes 21101591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5badccab6badfdfe013a46440dcac797"></a>

### [`005964f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/005964f4.md) → [`005964f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/005964f4.md) FUN_005964f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb640.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb690.md)

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
      "definition_site": "0059650c",
      "incomplete_value": false,
      "site": "00596510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059650c",
      "incomplete_value": false,
      "site": "00596510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "00596510",
      "DATA",
      [
        "storage",
        "00bf3578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00596510",
      "DATA",
      [
        "storage",
        "00bf35c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059650c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/005964f4.md#insn-0059650c)
- 新版 [`0059650c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/005964f4.md#insn-0059650c)

~~~diff
- 0059650c ["COPY", "tmp:0:8", ["const:578:8"]]
- 0059650c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059650c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059650c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059650c ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 0059650c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059650c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059650c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059650c bytes 29e11591
+ 0059650c bytes 29211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d9ef2b6bbc211130e3fe4e04ba3de93"></a>

### [`005965a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/005965a8.md) → [`005965a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/005965a8.md) FUN_005965a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb640.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb690.md)

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
      "definition_site": "005965c0",
      "incomplete_value": false,
      "site": "005965c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005965c0",
      "incomplete_value": false,
      "site": "005965c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "005965c4",
      "DATA",
      [
        "storage",
        "00bf3578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005965c4",
      "DATA",
      [
        "storage",
        "00bf35c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005965c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/005965a8.md#insn-005965c0)
- 新版 [`005965c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/005965a8.md#insn-005965c0)

~~~diff
- 005965c0 ["COPY", "tmp:0:8", ["const:578:8"]]
- 005965c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005965c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005965c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005965c0 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 005965c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005965c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005965c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005965c0 bytes 29e11591
+ 005965c0 bytes 29211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7097039255b0db77ad013e55e79d8ce2"></a>

### [`00596708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596708.md) → [`00596708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596708.md) FUN_00596708

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

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
      "definition_site": "0059672c",
      "incomplete_value": true,
      "site": "0059672c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0059672c",
      "incomplete_value": true,
      "site": "0059672c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00596720",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0059672c",
      "DATA",
      [
        "storage",
        "00c12ee0",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00596720",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "0059672c",
      "DATA",
      [
        "storage",
        "00c12f30",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596708.md#insn-00596720)
- 新版 [`00596720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596708.md#insn-00596720)

~~~diff
- 00596720 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 00596720 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00596720 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 00596720 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00596720 bytes 080947f9
+ 00596720 bytes 083147f9
~~~


<a id="compare-178314f8ee41867061470a82455ffc1a"></a>

### [`00596948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596948.md) → [`00596948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596948.md) _INIT_60

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.40% / 新版 90.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00596a04",
      "incomplete_value": true,
      "site": "00596a20",
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
                "const:36c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596a04",
      "incomplete_value": true,
      "site": "00596a20",
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
                "const:36e:8"
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
      "definition_site": "00596a44",
      "incomplete_value": true,
      "site": "00596a88",
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
                "const:526:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596a44",
      "incomplete_value": true,
      "site": "00596a88",
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
                "const:5b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00596b70",
      "incomplete_value": false,
      "site": "00596b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596b70",
      "incomplete_value": false,
      "site": "00596b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "00596984",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005969a8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005969c8",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00596984",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "005969a8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "005969c8",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596948.md#insn-00596974) · [`0059697c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596948.md#insn-0059697c)
- 新版 [`00596974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596948.md#insn-00596974) · [`0059697c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596948.md#insn-0059697c)

~~~diff
- 00596974 ["COPY", "tmp:0:8", ["const:948:8"]]
- 00596974 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00596974 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00596974 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00596974 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 00596974 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00596974 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00596974 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00596974 bytes 73222591
+ 00596974 bytes 73222691
- 0059697c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0059697c bytes 89e8ffb0
+ 0059697c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0059697c bytes 89e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8713deee1fad69f8c4fec38574e865b"></a>

### [`00596d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596d14.md) → [`00596d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596d14.md) FUN_00596d14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596cd8.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596cd8.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.54% / 新版 91.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596d54",
      "incomplete_value": false,
      "site": "00596d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596d54",
      "incomplete_value": false,
      "site": "00596d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "definition_site": "00596d88",
      "incomplete_value": true,
      "site": "00596d98",
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
                "const:291000:8"
              ],
              [
                "leaf",
                "const:c36:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596d88",
      "incomplete_value": true,
      "site": "00596d98",
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
                "const:291000:8"
              ],
              [
                "leaf",
                "const:cc3:8"
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
      "definition_site": "00596d8c",
      "incomplete_value": true,
      "site": "00596d9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00596d8c",
      "incomplete_value": true,
      "site": "00596d9c",
      "value": [
        "LOAD",
        "8",
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
      "00596d60",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00596d88",
      "READ",
      [
        "storage",
        "00291cc3",
        null,
        "string"
      ]
    ],
    [
      "00596d8c",
      "READ",
      [
        "storage",
        "00291cd3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00596d60",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00596d88",
      "READ",
      [
        "storage",
        "00291c36",
        null,
        "string"
      ]
    ],
    [
      "00596d8c",
      "READ",
      [
        "storage",
        "00291c46",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596d14.md#insn-00596d54) · [`00596d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596d14.md#insn-00596d80) · [`00596d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596d14.md#insn-00596d84)
- 新版 [`00596d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596d14.md#insn-00596d54) · [`00596d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596d14.md#insn-00596d80)

~~~diff
- 00596d54 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00596d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00596d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00596d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00596d54 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00596d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00596d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00596d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00596d54 bytes 08a13491
+ 00596d54 bytes 08e13591
- 00596d80 ["COPY", "tmp:0:8", ["const:cc3:8"]]
- 00596d80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00596d80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00596d80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00596d80 ["COPY", "tmp:0:8", ["const:c36:8"]]
+ 00596d80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00596d80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00596d80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00596d80 bytes 080d3391
+ 00596d80 bytes 08d93091
- 00596d84 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00596d84 bytes c9e8ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcd9b4f6918c8adbec91bb581a548cbe"></a>

### [`00597088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597088.md) → [`00597088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597088.md) FUN_00597088

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596cd8.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596cd8.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.57% / 新版 96.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005970c8",
      "incomplete_value": false,
      "site": "005970cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005970c8",
      "incomplete_value": false,
      "site": "005970cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "definition_site": "005970e4",
      "incomplete_value": true,
      "site": "005970f4",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005970e4",
      "incomplete_value": true,
      "site": "005970f4",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:5e9:8"
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
      "definition_site": "005970e8",
      "incomplete_value": true,
      "site": "005970f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005970e8",
      "incomplete_value": true,
      "site": "005970f8",
      "value": [
        "LOAD",
        "8",
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
      "005970cc",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "005970e4",
      "READ",
      [
        "storage",
        "0029d5e9",
        null,
        "string"
      ]
    ],
    [
      "005970e8",
      "READ",
      [
        "storage",
        "0029d5f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005970cc",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "005970e4",
      "READ",
      [
        "storage",
        "0029d674",
        null,
        "string"
      ]
    ],
    [
      "005970e8",
      "READ",
      [
        "storage",
        "0029d684",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005970c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597088.md#insn-005970c8) · [`005970dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597088.md#insn-005970dc) · [`005970e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597088.md#insn-005970e0)
- 新版 [`005970c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597088.md#insn-005970c8) · [`005970dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597088.md#insn-005970dc)

~~~diff
- 005970c8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 005970c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005970c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005970c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005970c8 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 005970c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005970c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005970c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005970c8 bytes 08a13491
+ 005970c8 bytes 08e13591
- 005970dc ["COPY", "tmp:0:8", ["const:5e9:8"]]
- 005970dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005970dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005970dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005970dc ["COPY", "tmp:0:8", ["const:674:8"]]
+ 005970dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005970dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005970dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005970dc bytes 08a51791
+ 005970dc bytes 08d11991
- 005970e0 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 005970e0 bytes c9e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a1889de001ff6eb65b8f10c6cadf08e"></a>

### [`005978a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/005978a4.md) → [`005978a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/005978a4.md) FUN_005978a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596cd8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596cd8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005978e4",
      "incomplete_value": false,
      "site": "005978ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005978e4",
      "incomplete_value": false,
      "site": "005978ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "definition_site": "00597908",
      "incomplete_value": true,
      "site": "00597918",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:9ba:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597908",
      "incomplete_value": true,
      "site": "00597918",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:a47:8"
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
      "definition_site": "0059790c",
      "incomplete_value": true,
      "site": "0059791c",
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
      "definition_site": "0059790c",
      "incomplete_value": true,
      "site": "0059791c",
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
      "005978ec",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00597908",
      "READ",
      [
        "storage",
        "00292a47",
        null,
        "string"
      ]
    ],
    [
      "0059790c",
      "READ",
      [
        "storage",
        "00292a50",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005978ec",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00597908",
      "READ",
      [
        "storage",
        "002929ba",
        null,
        "string"
      ]
    ],
    [
      "0059790c",
      "READ",
      [
        "storage",
        "002929c3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005978e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/005978a4.md#insn-005978e4) · [`00597900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/005978a4.md#insn-00597900) · [`00597904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/005978a4.md#insn-00597904)
- 新版 [`005978e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/005978a4.md#insn-005978e4) · [`00597900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/005978a4.md#insn-00597900)

~~~diff
- 005978e4 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 005978e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005978e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005978e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005978e4 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 005978e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005978e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005978e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005978e4 bytes 29a13491
+ 005978e4 bytes 29e13591
- 00597900 ["COPY", "tmp:0:8", ["const:a47:8"]]
- 00597900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00597900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00597900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597900 ["COPY", "tmp:0:8", ["const:9ba:8"]]
+ 00597900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00597900 bytes 081d2991
+ 00597900 bytes 08e92691
- 00597904 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00597904 bytes c9e8ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9edc4c048f0d5a3511d45e41418a3fb4"></a>

### [`00597bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597bc8.md) → [`00597bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597bc8.md) FUN_00597bc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596cd8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md)
- 新版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596cd8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.29% / 新版 93.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00597c0c",
      "incomplete_value": false,
      "site": "00597c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597c0c",
      "incomplete_value": false,
      "site": "00597c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "definition_site": "00597d78",
      "incomplete_value": true,
      "site": "00597d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00597d78",
      "incomplete_value": true,
      "site": "00597d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00597d74",
      "incomplete_value": true,
      "site": "00597d80",
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
      "definition_site": "00597d74",
      "incomplete_value": true,
      "site": "00597d80",
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
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00597c14",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00597d68",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "00597d6c",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00597c14",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00597d68",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "00597d6c",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597bc8.md#insn-00597c0c) · [`00597d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597bc8.md#insn-00597d68) · [`00597d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597bc8.md#insn-00597d6c)
- 新版 [`00597c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597bc8.md#insn-00597c0c) · [`00597d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597bc8.md#insn-00597d68) · [`00597d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597bc8.md#insn-00597d6c)

~~~diff
- 00597c0c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00597c0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00597c0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00597c0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00597c0c ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00597c0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00597c0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00597c0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00597c0c bytes 29a13491
+ 00597c0c bytes 29e13591
- 00597d68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 00597d68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00597d68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00597d68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00597d68 bytes 08b946f9
+ 00597d68 bytes 08e146f9
- 00597d6c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
- 00597d6c ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00597d6c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
+ 00597d6c ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00597d6c bytes b5be46f9
+ 00597d6c bytes b5e646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dec5402e244746cfea94c16305e235eb"></a>

### [`00597ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597ea8.md) → [`00597ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597ea8.md) FUN_00597ea8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596cd8.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596cd8.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.03% / 新版 89.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00597ee8",
      "incomplete_value": false,
      "site": "00597ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597ee8",
      "incomplete_value": false,
      "site": "00597ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "definition_site": "00597f1c",
      "incomplete_value": true,
      "site": "00597f2c",
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
                "const:745:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597f1c",
      "incomplete_value": true,
      "site": "00597f2c",
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
                "const:6ba:8"
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
      "definition_site": "00597f20",
      "incomplete_value": true,
      "site": "00597f30",
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
      "definition_site": "00597f20",
      "incomplete_value": true,
      "site": "00597f30",
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
      "00597ef8",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00597f1c",
      "READ",
      [
        "storage",
        "002a46ba",
        null,
        "string"
      ]
    ],
    [
      "00597f20",
      "READ",
      [
        "storage",
        "002a46c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00597ef8",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00597f1c",
      "READ",
      [
        "storage",
        "002a4745",
        null,
        "string"
      ]
    ],
    [
      "00597f20",
      "READ",
      [
        "storage",
        "002a4753",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597ea8.md#insn-00597ee8) · [`00597f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597ea8.md#insn-00597f14) · [`00597f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597ea8.md#insn-00597f18)
- 新版 [`00597ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597ea8.md#insn-00597ee8) · [`00597f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597ea8.md#insn-00597f14)

~~~diff
- 00597ee8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00597ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00597ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00597ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597ee8 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00597ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00597ee8 bytes 08a13491
+ 00597ee8 bytes 08e13591
- 00597f14 ["COPY", "tmp:0:8", ["const:6ba:8"]]
- 00597f14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00597f14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00597f14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597f14 ["COPY", "tmp:0:8", ["const:745:8"]]
+ 00597f14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597f14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597f14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00597f14 bytes 08e91a91
+ 00597f14 bytes 08151d91
- 00597f18 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00597f18 bytes c9e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b76e19b2401bae2006d7f374b13f24e8"></a>

### [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) → [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) FUN_0059815c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a90870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90870.md) [`00a90e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90e28.md) · 呼出先 59件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abfc.md)
- 新版 呼出元 2件 [`00a908b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a908b4.md) [`00a90e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90e6c.md) · 呼出先 59件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abfc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.57% / 新版 99.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005984b8",
      "incomplete_value": true,
      "site": "005984b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005984b8",
      "incomplete_value": true,
      "site": "005984b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00599cc0",
      "incomplete_value": true,
      "site": "00599cd0",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:61a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599cc0",
      "incomplete_value": true,
      "site": "00599cd0",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:58f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 271,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a060",
      "incomplete_value": true,
      "site": "0059a070",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:68d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a060",
      "incomplete_value": true,
      "site": "0059a070",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:602:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 311,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005984a0",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ],
    [
      "00599cc0",
      "READ",
      [
        "storage",
        "002a358f",
        null,
        "string"
      ]
    ],
    [
      "0059a060",
      "READ",
      [
        "storage",
        "0029d602",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005984a0",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "00599cc0",
      "READ",
      [
        "storage",
        "002a361a",
        null,
        "string"
      ]
    ],
    [
      "0059a060",
      "READ",
      [
        "storage",
        "0029d68d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00598494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md#insn-00598494) · [`00599cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md#insn-00599cbc) · [`0059a05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md#insn-0059a05c)
- 新版 [`00598494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md#insn-00598494) · [`00599cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md#insn-00599cbc) · [`0059a05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md#insn-0059a05c)

~~~diff
- 00598494 ["COPY", "tmp:0:8", ["const:a1:8"]]
- 00598494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00598494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00598494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00598494 ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 00598494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00598494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00598494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00598494 bytes 29850291
+ 00598494 bytes 29ed0491
- 00599cbc ["COPY", "tmp:0:8", ["const:58f:8"]]
- 00599cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00599cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00599cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00599cbc ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00599cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00599cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00599cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00599cbc bytes 083d1691
+ 00599cbc bytes 08691891
- 0059a05c ["COPY", "tmp:0:8", ["const:602:8"]]
- 0059a05c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059a05c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059a05c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059a05c ["COPY", "tmp:0:8", ["const:68d:8"]]
+ 0059a05c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a05c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a05c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059a05c bytes 08091891
+ 0059a05c bytes 08351a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43523e3286aa5009f6c07cfa6b4bf327"></a>

### [`0059d1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d1c0.md) → [`0059d1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d1c0.md) FUN_0059d1c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005978a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/005978a4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005978a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/005978a4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0059d1cc",
      "incomplete_value": false,
      "site": "0059d1d0",
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
      "definition_site": "0059d1cc",
      "incomplete_value": false,
      "site": "0059d1d0",
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
      "0059d1cc",
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
      "0059d1cc",
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

- 旧版 [`0059d1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d1c0.md#insn-0059d1cc)
- 新版 [`0059d1cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d1c0.md#insn-0059d1cc)

~~~diff
- 0059d1cc ["COPY", "tmp:0:8", ["const:303:8"]]
- 0059d1cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0059d1cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0059d1cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0059d1cc ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0059d1cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d1cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d1cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0059d1cc bytes 000c0c91
+ 0059d1cc bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfea64a2e11dea3f5900a964b5e6a751"></a>

### [`0059d658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d658.md) → [`0059d658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d658.md) FUN_0059d658

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0059d664",
      "incomplete_value": true,
      "site": "0059d668",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d664",
      "incomplete_value": true,
      "site": "0059d668",
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
      "0059d664",
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
      "0059d664",
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

- 旧版 [`0059d664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d658.md#insn-0059d664)
- 新版 [`0059d664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d658.md#insn-0059d664)

~~~diff
- 0059d664 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0059d664 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0059d664 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0059d664 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0059d664 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0059d664 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d664 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d664 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0059d664 bytes 000c0c91
+ 0059d664 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0e63bf1ca2b6523ecf2fb3eb04ddd00"></a>

### [`0059d66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d66c.md) → [`0059d66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d66c.md) FUN_0059d66c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) [`0067417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00674/0067417c.md) [`00678d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678d74.md) [`0067c708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c708.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 8件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`00678d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678d74.md) [`0067c708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c708.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0059d678",
      "incomplete_value": false,
      "site": "0059d67c",
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
      "definition_site": "0059d678",
      "incomplete_value": false,
      "site": "0059d67c",
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
      "0059d678",
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
      "0059d678",
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

- 旧版 [`0059d678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d66c.md#insn-0059d678)
- 新版 [`0059d678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d66c.md#insn-0059d678)

~~~diff
- 0059d678 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0059d678 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0059d678 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0059d678 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0059d678 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0059d678 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d678 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d678 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0059d678 bytes 000c0c91
+ 0059d678 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f763d0640b1482d941bc9beabe215eb"></a>

### [`0059f85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059f85c.md) → [`0059f85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f85c.md) _INIT_61

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059fa84",
      "incomplete_value": false,
      "site": "0059fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fa84",
      "incomplete_value": false,
      "site": "0059fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "0059fa8c",
      "incomplete_value": false,
      "site": "0059fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fa8c",
      "incomplete_value": false,
      "site": "0059fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0059f898",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0059f8bc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0059f8dc",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0059f898",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0059f8bc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0059f8dc",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059f888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059f85c.md#insn-0059f888) · [`0059f894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059f85c.md#insn-0059f894) · [`0059f8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059f85c.md#insn-0059f8b0)
- 新版 [`0059f888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f85c.md#insn-0059f888) · [`0059f894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f85c.md#insn-0059f894) · [`0059f8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f85c.md#insn-0059f8b0)

~~~diff
- 0059f888 ["COPY", "tmp:0:8", ["const:960:8"]]
- 0059f888 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0059f888 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0059f888 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0059f888 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 0059f888 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0059f888 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0059f888 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0059f888 bytes 73822591
+ 0059f888 bytes 73822691
- 0059f894 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 0059f894 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059f894 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059f894 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059f894 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 0059f894 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059f894 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059f894 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059f894 bytes 29750b91
+ 0059f894 bytes 29dd0d91
- 0059f8b0 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 0059f8b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059f8b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059f8b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059f8b0 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 0059f8b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f8b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f8b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059f8b0 bytes 4ac10b91
+ 0059f8b0 bytes 4a290e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a04eeb3f868f8b44111765cfa76a8387"></a>

### [`0059fbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059fbec.md) → [`0059fbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059fbec.md) FUN_0059fbec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0059ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059ff30.md) [`006612f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612f8.md)
- 新版 呼出元 1件 [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0059ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059ff30.md) [`006612f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006612f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.59% / 新版 86.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 7件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059fcb0",
      "incomplete_value": true,
      "site": "0059fcc0",
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
                "const:7a2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fcb0",
      "incomplete_value": true,
      "site": "0059fcc0",
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
                "const:717:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0059fe4c",
      "incomplete_value": false,
      "site": "0059fe4c",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "0059fe4c",
      "incomplete_value": false,
      "site": "0059fe4c",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0059fe50",
      "incomplete_value": false,
      "site": "0059fe50",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fe50",
      "incomplete_value": false,
      "site": "0059fe50",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0059fc94",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0059fcb0",
      "READ",
      [
        "storage",
        "002a0717",
        null,
        "string"
      ]
    ],
    [
      "0059fcb4",
      "READ",
      [
        "storage",
        "002a0726",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0059fc94",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0059fcb0",
      "READ",
      [
        "storage",
        "002a07a2",
        null,
        "string"
      ]
    ],
    [
      "0059fcb4",
      "READ",
      [
        "storage",
        "002a07b1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059fc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059fbec.md#insn-0059fc90) · [`0059fca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059fbec.md#insn-0059fca8) · [`0059fcac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059fbec.md#insn-0059fcac)
- 新版 [`0059fc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059fbec.md#insn-0059fc90) · [`0059fca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059fbec.md#insn-0059fca8)

~~~diff
- 0059fc90 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0059fc90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059fc90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059fc90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059fc90 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0059fc90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059fc90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059fc90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059fc90 bytes 08e10091
+ 0059fc90 bytes 08e10191
- 0059fca8 ["COPY", "tmp:0:8", ["const:717:8"]]
- 0059fca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059fca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059fca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059fca8 ["COPY", "tmp:0:8", ["const:7a2:8"]]
+ 0059fca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059fca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059fca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059fca8 bytes 085d1c91
+ 0059fca8 bytes 08891e91
- 0059fcac ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0059fcac bytes 89e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f86e89e9992f9b15e6a8633c0094d22"></a>

### [`0059ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059ff30.md) → [`0059ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059ff30.md) FUN_0059ff30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0059fbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059fbec.md) [`005a2308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a2/005a2308.md) · 呼出先 12件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0065ec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ec80.md) [`0065f044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f044.md) [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`006612f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612f8.md)
- 新版 呼出元 2件 [`0059fbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059fbec.md) [`005a2308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a2/005a2308.md) · 呼出先 12件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0065ec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ec80.md) [`0065f044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f044.md) [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`006612f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006612f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a0144",
      "incomplete_value": true,
      "site": "005a0150",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:ab2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0144",
      "incomplete_value": true,
      "site": "005a0150",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a0144",
      "READ",
      [
        "storage",
        "002aeb46",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a0144",
      "READ",
      [
        "storage",
        "002aeab2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a013c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059ff30.md#insn-005a013c)
- 新版 [`005a013c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059ff30.md#insn-005a013c)

~~~diff
- 005a013c ["COPY", "tmp:0:8", ["const:b46:8"]]
- 005a013c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a013c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a013c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a013c ["COPY", "tmp:0:8", ["const:ab2:8"]]
+ 005a013c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a013c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a013c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a013c bytes 29192d91
+ 005a013c bytes 29c92a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ee75ca5a600d499f4235fe5060c873d"></a>

### [`005a02e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a0/005a02e8.md) → [`005a02e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a0/005a02e8.md) FUN_005a02e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005a33f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a33f8.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446df4.md) [`00447378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447378.md)
- 新版 呼出元 1件 [`005a33f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a33f8.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00446df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446df4.md) [`00447378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447378.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a05c8",
      "incomplete_value": true,
      "site": "005a05e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
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
    "old": {
      "definition_site": "005a05c8",
      "incomplete_value": true,
      "site": "005a05e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
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
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a05d0",
      "incomplete_value": false,
      "site": "005a05e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a05d0",
      "incomplete_value": false,
      "site": "005a05e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "005a05d8",
      "incomplete_value": false,
      "site": "005a05e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a05d8",
      "incomplete_value": false,
      "site": "005a05e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a05c8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005a05d0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a05d8",
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005a05c8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "005a05d0",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a05d8",
      "PARAM",
      [
        "storage",
        "00bf3d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a05c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a0/005a02e8.md#insn-005a05c8) · [`005a05d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a0/005a02e8.md#insn-005a05d0) · [`005a05d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a0/005a02e8.md#insn-005a05d4)
- 新版 [`005a05c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a0/005a02e8.md#insn-005a05c8) · [`005a05d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a0/005a02e8.md#insn-005a05d0)

~~~diff
- 005a05c8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:a78:8"]]
- 005a05c8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a05c8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:ab8:8"]]
+ 005a05c8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005a05c8 bytes 603f45f9
+ 005a05c8 bytes 605f45f9
- 005a05d0 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005a05d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005a05d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005a05d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005a05d0 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005a05d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005a05d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005a05d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005a05d0 bytes 21203991
+ 005a05d0 bytes 21603a91
- 005a05d4 ["COPY", "register:4010:8", ["const:bf3000:8"]]
- 005a05d4 bytes 823200f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fc85550862ccab8414d32249b31fcef"></a>

### [`005a1ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1ae4.md) → [`005a1ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1ae4.md) FUN_005a1ae4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`009e9518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9518.md) · 呼出先 2件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 8件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005eb/005eb040.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`009e955c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e955c.md) · 呼出先 2件 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "005a1b0c",
      "incomplete_value": true,
      "site": "005a1b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a1b0c",
      "incomplete_value": true,
      "site": "005a1b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005a1b04",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "005a1b0c",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1b04",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "005a1b0c",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1ae4.md#insn-005a1b04)
- 新版 [`005a1b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1ae4.md#insn-005a1b04)

~~~diff
- 005a1b04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
- 005a1b04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a1b04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 005a1b04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a1b04 bytes 089142f9
+ 005a1b04 bytes 08b942f9
~~~


<a id="compare-1c3e4cb9f5fe5ac961b27f7421825844"></a>

### [`005a1b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1b30.md) → [`005a1b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1b30.md) FUN_005a1b30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 4件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 4件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005eb/005eb040.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 4件 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1b98",
      "incomplete_value": true,
      "site": "005a1b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a1b98",
      "incomplete_value": true,
      "site": "005a1b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005a1b58",
      "DATA",
      [
        "storage",
        "00c0bd40",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1b90",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "005a1b98",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1b58",
      "DATA",
      [
        "storage",
        "00c0bd90",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1b90",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "005a1b98",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1b30.md#insn-005a1b4c) · [`005a1b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1b30.md#insn-005a1b90)
- 新版 [`005a1b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1b30.md#insn-005a1b4c) · [`005a1b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1b30.md#insn-005a1b90)

~~~diff
- 005a1b4c ["COPY", "tmp:0:8", ["const:d30:8"]]
- 005a1b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1b4c ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 005a1b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1b4c bytes 08c13491
+ 005a1b4c bytes 08013691
- 005a1b90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
- 005a1b90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a1b90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 005a1b90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a1b90 bytes 089142f9
+ 005a1b90 bytes 08b942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-598c795d2d26396dba11169cbbcb0511"></a>

### [`005a1c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1c90.md) → [`005a1c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1c90.md) FUN_005a1c90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) · 呼出先 23件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`0094f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f7d0.md) · 呼出先 23件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1e20",
      "incomplete_value": false,
      "site": "005a1e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1e20",
      "incomplete_value": false,
      "site": "005a1e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "definition_site": "005a1e50",
      "incomplete_value": true,
      "site": "005a1e50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:77e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1e50",
      "incomplete_value": true,
      "site": "005a1e50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1e54",
      "incomplete_value": true,
      "site": "005a1e54",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005a1e54",
      "incomplete_value": true,
      "site": "005a1e54",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a1e28",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1e3c",
      "READ",
      [
        "storage",
        "0029f6f3",
        null,
        "string"
      ]
    ],
    [
      "005a1e44",
      "READ",
      [
        "storage",
        "0029f6f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a1e28",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1e3c",
      "READ",
      [
        "storage",
        "0029f77e",
        null,
        "string"
      ]
    ],
    [
      "005a1e44",
      "READ",
      [
        "storage",
        "0029f784",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1c90.md#insn-005a1e20) · [`005a1e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1c90.md#insn-005a1e38) · [`005a2044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1c90.md#insn-005a2044)
- 新版 [`005a1e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1c90.md#insn-005a1e20) · [`005a1e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1c90.md#insn-005a1e38) · [`005a2044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1c90.md#insn-005a2044)

~~~diff
- 005a1e20 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 005a1e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1e20 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 005a1e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1e20 bytes 08a13491
+ 005a1e20 bytes 08e13591
- 005a1e38 ["COPY", "tmp:0:8", ["const:6f3:8"]]
- 005a1e38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a1e38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a1e38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a1e38 ["COPY", "tmp:0:8", ["const:77e:8"]]
+ 005a1e38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1e38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1e38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a1e38 bytes 29cd1b91
+ 005a1e38 bytes 29f91d91
- 005a2044 ["COPY", "tmp:0:8", ["const:58a:8"]]
- 005a2044 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a2044 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a2044 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a2044 ["COPY", "tmp:0:8", ["const:615:8"]]
+ 005a2044 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a2044 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a2044 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a2044 bytes 29291691
+ 005a2044 bytes 29551891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bf5e2215936e68a21e065c2d97bd2eb"></a>

### [`005a33f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a33f8.md) → [`005a33f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a33f8.md) FUN_005a33f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00963004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00963/00963004.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444edc.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md)
- 新版 呼出元 1件 [`00963004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00963/00963004.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444edc.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.39% / 新版 99.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005a3a3c",
      "incomplete_value": true,
      "site": "005a3a3c",
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
      "definition_site": "005a3a3c",
      "incomplete_value": true,
      "site": "005a3a3c",
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
    "ordinal": 21,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a3a44",
      "incomplete_value": false,
      "site": "005a3a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a3a44",
      "incomplete_value": false,
      "site": "005a3a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "ordinal": 70,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a3a4c",
      "incomplete_value": false,
      "site": "005a3a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a3a4c",
      "incomplete_value": false,
      "site": "005a3a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "ordinal": 70,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a38e8",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "005a39c4",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "005a3a38",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005a38e8",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "005a39c4",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "005a3a38",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a38e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a33f8.md#insn-005a38e8) · [`005a3a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a33f8.md#insn-005a3a38) · [`005a3a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a33f8.md#insn-005a3a44)
- 新版 [`005a38e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a33f8.md#insn-005a38e8) · [`005a3a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a33f8.md#insn-005a3a38) · [`005a3a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a33f8.md#insn-005a3a44)

~~~diff
- 005a38e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d28:8"]]
- 005a38e8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a38e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
+ 005a38e8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 005a38e8 bytes b59646f9
+ 005a38e8 bytes b5be46f9
- 005a3a38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 005a3a38 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a3a38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 005a3a38 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005a3a38 bytes 003d45f9
+ 005a3a38 bytes 005d45f9
- 005a3a44 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 005a3a44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005a3a44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005a3a44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005a3a44 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 005a3a44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005a3a44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005a3a44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005a3a44 bytes 21203991
+ 005a3a44 bytes 21603a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-348332bb1ad97e5c53e833bbf7a1af39"></a>

### [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) → [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) FUN_005a45f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 68件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abfc.md)
- 新版 呼出元 2件 [`0094f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) · 呼出先 68件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abfc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.85% / 新版 98.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5a38",
      "incomplete_value": false,
      "site": "005a5a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5a38",
      "incomplete_value": false,
      "site": "005a5a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "ordinal": 211,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5b8c",
      "incomplete_value": false,
      "site": "005a5b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5b8c",
      "incomplete_value": false,
      "site": "005a5b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 221,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a6148",
      "incomplete_value": false,
      "site": "005a6148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6148",
      "incomplete_value": false,
      "site": "005a6148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "ordinal": 267,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a570c",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "005a5710",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ],
    [
      "005a59ac",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a570c",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "005a5710",
      "READ",
      [
        "storage",
        "00c1b578",
        null,
        "pointer"
      ]
    ],
    [
      "005a59ac",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a570c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md#insn-005a570c) · [`005a5710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md#insn-005a5710) · [`005a5a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md#insn-005a5a34)
- 新版 [`005a570c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md#insn-005a570c) · [`005a5710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md#insn-005a5710) · [`005a5a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md#insn-005a5a34)

~~~diff
- 005a570c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:520:8"]]
- 005a570c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a570c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:570:8"]]
+ 005a570c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 005a570c bytes 189342f9
+ 005a570c bytes 18bb42f9
- 005a5710 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:528:8"]]
- 005a5710 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a5710 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:578:8"]]
+ 005a5710 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 005a5710 bytes 399742f9
+ 005a5710 bytes 39bf42f9
- 005a5a34 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 005a5a34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5a34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5a34 ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 005a5a34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5a34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5a34 bytes 08c13591
+ 005a5a34 bytes 08013791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb8aa3d06f3c868d235f95b0b6d56f60"></a>

### [`005a74e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a74e4.md) → [`005a74e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a74e4.md) FUN_005a74e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 1件 [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.86% / 新版 87.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a7610",
      "incomplete_value": true,
      "site": "005a7620",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:9d4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7610",
      "incomplete_value": true,
      "site": "005a7620",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:a61:8"
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
      "definition_site": "005a7624",
      "incomplete_value": true,
      "site": "005a7624",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005a7624",
      "incomplete_value": true,
      "site": "005a7624",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005a7764",
      "incomplete_value": false,
      "site": "005a7764",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "005a7764",
      "incomplete_value": false,
      "site": "005a7764",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
    "ordinal": 40,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a75c4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "005a7610",
      "READ",
      [
        "storage",
        "00292a61",
        null,
        "string"
      ]
    ],
    [
      "005a7614",
      "READ",
      [
        "storage",
        "00292a6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a75c4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "005a7610",
      "READ",
      [
        "storage",
        "002929d4",
        null,
        "string"
      ]
    ],
    [
      "005a7614",
      "READ",
      [
        "storage",
        "002929e1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a75c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a74e4.md#insn-005a75c0) · [`005a7608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a74e4.md#insn-005a7608) · [`005a762c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a74e4.md#insn-005a762c)
- 新版 [`005a75c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a74e4.md#insn-005a75c0) · [`005a7608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a74e4.md#insn-005a7608) · [`005a762c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a74e4.md#insn-005a762c)

~~~diff
- 005a75c0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 005a75c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a75c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a75c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a75c0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 005a75c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a75c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a75c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a75c0 bytes 08e10091
+ 005a75c0 bytes 08e10191
- 005a7608 ["COPY", "tmp:0:8", ["const:a61:8"]]
- 005a7608 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a7608 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a7608 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a7608 ["COPY", "tmp:0:8", ["const:9d4:8"]]
+ 005a7608 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7608 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7608 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a7608 bytes 29852991
+ 005a7608 bytes 29512791
- 005a762c ["COPY", "tmp:0:8", ["const:0:8"]]
- 005a762c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005a762c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005a762c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005a762c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 005a762c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005a762c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005a762c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005a762c bytes 00000091
+ 005a762c bytes 00000191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-033c395f5544270de488319ea8fd65b0"></a>

### [`005a7844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7844.md) → [`005a7844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7844.md) FUN_005a7844

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 4件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 2件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 4件 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a78ac",
      "incomplete_value": true,
      "site": "005a78ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a78ac",
      "incomplete_value": true,
      "site": "005a78ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005a786c",
      "DATA",
      [
        "storage",
        "00c0bd40",
        null,
        "undefined *"
      ]
    ],
    [
      "005a78a4",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "005a78ac",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a786c",
      "DATA",
      [
        "storage",
        "00c0bd90",
        null,
        "undefined *"
      ]
    ],
    [
      "005a78a4",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ],
    [
      "005a78ac",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7844.md#insn-005a7860) · [`005a78a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7844.md#insn-005a78a4)
- 新版 [`005a7860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7844.md#insn-005a7860) · [`005a78a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7844.md#insn-005a78a4)

~~~diff
- 005a7860 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 005a7860 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7860 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7860 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7860 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 005a7860 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7860 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7860 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7860 bytes 08c13491
+ 005a7860 bytes 08013691
- 005a78a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
- 005a78a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a78a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
+ 005a78a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a78a4 bytes 089142f9
+ 005a78a4 bytes 08b942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c5d8365829330498cf9a55758b6ccd1"></a>

### [`005a7ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7ff8.md) → [`005a7ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7ff8.md) FUN_005a7ff8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`006525c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00652/006525c0.md) [`00686590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686590.md) [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) [`008f06a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f0/008f06a0.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 7件 [`006525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00652/006525c0.md) [`00686590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686590.md) [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`008e0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e0/008e0bc0.md) [`008f06a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f0/008f06a0.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a80e8",
      "incomplete_value": true,
      "site": "005a80e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:764:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a80e8",
      "incomplete_value": true,
      "site": "005a80e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d9:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a814c",
      "incomplete_value": false,
      "site": "005a814c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a814c",
      "incomplete_value": false,
      "site": "005a814c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a8104",
      "incomplete_value": false,
      "site": "005a8114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:a39:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8104",
      "incomplete_value": false,
      "site": "005a8114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:ac6:8"
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
      "005a8070",
      "READ",
      [
        "storage",
        "002a978d",
        null,
        "string"
      ]
    ],
    [
      "005a8074",
      "READ",
      [
        "storage",
        "002a9797",
        null,
        "string"
      ]
    ],
    [
      "005a80d8",
      "READ",
      [
        "storage",
        "002a46d9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a8070",
      "READ",
      [
        "storage",
        "002a979c",
        null,
        "string"
      ]
    ],
    [
      "005a8074",
      "READ",
      [
        "storage",
        "002a97a6",
        null,
        "string"
      ]
    ],
    [
      "005a80d8",
      "READ",
      [
        "storage",
        "002a4764",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7ff8.md#insn-005a8068) · [`005a80d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7ff8.md#insn-005a80d4) · [`005a8104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7ff8.md#insn-005a8104)
- 新版 [`005a8068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7ff8.md#insn-005a8068) · [`005a80d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7ff8.md#insn-005a80d4) · [`005a8104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7ff8.md#insn-005a8104)

~~~diff
- 005a8068 ["COPY", "tmp:0:8", ["const:78d:8"]]
- 005a8068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a8068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a8068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a8068 ["COPY", "tmp:0:8", ["const:79c:8"]]
+ 005a8068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a8068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a8068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a8068 bytes 08351e91
+ 005a8068 bytes 08711e91
- 005a80d4 ["COPY", "tmp:0:8", ["const:6d9:8"]]
- 005a80d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a80d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a80d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a80d4 ["COPY", "tmp:0:8", ["const:764:8"]]
+ 005a80d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a80d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a80d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a80d4 bytes 08651b91
+ 005a80d4 bytes 08911d91
- 005a8104 ["COPY", "tmp:0:8", ["const:ac6:8"]]
- 005a8104 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005a8104 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005a8104 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005a8104 ["COPY", "tmp:0:8", ["const:a39:8"]]
+ 005a8104 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005a8104 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005a8104 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005a8104 bytes 21182b91
+ 005a8104 bytes 21e42891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d81232cb197dc426e30522470659ca14"></a>

### [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md) → [`005a83e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a83e4.md) FUN_005a83e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 48件 [`005a7ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7ff8.md) [`005b6778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6778.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`005e53dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e5/005e53dc.md) [`005e8d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e8d4c.md) · 呼出先 14件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00470ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470ef0.md) [`005a8954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8954.md) [`005b0f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0f54.md)
- 新版 呼出元 48件 [`005a7ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7ff8.md) [`005b6778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6778.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`005e53dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e5/005e53dc.md) [`005e8d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e8/005e8d4c.md) · 呼出先 14件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00470ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470ef0.md) [`005a8954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8954.md) [`005b0f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0f54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.57% / 新版 99.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a841c",
      "incomplete_value": false,
      "site": "005a8430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:d3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a841c",
      "incomplete_value": false,
      "site": "005a8430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:dcb:8"
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
      "005a841c",
      "PARAM",
      [
        "storage",
        "00297dcb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a841c",
      "PARAM",
      [
        "storage",
        "00297d3e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a841c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md#insn-005a841c)
- 新版 [`005a841c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a83e4.md#insn-005a841c)

~~~diff
- 005a841c ["COPY", "tmp:0:8", ["const:dcb:8"]]
- 005a841c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005a841c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005a841c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005a841c ["COPY", "tmp:0:8", ["const:d3e:8"]]
+ 005a841c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005a841c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005a841c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005a841c bytes 212c3791
+ 005a841c bytes 21f83491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5f6aac42ce215a24aab205bda12099a"></a>

### [`005a8954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8954.md) → [`005a8954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8954.md) FUN_005a8954

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md) [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) · 呼出先 8件 [`005a8a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8a5c.md) [`005a8aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8aac.md) [`005a8df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8df0.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 2件 [`005a83e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a83e4.md) [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 8件 [`005a8a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8a5c.md) [`005a8aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md) [`005a8df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8df0.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a897c",
      "incomplete_value": true,
      "site": "005a8980",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a897c",
      "incomplete_value": true,
      "site": "005a8980",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:df0:8"
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
      "definition_site": "005a8990",
      "incomplete_value": true,
      "site": "005a8994",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8990",
      "incomplete_value": true,
      "site": "005a8994",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:530:8"
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
      "005a897c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "005a897c",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005a8990",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a897c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "005a897c",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005a8990",
      "READ",
      [
        "storage",
        "00c1b580",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a897c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8954.md#insn-005a897c) · [`005a8990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8954.md#insn-005a8990)
- 新版 [`005a897c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8954.md#insn-005a897c) · [`005a8990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8954.md#insn-005a8990)

~~~diff
- 005a897c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 005a897c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a897c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 005a897c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005a897c bytes 21f846f9
+ 005a897c bytes 212047f9
- 005a8990 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:530:8"]]
- 005a8990 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8990 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:580:8"]]
+ 005a8990 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8990 bytes 219842f9
+ 005a8990 bytes 21c042f9
~~~


<a id="compare-9c930983e39156eb425d7364d24d9816"></a>

### [`005a8aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8aac.md) → [`005a8aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md) FUN_005a8aac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005a8954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8954.md) [`005a98f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a98f4.md) · 呼出先 11件 [`005a8ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8ff4.md) [`005a9180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9180.md) [`005a92f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a92f4.md) [`005a94a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a94a8.md) [`005a965c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a965c.md)
- 新版 呼出元 2件 [`005a8954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8954.md) [`005a98f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md) · 呼出先 11件 [`005a8ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8ff4.md) [`005a9180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9180.md) [`005a92f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a92f4.md) [`005a94a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a94a8.md) [`005a965c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a965c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a8ae8",
      "incomplete_value": true,
      "site": "005a8aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a8ae8",
      "incomplete_value": true,
      "site": "005a8aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a8b08",
      "incomplete_value": true,
      "site": "005a8b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a8b08",
      "incomplete_value": true,
      "site": "005a8b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "005a8dbc",
      "incomplete_value": true,
      "site": "005a8dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a8dbc",
      "incomplete_value": true,
      "site": "005a8dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a8ae4",
      "READ",
      [
        "storage",
        "00c1b538",
        null,
        "pointer"
      ]
    ],
    [
      "005a8aec",
      "DATA",
      [
        "storage",
        "00bf3620",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005a8b00",
      "READ",
      [
        "storage",
        "00c1b540",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a8ae4",
      "READ",
      [
        "storage",
        "00c1b588",
        null,
        "pointer"
      ]
    ],
    [
      "005a8aec",
      "DATA",
      [
        "storage",
        "00bf3670",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005a8b00",
      "READ",
      [
        "storage",
        "00c1b590",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8aac.md#insn-005a8ae4) · [`005a8b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8aac.md#insn-005a8b00) · [`005a8b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8aac.md#insn-005a8b18)
- 新版 [`005a8ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md#insn-005a8ae4) · [`005a8b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md#insn-005a8b00) · [`005a8b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md#insn-005a8b18)

~~~diff
- 005a8ae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:538:8"]]
- 005a8ae4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8ae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:588:8"]]
+ 005a8ae4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8ae4 bytes 089d42f9
+ 005a8ae4 bytes 08c542f9
- 005a8b00 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:540:8"]]
- 005a8b00 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8b00 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:590:8"]]
+ 005a8b00 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8b00 bytes 18a342f9
+ 005a8b00 bytes 18cb42f9
- 005a8b18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:548:8"]]
- 005a8b18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8b18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:598:8"]]
+ 005a8b18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8b18 bytes 08a542f9
+ 005a8b18 bytes 08cd42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f9dc0a8484f57930971fd3adb2cdd94"></a>

### [`005a8df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8df0.md) → [`005a8df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8df0.md) FUN_005a8df0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005a8954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8954.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 1件 [`005a8954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8954.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005a8e1c",
      "incomplete_value": true,
      "site": "005a8e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8e1c",
      "incomplete_value": true,
      "site": "005a8e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "005a8e20",
      "incomplete_value": true,
      "site": "005a8e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8e20",
      "incomplete_value": true,
      "site": "005a8e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005a8e1c",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005a8e1c",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a8e20",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a8e1c",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005a8e1c",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a8e20",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8df0.md#insn-005a8e1c) · [`005a8e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8df0.md#insn-005a8e20)
- 新版 [`005a8e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8df0.md#insn-005a8e1c) · [`005a8e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8df0.md#insn-005a8e20)

~~~diff
- 005a8e1c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005a8e1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8e1c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005a8e1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8e1c bytes 21b442f9
+ 005a8e1c bytes 21dc42f9
- 005a8e20 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005a8e20 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8e20 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005a8e20 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8e20 bytes 42b842f9
+ 005a8e20 bytes 42e042f9
~~~


<a id="compare-2a1b08366c8243a9cb03caee41e2dd92"></a>

### [`005a965c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a965c.md) → [`005a965c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a965c.md) FUN_005a965c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005a8aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8aac.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 1件 [`005a8aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005a9688",
      "incomplete_value": true,
      "site": "005a9690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9688",
      "incomplete_value": true,
      "site": "005a9690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "005a968c",
      "incomplete_value": true,
      "site": "005a9690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a968c",
      "incomplete_value": true,
      "site": "005a9690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005a9688",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005a9688",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a968c",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a9688",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005a9688",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a968c",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a965c.md#insn-005a9688) · [`005a968c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a965c.md#insn-005a968c)
- 新版 [`005a9688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a965c.md#insn-005a9688) · [`005a968c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a965c.md#insn-005a968c)

~~~diff
- 005a9688 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005a9688 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9688 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005a9688 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9688 bytes 21b442f9
+ 005a9688 bytes 21dc42f9
- 005a968c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005a968c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a968c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005a968c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005a968c bytes 42b842f9
+ 005a968c bytes 42e042f9
~~~


<a id="compare-dd114fb9ef63a1ee3c6e6024543900fd"></a>

### [`005a98f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a98f4.md) → [`005a98f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md) FUN_005a98f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005a97c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a97c0.md) [`005a9860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9860.md) · 呼出先 8件 [`005a8a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8a0c.md) [`005a8aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8aac.md) [`005aa270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa270.md) [`005aa2dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa2dc.md) [`005aa390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa390.md)
- 新版 呼出元 2件 [`005a97c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a97c0.md) [`005a9860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9860.md) · 呼出先 8件 [`005a8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8a0c.md) [`005a8aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8aac.md) [`005aa270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa270.md) [`005aa2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa2dc.md) [`005aa390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa390.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.59% / 新版 96.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a9b04",
      "incomplete_value": true,
      "site": "005a9b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a9b04",
      "incomplete_value": true,
      "site": "005a9b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a9a24",
      "READ",
      [
        "storage",
        "00c1b578",
        null,
        "pointer"
      ]
    ],
    [
      "005a9a50",
      "READ",
      [
        "storage",
        "00c1b580",
        null,
        "pointer"
      ]
    ],
    [
      "005a9a74",
      "DATA",
      [
        "storage",
        "00bf37b8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005a9a24",
      "READ",
      [
        "storage",
        "00c1b5c8",
        null,
        "pointer"
      ]
    ],
    [
      "005a9a50",
      "READ",
      [
        "storage",
        "00c1b5d0",
        null,
        "pointer"
      ]
    ],
    [
      "005a9a74",
      "DATA",
      [
        "storage",
        "00bf3808",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a98f4.md#insn-005a9a24) · [`005a9a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a98f4.md#insn-005a9a50) · [`005a9af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a98f4.md#insn-005a9af4)
- 新版 [`005a9a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md#insn-005a9a24) · [`005a9a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md#insn-005a9a50) · [`005a9af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md#insn-005a9af4)

~~~diff
- 005a9a24 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:578:8"]]
- 005a9a24 ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9a24 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:5c8:8"]]
+ 005a9a24 ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9a24 bytes 6bbd42f9
+ 005a9a24 bytes 6be542f9
- 005a9a50 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:580:8"]]
- 005a9a50 ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9a50 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:5d0:8"]]
+ 005a9a50 ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9a50 bytes 6bc142f9
+ 005a9a50 bytes 6be942f9
- 005a9af4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:590:8"]]
- 005a9af4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9af4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5e0:8"]]
+ 005a9af4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9af4 bytes 29c942f9
+ 005a9af4 bytes 29f142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd4b087a53f129c5cbdcbd4180a6b3ac"></a>

### [`005a9c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9c58.md) → [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) FUN_005a9c58

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a97c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a97c0.md) [`005a9860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9860.md) · 呼出先 10件 [`005a8e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8e3c.md) [`005aa390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa390.md) [`005ab944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab944.md) [`005aba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005aba98.md) [`005abae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abae4.md)
- 新版 呼出元 2件 [`005a97c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a97c0.md) [`005a9860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9860.md) · 呼出先 10件 [`005a8e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8e3c.md) [`005aa390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa390.md) [`005ab944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab944.md) [`005aba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005aba98.md) [`005abae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abae4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a9cb0",
      "incomplete_value": true,
      "site": "005a9cc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a9cb0",
      "incomplete_value": true,
      "site": "005a9cc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a9e04",
      "incomplete_value": true,
      "site": "005a9e1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a9e04",
      "incomplete_value": true,
      "site": "005a9e1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a9eb0",
      "incomplete_value": true,
      "site": "005a9ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005a9eb0",
      "incomplete_value": true,
      "site": "005a9ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "005a9ca8",
      "READ",
      [
        "storage",
        "00c1b598",
        null,
        "pointer"
      ]
    ],
    [
      "005a9cc0",
      "DATA",
      [
        "storage",
        "00bf3890",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005a9df0",
      "READ",
      [
        "storage",
        "00c1b5a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a9ca8",
      "READ",
      [
        "storage",
        "00c1b5e8",
        null,
        "pointer"
      ]
    ],
    [
      "005a9cc0",
      "DATA",
      [
        "storage",
        "00bf38e0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005a9df0",
      "READ",
      [
        "storage",
        "00c1b5f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9c58.md#insn-005a9ca8) · [`005a9df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9c58.md#insn-005a9df0) · [`005a9ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9c58.md#insn-005a9ea4)
- 新版 [`005a9ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md#insn-005a9ca8) · [`005a9df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md#insn-005a9df0) · [`005a9ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md#insn-005a9ea4)

~~~diff
- 005a9ca8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:598:8"]]
- 005a9ca8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9ca8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5e8:8"]]
+ 005a9ca8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9ca8 bytes 29cd42f9
+ 005a9ca8 bytes 29f542f9
- 005a9df0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:5a0:8"]]
- 005a9df0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9df0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:5f0:8"]]
+ 005a9df0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9df0 bytes 4ad142f9
+ 005a9df0 bytes 4af942f9
- 005a9ea4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5a8:8"]]
- 005a9ea4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9ea4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5f8:8"]]
+ 005a9ea4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9ea4 bytes 29d542f9
+ 005a9ea4 bytes 29fd42f9
~~~


<a id="compare-c1de27bfb8eacf7792dae0469c528c9c"></a>

### [`005aa270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa270.md) → [`005aa270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa270.md) FUN_005aa270

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005a98f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a98f4.md) · 呼出先 2件 [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd900.md)
- 新版 呼出元 1件 [`005a98f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md) · 呼出先 2件 [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdd950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd950.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005aa28c",
      "incomplete_value": true,
      "site": "005aa290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa28c",
      "incomplete_value": true,
      "site": "005aa290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
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
      "definition_site": "005aa2a0",
      "incomplete_value": true,
      "site": "005aa2a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa2a0",
      "incomplete_value": true,
      "site": "005aa2a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
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
      "005aa28c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "005aa28c",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005aa2a0",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa28c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "005aa28c",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005aa2a0",
      "READ",
      [
        "storage",
        "00c1b580",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa270.md#insn-005aa28c) · [`005aa2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa270.md#insn-005aa2a0)
- 新版 [`005aa28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa270.md#insn-005aa28c) · [`005aa2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa270.md#insn-005aa2a0)

~~~diff
- 005aa28c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 005aa28c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa28c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 005aa28c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa28c bytes 21f846f9
+ 005aa28c bytes 212047f9
- 005aa2a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:530:8"]]
- 005aa2a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa2a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:580:8"]]
+ 005aa2a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa2a0 bytes 219842f9
+ 005aa2a0 bytes 21c042f9
~~~


<a id="compare-983d4b3bb1d5ae207cff9eefddd6fc81"></a>

### [`005aa390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa390.md) → [`005aa390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa390.md) FUN_005aa390

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005a98f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a98f4.md) [`005a9c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9c58.md) [`005b04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md) [`005b0b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0b60.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 4件 [`005a98f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md) [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) [`005b04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md) [`005b0b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b60.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005aa3bc",
      "incomplete_value": true,
      "site": "005aa3c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa3bc",
      "incomplete_value": true,
      "site": "005aa3c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:568:8"
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
      "definition_site": "005aa3c0",
      "incomplete_value": true,
      "site": "005aa3c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa3c0",
      "incomplete_value": true,
      "site": "005aa3c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005aa3bc",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005aa3bc",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005aa3c0",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa3bc",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005aa3bc",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005aa3c0",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa390.md#insn-005aa3bc) · [`005aa3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa390.md#insn-005aa3c0)
- 新版 [`005aa3bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa390.md#insn-005aa3bc) · [`005aa3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa390.md#insn-005aa3c0)

~~~diff
- 005aa3bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005aa3bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa3bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005aa3bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa3bc bytes 21b442f9
+ 005aa3bc bytes 21dc42f9
- 005aa3c0 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005aa3c0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa3c0 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005aa3c0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa3c0 bytes 42b842f9
+ 005aa3c0 bytes 42e042f9
~~~


<a id="compare-3076f9e6c3614a42f419b2375de5dd0c"></a>

### [`005aa51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa51c.md) → [`005aa51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa51c.md) FUN_005aa51c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

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
      "definition_site": "005aa538",
      "incomplete_value": true,
      "site": "005aa538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005aa538",
      "incomplete_value": true,
      "site": "005aa538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005aa530",
      "READ",
      [
        "storage",
        "00c1b590",
        null,
        "pointer"
      ]
    ],
    [
      "005aa538",
      "DATA",
      [
        "storage",
        "00bf3800",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa544",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa530",
      "READ",
      [
        "storage",
        "00c1b5e0",
        null,
        "pointer"
      ]
    ],
    [
      "005aa538",
      "DATA",
      [
        "storage",
        "00bf3850",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa544",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa51c.md#insn-005aa530) · [`005aa544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa51c.md#insn-005aa544)
- 新版 [`005aa530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa51c.md#insn-005aa530) · [`005aa544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa51c.md#insn-005aa544)

~~~diff
- 005aa530 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:590:8"]]
- 005aa530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa530 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5e0:8"]]
+ 005aa530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa530 bytes 08c942f9
+ 005aa530 bytes 08f142f9
- 005aa544 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005aa544 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa544 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005aa544 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa544 bytes 08b142f9
+ 005aa544 bytes 08d942f9
~~~


<a id="compare-27a625a9911d9dfd38e298f3a874e89e"></a>

### [`005aa578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa578.md) → [`005aa578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa578.md) FUN_005aa578

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005aa594",
      "incomplete_value": true,
      "site": "005aa594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005aa594",
      "incomplete_value": true,
      "site": "005aa594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005aa5a8",
      "incomplete_value": true,
      "site": "005aa5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005aa5a8",
      "incomplete_value": true,
      "site": "005aa5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005aa58c",
      "READ",
      [
        "storage",
        "00c1b590",
        null,
        "pointer"
      ]
    ],
    [
      "005aa594",
      "DATA",
      [
        "storage",
        "00bf3800",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa5a0",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa58c",
      "READ",
      [
        "storage",
        "00c1b5e0",
        null,
        "pointer"
      ]
    ],
    [
      "005aa594",
      "DATA",
      [
        "storage",
        "00bf3850",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa5a0",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa578.md#insn-005aa58c) · [`005aa5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa578.md#insn-005aa5a0)
- 新版 [`005aa58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa578.md#insn-005aa58c) · [`005aa5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa578.md#insn-005aa5a0)

~~~diff
- 005aa58c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:590:8"]]
- 005aa58c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa58c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5e0:8"]]
+ 005aa58c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa58c bytes 08c942f9
+ 005aa58c bytes 08f142f9
- 005aa5a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005aa5a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa5a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005aa5a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa5a0 bytes 08b142f9
+ 005aa5a0 bytes 08d942f9
~~~


<a id="compare-e8f523f1696daa03e204269e6b2f2ba3"></a>

### [`005aa6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa6e0.md) → [`005aa6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa6e0.md) FUN_005aa6e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

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
      "definition_site": "005aa6fc",
      "incomplete_value": true,
      "site": "005aa700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005aa6fc",
      "incomplete_value": true,
      "site": "005aa700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005aa744",
      "incomplete_value": true,
      "site": "005aa748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005aa744",
      "incomplete_value": true,
      "site": "005aa748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005aa6f4",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "005aa700",
      "DATA",
      [
        "storage",
        "00bf3848",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa73c",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa6f4",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "005aa700",
      "DATA",
      [
        "storage",
        "00bf3898",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa73c",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa6e0.md#insn-005aa6f4) · [`005aa73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa6e0.md#insn-005aa73c)
- 新版 [`005aa6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa6e0.md#insn-005aa6f4) · [`005aa73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa6e0.md#insn-005aa73c)

~~~diff
- 005aa6f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
- 005aa6f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa6f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
+ 005aa6f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa6f4 bytes 08d942f9
+ 005aa6f4 bytes 080143f9
- 005aa73c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005aa73c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa73c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005aa73c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa73c bytes 08b142f9
+ 005aa73c bytes 08d942f9
~~~


<a id="compare-1f30f7b1ef0102a9c41af73a0f2d0114"></a>

### [`005aa770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa770.md) → [`005aa770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa770.md) FUN_005aa770

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

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
      "definition_site": "005aa78c",
      "incomplete_value": true,
      "site": "005aa790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005aa78c",
      "incomplete_value": true,
      "site": "005aa790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005aa7d4",
      "incomplete_value": true,
      "site": "005aa7d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005aa7d4",
      "incomplete_value": true,
      "site": "005aa7d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005aa784",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "005aa790",
      "DATA",
      [
        "storage",
        "00bf3848",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa7cc",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa784",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "005aa790",
      "DATA",
      [
        "storage",
        "00bf3898",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa7cc",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa770.md#insn-005aa784) · [`005aa7cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa770.md#insn-005aa7cc)
- 新版 [`005aa784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa770.md#insn-005aa784) · [`005aa7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa770.md#insn-005aa7cc)

~~~diff
- 005aa784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
- 005aa784 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
+ 005aa784 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa784 bytes 08d942f9
+ 005aa784 bytes 080143f9
- 005aa7cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005aa7cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa7cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005aa7cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa7cc bytes 08b142f9
+ 005aa7cc bytes 08d942f9
~~~


<a id="compare-db5af37d4507d9dc2b6a87cdac9e3712"></a>

### [`005aaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aaff0.md) → [`005aaff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aaff0.md) FUN_005aaff0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005aae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aae28.md) [`005ab094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab094.md) [`005ab678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab678.md) [`005b3380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3380.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 4件 [`005aae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aae28.md) [`005ab094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab094.md) [`005ab678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab678.md) [`005b3380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3380.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005aaffc",
      "incomplete_value": false,
      "site": "005ab000",
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
      "definition_site": "005aaffc",
      "incomplete_value": false,
      "site": "005ab000",
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
      "005aaffc",
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
      "005aaffc",
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

- 旧版 [`005aaffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aaff0.md#insn-005aaffc)
- 新版 [`005aaffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aaff0.md#insn-005aaffc)

~~~diff
- 005aaffc ["COPY", "tmp:0:8", ["const:303:8"]]
- 005aaffc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005aaffc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005aaffc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005aaffc ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005aaffc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005aaffc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005aaffc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005aaffc bytes 000c0c91
+ 005aaffc bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1edbc9db6e0238a54611615a44f171a9"></a>

### [`005ab048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab048.md) → [`005ab048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab048.md) FUN_005ab048

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005aa9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa9b4.md) [`005b1404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b1/005b1404.md) [`005b1ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b1/005b1ce4.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 3件 [`005aa9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md) [`005b1404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md) [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005ab074",
      "incomplete_value": true,
      "site": "005ab07c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab074",
      "incomplete_value": true,
      "site": "005ab07c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:568:8"
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
      "definition_site": "005ab078",
      "incomplete_value": true,
      "site": "005ab07c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
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
    "old": {
      "definition_site": "005ab078",
      "incomplete_value": true,
      "site": "005ab07c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:570:8"
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
      "005ab074",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005ab074",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ab078",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ab074",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005ab074",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ab078",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab048.md#insn-005ab074) · [`005ab078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab048.md#insn-005ab078)
- 新版 [`005ab074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab048.md#insn-005ab074) · [`005ab078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab048.md#insn-005ab078)

~~~diff
- 005ab074 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005ab074 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ab074 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005ab074 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005ab074 bytes 21b442f9
+ 005ab074 bytes 21dc42f9
- 005ab078 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005ab078 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ab078 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005ab078 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005ab078 bytes 42b842f9
+ 005ab078 bytes 42e042f9
~~~


<a id="compare-47567f64a6155f81f1cdfdfe3707da7b"></a>

### [`005ab20c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab20c.md) → [`005ab20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab20c.md) FUN_005ab20c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005aa9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa9b4.md) [`005b1404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b1/005b1404.md) [`005b1ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b1/005b1ce4.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 3件 [`005aa9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md) [`005b1404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md) [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005ab23c",
      "incomplete_value": true,
      "site": "005ab240",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
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
    "old": {
      "definition_site": "005ab23c",
      "incomplete_value": true,
      "site": "005ab240",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:570:8"
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
      "005ab238",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005ab238",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ab23c",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ab238",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005ab238",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ab23c",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab20c.md#insn-005ab238) · [`005ab23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab20c.md#insn-005ab23c)
- 新版 [`005ab238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab20c.md#insn-005ab238) · [`005ab23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab20c.md#insn-005ab23c)

~~~diff
- 005ab238 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005ab238 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ab238 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005ab238 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005ab238 bytes 21b442f9
+ 005ab238 bytes 21dc42f9
- 005ab23c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005ab23c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ab23c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005ab23c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005ab23c bytes 42b842f9
+ 005ab23c bytes 42e042f9
~~~


<a id="compare-1b85519d08837f5e32cba2dbefedf596"></a>

### [`005ab664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab664.md) → [`005ab664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab664.md) FUN_005ab664

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005ab2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab2e0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005ab2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab2e0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005ab670",
      "incomplete_value": false,
      "site": "005ab674",
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
      "definition_site": "005ab670",
      "incomplete_value": false,
      "site": "005ab674",
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
      "005ab670",
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
      "005ab670",
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

- 旧版 [`005ab670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab664.md#insn-005ab670)
- 新版 [`005ab670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab664.md#insn-005ab670)

~~~diff
- 005ab670 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005ab670 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005ab670 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005ab670 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005ab670 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005ab670 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005ab670 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005ab670 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005ab670 bytes 000c0c91
+ 005ab670 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eac181c9759b5b38c7978eedc96e2f44"></a>

### [`005ab930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab930.md) → [`005ab930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab930.md) FUN_005ab930

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005ab094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab094.md) [`005ab804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab804.md) [`005b356c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b356c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`005ab094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab094.md) [`005ab804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab804.md) [`005b356c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b356c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005ab93c",
      "incomplete_value": false,
      "site": "005ab940",
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
      "definition_site": "005ab93c",
      "incomplete_value": false,
      "site": "005ab940",
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
      "005ab93c",
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
      "005ab93c",
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

- 旧版 [`005ab93c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab930.md#insn-005ab93c)
- 新版 [`005ab93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab930.md#insn-005ab93c)

~~~diff
- 005ab93c ["COPY", "tmp:0:8", ["const:303:8"]]
- 005ab93c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005ab93c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005ab93c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005ab93c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005ab93c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005ab93c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005ab93c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005ab93c bytes 000c0c91
+ 005ab93c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9d8f1636c42378c1f5d18a87c256753"></a>

### [`005aba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005aba98.md) → [`005aba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005aba98.md) FUN_005aba98

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005a9c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9c58.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 1件 [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005abac4",
      "incomplete_value": true,
      "site": "005abacc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abac4",
      "incomplete_value": true,
      "site": "005abacc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:568:8"
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
      "definition_site": "005abac8",
      "incomplete_value": true,
      "site": "005abacc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abac8",
      "incomplete_value": true,
      "site": "005abacc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005abac4",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005abac4",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005abac8",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005abac4",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005abac4",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005abac8",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005abac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005aba98.md#insn-005abac4) · [`005abac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005aba98.md#insn-005abac8)
- 新版 [`005abac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005aba98.md#insn-005abac4) · [`005abac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005aba98.md#insn-005abac8)

~~~diff
- 005abac4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005abac4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005abac4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005abac4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005abac4 bytes 21b442f9
+ 005abac4 bytes 21dc42f9
- 005abac8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005abac8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005abac8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005abac8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005abac8 bytes 42b842f9
+ 005abac8 bytes 42e042f9
~~~


<a id="compare-cfe65b7723e8c6b0325b20c8fad70767"></a>

### [`005abb94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abb94.md) → [`005abb94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abb94.md) FUN_005abb94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005a9c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9c58.md) [`005abeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abeac.md) [`005ae770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae770.md) [`005ae894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae894.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 4件 [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) [`005abeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abeac.md) [`005ae770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae770.md) [`005ae894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae894.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005abbc0",
      "incomplete_value": true,
      "site": "005abbc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abbc0",
      "incomplete_value": true,
      "site": "005abbc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "005abbc4",
      "incomplete_value": true,
      "site": "005abbc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abbc4",
      "incomplete_value": true,
      "site": "005abbc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005abbc0",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005abbc0",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005abbc4",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005abbc0",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005abbc0",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005abbc4",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005abbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abb94.md#insn-005abbc0) · [`005abbc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abb94.md#insn-005abbc4)
- 新版 [`005abbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abb94.md#insn-005abbc0) · [`005abbc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abb94.md#insn-005abbc4)

~~~diff
- 005abbc0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005abbc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005abbc0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005abbc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005abbc0 bytes 21b442f9
+ 005abbc0 bytes 21dc42f9
- 005abbc4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005abbc4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005abbc4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005abbc4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005abbc4 bytes 42b842f9
+ 005abbc4 bytes 42e042f9
~~~


<a id="compare-faeda4f70f12f18affc546da3b9d1a85"></a>

### [`005ac1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac1ac.md) → [`005ac1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md) FUN_005ac1ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`005abae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abae4.md) [`005abbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abbe0.md) [`005abeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abeac.md) [`005ae894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae894.md) [`005b093c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b093c.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md)
- 新版 呼出元 7件 [`005abae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abae4.md) [`005abbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abbe0.md) [`005abeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abeac.md) [`005ae894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae894.md) [`005b093c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b093c.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ac1f0",
      "incomplete_value": true,
      "site": "005ac1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac1f0",
      "incomplete_value": true,
      "site": "005ac1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac220",
      "incomplete_value": true,
      "site": "005ac220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac220",
      "incomplete_value": true,
      "site": "005ac220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac274",
      "incomplete_value": true,
      "site": "005ac274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac274",
      "incomplete_value": true,
      "site": "005ac274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "005ac1e0",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac1f0",
      "DATA",
      [
        "storage",
        "00bf3968",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac210",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac1e0",
      "READ",
      [
        "storage",
        "00c1b608",
        null,
        "pointer"
      ]
    ],
    [
      "005ac1f0",
      "DATA",
      [
        "storage",
        "00bf39b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac210",
      "READ",
      [
        "storage",
        "00c1b610",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac1ac.md#insn-005ac1e0) · [`005ac210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac1ac.md#insn-005ac210) · [`005ac264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac1ac.md#insn-005ac264)
- 新版 [`005ac1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md#insn-005ac1e0) · [`005ac210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md#insn-005ac210) · [`005ac264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md#insn-005ac264)

~~~diff
- 005ac1e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5b8:8"]]
- 005ac1e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac1e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:608:8"]]
+ 005ac1e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac1e0 bytes 29dd42f9
+ 005ac1e0 bytes 290543f9
- 005ac210 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5c0:8"]]
- 005ac210 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac210 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:610:8"]]
+ 005ac210 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac210 bytes 29e142f9
+ 005ac210 bytes 290943f9
- 005ac264 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5c8:8"]]
- 005ac264 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac264 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:618:8"]]
+ 005ac264 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac264 bytes 29e542f9
+ 005ac264 bytes 290d43f9
~~~


<a id="compare-f1d952cfbb932de84d61c9b8920e22be"></a>

### [`005ac2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac2ec.md) → [`005ac2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac2ec.md) FUN_005ac2ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005abbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abbe0.md) [`005ac9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac9d8.md) [`005b04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md) [`005b0b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0b00.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 4件 [`005abbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abbe0.md) [`005ac9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac9d8.md) [`005b04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md) [`005b0b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b00.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005ac318",
      "incomplete_value": true,
      "site": "005ac320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac318",
      "incomplete_value": true,
      "site": "005ac320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "005ac31c",
      "incomplete_value": true,
      "site": "005ac320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac31c",
      "incomplete_value": true,
      "site": "005ac320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005ac318",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005ac318",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ac31c",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac318",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac318",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ac31c",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac2ec.md#insn-005ac318) · [`005ac31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac2ec.md#insn-005ac31c)
- 新版 [`005ac318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac2ec.md#insn-005ac318) · [`005ac31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac2ec.md#insn-005ac31c)

~~~diff
- 005ac318 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005ac318 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac318 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005ac318 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac318 bytes 21b442f9
+ 005ac318 bytes 21dc42f9
- 005ac31c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005ac31c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac31c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005ac31c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac31c bytes 42b842f9
+ 005ac31c bytes 42e042f9
~~~


<a id="compare-fcd492589a13aa6cb79357d9b2c03c44"></a>

### [`005ac400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac400.md) → [`005ac400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac400.md) FUN_005ac400

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005ac41c",
      "incomplete_value": true,
      "site": "005ac41c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac41c",
      "incomplete_value": true,
      "site": "005ac41c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac430",
      "incomplete_value": true,
      "site": "005ac434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac430",
      "incomplete_value": true,
      "site": "005ac434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005ac414",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ],
    [
      "005ac41c",
      "DATA",
      [
        "storage",
        "00bf38d8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac428",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac414",
      "READ",
      [
        "storage",
        "00c1b610",
        null,
        "pointer"
      ]
    ],
    [
      "005ac41c",
      "DATA",
      [
        "storage",
        "00bf3928",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac428",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac400.md#insn-005ac414) · [`005ac428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac400.md#insn-005ac428)
- 新版 [`005ac414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac400.md#insn-005ac414) · [`005ac428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac400.md#insn-005ac428)

~~~diff
- 005ac414 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
- 005ac414 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac414 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:610:8"]]
+ 005ac414 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac414 bytes 08e142f9
+ 005ac414 bytes 080943f9
- 005ac428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005ac428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005ac428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac428 bytes 08b142f9
+ 005ac428 bytes 08d942f9
~~~


<a id="compare-9859501aa22a6603c9c570f76c570699"></a>

### [`005ac45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac45c.md) → [`005ac45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac45c.md) FUN_005ac45c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005ac478",
      "incomplete_value": true,
      "site": "005ac478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac478",
      "incomplete_value": true,
      "site": "005ac478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac48c",
      "incomplete_value": true,
      "site": "005ac490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac48c",
      "incomplete_value": true,
      "site": "005ac490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005ac470",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ],
    [
      "005ac478",
      "DATA",
      [
        "storage",
        "00bf38d8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac484",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac470",
      "READ",
      [
        "storage",
        "00c1b610",
        null,
        "pointer"
      ]
    ],
    [
      "005ac478",
      "DATA",
      [
        "storage",
        "00bf3928",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac484",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac45c.md#insn-005ac470) · [`005ac484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac45c.md#insn-005ac484)
- 新版 [`005ac470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac45c.md#insn-005ac470) · [`005ac484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac45c.md#insn-005ac484)

~~~diff
- 005ac470 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
- 005ac470 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac470 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:610:8"]]
+ 005ac470 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac470 bytes 08e142f9
+ 005ac470 bytes 080943f9
- 005ac484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005ac484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005ac484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac484 bytes 08b142f9
+ 005ac484 bytes 08d942f9
~~~


<a id="compare-6766c906c318a3c703edb02f6a8184b4"></a>

### [`005ac52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac52c.md) → [`005ac52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac52c.md) FUN_005ac52c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005ac548",
      "incomplete_value": true,
      "site": "005ac548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac548",
      "incomplete_value": true,
      "site": "005ac548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac55c",
      "incomplete_value": true,
      "site": "005ac560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac55c",
      "incomplete_value": true,
      "site": "005ac560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005ac540",
      "READ",
      [
        "storage",
        "00c1b5c8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac548",
      "DATA",
      [
        "storage",
        "00bf3920",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac554",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac540",
      "READ",
      [
        "storage",
        "00c1b618",
        null,
        "pointer"
      ]
    ],
    [
      "005ac548",
      "DATA",
      [
        "storage",
        "00bf3970",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac554",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac52c.md#insn-005ac540) · [`005ac554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac52c.md#insn-005ac554)
- 新版 [`005ac540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac52c.md#insn-005ac540) · [`005ac554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac52c.md#insn-005ac554)

~~~diff
- 005ac540 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c8:8"]]
- 005ac540 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac540 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:618:8"]]
+ 005ac540 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac540 bytes 08e542f9
+ 005ac540 bytes 080d43f9
- 005ac554 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005ac554 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac554 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005ac554 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac554 bytes 08b142f9
+ 005ac554 bytes 08d942f9
~~~


<a id="compare-404a5d7e3e31d9b2841e9daf8e7e7f7b"></a>

### [`005ac588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac588.md) → [`005ac588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac588.md) FUN_005ac588

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005ac5a4",
      "incomplete_value": true,
      "site": "005ac5a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac5a4",
      "incomplete_value": true,
      "site": "005ac5a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac5b8",
      "incomplete_value": true,
      "site": "005ac5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac5b8",
      "incomplete_value": true,
      "site": "005ac5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005ac59c",
      "READ",
      [
        "storage",
        "00c1b5c8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac5a4",
      "DATA",
      [
        "storage",
        "00bf3920",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac5b0",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac59c",
      "READ",
      [
        "storage",
        "00c1b618",
        null,
        "pointer"
      ]
    ],
    [
      "005ac5a4",
      "DATA",
      [
        "storage",
        "00bf3970",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac5b0",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac588.md#insn-005ac59c) · [`005ac5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac588.md#insn-005ac5b0)
- 新版 [`005ac59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac588.md#insn-005ac59c) · [`005ac5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac588.md#insn-005ac5b0)

~~~diff
- 005ac59c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c8:8"]]
- 005ac59c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac59c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:618:8"]]
+ 005ac59c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac59c bytes 08e542f9
+ 005ac59c bytes 080d43f9
- 005ac5b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005ac5b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac5b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005ac5b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac5b0 bytes 08b142f9
+ 005ac5b0 bytes 08d942f9
~~~


<a id="compare-972b8b6dc07477daf0cc9cfa06de0887"></a>

### [`005ac6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac6b8.md) → [`005ac6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac6b8.md) FUN_005ac6b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005ac6d4",
      "incomplete_value": true,
      "site": "005ac6d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac6d4",
      "incomplete_value": true,
      "site": "005ac6d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac6e8",
      "incomplete_value": true,
      "site": "005ac6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac6e8",
      "incomplete_value": true,
      "site": "005ac6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005ac6cc",
      "READ",
      [
        "storage",
        "00c1b5d8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac6d4",
      "DATA",
      [
        "storage",
        "00bf39b0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac6e0",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac6cc",
      "READ",
      [
        "storage",
        "00c1b628",
        null,
        "pointer"
      ]
    ],
    [
      "005ac6d4",
      "DATA",
      [
        "storage",
        "00bf3a00",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac6e0",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac6cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac6b8.md#insn-005ac6cc) · [`005ac6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac6b8.md#insn-005ac6e0)
- 新版 [`005ac6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac6b8.md#insn-005ac6cc) · [`005ac6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac6b8.md#insn-005ac6e0)

~~~diff
- 005ac6cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5d8:8"]]
- 005ac6cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac6cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:628:8"]]
+ 005ac6cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac6cc bytes 08ed42f9
+ 005ac6cc bytes 081543f9
- 005ac6e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005ac6e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac6e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005ac6e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac6e0 bytes 08b142f9
+ 005ac6e0 bytes 08d942f9
~~~


<a id="compare-34c715a7f54c0fbee115b9c8f709264e"></a>

### [`005ac714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac714.md) → [`005ac714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac714.md) FUN_005ac714

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005ac730",
      "incomplete_value": true,
      "site": "005ac730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac730",
      "incomplete_value": true,
      "site": "005ac730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac744",
      "incomplete_value": true,
      "site": "005ac748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac744",
      "incomplete_value": true,
      "site": "005ac748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005ac728",
      "READ",
      [
        "storage",
        "00c1b5d8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac730",
      "DATA",
      [
        "storage",
        "00bf39b0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac73c",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac728",
      "READ",
      [
        "storage",
        "00c1b628",
        null,
        "pointer"
      ]
    ],
    [
      "005ac730",
      "DATA",
      [
        "storage",
        "00bf3a00",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac73c",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac714.md#insn-005ac728) · [`005ac73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac714.md#insn-005ac73c)
- 新版 [`005ac728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac714.md#insn-005ac728) · [`005ac73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac714.md#insn-005ac73c)

~~~diff
- 005ac728 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5d8:8"]]
- 005ac728 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac728 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:628:8"]]
+ 005ac728 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac728 bytes 08ed42f9
+ 005ac728 bytes 081543f9
- 005ac73c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005ac73c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac73c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005ac73c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac73c bytes 08b142f9
+ 005ac73c bytes 08d942f9
~~~


<a id="compare-3d9911550651e799aff02f1485128a23"></a>

### [`005ac854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac854.md) → [`005ac854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac854.md) FUN_005ac854

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005ac870",
      "incomplete_value": true,
      "site": "005ac870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac870",
      "incomplete_value": true,
      "site": "005ac870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac884",
      "incomplete_value": true,
      "site": "005ac888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac884",
      "incomplete_value": true,
      "site": "005ac888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005ac868",
      "READ",
      [
        "storage",
        "00c1b5e0",
        null,
        "pointer"
      ]
    ],
    [
      "005ac870",
      "DATA",
      [
        "storage",
        "00bf39f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac87c",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac868",
      "READ",
      [
        "storage",
        "00c1b630",
        null,
        "pointer"
      ]
    ],
    [
      "005ac870",
      "DATA",
      [
        "storage",
        "00bf3a48",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac87c",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac854.md#insn-005ac868) · [`005ac87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac854.md#insn-005ac87c)
- 新版 [`005ac868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac854.md#insn-005ac868) · [`005ac87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac854.md#insn-005ac87c)

~~~diff
- 005ac868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5e0:8"]]
- 005ac868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:630:8"]]
+ 005ac868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac868 bytes 08f142f9
+ 005ac868 bytes 081943f9
- 005ac87c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005ac87c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac87c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005ac87c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac87c bytes 08b142f9
+ 005ac87c bytes 08d942f9
~~~


<a id="compare-1f3459cade374b8222a827d3b2f94484"></a>

### [`005ac8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac8b0.md) → [`005ac8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac8b0.md) FUN_005ac8b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005ac8cc",
      "incomplete_value": true,
      "site": "005ac8cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac8cc",
      "incomplete_value": true,
      "site": "005ac8cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac8e0",
      "incomplete_value": true,
      "site": "005ac8e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ac8e0",
      "incomplete_value": true,
      "site": "005ac8e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005ac8c4",
      "READ",
      [
        "storage",
        "00c1b5e0",
        null,
        "pointer"
      ]
    ],
    [
      "005ac8cc",
      "DATA",
      [
        "storage",
        "00bf39f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac8d8",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac8c4",
      "READ",
      [
        "storage",
        "00c1b630",
        null,
        "pointer"
      ]
    ],
    [
      "005ac8cc",
      "DATA",
      [
        "storage",
        "00bf3a48",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac8d8",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac8b0.md#insn-005ac8c4) · [`005ac8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac8b0.md#insn-005ac8d8)
- 新版 [`005ac8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac8b0.md#insn-005ac8c4) · [`005ac8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac8b0.md#insn-005ac8d8)

~~~diff
- 005ac8c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5e0:8"]]
- 005ac8c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac8c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:630:8"]]
+ 005ac8c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac8c4 bytes 08f142f9
+ 005ac8c4 bytes 081943f9
- 005ac8d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005ac8d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac8d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005ac8d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac8d8 bytes 08b142f9
+ 005ac8d8 bytes 08d942f9
~~~


<a id="compare-140f6cb9044fb4e99bec43a25b2cf21d"></a>

### [`005acbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005acbf4.md) → [`005acbf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acbf4.md) FUN_005acbf4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005ab944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab944.md) [`005abca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abca8.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00bdd950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd950.md)
- 新版 呼出元 2件 [`005ab944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab944.md) [`005abca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abca8.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00bdd9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9a0.md)

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
      "definition_site": "005acc3c",
      "incomplete_value": true,
      "site": "005acc3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005acc3c",
      "incomplete_value": true,
      "site": "005acc3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005acc20",
      "READ",
      [
        "storage",
        "00c1b5e8",
        null,
        "pointer"
      ]
    ],
    [
      "005acc3c",
      "DATA",
      [
        "storage",
        "00bf3a88",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005acc20",
      "READ",
      [
        "storage",
        "00c1b638",
        null,
        "pointer"
      ]
    ],
    [
      "005acc3c",
      "DATA",
      [
        "storage",
        "00bf3ad8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005acc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005acbf4.md#insn-005acc20)
- 新版 [`005acc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acbf4.md#insn-005acc20)

~~~diff
- 005acc20 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5e8:8"]]
- 005acc20 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005acc20 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:638:8"]]
+ 005acc20 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005acc20 bytes 29f542f9
+ 005acc20 bytes 291d43f9
~~~


<a id="compare-77432af4314d536d8a1c28b85d09e329"></a>

### [`005ace3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ace3c.md) → [`005ace3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ace3c.md) FUN_005ace3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005acf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005acf80.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 1件 [`005acf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acf80.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

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
      "definition_site": "005ace5c",
      "incomplete_value": true,
      "site": "005ace60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005ace5c",
      "incomplete_value": true,
      "site": "005ace60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005acf4c",
      "incomplete_value": true,
      "site": "005acf50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005acf4c",
      "incomplete_value": true,
      "site": "005acf50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005ace54",
      "READ",
      [
        "storage",
        "00c1b5e8",
        null,
        "pointer"
      ]
    ],
    [
      "005ace60",
      "DATA",
      [
        "storage",
        "00bf3a88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005acf44",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ace54",
      "READ",
      [
        "storage",
        "00c1b638",
        null,
        "pointer"
      ]
    ],
    [
      "005ace60",
      "DATA",
      [
        "storage",
        "00bf3ad8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005acf44",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ace54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ace3c.md#insn-005ace54) · [`005acf44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ace3c.md#insn-005acf44)
- 新版 [`005ace54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ace3c.md#insn-005ace54) · [`005acf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ace3c.md#insn-005acf44)

~~~diff
- 005ace54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5e8:8"]]
- 005ace54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ace54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:638:8"]]
+ 005ace54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ace54 bytes 08f542f9
+ 005ace54 bytes 081d43f9
- 005acf44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005acf44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005acf44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005acf44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005acf44 bytes 08b142f9
+ 005acf44 bytes 08d942f9
~~~


<a id="compare-c85bc462fefeea540abb47c5eb5f8a5d"></a>

### [`005adeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ad/005adeac.md) → [`005adeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adeac.md) FUN_005adeac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005ab944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab944.md) [`005adef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ad/005adef8.md) [`005ae3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae3c8.md) [`005ae654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae654.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 4件 [`005ab944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab944.md) [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) [`005ae3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae3c8.md) [`005ae654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae654.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005aded8",
      "incomplete_value": true,
      "site": "005adee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aded8",
      "incomplete_value": true,
      "site": "005adee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "005adedc",
      "incomplete_value": true,
      "site": "005adee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005adedc",
      "incomplete_value": true,
      "site": "005adee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005aded8",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005aded8",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005adedc",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aded8",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005aded8",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005adedc",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aded8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ad/005adeac.md#insn-005aded8) · [`005adedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ad/005adeac.md#insn-005adedc)
- 新版 [`005aded8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adeac.md#insn-005aded8) · [`005adedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adeac.md#insn-005adedc)

~~~diff
- 005aded8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005aded8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aded8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005aded8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005aded8 bytes 21b442f9
+ 005aded8 bytes 21dc42f9
- 005adedc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005adedc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005adedc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005adedc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005adedc bytes 42b842f9
+ 005adedc bytes 42e042f9
~~~


<a id="compare-3ff70b44c29ee941f3ef54cd899fd6ac"></a>

### [`005af158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005af158.md) → [`005af158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af158.md) FUN_005af158

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005ae3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae3c8.md) [`005ae654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae654.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 2件 [`005ae3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae3c8.md) [`005ae654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae654.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005af184",
      "incomplete_value": true,
      "site": "005af18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005af184",
      "incomplete_value": true,
      "site": "005af18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "005af188",
      "incomplete_value": true,
      "site": "005af18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005af188",
      "incomplete_value": true,
      "site": "005af18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005af184",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005af184",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005af188",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005af184",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005af184",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005af188",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005af184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005af158.md#insn-005af184) · [`005af188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005af158.md#insn-005af188)
- 新版 [`005af184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af158.md#insn-005af184) · [`005af188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af158.md#insn-005af188)

~~~diff
- 005af184 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005af184 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005af184 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005af184 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005af184 bytes 21b442f9
+ 005af184 bytes 21dc42f9
- 005af188 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005af188 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005af188 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005af188 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005af188 bytes 42b842f9
+ 005af188 bytes 42e042f9
~~~


<a id="compare-80283a1ed4bc7396b190f1af47a2ca6f"></a>

### [`005af630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005af630.md) → [`005af630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af630.md) FUN_005af630

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005adef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ad/005adef8.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 1件 [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005af65c",
      "incomplete_value": true,
      "site": "005af664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005af65c",
      "incomplete_value": true,
      "site": "005af664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "005af660",
      "incomplete_value": true,
      "site": "005af664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005af660",
      "incomplete_value": true,
      "site": "005af664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005af65c",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005af65c",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005af660",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005af65c",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005af65c",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005af660",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005af65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005af630.md#insn-005af65c) · [`005af660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005af630.md#insn-005af660)
- 新版 [`005af65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af630.md#insn-005af65c) · [`005af660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af630.md#insn-005af660)

~~~diff
- 005af65c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005af65c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005af65c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005af65c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005af65c bytes 21b442f9
+ 005af65c bytes 21dc42f9
- 005af660 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005af660 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005af660 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005af660 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005af660 bytes 42b842f9
+ 005af660 bytes 42e042f9
~~~


<a id="compare-1ab0124dc94ff211cea612609f682170"></a>

### [`005afb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afb30.md) → [`005afb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afb30.md) FUN_005afb30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005aea7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005aea7c.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 1件 [`005aea7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aea7c.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005afb5c",
      "incomplete_value": true,
      "site": "005afb64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afb5c",
      "incomplete_value": true,
      "site": "005afb64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "005afb60",
      "incomplete_value": true,
      "site": "005afb64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afb60",
      "incomplete_value": true,
      "site": "005afb64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005afb5c",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005afb5c",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005afb60",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005afb5c",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005afb5c",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005afb60",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005afb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afb30.md#insn-005afb5c) · [`005afb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afb30.md#insn-005afb60)
- 新版 [`005afb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afb30.md#insn-005afb5c) · [`005afb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afb30.md#insn-005afb60)

~~~diff
- 005afb5c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005afb5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afb5c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005afb5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005afb5c bytes 21b442f9
+ 005afb5c bytes 21dc42f9
- 005afb60 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005afb60 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afb60 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005afb60 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005afb60 bytes 42b842f9
+ 005afb60 bytes 42e042f9
~~~


<a id="compare-3d7fe3aca0c249af8558963c3d496e45"></a>

### [`005afd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afd1c.md) → [`005afd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd1c.md) FUN_005afd1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005afb7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afb7c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005afb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afb7c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005afd28",
      "incomplete_value": false,
      "site": "005afd2c",
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
      "definition_site": "005afd28",
      "incomplete_value": false,
      "site": "005afd2c",
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
      "005afd28",
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
      "005afd28",
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

- 旧版 [`005afd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afd1c.md#insn-005afd28)
- 新版 [`005afd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd1c.md#insn-005afd28)

~~~diff
- 005afd28 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005afd28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005afd28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005afd28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005afd28 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005afd28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005afd28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005afd28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005afd28 bytes 000c0c91
+ 005afd28 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48ef0635348df6f9f7830212c7a2cb49"></a>

### [`005afd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afd30.md) → [`005afd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd30.md) FUN_005afd30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005aef4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005aef4c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005aef4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aef4c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005afd3c",
      "incomplete_value": false,
      "site": "005afd40",
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
      "definition_site": "005afd3c",
      "incomplete_value": false,
      "site": "005afd40",
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
      "005afd3c",
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
      "005afd3c",
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

- 旧版 [`005afd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afd30.md#insn-005afd3c)
- 新版 [`005afd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd30.md#insn-005afd3c)

~~~diff
- 005afd3c ["COPY", "tmp:0:8", ["const:303:8"]]
- 005afd3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005afd3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005afd3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005afd3c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005afd3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005afd3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005afd3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005afd3c bytes 000c0c91
+ 005afd3c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7477316dcb4e4f03eea4b3f8d0e6ea9"></a>

### [`005afe3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afe3c.md) → [`005afe3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afe3c.md) FUN_005afe3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b06fc.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b06fc.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.16% / 新版 90.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005afe94",
      "incomplete_value": true,
      "site": "005afe94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005afe94",
      "incomplete_value": true,
      "site": "005afe94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005afec8",
      "incomplete_value": true,
      "site": "005afec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005afec8",
      "incomplete_value": true,
      "site": "005afec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005afef8",
      "incomplete_value": true,
      "site": "005aff00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005afef8",
      "incomplete_value": true,
      "site": "005aff00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "005afe88",
      "READ",
      [
        "storage",
        "00c1b540",
        null,
        "pointer"
      ]
    ],
    [
      "005afe94",
      "DATA",
      [
        "storage",
        "00bf36c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005afeb0",
      "READ",
      [
        "storage",
        "00c1b5f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005afe88",
      "READ",
      [
        "storage",
        "00c1b590",
        null,
        "pointer"
      ]
    ],
    [
      "005afe94",
      "DATA",
      [
        "storage",
        "00bf3718",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005afeb0",
      "READ",
      [
        "storage",
        "00c1b640",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005afe88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afe3c.md#insn-005afe88) · [`005afeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afe3c.md#insn-005afeb0) · [`005afee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afe3c.md#insn-005afee8)
- 新版 [`005afe88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afe3c.md#insn-005afe88) · [`005afeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afe3c.md#insn-005afeb0) · [`005afee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afe3c.md#insn-005afee8)

~~~diff
- 005afe88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:540:8"]]
- 005afe88 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afe88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:590:8"]]
+ 005afe88 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005afe88 bytes 29a142f9
+ 005afe88 bytes 29c942f9
- 005afeb0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5f0:8"]]
- 005afeb0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afeb0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:640:8"]]
+ 005afeb0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005afeb0 bytes 29f942f9
+ 005afeb0 bytes 292143f9
- 005afee8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5f8:8"]]
- 005afee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afee8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:648:8"]]
+ 005afee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005afee8 bytes 08fd42f9
+ 005afee8 bytes 082543f9
~~~


<a id="compare-14477c65cc49ba808a7decf34de5fec9"></a>

### [`005aff7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005aff7c.md) → [`005aff7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005aff7c.md) FUN_005aff7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b06fc.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b06fc.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005affa8",
      "incomplete_value": true,
      "site": "005affb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005affa8",
      "incomplete_value": true,
      "site": "005affb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "005affac",
      "incomplete_value": true,
      "site": "005affb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005affac",
      "incomplete_value": true,
      "site": "005affb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005affa8",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005affa8",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005affac",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005affa8",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005affa8",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005affac",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005affa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005aff7c.md#insn-005affa8) · [`005affac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005aff7c.md#insn-005affac)
- 新版 [`005affa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005aff7c.md#insn-005affa8) · [`005affac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005aff7c.md#insn-005affac)

~~~diff
- 005affa8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005affa8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005affa8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005affa8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005affa8 bytes 21b442f9
+ 005affa8 bytes 21dc42f9
- 005affac ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005affac ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005affac ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005affac ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005affac bytes 42b842f9
+ 005affac bytes 42e042f9
~~~


<a id="compare-0c3ffacbda021a958c80335a3c006d11"></a>

### [`005affc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005affc8.md) → [`005affc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005affc8.md) FUN_005affc8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b06fc.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b06fc.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005afff4",
      "incomplete_value": true,
      "site": "005afffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afff4",
      "incomplete_value": true,
      "site": "005afffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "005afff8",
      "incomplete_value": true,
      "site": "005afffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afff8",
      "incomplete_value": true,
      "site": "005afffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005afff4",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005afff4",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005afff8",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005afff4",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005afff4",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005afff8",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005afff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005affc8.md#insn-005afff4) · [`005afff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005affc8.md#insn-005afff8)
- 新版 [`005afff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005affc8.md#insn-005afff4) · [`005afff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005affc8.md#insn-005afff8)

~~~diff
- 005afff4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005afff4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afff4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005afff4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005afff4 bytes 21b442f9
+ 005afff4 bytes 21dc42f9
- 005afff8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005afff8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afff8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005afff8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005afff8 bytes 42b842f9
+ 005afff8 bytes 42e042f9
~~~


<a id="compare-889dd3de4c4fa45152d463b43411a8f0"></a>

### [`005b0014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0014.md) → [`005b0014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0014.md) FUN_005b0014

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

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
      "definition_site": "005b0030",
      "incomplete_value": true,
      "site": "005b0034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b0030",
      "incomplete_value": true,
      "site": "005b0034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b0054",
      "incomplete_value": true,
      "site": "005b0058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b0054",
      "incomplete_value": true,
      "site": "005b0058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005b0028",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "005b0034",
      "DATA",
      [
        "storage",
        "00bf3bc0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b004c",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b0028",
      "READ",
      [
        "storage",
        "00c1b650",
        null,
        "pointer"
      ]
    ],
    [
      "005b0034",
      "DATA",
      [
        "storage",
        "00bf3c10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b004c",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0014.md#insn-005b0028) · [`005b004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0014.md#insn-005b004c)
- 新版 [`005b0028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0014.md#insn-005b0028) · [`005b004c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0014.md#insn-005b004c)

~~~diff
- 005b0028 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
- 005b0028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0028 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:650:8"]]
+ 005b0028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0028 bytes 080143f9
+ 005b0028 bytes 082943f9
- 005b004c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005b004c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b004c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005b004c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b004c bytes 08b142f9
+ 005b004c bytes 08d942f9
~~~


<a id="compare-c66f8a0c1f03078cd50d82b7883623e9"></a>

### [`005b0304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0304.md) → [`005b0304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0304.md) FUN_005b0304

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

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
      "definition_site": "005b0320",
      "incomplete_value": true,
      "site": "005b0324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b0320",
      "incomplete_value": true,
      "site": "005b0324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b0344",
      "incomplete_value": true,
      "site": "005b0348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b0344",
      "incomplete_value": true,
      "site": "005b0348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005b0318",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "005b0324",
      "DATA",
      [
        "storage",
        "00bf3bc0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b033c",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b0318",
      "READ",
      [
        "storage",
        "00c1b650",
        null,
        "pointer"
      ]
    ],
    [
      "005b0324",
      "DATA",
      [
        "storage",
        "00bf3c10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b033c",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0304.md#insn-005b0318) · [`005b033c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0304.md#insn-005b033c)
- 新版 [`005b0318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0304.md#insn-005b0318) · [`005b033c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0304.md#insn-005b033c)

~~~diff
- 005b0318 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
- 005b0318 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0318 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:650:8"]]
+ 005b0318 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0318 bytes 080143f9
+ 005b0318 bytes 082943f9
- 005b033c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005b033c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b033c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005b033c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b033c bytes 08b142f9
+ 005b033c bytes 08d942f9
~~~


<a id="compare-84088008a18d8b76862b8473e5d764a5"></a>

### [`005b0384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0384.md) → [`005b0384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0384.md) FUN_005b0384

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "005b03a0",
      "incomplete_value": true,
      "site": "005b03a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b03a0",
      "incomplete_value": true,
      "site": "005b03a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b03c4",
      "incomplete_value": true,
      "site": "005b03c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b03c4",
      "incomplete_value": true,
      "site": "005b03c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005b0398",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "005b03a4",
      "DATA",
      [
        "storage",
        "00bf3bc0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b03bc",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b0398",
      "READ",
      [
        "storage",
        "00c1b650",
        null,
        "pointer"
      ]
    ],
    [
      "005b03a4",
      "DATA",
      [
        "storage",
        "00bf3c10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b03bc",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0384.md#insn-005b0398) · [`005b03bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0384.md#insn-005b03bc)
- 新版 [`005b0398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0384.md#insn-005b0398) · [`005b03bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0384.md#insn-005b03bc)

~~~diff
- 005b0398 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
- 005b0398 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0398 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:650:8"]]
+ 005b0398 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0398 bytes 080143f9
+ 005b0398 bytes 082943f9
- 005b03bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005b03bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b03bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005b03bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b03bc bytes 08b142f9
+ 005b03bc bytes 08d942f9
~~~


<a id="compare-f203c7cff20520902e40a4a969514304"></a>

### [`005b03f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b03f0.md) → [`005b03f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b03f0.md) FUN_005b03f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

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
      "definition_site": "005b040c",
      "incomplete_value": true,
      "site": "005b0410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b040c",
      "incomplete_value": true,
      "site": "005b0410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b0430",
      "incomplete_value": true,
      "site": "005b0434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b0430",
      "incomplete_value": true,
      "site": "005b0434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005b0404",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "005b0410",
      "DATA",
      [
        "storage",
        "00bf3bc0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b0428",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b0404",
      "READ",
      [
        "storage",
        "00c1b650",
        null,
        "pointer"
      ]
    ],
    [
      "005b0410",
      "DATA",
      [
        "storage",
        "00bf3c10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b0428",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b03f0.md#insn-005b0404) · [`005b0428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b03f0.md#insn-005b0428)
- 新版 [`005b0404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b03f0.md#insn-005b0404) · [`005b0428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b03f0.md#insn-005b0428)

~~~diff
- 005b0404 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
- 005b0404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0404 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:650:8"]]
+ 005b0404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0404 bytes 080143f9
+ 005b0404 bytes 082943f9
- 005b0428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 005b0428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005b0428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0428 bytes 08b142f9
+ 005b0428 bytes 08d942f9
~~~


<a id="compare-d137eb47f8c3e436dfb454c9786f7391"></a>

### [`005b04a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04a4.md) → [`005b04a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04a4.md) FUN_005b04a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a8ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8ff4.md) [`005a9180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9180.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)
- 新版 呼出元 2件 [`005a8ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8ff4.md) [`005a9180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9180.md) · 呼出先 4件 [`00bba418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba418.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md)

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
      "definition_site": "005b04d0",
      "incomplete_value": true,
      "site": "005b04d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b04d0",
      "incomplete_value": true,
      "site": "005b04d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
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
      "definition_site": "005b04d4",
      "incomplete_value": true,
      "site": "005b04d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b04d4",
      "incomplete_value": true,
      "site": "005b04d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
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
      "005b04d0",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005b04d0",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005b04d4",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b04d0",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005b04d0",
      "PARAM",
      [
        "storage",
        "00c16810",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005b04d4",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b04d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04a4.md#insn-005b04d0) · [`005b04d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04a4.md#insn-005b04d4)
- 新版 [`005b04d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04a4.md#insn-005b04d0) · [`005b04d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04a4.md#insn-005b04d4)

~~~diff
- 005b04d0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
- 005b04d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b04d0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:5b8:8"]]
+ 005b04d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005b04d0 bytes 21b442f9
+ 005b04d0 bytes 21dc42f9
- 005b04d4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
- 005b04d4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b04d4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:5c0:8"]]
+ 005b04d4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005b04d4 bytes 42b842f9
+ 005b04d4 bytes 42e042f9
~~~


<a id="compare-6ec16330a2e6b49023192702d15e2426"></a>

### [`005b04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md) → [`005b04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md) FUN_005b04f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a8ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8ff4.md) [`005b04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md) · 呼出先 7件 [`005aa390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa390.md) [`005ac2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac2ec.md) [`005ac338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac338.md) [`005b04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md) [`005b06fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b06fc.md)
- 新版 呼出元 2件 [`005a8ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8ff4.md) [`005b04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md) · 呼出先 7件 [`005aa390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa390.md) [`005ac2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac2ec.md) [`005ac338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac338.md) [`005b04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md) [`005b06fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b06fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.42% / 新版 95.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b0580",
      "incomplete_value": true,
      "site": "005b0598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b0580",
      "incomplete_value": true,
      "site": "005b0598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b06d4",
      "incomplete_value": true,
      "site": "005b06e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b06d4",
      "incomplete_value": true,
      "site": "005b06e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005b0570",
      "READ",
      [
        "storage",
        "00c1b5a0",
        null,
        "pointer"
      ]
    ],
    [
      "005b0598",
      "DATA",
      [
        "storage",
        "00bf3ad0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b06c4",
      "READ",
      [
        "storage",
        "00c1b5a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b0570",
      "READ",
      [
        "storage",
        "00c1b5f0",
        null,
        "pointer"
      ]
    ],
    [
      "005b0598",
      "DATA",
      [
        "storage",
        "00bf3b20",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b06c4",
      "READ",
      [
        "storage",
        "00c1b5f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md#insn-005b0570) · [`005b06c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md#insn-005b06c4)
- 新版 [`005b0570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md#insn-005b0570) · [`005b06c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b04f0.md#insn-005b06c4)

~~~diff
- 005b0570 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:5a0:8"]]
- 005b0570 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0570 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:5f0:8"]]
+ 005b0570 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0570 bytes 4ad142f9
+ 005b0570 bytes 4af942f9
- 005b06c4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:5a8:8"]]
- 005b06c4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b06c4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:5f8:8"]]
+ 005b06c4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 005b06c4 bytes 4ad542f9
+ 005b06c4 bytes 4afd42f9
~~~


<a id="compare-abc9cffa7b98d61cda0c79055687d487"></a>

### [`005b0a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0a4c.md) → [`005b0a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0a4c.md) FUN_005b0a4c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b0a5c",
      "incomplete_value": true,
      "site": "005b0a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005b0a5c",
      "incomplete_value": true,
      "site": "005b0a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005b0a54",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ],
    [
      "005b0a60",
      "DATA",
      [
        "storage",
        "00bf3740",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005b0a54",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "005b0a60",
      "DATA",
      [
        "storage",
        "00bf3790",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0a4c.md#insn-005b0a54)
- 新版 [`005b0a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0a4c.md#insn-005b0a54)

~~~diff
- 005b0a54 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:560:8"]]
- 005b0a54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0a54 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5b0:8"]]
+ 005b0a54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0a54 bytes 29b142f9
+ 005b0a54 bytes 29d942f9
~~~


<a id="compare-da861943f8a64b739e5b0aef4a3f786d"></a>

### [`005b39cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b39cc.md) → [`005b39cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39cc.md) FUN_005b39cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005b3850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3850.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005b3850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3850.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005b39d8",
      "incomplete_value": false,
      "site": "005b39dc",
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
      "definition_site": "005b39d8",
      "incomplete_value": false,
      "site": "005b39dc",
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
      "005b39d8",
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
      "005b39d8",
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

- 旧版 [`005b39d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b39cc.md#insn-005b39d8)
- 新版 [`005b39d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39cc.md#insn-005b39d8)

~~~diff
- 005b39d8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 005b39d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005b39d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005b39d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005b39d8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005b39d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005b39d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005b39d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005b39d8 bytes 000c0c91
+ 005b39d8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa1ba6d6f027e348b99a33e150044ae1"></a>

### [`005b4210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4210.md) → [`005b4210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4210.md) FUN_005b4210

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005b4028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4028.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005b4028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4028.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "005b421c",
      "incomplete_value": false,
      "site": "005b4220",
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
      "definition_site": "005b421c",
      "incomplete_value": false,
      "site": "005b4220",
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
      "005b421c",
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
      "005b421c",
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

- 旧版 [`005b421c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4210.md#insn-005b421c)
- 新版 [`005b421c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4210.md#insn-005b421c)

~~~diff
- 005b421c ["COPY", "tmp:0:8", ["const:303:8"]]
- 005b421c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005b421c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005b421c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005b421c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 005b421c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005b421c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005b421c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005b421c bytes 000c0c91
+ 005b421c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-278449920259e2eb6209f317c9f84dfb"></a>

### [`005b4228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4228.md) → [`005b4228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4228.md) FUN_005b4228

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
      "definition_site": "005b424c",
      "incomplete_value": false,
      "site": "005b424c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b424c",
      "incomplete_value": false,
      "site": "005b424c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "005b424c",
      "DATA",
      [
        "storage",
        "00bf3d70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b424c",
      "DATA",
      [
        "storage",
        "00bf3dc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4228.md#insn-005b4248)
- 新版 [`005b4248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4228.md#insn-005b4248)

~~~diff
- 005b4248 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 005b4248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4248 ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 005b4248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4248 bytes 08c13591
+ 005b4248 bytes 08013791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0ee87c7a98c3a86f3e2e27abb23ff8f"></a>

### [`005b425c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b425c.md) → [`005b425c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b425c.md) FUN_005b425c

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
      "definition_site": "005b4268",
      "incomplete_value": false,
      "site": "005b4268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4268",
      "incomplete_value": false,
      "site": "005b4268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "005b4268",
      "DATA",
      [
        "storage",
        "00bf3d70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4268",
      "DATA",
      [
        "storage",
        "00bf3dc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b425c.md#insn-005b4264)
- 新版 [`005b4264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b425c.md#insn-005b4264)

~~~diff
- 005b4264 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 005b4264 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b4264 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b4264 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b4264 ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 005b4264 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b4264 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b4264 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b4264 bytes 29c13591
+ 005b4264 bytes 29013791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b79690b914e464533b371af1813ffad8"></a>

### [`005b4278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4278.md) → [`005b4278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4278.md) FUN_005b4278

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 32件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 0件  · 呼出先 32件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.58% / 新版 96.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b445c",
      "incomplete_value": true,
      "site": "005b446c",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:ac3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b445c",
      "incomplete_value": true,
      "site": "005b446c",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:b57:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4480",
      "incomplete_value": false,
      "site": "005b4488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4480",
      "incomplete_value": false,
      "site": "005b4488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b48b4",
      "incomplete_value": false,
      "site": "005b48b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b48b4",
      "incomplete_value": false,
      "site": "005b48b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b4434",
      "PARAM",
      [
        "storage",
        "0029c718",
        null,
        "string"
      ]
    ],
    [
      "005b445c",
      "READ",
      [
        "storage",
        "002aeb57",
        null,
        "string"
      ]
    ],
    [
      "005b4488",
      "DATA",
      [
        "storage",
        "00bf3df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4434",
      "PARAM",
      [
        "storage",
        "0029c7a3",
        null,
        "string"
      ]
    ],
    [
      "005b445c",
      "READ",
      [
        "storage",
        "002aeac3",
        null,
        "string"
      ]
    ],
    [
      "005b4488",
      "DATA",
      [
        "storage",
        "00bf3e40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4278.md#insn-005b4434) · [`005b4454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4278.md#insn-005b4454) · [`005b4480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4278.md#insn-005b4480)
- 新版 [`005b4434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4278.md#insn-005b4434) · [`005b4454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4278.md#insn-005b4454) · [`005b4480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4278.md#insn-005b4480)

~~~diff
- 005b4434 ["COPY", "tmp:0:8", ["const:718:8"]]
- 005b4434 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b4434 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b4434 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b4434 ["COPY", "tmp:0:8", ["const:7a3:8"]]
+ 005b4434 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b4434 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b4434 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b4434 bytes 21601c91
+ 005b4434 bytes 218c1e91
- 005b4454 ["COPY", "tmp:0:8", ["const:b57:8"]]
- 005b4454 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b4454 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b4454 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b4454 ["COPY", "tmp:0:8", ["const:ac3:8"]]
+ 005b4454 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b4454 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b4454 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b4454 bytes 295d2d91
+ 005b4454 bytes 290d2b91
- 005b4480 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 005b4480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4480 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 005b4480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4480 bytes 08c13791
+ 005b4480 bytes 08013991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f62d8babd198d4ae5469e8cc0a228db8"></a>

### [`005b4f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4f4c.md) → [`005b4f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4f4c.md) FUN_005b4f4c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "005b4f60",
      "incomplete_value": false,
      "site": "005b4f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4f60",
      "incomplete_value": false,
      "site": "005b4f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "005b4f64",
      "DATA",
      [
        "storage",
        "00bf3df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4f64",
      "DATA",
      [
        "storage",
        "00bf3e40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4f4c.md#insn-005b4f60)
- 新版 [`005b4f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4f4c.md#insn-005b4f60)

~~~diff
- 005b4f60 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 005b4f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4f60 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 005b4f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4f60 bytes 08c13791
+ 005b4f60 bytes 08013991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac9d213386792e3ec29c294fce4a5353"></a>

### [`005b4f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4f70.md) → [`005b4f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4f70.md) FUN_005b4f70

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b4f74",
      "incomplete_value": false,
      "site": "005b4f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4f74",
      "incomplete_value": false,
      "site": "005b4f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "005b4f78",
      "DATA",
      [
        "storage",
        "00bf3df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4f78",
      "DATA",
      [
        "storage",
        "00bf3e40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4f70.md#insn-005b4f74)
- 新版 [`005b4f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4f70.md#insn-005b4f74)

~~~diff
- 005b4f74 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 005b4f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4f74 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 005b4f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4f74 bytes 08c13791
+ 005b4f74 bytes 08013991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04af1d007ead12994af06ee2998042bc"></a>

### [`005b5220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5220.md) → [`005b5220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5220.md) FUN_005b5220

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5224",
      "incomplete_value": false,
      "site": "005b5228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5224",
      "incomplete_value": false,
      "site": "005b5228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:e80:8"
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
      "005b5228",
      "DATA",
      [
        "storage",
        "00bf3e80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5228",
      "DATA",
      [
        "storage",
        "00bf3ed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5220.md#insn-005b5224)
- 新版 [`005b5224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5220.md#insn-005b5224)

~~~diff
- 005b5224 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 005b5224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5224 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 005b5224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5224 bytes 08013a91
+ 005b5224 bytes 08413b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5cd2a43fabf404c3b7866af054eacd8"></a>

### [`005b5240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5240.md) → [`005b5240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5240.md) FUN_005b5240

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.11% / 新版 97.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b5314",
      "incomplete_value": true,
      "site": "005b5324",
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
                "const:c19:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5314",
      "incomplete_value": true,
      "site": "005b5324",
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
                "const:ca6:8"
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
      "definition_site": "005b5318",
      "incomplete_value": true,
      "site": "005b5328",
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
      "definition_site": "005b5318",
      "incomplete_value": true,
      "site": "005b5328",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b5644",
      "incomplete_value": false,
      "site": "005b5644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5644",
      "incomplete_value": false,
      "site": "005b5644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b5314",
      "READ",
      [
        "storage",
        "00296ca6",
        null,
        "string"
      ]
    ],
    [
      "005b5318",
      "READ",
      [
        "storage",
        "00296cb2",
        null,
        "string"
      ]
    ],
    [
      "005b53d0",
      "READ",
      [
        "storage",
        "0029c72e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005b5314",
      "READ",
      [
        "storage",
        "00296c19",
        null,
        "string"
      ]
    ],
    [
      "005b5318",
      "READ",
      [
        "storage",
        "00296c25",
        null,
        "string"
      ]
    ],
    [
      "005b53d0",
      "READ",
      [
        "storage",
        "0029c7b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b530c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5240.md#insn-005b530c) · [`005b5310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5240.md#insn-005b5310)
- 新版 [`005b530c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5240.md#insn-005b530c) · [`005b5310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5240.md#insn-005b5310)

~~~diff
- 005b530c ["COPY", "tmp:0:8", ["const:ca6:8"]]
- 005b530c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b530c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b530c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b530c ["COPY", "tmp:0:8", ["const:c19:8"]]
+ 005b530c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b530c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b530c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b530c bytes 08993291
+ 005b530c bytes 08653091
- 005b5310 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 005b5310 bytes e9e7ff90
+ 005b5310 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 005b5310 bytes e9e7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a572f9e729442489735d4fe2f203522"></a>

### [`005b59a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b59a0.md) → [`005b59a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b59a0.md) FUN_005b59a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005b5878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b5878.md) [`005b59a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b59a0.md) [`0060320c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00603/0060320c.md) [`00641308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00641/00641308.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`005b5878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5878.md) [`005b59a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b59a0.md) [`0060320c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00603/0060320c.md) [`00641308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/00641308.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005b5bc4",
      "incomplete_value": false,
      "site": "005b5bcc",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5bc4",
      "incomplete_value": false,
      "site": "005b5bcc",
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
            "const:2ee:8"
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
      "definition_site": "005b5be0",
      "incomplete_value": false,
      "site": "005b5bec",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5be0",
      "incomplete_value": false,
      "site": "005b5bec",
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
            "const:919:8"
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
      "definition_site": "005b5ea8",
      "incomplete_value": false,
      "site": "005b5eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5e5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5ea8",
      "incomplete_value": false,
      "site": "005b5eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:672:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b5b0c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "005b5bc4",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "005b5be0",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005b5b0c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005b5bc4",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "005b5be0",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b59a0.md#insn-005b5b0c) · [`005b5bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b59a0.md#insn-005b5bc4) · [`005b5be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b5/005b59a0.md#insn-005b5be0)
- 新版 [`005b5b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b59a0.md#insn-005b5b0c) · [`005b5bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b59a0.md#insn-005b5bc4) · [`005b5be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b59a0.md#insn-005b5be0)

~~~diff
- 005b5b0c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005b5b0c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b5b0c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b5b0c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b5b0c ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 005b5b0c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b5b0c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b5b0c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b5b0c bytes 21280c91
+ 005b5b0c bytes 21900e91
- 005b5bc4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005b5bc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b5bc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b5bc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b5bc4 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005b5bc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b5bc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b5bc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b5bc4 bytes 21b80b91
+ 005b5bc4 bytes 21e40d91
- 005b5be0 ["COPY", "tmp:0:8", ["const:919:8"]]
- 005b5be0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b5be0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b5be0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b5be0 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005b5be0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b5be0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b5be0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b5be0 bytes 21642491
+ 005b5be0 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e214e70c5b3832723fcd4bdca5b0ea58"></a>

### [`005b6284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6284.md) → [`005b6284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6284.md) FUN_005b6284

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "005b6298",
      "incomplete_value": false,
      "site": "005b629c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6298",
      "incomplete_value": false,
      "site": "005b629c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "005b629c",
      "DATA",
      [
        "storage",
        "00bf3ef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b629c",
      "DATA",
      [
        "storage",
        "00bf3f40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6284.md#insn-005b6298)
- 新版 [`005b6298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6284.md#insn-005b6298)

~~~diff
- 005b6298 ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 005b6298 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6298 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6298 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6298 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 005b6298 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6298 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6298 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6298 bytes 08c13b91
+ 005b6298 bytes 08013d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-757cfbed45d9cad385d3b50bcb83a94b"></a>

### [`005b62a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b62a8.md) → [`005b62a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b62a8.md) FUN_005b62a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b62ac",
      "incomplete_value": false,
      "site": "005b62b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b62ac",
      "incomplete_value": false,
      "site": "005b62b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "005b62b0",
      "DATA",
      [
        "storage",
        "00bf3ef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b62b0",
      "DATA",
      [
        "storage",
        "00bf3f40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b62ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b62a8.md#insn-005b62ac)
- 新版 [`005b62ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b62a8.md#insn-005b62ac)

~~~diff
- 005b62ac ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 005b62ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b62ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b62ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b62ac ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 005b62ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b62ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b62ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b62ac bytes 08c13b91
+ 005b62ac bytes 08013d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-870f21fba7c0dc30a4bfc92be2d6bb65"></a>

### [`005b632c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b632c.md) → [`005b632c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b632c.md) FUN_005b632c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "005b6340",
      "incomplete_value": false,
      "site": "005b6344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6340",
      "incomplete_value": false,
      "site": "005b6344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "005b6344",
      "DATA",
      [
        "storage",
        "00bf3f80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6344",
      "DATA",
      [
        "storage",
        "00bf3fd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b632c.md#insn-005b6340)
- 新版 [`005b6340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b632c.md#insn-005b6340)

~~~diff
- 005b6340 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 005b6340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6340 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 005b6340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6340 bytes 08013e91
+ 005b6340 bytes 08413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f48fd2862061df4ebd913b93b099b57c"></a>

### [`005b6350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6350.md) → [`005b6350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6350.md) FUN_005b6350

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6354",
      "incomplete_value": false,
      "site": "005b6358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6354",
      "incomplete_value": false,
      "site": "005b6358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "005b6358",
      "DATA",
      [
        "storage",
        "00bf3f80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6358",
      "DATA",
      [
        "storage",
        "00bf3fd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6350.md#insn-005b6354)
- 新版 [`005b6354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6350.md#insn-005b6354)

~~~diff
- 005b6354 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 005b6354 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6354 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6354 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6354 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 005b6354 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6354 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6354 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6354 bytes 08013e91
+ 005b6354 bytes 08413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2b3fc69ce56dcb1f6ee759174efd9d7"></a>

### [`005b63dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b63dc.md) → [`005b63dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b63dc.md) FUN_005b63dc

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
      "definition_site": "005b6400",
      "incomplete_value": false,
      "site": "005b6400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6400",
      "incomplete_value": false,
      "site": "005b6400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
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
      "005b6400",
      "DATA",
      [
        "storage",
        "00bf4010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6400",
      "DATA",
      [
        "storage",
        "00bf4060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b63fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b63dc.md#insn-005b63fc)
- 新版 [`005b63fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b63dc.md#insn-005b63fc)

~~~diff
- 005b63fc ["COPY", "tmp:0:8", ["const:10:8"]]
- 005b63fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b63fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b63fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b63fc ["COPY", "tmp:0:8", ["const:60:8"]]
+ 005b63fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b63fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b63fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b63fc bytes 08410091
+ 005b63fc bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83080a6ade08c95c8d7e01529e0aee72"></a>

### [`005b64ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b64ac.md) → [`005b64ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b64ac.md) FUN_005b64ac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b64d0",
      "incomplete_value": true,
      "site": "005b64d0",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b64d0",
      "incomplete_value": true,
      "site": "005b64d0",
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
            "const:90:8"
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
      "005b64d0",
      "DATA",
      [
        "storage",
        "00bf4090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b64d0",
      "DATA",
      [
        "storage",
        "00bf40e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b64cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b64ac.md#insn-005b64cc)
- 新版 [`005b64cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b64ac.md#insn-005b64cc)

~~~diff
- 005b64cc ["COPY", "tmp:0:8", ["const:90:8"]]
- 005b64cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b64cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b64cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b64cc ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 005b64cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b64cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b64cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b64cc bytes 08410291
+ 005b64cc bytes 08810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2efa2bb3b8681ba3628b04109907b4a1"></a>

### [`005b64e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b64e0.md) → [`005b64e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b64e0.md) FUN_005b64e0

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
      "definition_site": "005b64ec",
      "incomplete_value": false,
      "site": "005b64ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b64ec",
      "incomplete_value": false,
      "site": "005b64ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "005b64ec",
      "DATA",
      [
        "storage",
        "00bf4090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b64ec",
      "DATA",
      [
        "storage",
        "00bf40e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b64e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b64e0.md#insn-005b64e8)
- 新版 [`005b64e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b64e0.md#insn-005b64e8)

~~~diff
- 005b64e8 ["COPY", "tmp:0:8", ["const:90:8"]]
- 005b64e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b64e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b64e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b64e8 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 005b64e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b64e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b64e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b64e8 bytes 29410291
+ 005b64e8 bytes 29810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a20887bf9344f48b2ee50c8450e7e9a"></a>

### [`005b6728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6728.md) → [`005b6728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6728.md) FUN_005b6728

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
      "definition_site": "005b674c",
      "incomplete_value": false,
      "site": "005b674c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b674c",
      "incomplete_value": false,
      "site": "005b674c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "005b674c",
      "DATA",
      [
        "storage",
        "00bf4110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b674c",
      "DATA",
      [
        "storage",
        "00bf4160",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6728.md#insn-005b6748)
- 新版 [`005b6748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6728.md#insn-005b6748)

~~~diff
- 005b6748 ["COPY", "tmp:0:8", ["const:110:8"]]
- 005b6748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6748 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 005b6748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6748 bytes 08410491
+ 005b6748 bytes 08810591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81dbfb2fdfd7cccc36af11a022121c38"></a>

### [`005b675c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b675c.md) → [`005b675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b675c.md) FUN_005b675c

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
      "definition_site": "005b6768",
      "incomplete_value": false,
      "site": "005b6768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6768",
      "incomplete_value": false,
      "site": "005b6768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "005b6768",
      "DATA",
      [
        "storage",
        "00bf4110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6768",
      "DATA",
      [
        "storage",
        "00bf4160",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b675c.md#insn-005b6764)
- 新版 [`005b6764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b675c.md#insn-005b6764)

~~~diff
- 005b6764 ["COPY", "tmp:0:8", ["const:110:8"]]
- 005b6764 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6764 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6764 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6764 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 005b6764 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6764 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6764 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6764 bytes 29410491
+ 005b6764 bytes 29810591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95e4ec82172ec046f304aa28d1c1c4ac"></a>

### [`005b6778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6778.md) → [`005b6778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6778.md) FUN_005b6778

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b68b4",
      "incomplete_value": false,
      "site": "005b68b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b68b4",
      "incomplete_value": false,
      "site": "005b68b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:180:8"
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
      "definition_site": "005b6870",
      "incomplete_value": false,
      "site": "005b6880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:a39:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6870",
      "incomplete_value": false,
      "site": "005b6880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:ac6:8"
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
      "definition_site": "005b6878",
      "incomplete_value": false,
      "site": "005b6880",
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
            "const:c16:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6878",
      "incomplete_value": false,
      "site": "005b6880",
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
            "const:ca3:8"
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
      "005b6840",
      "READ",
      [
        "storage",
        "00294b46",
        null,
        "string"
      ]
    ],
    [
      "005b6844",
      "READ",
      [
        "storage",
        "00294b4f",
        null,
        "string"
      ]
    ],
    [
      "005b6870",
      "PARAM",
      [
        "storage",
        "00293ac6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005b6840",
      "READ",
      [
        "storage",
        "00294ab9",
        null,
        "string"
      ]
    ],
    [
      "005b6844",
      "READ",
      [
        "storage",
        "00294ac2",
        null,
        "string"
      ]
    ],
    [
      "005b6870",
      "PARAM",
      [
        "storage",
        "00293a39",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6778.md#insn-005b6824) · [`005b682c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6778.md#insn-005b682c)
- 新版 [`005b6824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6778.md#insn-005b6824) · [`005b682c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6778.md#insn-005b682c)

~~~diff
- 005b6824 ["COPY", "tmp:0:8", ["const:b46:8"]]
- 005b6824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6824 ["COPY", "tmp:0:8", ["const:ab9:8"]]
+ 005b6824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6824 bytes 29192d91
+ 005b6824 bytes 29e52a91
- 005b682c ["COPY", "register:4040:8", ["const:292000:8"]]
- 005b682c bytes e8e6ff90
+ 005b682c ["COPY", "register:4040:8", ["const:292000:8"]]
+ 005b682c bytes e8e6ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe5638c54dc9a23186f24266e5d4c3c9"></a>

### [`005b6a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6a94.md) → [`005b6a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6a94.md) FUN_005b6a94

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
      "definition_site": "005b6ab8",
      "incomplete_value": false,
      "site": "005b6ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6ab8",
      "incomplete_value": false,
      "site": "005b6ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:180:8"
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
      "005b6ab8",
      "DATA",
      [
        "storage",
        "00bf4180",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6ab8",
      "DATA",
      [
        "storage",
        "00bf41d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6a94.md#insn-005b6ab4)
- 新版 [`005b6ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6a94.md#insn-005b6ab4)

~~~diff
- 005b6ab4 ["COPY", "tmp:0:8", ["const:180:8"]]
- 005b6ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6ab4 ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 005b6ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6ab4 bytes 08010691
+ 005b6ab4 bytes 08410791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbc4566f7af1e471ae18ae0b52be2a32"></a>

### [`005b6ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6ac8.md) → [`005b6ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6ac8.md) FUN_005b6ac8

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
      "definition_site": "005b6ad4",
      "incomplete_value": false,
      "site": "005b6ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6ad4",
      "incomplete_value": false,
      "site": "005b6ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:180:8"
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
      "005b6ad4",
      "DATA",
      [
        "storage",
        "00bf4180",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6ad4",
      "DATA",
      [
        "storage",
        "00bf41d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6ac8.md#insn-005b6ad0)
- 新版 [`005b6ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6ac8.md#insn-005b6ad0)

~~~diff
- 005b6ad0 ["COPY", "tmp:0:8", ["const:180:8"]]
- 005b6ad0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6ad0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6ad0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6ad0 ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 005b6ad0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6ad0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6ad0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6ad0 bytes 29010691
+ 005b6ad0 bytes 29410791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-256d986c0753273d806e5ace08b0412f"></a>

### [`005b6b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6b58.md) → [`005b6b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6b58.md) FUN_005b6b58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b6b78",
      "incomplete_value": false,
      "site": "005b6b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6b78",
      "incomplete_value": false,
      "site": "005b6b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:210:8"
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
      "005b6b7c",
      "DATA",
      [
        "storage",
        "00bf4210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6b7c",
      "DATA",
      [
        "storage",
        "00bf4260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6b58.md#insn-005b6b78)
- 新版 [`005b6b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6b58.md#insn-005b6b78)

~~~diff
- 005b6b78 ["COPY", "tmp:0:8", ["const:210:8"]]
- 005b6b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6b78 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 005b6b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6b78 bytes 08410891
+ 005b6b78 bytes 08810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-568f4d265f8837fff11a55c9cf7bbd83"></a>

### [`005b6b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6b90.md) → [`005b6b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6b90.md) FUN_005b6b90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6b94",
      "incomplete_value": false,
      "site": "005b6b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6b94",
      "incomplete_value": false,
      "site": "005b6b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:210:8"
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
      "005b6b98",
      "DATA",
      [
        "storage",
        "00bf4210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6b98",
      "DATA",
      [
        "storage",
        "00bf4260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6b90.md#insn-005b6b94)
- 新版 [`005b6b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6b90.md#insn-005b6b94)

~~~diff
- 005b6b94 ["COPY", "tmp:0:8", ["const:210:8"]]
- 005b6b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6b94 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 005b6b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6b94 bytes 08410891
+ 005b6b94 bytes 08810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

