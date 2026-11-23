# v15.7.3 → v15.7.4 · 最優先の変更候補 (75)

[一覧の目次](README.md)

<a id="compare-ebb980de0521ab784e7f0e80f44e73cd"></a>

### [`00b77f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77f60.md) → [`00b77fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77fa4.md) _ZNSt6__ndk15stoulERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb50.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)
- 新版 呼出元 1件 [`00bdbba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbba0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.41% / 新版 93.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b780a0",
      "incomplete_value": true,
      "site": "00b780a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7805c",
      "incomplete_value": true,
      "site": "00b7805c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55:8"
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
      "00b78088",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b7808c",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b780c8",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78088",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b7808c",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b780c8",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77f60.md#insn-00b77fbc) · [`00b77fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77f60.md#insn-00b77fd8) · [`00b78008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77f60.md#insn-00b78008)
- 新版 [`00b78000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77fa4.md#insn-00b78000) · [`00b7801c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77fa4.md#insn-00b7801c) · [`00b7804c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77fa4.md#insn-00b7804c)

~~~diff
- 00b77fbc ["INT_ADD", "register:40f0:8", ["const:b77fbc:8", "const:4:8"]]
- 00b77fbc ["CALL", null, ["callee:00bdb270:8"]]
+ 00b78000 ["INT_ADD", "register:40f0:8", ["const:b78000:8", "const:4:8"]]
+ 00b78000 ["CALL", null, ["callee:00bdb270:8"]]
- 00b77fbc bytes 998c0194
+ 00b78000 bytes 9c8c0194
- 00b77fd8 ["INT_ADD", "register:40f0:8", ["const:b77fd8:8", "const:4:8"]]
- 00b77fd8 ["CALL", null, ["callee:00be1070:8"]]
+ 00b7801c ["INT_ADD", "register:40f0:8", ["const:b7801c:8", "const:4:8"]]
+ 00b7801c ["CALL", null, ["callee:00be1070:8"]]
- 00b77fd8 bytes 12a40194
+ 00b7801c bytes 15a40194
- 00b78008 ["INT_ADD", "register:40f0:8", ["const:b78008:8", "const:4:8"]]
- 00b78008 ["CALL", null, ["callee:00be1060:8"]]
+ 00b7804c ["INT_ADD", "register:40f0:8", ["const:b7804c:8", "const:4:8"]]
+ 00b7804c ["CALL", null, ["callee:00be1060:8"]]
- 00b78008 bytes 02a40194
+ 00b7804c bytes 05a40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39a40ac05182394f1255aedae1775813"></a>

### [`00b780cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b780cc.md) → [`00b78110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78110.md) _ZNSt6__ndk15stollERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb390.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb700.md)
- 新版 呼出元 1件 [`00bdb3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3e0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb750.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.21% / 新版 91.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7824c",
      "incomplete_value": true,
      "site": "00b7824c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78208",
      "incomplete_value": true,
      "site": "00b78208",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:880:8"
              ]
            ]
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
      "definition_site": "00b78250",
      "incomplete_value": true,
      "site": "00b78250",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b7820c",
      "incomplete_value": true,
      "site": "00b7820c",
      "value": [
        "LOAD",
        "8",
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
      "00b781f4",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b781f8",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78234",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b781f4",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b781f8",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b78234",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b780cc.md#insn-00b78128) · [`00b78144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b780cc.md#insn-00b78144) · [`00b78174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b780cc.md#insn-00b78174)
- 新版 [`00b7816c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78110.md#insn-00b7816c) · [`00b78188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78110.md#insn-00b78188) · [`00b781b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78110.md#insn-00b781b8)

~~~diff
- 00b78128 ["INT_ADD", "register:40f0:8", ["const:b78128:8", "const:4:8"]]
- 00b78128 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b7816c ["INT_ADD", "register:40f0:8", ["const:b7816c:8", "const:4:8"]]
+ 00b7816c ["CALL", null, ["callee:00bdb270:8"]]
- 00b78128 bytes 3e8c0194
+ 00b7816c bytes 418c0194
- 00b78144 ["INT_ADD", "register:40f0:8", ["const:b78144:8", "const:4:8"]]
- 00b78144 ["CALL", null, ["callee:00bdb750:8"]]
+ 00b78188 ["INT_ADD", "register:40f0:8", ["const:b78188:8", "const:4:8"]]
+ 00b78188 ["CALL", null, ["callee:00bdb750:8"]]
- 00b78144 bytes 6f8d0194
+ 00b78188 bytes 728d0194
- 00b78174 ["INT_ADD", "register:40f0:8", ["const:b78174:8", "const:4:8"]]
- 00b78174 ["CALL", null, ["callee:00be1060:8"]]
+ 00b781b8 ["INT_ADD", "register:40f0:8", ["const:b781b8:8", "const:4:8"]]
+ 00b781b8 ["CALL", null, ["callee:00be1060:8"]]
- 00b78174 bytes a7a30194
+ 00b781b8 bytes aaa30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bff10e036c3ca3bf9d626838d360193"></a>

### [`00b78238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78238.md) → [`00b7827c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b7827c.md) _ZNSt6__ndk16stoullERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3a0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be0200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0200.md)
- 新版 呼出元 1件 [`00bdb3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3f0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be0250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0250.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.39% / 新版 92.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7837c",
      "incomplete_value": true,
      "site": "00b7837c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78338",
      "incomplete_value": true,
      "site": "00b78338",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55:8"
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
      "definition_site": "00b78380",
      "incomplete_value": true,
      "site": "00b78380",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b7833c",
      "incomplete_value": true,
      "site": "00b7833c",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b78364",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b78368",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b783a4",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78364",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b78368",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b783a4",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78238.md#insn-00b78298) · [`00b782b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78238.md#insn-00b782b4) · [`00b782e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78238.md#insn-00b782e4)
- 新版 [`00b782dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b7827c.md#insn-00b782dc) · [`00b782f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b7827c.md#insn-00b782f8) · [`00b78328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b7827c.md#insn-00b78328)

~~~diff
- 00b78298 ["INT_ADD", "register:40f0:8", ["const:b78298:8", "const:4:8"]]
- 00b78298 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b782dc ["INT_ADD", "register:40f0:8", ["const:b782dc:8", "const:4:8"]]
+ 00b782dc ["CALL", null, ["callee:00bdb270:8"]]
- 00b78298 bytes e28b0194
+ 00b782dc bytes e58b0194
- 00b782b4 ["INT_ADD", "register:40f0:8", ["const:b782b4:8", "const:4:8"]]
- 00b782b4 ["CALL", null, ["callee:00be0250:8"]]
+ 00b782f8 ["INT_ADD", "register:40f0:8", ["const:b782f8:8", "const:4:8"]]
+ 00b782f8 ["CALL", null, ["callee:00be0250:8"]]
- 00b782b4 bytes d39f0194
+ 00b782f8 bytes d69f0194
- 00b782e4 ["INT_ADD", "register:40f0:8", ["const:b782e4:8", "const:4:8"]]
- 00b782e4 ["CALL", null, ["callee:00be1060:8"]]
+ 00b78328 ["INT_ADD", "register:40f0:8", ["const:b78328:8", "const:4:8"]]
+ 00b78328 ["CALL", null, ["callee:00be1060:8"]]
- 00b782e4 bytes 4ba30194
+ 00b78328 bytes 4ea30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-738f777f8cb2ee0f4354347177af8860"></a>

### [`00b783a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b783a8.md) → [`00b783ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b783ec.md) _ZNSt6__ndk14stofERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb740.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb710.md)
- 新版 呼出元 1件 [`00bdb790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb790.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb760.md)

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
      "definition_site": "00b784c8",
      "incomplete_value": true,
      "site": "00b784c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78484",
      "incomplete_value": true,
      "site": "00b78484",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55:8"
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
      "definition_site": "00b784d0",
      "incomplete_value": true,
      "site": "00b784d0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b7848c",
      "incomplete_value": true,
      "site": "00b7848c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b78500",
      "incomplete_value": true,
      "site": "00b78500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b784bc",
      "incomplete_value": true,
      "site": "00b784bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "00b784b8",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b784bc",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b784f0",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b784b8",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b784bc",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b784f0",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b783f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b783a8.md#insn-00b783f4) · [`00b7840c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b783a8.md#insn-00b7840c) · [`00b7843c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b783a8.md#insn-00b7843c)
- 新版 [`00b78438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b783ec.md#insn-00b78438) · [`00b78450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b783ec.md#insn-00b78450) · [`00b78480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b783ec.md#insn-00b78480)

~~~diff
- 00b783f4 ["INT_ADD", "register:40f0:8", ["const:b783f4:8", "const:4:8"]]
- 00b783f4 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b78438 ["INT_ADD", "register:40f0:8", ["const:b78438:8", "const:4:8"]]
+ 00b78438 ["CALL", null, ["callee:00bdb270:8"]]
- 00b783f4 bytes 8b8b0194
+ 00b78438 bytes 8e8b0194
- 00b7840c ["INT_ADD", "register:40f0:8", ["const:b7840c:8", "const:4:8"]]
- 00b7840c ["CALL", null, ["callee:00bdb760:8"]]
+ 00b78450 ["INT_ADD", "register:40f0:8", ["const:b78450:8", "const:4:8"]]
+ 00b78450 ["CALL", null, ["callee:00bdb760:8"]]
- 00b7840c bytes c18c0194
+ 00b78450 bytes c48c0194
- 00b7843c ["INT_ADD", "register:40f0:8", ["const:b7843c:8", "const:4:8"]]
- 00b7843c ["CALL", null, ["callee:00be1060:8"]]
+ 00b78480 ["INT_ADD", "register:40f0:8", ["const:b78480:8", "const:4:8"]]
+ 00b78480 ["CALL", null, ["callee:00be1060:8"]]
- 00b7843c bytes f5a20194
+ 00b78480 bytes f8a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09708b6af4b56351b728d54041608955"></a>

### [`00b784f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b784f0.md) → [`00b78534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78534.md) _ZNSt6__ndk14stodERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3b0.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb720.md)
- 新版 呼出元 1件 [`00bdb400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb400.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb770.md)

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
      "definition_site": "00b78610",
      "incomplete_value": true,
      "site": "00b78610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b785cc",
      "incomplete_value": true,
      "site": "00b785cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55:8"
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
      "definition_site": "00b78618",
      "incomplete_value": true,
      "site": "00b78618",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b785d4",
      "incomplete_value": true,
      "site": "00b785d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b78648",
      "incomplete_value": true,
      "site": "00b78648",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78604",
      "incomplete_value": true,
      "site": "00b78604",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "00b78600",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b78604",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78638",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78600",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b78604",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b78638",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7853c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b784f0.md#insn-00b7853c) · [`00b78554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b784f0.md#insn-00b78554) · [`00b78584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b784f0.md#insn-00b78584)
- 新版 [`00b78580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78534.md#insn-00b78580) · [`00b78598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78534.md#insn-00b78598) · [`00b785c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78534.md#insn-00b785c8)

~~~diff
- 00b7853c ["INT_ADD", "register:40f0:8", ["const:b7853c:8", "const:4:8"]]
- 00b7853c ["CALL", null, ["callee:00bdb270:8"]]
+ 00b78580 ["INT_ADD", "register:40f0:8", ["const:b78580:8", "const:4:8"]]
+ 00b78580 ["CALL", null, ["callee:00bdb270:8"]]
- 00b7853c bytes 398b0194
+ 00b78580 bytes 3c8b0194
- 00b78554 ["INT_ADD", "register:40f0:8", ["const:b78554:8", "const:4:8"]]
- 00b78554 ["CALL", null, ["callee:00bdb770:8"]]
+ 00b78598 ["INT_ADD", "register:40f0:8", ["const:b78598:8", "const:4:8"]]
+ 00b78598 ["CALL", null, ["callee:00bdb770:8"]]
- 00b78554 bytes 738c0194
+ 00b78598 bytes 768c0194
- 00b78584 ["INT_ADD", "register:40f0:8", ["const:b78584:8", "const:4:8"]]
- 00b78584 ["CALL", null, ["callee:00be1060:8"]]
+ 00b785c8 ["INT_ADD", "register:40f0:8", ["const:b785c8:8", "const:4:8"]]
+ 00b785c8 ["CALL", null, ["callee:00be1060:8"]]
- 00b78584 bytes a3a20194
+ 00b785c8 bytes a6a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9113607bc2bcdc756f5a1c522d8d1cdd"></a>

### [`00b78638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78638.md) → [`00b7867c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b7867c.md) _ZNSt6__ndk15stoldERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md)

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
      "definition_site": "00b78770",
      "incomplete_value": true,
      "site": "00b78770",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7872c",
      "incomplete_value": true,
      "site": "00b7872c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55:8"
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
      "definition_site": "00b78774",
      "incomplete_value": true,
      "site": "00b78774",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b78730",
      "incomplete_value": true,
      "site": "00b78730",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b787b0",
      "incomplete_value": true,
      "site": "00b787b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7876c",
      "incomplete_value": true,
      "site": "00b7876c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "00b78758",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b7875c",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78798",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78758",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b7875c",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b78798",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78638.md#insn-00b78690) · [`00b786a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78638.md#insn-00b786a8) · [`00b786d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78638.md#insn-00b786d8)
- 新版 [`00b786d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b7867c.md#insn-00b786d4) · [`00b786ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b7867c.md#insn-00b786ec) · [`00b7871c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b7867c.md#insn-00b7871c)

~~~diff
- 00b78690 ["INT_ADD", "register:40f0:8", ["const:b78690:8", "const:4:8"]]
- 00b78690 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b786d4 ["INT_ADD", "register:40f0:8", ["const:b786d4:8", "const:4:8"]]
+ 00b786d4 ["CALL", null, ["callee:00bdb270:8"]]
- 00b78690 bytes e48a0194
+ 00b786d4 bytes e78a0194
- 00b786a8 ["INT_ADD", "register:40f0:8", ["const:b786a8:8", "const:4:8"]]
- 00b786a8 ["CALL", null, ["callee:00be1080:8"]]
+ 00b786ec ["INT_ADD", "register:40f0:8", ["const:b786ec:8", "const:4:8"]]
+ 00b786ec ["CALL", null, ["callee:00be1080:8"]]
- 00b786a8 bytes 62a20194
+ 00b786ec bytes 65a20194
- 00b786d8 ["INT_ADD", "register:40f0:8", ["const:b786d8:8", "const:4:8"]]
- 00b786d8 ["CALL", null, ["callee:00be1060:8"]]
+ 00b7871c ["INT_ADD", "register:40f0:8", ["const:b7871c:8", "const:4:8"]]
+ 00b7871c ["CALL", null, ["callee:00be1060:8"]]
- 00b786d8 bytes 4ea20194
+ 00b7871c bytes 51a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-378b99942fccad50f4473ae010903366"></a>

### [`00b7879c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b7879c.md) → [`00b787e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b787e0.md) _ZNSt6__ndk14stoiERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045efa8.md) [`00b7b2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045efa8.md) [`00b7b30c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b30c.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md)

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
      "definition_site": "00b78908",
      "incomplete_value": true,
      "site": "00b78908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b788c4",
      "incomplete_value": true,
      "site": "00b788c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55:8"
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
      "definition_site": "00b78910",
      "incomplete_value": true,
      "site": "00b78910",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b788cc",
      "incomplete_value": true,
      "site": "00b788cc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b788b4",
      "incomplete_value": false,
      "site": "00b788c4",
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
            "const:ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78870",
      "incomplete_value": false,
      "site": "00b78880",
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
            "const:55:8"
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
      "00b788b4",
      "PARAM",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b788f8",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b788fc",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b788b4",
      "PARAM",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b788f8",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b788fc",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b7879c.md#insn-00b78880) · [`00b787f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b7879c.md#insn-00b787f0) · [`00b7880c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b7879c.md#insn-00b7880c)
- 新版 [`00b788c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b787e0.md#insn-00b788c4) · [`00b78834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b787e0.md#insn-00b78834) · [`00b78850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b787e0.md#insn-00b78850)

~~~diff
- 00b78880 ["INT_ADD", "register:40f0:8", ["const:b78880:8", "const:4:8"]]
- 00b78880 ["CALL", null, ["callee:0045efa8:8"]]
+ 00b788c4 ["INT_ADD", "register:40f0:8", ["const:b788c4:8", "const:4:8"]]
+ 00b788c4 ["CALL", null, ["callee:0045efa8:8"]]
- 00b78880 bytes ca99e397
+ 00b788c4 bytes b999e397
- 00b787f0 ["INT_ADD", "register:40f0:8", ["const:b787f0:8", "const:4:8"]]
- 00b787f0 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b78834 ["INT_ADD", "register:40f0:8", ["const:b78834:8", "const:4:8"]]
+ 00b78834 ["CALL", null, ["callee:00bdb270:8"]]
- 00b787f0 bytes 8c8a0194
+ 00b78834 bytes 8f8a0194
- 00b7880c ["INT_ADD", "register:40f0:8", ["const:b7880c:8", "const:4:8"]]
- 00b7880c ["CALL", null, ["callee:00be1090:8"]]
+ 00b78850 ["INT_ADD", "register:40f0:8", ["const:b78850:8", "const:4:8"]]
+ 00b78850 ["CALL", null, ["callee:00be1090:8"]]
- 00b7880c bytes 0da20194
+ 00b78850 bytes 10a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b33325216a8d8232dff79f585dbba73b"></a>

### [`00b78900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78900.md) → [`00b78944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78944.md) _ZNSt6__ndk14stolERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045efa8.md) [`00b7b2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0045efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045efa8.md) [`00b7b30c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b30c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md)

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
      "definition_site": "00b78a10",
      "incomplete_value": false,
      "site": "00b78a20",
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
            "const:ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b789cc",
      "incomplete_value": false,
      "site": "00b789dc",
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
            "const:55:8"
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
      "00b78a10",
      "PARAM",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78a10",
      "PARAM",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b789dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78900.md#insn-00b789dc) · [`00b78954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78900.md#insn-00b78954) · [`00b78970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78900.md#insn-00b78970)
- 新版 [`00b78a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78944.md#insn-00b78a20) · [`00b78998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78944.md#insn-00b78998) · [`00b789b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78944.md#insn-00b789b4)

~~~diff
- 00b789dc ["INT_ADD", "register:40f0:8", ["const:b789dc:8", "const:4:8"]]
- 00b789dc ["CALL", null, ["callee:0045efa8:8"]]
+ 00b78a20 ["INT_ADD", "register:40f0:8", ["const:b78a20:8", "const:4:8"]]
+ 00b78a20 ["CALL", null, ["callee:0045efa8:8"]]
- 00b789dc bytes 7399e397
+ 00b78a20 bytes 6299e397
- 00b78954 ["INT_ADD", "register:40f0:8", ["const:b78954:8", "const:4:8"]]
- 00b78954 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b78998 ["INT_ADD", "register:40f0:8", ["const:b78998:8", "const:4:8"]]
+ 00b78998 ["CALL", null, ["callee:00bdb270:8"]]
- 00b78954 bytes 338a0194
+ 00b78998 bytes 368a0194
- 00b78970 ["INT_ADD", "register:40f0:8", ["const:b78970:8", "const:4:8"]]
- 00b78970 ["CALL", null, ["callee:00be1090:8"]]
+ 00b789b4 ["INT_ADD", "register:40f0:8", ["const:b789b4:8", "const:4:8"]]
+ 00b789b4 ["CALL", null, ["callee:00be1090:8"]]
- 00b78970 bytes b4a10194
+ 00b789b4 bytes b7a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-976d9dda9be6d0257ac4ea4e12022b6d"></a>

### [`00b78a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78a20.md) → [`00b78a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78a64.md) _ZNSt6__ndk15stoulERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md)

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
      "definition_site": "00b78b68",
      "incomplete_value": true,
      "site": "00b78b68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78b24",
      "incomplete_value": true,
      "site": "00b78b24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55:8"
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
      "definition_site": "00b78b6c",
      "incomplete_value": true,
      "site": "00b78b6c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b78b28",
      "incomplete_value": true,
      "site": "00b78b28",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b78ba8",
      "incomplete_value": true,
      "site": "00b78ba8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78b64",
      "incomplete_value": true,
      "site": "00b78b64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "00b78b50",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b78b58",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78b90",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78b50",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b78b58",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b78b90",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78a20.md#insn-00b78a78) · [`00b78a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78a20.md#insn-00b78a94) · [`00b78ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78a20.md#insn-00b78ad0)
- 新版 [`00b78abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78a64.md#insn-00b78abc) · [`00b78ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78a64.md#insn-00b78ad8) · [`00b78b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78a64.md#insn-00b78b14)

~~~diff
- 00b78a78 ["INT_ADD", "register:40f0:8", ["const:b78a78:8", "const:4:8"]]
- 00b78a78 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b78abc ["INT_ADD", "register:40f0:8", ["const:b78abc:8", "const:4:8"]]
+ 00b78abc ["CALL", null, ["callee:00bdb270:8"]]
- 00b78a78 bytes ea890194
+ 00b78abc bytes ed890194
- 00b78a94 ["INT_ADD", "register:40f0:8", ["const:b78a94:8", "const:4:8"]]
- 00b78a94 ["CALL", null, ["callee:00be10a0:8"]]
+ 00b78ad8 ["INT_ADD", "register:40f0:8", ["const:b78ad8:8", "const:4:8"]]
+ 00b78ad8 ["CALL", null, ["callee:00be10a0:8"]]
- 00b78a94 bytes 6fa10194
+ 00b78ad8 bytes 72a10194
- 00b78ad0 ["INT_ADD", "register:40f0:8", ["const:b78ad0:8", "const:4:8"]]
- 00b78ad0 ["CALL", null, ["callee:00be1060:8"]]
+ 00b78b14 ["INT_ADD", "register:40f0:8", ["const:b78b14:8", "const:4:8"]]
+ 00b78b14 ["CALL", null, ["callee:00be1060:8"]]
- 00b78ad0 bytes 50a10194
+ 00b78b14 bytes 53a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-393c14205a5c1fe6eb72abfed7993fc1"></a>

### [`00b78b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78b9c.md) → [`00b78be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78be0.md) _ZNSt6__ndk15stollERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md)

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
      "definition_site": "00b78ce4",
      "incomplete_value": true,
      "site": "00b78ce4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78ca0",
      "incomplete_value": true,
      "site": "00b78ca0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55:8"
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
      "definition_site": "00b78ce8",
      "incomplete_value": true,
      "site": "00b78ce8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b78ca4",
      "incomplete_value": true,
      "site": "00b78ca4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b78d24",
      "incomplete_value": true,
      "site": "00b78d24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78ce0",
      "incomplete_value": true,
      "site": "00b78ce0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "00b78ccc",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b78cd4",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78d0c",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78ccc",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b78cd4",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b78d0c",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78b9c.md#insn-00b78bf4) · [`00b78c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78b9c.md#insn-00b78c10) · [`00b78c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78b9c.md#insn-00b78c4c)
- 新版 [`00b78c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78be0.md#insn-00b78c38) · [`00b78c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78be0.md#insn-00b78c54) · [`00b78c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78be0.md#insn-00b78c90)

~~~diff
- 00b78bf4 ["INT_ADD", "register:40f0:8", ["const:b78bf4:8", "const:4:8"]]
- 00b78bf4 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b78c38 ["INT_ADD", "register:40f0:8", ["const:b78c38:8", "const:4:8"]]
+ 00b78c38 ["CALL", null, ["callee:00bdb270:8"]]
- 00b78bf4 bytes 8b890194
+ 00b78c38 bytes 8e890194
- 00b78c10 ["INT_ADD", "register:40f0:8", ["const:b78c10:8", "const:4:8"]]
- 00b78c10 ["CALL", null, ["callee:00be10b0:8"]]
+ 00b78c54 ["INT_ADD", "register:40f0:8", ["const:b78c54:8", "const:4:8"]]
+ 00b78c54 ["CALL", null, ["callee:00be10b0:8"]]
- 00b78c10 bytes 14a10194
+ 00b78c54 bytes 17a10194
- 00b78c4c ["INT_ADD", "register:40f0:8", ["const:b78c4c:8", "const:4:8"]]
- 00b78c4c ["CALL", null, ["callee:00be1060:8"]]
+ 00b78c90 ["INT_ADD", "register:40f0:8", ["const:b78c90:8", "const:4:8"]]
+ 00b78c90 ["CALL", null, ["callee:00be1060:8"]]
- 00b78c4c bytes f1a00194
+ 00b78c90 bytes f4a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27c4a64194d36a30dde168c4d72df3f6"></a>

### [`00b78d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78d18.md) → [`00b78d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78d5c.md) _ZNSt6__ndk16stoullERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md)

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
      "definition_site": "00b78e64",
      "incomplete_value": true,
      "site": "00b78e64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78e20",
      "incomplete_value": true,
      "site": "00b78e20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55:8"
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
      "definition_site": "00b78e68",
      "incomplete_value": true,
      "site": "00b78e68",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b78e24",
      "incomplete_value": true,
      "site": "00b78e24",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b78ea4",
      "incomplete_value": true,
      "site": "00b78ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78e60",
      "incomplete_value": true,
      "site": "00b78e60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "00b78e4c",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b78e54",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78e8c",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78e4c",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b78e54",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b78e8c",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78d18.md#insn-00b78d74) · [`00b78d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78d18.md#insn-00b78d90) · [`00b78dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78d18.md#insn-00b78dcc)
- 新版 [`00b78db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78d5c.md#insn-00b78db8) · [`00b78dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78d5c.md#insn-00b78dd4) · [`00b78e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78d5c.md#insn-00b78e10)

~~~diff
- 00b78d74 ["INT_ADD", "register:40f0:8", ["const:b78d74:8", "const:4:8"]]
- 00b78d74 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b78db8 ["INT_ADD", "register:40f0:8", ["const:b78db8:8", "const:4:8"]]
+ 00b78db8 ["CALL", null, ["callee:00bdb270:8"]]
- 00b78d74 bytes 2b890194
+ 00b78db8 bytes 2e890194
- 00b78d90 ["INT_ADD", "register:40f0:8", ["const:b78d90:8", "const:4:8"]]
- 00b78d90 ["CALL", null, ["callee:00be10c0:8"]]
+ 00b78dd4 ["INT_ADD", "register:40f0:8", ["const:b78dd4:8", "const:4:8"]]
+ 00b78dd4 ["CALL", null, ["callee:00be10c0:8"]]
- 00b78d90 bytes b8a00194
+ 00b78dd4 bytes bba00194
- 00b78dcc ["INT_ADD", "register:40f0:8", ["const:b78dcc:8", "const:4:8"]]
- 00b78dcc ["CALL", null, ["callee:00be1060:8"]]
+ 00b78e10 ["INT_ADD", "register:40f0:8", ["const:b78e10:8", "const:4:8"]]
+ 00b78e10 ["CALL", null, ["callee:00be1060:8"]]
- 00b78dcc bytes 91a00194
+ 00b78e10 bytes 94a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4fb5153bfe8d491ee939c32462dd3bb"></a>

### [`00b78e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78e98.md) → [`00b78edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78edc.md) _ZNSt6__ndk14stofERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md)

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
      "definition_site": "00b78fc0",
      "incomplete_value": true,
      "site": "00b78fc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78f7c",
      "incomplete_value": true,
      "site": "00b78f7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55:8"
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
      "definition_site": "00b78fc8",
      "incomplete_value": true,
      "site": "00b78fc8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b78f84",
      "incomplete_value": true,
      "site": "00b78f84",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b78ff8",
      "incomplete_value": true,
      "site": "00b78ff8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78fb4",
      "incomplete_value": true,
      "site": "00b78fb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "00b78fb0",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b78fb4",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b78fe8",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78fb0",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b78fb4",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b78fe8",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78e98.md#insn-00b78ee8) · [`00b78f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78e98.md#insn-00b78f00) · [`00b78f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78e98.md#insn-00b78f34)
- 新版 [`00b78f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78edc.md#insn-00b78f2c) · [`00b78f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78edc.md#insn-00b78f44) · [`00b78f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78edc.md#insn-00b78f78)

~~~diff
- 00b78ee8 ["INT_ADD", "register:40f0:8", ["const:b78ee8:8", "const:4:8"]]
- 00b78ee8 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b78f2c ["INT_ADD", "register:40f0:8", ["const:b78f2c:8", "const:4:8"]]
+ 00b78f2c ["CALL", null, ["callee:00bdb270:8"]]
- 00b78ee8 bytes ce880194
+ 00b78f2c bytes d1880194
- 00b78f00 ["INT_ADD", "register:40f0:8", ["const:b78f00:8", "const:4:8"]]
- 00b78f00 ["CALL", null, ["callee:00be10d0:8"]]
+ 00b78f44 ["INT_ADD", "register:40f0:8", ["const:b78f44:8", "const:4:8"]]
+ 00b78f44 ["CALL", null, ["callee:00be10d0:8"]]
- 00b78f00 bytes 60a00194
+ 00b78f44 bytes 63a00194
- 00b78f34 ["INT_ADD", "register:40f0:8", ["const:b78f34:8", "const:4:8"]]
- 00b78f34 ["CALL", null, ["callee:00be1060:8"]]
+ 00b78f78 ["INT_ADD", "register:40f0:8", ["const:b78f78:8", "const:4:8"]]
+ 00b78f78 ["CALL", null, ["callee:00be1060:8"]]
- 00b78f34 bytes 37a00194
+ 00b78f78 bytes 3aa00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e2b4324e72a90d80c72e141584ab0ff"></a>

### [`00b78ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78ff0.md) → [`00b79034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79034.md) _ZNSt6__ndk14stodERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.94% / 新版 92.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b79150",
      "incomplete_value": true,
      "site": "00b79150",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7910c",
      "incomplete_value": true,
      "site": "00b7910c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b79158",
      "incomplete_value": true,
      "site": "00b79158",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b79114",
      "incomplete_value": true,
      "site": "00b79114",
      "value": [
        "LOAD",
        "8",
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
      "00b79108",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b7910c",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b79140",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b79108",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b7910c",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b79140",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b79040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78ff0.md#insn-00b79040) · [`00b79058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78ff0.md#insn-00b79058) · [`00b7908c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78ff0.md#insn-00b7908c)
- 新版 [`00b79084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79034.md#insn-00b79084) · [`00b7909c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79034.md#insn-00b7909c) · [`00b790d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79034.md#insn-00b790d0)

~~~diff
- 00b79040 ["INT_ADD", "register:40f0:8", ["const:b79040:8", "const:4:8"]]
- 00b79040 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b79084 ["INT_ADD", "register:40f0:8", ["const:b79084:8", "const:4:8"]]
+ 00b79084 ["CALL", null, ["callee:00bdb270:8"]]
- 00b79040 bytes 78880194
+ 00b79084 bytes 7b880194
- 00b79058 ["INT_ADD", "register:40f0:8", ["const:b79058:8", "const:4:8"]]
- 00b79058 ["CALL", null, ["callee:00be10e0:8"]]
+ 00b7909c ["INT_ADD", "register:40f0:8", ["const:b7909c:8", "const:4:8"]]
+ 00b7909c ["CALL", null, ["callee:00be10e0:8"]]
- 00b79058 bytes 0ea00194
+ 00b7909c bytes 11a00194
- 00b7908c ["INT_ADD", "register:40f0:8", ["const:b7908c:8", "const:4:8"]]
- 00b7908c ["CALL", null, ["callee:00be1060:8"]]
+ 00b790d0 ["INT_ADD", "register:40f0:8", ["const:b790d0:8", "const:4:8"]]
+ 00b790d0 ["CALL", null, ["callee:00be1060:8"]]
- 00b7908c bytes e19f0194
+ 00b790d0 bytes e49f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4acd7f539bc525201fcbde8a4451df2e"></a>

### [`00b79148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79148.md) → [`00b7918c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7918c.md) _ZNSt6__ndk15stoldERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b79280",
      "incomplete_value": true,
      "site": "00b79280",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7923c",
      "incomplete_value": true,
      "site": "00b7923c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55:8"
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
      "definition_site": "00b79284",
      "incomplete_value": true,
      "site": "00b79284",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b79240",
      "incomplete_value": true,
      "site": "00b79240",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b79268",
      "READ",
      [
        "storage",
        "002a9055",
        null,
        "string"
      ]
    ],
    [
      "00b79270",
      "READ",
      [
        "storage",
        "002a905b",
        null,
        "string"
      ]
    ],
    [
      "00b792a8",
      "READ",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b79268",
      "READ",
      [
        "storage",
        "002a90ef",
        null,
        "string"
      ]
    ],
    [
      "00b79270",
      "READ",
      [
        "storage",
        "002a90f5",
        null,
        "string"
      ]
    ],
    [
      "00b792a8",
      "READ",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b79198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79148.md#insn-00b79198) · [`00b791b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79148.md#insn-00b791b0) · [`00b791ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79148.md#insn-00b791ec)
- 新版 [`00b791dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7918c.md#insn-00b791dc) · [`00b791f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7918c.md#insn-00b791f4) · [`00b79230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7918c.md#insn-00b79230)

~~~diff
- 00b79198 ["INT_ADD", "register:40f0:8", ["const:b79198:8", "const:4:8"]]
- 00b79198 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b791dc ["INT_ADD", "register:40f0:8", ["const:b791dc:8", "const:4:8"]]
+ 00b791dc ["CALL", null, ["callee:00bdb270:8"]]
- 00b79198 bytes 22880194
+ 00b791dc bytes 25880194
- 00b791b0 ["INT_ADD", "register:40f0:8", ["const:b791b0:8", "const:4:8"]]
- 00b791b0 ["CALL", null, ["callee:00be10f0:8"]]
+ 00b791f4 ["INT_ADD", "register:40f0:8", ["const:b791f4:8", "const:4:8"]]
+ 00b791f4 ["CALL", null, ["callee:00be10f0:8"]]
- 00b791b0 bytes bc9f0194
+ 00b791f4 bytes bf9f0194
- 00b791ec ["INT_ADD", "register:40f0:8", ["const:b791ec:8", "const:4:8"]]
- 00b791ec ["CALL", null, ["callee:00be1060:8"]]
+ 00b79230 ["INT_ADD", "register:40f0:8", ["const:b79230:8", "const:4:8"]]
+ 00b79230 ["CALL", null, ["callee:00be1060:8"]]
- 00b791ec bytes 899f0194
+ 00b79230 bytes 8c9f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a57cdfbf55185f2c0cfb57c9ff9ab28a"></a>

### [`00b7b2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md) → [`00b7b30c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b30c.md) FUN_00b7b30c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b77cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cec.md) [`00b77e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77e48.md) [`00b7879c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b7879c.md) [`00b78900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78900.md) · 呼出先 4件 [`0045efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045efa8.md) [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00be1010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1010.md)
- 新版 呼出元 4件 [`00b77d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77d30.md) [`00b77e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77e8c.md) [`00b787e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b787e0.md) [`00b78944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78944.md) · 呼出先 4件 [`0045efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045efa8.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md)

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
      "definition_site": "00b7b324",
      "incomplete_value": false,
      "site": "00b7b330",
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
            "const:7f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b2e0",
      "incomplete_value": false,
      "site": "00b7b2ec",
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
            "const:880:8"
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
      "00b7b324",
      "PARAM",
      [
        "storage",
        "00297880",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7b324",
      "PARAM",
      [
        "storage",
        "002977f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md#insn-00b7b2ec) · [`00b7b2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md#insn-00b7b2e0) · [`00b7b300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b2c8.md#insn-00b7b300)
- 新版 [`00b7b330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b30c.md#insn-00b7b330) · [`00b7b324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b30c.md#insn-00b7b324) · [`00b7b344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b30c.md#insn-00b7b344)

~~~diff
- 00b7b2ec ["INT_ADD", "register:40f0:8", ["const:b7b2ec:8", "const:4:8"]]
- 00b7b2ec ["CALL", null, ["callee:0045efa8:8"]]
+ 00b7b330 ["INT_ADD", "register:40f0:8", ["const:b7b330:8", "const:4:8"]]
+ 00b7b330 ["CALL", null, ["callee:0045efa8:8"]]
- 00b7b2ec bytes 2f8fe397
+ 00b7b330 bytes 1e8fe397
- 00b7b2e0 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00b7b2e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b7b2e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b7b2e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b7b324 ["COPY", "tmp:0:8", ["const:7f3:8"]]
+ 00b7b324 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7b324 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7b324 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b7b2e0 bytes 21002291
+ 00b7b324 bytes 21cc1f91
- 00b7b300 ["INT_ADD", "register:40f0:8", ["const:b7b300:8", "const:4:8"]]
- 00b7b300 ["CALL", null, ["callee:00b7b35c:8"]]
+ 00b7b344 ["INT_ADD", "register:40f0:8", ["const:b7b344:8", "const:4:8"]]
+ 00b7b344 ["CALL", null, ["callee:00b7b35c:8"]]
- 00b7b300 bytes 06000094
+ 00b7b344 bytes 06000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff80404163fc738b10daa2c733e4119f"></a>

### [`00b7b318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md) → [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) FUN_00b7b35c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 13件 [`00b77f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77f60.md) [`00b780cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b780cc.md) [`00b78238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78238.md) [`00b783a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b783a8.md) [`00b784f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b784f0.md) · 呼出先 4件 [`00b7b36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b36c.md) [`00bbae18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae18.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 13件 [`00b77fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77fa4.md) [`00b78110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78110.md) [`00b7827c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b7827c.md) [`00b783ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b783ec.md) [`00b78534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b78/00b78534.md) · 呼出先 4件 [`00b7b3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3b0.md) [`00bbae5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae5c.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "00b7b390",
      "incomplete_value": true,
      "site": "00b7b398",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b34c",
      "incomplete_value": true,
      "site": "00b7b354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c38:8"
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
      "definition_site": "00b7b394",
      "incomplete_value": true,
      "site": "00b7b398",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b350",
      "incomplete_value": true,
      "site": "00b7b354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c40:8"
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
      "00b7b390",
      "READ",
      [
        "storage",
        "00c1bc38",
        null,
        "pointer"
      ]
    ],
    [
      "00b7b390",
      "PARAM",
      [
        "storage",
        "00c169a0",
        "_ZTISt16invalid_argument",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b7b394",
      "READ",
      [
        "storage",
        "00c1bc40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7b390",
      "READ",
      [
        "storage",
        "00c1bc88",
        null,
        "pointer"
      ]
    ],
    [
      "00b7b390",
      "PARAM",
      [
        "storage",
        "00c169f0",
        "_ZTISt16invalid_argument",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b7b394",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md#insn-00b7b354) · [`00b7b330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md#insn-00b7b330) · [`00b7b33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b318.md#insn-00b7b33c)
- 新版 [`00b7b398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md#insn-00b7b398) · [`00b7b374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md#insn-00b7b374) · [`00b7b380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md#insn-00b7b380)

~~~diff
- 00b7b354 ["INT_ADD", "register:40f0:8", ["const:b7b354:8", "const:4:8"]]
- 00b7b354 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 00b7b398 ["INT_ADD", "register:40f0:8", ["const:b7b398:8", "const:4:8"]]
+ 00b7b398 ["CALL", null, ["callee:00bdb0c0:8"]]
- 00b7b354 bytes 477f0194
+ 00b7b398 bytes 4a7f0194
- 00b7b330 ["INT_ADD", "register:40f0:8", ["const:b7b330:8", "const:4:8"]]
- 00b7b330 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b7b374 ["INT_ADD", "register:40f0:8", ["const:b7b374:8", "const:4:8"]]
+ 00b7b374 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b7b330 bytes 487f0194
+ 00b7b374 bytes 4b7f0194
- 00b7b33c ["INT_ADD", "register:40f0:8", ["const:b7b33c:8", "const:4:8"]]
- 00b7b33c ["CALL", null, ["callee:00b7b3b0:8"]]
+ 00b7b380 ["INT_ADD", "register:40f0:8", ["const:b7b380:8", "const:4:8"]]
+ 00b7b380 ["CALL", null, ["callee:00b7b3b0:8"]]
- 00b7b33c bytes 0c000094
+ 00b7b380 bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7f04d47a6153bedc3aeb17f65a57ef2"></a>

### [`00b7b75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b75c.md) → [`00b7b7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b7a0.md) FUN_00b7b7a0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00b7b890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b890.md) [`00b7b958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b958.md) [`00b7dfc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dfc4.md) · 呼出先 8件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md)
- 新版 呼出元 3件 [`00b7b8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b8d4.md) [`00b7b99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b99c.md) [`00b7e008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e008.md) · 呼出先 8件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md)

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
      "definition_site": "00b7b810",
      "incomplete_value": false,
      "site": "00b7b824",
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
            "const:2ac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b7cc",
      "incomplete_value": false,
      "site": "00b7b7e0",
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
            "const:212:8"
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
      "00b7b804",
      "READ",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7b810",
      "PARAM",
      [
        "storage",
        "002a7212",
        null,
        "string"
      ]
    ],
    [
      "00b7b828",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7b804",
      "READ",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7b810",
      "PARAM",
      [
        "storage",
        "002a72ac",
        null,
        "string"
      ]
    ],
    [
      "00b7b828",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b79c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b75c.md#insn-00b7b79c) · [`00b7b7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b75c.md#insn-00b7b7e0) · [`00b7b780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b75c.md#insn-00b7b780)
- 新版 [`00b7b7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b7a0.md#insn-00b7b7e0) · [`00b7b824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b7a0.md#insn-00b7b824) · [`00b7b7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b7a0.md#insn-00b7b7c4)

~~~diff
- 00b7b79c ["INT_ADD", "register:40f0:8", ["const:b7b79c:8", "const:4:8"]]
- 00b7b79c ["CALL", null, ["callee:00be1190:8"]]
+ 00b7b7e0 ["INT_ADD", "register:40f0:8", ["const:b7b7e0:8", "const:4:8"]]
+ 00b7b7e0 ["CALL", null, ["callee:00be1190:8"]]
- 00b7b79c bytes 69960194
+ 00b7b7e0 bytes 6c960194
- 00b7b7e0 ["INT_ADD", "register:40f0:8", ["const:b7b7e0:8", "const:4:8"]]
- 00b7b7e0 ["CALL", null, ["callee:00be1100:8"]]
+ 00b7b824 ["INT_ADD", "register:40f0:8", ["const:b7b824:8", "const:4:8"]]
+ 00b7b824 ["CALL", null, ["callee:00be1100:8"]]
- 00b7b7e0 bytes 34960194
+ 00b7b824 bytes 37960194
- 00b7b780 ["INT_ADD", "register:40f0:8", ["const:b7b780:8", "const:4:8"]]
- 00b7b780 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b7b7c4 ["INT_ADD", "register:40f0:8", ["const:b7b7c4:8", "const:4:8"]]
+ 00b7b7c4 ["CALL", null, ["callee:00bdb270:8"]]
- 00b7b780 bytes a87e0194
+ 00b7b7c4 bytes ab7e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-927b9b78bae380cc895fd5372b7192f9"></a>

### [`00b7b890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b890.md) → [`00b7b8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b8d4.md) FUN_00b7b8d4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7b75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b75c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b7b7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b7a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7b914",
      "incomplete_value": true,
      "site": "00b7b920",
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
                "const:6b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b8d0",
      "incomplete_value": true,
      "site": "00b7b8dc",
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
                "const:740:8"
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
      "definition_site": "00b7b914",
      "incomplete_value": true,
      "site": "00b7b920",
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
      "definition_site": "00b7b8d0",
      "incomplete_value": true,
      "site": "00b7b8dc",
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
      "00b7b914",
      "READ",
      [
        "storage",
        "00296740",
        null,
        "string"
      ]
    ],
    [
      "00b7b914",
      "READ",
      [
        "storage",
        "00296750",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7b914",
      "READ",
      [
        "storage",
        "002966b3",
        null,
        "string"
      ]
    ],
    [
      "00b7b914",
      "READ",
      [
        "storage",
        "002966c3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b890.md#insn-00b7b8b4) · [`00b7b8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b890.md#insn-00b7b8cc)
- 新版 [`00b7b8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b8d4.md#insn-00b7b8f8) · [`00b7b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b8d4.md#insn-00b7b910)

~~~diff
- 00b7b8b4 ["INT_ADD", "register:40f0:8", ["const:b7b8b4:8", "const:4:8"]]
- 00b7b8b4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7b8f8 ["INT_ADD", "register:40f0:8", ["const:b7b8f8:8", "const:4:8"]]
+ 00b7b8f8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7b8b4 bytes cf7d0194
+ 00b7b8f8 bytes d27d0194
- 00b7b8cc ["COPY", "tmp:0:8", ["const:740:8"]]
- 00b7b8cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b7b8cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b7b8cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b7b910 ["COPY", "tmp:0:8", ["const:6b3:8"]]
+ 00b7b910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7b910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7b910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b7b8cc bytes 08011d91
+ 00b7b910 bytes 08cd1a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a528d3cca1eadf69b60959749bc9789"></a>

### [`00b7b8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b8f8.md) → [`00b7b93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b93c.md) _ZNSt6__ndk116generic_categoryEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

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
      "definition_site": "00b7b970",
      "incomplete_value": false,
      "site": "00b7b974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b92c",
      "incomplete_value": false,
      "site": "00b7b930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
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
    "new": {
      "definition_site": "00b7b980",
      "incomplete_value": false,
      "site": "00b7b984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b93c",
      "incomplete_value": false,
      "site": "00b7b940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00b7b95c",
      "incomplete_value": false,
      "site": "00b7b968",
      "value": [
        "leaf",
        "const:c24908:8"
      ]
    },
    "old": {
      "definition_site": "00b7b918",
      "incomplete_value": false,
      "site": "00b7b924",
      "value": [
        "leaf",
        "const:c248b8:8"
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
      "00b7b950",
      "READ",
      [
        "storage",
        "010a2018",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7b95c",
      "DATA",
      [
        "storage",
        "00c248b8",
        null,
        "pointer"
      ]
    ],
    [
      "00b7b970",
      "PARAM",
      [
        "storage",
        "010a2018",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7b950",
      "READ",
      [
        "storage",
        "010a2058",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7b95c",
      "DATA",
      [
        "storage",
        "00c24908",
        null,
        "pointer"
      ]
    ],
    [
      "00b7b970",
      "PARAM",
      [
        "storage",
        "010a2058",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b8f8.md#insn-00b7b930) · [`00b7b940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b8f8.md#insn-00b7b940) · [`00b7b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b8f8.md#insn-00b7b908)
- 新版 [`00b7b974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b93c.md#insn-00b7b974) · [`00b7b984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b93c.md#insn-00b7b984) · [`00b7b94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b93c.md#insn-00b7b94c)

~~~diff
- 00b7b930 ["INT_ADD", "register:40f0:8", ["const:b7b930:8", "const:4:8"]]
- 00b7b930 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b7b974 ["INT_ADD", "register:40f0:8", ["const:b7b974:8", "const:4:8"]]
+ 00b7b974 ["CALL", null, ["callee:00bdb000:8"]]
- 00b7b930 bytes a07d0194
+ 00b7b974 bytes a37d0194
- 00b7b940 ["INT_ADD", "register:40f0:8", ["const:b7b940:8", "const:4:8"]]
- 00b7b940 ["CALL", null, ["callee:00bdb020:8"]]
+ 00b7b984 ["INT_ADD", "register:40f0:8", ["const:b7b984:8", "const:4:8"]]
+ 00b7b984 ["CALL", null, ["callee:00bdb020:8"]]
- 00b7b940 bytes a47d0194
+ 00b7b984 bytes a77d0194
- 00b7b908 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00b7b908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b7b908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b7b908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b7b94c ["COPY", "tmp:0:8", ["const:58:8"]]
+ 00b7b94c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7b94c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7b94c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b7b908 bytes 08610091
+ 00b7b94c bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4190612bc03e8b5ddfbe6c45ef9cab6"></a>

### [`00b7b9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b9e0.md) → [`00b7ba24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7ba24.md) _ZNSt6__ndk115system_categoryEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

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
      "definition_site": "00b7ba58",
      "incomplete_value": false,
      "site": "00b7ba5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7ba14",
      "incomplete_value": false,
      "site": "00b7ba18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "00b7ba68",
      "incomplete_value": false,
      "site": "00b7ba6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7ba24",
      "incomplete_value": false,
      "site": "00b7ba28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "00b7ba44",
      "incomplete_value": false,
      "site": "00b7ba50",
      "value": [
        "leaf",
        "const:c24910:8"
      ]
    },
    "old": {
      "definition_site": "00b7ba00",
      "incomplete_value": false,
      "site": "00b7ba0c",
      "value": [
        "leaf",
        "const:c248c0:8"
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
      "00b7ba38",
      "READ",
      [
        "storage",
        "010a2020",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7ba44",
      "DATA",
      [
        "storage",
        "00c248c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ba58",
      "PARAM",
      [
        "storage",
        "010a2020",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7ba38",
      "READ",
      [
        "storage",
        "010a2060",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7ba44",
      "DATA",
      [
        "storage",
        "00c24910",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ba58",
      "PARAM",
      [
        "storage",
        "010a2060",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ba18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b9e0.md#insn-00b7ba18) · [`00b7ba28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b9e0.md#insn-00b7ba28) · [`00b7b9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b9e0.md#insn-00b7b9f0)
- 新版 [`00b7ba5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7ba24.md#insn-00b7ba5c) · [`00b7ba6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7ba24.md#insn-00b7ba6c) · [`00b7ba34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7ba24.md#insn-00b7ba34)

~~~diff
- 00b7ba18 ["INT_ADD", "register:40f0:8", ["const:b7ba18:8", "const:4:8"]]
- 00b7ba18 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b7ba5c ["INT_ADD", "register:40f0:8", ["const:b7ba5c:8", "const:4:8"]]
+ 00b7ba5c ["CALL", null, ["callee:00bdb000:8"]]
- 00b7ba18 bytes 667d0194
+ 00b7ba5c bytes 697d0194
- 00b7ba28 ["INT_ADD", "register:40f0:8", ["const:b7ba28:8", "const:4:8"]]
- 00b7ba28 ["CALL", null, ["callee:00bdb020:8"]]
+ 00b7ba6c ["INT_ADD", "register:40f0:8", ["const:b7ba6c:8", "const:4:8"]]
+ 00b7ba6c ["CALL", null, ["callee:00bdb020:8"]]
- 00b7ba28 bytes 6a7d0194
+ 00b7ba6c bytes 6d7d0194
- 00b7b9f0 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00b7b9f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b7b9f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b7b9f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b7ba34 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 00b7ba34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7ba34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7ba34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b7b9f0 bytes 08810091
+ 00b7ba34 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79860ff2c9683f337d3e79a25dfafa17"></a>

### [`00b7c1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c1d4.md) → [`00b7c218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c218.md) FUN_00b7c218

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b7c1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c1b4.md) · 呼出先 4件 [`00b7c180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c180.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00be1160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1160.md)
- 新版 呼出元 1件 [`00b7c1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c1f8.md) · 呼出先 4件 [`00b7c1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c1c4.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00be11b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11b0.md)

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
      "definition_site": "00b7c260",
      "incomplete_value": true,
      "site": "00b7c268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c21c",
      "incomplete_value": true,
      "site": "00b7c224",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c60:8"
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
      "definition_site": "00b7c264",
      "incomplete_value": true,
      "site": "00b7c268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c220",
      "incomplete_value": true,
      "site": "00b7c224",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
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
      "00b7c260",
      "READ",
      [
        "storage",
        "00c1bc60",
        null,
        "pointer"
      ]
    ],
    [
      "00b7c260",
      "PARAM",
      [
        "storage",
        "00c12da8",
        "_ZTINSt6__ndk112system_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b7c264",
      "READ",
      [
        "storage",
        "00c1bc58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7c260",
      "READ",
      [
        "storage",
        "00c1bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7c260",
      "PARAM",
      [
        "storage",
        "00c12df8",
        "_ZTINSt6__ndk112system_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b7c264",
      "READ",
      [
        "storage",
        "00c1bca8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c1d4.md#insn-00b7c224) · [`00b7c1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c1d4.md#insn-00b7c1f8) · [`00b7c20c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c1d4.md#insn-00b7c20c)
- 新版 [`00b7c268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c218.md#insn-00b7c268) · [`00b7c23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c218.md#insn-00b7c23c) · [`00b7c250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c218.md#insn-00b7c250)

~~~diff
- 00b7c224 ["INT_ADD", "register:40f0:8", ["const:b7c224:8", "const:4:8"]]
- 00b7c224 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 00b7c268 ["INT_ADD", "register:40f0:8", ["const:b7c268:8", "const:4:8"]]
+ 00b7c268 ["CALL", null, ["callee:00bdb0c0:8"]]
- 00b7c224 bytes 937b0194
+ 00b7c268 bytes 967b0194
- 00b7c1f8 ["INT_ADD", "register:40f0:8", ["const:b7c1f8:8", "const:4:8"]]
- 00b7c1f8 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00b7c23c ["INT_ADD", "register:40f0:8", ["const:b7c23c:8", "const:4:8"]]
+ 00b7c23c ["CALL", null, ["callee:00bdb0a0:8"]]
- 00b7c1f8 bytes 967b0194
+ 00b7c23c bytes 997b0194
- 00b7c20c ["INT_ADD", "register:40f0:8", ["const:b7c20c:8", "const:4:8"]]
- 00b7c20c ["CALL", null, ["callee:00be11b0:8"]]
+ 00b7c250 ["INT_ADD", "register:40f0:8", ["const:b7c250:8", "const:4:8"]]
+ 00b7c250 ["CALL", null, ["callee:00be11b0:8"]]
- 00b7c20c bytes d5930194
+ 00b7c250 bytes d8930194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c231dbadd91ac769d990c2410d5df42d"></a>

### [`00b7c51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c51c.md) → [`00b7c560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c560.md) FUN_00b7c560

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7c5c0",
      "incomplete_value": true,
      "site": "00b7c5cc",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c57c",
      "incomplete_value": true,
      "site": "00b7c588",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
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
      "definition_site": "00b7c5c8",
      "incomplete_value": true,
      "site": "00b7c5d0",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c584",
      "incomplete_value": true,
      "site": "00b7c58c",
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
                "const:20:8"
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
      "definition_site": "00b7c5c8",
      "incomplete_value": true,
      "site": "00b7c5d0",
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
      "definition_site": "00b7c584",
      "incomplete_value": true,
      "site": "00b7c58c",
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
      "00b7c5c0",
      "READ",
      [
        "storage",
        "00294426",
        null,
        "string"
      ]
    ],
    [
      "00b7c5c8",
      "READ",
      [
        "storage",
        "00294406",
        null,
        "string"
      ]
    ],
    [
      "00b7c5c8",
      "READ",
      [
        "storage",
        "00294416",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7c5c0",
      "READ",
      [
        "storage",
        "00294399",
        null,
        "string"
      ]
    ],
    [
      "00b7c5c8",
      "READ",
      [
        "storage",
        "00294379",
        null,
        "string"
      ]
    ],
    [
      "00b7c5c8",
      "READ",
      [
        "storage",
        "00294389",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c51c.md#insn-00b7c624) · [`00b7c564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c51c.md#insn-00b7c564) · [`00b7c578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c51c.md#insn-00b7c578)
- 新版 [`00b7c668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c560.md#insn-00b7c668) · [`00b7c5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c560.md#insn-00b7c5a8) · [`00b7c5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c560.md#insn-00b7c5bc)

~~~diff
- 00b7c624 ["INT_ADD", "register:40f0:8", ["const:b7c624:8", "const:4:8"]]
- 00b7c624 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7c668 ["INT_ADD", "register:40f0:8", ["const:b7c668:8", "const:4:8"]]
+ 00b7c668 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7c624 bytes 737a0194
+ 00b7c668 bytes 767a0194
- 00b7c564 ["INT_ADD", "register:40f0:8", ["const:b7c564:8", "const:4:8"]]
- 00b7c564 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7c5a8 ["INT_ADD", "register:40f0:8", ["const:b7c5a8:8", "const:4:8"]]
+ 00b7c5a8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b7c564 bytes a37a0194
+ 00b7c5a8 bytes a67a0194
- 00b7c578 ["COPY", "tmp:0:8", ["const:3e6:8"]]
- 00b7c578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b7c578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b7c578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b7c5bc ["COPY", "tmp:0:8", ["const:359:8"]]
+ 00b7c5bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7c5bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7c5bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b7c578 bytes 08990f91
+ 00b7c5bc bytes 08650d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40d8721c498f036df0680944b7b8e949"></a>

### [`00b7c6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c6a8.md) → [`00b7c6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c6ec.md) _ZNSt6__ndk115future_categoryEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb470.md) · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00bdb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4c0.md) · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

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
      "definition_site": "00b7c720",
      "incomplete_value": false,
      "site": "00b7c724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c6dc",
      "incomplete_value": false,
      "site": "00b7c6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "definition_site": "00b7c730",
      "incomplete_value": false,
      "site": "00b7c734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c6ec",
      "incomplete_value": false,
      "site": "00b7c6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "definition_site": "00b7c70c",
      "incomplete_value": false,
      "site": "00b7c718",
      "value": [
        "leaf",
        "const:c24918:8"
      ]
    },
    "old": {
      "definition_site": "00b7c6c8",
      "incomplete_value": false,
      "site": "00b7c6d4",
      "value": [
        "leaf",
        "const:c248c8:8"
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
      "00b7c700",
      "READ",
      [
        "storage",
        "010a2028",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7c70c",
      "DATA",
      [
        "storage",
        "00c248c8",
        null,
        null
      ]
    ],
    [
      "00b7c720",
      "PARAM",
      [
        "storage",
        "010a2028",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7c700",
      "READ",
      [
        "storage",
        "010a2068",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7c70c",
      "DATA",
      [
        "storage",
        "00c24918",
        null,
        null
      ]
    ],
    [
      "00b7c720",
      "PARAM",
      [
        "storage",
        "010a2068",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c6a8.md#insn-00b7c6e0) · [`00b7c6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c6a8.md#insn-00b7c6f0) · [`00b7c6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c6a8.md#insn-00b7c6b8)
- 新版 [`00b7c724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c6ec.md#insn-00b7c724) · [`00b7c734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c6ec.md#insn-00b7c734) · [`00b7c6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c6ec.md#insn-00b7c6fc)

~~~diff
- 00b7c6e0 ["INT_ADD", "register:40f0:8", ["const:b7c6e0:8", "const:4:8"]]
- 00b7c6e0 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b7c724 ["INT_ADD", "register:40f0:8", ["const:b7c724:8", "const:4:8"]]
+ 00b7c724 ["CALL", null, ["callee:00bdb000:8"]]
- 00b7c6e0 bytes 347a0194
+ 00b7c724 bytes 377a0194
- 00b7c6f0 ["INT_ADD", "register:40f0:8", ["const:b7c6f0:8", "const:4:8"]]
- 00b7c6f0 ["CALL", null, ["callee:00bdb020:8"]]
+ 00b7c734 ["INT_ADD", "register:40f0:8", ["const:b7c734:8", "const:4:8"]]
+ 00b7c734 ["CALL", null, ["callee:00bdb020:8"]]
- 00b7c6f0 bytes 387a0194
+ 00b7c734 bytes 3b7a0194
- 00b7c6b8 ["COPY", "tmp:0:8", ["const:28:8"]]
- 00b7c6b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b7c6b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b7c6b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b7c6fc ["COPY", "tmp:0:8", ["const:68:8"]]
+ 00b7c6fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7c6fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7c6fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b7c6b8 bytes 08a10091
+ 00b7c6fc bytes 08a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f77c11f658f3f43b12fb2007b8452685"></a>

### [`00b7cdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cdf0.md) → [`00b7ce34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce34.md) _ZNSt6__ndk17promiseIvEC1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b7ce64",
      "incomplete_value": true,
      "site": "00b7ce64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b7ce20",
      "incomplete_value": true,
      "site": "00b7ce20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b7ce58",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ce64",
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
      "00b7ce58",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ce64",
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

- 旧版 [`00b7ce08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cdf0.md#insn-00b7ce08) · [`00b7ce14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cdf0.md#insn-00b7ce14)
- 新版 [`00b7ce4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce34.md#insn-00b7ce4c) · [`00b7ce58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce34.md#insn-00b7ce58)

~~~diff
- 00b7ce08 ["INT_ADD", "register:40f0:8", ["const:b7ce08:8", "const:4:8"]]
- 00b7ce08 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b7ce4c ["INT_ADD", "register:40f0:8", ["const:b7ce4c:8", "const:4:8"]]
+ 00b7ce4c ["CALL", null, ["callee:00bdb040:8"]]
- 00b7ce08 bytes 7a780194
+ 00b7ce4c bytes 7d780194
- 00b7ce14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 00b7ce14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7ce58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 00b7ce58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7ce14 bytes 080947f9
+ 00b7ce58 bytes 083147f9
~~~


<a id="compare-3939322e9996f85d6b41a7668f8bf778"></a>

### [`00b7ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ce44.md) → [`00b7ce88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce88.md) _ZNSt6__ndk17promiseIvED1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`004377f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377f0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 14件 [`004377f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377f0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.21% / 新版 91.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7cef4",
      "incomplete_value": false,
      "site": "00b7cef4",
      "value": [
        "leaf",
        "const:c24918:8"
      ]
    },
    "old": {
      "definition_site": "00b7ceb0",
      "incomplete_value": false,
      "site": "00b7ceb0",
      "value": [
        "leaf",
        "const:c248c8:8"
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7cf30",
      "incomplete_value": true,
      "site": "00b7cf38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b7ceec",
      "incomplete_value": true,
      "site": "00b7cef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b7cf4c",
      "incomplete_value": true,
      "site": "00b7cf54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7cf08",
      "incomplete_value": true,
      "site": "00b7cf10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "00b7cee0",
      "READ",
      [
        "storage",
        "010a2028",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7cef4",
      "DATA",
      [
        "storage",
        "00c248c8",
        null,
        null
      ]
    ],
    [
      "00b7cf28",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7cee0",
      "READ",
      [
        "storage",
        "010a2068",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7cef4",
      "DATA",
      [
        "storage",
        "00c24918",
        null,
        null
      ]
    ],
    [
      "00b7cf28",
      "READ",
      [
        "storage",
        "00c1ae70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7cf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ce44.md#insn-00b7cf10) · [`00b7cf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ce44.md#insn-00b7cf98) · [`00b7cfa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ce44.md#insn-00b7cfa8)
- 新版 [`00b7cf54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce88.md#insn-00b7cf54) · [`00b7cfdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce88.md#insn-00b7cfdc) · [`00b7cfec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce88.md#insn-00b7cfec)

~~~diff
- 00b7cf10 ["INT_ADD", "register:40f0:8", ["const:b7cf10:8", "const:4:8"]]
- 00b7cf10 ["CALL", null, ["callee:00bdb4e0:8"]]
+ 00b7cf54 ["INT_ADD", "register:40f0:8", ["const:b7cf54:8", "const:4:8"]]
+ 00b7cf54 ["CALL", null, ["callee:00bdb4e0:8"]]
- 00b7cf10 bytes 60790194
+ 00b7cf54 bytes 63790194
- 00b7cf98 ["INT_ADD", "register:40f0:8", ["const:b7cf98:8", "const:4:8"]]
- 00b7cf98 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b7cfdc ["INT_ADD", "register:40f0:8", ["const:b7cfdc:8", "const:4:8"]]
+ 00b7cfdc ["CALL", null, ["callee:00bdb000:8"]]
- 00b7cf98 bytes 06780194
+ 00b7cfdc bytes 09780194
- 00b7cfa8 ["INT_ADD", "register:40f0:8", ["const:b7cfa8:8", "const:4:8"]]
- 00b7cfa8 ["CALL", null, ["callee:00bdb020:8"]]
+ 00b7cfec ["INT_ADD", "register:40f0:8", ["const:b7cfec:8", "const:4:8"]]
+ 00b7cfec ["CALL", null, ["callee:00bdb020:8"]]
- 00b7cfa8 bytes 0a780194
+ 00b7cfec bytes 0d780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ce33603950627da7842e781b8cc23f5"></a>

### [`00b7d1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d1d4.md) → [`00b7d218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d218.md) FUN_00b7d218

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

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
      "definition_site": "00b7d240",
      "incomplete_value": true,
      "site": "00b7d240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b7d1fc",
      "incomplete_value": true,
      "site": "00b7d1fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b7d234",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00b7d240",
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
      "00b7d234",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "00b7d240",
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

- 旧版 [`00b7d1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d1d4.md#insn-00b7d1f0) · [`00b7d200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d1d4.md#insn-00b7d200) · [`00b7d208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d1d4.md#insn-00b7d208)
- 新版 [`00b7d234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d218.md#insn-00b7d234) · [`00b7d244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d218.md#insn-00b7d244) · [`00b7d24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d218.md#insn-00b7d24c)

~~~diff
- 00b7d1f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 00b7d1f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7d234 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 00b7d234 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7d1f0 bytes 080947f9
+ 00b7d234 bytes 083147f9
- 00b7d200 ["INT_ADD", "register:40f0:8", ["const:b7d200:8", "const:4:8"]]
- 00b7d200 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d244 ["INT_ADD", "register:40f0:8", ["const:b7d244:8", "const:4:8"]]
+ 00b7d244 ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d200 bytes 0c780194
+ 00b7d244 bytes 0f780194
- 00b7d208 ["INT_ADD", "register:40f0:8", ["const:b7d208:8", "const:4:8"]]
- 00b7d208 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b7d24c ["INT_ADD", "register:40f0:8", ["const:b7d24c:8", "const:4:8"]]
+ 00b7d24c ["CALL", null, ["callee:00bdb010:8"]]
- 00b7d208 bytes 6e770194
+ 00b7d24c bytes 71770194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28b1f61997d4a4846628b044a3d2103e"></a>

### [`00b7d27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d27c.md) → [`00b7d2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2c0.md) _ZNSt6__ndk15mutex4lockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) · 呼出先 2件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md)
- 新版 呼出元 1件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) · 呼出先 2件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md)

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
      "definition_site": "00b7d2e4",
      "incomplete_value": false,
      "site": "00b7d2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:112:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d2a0",
      "incomplete_value": false,
      "site": "00b7d2a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:87:8"
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
      "00b7d2e4",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d2e4",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d27c.md#insn-00b7d2a4) · [`00b7d288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d27c.md#insn-00b7d288) · [`00b7d2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d27c.md#insn-00b7d2a0)
- 新版 [`00b7d2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2c0.md#insn-00b7d2e8) · [`00b7d2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2c0.md#insn-00b7d2cc) · [`00b7d2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2c0.md#insn-00b7d2e4)

~~~diff
- 00b7d2a4 ["INT_ADD", "register:40f0:8", ["const:b7d2a4:8", "const:4:8"]]
- 00b7d2a4 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d2e8 ["INT_ADD", "register:40f0:8", ["const:b7d2e8:8", "const:4:8"]]
+ 00b7d2e8 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d2a4 bytes f7770194
+ 00b7d2e8 bytes fa770194
- 00b7d288 ["INT_ADD", "register:40f0:8", ["const:b7d288:8", "const:4:8"]]
- 00b7d288 ["CALL", null, ["callee:00bde820:8"]]
+ 00b7d2cc ["INT_ADD", "register:40f0:8", ["const:b7d2cc:8", "const:4:8"]]
+ 00b7d2cc ["CALL", null, ["callee:00bde820:8"]]
- 00b7d288 bytes 52850194
+ 00b7d2cc bytes 55850194
- 00b7d2a0 ["COPY", "tmp:0:8", ["const:87:8"]]
- 00b7d2a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d2a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d2a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b7d2e4 ["COPY", "tmp:0:8", ["const:112:8"]]
+ 00b7d2e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d2e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d2e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b7d2a0 bytes 211c0291
+ 00b7d2e4 bytes 21480491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b65ffabf30bd7d599b9a0fb6c2ed18a6"></a>

### [`00b7d2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2f0.md) → [`00b7d334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d334.md) _ZNSt6__ndk115recursive_mutexC1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd220.md) · 呼出先 6件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bde7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7c0.md) [`00bdef80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef80.md) [`00bdef90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef90.md) [`00bdefa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdefa0.md)
- 新版 呼出元 1件 [`00bdd270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd270.md) · 呼出先 6件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bde810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde810.md) [`00bdefd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefd0.md) [`00bdefe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefe0.md) [`00bdeff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeff0.md)

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
      "definition_site": "00b7d3d0",
      "incomplete_value": false,
      "site": "00b7d3d4",
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
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d38c",
      "incomplete_value": false,
      "site": "00b7d390",
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
            "const:ac5:8"
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
      "00b7d3d0",
      "PARAM",
      [
        "storage",
        "00298ac5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d3d0",
      "PARAM",
      [
        "storage",
        "00298a38",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2f0.md#insn-00b7d390) · [`00b7d30c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2f0.md#insn-00b7d30c) · [`00b7d31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2f0.md#insn-00b7d31c)
- 新版 [`00b7d3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d334.md#insn-00b7d3d4) · [`00b7d350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d334.md#insn-00b7d350) · [`00b7d360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d334.md#insn-00b7d360)

~~~diff
- 00b7d390 ["INT_ADD", "register:40f0:8", ["const:b7d390:8", "const:4:8"]]
- 00b7d390 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d3d4 ["INT_ADD", "register:40f0:8", ["const:b7d3d4:8", "const:4:8"]]
+ 00b7d3d4 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d390 bytes bc770194
+ 00b7d3d4 bytes bf770194
- 00b7d30c ["INT_ADD", "register:40f0:8", ["const:b7d30c:8", "const:4:8"]]
- 00b7d30c ["CALL", null, ["callee:00bdeff0:8"]]
+ 00b7d350 ["INT_ADD", "register:40f0:8", ["const:b7d350:8", "const:4:8"]]
+ 00b7d350 ["CALL", null, ["callee:00bdeff0:8"]]
- 00b7d30c bytes 25870194
+ 00b7d350 bytes 28870194
- 00b7d31c ["INT_ADD", "register:40f0:8", ["const:b7d31c:8", "const:4:8"]]
- 00b7d31c ["CALL", null, ["callee:00bdf000:8"]]
+ 00b7d360 ["INT_ADD", "register:40f0:8", ["const:b7d360:8", "const:4:8"]]
+ 00b7d360 ["CALL", null, ["callee:00bdf000:8"]]
- 00b7d31c bytes 25870194
+ 00b7d360 bytes 28870194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5f88fe4fdf6850c67ba6030330d8540"></a>

### [`00b7d3b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d3b4.md) → [`00b7d3f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3f8.md) _ZNSt6__ndk115recursive_mutex4lockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd240.md) · 呼出先 2件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md)
- 新版 呼出元 1件 [`00bdd290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd290.md) · 呼出先 2件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md)

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
      "definition_site": "00b7d41c",
      "incomplete_value": false,
      "site": "00b7d420",
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
            "const:803:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d3d8",
      "incomplete_value": false,
      "site": "00b7d3dc",
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
            "const:890:8"
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
      "00b7d41c",
      "PARAM",
      [
        "storage",
        "00297890",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d41c",
      "PARAM",
      [
        "storage",
        "00297803",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d3b4.md#insn-00b7d3dc) · [`00b7d3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d3b4.md#insn-00b7d3c0) · [`00b7d3d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d3b4.md#insn-00b7d3d8)
- 新版 [`00b7d420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3f8.md#insn-00b7d420) · [`00b7d404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3f8.md#insn-00b7d404) · [`00b7d41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3f8.md#insn-00b7d41c)

~~~diff
- 00b7d3dc ["INT_ADD", "register:40f0:8", ["const:b7d3dc:8", "const:4:8"]]
- 00b7d3dc ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d420 ["INT_ADD", "register:40f0:8", ["const:b7d420:8", "const:4:8"]]
+ 00b7d420 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d3dc bytes a9770194
+ 00b7d420 bytes ac770194
- 00b7d3c0 ["INT_ADD", "register:40f0:8", ["const:b7d3c0:8", "const:4:8"]]
- 00b7d3c0 ["CALL", null, ["callee:00bde820:8"]]
+ 00b7d404 ["INT_ADD", "register:40f0:8", ["const:b7d404:8", "const:4:8"]]
+ 00b7d404 ["CALL", null, ["callee:00bde820:8"]]
- 00b7d3c0 bytes 04850194
+ 00b7d404 bytes 07850194
- 00b7d3d8 ["COPY", "tmp:0:8", ["const:890:8"]]
- 00b7d3d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d3d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d3d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b7d41c ["COPY", "tmp:0:8", ["const:803:8"]]
+ 00b7d41c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d41c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d41c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b7d3d8 bytes 21402291
+ 00b7d41c bytes 210c2091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e58249630dc7074e29824c83ec835538"></a>

### [`00b7d444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d444.md) → [`00b7d488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d488.md) _ZNSt6__ndk111timed_mutexD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

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
      "definition_site": "00b7d4cc",
      "incomplete_value": false,
      "site": "00b7d4d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:112:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d488",
      "incomplete_value": false,
      "site": "00b7d48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:87:8"
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
      "00b7d4cc",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d4cc",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d444.md#insn-00b7d48c) · [`00b7d458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d444.md#insn-00b7d458) · [`00b7d464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d444.md#insn-00b7d464)
- 新版 [`00b7d4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d488.md#insn-00b7d4d0) · [`00b7d49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d488.md#insn-00b7d49c) · [`00b7d4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d488.md#insn-00b7d4a8)

~~~diff
- 00b7d48c ["INT_ADD", "register:40f0:8", ["const:b7d48c:8", "const:4:8"]]
- 00b7d48c ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d4d0 ["INT_ADD", "register:40f0:8", ["const:b7d4d0:8", "const:4:8"]]
+ 00b7d4d0 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d48c bytes 7d770194
+ 00b7d4d0 bytes 80770194
- 00b7d458 ["INT_ADD", "register:40f0:8", ["const:b7d458:8", "const:4:8"]]
- 00b7d458 ["CALL", null, ["callee:00bde820:8"]]
+ 00b7d49c ["INT_ADD", "register:40f0:8", ["const:b7d49c:8", "const:4:8"]]
+ 00b7d49c ["CALL", null, ["callee:00bde820:8"]]
- 00b7d458 bytes de840194
+ 00b7d49c bytes e1840194
- 00b7d464 ["INT_ADD", "register:40f0:8", ["const:b7d464:8", "const:4:8"]]
- 00b7d464 ["CALL", null, ["callee:00bde830:8"]]
+ 00b7d4a8 ["INT_ADD", "register:40f0:8", ["const:b7d4a8:8", "const:4:8"]]
+ 00b7d4a8 ["CALL", null, ["callee:00bde830:8"]]
- 00b7d464 bytes df840194
+ 00b7d4a8 bytes e2840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74a6b944f19bf360c8221a9268ee976d"></a>

### [`00b7d498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d498.md) → [`00b7d4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d4dc.md) _ZNSt6__ndk111timed_mutex4lockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5e0.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

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
      "definition_site": "00b7d560",
      "incomplete_value": false,
      "site": "00b7d564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:112:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d51c",
      "incomplete_value": false,
      "site": "00b7d520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:87:8"
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
      "00b7d560",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d560",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d498.md#insn-00b7d520) · [`00b7d4bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d498.md#insn-00b7d4bc) · [`00b7d4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d498.md#insn-00b7d4d4)
- 新版 [`00b7d564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d4dc.md#insn-00b7d564) · [`00b7d500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d4dc.md#insn-00b7d500) · [`00b7d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d4dc.md#insn-00b7d518)

~~~diff
- 00b7d520 ["INT_ADD", "register:40f0:8", ["const:b7d520:8", "const:4:8"]]
- 00b7d520 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d564 ["INT_ADD", "register:40f0:8", ["const:b7d564:8", "const:4:8"]]
+ 00b7d564 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d520 bytes 58770194
+ 00b7d564 bytes 5b770194
- 00b7d4bc ["INT_ADD", "register:40f0:8", ["const:b7d4bc:8", "const:4:8"]]
- 00b7d4bc ["CALL", null, ["callee:00bde820:8"]]
+ 00b7d500 ["INT_ADD", "register:40f0:8", ["const:b7d500:8", "const:4:8"]]
+ 00b7d500 ["CALL", null, ["callee:00bde820:8"]]
- 00b7d4bc bytes c5840194
+ 00b7d500 bytes c8840194
- 00b7d4d4 ["INT_ADD", "register:40f0:8", ["const:b7d4d4:8", "const:4:8"]]
- 00b7d4d4 ["CALL", null, ["callee:00bdb630:8"]]
+ 00b7d518 ["INT_ADD", "register:40f0:8", ["const:b7d518:8", "const:4:8"]]
+ 00b7d518 ["CALL", null, ["callee:00bdb630:8"]]
- 00b7d4d4 bytes 43780194
+ 00b7d518 bytes 46780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0dd4bb971023f7bdcef46070fa4acd6"></a>

### [`00b7d588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d588.md) → [`00b7d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d5cc.md) _ZNSt6__ndk111timed_mutex6unlockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdc270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc270.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdc2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2c0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

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
      "definition_site": "00b7d610",
      "incomplete_value": false,
      "site": "00b7d614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:112:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d5cc",
      "incomplete_value": false,
      "site": "00b7d5d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:87:8"
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
      "00b7d610",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d610",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d588.md#insn-00b7d5d0) · [`00b7d59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d588.md#insn-00b7d59c) · [`00b7d5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d588.md#insn-00b7d5ac)
- 新版 [`00b7d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d5cc.md#insn-00b7d614) · [`00b7d5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d5cc.md#insn-00b7d5e0) · [`00b7d5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d5cc.md#insn-00b7d5f0)

~~~diff
- 00b7d5d0 ["INT_ADD", "register:40f0:8", ["const:b7d5d0:8", "const:4:8"]]
- 00b7d5d0 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d614 ["INT_ADD", "register:40f0:8", ["const:b7d614:8", "const:4:8"]]
+ 00b7d614 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d5d0 bytes 2c770194
+ 00b7d614 bytes 2f770194
- 00b7d59c ["INT_ADD", "register:40f0:8", ["const:b7d59c:8", "const:4:8"]]
- 00b7d59c ["CALL", null, ["callee:00bde820:8"]]
+ 00b7d5e0 ["INT_ADD", "register:40f0:8", ["const:b7d5e0:8", "const:4:8"]]
+ 00b7d5e0 ["CALL", null, ["callee:00bde820:8"]]
- 00b7d59c bytes 8d840194
+ 00b7d5e0 bytes 90840194
- 00b7d5ac ["INT_ADD", "register:40f0:8", ["const:b7d5ac:8", "const:4:8"]]
- 00b7d5ac ["CALL", null, ["callee:00bdc2c0:8"]]
+ 00b7d5f0 ["INT_ADD", "register:40f0:8", ["const:b7d5f0:8", "const:4:8"]]
+ 00b7d5f0 ["CALL", null, ["callee:00bdc2c0:8"]]
- 00b7d5ac bytes 317b0194
+ 00b7d5f0 bytes 347b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7153433d6dca85061e7abac67a12adfd"></a>

### [`00b7d5f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d5f8.md) → [`00b7d63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d63c.md) _ZNSt6__ndk121recursive_timed_mutexD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

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
      "definition_site": "00b7d680",
      "incomplete_value": false,
      "site": "00b7d684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:112:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d63c",
      "incomplete_value": false,
      "site": "00b7d640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:87:8"
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
      "00b7d680",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d680",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d5f8.md#insn-00b7d640) · [`00b7d60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d5f8.md#insn-00b7d60c) · [`00b7d618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d5f8.md#insn-00b7d618)
- 新版 [`00b7d684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d63c.md#insn-00b7d684) · [`00b7d650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d63c.md#insn-00b7d650) · [`00b7d65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d63c.md#insn-00b7d65c)

~~~diff
- 00b7d640 ["INT_ADD", "register:40f0:8", ["const:b7d640:8", "const:4:8"]]
- 00b7d640 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d684 ["INT_ADD", "register:40f0:8", ["const:b7d684:8", "const:4:8"]]
+ 00b7d684 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d640 bytes 10770194
+ 00b7d684 bytes 13770194
- 00b7d60c ["INT_ADD", "register:40f0:8", ["const:b7d60c:8", "const:4:8"]]
- 00b7d60c ["CALL", null, ["callee:00bde820:8"]]
+ 00b7d650 ["INT_ADD", "register:40f0:8", ["const:b7d650:8", "const:4:8"]]
+ 00b7d650 ["CALL", null, ["callee:00bde820:8"]]
- 00b7d60c bytes 71840194
+ 00b7d650 bytes 74840194
- 00b7d618 ["INT_ADD", "register:40f0:8", ["const:b7d618:8", "const:4:8"]]
- 00b7d618 ["CALL", null, ["callee:00bde830:8"]]
+ 00b7d65c ["INT_ADD", "register:40f0:8", ["const:b7d65c:8", "const:4:8"]]
+ 00b7d65c ["CALL", null, ["callee:00bde830:8"]]
- 00b7d618 bytes 72840194
+ 00b7d65c bytes 75840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbe0b7584cbc62233ec441d311794664"></a>

### [`00b7d64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d64c.md) → [`00b7d690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d690.md) _ZNSt6__ndk121recursive_timed_mutex4lockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdb5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5e0.md) [`00bdb780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb780.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md) [`00bdb7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7d0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

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
      "definition_site": "00b7d73c",
      "incomplete_value": false,
      "site": "00b7d740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:112:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d6f8",
      "incomplete_value": false,
      "site": "00b7d6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:87:8"
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
      "definition_site": "00b7d748",
      "incomplete_value": false,
      "site": "00b7d750",
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
            "const:3e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d704",
      "incomplete_value": false,
      "site": "00b7d70c",
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
            "const:471:8"
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
      "00b7d73c",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ],
    [
      "00b7d748",
      "PARAM",
      [
        "storage",
        "00294471",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d73c",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ],
    [
      "00b7d748",
      "PARAM",
      [
        "storage",
        "002943e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d64c.md#insn-00b7d6fc) · [`00b7d70c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d64c.md#insn-00b7d70c) · [`00b7d664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d64c.md#insn-00b7d664)
- 新版 [`00b7d740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d690.md#insn-00b7d740) · [`00b7d750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d690.md#insn-00b7d750) · [`00b7d6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d690.md#insn-00b7d6a8)

~~~diff
- 00b7d6fc ["INT_ADD", "register:40f0:8", ["const:b7d6fc:8", "const:4:8"]]
- 00b7d6fc ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d740 ["INT_ADD", "register:40f0:8", ["const:b7d740:8", "const:4:8"]]
+ 00b7d740 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d6fc bytes e1760194
+ 00b7d740 bytes e4760194
- 00b7d70c ["INT_ADD", "register:40f0:8", ["const:b7d70c:8", "const:4:8"]]
- 00b7d70c ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d750 ["INT_ADD", "register:40f0:8", ["const:b7d750:8", "const:4:8"]]
+ 00b7d750 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d70c bytes dd760194
+ 00b7d750 bytes e0760194
- 00b7d664 ["INT_ADD", "register:40f0:8", ["const:b7d664:8", "const:4:8"]]
- 00b7d664 ["CALL", null, ["callee:00bdb7d0:8"]]
+ 00b7d6a8 ["INT_ADD", "register:40f0:8", ["const:b7d6a8:8", "const:4:8"]]
+ 00b7d6a8 ["CALL", null, ["callee:00bdb7d0:8"]]
- 00b7d664 bytes 47780194
+ 00b7d6a8 bytes 4a780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bea999fc624a319d59ecec6c40605c74"></a>

### [`00b7d7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d7b4.md) → [`00b7d7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d7f8.md) _ZNSt6__ndk121recursive_timed_mutex6unlockEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdc270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc270.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdc2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2c0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)

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
      "definition_site": "00b7d860",
      "incomplete_value": false,
      "site": "00b7d864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:112:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d81c",
      "incomplete_value": false,
      "site": "00b7d820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:87:8"
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
      "00b7d860",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d860",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d7b4.md#insn-00b7d820) · [`00b7d7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d7b4.md#insn-00b7d7c8) · [`00b7d7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d7b4.md#insn-00b7d7e4)
- 新版 [`00b7d864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d7f8.md#insn-00b7d864) · [`00b7d80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d7f8.md#insn-00b7d80c) · [`00b7d828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d7f8.md#insn-00b7d828)

~~~diff
- 00b7d820 ["INT_ADD", "register:40f0:8", ["const:b7d820:8", "const:4:8"]]
- 00b7d820 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d864 ["INT_ADD", "register:40f0:8", ["const:b7d864:8", "const:4:8"]]
+ 00b7d864 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d820 bytes 98760194
+ 00b7d864 bytes 9b760194
- 00b7d7c8 ["INT_ADD", "register:40f0:8", ["const:b7d7c8:8", "const:4:8"]]
- 00b7d7c8 ["CALL", null, ["callee:00bde820:8"]]
+ 00b7d80c ["INT_ADD", "register:40f0:8", ["const:b7d80c:8", "const:4:8"]]
+ 00b7d80c ["CALL", null, ["callee:00bde820:8"]]
- 00b7d7c8 bytes 02840194
+ 00b7d80c bytes 05840194
- 00b7d7e4 ["INT_ADD", "register:40f0:8", ["const:b7d7e4:8", "const:4:8"]]
- 00b7d7e4 ["CALL", null, ["callee:00bde830:8"]]
+ 00b7d828 ["INT_ADD", "register:40f0:8", ["const:b7d828:8", "const:4:8"]]
+ 00b7d828 ["CALL", null, ["callee:00bde830:8"]]
- 00b7d7e4 bytes ff830194
+ 00b7d828 bytes 02840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad5d15ae1108fc3e1473ee488242df6"></a>

### [`00b7d850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d850.md) → [`00b7d894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d894.md) _ZNSt6__ndk16thread4joinEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2d0.md) · 呼出先 2件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00be0610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0610.md)
- 新版 呼出元 1件 [`00bdb320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb320.md) · 呼出先 2件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00be0660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0660.md)

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
      "definition_site": "00b7d8d8",
      "incomplete_value": false,
      "site": "00b7d8dc",
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
            "const:6d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d894",
      "incomplete_value": false,
      "site": "00b7d898",
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
            "const:763:8"
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
      "00b7d8d8",
      "PARAM",
      [
        "storage",
        "00296763",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d8d8",
      "PARAM",
      [
        "storage",
        "002966d6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d850.md#insn-00b7d898) · [`00b7d870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d850.md#insn-00b7d870) · [`00b7d894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d850.md#insn-00b7d894)
- 新版 [`00b7d8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d894.md#insn-00b7d8dc) · [`00b7d8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d894.md#insn-00b7d8b4) · [`00b7d8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d894.md#insn-00b7d8d8)

~~~diff
- 00b7d898 ["INT_ADD", "register:40f0:8", ["const:b7d898:8", "const:4:8"]]
- 00b7d898 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d8dc ["INT_ADD", "register:40f0:8", ["const:b7d8dc:8", "const:4:8"]]
+ 00b7d8dc ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d898 bytes 7a760194
+ 00b7d8dc bytes 7d760194
- 00b7d870 ["INT_ADD", "register:40f0:8", ["const:b7d870:8", "const:4:8"]]
- 00b7d870 ["CALL", null, ["callee:00be0660:8"]]
+ 00b7d8b4 ["INT_ADD", "register:40f0:8", ["const:b7d8b4:8", "const:4:8"]]
+ 00b7d8b4 ["CALL", null, ["callee:00be0660:8"]]
- 00b7d870 bytes 688b0194
+ 00b7d8b4 bytes 6b8b0194
- 00b7d894 ["COPY", "tmp:0:8", ["const:763:8"]]
- 00b7d894 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d894 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d894 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b7d8d8 ["COPY", "tmp:0:8", ["const:6d6:8"]]
+ 00b7d8d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d8d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d8d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b7d894 bytes 218c1d91
+ 00b7d8d8 bytes 21581b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e449ad59da4dde70cf1f6cf8fe12885"></a>

### [`00b7d89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d89c.md) → [`00b7d8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d8e0.md) _ZNSt6__ndk16thread6detachEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb670.md) · 呼出先 2件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00be1230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1230.md)
- 新版 呼出元 1件 [`00bdb6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6c0.md) · 呼出先 2件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00be1280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1280.md)

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
      "definition_site": "00b7d920",
      "incomplete_value": false,
      "site": "00b7d924",
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
            "const:186:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d8dc",
      "incomplete_value": false,
      "site": "00b7d8e0",
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
            "const:fb:8"
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
      "00b7d920",
      "PARAM",
      [
        "storage",
        "0029e0fb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7d920",
      "PARAM",
      [
        "storage",
        "0029e186",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d89c.md#insn-00b7d8e0) · [`00b7d8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d89c.md#insn-00b7d8b8) · [`00b7d8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d89c.md#insn-00b7d8dc)
- 新版 [`00b7d924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d8e0.md#insn-00b7d924) · [`00b7d8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d8e0.md#insn-00b7d8fc) · [`00b7d920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d8e0.md#insn-00b7d920)

~~~diff
- 00b7d8e0 ["INT_ADD", "register:40f0:8", ["const:b7d8e0:8", "const:4:8"]]
- 00b7d8e0 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7d924 ["INT_ADD", "register:40f0:8", ["const:b7d924:8", "const:4:8"]]
+ 00b7d924 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7d8e0 bytes 68760194
+ 00b7d924 bytes 6b760194
- 00b7d8b8 ["INT_ADD", "register:40f0:8", ["const:b7d8b8:8", "const:4:8"]]
- 00b7d8b8 ["CALL", null, ["callee:00be1280:8"]]
+ 00b7d8fc ["INT_ADD", "register:40f0:8", ["const:b7d8fc:8", "const:4:8"]]
+ 00b7d8fc ["CALL", null, ["callee:00be1280:8"]]
- 00b7d8b8 bytes 5e8e0194
+ 00b7d8fc bytes 618e0194
- 00b7d8dc ["COPY", "tmp:0:8", ["const:fb:8"]]
- 00b7d8dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d8dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b7d8dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b7d920 ["COPY", "tmp:0:8", ["const:186:8"]]
+ 00b7d920 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d920 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7d920 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b7d8dc bytes 21ec0391
+ 00b7d920 bytes 21180691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-372750b8f2c8617cce7c57d588a56908"></a>

### [`00b7d990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d990.md) → [`00b7d9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d9d4.md) _ZNSt6__ndk119__thread_local_dataEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb290.md) · 呼出先 3件 [`00b7da14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da14.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00bdb2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2e0.md) · 呼出先 3件 [`00b7da58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da58.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

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
      "definition_site": "00b7da34",
      "incomplete_value": true,
      "site": "00b7da34",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d9f0",
      "incomplete_value": true,
      "site": "00b7d9f0",
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
            "const:38:8"
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
      "definition_site": "00b7da10",
      "incomplete_value": false,
      "site": "00b7da14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d9cc",
      "incomplete_value": false,
      "site": "00b7d9d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:40:8"
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
      "definition_site": "00b7da24",
      "incomplete_value": false,
      "site": "00b7da28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d9e0",
      "incomplete_value": false,
      "site": "00b7d9e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:30:8"
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
      "00b7d9f0",
      "READ",
      [
        "storage",
        "010a2040",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7d9f8",
      "READ",
      [
        "storage",
        "010a2038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7d9f8",
      "DATA",
      [
        "storage",
        "010a2030",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b7d9f0",
      "READ",
      [
        "storage",
        "010a2080",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7d9f8",
      "READ",
      [
        "storage",
        "010a2078",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7d9f8",
      "DATA",
      [
        "storage",
        "010a2070",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d990.md#insn-00b7d9d0) · [`00b7d9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d990.md#insn-00b7d9e4) · [`00b7d9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d990.md#insn-00b7d9f0)
- 新版 [`00b7da14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d9d4.md#insn-00b7da14) · [`00b7da28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d9d4.md#insn-00b7da28) · [`00b7da34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d9d4.md#insn-00b7da34)

~~~diff
- 00b7d9d0 ["INT_ADD", "register:40f0:8", ["const:b7d9d0:8", "const:4:8"]]
- 00b7d9d0 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b7da14 ["INT_ADD", "register:40f0:8", ["const:b7da14:8", "const:4:8"]]
+ 00b7da14 ["CALL", null, ["callee:00bdb000:8"]]
- 00b7d9d0 bytes 78750194
+ 00b7da14 bytes 7b750194
- 00b7d9e4 ["INT_ADD", "register:40f0:8", ["const:b7d9e4:8", "const:4:8"]]
- 00b7d9e4 ["CALL", null, ["callee:00b7da58:8"]]
+ 00b7da28 ["INT_ADD", "register:40f0:8", ["const:b7da28:8", "const:4:8"]]
+ 00b7da28 ["CALL", null, ["callee:00b7da58:8"]]
- 00b7d9e4 bytes 0c000094
+ 00b7da28 bytes 0c000094
- 00b7d9f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:38:8"]]
- 00b7d9f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00b7da34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
+ 00b7da34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b7d9f0 bytes 931e00f9
+ 00b7da34 bytes 933e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e5125f469a8bc93d2b08a4b30a47b9d"></a>

### [`00b7da14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da14.md) → [`00b7da58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da58.md) FUN_00b7da58

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b7d990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d990.md) · 呼出先 3件 [`00b7ddc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7ddc8.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdd460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd460.md)
- 新版 呼出元 1件 [`00b7d9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d9d4.md) · 呼出先 3件 [`00b7de0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de0c.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdd4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4b0.md)

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
      "definition_site": "00b7da68",
      "incomplete_value": false,
      "site": "00b7da6c",
      "value": [
        "leaf",
        "const:b7de0c:8"
      ]
    },
    "old": {
      "definition_site": "00b7da24",
      "incomplete_value": false,
      "site": "00b7da28",
      "value": [
        "leaf",
        "const:b7ddc8:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7da84",
      "incomplete_value": false,
      "site": "00b7da88",
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
            "const:40d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7da40",
      "incomplete_value": false,
      "site": "00b7da44",
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
            "const:49a:8"
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
      "00b7da68",
      "PARAM",
      [
        "storage",
        "00b7ddc8",
        null,
        null
      ]
    ],
    [
      "00b7da84",
      "PARAM",
      [
        "storage",
        "0029449a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7da68",
      "PARAM",
      [
        "storage",
        "00b7de0c",
        null,
        null
      ]
    ],
    [
      "00b7da84",
      "PARAM",
      [
        "storage",
        "0029440d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7da28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da14.md#insn-00b7da28) · [`00b7da44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da14.md#insn-00b7da44) · [`00b7da24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da14.md#insn-00b7da24)
- 新版 [`00b7da6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da58.md#insn-00b7da6c) · [`00b7da88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da58.md#insn-00b7da88) · [`00b7da68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da58.md#insn-00b7da68)

~~~diff
- 00b7da28 ["INT_ADD", "register:40f0:8", ["const:b7da28:8", "const:4:8"]]
- 00b7da28 ["CALL", null, ["callee:00bdd4b0:8"]]
+ 00b7da6c ["INT_ADD", "register:40f0:8", ["const:b7da6c:8", "const:4:8"]]
+ 00b7da6c ["CALL", null, ["callee:00bdd4b0:8"]]
- 00b7da28 bytes 8e7e0194
+ 00b7da6c bytes 917e0194
- 00b7da44 ["INT_ADD", "register:40f0:8", ["const:b7da44:8", "const:4:8"]]
- 00b7da44 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7da88 ["INT_ADD", "register:40f0:8", ["const:b7da88:8", "const:4:8"]]
+ 00b7da88 ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7da44 bytes 0f760194
+ 00b7da88 bytes 12760194
- 00b7da24 ["COPY", "register:4008:8", ["const:b7ddc8:8"]]
+ 00b7da68 ["COPY", "register:4008:8", ["const:b7de0c:8"]]
- 00b7da24 bytes 211d0010
+ 00b7da68 bytes 211d0010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3f7685b356fe867d9d326b85c703d34"></a>

### [`00b7dd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd98.md) → [`00b7dddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dddc.md) FUN_00b7dddc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b7db14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7db14.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00b7db58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7db58.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00b7ddec",
      "incomplete_value": false,
      "site": "00b7ddf0",
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
      "definition_site": "00b7dda8",
      "incomplete_value": false,
      "site": "00b7ddac",
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
      "00b7ddec",
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
      "00b7ddec",
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

- 旧版 [`00b7ddac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd98.md#insn-00b7ddac) · [`00b7dda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd98.md#insn-00b7dda8)
- 新版 [`00b7ddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dddc.md#insn-00b7ddf0) · [`00b7ddec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dddc.md#insn-00b7ddec)

~~~diff
- 00b7ddac ["INT_ADD", "register:40f0:8", ["const:b7ddac:8", "const:4:8"]]
- 00b7ddac ["CALL", null, ["callee:00418c38:8"]]
+ 00b7ddf0 ["INT_ADD", "register:40f0:8", ["const:b7ddf0:8", "const:4:8"]]
+ 00b7ddf0 ["CALL", null, ["callee:00418c38:8"]]
- 00b7ddac bytes a36be297
+ 00b7ddf0 bytes 926be297
- 00b7dda8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00b7dda8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b7dda8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b7dda8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b7ddec ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00b7ddec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7ddec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7ddec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b7dda8 bytes 000c0c91
+ 00b7ddec bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf955e731b9fa2851ee6a9a37bc1d50c"></a>

### [`00b7ddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7ddb0.md) → [`00b7ddf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddf4.md) FUN_00b7ddf4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b7dc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dc10.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00b7dc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dc54.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00b7de04",
      "incomplete_value": false,
      "site": "00b7de08",
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
      "definition_site": "00b7ddc0",
      "incomplete_value": false,
      "site": "00b7ddc4",
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
      "00b7de04",
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
      "00b7de04",
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

- 旧版 [`00b7ddc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7ddb0.md#insn-00b7ddc4) · [`00b7ddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7ddb0.md#insn-00b7ddc0)
- 新版 [`00b7de08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddf4.md#insn-00b7de08) · [`00b7de04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddf4.md#insn-00b7de04)

~~~diff
- 00b7ddc4 ["INT_ADD", "register:40f0:8", ["const:b7ddc4:8", "const:4:8"]]
- 00b7ddc4 ["CALL", null, ["callee:00418c38:8"]]
+ 00b7de08 ["INT_ADD", "register:40f0:8", ["const:b7de08:8", "const:4:8"]]
+ 00b7de08 ["CALL", null, ["callee:00418c38:8"]]
- 00b7ddc4 bytes 9d6be297
+ 00b7de08 bytes 8c6be297
- 00b7ddc0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00b7ddc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b7ddc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b7ddc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b7de04 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00b7de04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7de04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7de04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b7ddc0 bytes 000c0c91
+ 00b7de04 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de8c5e6fdb6be0c2bdf59a44c12f5435"></a>

### [`00b7de00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7de00.md) → [`00b7de44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de44.md) _ZNSt6__ndk113random_deviceC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) · 呼出先 4件 [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00be05e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be05e0.md)
- 新版 呼出元 1件 [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) · 呼出先 4件 [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00be0630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0630.md)

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
      "definition_site": "00b7dea0",
      "incomplete_value": false,
      "site": "00b7deb0",
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
            "const:155:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7de5c",
      "incomplete_value": false,
      "site": "00b7de6c",
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
            "const:ca:8"
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
      "00b7dea0",
      "PARAM",
      [
        "storage",
        "002a40ca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7dea0",
      "PARAM",
      [
        "storage",
        "002a4155",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7de6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7de00.md#insn-00b7de6c) · [`00b7de30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7de00.md#insn-00b7de30) · [`00b7de50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7de00.md#insn-00b7de50)
- 新版 [`00b7deb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de44.md#insn-00b7deb0) · [`00b7de74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de44.md#insn-00b7de74) · [`00b7de94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de44.md#insn-00b7de94)

~~~diff
- 00b7de6c ["INT_ADD", "register:40f0:8", ["const:b7de6c:8", "const:4:8"]]
- 00b7de6c ["CALL", null, ["callee:00bdb260:8"]]
+ 00b7deb0 ["INT_ADD", "register:40f0:8", ["const:b7deb0:8", "const:4:8"]]
+ 00b7deb0 ["CALL", null, ["callee:00bdb260:8"]]
- 00b7de6c bytes e9740194
+ 00b7deb0 bytes ec740194
- 00b7de30 ["INT_ADD", "register:40f0:8", ["const:b7de30:8", "const:4:8"]]
- 00b7de30 ["CALL", null, ["callee:00be0630:8"]]
+ 00b7de74 ["INT_ADD", "register:40f0:8", ["const:b7de74:8", "const:4:8"]]
+ 00b7de74 ["CALL", null, ["callee:00be0630:8"]]
- 00b7de30 bytes ec890194
+ 00b7de74 bytes ef890194
- 00b7de50 ["INT_ADD", "register:40f0:8", ["const:b7de50:8", "const:4:8"]]
- 00b7de50 ["CALL", null, ["callee:00bdb270:8"]]
+ 00b7de94 ["INT_ADD", "register:40f0:8", ["const:b7de94:8", "const:4:8"]]
+ 00b7de94 ["CALL", null, ["callee:00bdb270:8"]]
- 00b7de50 bytes f4740194
+ 00b7de94 bytes f7740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d45fbb128b15aabab313501d5c9a2b35"></a>

### [`00b7dec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dec8.md) → [`00b7df0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7df0c.md) _ZNSt6__ndk113random_deviceclEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md) · 呼出先 3件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00be0620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0620.md)
- 新版 呼出元 1件 [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md) · 呼出先 3件 [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00be0670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0670.md)

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
      "definition_site": "00b7df88",
      "incomplete_value": false,
      "site": "00b7df8c",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7df44",
      "incomplete_value": false,
      "site": "00b7df48",
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
            "const:fc6:8"
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
      "definition_site": "00b7df94",
      "incomplete_value": false,
      "site": "00b7df9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:245:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7df50",
      "incomplete_value": false,
      "site": "00b7df58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:247:8"
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
      "00b7df88",
      "PARAM",
      [
        "storage",
        "002a7fc6",
        null,
        "string"
      ]
    ],
    [
      "00b7df94",
      "PARAM",
      [
        "storage",
        "0029c247",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7df88",
      "PARAM",
      [
        "storage",
        "002a8060",
        null,
        "string"
      ]
    ],
    [
      "00b7df94",
      "PARAM",
      [
        "storage",
        "0029c245",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7df48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dec8.md#insn-00b7df48) · [`00b7df58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dec8.md#insn-00b7df58) · [`00b7deec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dec8.md#insn-00b7deec)
- 新版 [`00b7df8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7df0c.md#insn-00b7df8c) · [`00b7df9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7df0c.md#insn-00b7df9c) · [`00b7df30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7df0c.md#insn-00b7df30)

~~~diff
- 00b7df48 ["INT_ADD", "register:40f0:8", ["const:b7df48:8", "const:4:8"]]
- 00b7df48 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7df8c ["INT_ADD", "register:40f0:8", ["const:b7df8c:8", "const:4:8"]]
+ 00b7df8c ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7df48 bytes ce740194
+ 00b7df8c bytes d1740194
- 00b7df58 ["INT_ADD", "register:40f0:8", ["const:b7df58:8", "const:4:8"]]
- 00b7df58 ["CALL", null, ["callee:00bdb2d0:8"]]
+ 00b7df9c ["INT_ADD", "register:40f0:8", ["const:b7df9c:8", "const:4:8"]]
+ 00b7df9c ["CALL", null, ["callee:00bdb2d0:8"]]
- 00b7df58 bytes ca740194
+ 00b7df9c bytes cd740194
- 00b7deec ["INT_ADD", "register:40f0:8", ["const:b7deec:8", "const:4:8"]]
- 00b7deec ["CALL", null, ["callee:00bdb270:8"]]
+ 00b7df30 ["INT_ADD", "register:40f0:8", ["const:b7df30:8", "const:4:8"]]
+ 00b7df30 ["CALL", null, ["callee:00bdb270:8"]]
- 00b7deec bytes cd740194
+ 00b7df30 bytes d0740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68f17b2ad7a7bc13fadb93a6f65fa12e"></a>

### [`00b7e038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e038.md) → [`00b7e07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e07c.md) _ZNSt6__ndk117iostream_categoryEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7e0b0",
      "incomplete_value": false,
      "site": "00b7e0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e06c",
      "incomplete_value": false,
      "site": "00b7e070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "definition_site": "00b7e0c0",
      "incomplete_value": false,
      "site": "00b7e0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e07c",
      "incomplete_value": false,
      "site": "00b7e080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "00b7e090",
      "READ",
      [
        "storage",
        "010a2048",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7e09c",
      "DATA",
      [
        "storage",
        "00c248d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e0b0",
      "PARAM",
      [
        "storage",
        "010a2048",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7e090",
      "READ",
      [
        "storage",
        "010a2088",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7e09c",
      "DATA",
      [
        "storage",
        "00c24920",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e0b0",
      "PARAM",
      [
        "storage",
        "010a2088",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e038.md#insn-00b7e070) · [`00b7e080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e038.md#insn-00b7e080) · [`00b7e048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e038.md#insn-00b7e048)
- 新版 [`00b7e0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e07c.md#insn-00b7e0b4) · [`00b7e0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e07c.md#insn-00b7e0c4) · [`00b7e08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e07c.md#insn-00b7e08c)

~~~diff
- 00b7e070 ["INT_ADD", "register:40f0:8", ["const:b7e070:8", "const:4:8"]]
- 00b7e070 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b7e0b4 ["INT_ADD", "register:40f0:8", ["const:b7e0b4:8", "const:4:8"]]
+ 00b7e0b4 ["CALL", null, ["callee:00bdb000:8"]]
- 00b7e070 bytes d0730194
+ 00b7e0b4 bytes d3730194
- 00b7e080 ["INT_ADD", "register:40f0:8", ["const:b7e080:8", "const:4:8"]]
- 00b7e080 ["CALL", null, ["callee:00bdb020:8"]]
+ 00b7e0c4 ["INT_ADD", "register:40f0:8", ["const:b7e0c4:8", "const:4:8"]]
+ 00b7e0c4 ["CALL", null, ["callee:00bdb020:8"]]
- 00b7e080 bytes d4730194
+ 00b7e0c4 bytes d7730194
- 00b7e048 ["COPY", "tmp:0:8", ["const:48:8"]]
- 00b7e048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b7e048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b7e048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b7e08c ["COPY", "tmp:0:8", ["const:88:8"]]
+ 00b7e08c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7e08c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7e08c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b7e048 bytes 08210191
+ 00b7e08c bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1af616a38a7f402246652b1aac33893e"></a>

### [`00b7e240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e240.md) → [`00b7e284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e284.md) _ZNSt6__ndk18ios_base6xallocEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md)

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
      "definition_site": "00b7e298",
      "incomplete_value": true,
      "site": "00b7e29c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e254",
      "incomplete_value": true,
      "site": "00b7e258",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
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
      "00b7e298",
      "READ",
      [
        "storage",
        "00c1bc78",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e298",
      "PARAM",
      [
        "storage",
        "010a2050",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b7e298",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e298",
      "PARAM",
      [
        "storage",
        "010a2090",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e240.md#insn-00b7e258) · [`00b7e254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e240.md#insn-00b7e254)
- 新版 [`00b7e29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e284.md#insn-00b7e29c) · [`00b7e298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e284.md#insn-00b7e298)

~~~diff
- 00b7e258 ["INT_ADD", "register:40f0:8", ["const:b7e258:8", "const:4:8"]]
- 00b7e258 ["CALL", null, ["callee:00bd6e30:8"]]
+ 00b7e29c ["INT_ADD", "register:40f0:8", ["const:b7e29c:8", "const:4:8"]]
+ 00b7e29c ["CALL", null, ["callee:00bd6e30:8"]]
- 00b7e258 bytes e6620194
+ 00b7e29c bytes e5620194
- 00b7e254 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:c78:8"]]
- 00b7e254 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7e298 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc8:8"]]
+ 00b7e298 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7e254 bytes 213c46f9
+ 00b7e298 bytes 216446f9
~~~


<a id="compare-5a6f423c3cc15a497062e7f51d998eb2"></a>

### [`00b7e268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e268.md) → [`00b7e2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e2ac.md) _ZNSt6__ndk18ios_base5iwordEi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b7e690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b7e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7e3b8",
      "incomplete_value": true,
      "site": "00b7e3bc",
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
            "const:81f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e374",
      "incomplete_value": true,
      "site": "00b7e378",
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
            "const:8ac:8"
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
      "00b7e3a8",
      "DATA",
      [
        "storage",
        "010a2058",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7e3ac",
      "WRITE",
      [
        "storage",
        "010a2058",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7e3b8",
      "PARAM",
      [
        "storage",
        "002978ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7e3a8",
      "DATA",
      [
        "storage",
        "010a2098",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7e3ac",
      "WRITE",
      [
        "storage",
        "010a2098",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7e3b8",
      "PARAM",
      [
        "storage",
        "0029781f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e268.md#insn-00b7e378) · [`00b7e2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e268.md#insn-00b7e2c0) · [`00b7e310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e268.md#insn-00b7e310)
- 新版 [`00b7e3bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e2ac.md#insn-00b7e3bc) · [`00b7e304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e2ac.md#insn-00b7e304) · [`00b7e354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e2ac.md#insn-00b7e354)

~~~diff
- 00b7e378 ["INT_ADD", "register:40f0:8", ["const:b7e378:8", "const:4:8"]]
- 00b7e378 ["CALL", null, ["callee:00b7e6d4:8"]]
+ 00b7e3bc ["INT_ADD", "register:40f0:8", ["const:b7e3bc:8", "const:4:8"]]
+ 00b7e3bc ["CALL", null, ["callee:00b7e6d4:8"]]
- 00b7e378 bytes c6000094
+ 00b7e3bc bytes c6000094
- 00b7e2c0 ["INT_ADD", "register:40f0:8", ["const:b7e2c0:8", "const:4:8"]]
- 00b7e2c0 ["CALL", null, ["callee:00bdd250:8"]]
+ 00b7e304 ["INT_ADD", "register:40f0:8", ["const:b7e304:8", "const:4:8"]]
+ 00b7e304 ["CALL", null, ["callee:00bdd250:8"]]
- 00b7e2c0 bytes d07b0194
+ 00b7e304 bytes d37b0194
- 00b7e310 ["INT_ADD", "register:40f0:8", ["const:b7e310:8", "const:4:8"]]
- 00b7e310 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b7e354 ["INT_ADD", "register:40f0:8", ["const:b7e354:8", "const:4:8"]]
+ 00b7e354 ["CALL", null, ["callee:00bdb240:8"]]
- 00b7e310 bytes b8730194
+ 00b7e354 bytes bb730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dce59cfe9a0e4d9bb4ae26df52f6e802"></a>

### [`00b7e37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e37c.md) → [`00b7e3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e3c0.md) _ZNSt6__ndk18ios_base5pwordEi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b7e690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b7e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md)

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
      "definition_site": "00b7e4c0",
      "incomplete_value": false,
      "site": "00b7e4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e47c",
      "incomplete_value": false,
      "site": "00b7e47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "definition_site": "00b7e4cc",
      "incomplete_value": false,
      "site": "00b7e4d0",
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
            "const:81f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e488",
      "incomplete_value": false,
      "site": "00b7e48c",
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
            "const:8ac:8"
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
      "00b7e4bc",
      "DATA",
      [
        "storage",
        "010a2060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7e4c0",
      "WRITE",
      [
        "storage",
        "010a2060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7e4cc",
      "PARAM",
      [
        "storage",
        "002978ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7e4bc",
      "DATA",
      [
        "storage",
        "010a20a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7e4c0",
      "WRITE",
      [
        "storage",
        "010a20a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7e4cc",
      "PARAM",
      [
        "storage",
        "0029781f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e37c.md#insn-00b7e48c) · [`00b7e3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e37c.md#insn-00b7e3d4) · [`00b7e424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e37c.md#insn-00b7e424)
- 新版 [`00b7e4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e3c0.md#insn-00b7e4d0) · [`00b7e418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e3c0.md#insn-00b7e418) · [`00b7e468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e3c0.md#insn-00b7e468)

~~~diff
- 00b7e48c ["INT_ADD", "register:40f0:8", ["const:b7e48c:8", "const:4:8"]]
- 00b7e48c ["CALL", null, ["callee:00b7e6d4:8"]]
+ 00b7e4d0 ["INT_ADD", "register:40f0:8", ["const:b7e4d0:8", "const:4:8"]]
+ 00b7e4d0 ["CALL", null, ["callee:00b7e6d4:8"]]
- 00b7e48c bytes 81000094
+ 00b7e4d0 bytes 81000094
- 00b7e3d4 ["INT_ADD", "register:40f0:8", ["const:b7e3d4:8", "const:4:8"]]
- 00b7e3d4 ["CALL", null, ["callee:00bdd250:8"]]
+ 00b7e418 ["INT_ADD", "register:40f0:8", ["const:b7e418:8", "const:4:8"]]
+ 00b7e418 ["CALL", null, ["callee:00bdd250:8"]]
- 00b7e3d4 bytes 8b7b0194
+ 00b7e418 bytes 8e7b0194
- 00b7e424 ["INT_ADD", "register:40f0:8", ["const:b7e424:8", "const:4:8"]]
- 00b7e424 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b7e468 ["INT_ADD", "register:40f0:8", ["const:b7e468:8", "const:4:8"]]
+ 00b7e468 ["CALL", null, ["callee:00bdb240:8"]]
- 00b7e424 bytes 73730194
+ 00b7e468 bytes 76730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b3fa2d8c568f478924a8998f2ae37be"></a>

### [`00b7e490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e490.md) → [`00b7e4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e4d4.md) _ZNSt6__ndk18ios_base17register_callbackEPFvNS0_5eventERS0_iEi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7e690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b7e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md)

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
      "definition_site": "00b7e5ac",
      "incomplete_value": false,
      "site": "00b7e5b0",
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
            "const:81f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e568",
      "incomplete_value": false,
      "site": "00b7e56c",
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
            "const:8ac:8"
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
      "00b7e5ac",
      "PARAM",
      [
        "storage",
        "002978ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7e5ac",
      "PARAM",
      [
        "storage",
        "0029781f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e490.md#insn-00b7e56c) · [`00b7e4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e490.md#insn-00b7e4e4) · [`00b7e510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e490.md#insn-00b7e510)
- 新版 [`00b7e5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e4d4.md#insn-00b7e5b0) · [`00b7e528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e4d4.md#insn-00b7e528) · [`00b7e554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e4d4.md#insn-00b7e554)

~~~diff
- 00b7e56c ["INT_ADD", "register:40f0:8", ["const:b7e56c:8", "const:4:8"]]
- 00b7e56c ["CALL", null, ["callee:00b7e6d4:8"]]
+ 00b7e5b0 ["INT_ADD", "register:40f0:8", ["const:b7e5b0:8", "const:4:8"]]
+ 00b7e5b0 ["CALL", null, ["callee:00b7e6d4:8"]]
- 00b7e56c bytes 49000094
+ 00b7e5b0 bytes 49000094
- 00b7e4e4 ["INT_ADD", "register:40f0:8", ["const:b7e4e4:8", "const:4:8"]]
- 00b7e4e4 ["CALL", null, ["callee:00bdd250:8"]]
+ 00b7e528 ["INT_ADD", "register:40f0:8", ["const:b7e528:8", "const:4:8"]]
+ 00b7e528 ["CALL", null, ["callee:00bdd250:8"]]
- 00b7e4e4 bytes 477b0194
+ 00b7e528 bytes 4a7b0194
- 00b7e510 ["INT_ADD", "register:40f0:8", ["const:b7e510:8", "const:4:8"]]
- 00b7e510 ["CALL", null, ["callee:00bdd250:8"]]
+ 00b7e554 ["INT_ADD", "register:40f0:8", ["const:b7e554:8", "const:4:8"]]
+ 00b7e554 ["CALL", null, ["callee:00bdd250:8"]]
- 00b7e510 bytes 3c7b0194
+ 00b7e554 bytes 3f7b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14a9af6b7e3188e758feb887e90bcf97"></a>

### [`00b7e570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e570.md) → [`00b7e5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e5b4.md) _ZNSt6__ndk18ios_baseD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md) [`00be12a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12a0.md) · 呼出先 2件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 2件 [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md) [`00be12f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12f0.md) · 呼出先 2件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

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
      "definition_site": "00b7e5d8",
      "incomplete_value": true,
      "site": "00b7e5dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b7e594",
      "incomplete_value": true,
      "site": "00b7e598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b7e5d0",
      "READ",
      [
        "storage",
        "00c1bc80",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e5dc",
      "DATA",
      [
        "storage",
        "00c12fb0",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b7e5d0",
      "READ",
      [
        "storage",
        "00c1bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e5dc",
      "DATA",
      [
        "storage",
        "00c13000",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e570.md#insn-00b7e58c) · [`00b7e5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e570.md#insn-00b7e5c4) · [`00b7e5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e570.md#insn-00b7e5d8)
- 新版 [`00b7e5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e5b4.md#insn-00b7e5d0) · [`00b7e608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e5b4.md#insn-00b7e608) · [`00b7e61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e5b4.md#insn-00b7e61c)

~~~diff
- 00b7e58c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c80:8"]]
- 00b7e58c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7e5d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
+ 00b7e5d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7e58c bytes 084146f9
+ 00b7e5d0 bytes 086946f9
- 00b7e5c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7e5c4 ["INT_ADD", "register:40f0:8", ["const:b7e5c4:8", "const:4:8"]]
- 00b7e5c4 ["CALLIND", null, ["register:0:8"]]
+ 00b7e608 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b7e608 ["INT_ADD", "register:40f0:8", ["const:b7e608:8", "const:4:8"]]
+ 00b7e608 ["CALLIND", null, ["register:0:8"]]
- 00b7e5c4 bytes 00013fd6
+ 00b7e608 bytes 00013fd6
- 00b7e5d8 ["INT_ADD", "register:40f0:8", ["const:b7e5d8:8", "const:4:8"]]
- 00b7e5d8 ["CALL", null, ["callee:00bdb440:8"]]
+ 00b7e61c ["INT_ADD", "register:40f0:8", ["const:b7e61c:8", "const:4:8"]]
+ 00b7e61c ["CALL", null, ["callee:00bdb440:8"]]
- 00b7e5d8 bytes 86730194
+ 00b7e61c bytes 89730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e42a055f4b74ac3f9e77346519314f9"></a>

### [`00b7e650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e650.md) → [`00b7e694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e694.md) _ZNSt6__ndk18ios_base5clearEj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) · 呼出先 1件 [`00b7e690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md)
- 新版 呼出元 1件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) · 呼出先 1件 [`00b7e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md)

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
      "definition_site": "00b7e6cc",
      "incomplete_value": false,
      "site": "00b7e6d0",
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
            "const:81f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e688",
      "incomplete_value": false,
      "site": "00b7e68c",
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
            "const:8ac:8"
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
      "00b7e6cc",
      "PARAM",
      [
        "storage",
        "002978ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7e6cc",
      "PARAM",
      [
        "storage",
        "0029781f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e650.md#insn-00b7e68c) · [`00b7e688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e650.md#insn-00b7e688)
- 新版 [`00b7e6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e694.md#insn-00b7e6d0) · [`00b7e6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e694.md#insn-00b7e6cc)

~~~diff
- 00b7e68c ["INT_ADD", "register:40f0:8", ["const:b7e68c:8", "const:4:8"]]
- 00b7e68c ["CALL", null, ["callee:00b7e6d4:8"]]
+ 00b7e6d0 ["INT_ADD", "register:40f0:8", ["const:b7e6d0:8", "const:4:8"]]
+ 00b7e6d0 ["CALL", null, ["callee:00b7e6d4:8"]]
- 00b7e68c bytes 01000094
+ 00b7e6d0 bytes 01000094
- 00b7e688 ["COPY", "tmp:0:8", ["const:8ac:8"]]
- 00b7e688 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b7e688 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b7e688 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b7e6cc ["COPY", "tmp:0:8", ["const:81f:8"]]
+ 00b7e6cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7e6cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b7e6cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b7e688 bytes 00b02291
+ 00b7e6cc bytes 007c2091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46ab9e6019ebf8f421b52b2d3719ecec"></a>

### [`00b7e690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md) → [`00b7e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md) FUN_00b7e6d4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00b7e268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e268.md) [`00b7e37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e37c.md) [`00b7e490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e490.md) [`00b7e650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e650.md) · 呼出先 6件 [`00b7e108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e108.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 4件 [`00b7e2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e2ac.md) [`00b7e3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e3c0.md) [`00b7e4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e4d4.md) [`00b7e694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e694.md) · 呼出先 6件 [`00b7e14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e14c.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "00b7e714",
      "incomplete_value": false,
      "site": "00b7e714",
      "value": [
        "leaf",
        "const:c24920:8"
      ]
    },
    "old": {
      "definition_site": "00b7e6d0",
      "incomplete_value": false,
      "site": "00b7e6d0",
      "value": [
        "leaf",
        "const:c248d0:8"
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7e734",
      "incomplete_value": true,
      "site": "00b7e73c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e6f0",
      "incomplete_value": true,
      "site": "00b7e6f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "definition_site": "00b7e738",
      "incomplete_value": true,
      "site": "00b7e73c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e6f4",
      "incomplete_value": true,
      "site": "00b7e6f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c70:8"
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
      "00b7e700",
      "READ",
      [
        "storage",
        "010a2048",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7e714",
      "DATA",
      [
        "storage",
        "00c248d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e734",
      "READ",
      [
        "storage",
        "00c1bc88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7e700",
      "READ",
      [
        "storage",
        "010a2088",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7e714",
      "DATA",
      [
        "storage",
        "00c24920",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e734",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e6b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md#insn-00b7e6b4) · [`00b7e6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md#insn-00b7e6f8) · [`00b7e704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md#insn-00b7e704)
- 新版 [`00b7e6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md#insn-00b7e6f8) · [`00b7e73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md#insn-00b7e73c) · [`00b7e748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md#insn-00b7e748)

~~~diff
- 00b7e6b4 ["COPY", "tmp:0:8", ["const:48:8"]]
- 00b7e6b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b7e6b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b7e6b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b7e6f8 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 00b7e6f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7e6f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7e6f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b7e6b4 bytes 08210191
+ 00b7e6f8 bytes 08210291
- 00b7e6f8 ["INT_ADD", "register:40f0:8", ["const:b7e6f8:8", "const:4:8"]]
- 00b7e6f8 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 00b7e73c ["INT_ADD", "register:40f0:8", ["const:b7e73c:8", "const:4:8"]]
+ 00b7e73c ["CALL", null, ["callee:00bdb0c0:8"]]
- 00b7e6f8 bytes 5e720194
+ 00b7e73c bytes 61720194
- 00b7e704 ["INT_ADD", "register:40f0:8", ["const:b7e704:8", "const:4:8"]]
- 00b7e704 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b7e748 ["INT_ADD", "register:40f0:8", ["const:b7e748:8", "const:4:8"]]
+ 00b7e748 ["CALL", null, ["callee:00bdb000:8"]]
- 00b7e704 bytes 2b720194
+ 00b7e748 bytes 2e720194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-898c45ebb501e62e5462ddd76e60ccc1"></a>

### [`00b7ec4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec4c.md) → [`00b7ec90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec90.md) _ZNSt6__ndk18ios_base15sync_with_stdioEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b7eca0",
      "incomplete_value": false,
      "site": "00b7eca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7ec5c",
      "incomplete_value": false,
      "site": "00b7ec5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "00b7ec9c",
      "READ",
      [
        "storage",
        "00c248d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7eca0",
      "WRITE",
      [
        "storage",
        "00c248d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b7ec9c",
      "READ",
      [
        "storage",
        "00c24928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b7eca0",
      "WRITE",
      [
        "storage",
        "00c24928",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ec5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec4c.md#insn-00b7ec5c) · [`00b7ec58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec4c.md#insn-00b7ec58)
- 新版 [`00b7eca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec90.md#insn-00b7eca0) · [`00b7ec9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec90.md#insn-00b7ec9c)

~~~diff
- 00b7ec5c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b7ec5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "const:8d8:8"]]
- 00b7ec5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b7eca0 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00b7eca0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "const:928:8"]]
+ 00b7eca0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b7ec5c bytes 49612339
+ 00b7eca0 bytes 49a12439
- 00b7ec58 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:8d8:8"]]
- 00b7ec58 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b7ec58 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b7ec9c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:928:8"]]
+ 00b7ec9c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b7ec9c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b7ec58 bytes 48616339
+ 00b7ec9c bytes 48a16439
~~~


<a id="compare-33086c933b213196705f89527f03229f"></a>

### [`00b7efe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7efe8.md) → [`00b7f02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f02c.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb350.md) · 呼出先 1件 [`00bdd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd900.md)
- 新版 呼出元 1件 [`00bdb3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3a0.md) · 呼出先 1件 [`00bdd950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd950.md)

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
      "definition_site": "00b7f04c",
      "incomplete_value": true,
      "site": "00b7f04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b7f008",
      "incomplete_value": true,
      "site": "00b7f008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b7f044",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f04c",
      "DATA",
      [
        "storage",
        "00c111d0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00b7f044",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f04c",
      "DATA",
      [
        "storage",
        "00c11220",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7efe8.md#insn-00b7f000) · [`00b7f00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7efe8.md#insn-00b7f00c)
- 新版 [`00b7f044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f02c.md#insn-00b7f044) · [`00b7f050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f02c.md#insn-00b7f050)

~~~diff
- 00b7f000 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a00:8"]]
- 00b7f000 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7f044 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
+ 00b7f044 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7f000 bytes 080145f9
+ 00b7f044 bytes 082945f9
- 00b7f00c ["INT_ADD", "register:40f0:8", ["const:b7f00c:8", "const:4:8"]]
- 00b7f00c ["CALL", null, ["callee:00bdd950:8"]]
+ 00b7f050 ["INT_ADD", "register:40f0:8", ["const:b7f050:8", "const:4:8"]]
+ 00b7f050 ["CALL", null, ["callee:00bdd950:8"]]
- 00b7f00c bytes 3d7a0194
+ 00b7f050 bytes 407a0194
~~~


<a id="compare-b00221287748ce6b2beb8ade66ddf3b0"></a>

### [`00b7f02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f02c.md) → [`00b7f070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f070.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC2ERKS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)

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
      "definition_site": "00b7f098",
      "incomplete_value": true,
      "site": "00b7f098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b7f054",
      "incomplete_value": true,
      "site": "00b7f054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b7f08c",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f098",
      "DATA",
      [
        "storage",
        "00c111d0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00b7f08c",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f098",
      "DATA",
      [
        "storage",
        "00c11220",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f02c.md#insn-00b7f048) · [`00b7f058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f02c.md#insn-00b7f058)
- 新版 [`00b7f08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f070.md#insn-00b7f08c) · [`00b7f09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f070.md#insn-00b7f09c)

~~~diff
- 00b7f048 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a00:8"]]
- 00b7f048 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7f08c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
+ 00b7f08c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7f048 bytes 080145f9
+ 00b7f08c bytes 082945f9
- 00b7f058 ["INT_ADD", "register:40f0:8", ["const:b7f058:8", "const:4:8"]]
- 00b7f058 ["CALL", null, ["callee:00bdd980:8"]]
+ 00b7f09c ["INT_ADD", "register:40f0:8", ["const:b7f09c:8", "const:4:8"]]
+ 00b7f09c ["CALL", null, ["callee:00bdd980:8"]]
- 00b7f058 bytes 367a0194
+ 00b7f09c bytes 397a0194
~~~


<a id="compare-ddfbdc8c16058855353296deceb9c472"></a>

### [`00b7f234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f234.md) → [`00b7f278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f278.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)

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
      "definition_site": "00b7f2a4",
      "incomplete_value": true,
      "site": "00b7f2a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b7f260",
      "incomplete_value": true,
      "site": "00b7f260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b7f2a8",
      "incomplete_value": true,
      "site": "00b7f2a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b7f264",
      "incomplete_value": true,
      "site": "00b7f264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b7f294",
      "READ",
      [
        "storage",
        "00c1b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f2a4",
      "DATA",
      [
        "storage",
        "00c13040",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f2a8",
      "DATA",
      [
        "storage",
        "00c13018",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b7f294",
      "READ",
      [
        "storage",
        "00c1b440",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f2a4",
      "DATA",
      [
        "storage",
        "00c13090",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f2a8",
      "DATA",
      [
        "storage",
        "00c13068",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f234.md#insn-00b7f250) · [`00b7f26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f234.md#insn-00b7f26c)
- 新版 [`00b7f294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f278.md#insn-00b7f294) · [`00b7f2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f278.md#insn-00b7f2b0)

~~~diff
- 00b7f250 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f0:8"]]
- 00b7f250 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b7f294 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:440:8"]]
+ 00b7f294 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7f250 bytes 08f941f9
+ 00b7f294 bytes 082142f9
- 00b7f26c ["INT_ADD", "register:40f0:8", ["const:b7f26c:8", "const:4:8"]]
- 00b7f26c ["CALL", null, ["callee:00bdb390:8"]]
+ 00b7f2b0 ["INT_ADD", "register:40f0:8", ["const:b7f2b0:8", "const:4:8"]]
+ 00b7f2b0 ["CALL", null, ["callee:00bdb390:8"]]
- 00b7f26c bytes 35700194
+ 00b7f2b0 bytes 38700194
~~~


<a id="compare-539aa0cea0859a5a3142f59fa43986f7"></a>

### [`00b7f314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f314.md) → [`00b7f358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f358.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC2ERS3_b

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md)
- 新版 呼出元 1件 [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md)

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
      "definition_site": "00b7f3e8",
      "incomplete_value": true,
      "site": "00b7f3ec",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b7f3a4",
      "incomplete_value": true,
      "site": "00b7f3a8",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b7f3e8",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f3e8",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7f3e8",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f3e8",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f314.md#insn-00b7f3a8) · [`00b7f374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f314.md#insn-00b7f374) · [`00b7f398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f314.md#insn-00b7f398)
- 新版 [`00b7f3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f358.md#insn-00b7f3ec) · [`00b7f3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f358.md#insn-00b7f3b8) · [`00b7f3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f358.md#insn-00b7f3dc)

~~~diff
- 00b7f3a8 ["INT_ADD", "register:40f0:8", ["const:b7f3a8:8", "const:4:8"]]
- 00b7f3a8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b7f3ec ["INT_ADD", "register:40f0:8", ["const:b7f3ec:8", "const:4:8"]]
+ 00b7f3ec ["CALL", null, ["callee:00bdb430:8"]]
- 00b7f3a8 bytes 0e700194
+ 00b7f3ec bytes 11700194
- 00b7f374 ["INT_ADD", "register:40f0:8", ["const:b7f374:8", "const:4:8"]]
- 00b7f374 ["CALL", null, ["callee:00bdc0a0:8"]]
+ 00b7f3b8 ["INT_ADD", "register:40f0:8", ["const:b7f3b8:8", "const:4:8"]]
+ 00b7f3b8 ["CALL", null, ["callee:00bdc0a0:8"]]
- 00b7f374 bytes 37730194
+ 00b7f3b8 bytes 3a730194
- 00b7f398 ["INT_ADD", "register:40f0:8", ["const:b7f398:8", "const:4:8"]]
- 00b7f398 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b7f3dc ["INT_ADD", "register:40f0:8", ["const:b7f3dc:8", "const:4:8"]]
+ 00b7f3dc ["CALL", null, ["callee:00bdb420:8"]]
- 00b7f398 bytes 0e700194
+ 00b7f3dc bytes 11700194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fdec84d76ccec02da07e59e66142a0f"></a>

### [`00b7f724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f724.md) → [`00b7f768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f768.md) FUN_00b7f768

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7f71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f71c.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b7f760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f760.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b7f7bc",
      "incomplete_value": true,
      "site": "00b7f7c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f778",
      "incomplete_value": true,
      "site": "00b7f77c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b7f7bc",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f7bc",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7f7bc",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f7bc",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f77c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f724.md#insn-00b7f77c) · [`00b7f750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f724.md#insn-00b7f750) · [`00b7f76c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f724.md#insn-00b7f76c)
- 新版 [`00b7f7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f768.md#insn-00b7f7c0) · [`00b7f794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f768.md#insn-00b7f794) · [`00b7f7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f768.md#insn-00b7f7b0)

~~~diff
- 00b7f77c ["INT_ADD", "register:40f0:8", ["const:b7f77c:8", "const:4:8"]]
- 00b7f77c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b7f7c0 ["INT_ADD", "register:40f0:8", ["const:b7f7c0:8", "const:4:8"]]
+ 00b7f7c0 ["CALL", null, ["callee:00bdb430:8"]]
- 00b7f77c bytes 196f0194
+ 00b7f7c0 bytes 1c6f0194
- 00b7f750 ["INT_ADD", "register:40f0:8", ["const:b7f750:8", "const:4:8"]]
- 00b7f750 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b7f794 ["INT_ADD", "register:40f0:8", ["const:b7f794:8", "const:4:8"]]
+ 00b7f794 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b7f750 bytes f8750194
+ 00b7f794 bytes fb750194
- 00b7f76c ["INT_ADD", "register:40f0:8", ["const:b7f76c:8", "const:4:8"]]
- 00b7f76c ["CALL", null, ["callee:00bdb420:8"]]
+ 00b7f7b0 ["INT_ADD", "register:40f0:8", ["const:b7f7b0:8", "const:4:8"]]
+ 00b7f7b0 ["CALL", null, ["callee:00bdb420:8"]]
- 00b7f76c bytes 196f0194
+ 00b7f7b0 bytes 1c6f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03e8014d1bf08234a5ff3d677999ecb3"></a>

### [`00b7f85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f85c.md) → [`00b7f8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f8a0.md) FUN_00b7f8a0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7f854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f854.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b7f898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f898.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b7f8f4",
      "incomplete_value": true,
      "site": "00b7f8f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f8b0",
      "incomplete_value": true,
      "site": "00b7f8b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b7f8f4",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f8f4",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7f8f4",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7f8f4",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f85c.md#insn-00b7f8b4) · [`00b7f888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f85c.md#insn-00b7f888) · [`00b7f8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f85c.md#insn-00b7f8a4)
- 新版 [`00b7f8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f8a0.md#insn-00b7f8f8) · [`00b7f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f8a0.md#insn-00b7f8cc) · [`00b7f8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f8a0.md#insn-00b7f8e8)

~~~diff
- 00b7f8b4 ["INT_ADD", "register:40f0:8", ["const:b7f8b4:8", "const:4:8"]]
- 00b7f8b4 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b7f8f8 ["INT_ADD", "register:40f0:8", ["const:b7f8f8:8", "const:4:8"]]
+ 00b7f8f8 ["CALL", null, ["callee:00bdb430:8"]]
- 00b7f8b4 bytes cb6e0194
+ 00b7f8f8 bytes ce6e0194
- 00b7f888 ["INT_ADD", "register:40f0:8", ["const:b7f888:8", "const:4:8"]]
- 00b7f888 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b7f8cc ["INT_ADD", "register:40f0:8", ["const:b7f8cc:8", "const:4:8"]]
+ 00b7f8cc ["CALL", null, ["callee:00bdcf80:8"]]
- 00b7f888 bytes aa750194
+ 00b7f8cc bytes ad750194
- 00b7f8a4 ["INT_ADD", "register:40f0:8", ["const:b7f8a4:8", "const:4:8"]]
- 00b7f8a4 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b7f8e8 ["INT_ADD", "register:40f0:8", ["const:b7f8e8:8", "const:4:8"]]
+ 00b7f8e8 ["CALL", null, ["callee:00bdb420:8"]]
- 00b7f8a4 bytes cb6e0194
+ 00b7f8e8 bytes ce6e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-874758f3d03bd24d59d0e32613fd5fd6"></a>

### [`00b7f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f9d4.md) → [`00b7fa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fa18.md) FUN_00b7fa18

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7f9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f9cc.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b7fa10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fa10.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b7fa6c",
      "incomplete_value": true,
      "site": "00b7fa70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fa28",
      "incomplete_value": true,
      "site": "00b7fa2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b7fa6c",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fa6c",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7fa6c",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fa6c",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f9d4.md#insn-00b7fa2c) · [`00b7fa00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f9d4.md#insn-00b7fa00) · [`00b7fa1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f9d4.md#insn-00b7fa1c)
- 新版 [`00b7fa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fa18.md#insn-00b7fa70) · [`00b7fa44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fa18.md#insn-00b7fa44) · [`00b7fa60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fa18.md#insn-00b7fa60)

~~~diff
- 00b7fa2c ["INT_ADD", "register:40f0:8", ["const:b7fa2c:8", "const:4:8"]]
- 00b7fa2c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b7fa70 ["INT_ADD", "register:40f0:8", ["const:b7fa70:8", "const:4:8"]]
+ 00b7fa70 ["CALL", null, ["callee:00bdb430:8"]]
- 00b7fa2c bytes 6d6e0194
+ 00b7fa70 bytes 706e0194
- 00b7fa00 ["INT_ADD", "register:40f0:8", ["const:b7fa00:8", "const:4:8"]]
- 00b7fa00 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b7fa44 ["INT_ADD", "register:40f0:8", ["const:b7fa44:8", "const:4:8"]]
+ 00b7fa44 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b7fa00 bytes 4c750194
+ 00b7fa44 bytes 4f750194
- 00b7fa1c ["INT_ADD", "register:40f0:8", ["const:b7fa1c:8", "const:4:8"]]
- 00b7fa1c ["CALL", null, ["callee:00bdb420:8"]]
+ 00b7fa60 ["INT_ADD", "register:40f0:8", ["const:b7fa60:8", "const:4:8"]]
+ 00b7fa60 ["CALL", null, ["callee:00bdb420:8"]]
- 00b7fa1c bytes 6d6e0194
+ 00b7fa60 bytes 706e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7da31fe95670f28ec62bd3a1f7fec4b6"></a>

### [`00b7fb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fb0c.md) → [`00b7fb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fb50.md) FUN_00b7fb50

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7fb04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fb04.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b7fb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fb48.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b7fba4",
      "incomplete_value": true,
      "site": "00b7fba8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fb60",
      "incomplete_value": true,
      "site": "00b7fb64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b7fba4",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fba4",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7fba4",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fba4",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fb64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fb0c.md#insn-00b7fb64) · [`00b7fb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fb0c.md#insn-00b7fb38) · [`00b7fb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fb0c.md#insn-00b7fb54)
- 新版 [`00b7fba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fb50.md#insn-00b7fba8) · [`00b7fb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fb50.md#insn-00b7fb7c) · [`00b7fb98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fb50.md#insn-00b7fb98)

~~~diff
- 00b7fb64 ["INT_ADD", "register:40f0:8", ["const:b7fb64:8", "const:4:8"]]
- 00b7fb64 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b7fba8 ["INT_ADD", "register:40f0:8", ["const:b7fba8:8", "const:4:8"]]
+ 00b7fba8 ["CALL", null, ["callee:00bdb430:8"]]
- 00b7fb64 bytes 1f6e0194
+ 00b7fba8 bytes 226e0194
- 00b7fb38 ["INT_ADD", "register:40f0:8", ["const:b7fb38:8", "const:4:8"]]
- 00b7fb38 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b7fb7c ["INT_ADD", "register:40f0:8", ["const:b7fb7c:8", "const:4:8"]]
+ 00b7fb7c ["CALL", null, ["callee:00bdcf80:8"]]
- 00b7fb38 bytes fe740194
+ 00b7fb7c bytes 01750194
- 00b7fb54 ["INT_ADD", "register:40f0:8", ["const:b7fb54:8", "const:4:8"]]
- 00b7fb54 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b7fb98 ["INT_ADD", "register:40f0:8", ["const:b7fb98:8", "const:4:8"]]
+ 00b7fb98 ["CALL", null, ["callee:00bdb420:8"]]
- 00b7fb54 bytes 1f6e0194
+ 00b7fb98 bytes 226e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af15c978bd70742e7e0bd4c3342dbbc0"></a>

### [`00b7fc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fc88.md) → [`00b7fccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fccc.md) FUN_00b7fccc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7fc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fc80.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b7fcc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fcc4.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b7fd20",
      "incomplete_value": true,
      "site": "00b7fd24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fcdc",
      "incomplete_value": true,
      "site": "00b7fce0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b7fd20",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fd20",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7fd20",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fd20",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fc88.md#insn-00b7fce0) · [`00b7fcb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fc88.md#insn-00b7fcb4) · [`00b7fcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fc88.md#insn-00b7fcd0)
- 新版 [`00b7fd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fccc.md#insn-00b7fd24) · [`00b7fcf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fccc.md#insn-00b7fcf8) · [`00b7fd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fccc.md#insn-00b7fd14)

~~~diff
- 00b7fce0 ["INT_ADD", "register:40f0:8", ["const:b7fce0:8", "const:4:8"]]
- 00b7fce0 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b7fd24 ["INT_ADD", "register:40f0:8", ["const:b7fd24:8", "const:4:8"]]
+ 00b7fd24 ["CALL", null, ["callee:00bdb430:8"]]
- 00b7fce0 bytes c06d0194
+ 00b7fd24 bytes c36d0194
- 00b7fcb4 ["INT_ADD", "register:40f0:8", ["const:b7fcb4:8", "const:4:8"]]
- 00b7fcb4 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b7fcf8 ["INT_ADD", "register:40f0:8", ["const:b7fcf8:8", "const:4:8"]]
+ 00b7fcf8 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b7fcb4 bytes 9f740194
+ 00b7fcf8 bytes a2740194
- 00b7fcd0 ["INT_ADD", "register:40f0:8", ["const:b7fcd0:8", "const:4:8"]]
- 00b7fcd0 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b7fd14 ["INT_ADD", "register:40f0:8", ["const:b7fd14:8", "const:4:8"]]
+ 00b7fd14 ["CALL", null, ["callee:00bdb420:8"]]
- 00b7fcd0 bytes c06d0194
+ 00b7fd14 bytes c36d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f78ecfddcf8e6491c71470a76543f401"></a>

### [`00b7fdc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fdc0.md) → [`00b7fe04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fe04.md) FUN_00b7fe04

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7fdb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fdb8.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b7fdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fdfc.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b7fe58",
      "incomplete_value": true,
      "site": "00b7fe5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fe14",
      "incomplete_value": true,
      "site": "00b7fe18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b7fe58",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fe58",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7fe58",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7fe58",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fe18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fdc0.md#insn-00b7fe18) · [`00b7fdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fdc0.md#insn-00b7fdec) · [`00b7fe08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fdc0.md#insn-00b7fe08)
- 新版 [`00b7fe5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fe04.md#insn-00b7fe5c) · [`00b7fe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fe04.md#insn-00b7fe30) · [`00b7fe4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fe04.md#insn-00b7fe4c)

~~~diff
- 00b7fe18 ["INT_ADD", "register:40f0:8", ["const:b7fe18:8", "const:4:8"]]
- 00b7fe18 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b7fe5c ["INT_ADD", "register:40f0:8", ["const:b7fe5c:8", "const:4:8"]]
+ 00b7fe5c ["CALL", null, ["callee:00bdb430:8"]]
- 00b7fe18 bytes 726d0194
+ 00b7fe5c bytes 756d0194
- 00b7fdec ["INT_ADD", "register:40f0:8", ["const:b7fdec:8", "const:4:8"]]
- 00b7fdec ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b7fe30 ["INT_ADD", "register:40f0:8", ["const:b7fe30:8", "const:4:8"]]
+ 00b7fe30 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b7fdec bytes 51740194
+ 00b7fe30 bytes 54740194
- 00b7fe08 ["INT_ADD", "register:40f0:8", ["const:b7fe08:8", "const:4:8"]]
- 00b7fe08 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b7fe4c ["INT_ADD", "register:40f0:8", ["const:b7fe4c:8", "const:4:8"]]
+ 00b7fe4c ["CALL", null, ["callee:00bdb420:8"]]
- 00b7fe08 bytes 726d0194
+ 00b7fe4c bytes 756d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e97a6868d257ae53d08ebc10bf9fe373"></a>

### [`00b7fef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fef8.md) → [`00b7ff3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7ff3c.md) FUN_00b7ff3c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7fef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fef0.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b7ff34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7ff34.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b7ff90",
      "incomplete_value": true,
      "site": "00b7ff94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7ff4c",
      "incomplete_value": true,
      "site": "00b7ff50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b7ff90",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ff90",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7ff90",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ff90",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ff50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fef8.md#insn-00b7ff50) · [`00b7ff24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fef8.md#insn-00b7ff24) · [`00b7ff40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fef8.md#insn-00b7ff40)
- 新版 [`00b7ff94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7ff3c.md#insn-00b7ff94) · [`00b7ff68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7ff3c.md#insn-00b7ff68) · [`00b7ff84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7ff3c.md#insn-00b7ff84)

~~~diff
- 00b7ff50 ["INT_ADD", "register:40f0:8", ["const:b7ff50:8", "const:4:8"]]
- 00b7ff50 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b7ff94 ["INT_ADD", "register:40f0:8", ["const:b7ff94:8", "const:4:8"]]
+ 00b7ff94 ["CALL", null, ["callee:00bdb430:8"]]
- 00b7ff50 bytes 246d0194
+ 00b7ff94 bytes 276d0194
- 00b7ff24 ["INT_ADD", "register:40f0:8", ["const:b7ff24:8", "const:4:8"]]
- 00b7ff24 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b7ff68 ["INT_ADD", "register:40f0:8", ["const:b7ff68:8", "const:4:8"]]
+ 00b7ff68 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b7ff24 bytes 03740194
+ 00b7ff68 bytes 06740194
- 00b7ff40 ["INT_ADD", "register:40f0:8", ["const:b7ff40:8", "const:4:8"]]
- 00b7ff40 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b7ff84 ["INT_ADD", "register:40f0:8", ["const:b7ff84:8", "const:4:8"]]
+ 00b7ff84 ["CALL", null, ["callee:00bdb420:8"]]
- 00b7ff40 bytes 246d0194
+ 00b7ff84 bytes 276d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffe44c7a8e9bac2c94138a2b53588f4e"></a>

### [`00b80030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80030.md) → [`00b80074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80074.md) FUN_00b80074

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b80028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80028.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b8006c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8006c.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b800c8",
      "incomplete_value": true,
      "site": "00b800cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b80084",
      "incomplete_value": true,
      "site": "00b80088",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b800c8",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b800c8",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b800c8",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b800c8",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80030.md#insn-00b80088) · [`00b8005c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80030.md#insn-00b8005c) · [`00b80078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80030.md#insn-00b80078)
- 新版 [`00b800cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80074.md#insn-00b800cc) · [`00b800a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80074.md#insn-00b800a0) · [`00b800bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80074.md#insn-00b800bc)

~~~diff
- 00b80088 ["INT_ADD", "register:40f0:8", ["const:b80088:8", "const:4:8"]]
- 00b80088 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b800cc ["INT_ADD", "register:40f0:8", ["const:b800cc:8", "const:4:8"]]
+ 00b800cc ["CALL", null, ["callee:00bdb430:8"]]
- 00b80088 bytes d66c0194
+ 00b800cc bytes d96c0194
- 00b8005c ["INT_ADD", "register:40f0:8", ["const:b8005c:8", "const:4:8"]]
- 00b8005c ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b800a0 ["INT_ADD", "register:40f0:8", ["const:b800a0:8", "const:4:8"]]
+ 00b800a0 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b8005c bytes b5730194
+ 00b800a0 bytes b8730194
- 00b80078 ["INT_ADD", "register:40f0:8", ["const:b80078:8", "const:4:8"]]
- 00b80078 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b800bc ["INT_ADD", "register:40f0:8", ["const:b800bc:8", "const:4:8"]]
+ 00b800bc ["CALL", null, ["callee:00bdb420:8"]]
- 00b80078 bytes d66c0194
+ 00b800bc bytes d96c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cac631dff4365a6cf57ab9c6d96734a"></a>

### [`00b802a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b802a0.md) → [`00b802e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b802e4.md) FUN_00b802e4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b80298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80298.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b802dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b802dc.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b80338",
      "incomplete_value": true,
      "site": "00b8033c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b802f4",
      "incomplete_value": true,
      "site": "00b802f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b80338",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b80338",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b80338",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b80338",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b802f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b802a0.md#insn-00b802f8) · [`00b802cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b802a0.md#insn-00b802cc) · [`00b802e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b802a0.md#insn-00b802e8)
- 新版 [`00b8033c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b802e4.md#insn-00b8033c) · [`00b80310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b802e4.md#insn-00b80310) · [`00b8032c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b802e4.md#insn-00b8032c)

~~~diff
- 00b802f8 ["INT_ADD", "register:40f0:8", ["const:b802f8:8", "const:4:8"]]
- 00b802f8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8033c ["INT_ADD", "register:40f0:8", ["const:b8033c:8", "const:4:8"]]
+ 00b8033c ["CALL", null, ["callee:00bdb430:8"]]
- 00b802f8 bytes 3a6c0194
+ 00b8033c bytes 3d6c0194
- 00b802cc ["INT_ADD", "register:40f0:8", ["const:b802cc:8", "const:4:8"]]
- 00b802cc ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b80310 ["INT_ADD", "register:40f0:8", ["const:b80310:8", "const:4:8"]]
+ 00b80310 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b802cc bytes 19730194
+ 00b80310 bytes 1c730194
- 00b802e8 ["INT_ADD", "register:40f0:8", ["const:b802e8:8", "const:4:8"]]
- 00b802e8 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b8032c ["INT_ADD", "register:40f0:8", ["const:b8032c:8", "const:4:8"]]
+ 00b8032c ["CALL", null, ["callee:00bdb420:8"]]
- 00b802e8 bytes 3a6c0194
+ 00b8032c bytes 3d6c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9efad93efb69ee372f51f7461179ff0f"></a>

### [`00b803d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b803d8.md) → [`00b8041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8041c.md) FUN_00b8041c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b803d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b803d0.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b80414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80414.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b80470",
      "incomplete_value": true,
      "site": "00b80474",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8042c",
      "incomplete_value": true,
      "site": "00b80430",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b80470",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b80470",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b80470",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b80470",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b803d8.md#insn-00b80430) · [`00b80404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b803d8.md#insn-00b80404) · [`00b80420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b803d8.md#insn-00b80420)
- 新版 [`00b80474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8041c.md#insn-00b80474) · [`00b80448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8041c.md#insn-00b80448) · [`00b80464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8041c.md#insn-00b80464)

~~~diff
- 00b80430 ["INT_ADD", "register:40f0:8", ["const:b80430:8", "const:4:8"]]
- 00b80430 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b80474 ["INT_ADD", "register:40f0:8", ["const:b80474:8", "const:4:8"]]
+ 00b80474 ["CALL", null, ["callee:00bdb430:8"]]
- 00b80430 bytes ec6b0194
+ 00b80474 bytes ef6b0194
- 00b80404 ["INT_ADD", "register:40f0:8", ["const:b80404:8", "const:4:8"]]
- 00b80404 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b80448 ["INT_ADD", "register:40f0:8", ["const:b80448:8", "const:4:8"]]
+ 00b80448 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b80404 bytes cb720194
+ 00b80448 bytes ce720194
- 00b80420 ["INT_ADD", "register:40f0:8", ["const:b80420:8", "const:4:8"]]
- 00b80420 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b80464 ["INT_ADD", "register:40f0:8", ["const:b80464:8", "const:4:8"]]
+ 00b80464 ["CALL", null, ["callee:00bdb420:8"]]
- 00b80420 bytes ec6b0194
+ 00b80464 bytes ef6b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1e550810e4255e5e5677c781fa45112"></a>

### [`00b80510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80510.md) → [`00b80554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80554.md) FUN_00b80554

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b80508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80508.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b8054c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8054c.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b805a8",
      "incomplete_value": true,
      "site": "00b805ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b80564",
      "incomplete_value": true,
      "site": "00b80568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b805a8",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b805a8",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b805a8",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b805a8",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80510.md#insn-00b80568) · [`00b8053c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80510.md#insn-00b8053c) · [`00b80558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80510.md#insn-00b80558)
- 新版 [`00b805ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80554.md#insn-00b805ac) · [`00b80580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80554.md#insn-00b80580) · [`00b8059c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80554.md#insn-00b8059c)

~~~diff
- 00b80568 ["INT_ADD", "register:40f0:8", ["const:b80568:8", "const:4:8"]]
- 00b80568 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b805ac ["INT_ADD", "register:40f0:8", ["const:b805ac:8", "const:4:8"]]
+ 00b805ac ["CALL", null, ["callee:00bdb430:8"]]
- 00b80568 bytes 9e6b0194
+ 00b805ac bytes a16b0194
- 00b8053c ["INT_ADD", "register:40f0:8", ["const:b8053c:8", "const:4:8"]]
- 00b8053c ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b80580 ["INT_ADD", "register:40f0:8", ["const:b80580:8", "const:4:8"]]
+ 00b80580 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b8053c bytes 7d720194
+ 00b80580 bytes 80720194
- 00b80558 ["INT_ADD", "register:40f0:8", ["const:b80558:8", "const:4:8"]]
- 00b80558 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b8059c ["INT_ADD", "register:40f0:8", ["const:b8059c:8", "const:4:8"]]
+ 00b8059c ["CALL", null, ["callee:00bdb420:8"]]
- 00b80558 bytes 9e6b0194
+ 00b8059c bytes a16b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1476b7cdbbc694bd983ab4debf084fcb"></a>

### [`00b80648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80648.md) → [`00b8068c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8068c.md) FUN_00b8068c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b80640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80640.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdcf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf30.md)
- 新版 呼出元 1件 [`00b80684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80684.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)

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
      "definition_site": "00b806e0",
      "incomplete_value": true,
      "site": "00b806e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8069c",
      "incomplete_value": true,
      "site": "00b806a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
      "00b806e0",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00b806e0",
      "PARAM",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b806e0",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00b806e0",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b806a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80648.md#insn-00b806a0) · [`00b80674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80648.md#insn-00b80674) · [`00b80690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80648.md#insn-00b80690)
- 新版 [`00b806e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8068c.md#insn-00b806e4) · [`00b806b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8068c.md#insn-00b806b8) · [`00b806d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8068c.md#insn-00b806d4)

~~~diff
- 00b806a0 ["INT_ADD", "register:40f0:8", ["const:b806a0:8", "const:4:8"]]
- 00b806a0 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b806e4 ["INT_ADD", "register:40f0:8", ["const:b806e4:8", "const:4:8"]]
+ 00b806e4 ["CALL", null, ["callee:00bdb430:8"]]
- 00b806a0 bytes 506b0194
+ 00b806e4 bytes 536b0194
- 00b80674 ["INT_ADD", "register:40f0:8", ["const:b80674:8", "const:4:8"]]
- 00b80674 ["CALL", null, ["callee:00bdcf80:8"]]
+ 00b806b8 ["INT_ADD", "register:40f0:8", ["const:b806b8:8", "const:4:8"]]
+ 00b806b8 ["CALL", null, ["callee:00bdcf80:8"]]
- 00b80674 bytes 2f720194
+ 00b806b8 bytes 32720194
- 00b80690 ["INT_ADD", "register:40f0:8", ["const:b80690:8", "const:4:8"]]
- 00b80690 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b806d4 ["INT_ADD", "register:40f0:8", ["const:b806d4:8", "const:4:8"]]
+ 00b806d4 ["CALL", null, ["callee:00bdb420:8"]]
- 00b80690 bytes 506b0194
+ 00b806d4 bytes 536b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-783235aebd1cb6e3695faba521bbe076"></a>

### [`00b808cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b808cc.md) → [`00b80910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80910.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPcl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1370.md)

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
      "definition_site": "00b80950",
      "incomplete_value": true,
      "site": "00b80954",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b8090c",
      "incomplete_value": true,
      "site": "00b80910",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b80950",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b80950",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b80950",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b80950",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b808cc.md#insn-00b80910) · [`00b80900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b808cc.md#insn-00b80900) · [`00b8090c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b808cc.md#insn-00b8090c)
- 新版 [`00b80954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80910.md#insn-00b80954) · [`00b80944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80910.md#insn-00b80944) · [`00b80950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80910.md#insn-00b80950)

~~~diff
- 00b80910 ["INT_ADD", "register:40f0:8", ["const:b80910:8", "const:4:8"]]
- 00b80910 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b80954 ["INT_ADD", "register:40f0:8", ["const:b80954:8", "const:4:8"]]
+ 00b80954 ["CALL", null, ["callee:00bdb430:8"]]
- 00b80910 bytes b46a0194
+ 00b80954 bytes b76a0194
- 00b80900 ["INT_ADD", "register:40f0:8", ["const:b80900:8", "const:4:8"]]
- 00b80900 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b80944 ["INT_ADD", "register:40f0:8", ["const:b80944:8", "const:4:8"]]
+ 00b80944 ["CALL", null, ["callee:00bdb420:8"]]
- 00b80900 bytes b46a0194
+ 00b80944 bytes b76a0194
- 00b8090c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 00b8090c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b80950 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 00b80950 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8090c bytes 21f846f9
+ 00b80950 bytes 212047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-413cd81f223def10885661067b670e45"></a>

### [`00b80b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80b44.md) → [`00b80b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80b88.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be1330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1330.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1380.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b80bc0",
      "incomplete_value": true,
      "site": "00b80bc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b80b7c",
      "incomplete_value": true,
      "site": "00b80b80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b80bc0",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b80bc0",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b80bc0",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b80bc0",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80b44.md#insn-00b80b80) · [`00b80b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80b44.md#insn-00b80b70) · [`00b80b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80b44.md#insn-00b80b7c)
- 新版 [`00b80bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80b88.md#insn-00b80bc4) · [`00b80bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80b88.md#insn-00b80bb4) · [`00b80bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80b88.md#insn-00b80bc0)

~~~diff
- 00b80b80 ["INT_ADD", "register:40f0:8", ["const:b80b80:8", "const:4:8"]]
- 00b80b80 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b80bc4 ["INT_ADD", "register:40f0:8", ["const:b80bc4:8", "const:4:8"]]
+ 00b80bc4 ["CALL", null, ["callee:00bdb430:8"]]
- 00b80b80 bytes 186a0194
+ 00b80bc4 bytes 1b6a0194
- 00b80b70 ["INT_ADD", "register:40f0:8", ["const:b80b70:8", "const:4:8"]]
- 00b80b70 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b80bb4 ["INT_ADD", "register:40f0:8", ["const:b80bb4:8", "const:4:8"]]
+ 00b80bb4 ["CALL", null, ["callee:00bdb420:8"]]
- 00b80b70 bytes 186a0194
+ 00b80bb4 bytes 1b6a0194
- 00b80b7c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 00b80b7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b80bc0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 00b80bc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b80b7c bytes 21f846f9
+ 00b80bc0 bytes 212047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67c13f663636c90e4bcb129626bdb6c7"></a>

### [`00b80d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80d48.md) → [`00b80d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80d8c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be1340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1340.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1390.md)

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
      "definition_site": "00b80dcc",
      "incomplete_value": true,
      "site": "00b80dd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b80d88",
      "incomplete_value": true,
      "site": "00b80d8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b80dcc",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b80dcc",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b80dcc",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00b80dcc",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80d48.md#insn-00b80d8c) · [`00b80d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80d48.md#insn-00b80d7c) · [`00b80d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b80/00b80d48.md#insn-00b80d88)
- 新版 [`00b80dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80d8c.md#insn-00b80dd0) · [`00b80dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80d8c.md#insn-00b80dc0) · [`00b80dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80d8c.md#insn-00b80dcc)

~~~diff
- 00b80d8c ["INT_ADD", "register:40f0:8", ["const:b80d8c:8", "const:4:8"]]
- 00b80d8c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b80dd0 ["INT_ADD", "register:40f0:8", ["const:b80dd0:8", "const:4:8"]]
+ 00b80dd0 ["CALL", null, ["callee:00bdb430:8"]]
- 00b80d8c bytes 95690194
+ 00b80dd0 bytes 98690194
- 00b80d7c ["INT_ADD", "register:40f0:8", ["const:b80d7c:8", "const:4:8"]]
- 00b80d7c ["CALL", null, ["callee:00bdb420:8"]]
+ 00b80dc0 ["INT_ADD", "register:40f0:8", ["const:b80dc0:8", "const:4:8"]]
+ 00b80dc0 ["CALL", null, ["callee:00bdb420:8"]]
- 00b80d7c bytes 95690194
+ 00b80dc0 bytes 98690194
- 00b80d88 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 00b80d88 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b80dcc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 00b80dcc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b80d88 bytes 21f846f9
+ 00b80dcc bytes 212047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c2ee299d32e2e3a882e476fc6ac3a51"></a>

### [`00b819e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b819e8.md) → [`00b81a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81a2c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)

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
      "definition_site": "00b81a58",
      "incomplete_value": true,
      "site": "00b81a58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b81a14",
      "incomplete_value": true,
      "site": "00b81a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b81a54",
      "incomplete_value": true,
      "site": "00b81a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b81a10",
      "incomplete_value": true,
      "site": "00b81a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b81a48",
      "READ",
      [
        "storage",
        "00c1bc98",
        null,
        "pointer"
      ]
    ],
    [
      "00b81a58",
      "DATA",
      [
        "storage",
        "00c130a0",
        null,
        "pointer"
      ]
    ],
    [
      "00b81a5c",
      "DATA",
      [
        "storage",
        "00c13078",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b81a48",
      "READ",
      [
        "storage",
        "00c1bce8",
        null,
        "pointer"
      ]
    ],
    [
      "00b81a58",
      "DATA",
      [
        "storage",
        "00c130f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b81a5c",
      "DATA",
      [
        "storage",
        "00c130c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b819e8.md#insn-00b81a04) · [`00b81a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b819e8.md#insn-00b81a20)
- 新版 [`00b81a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81a2c.md#insn-00b81a48) · [`00b81a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81a2c.md#insn-00b81a64)

~~~diff
- 00b81a04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
- 00b81a04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b81a48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce8:8"]]
+ 00b81a48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b81a04 bytes 084d46f9
+ 00b81a48 bytes 087546f9
- 00b81a20 ["INT_ADD", "register:40f0:8", ["const:b81a20:8", "const:4:8"]]
- 00b81a20 ["CALL", null, ["callee:00bdb390:8"]]
+ 00b81a64 ["INT_ADD", "register:40f0:8", ["const:b81a64:8", "const:4:8"]]
+ 00b81a64 ["CALL", null, ["callee:00bdb390:8"]]
- 00b81a20 bytes 48660194
+ 00b81a64 bytes 4b660194
~~~


<a id="compare-1189aa456bac2c78d3743ba5c5d609ff"></a>

### [`00b81c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81c48.md) → [`00b81c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c8c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b81ce0",
      "incomplete_value": true,
      "site": "00b81ce4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81c9c",
      "incomplete_value": true,
      "site": "00b81ca0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
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
      "definition_site": "00b81d28",
      "incomplete_value": true,
      "site": "00b81d2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b81ce4",
      "incomplete_value": true,
      "site": "00b81ce8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b81ce0",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b81ce0",
      "PARAM",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b81d28",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b81ce0",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00b81ce0",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b81d28",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81c48.md#insn-00b81ca0) · [`00b81ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81c48.md#insn-00b81ce4) · [`00b81ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81c48.md#insn-00b81ce8)
- 新版 [`00b81ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c8c.md#insn-00b81ce4) · [`00b81d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c8c.md#insn-00b81d28) · [`00b81d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c8c.md#insn-00b81d2c)

~~~diff
- 00b81ca0 ["INT_ADD", "register:40f0:8", ["const:b81ca0:8", "const:4:8"]]
- 00b81ca0 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b81ce4 ["INT_ADD", "register:40f0:8", ["const:b81ce4:8", "const:4:8"]]
+ 00b81ce4 ["CALL", null, ["callee:00bdb430:8"]]
- 00b81ca0 bytes d0650194
+ 00b81ce4 bytes d3650194
- 00b81ce4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 00b81ce4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b81d28 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 00b81d28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b81ce4 bytes 21f846f9
+ 00b81d28 bytes 212047f9
- 00b81ce8 ["INT_ADD", "register:40f0:8", ["const:b81ce8:8", "const:4:8"]]
- 00b81ce8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b81d2c ["INT_ADD", "register:40f0:8", ["const:b81d2c:8", "const:4:8"]]
+ 00b81d2c ["CALL", null, ["callee:00bdb430:8"]]
- 00b81ce8 bytes be650194
+ 00b81d2c bytes c1650194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5460b37e409f3a60e27be0dbf4539fed"></a>

### [`00b81dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81dd8.md) → [`00b81e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81e1c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEx

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b81e70",
      "incomplete_value": true,
      "site": "00b81e74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81e2c",
      "incomplete_value": true,
      "site": "00b81e30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
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
      "definition_site": "00b81eb8",
      "incomplete_value": true,
      "site": "00b81ebc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b81e74",
      "incomplete_value": true,
      "site": "00b81e78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b81e70",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b81e70",
      "PARAM",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b81eb8",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b81e70",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00b81e70",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b81eb8",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81dd8.md#insn-00b81e30) · [`00b81e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81dd8.md#insn-00b81e74) · [`00b81e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81dd8.md#insn-00b81e78)
- 新版 [`00b81e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81e1c.md#insn-00b81e74) · [`00b81eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81e1c.md#insn-00b81eb8) · [`00b81ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81e1c.md#insn-00b81ebc)

~~~diff
- 00b81e30 ["INT_ADD", "register:40f0:8", ["const:b81e30:8", "const:4:8"]]
- 00b81e30 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b81e74 ["INT_ADD", "register:40f0:8", ["const:b81e74:8", "const:4:8"]]
+ 00b81e74 ["CALL", null, ["callee:00bdb430:8"]]
- 00b81e30 bytes 6c650194
+ 00b81e74 bytes 6f650194
- 00b81e74 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 00b81e74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b81eb8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 00b81eb8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b81e74 bytes 21f846f9
+ 00b81eb8 bytes 212047f9
- 00b81e78 ["INT_ADD", "register:40f0:8", ["const:b81e78:8", "const:4:8"]]
- 00b81e78 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b81ebc ["INT_ADD", "register:40f0:8", ["const:b81ebc:8", "const:4:8"]]
+ 00b81ebc ["CALL", null, ["callee:00bdb430:8"]]
- 00b81e78 bytes 5a650194
+ 00b81ebc bytes 5d650194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e38604b3b3516f4eb834d0f84860c90f"></a>

### [`00b81f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81f68.md) → [`00b81fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81fac.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEy

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b82000",
      "incomplete_value": true,
      "site": "00b82004",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81fbc",
      "incomplete_value": true,
      "site": "00b81fc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
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
      "definition_site": "00b82048",
      "incomplete_value": true,
      "site": "00b8204c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b82004",
      "incomplete_value": true,
      "site": "00b82008",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b82000",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b82000",
      "PARAM",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b82048",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b82000",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00b82000",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b82048",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81f68.md#insn-00b81fc0) · [`00b82004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81f68.md#insn-00b82004) · [`00b82008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81f68.md#insn-00b82008)
- 新版 [`00b82004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81fac.md#insn-00b82004) · [`00b82048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81fac.md#insn-00b82048) · [`00b8204c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81fac.md#insn-00b8204c)

~~~diff
- 00b81fc0 ["INT_ADD", "register:40f0:8", ["const:b81fc0:8", "const:4:8"]]
- 00b81fc0 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b82004 ["INT_ADD", "register:40f0:8", ["const:b82004:8", "const:4:8"]]
+ 00b82004 ["CALL", null, ["callee:00bdb430:8"]]
- 00b81fc0 bytes 08650194
+ 00b82004 bytes 0b650194
- 00b82004 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 00b82004 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b82048 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 00b82048 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b82004 bytes 21f846f9
+ 00b82048 bytes 212047f9
- 00b82008 ["INT_ADD", "register:40f0:8", ["const:b82008:8", "const:4:8"]]
- 00b82008 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8204c ["INT_ADD", "register:40f0:8", ["const:b8204c:8", "const:4:8"]]
+ 00b8204c ["CALL", null, ["callee:00bdb430:8"]]
- 00b82008 bytes f6640194
+ 00b8204c bytes f9640194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54403c1380169b71f9421355764ef29e"></a>

### [`00b820f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b820f8.md) → [`00b8213c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8213c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEf

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b82194",
      "incomplete_value": true,
      "site": "00b82198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b82150",
      "incomplete_value": true,
      "site": "00b82154",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
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
      "definition_site": "00b821dc",
      "incomplete_value": true,
      "site": "00b821e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b82198",
      "incomplete_value": true,
      "site": "00b8219c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b82194",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b82194",
      "PARAM",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b821dc",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b82194",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00b82194",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b821dc",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b820f8.md#insn-00b82154) · [`00b82198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b820f8.md#insn-00b82198) · [`00b8219c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b820f8.md#insn-00b8219c)
- 新版 [`00b82198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8213c.md#insn-00b82198) · [`00b821dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8213c.md#insn-00b821dc) · [`00b821e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8213c.md#insn-00b821e0)

~~~diff
- 00b82154 ["INT_ADD", "register:40f0:8", ["const:b82154:8", "const:4:8"]]
- 00b82154 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b82198 ["INT_ADD", "register:40f0:8", ["const:b82198:8", "const:4:8"]]
+ 00b82198 ["CALL", null, ["callee:00bdb430:8"]]
- 00b82154 bytes a3640194
+ 00b82198 bytes a6640194
- 00b82198 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 00b82198 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b821dc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 00b821dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b82198 bytes 21f846f9
+ 00b821dc bytes 212047f9
- 00b8219c ["INT_ADD", "register:40f0:8", ["const:b8219c:8", "const:4:8"]]
- 00b8219c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b821e0 ["INT_ADD", "register:40f0:8", ["const:b821e0:8", "const:4:8"]]
+ 00b821e0 ["CALL", null, ["callee:00bdb430:8"]]
- 00b8219c bytes 91640194
+ 00b821e0 bytes 94640194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a891c8b6f5dcf9917ba1aa920da5e363"></a>

### [`00b82290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82290.md) → [`00b822d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b822d4.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEe

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b82328",
      "incomplete_value": true,
      "site": "00b8232c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b822e4",
      "incomplete_value": true,
      "site": "00b822e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
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
      "definition_site": "00b82370",
      "incomplete_value": true,
      "site": "00b82374",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b8232c",
      "incomplete_value": true,
      "site": "00b82330",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b82328",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b82328",
      "PARAM",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b82370",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b82328",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00b82328",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b82370",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b822e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82290.md#insn-00b822e8) · [`00b8232c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82290.md#insn-00b8232c) · [`00b82330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82290.md#insn-00b82330)
- 新版 [`00b8232c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b822d4.md#insn-00b8232c) · [`00b82370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b822d4.md#insn-00b82370) · [`00b82374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b822d4.md#insn-00b82374)

~~~diff
- 00b822e8 ["INT_ADD", "register:40f0:8", ["const:b822e8:8", "const:4:8"]]
- 00b822e8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8232c ["INT_ADD", "register:40f0:8", ["const:b8232c:8", "const:4:8"]]
+ 00b8232c ["CALL", null, ["callee:00bdb430:8"]]
- 00b822e8 bytes 3e640194
+ 00b8232c bytes 41640194
- 00b8232c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 00b8232c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b82370 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 00b82370 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8232c bytes 21f846f9
+ 00b82370 bytes 212047f9
- 00b82330 ["INT_ADD", "register:40f0:8", ["const:b82330:8", "const:4:8"]]
- 00b82330 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b82374 ["INT_ADD", "register:40f0:8", ["const:b82374:8", "const:4:8"]]
+ 00b82374 ["CALL", null, ["callee:00bdb430:8"]]
- 00b82330 bytes 2c640194
+ 00b82374 bytes 2f640194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7472b9d3d96dce82dd7ec79a6ace6dcf"></a>

### [`00b82420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82420.md) → [`00b82464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82464.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPKv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b824b8",
      "incomplete_value": true,
      "site": "00b824bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b82474",
      "incomplete_value": true,
      "site": "00b82478",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
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
      "definition_site": "00b82500",
      "incomplete_value": true,
      "site": "00b82504",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b824bc",
      "incomplete_value": true,
      "site": "00b824c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b824b8",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b824b8",
      "PARAM",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b82500",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b824b8",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00b824b8",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b82500",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82420.md#insn-00b82478) · [`00b824bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82420.md#insn-00b824bc) · [`00b824c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82420.md#insn-00b824c0)
- 新版 [`00b824bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82464.md#insn-00b824bc) · [`00b82500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82464.md#insn-00b82500) · [`00b82504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82464.md#insn-00b82504)

~~~diff
- 00b82478 ["INT_ADD", "register:40f0:8", ["const:b82478:8", "const:4:8"]]
- 00b82478 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b824bc ["INT_ADD", "register:40f0:8", ["const:b824bc:8", "const:4:8"]]
+ 00b824bc ["CALL", null, ["callee:00bdb430:8"]]
- 00b82478 bytes da630194
+ 00b824bc bytes dd630194
- 00b824bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 00b824bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b82500 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 00b82500 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b824bc bytes 21f846f9
+ 00b82500 bytes 212047f9
- 00b824c0 ["INT_ADD", "register:40f0:8", ["const:b824c0:8", "const:4:8"]]
- 00b824c0 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b82504 ["INT_ADD", "register:40f0:8", ["const:b82504:8", "const:4:8"]]
+ 00b82504 ["CALL", null, ["callee:00bdb430:8"]]
- 00b824c0 bytes c8630194
+ 00b82504 bytes cb630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a485aca00b2e56a6057af7c4009fca7f"></a>

### [`00b82930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82930.md) → [`00b82974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82974.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b829a0",
      "incomplete_value": true,
      "site": "00b829a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b8295c",
      "incomplete_value": true,
      "site": "00b8295c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b829a4",
      "incomplete_value": true,
      "site": "00b829a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b82960",
      "incomplete_value": true,
      "site": "00b82960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b829c4",
      "incomplete_value": true,
      "site": "00b829d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b82980",
      "incomplete_value": true,
      "site": "00b8298c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b82990",
      "READ",
      [
        "storage",
        "00c1bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00b829a0",
      "DATA",
      [
        "storage",
        "00c13560",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00b829a4",
      "DATA",
      [
        "storage",
        "00c13538",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00b82990",
      "READ",
      [
        "storage",
        "00c1bcf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b829a0",
      "DATA",
      [
        "storage",
        "00c135b0",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00b829a4",
      "DATA",
      [
        "storage",
        "00c13588",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8294c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82930.md#insn-00b8294c) · [`00b82968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82930.md#insn-00b82968) · [`00b82974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82930.md#insn-00b82974)
- 新版 [`00b82990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82974.md#insn-00b82990) · [`00b829ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82974.md#insn-00b829ac) · [`00b829b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82974.md#insn-00b829b8)

~~~diff
- 00b8294c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ca0:8"]]
- 00b8294c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b82990 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf0:8"]]
+ 00b82990 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8294c bytes 085146f9
+ 00b82990 bytes 087946f9
- 00b82968 ["INT_ADD", "register:40f0:8", ["const:b82968:8", "const:4:8"]]
- 00b82968 ["CALL", null, ["callee:00bdb390:8"]]
+ 00b829ac ["INT_ADD", "register:40f0:8", ["const:b829ac:8", "const:4:8"]]
+ 00b829ac ["CALL", null, ["callee:00bdb390:8"]]
- 00b82968 bytes 76620194
+ 00b829ac bytes 79620194
- 00b82974 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ca8:8"]]
- 00b82974 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b829b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf8:8"]]
+ 00b829b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b82974 bytes 085546f9
+ 00b829b8 bytes 087d46f9
~~~


<a id="compare-9a70f5c1602877d60b63524ab8651289"></a>

### [`00b82e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82e54.md) → [`00b82e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82e98.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1390.md) · 呼出先 1件 [`00bdd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd900.md)
- 新版 呼出元 1件 [`00be13e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13e0.md) · 呼出先 1件 [`00bdd950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd950.md)

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
      "definition_site": "00b82eb8",
      "incomplete_value": true,
      "site": "00b82eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b82e74",
      "incomplete_value": true,
      "site": "00b82e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b82eb0",
      "READ",
      [
        "storage",
        "00c1bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "00b82eb8",
      "DATA",
      [
        "storage",
        "00c13180",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00b82eb0",
      "READ",
      [
        "storage",
        "00c1bd00",
        null,
        "pointer"
      ]
    ],
    [
      "00b82eb8",
      "DATA",
      [
        "storage",
        "00c131d0",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82e54.md#insn-00b82e6c) · [`00b82e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82e54.md#insn-00b82e78)
- 新版 [`00b82eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82e98.md#insn-00b82eb0) · [`00b82ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82e98.md#insn-00b82ebc)

~~~diff
- 00b82e6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb0:8"]]
- 00b82e6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b82eb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d00:8"]]
+ 00b82eb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b82e6c bytes 085946f9
+ 00b82eb0 bytes 088146f9
- 00b82e78 ["INT_ADD", "register:40f0:8", ["const:b82e78:8", "const:4:8"]]
- 00b82e78 ["CALL", null, ["callee:00bdd950:8"]]
+ 00b82ebc ["INT_ADD", "register:40f0:8", ["const:b82ebc:8", "const:4:8"]]
+ 00b82ebc ["CALL", null, ["callee:00bdd950:8"]]
- 00b82e78 bytes a26a0194
+ 00b82ebc bytes a56a0194
~~~


<a id="compare-f3329f876770ff43350fd241e9bb9ae7"></a>

### [`00b832fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b832fc.md) → [`00b83340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83340.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC1EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)

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
      "definition_site": "00b8336c",
      "incomplete_value": true,
      "site": "00b8336c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b83328",
      "incomplete_value": true,
      "site": "00b83328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b83370",
      "incomplete_value": true,
      "site": "00b83370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b8332c",
      "incomplete_value": true,
      "site": "00b8332c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b8335c",
      "READ",
      [
        "storage",
        "00c1bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b8336c",
      "DATA",
      [
        "storage",
        "00c13230",
        null,
        "pointer"
      ]
    ],
    [
      "00b83370",
      "DATA",
      [
        "storage",
        "00c13208",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b8335c",
      "READ",
      [
        "storage",
        "00c1bd08",
        null,
        "pointer"
      ]
    ],
    [
      "00b8336c",
      "DATA",
      [
        "storage",
        "00c13280",
        null,
        "pointer"
      ]
    ],
    [
      "00b83370",
      "DATA",
      [
        "storage",
        "00c13258",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b832fc.md#insn-00b83318) · [`00b83334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b832fc.md#insn-00b83334)
- 新版 [`00b8335c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83340.md#insn-00b8335c) · [`00b83378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83340.md#insn-00b83378)

~~~diff
- 00b83318 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb8:8"]]
- 00b83318 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b8335c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d08:8"]]
+ 00b8335c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b83318 bytes 085d46f9
+ 00b8335c bytes 088546f9
- 00b83334 ["INT_ADD", "register:40f0:8", ["const:b83334:8", "const:4:8"]]
- 00b83334 ["CALL", null, ["callee:00bdb390:8"]]
+ 00b83378 ["INT_ADD", "register:40f0:8", ["const:b83378:8", "const:4:8"]]
+ 00b83378 ["CALL", null, ["callee:00bdb390:8"]]
- 00b83334 bytes 03600194
+ 00b83378 bytes 06600194
~~~


<a id="compare-bca0d06f4e261e48c3c4f455f9a8add8"></a>

### [`00b83468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83468.md) → [`00b834ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b834ac.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6sentryC1ERS3_b

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13a0.md)
- 新版 呼出元 1件 [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be13f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8353c",
      "incomplete_value": true,
      "site": "00b83540",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b834f8",
      "incomplete_value": true,
      "site": "00b834fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b8353c",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b8353c",
      "PARAM",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b8353c",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b8353c",
      "PARAM",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b834fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83468.md#insn-00b834fc) · [`00b834c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83468.md#insn-00b834c8) · [`00b834ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83468.md#insn-00b834ec)
- 新版 [`00b83540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b834ac.md#insn-00b83540) · [`00b8350c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b834ac.md#insn-00b8350c) · [`00b83530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b834ac.md#insn-00b83530)

~~~diff
- 00b834fc ["INT_ADD", "register:40f0:8", ["const:b834fc:8", "const:4:8"]]
- 00b834fc ["CALL", null, ["callee:00bdb430:8"]]
+ 00b83540 ["INT_ADD", "register:40f0:8", ["const:b83540:8", "const:4:8"]]
+ 00b83540 ["CALL", null, ["callee:00bdb430:8"]]
- 00b834fc bytes b95f0194
+ 00b83540 bytes bc5f0194
- 00b834c8 ["INT_ADD", "register:40f0:8", ["const:b834c8:8", "const:4:8"]]
- 00b834c8 ["CALL", null, ["callee:00be13f0:8"]]
+ 00b8350c ["INT_ADD", "register:40f0:8", ["const:b8350c:8", "const:4:8"]]
+ 00b8350c ["CALL", null, ["callee:00be13f0:8"]]
- 00b834c8 bytes b6770194
+ 00b8350c bytes b9770194
- 00b834ec ["INT_ADD", "register:40f0:8", ["const:b834ec:8", "const:4:8"]]
- 00b834ec ["CALL", null, ["callee:00bdb420:8"]]
+ 00b83530 ["INT_ADD", "register:40f0:8", ["const:b83530:8", "const:4:8"]]
+ 00b83530 ["CALL", null, ["callee:00bdb420:8"]]
- 00b834ec bytes b95f0194
+ 00b83530 bytes bc5f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46485e68c29f04f0c18d6fc93ebd1812"></a>

### [`00b83970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83970.md) → [`00b839b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b839b4.md) FUN_00b839b4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83968.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b839ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b839ac.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b83a08",
      "incomplete_value": true,
      "site": "00b83a0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b839c4",
      "incomplete_value": true,
      "site": "00b839c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b83a08",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b83a08",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b83a08",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b83a08",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b839c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83970.md#insn-00b839c8) · [`00b8399c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83970.md#insn-00b8399c) · [`00b839b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83970.md#insn-00b839b8)
- 新版 [`00b83a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b839b4.md#insn-00b83a0c) · [`00b839e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b839b4.md#insn-00b839e0) · [`00b839fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b839b4.md#insn-00b839fc)

~~~diff
- 00b839c8 ["INT_ADD", "register:40f0:8", ["const:b839c8:8", "const:4:8"]]
- 00b839c8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b83a0c ["INT_ADD", "register:40f0:8", ["const:b83a0c:8", "const:4:8"]]
+ 00b83a0c ["CALL", null, ["callee:00bdb430:8"]]
- 00b839c8 bytes 865e0194
+ 00b83a0c bytes 895e0194
- 00b8399c ["INT_ADD", "register:40f0:8", ["const:b8399c:8", "const:4:8"]]
- 00b8399c ["CALL", null, ["callee:00be1420:8"]]
+ 00b839e0 ["INT_ADD", "register:40f0:8", ["const:b839e0:8", "const:4:8"]]
+ 00b839e0 ["CALL", null, ["callee:00be1420:8"]]
- 00b8399c bytes 8d760194
+ 00b839e0 bytes 90760194
- 00b839b8 ["INT_ADD", "register:40f0:8", ["const:b839b8:8", "const:4:8"]]
- 00b839b8 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b839fc ["INT_ADD", "register:40f0:8", ["const:b839fc:8", "const:4:8"]]
+ 00b839fc ["CALL", null, ["callee:00bdb420:8"]]
- 00b839b8 bytes 865e0194
+ 00b839fc bytes 895e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0aa633f97be644b8bb357cee7594edd"></a>

### [`00b83aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83aa8.md) → [`00b83aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83aec.md) FUN_00b83aec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83aa0.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b83ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83ae4.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b83b40",
      "incomplete_value": true,
      "site": "00b83b44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b83afc",
      "incomplete_value": true,
      "site": "00b83b00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b83b40",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b83b40",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b83b40",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b83b40",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83aa8.md#insn-00b83b00) · [`00b83ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83aa8.md#insn-00b83ad4) · [`00b83af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83aa8.md#insn-00b83af0)
- 新版 [`00b83b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83aec.md#insn-00b83b44) · [`00b83b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83aec.md#insn-00b83b18) · [`00b83b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83aec.md#insn-00b83b34)

~~~diff
- 00b83b00 ["INT_ADD", "register:40f0:8", ["const:b83b00:8", "const:4:8"]]
- 00b83b00 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b83b44 ["INT_ADD", "register:40f0:8", ["const:b83b44:8", "const:4:8"]]
+ 00b83b44 ["CALL", null, ["callee:00bdb430:8"]]
- 00b83b00 bytes 385e0194
+ 00b83b44 bytes 3b5e0194
- 00b83ad4 ["INT_ADD", "register:40f0:8", ["const:b83ad4:8", "const:4:8"]]
- 00b83ad4 ["CALL", null, ["callee:00be1420:8"]]
+ 00b83b18 ["INT_ADD", "register:40f0:8", ["const:b83b18:8", "const:4:8"]]
+ 00b83b18 ["CALL", null, ["callee:00be1420:8"]]
- 00b83ad4 bytes 3f760194
+ 00b83b18 bytes 42760194
- 00b83af0 ["INT_ADD", "register:40f0:8", ["const:b83af0:8", "const:4:8"]]
- 00b83af0 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b83b34 ["INT_ADD", "register:40f0:8", ["const:b83b34:8", "const:4:8"]]
+ 00b83b34 ["CALL", null, ["callee:00bdb420:8"]]
- 00b83af0 bytes 385e0194
+ 00b83b34 bytes 3b5e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-733195e3cb5cad988fadf8b86d5281ea"></a>

### [`00b83c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83c20.md) → [`00b83c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83c64.md) FUN_00b83c64

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83c18.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b83c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83c5c.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b83cb8",
      "incomplete_value": true,
      "site": "00b83cbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b83c74",
      "incomplete_value": true,
      "site": "00b83c78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b83cb8",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b83cb8",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b83cb8",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b83cb8",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83c20.md#insn-00b83c78) · [`00b83c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83c20.md#insn-00b83c4c) · [`00b83c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83c20.md#insn-00b83c68)
- 新版 [`00b83cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83c64.md#insn-00b83cbc) · [`00b83c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83c64.md#insn-00b83c90) · [`00b83cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83c64.md#insn-00b83cac)

~~~diff
- 00b83c78 ["INT_ADD", "register:40f0:8", ["const:b83c78:8", "const:4:8"]]
- 00b83c78 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b83cbc ["INT_ADD", "register:40f0:8", ["const:b83cbc:8", "const:4:8"]]
+ 00b83cbc ["CALL", null, ["callee:00bdb430:8"]]
- 00b83c78 bytes da5d0194
+ 00b83cbc bytes dd5d0194
- 00b83c4c ["INT_ADD", "register:40f0:8", ["const:b83c4c:8", "const:4:8"]]
- 00b83c4c ["CALL", null, ["callee:00be1420:8"]]
+ 00b83c90 ["INT_ADD", "register:40f0:8", ["const:b83c90:8", "const:4:8"]]
+ 00b83c90 ["CALL", null, ["callee:00be1420:8"]]
- 00b83c4c bytes e1750194
+ 00b83c90 bytes e4750194
- 00b83c68 ["INT_ADD", "register:40f0:8", ["const:b83c68:8", "const:4:8"]]
- 00b83c68 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b83cac ["INT_ADD", "register:40f0:8", ["const:b83cac:8", "const:4:8"]]
+ 00b83cac ["CALL", null, ["callee:00bdb420:8"]]
- 00b83c68 bytes da5d0194
+ 00b83cac bytes dd5d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae3060d6aa2da4c4605c1df4a471c719"></a>

### [`00b83d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83d58.md) → [`00b83d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83d9c.md) FUN_00b83d9c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83d50.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b83d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83d94.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b83df0",
      "incomplete_value": true,
      "site": "00b83df4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b83dac",
      "incomplete_value": true,
      "site": "00b83db0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b83df0",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b83df0",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b83df0",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b83df0",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83d58.md#insn-00b83db0) · [`00b83d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83d58.md#insn-00b83d84) · [`00b83da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83d58.md#insn-00b83da0)
- 新版 [`00b83df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83d9c.md#insn-00b83df4) · [`00b83dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83d9c.md#insn-00b83dc8) · [`00b83de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83d9c.md#insn-00b83de4)

~~~diff
- 00b83db0 ["INT_ADD", "register:40f0:8", ["const:b83db0:8", "const:4:8"]]
- 00b83db0 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b83df4 ["INT_ADD", "register:40f0:8", ["const:b83df4:8", "const:4:8"]]
+ 00b83df4 ["CALL", null, ["callee:00bdb430:8"]]
- 00b83db0 bytes 8c5d0194
+ 00b83df4 bytes 8f5d0194
- 00b83d84 ["INT_ADD", "register:40f0:8", ["const:b83d84:8", "const:4:8"]]
- 00b83d84 ["CALL", null, ["callee:00be1420:8"]]
+ 00b83dc8 ["INT_ADD", "register:40f0:8", ["const:b83dc8:8", "const:4:8"]]
+ 00b83dc8 ["CALL", null, ["callee:00be1420:8"]]
- 00b83d84 bytes 93750194
+ 00b83dc8 bytes 96750194
- 00b83da0 ["INT_ADD", "register:40f0:8", ["const:b83da0:8", "const:4:8"]]
- 00b83da0 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b83de4 ["INT_ADD", "register:40f0:8", ["const:b83de4:8", "const:4:8"]]
+ 00b83de4 ["CALL", null, ["callee:00bdb420:8"]]
- 00b83da0 bytes 8c5d0194
+ 00b83de4 bytes 8f5d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19a051603d05079e606b091dbdc86e04"></a>

### [`00b83ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83ed4.md) → [`00b83f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83f18.md) FUN_00b83f18

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83ecc.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b83f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83f10.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b83f6c",
      "incomplete_value": true,
      "site": "00b83f70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b83f28",
      "incomplete_value": true,
      "site": "00b83f2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b83f6c",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b83f6c",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b83f6c",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b83f6c",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83ed4.md#insn-00b83f2c) · [`00b83f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83ed4.md#insn-00b83f00) · [`00b83f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b83/00b83ed4.md#insn-00b83f1c)
- 新版 [`00b83f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83f18.md#insn-00b83f70) · [`00b83f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83f18.md#insn-00b83f44) · [`00b83f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83f18.md#insn-00b83f60)

~~~diff
- 00b83f2c ["INT_ADD", "register:40f0:8", ["const:b83f2c:8", "const:4:8"]]
- 00b83f2c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b83f70 ["INT_ADD", "register:40f0:8", ["const:b83f70:8", "const:4:8"]]
+ 00b83f70 ["CALL", null, ["callee:00bdb430:8"]]
- 00b83f2c bytes 2d5d0194
+ 00b83f70 bytes 305d0194
- 00b83f00 ["INT_ADD", "register:40f0:8", ["const:b83f00:8", "const:4:8"]]
- 00b83f00 ["CALL", null, ["callee:00be1420:8"]]
+ 00b83f44 ["INT_ADD", "register:40f0:8", ["const:b83f44:8", "const:4:8"]]
+ 00b83f44 ["CALL", null, ["callee:00be1420:8"]]
- 00b83f00 bytes 34750194
+ 00b83f44 bytes 37750194
- 00b83f1c ["INT_ADD", "register:40f0:8", ["const:b83f1c:8", "const:4:8"]]
- 00b83f1c ["CALL", null, ["callee:00bdb420:8"]]
+ 00b83f60 ["INT_ADD", "register:40f0:8", ["const:b83f60:8", "const:4:8"]]
+ 00b83f60 ["CALL", null, ["callee:00bdb420:8"]]
- 00b83f1c bytes 2d5d0194
+ 00b83f60 bytes 305d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d60f6dcd98cdcb152f816e77943548e8"></a>

### [`00b8400c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8400c.md) → [`00b84050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84050.md) FUN_00b84050

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b84004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84004.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b84048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84048.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b840a4",
      "incomplete_value": true,
      "site": "00b840a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84060",
      "incomplete_value": true,
      "site": "00b84064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b840a4",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b840a4",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b840a4",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b840a4",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8400c.md#insn-00b84064) · [`00b84038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8400c.md#insn-00b84038) · [`00b84054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8400c.md#insn-00b84054)
- 新版 [`00b840a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84050.md#insn-00b840a8) · [`00b8407c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84050.md#insn-00b8407c) · [`00b84098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84050.md#insn-00b84098)

~~~diff
- 00b84064 ["INT_ADD", "register:40f0:8", ["const:b84064:8", "const:4:8"]]
- 00b84064 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b840a8 ["INT_ADD", "register:40f0:8", ["const:b840a8:8", "const:4:8"]]
+ 00b840a8 ["CALL", null, ["callee:00bdb430:8"]]
- 00b84064 bytes df5c0194
+ 00b840a8 bytes e25c0194
- 00b84038 ["INT_ADD", "register:40f0:8", ["const:b84038:8", "const:4:8"]]
- 00b84038 ["CALL", null, ["callee:00be1420:8"]]
+ 00b8407c ["INT_ADD", "register:40f0:8", ["const:b8407c:8", "const:4:8"]]
+ 00b8407c ["CALL", null, ["callee:00be1420:8"]]
- 00b84038 bytes e6740194
+ 00b8407c bytes e9740194
- 00b84054 ["INT_ADD", "register:40f0:8", ["const:b84054:8", "const:4:8"]]
- 00b84054 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b84098 ["INT_ADD", "register:40f0:8", ["const:b84098:8", "const:4:8"]]
+ 00b84098 ["CALL", null, ["callee:00bdb420:8"]]
- 00b84054 bytes df5c0194
+ 00b84098 bytes e25c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f1dff5784b298f73eefd036e65a3bf4"></a>

### [`00b84144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84144.md) → [`00b84188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84188.md) FUN_00b84188

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8413c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8413c.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b84180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84180.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b841dc",
      "incomplete_value": true,
      "site": "00b841e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84198",
      "incomplete_value": true,
      "site": "00b8419c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b841dc",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b841dc",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b841dc",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b841dc",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8419c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84144.md#insn-00b8419c) · [`00b84170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84144.md#insn-00b84170) · [`00b8418c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84144.md#insn-00b8418c)
- 新版 [`00b841e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84188.md#insn-00b841e0) · [`00b841b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84188.md#insn-00b841b4) · [`00b841d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84188.md#insn-00b841d0)

~~~diff
- 00b8419c ["INT_ADD", "register:40f0:8", ["const:b8419c:8", "const:4:8"]]
- 00b8419c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b841e0 ["INT_ADD", "register:40f0:8", ["const:b841e0:8", "const:4:8"]]
+ 00b841e0 ["CALL", null, ["callee:00bdb430:8"]]
- 00b8419c bytes 915c0194
+ 00b841e0 bytes 945c0194
- 00b84170 ["INT_ADD", "register:40f0:8", ["const:b84170:8", "const:4:8"]]
- 00b84170 ["CALL", null, ["callee:00be1420:8"]]
+ 00b841b4 ["INT_ADD", "register:40f0:8", ["const:b841b4:8", "const:4:8"]]
+ 00b841b4 ["CALL", null, ["callee:00be1420:8"]]
- 00b84170 bytes 98740194
+ 00b841b4 bytes 9b740194
- 00b8418c ["INT_ADD", "register:40f0:8", ["const:b8418c:8", "const:4:8"]]
- 00b8418c ["CALL", null, ["callee:00bdb420:8"]]
+ 00b841d0 ["INT_ADD", "register:40f0:8", ["const:b841d0:8", "const:4:8"]]
+ 00b841d0 ["CALL", null, ["callee:00bdb420:8"]]
- 00b8418c bytes 915c0194
+ 00b841d0 bytes 945c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3753070c337b92fc8aff4942563657e9"></a>

### [`00b8427c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8427c.md) → [`00b842c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b842c0.md) FUN_00b842c0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b84274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84274.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b842b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b842b8.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b84314",
      "incomplete_value": true,
      "site": "00b84318",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b842d0",
      "incomplete_value": true,
      "site": "00b842d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b84314",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b84314",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84314",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b84314",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b842d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8427c.md#insn-00b842d4) · [`00b842a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8427c.md#insn-00b842a8) · [`00b842c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8427c.md#insn-00b842c4)
- 新版 [`00b84318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b842c0.md#insn-00b84318) · [`00b842ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b842c0.md#insn-00b842ec) · [`00b84308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b842c0.md#insn-00b84308)

~~~diff
- 00b842d4 ["INT_ADD", "register:40f0:8", ["const:b842d4:8", "const:4:8"]]
- 00b842d4 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b84318 ["INT_ADD", "register:40f0:8", ["const:b84318:8", "const:4:8"]]
+ 00b84318 ["CALL", null, ["callee:00bdb430:8"]]
- 00b842d4 bytes 435c0194
+ 00b84318 bytes 465c0194
- 00b842a8 ["INT_ADD", "register:40f0:8", ["const:b842a8:8", "const:4:8"]]
- 00b842a8 ["CALL", null, ["callee:00be1420:8"]]
+ 00b842ec ["INT_ADD", "register:40f0:8", ["const:b842ec:8", "const:4:8"]]
+ 00b842ec ["CALL", null, ["callee:00be1420:8"]]
- 00b842a8 bytes 4a740194
+ 00b842ec bytes 4d740194
- 00b842c4 ["INT_ADD", "register:40f0:8", ["const:b842c4:8", "const:4:8"]]
- 00b842c4 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b84308 ["INT_ADD", "register:40f0:8", ["const:b84308:8", "const:4:8"]]
+ 00b84308 ["CALL", null, ["callee:00bdb420:8"]]
- 00b842c4 bytes 435c0194
+ 00b84308 bytes 465c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feaba67f01167a69ff4a28d514a0ba16"></a>

### [`00b843b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b843b4.md) → [`00b843f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b843f8.md) FUN_00b843f8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b843ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b843ac.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b843f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b843f0.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b8444c",
      "incomplete_value": true,
      "site": "00b84450",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84408",
      "incomplete_value": true,
      "site": "00b8440c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b8444c",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b8444c",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b8444c",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b8444c",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8440c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b843b4.md#insn-00b8440c) · [`00b843e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b843b4.md#insn-00b843e0) · [`00b843fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b843b4.md#insn-00b843fc)
- 新版 [`00b84450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b843f8.md#insn-00b84450) · [`00b84424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b843f8.md#insn-00b84424) · [`00b84440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b843f8.md#insn-00b84440)

~~~diff
- 00b8440c ["INT_ADD", "register:40f0:8", ["const:b8440c:8", "const:4:8"]]
- 00b8440c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b84450 ["INT_ADD", "register:40f0:8", ["const:b84450:8", "const:4:8"]]
+ 00b84450 ["CALL", null, ["callee:00bdb430:8"]]
- 00b8440c bytes f55b0194
+ 00b84450 bytes f85b0194
- 00b843e0 ["INT_ADD", "register:40f0:8", ["const:b843e0:8", "const:4:8"]]
- 00b843e0 ["CALL", null, ["callee:00be1420:8"]]
+ 00b84424 ["INT_ADD", "register:40f0:8", ["const:b84424:8", "const:4:8"]]
+ 00b84424 ["CALL", null, ["callee:00be1420:8"]]
- 00b843e0 bytes fc730194
+ 00b84424 bytes ff730194
- 00b843fc ["INT_ADD", "register:40f0:8", ["const:b843fc:8", "const:4:8"]]
- 00b843fc ["CALL", null, ["callee:00bdb420:8"]]
+ 00b84440 ["INT_ADD", "register:40f0:8", ["const:b84440:8", "const:4:8"]]
+ 00b84440 ["CALL", null, ["callee:00bdb420:8"]]
- 00b843fc bytes f55b0194
+ 00b84440 bytes f85b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a43cfce65c9e2d8b14aa6b98f0ac833"></a>

### [`00b844ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b844ec.md) → [`00b84530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84530.md) FUN_00b84530

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b844e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b844e4.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b84528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84528.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b84584",
      "incomplete_value": true,
      "site": "00b84588",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84540",
      "incomplete_value": true,
      "site": "00b84544",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b84584",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b84584",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84584",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b84584",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b844ec.md#insn-00b84544) · [`00b84518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b844ec.md#insn-00b84518) · [`00b84534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b844ec.md#insn-00b84534)
- 新版 [`00b84588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84530.md#insn-00b84588) · [`00b8455c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84530.md#insn-00b8455c) · [`00b84578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84530.md#insn-00b84578)

~~~diff
- 00b84544 ["INT_ADD", "register:40f0:8", ["const:b84544:8", "const:4:8"]]
- 00b84544 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b84588 ["INT_ADD", "register:40f0:8", ["const:b84588:8", "const:4:8"]]
+ 00b84588 ["CALL", null, ["callee:00bdb430:8"]]
- 00b84544 bytes a75b0194
+ 00b84588 bytes aa5b0194
- 00b84518 ["INT_ADD", "register:40f0:8", ["const:b84518:8", "const:4:8"]]
- 00b84518 ["CALL", null, ["callee:00be1420:8"]]
+ 00b8455c ["INT_ADD", "register:40f0:8", ["const:b8455c:8", "const:4:8"]]
+ 00b8455c ["CALL", null, ["callee:00be1420:8"]]
- 00b84518 bytes ae730194
+ 00b8455c bytes b1730194
- 00b84534 ["INT_ADD", "register:40f0:8", ["const:b84534:8", "const:4:8"]]
- 00b84534 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b84578 ["INT_ADD", "register:40f0:8", ["const:b84578:8", "const:4:8"]]
+ 00b84578 ["CALL", null, ["callee:00bdb420:8"]]
- 00b84534 bytes a75b0194
+ 00b84578 bytes aa5b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ce56019945ede707a040cee364ec464"></a>

### [`00b84624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84624.md) → [`00b84668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84668.md) FUN_00b84668

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8461c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8461c.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b84660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84660.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b846bc",
      "incomplete_value": true,
      "site": "00b846c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84678",
      "incomplete_value": true,
      "site": "00b8467c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b846bc",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b846bc",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b846bc",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b846bc",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8467c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84624.md#insn-00b8467c) · [`00b84650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84624.md#insn-00b84650) · [`00b8466c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84624.md#insn-00b8466c)
- 新版 [`00b846c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84668.md#insn-00b846c0) · [`00b84694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84668.md#insn-00b84694) · [`00b846b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84668.md#insn-00b846b0)

~~~diff
- 00b8467c ["INT_ADD", "register:40f0:8", ["const:b8467c:8", "const:4:8"]]
- 00b8467c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b846c0 ["INT_ADD", "register:40f0:8", ["const:b846c0:8", "const:4:8"]]
+ 00b846c0 ["CALL", null, ["callee:00bdb430:8"]]
- 00b8467c bytes 595b0194
+ 00b846c0 bytes 5c5b0194
- 00b84650 ["INT_ADD", "register:40f0:8", ["const:b84650:8", "const:4:8"]]
- 00b84650 ["CALL", null, ["callee:00be1420:8"]]
+ 00b84694 ["INT_ADD", "register:40f0:8", ["const:b84694:8", "const:4:8"]]
+ 00b84694 ["CALL", null, ["callee:00be1420:8"]]
- 00b84650 bytes 60730194
+ 00b84694 bytes 63730194
- 00b8466c ["INT_ADD", "register:40f0:8", ["const:b8466c:8", "const:4:8"]]
- 00b8466c ["CALL", null, ["callee:00bdb420:8"]]
+ 00b846b0 ["INT_ADD", "register:40f0:8", ["const:b846b0:8", "const:4:8"]]
+ 00b846b0 ["CALL", null, ["callee:00bdb420:8"]]
- 00b8466c bytes 595b0194
+ 00b846b0 bytes 5c5b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3912bf427d7cd246ff4aed8810df6c39"></a>

### [`00b8475c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8475c.md) → [`00b847a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b847a0.md) FUN_00b847a0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b84754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84754.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b84798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84798.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b847f4",
      "incomplete_value": true,
      "site": "00b847f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b847b0",
      "incomplete_value": true,
      "site": "00b847b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b847f4",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b847f4",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b847f4",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b847f4",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b847b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8475c.md#insn-00b847b4) · [`00b84788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8475c.md#insn-00b84788) · [`00b847a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8475c.md#insn-00b847a4)
- 新版 [`00b847f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b847a0.md#insn-00b847f8) · [`00b847cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b847a0.md#insn-00b847cc) · [`00b847e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b847a0.md#insn-00b847e8)

~~~diff
- 00b847b4 ["INT_ADD", "register:40f0:8", ["const:b847b4:8", "const:4:8"]]
- 00b847b4 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b847f8 ["INT_ADD", "register:40f0:8", ["const:b847f8:8", "const:4:8"]]
+ 00b847f8 ["CALL", null, ["callee:00bdb430:8"]]
- 00b847b4 bytes 0b5b0194
+ 00b847f8 bytes 0e5b0194
- 00b84788 ["INT_ADD", "register:40f0:8", ["const:b84788:8", "const:4:8"]]
- 00b84788 ["CALL", null, ["callee:00be1420:8"]]
+ 00b847cc ["INT_ADD", "register:40f0:8", ["const:b847cc:8", "const:4:8"]]
+ 00b847cc ["CALL", null, ["callee:00be1420:8"]]
- 00b84788 bytes 12730194
+ 00b847cc bytes 15730194
- 00b847a4 ["INT_ADD", "register:40f0:8", ["const:b847a4:8", "const:4:8"]]
- 00b847a4 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b847e8 ["INT_ADD", "register:40f0:8", ["const:b847e8:8", "const:4:8"]]
+ 00b847e8 ["CALL", null, ["callee:00bdb420:8"]]
- 00b847a4 bytes 0b5b0194
+ 00b847e8 bytes 0e5b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9338cfc2fd5d845ec3631c59f045ca62"></a>

### [`00b84894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84894.md) → [`00b848d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b848d8.md) FUN_00b848d8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8488c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b8488c.md) · 呼出先 5件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)
- 新版 呼出元 1件 [`00b848d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b848d0.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)

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
      "definition_site": "00b8492c",
      "incomplete_value": true,
      "site": "00b84930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b848e8",
      "incomplete_value": true,
      "site": "00b848ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
      "00b8492c",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b8492c",
      "PARAM",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b8492c",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00b8492c",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b848ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84894.md#insn-00b848ec) · [`00b848c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84894.md#insn-00b848c0) · [`00b848dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84894.md#insn-00b848dc)
- 新版 [`00b84930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b848d8.md#insn-00b84930) · [`00b84904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b848d8.md#insn-00b84904) · [`00b84920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b848d8.md#insn-00b84920)

~~~diff
- 00b848ec ["INT_ADD", "register:40f0:8", ["const:b848ec:8", "const:4:8"]]
- 00b848ec ["CALL", null, ["callee:00bdb430:8"]]
+ 00b84930 ["INT_ADD", "register:40f0:8", ["const:b84930:8", "const:4:8"]]
+ 00b84930 ["CALL", null, ["callee:00bdb430:8"]]
- 00b848ec bytes bd5a0194
+ 00b84930 bytes c05a0194
- 00b848c0 ["INT_ADD", "register:40f0:8", ["const:b848c0:8", "const:4:8"]]
- 00b848c0 ["CALL", null, ["callee:00be1420:8"]]
+ 00b84904 ["INT_ADD", "register:40f0:8", ["const:b84904:8", "const:4:8"]]
+ 00b84904 ["CALL", null, ["callee:00be1420:8"]]
- 00b848c0 bytes c4720194
+ 00b84904 bytes c7720194
- 00b848dc ["INT_ADD", "register:40f0:8", ["const:b848dc:8", "const:4:8"]]
- 00b848dc ["CALL", null, ["callee:00bdb420:8"]]
+ 00b84920 ["INT_ADD", "register:40f0:8", ["const:b84920:8", "const:4:8"]]
+ 00b84920 ["CALL", null, ["callee:00bdb420:8"]]
- 00b848dc bytes bd5a0194
+ 00b84920 bytes c05a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4519a96af76c16be744ab4fd49155b5c"></a>

### [`00b84b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84b18.md) → [`00b84b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b5c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEPwl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be13f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1440.md)

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
      "definition_site": "00b84b9c",
      "incomplete_value": true,
      "site": "00b84ba0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84b58",
      "incomplete_value": true,
      "site": "00b84b5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b84b9c",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b84b9c",
      "PARAM",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84b9c",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b84b9c",
      "PARAM",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84b18.md#insn-00b84b5c) · [`00b84b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84b18.md#insn-00b84b4c) · [`00b84b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84b18.md#insn-00b84b58)
- 新版 [`00b84ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b5c.md#insn-00b84ba0) · [`00b84b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b5c.md#insn-00b84b90) · [`00b84b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b5c.md#insn-00b84b9c)

~~~diff
- 00b84b5c ["INT_ADD", "register:40f0:8", ["const:b84b5c:8", "const:4:8"]]
- 00b84b5c ["CALL", null, ["callee:00bdb430:8"]]
+ 00b84ba0 ["INT_ADD", "register:40f0:8", ["const:b84ba0:8", "const:4:8"]]
+ 00b84ba0 ["CALL", null, ["callee:00bdb430:8"]]
- 00b84b5c bytes 215a0194
+ 00b84ba0 bytes 245a0194
- 00b84b4c ["INT_ADD", "register:40f0:8", ["const:b84b4c:8", "const:4:8"]]
- 00b84b4c ["CALL", null, ["callee:00bdb420:8"]]
+ 00b84b90 ["INT_ADD", "register:40f0:8", ["const:b84b90:8", "const:4:8"]]
+ 00b84b90 ["CALL", null, ["callee:00bdb420:8"]]
- 00b84b4c bytes 215a0194
+ 00b84b90 bytes 245a0194
- 00b84b58 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b84b58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b84b9c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b84b9c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b84b58 bytes 216046f9
+ 00b84b9c bytes 218846f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-101cbdbce167d138da0a2a4515e117a6"></a>

### [`00b84d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84d8c.md) → [`00b84dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84dd0.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be1400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1450.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b84e08",
      "incomplete_value": true,
      "site": "00b84e0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84dc4",
      "incomplete_value": true,
      "site": "00b84dc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b84e08",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b84e08",
      "PARAM",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b84e08",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b84e08",
      "PARAM",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84d8c.md#insn-00b84dc8) · [`00b84db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84d8c.md#insn-00b84db8) · [`00b84dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84d8c.md#insn-00b84dc4)
- 新版 [`00b84e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84dd0.md#insn-00b84e0c) · [`00b84dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84dd0.md#insn-00b84dfc) · [`00b84e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84dd0.md#insn-00b84e08)

~~~diff
- 00b84dc8 ["INT_ADD", "register:40f0:8", ["const:b84dc8:8", "const:4:8"]]
- 00b84dc8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b84e0c ["INT_ADD", "register:40f0:8", ["const:b84e0c:8", "const:4:8"]]
+ 00b84e0c ["CALL", null, ["callee:00bdb430:8"]]
- 00b84dc8 bytes 86590194
+ 00b84e0c bytes 89590194
- 00b84db8 ["INT_ADD", "register:40f0:8", ["const:b84db8:8", "const:4:8"]]
- 00b84db8 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b84dfc ["INT_ADD", "register:40f0:8", ["const:b84dfc:8", "const:4:8"]]
+ 00b84dfc ["CALL", null, ["callee:00bdb420:8"]]
- 00b84db8 bytes 86590194
+ 00b84dfc bytes 89590194
- 00b84dc4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b84dc4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b84e08 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b84e08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b84dc4 bytes 216046f9
+ 00b84e08 bytes 218846f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1778284200c7c05446e1b00a9f01580c"></a>

### [`00b84f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84f84.md) → [`00b84fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84fc8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7getlineEPwl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be1410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1410.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1460.md)

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
      "definition_site": "00b85008",
      "incomplete_value": true,
      "site": "00b8500c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84fc4",
      "incomplete_value": true,
      "site": "00b84fc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b85008",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b85008",
      "PARAM",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b85008",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00b85008",
      "PARAM",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84f84.md#insn-00b84fc8) · [`00b84fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84f84.md#insn-00b84fb8) · [`00b84fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b84/00b84f84.md#insn-00b84fc4)
- 新版 [`00b8500c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84fc8.md#insn-00b8500c) · [`00b84ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84fc8.md#insn-00b84ffc) · [`00b85008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84fc8.md#insn-00b85008)

~~~diff
- 00b84fc8 ["INT_ADD", "register:40f0:8", ["const:b84fc8:8", "const:4:8"]]
- 00b84fc8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8500c ["INT_ADD", "register:40f0:8", ["const:b8500c:8", "const:4:8"]]
+ 00b8500c ["CALL", null, ["callee:00bdb430:8"]]
- 00b84fc8 bytes 06590194
+ 00b8500c bytes 09590194
- 00b84fb8 ["INT_ADD", "register:40f0:8", ["const:b84fb8:8", "const:4:8"]]
- 00b84fb8 ["CALL", null, ["callee:00bdb420:8"]]
+ 00b84ffc ["INT_ADD", "register:40f0:8", ["const:b84ffc:8", "const:4:8"]]
+ 00b84ffc ["CALL", null, ["callee:00bdb420:8"]]
- 00b84fb8 bytes 06590194
+ 00b84ffc bytes 09590194
- 00b84fc4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b84fc4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b85008 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b85008 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b84fc4 bytes 216046f9
+ 00b85008 bytes 218846f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fb0035f7ad83d5b76af9a7202598bf5"></a>

### [`00b85e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85e3c.md) → [`00b85e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85e80.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEEC1EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)

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
      "definition_site": "00b85eac",
      "incomplete_value": true,
      "site": "00b85eac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b85e68",
      "incomplete_value": true,
      "site": "00b85e68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b85ea8",
      "incomplete_value": true,
      "site": "00b85eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b85e64",
      "incomplete_value": true,
      "site": "00b85e6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b85e9c",
      "READ",
      [
        "storage",
        "00c1bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00b85eac",
      "DATA",
      [
        "storage",
        "00c13290",
        null,
        "pointer"
      ]
    ],
    [
      "00b85eb0",
      "DATA",
      [
        "storage",
        "00c13268",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b85e9c",
      "READ",
      [
        "storage",
        "00c1bd20",
        null,
        "pointer"
      ]
    ],
    [
      "00b85eac",
      "DATA",
      [
        "storage",
        "00c132e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b85eb0",
      "DATA",
      [
        "storage",
        "00c132b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b85e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85e3c.md#insn-00b85e58) · [`00b85e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85e3c.md#insn-00b85e74)
- 新版 [`00b85e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85e80.md#insn-00b85e9c) · [`00b85eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85e80.md#insn-00b85eb8)

~~~diff
- 00b85e58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 00b85e58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b85e9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
+ 00b85e9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b85e58 bytes 086946f9
+ 00b85e9c bytes 089146f9
- 00b85e74 ["INT_ADD", "register:40f0:8", ["const:b85e74:8", "const:4:8"]]
- 00b85e74 ["CALL", null, ["callee:00bdb390:8"]]
+ 00b85eb8 ["INT_ADD", "register:40f0:8", ["const:b85eb8:8", "const:4:8"]]
+ 00b85eb8 ["CALL", null, ["callee:00bdb390:8"]]
- 00b85e74 bytes 33550194
+ 00b85eb8 bytes 36550194
~~~


<a id="compare-d26404c486ad8d94faefe3a3b2293e20"></a>

### [`00b86128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86128.md) → [`00b8616c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8616c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b861c0",
      "incomplete_value": true,
      "site": "00b861c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8617c",
      "incomplete_value": true,
      "site": "00b86180",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00b86208",
      "incomplete_value": true,
      "site": "00b8620c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b861c4",
      "incomplete_value": true,
      "site": "00b861c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00b861c0",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00b861c0",
      "PARAM",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86208",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b861c0",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00b861c0",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00b86208",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86128.md#insn-00b86180) · [`00b861c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86128.md#insn-00b861c4) · [`00b861c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b86/00b86128.md#insn-00b861c8)
- 新版 [`00b861c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8616c.md#insn-00b861c4) · [`00b86208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8616c.md#insn-00b86208) · [`00b8620c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8616c.md#insn-00b8620c)

~~~diff
- 00b86180 ["INT_ADD", "register:40f0:8", ["const:b86180:8", "const:4:8"]]
- 00b86180 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b861c4 ["INT_ADD", "register:40f0:8", ["const:b861c4:8", "const:4:8"]]
+ 00b861c4 ["CALL", null, ["callee:00bdb430:8"]]
- 00b86180 bytes 98540194
+ 00b861c4 bytes 9b540194
- 00b861c4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc0:8"]]
- 00b861c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b86208 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d10:8"]]
+ 00b86208 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b861c4 bytes 216046f9
+ 00b86208 bytes 218846f9
- 00b861c8 ["INT_ADD", "register:40f0:8", ["const:b861c8:8", "const:4:8"]]
- 00b861c8 ["CALL", null, ["callee:00bdb430:8"]]
+ 00b8620c ["INT_ADD", "register:40f0:8", ["const:b8620c:8", "const:4:8"]]
+ 00b8620c ["CALL", null, ["callee:00bdb430:8"]]
- 00b861c8 bytes 86540194
+ 00b8620c bytes 89540194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

