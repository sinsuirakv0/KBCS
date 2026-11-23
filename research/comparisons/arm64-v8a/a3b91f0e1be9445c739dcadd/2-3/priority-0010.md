# v15.7.4 → v16.0.0 · 最優先の変更候補 (10)

[一覧の目次](README.md)

<a id="compare-c37ee5c0dc3c7ab6e350ae541a494c22"></a>

### [`004cadbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cadbc.md) → [`004edc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edc54.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7e0.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`005229d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/005229d4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c59230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59230.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`0054586c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/0054586c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004edcc4",
      "incomplete_value": false,
      "site": "004edcc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cae2c",
      "incomplete_value": false,
      "site": "004cae2c",
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
            "const:560:8"
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
      "004edcc4",
      "DATA",
      [
        "storage",
        "00bed560",
        null,
        "undefined *"
      ]
    ],
    [
      "004edd08",
      "READ",
      [
        "storage",
        "00bed588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004edcc4",
      "DATA",
      [
        "storage",
        "00c6a120",
        null,
        "undefined *"
      ]
    ],
    [
      "004edd08",
      "READ",
      [
        "storage",
        "00c6a148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cadbc.md#insn-004cae0c) · [`004cae18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cadbc.md#insn-004cae18) · [`004cae24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cadbc.md#insn-004cae24)
- 新版 `004edca4`（命令位置の公開資料なし） · `004edcb0`（命令位置の公開資料なし） · `004edcbc`（命令位置の公開資料なし）

~~~diff
- 004cae0c ["INT_ADD", "register:40f0:8", ["const:4cae0c:8", "const:4:8"]]
- 004cae0c ["CALL", null, ["callee:0043bae0:8"]]
+ 004edca4 ["INT_ADD", "register:40f0:8", ["const:4edca4:8", "const:4:8"]]
+ 004edca4 ["CALL", null, ["callee:0043bae0:8"]]
- 004cae0c bytes 7538fd97
+ 004edca4 bytes 8f37fd97
- 004cae18 ["INT_ADD", "register:40f0:8", ["const:4cae18:8", "const:4:8"]]
- 004cae18 ["CALL", null, ["callee:00c57a90:8"]]
+ 004edcb0 ["INT_ADD", "register:40f0:8", ["const:4edcb0:8", "const:4:8"]]
+ 004edcb0 ["CALL", null, ["callee:00c57a90:8"]]
- 004cae18 bytes 8a401c94
+ 004edcb0 bytes 78a71d94
- 004cae24 ["COPY", "register:4048:8", ["const:bed000:8"]]
+ 004edcbc ["COPY", "register:4048:8", ["const:c6a000:8"]]
- 004cae24 bytes 093900f0
+ 004edcbc bytes e93b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-212a8b0f59c7cacc91c76c9ee2715aa6"></a>

### [`004caf04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004caf04.md) → [`004edd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edd9c.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7f0.md) · 呼出先 4件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59240.md) · 呼出先 4件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
      "definition_site": "004eddb4",
      "incomplete_value": false,
      "site": "004eddc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004caf1c",
      "incomplete_value": false,
      "site": "004caf2c",
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
            "const:5f0:8"
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
      "004eddc4",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004eddfc",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      "004eddfc",
      "READ",
      [
        "storage",
        "00bed618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004eddc4",
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004eddfc",
      "READ",
      [
        "storage",
        "00c6a1d0",
        null,
        "pointer"
      ]
    ],
    [
      "004eddfc",
      "READ",
      [
        "storage",
        "00c6a1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004caf18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004caf04.md#insn-004caf18) · [`004caf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004caf04.md#insn-004caf1c) · [`004caf3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004caf04.md#insn-004caf3c)
- 新版 `004eddb0`（命令位置の公開資料なし） · `004eddb4`（命令位置の公開資料なし） · `004eddd4`（命令位置の公開資料なし）

~~~diff
- 004caf18 ["COPY", "register:4050:8", ["const:bed000:8"]]
+ 004eddb0 ["COPY", "register:4050:8", ["const:c6a000:8"]]
- 004caf18 bytes 0a3900f0
+ 004eddb0 bytes ea3b00b0
- 004caf1c ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 004caf1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004caf1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004caf1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004eddb4 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 004eddb4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004eddb4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004eddb4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004caf1c bytes 4ac11791
+ 004eddb4 bytes 4ac10691
- 004caf3c ["INT_ADD", "register:40f0:8", ["const:4caf3c:8", "const:4:8"]]
- 004caf3c ["CALL", null, ["callee:004eccd0:8"]]
+ 004eddd4 ["INT_ADD", "register:40f0:8", ["const:4eddd4:8", "const:4:8"]]
+ 004eddd4 ["CALL", null, ["callee:004eccd0:8"]]
- 004caf3c bytes bffbff97
+ 004eddd4 bytes bffbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fda5e7549e03bc4a540a8891b26d7b4"></a>

### [`004cafdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cafdc.md) → [`004ede74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004ede74.md) _ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc800.md) · 呼出先 9件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a9c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59250.md) · 呼出先 9件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004edec0",
      "incomplete_value": false,
      "site": "004edec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cb028",
      "incomplete_value": false,
      "site": "004cb030",
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
            "const:5f0:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004edea8",
      "value": [
        "leaf",
        "ram:c590c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cb010",
      "value": [
        "leaf",
        "ram:bdc670:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004edf34",
      "incomplete_value": true,
      "site": "004edf34",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
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
    "old": {
      "definition_site": "004cb09c",
      "incomplete_value": true,
      "site": "004cb09c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004edea8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc670"
      ]
    ],
    [
      "004edec8",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004edf08",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004edea8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c590c0"
      ]
    ],
    [
      "004edec8",
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004edf08",
      "READ",
      [
        "storage",
        "00c6a1d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cafdc.md#insn-004cb010) · [`004cb09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cafdc.md#insn-004cb09c) · [`004cb004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cafdc.md#insn-004cb004)
- 新版 `004edea8`（命令位置の公開資料なし） · `004edf34`（命令位置の公開資料なし） · `004ede9c`（命令位置の公開資料なし）

~~~diff
- 004cb010 ["INT_ADD", "register:40f0:8", ["const:4cb010:8", "const:4:8"]]
- 004cb010 ["CALL", null, ["ram:bdc670:8"]]
+ 004edea8 ["INT_ADD", "register:40f0:8", ["const:4edea8:8", "const:4:8"]]
+ 004edea8 ["CALL", null, ["ram:c590c0:8"]]
- 004cb010 bytes 98451c94
+ 004edea8 bytes 86ac1d94
- 004cb09c ["COPY", "register:0:8", ["register:4048:8"]]
- 004cb09c ["INT_ADD", "register:40f0:8", ["const:4cb09c:8", "const:4:8"]]
- 004cb09c ["CALLIND", null, ["register:0:8"]]
+ 004edf34 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004edf34 ["INT_ADD", "register:40f0:8", ["const:4edf34:8", "const:4:8"]]
+ 004edf34 ["CALLIND", null, ["register:0:8"]]
- 004cb09c bytes 20013fd6
+ 004edf34 bytes 20013fd6
- 004cb004 ["INT_ADD", "register:40f0:8", ["const:4cb004:8", "const:4:8"]]
- 004cb004 ["CALL", null, ["callee:00c591f0:8"]]
+ 004ede9c ["INT_ADD", "register:40f0:8", ["const:4ede9c:8", "const:4:8"]]
+ 004ede9c ["CALL", null, ["callee:00c591f0:8"]]
- 004cb004 bytes e7451c94
+ 004ede9c bytes d5ac1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9989cb05350d04aa72eae5b152d83ba4"></a>

### [`004cb37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb37c.md) → [`004ee214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee214.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004ee22c",
      "incomplete_value": false,
      "site": "004ee23c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cb394",
      "incomplete_value": false,
      "site": "004cb3a4",
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
            "const:5f0:8"
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
      "004ee23c",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee278",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      "004ee278",
      "READ",
      [
        "storage",
        "00bed618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004ee23c",
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee278",
      "READ",
      [
        "storage",
        "00c6a1d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ee278",
      "READ",
      [
        "storage",
        "00c6a1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb37c.md#insn-004cb390) · [`004cb394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb37c.md#insn-004cb394) · [`004cb3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb37c.md#insn-004cb3b8)
- 新版 `004ee228`（命令位置の公開資料なし） · `004ee22c`（命令位置の公開資料なし） · `004ee250`（命令位置の公開資料なし）

~~~diff
- 004cb390 ["COPY", "register:4048:8", ["const:bed000:8"]]
+ 004ee228 ["COPY", "register:4048:8", ["const:c6a000:8"]]
- 004cb390 bytes 093900d0
+ 004ee228 bytes e93b0090
- 004cb394 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 004cb394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004cb394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004cb394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ee22c ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 004ee22c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ee22c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ee22c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004cb394 bytes 29c11791
+ 004ee22c bytes 29c10691
- 004cb3b8 ["INT_ADD", "register:40f0:8", ["const:4cb3b8:8", "const:4:8"]]
- 004cb3b8 ["CALL", null, ["callee:004eccd0:8"]]
+ 004ee250 ["INT_ADD", "register:40f0:8", ["const:4ee250:8", "const:4:8"]]
+ 004ee250 ["CALL", null, ["callee:004eccd0:8"]]
- 004cb3b8 bytes a0faff97
+ 004ee250 bytes a0faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68b484b15dfd6cdd7e2d3b06dac2ccbc"></a>

### [`004cb45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb45c.md) → [`004ee2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee2f4.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorENS1_8functionIFS7_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md) [`00bdc820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

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
      "site": "004ee414",
      "value": [
        "leaf",
        "ram:c59270:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cb57c",
      "value": [
        "leaf",
        "ram:bdc820:8"
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
      "004ee414",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc820"
      ]
    ]
  ],
  "added": [
    [
      "004ee414",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59270"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb45c.md#insn-004cb57c) · [`004cb488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb45c.md#insn-004cb488) · [`004cb4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb45c.md#insn-004cb4a4)
- 新版 `004ee414`（命令位置の公開資料なし） · `004ee320`（命令位置の公開資料なし） · `004ee33c`（命令位置の公開資料なし）

~~~diff
- 004cb57c ["INT_ADD", "register:40f0:8", ["const:4cb57c:8", "const:4:8"]]
- 004cb57c ["CALL", null, ["ram:bdc820:8"]]
+ 004ee414 ["INT_ADD", "register:40f0:8", ["const:4ee414:8", "const:4:8"]]
+ 004ee414 ["CALL", null, ["ram:c59270:8"]]
- 004cb57c bytes a9441c94
+ 004ee414 bytes 97ab1d94
- 004cb488 ["INT_ADD", "register:40f0:8", ["const:4cb488:8", "const:4:8"]]
- 004cb488 ["CALL", null, ["callee:00c59260:8"]]
+ 004ee320 ["INT_ADD", "register:40f0:8", ["const:4ee320:8", "const:4:8"]]
+ 004ee320 ["CALL", null, ["callee:00c59260:8"]]
- 004cb488 bytes e2441c94
+ 004ee320 bytes d0ab1d94
- 004cb4a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004cb4a4 ["INT_ADD", "register:40f0:8", ["const:4cb4a4:8", "const:4:8"]]
- 004cb4a4 ["CALLIND", null, ["register:0:8"]]
+ 004ee33c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee33c ["INT_ADD", "register:40f0:8", ["const:4ee33c:8", "const:4:8"]]
+ 004ee33c ["CALLIND", null, ["register:0:8"]]
- 004cb4a4 bytes 00013fd6
+ 004ee33c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-475b2680b9e55f873d1a24aef55e3c31"></a>

### [`004cb65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb65c.md) → [`004ee4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee4f4.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522c18.md) [`00522cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522cdc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545ab0.md) [`00545b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545b74.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004ee56c",
      "incomplete_value": false,
      "site": "004ee56c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cb6d4",
      "incomplete_value": false,
      "site": "004cb6d4",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ee62c",
      "value": [
        "leaf",
        "ram:c59270:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cb794",
      "value": [
        "leaf",
        "ram:bdc820:8"
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
      "004ee56c",
      "DATA",
      [
        "storage",
        "00bed670",
        null,
        "pointer"
      ]
    ],
    [
      "004ee5ac",
      "READ",
      [
        "storage",
        "00bed680",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee610",
      "READ",
      [
        "storage",
        "00bed698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004ee56c",
      "DATA",
      [
        "storage",
        "00c6a230",
        null,
        "pointer"
      ]
    ],
    [
      "004ee5ac",
      "READ",
      [
        "storage",
        "00c6a240",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee610",
      "READ",
      [
        "storage",
        "00c6a258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb65c.md#insn-004cb794) · [`004cb68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb65c.md#insn-004cb68c) · [`004cb6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb65c.md#insn-004cb6b4)
- 新版 `004ee62c`（命令位置の公開資料なし） · `004ee524`（命令位置の公開資料なし） · `004ee54c`（命令位置の公開資料なし）

~~~diff
- 004cb794 ["INT_ADD", "register:40f0:8", ["const:4cb794:8", "const:4:8"]]
- 004cb794 ["CALL", null, ["ram:bdc820:8"]]
+ 004ee62c ["INT_ADD", "register:40f0:8", ["const:4ee62c:8", "const:4:8"]]
+ 004ee62c ["CALL", null, ["ram:c59270:8"]]
- 004cb794 bytes 23441c94
+ 004ee62c bytes 11ab1d94
- 004cb68c ["INT_ADD", "register:40f0:8", ["const:4cb68c:8", "const:4:8"]]
- 004cb68c ["CALL", null, ["callee:00c59260:8"]]
+ 004ee524 ["INT_ADD", "register:40f0:8", ["const:4ee524:8", "const:4:8"]]
+ 004ee524 ["CALL", null, ["callee:00c59260:8"]]
- 004cb68c bytes 61441c94
+ 004ee524 bytes 4fab1d94
- 004cb6b4 ["INT_ADD", "register:40f0:8", ["const:4cb6b4:8", "const:4:8"]]
- 004cb6b4 ["CALL", null, ["callee:0043bae0:8"]]
+ 004ee54c ["INT_ADD", "register:40f0:8", ["const:4ee54c:8", "const:4:8"]]
+ 004ee54c ["CALL", null, ["callee:0043bae0:8"]]
- 004cb6b4 bytes 4b36fd97
+ 004ee54c bytes 6535fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f45f55dee4654dbcdc39f788412a580"></a>

### [`004cb868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb868.md) → [`004ee700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee700.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`00522a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a98.md) [`00522a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004ee730",
      "incomplete_value": false,
      "site": "004ee738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cb898",
      "incomplete_value": false,
      "site": "004cb8a0",
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
            "const:5f0:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ee788",
      "value": [
        "leaf",
        "ram:c59270:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cb8f0",
      "value": [
        "leaf",
        "ram:bdc820:8"
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
      "004ee738",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee778",
      "READ",
      [
        "storage",
        "00bed610",
        null,
        "pointer"
      ]
    ],
    [
      "004ee778",
      "READ",
      [
        "storage",
        "00bed618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004ee738",
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee778",
      "READ",
      [
        "storage",
        "00c6a1d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ee778",
      "READ",
      [
        "storage",
        "00c6a1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb868.md#insn-004cb8f0) · [`004cb890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb868.md#insn-004cb890) · [`004cb894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb868.md#insn-004cb894)
- 新版 `004ee788`（命令位置の公開資料なし） · `004ee728`（命令位置の公開資料なし） · `004ee72c`（命令位置の公開資料なし）

~~~diff
- 004cb8f0 ["INT_ADD", "register:40f0:8", ["const:4cb8f0:8", "const:4:8"]]
- 004cb8f0 ["CALL", null, ["ram:bdc820:8"]]
+ 004ee788 ["INT_ADD", "register:40f0:8", ["const:4ee788:8", "const:4:8"]]
+ 004ee788 ["CALL", null, ["ram:c59270:8"]]
- 004cb8f0 bytes cc431c94
+ 004ee788 bytes baaa1d94
- 004cb890 ["INT_ADD", "register:40f0:8", ["const:4cb890:8", "const:4:8"]]
- 004cb890 ["CALL", null, ["callee:00c59260:8"]]
+ 004ee728 ["INT_ADD", "register:40f0:8", ["const:4ee728:8", "const:4:8"]]
+ 004ee728 ["CALL", null, ["callee:00c59260:8"]]
- 004cb890 bytes e0431c94
+ 004ee728 bytes ceaa1d94
- 004cb894 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 004ee72c ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 004cb894 bytes 083900d0
+ 004ee72c bytes e83b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33f3d17031cd9b908669515433052e80"></a>

### [`004cb9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb9bc.md) → [`004ee854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee854.md) _ZNK5Botan12PK_Decryptor7decryptEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3a0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58df0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

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
      "definition_site": "004ee8d8",
      "incomplete_value": false,
      "site": "004ee8e0",
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
            "const:fcc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cba40",
      "incomplete_value": false,
      "site": "004cba48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:a8a:8"
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
      "definition_site": "004ee914",
      "incomplete_value": true,
      "site": "004ee920",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cba7c",
      "incomplete_value": true,
      "site": "004cba88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ee910",
      "incomplete_value": false,
      "site": "004ee920",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004cba78",
      "incomplete_value": false,
      "site": "004cba88",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ee8d8",
      "PARAM",
      [
        "storage",
        "00290a8a",
        null,
        "string"
      ]
    ],
    [
      "004ee910",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004ee914",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ee8d8",
      "PARAM",
      [
        "storage",
        "0029ffcc",
        null,
        "string"
      ]
    ],
    [
      "004ee910",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ee914",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cba48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb9bc.md#insn-004cba48) · [`004cba88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb9bc.md#insn-004cba88) · [`004cb9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb9bc.md#insn-004cb9fc)
- 新版 `004ee8e0`（命令位置の公開資料なし） · `004ee920`（命令位置の公開資料なし） · `004ee894`（命令位置の公開資料なし）

~~~diff
- 004cba48 ["INT_ADD", "register:40f0:8", ["const:4cba48:8", "const:4:8"]]
- 004cba48 ["CALL", null, ["callee:0043dd98:8"]]
+ 004ee8e0 ["INT_ADD", "register:40f0:8", ["const:4ee8e0:8", "const:4:8"]]
+ 004ee8e0 ["CALL", null, ["callee:0043dd98:8"]]
- 004cba48 bytes 143efd97
+ 004ee8e0 bytes 2e3dfd97
- 004cba88 ["INT_ADD", "register:40f0:8", ["const:4cba88:8", "const:4:8"]]
- 004cba88 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ee920 ["INT_ADD", "register:40f0:8", ["const:4ee920:8", "const:4:8"]]
+ 004ee920 ["CALL", null, ["callee:00c57b10:8"]]
- 004cba88 bytes 8e3d1c94
+ 004ee920 bytes 7ca41d94
- 004cb9fc ["COPY", "register:0:8", ["register:4048:8"]]
- 004cb9fc ["INT_ADD", "register:40f0:8", ["const:4cb9fc:8", "const:4:8"]]
- 004cb9fc ["CALLIND", null, ["register:0:8"]]
+ 004ee894 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ee894 ["INT_ADD", "register:40f0:8", ["const:4ee894:8", "const:4:8"]]
+ 004ee894 ["CALLIND", null, ["register:0:8"]]
- 004cb9fc bytes 20013fd6
+ 004ee894 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1b082b638698e85dac6cf89a81d42a6"></a>

### [`004cbae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cbae4.md) → [`004ee97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee97c.md) _ZNK5Botan12PK_Decryptor17decrypt_or_randomEPKhmmRNS_21RandomNumberGeneratorES2_S2_m

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc830.md) · 呼出先 6件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 1件 [`00c59280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59280.md) · 呼出先 6件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004eeb38",
      "incomplete_value": true,
      "site": "004eeb38",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
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
    "old": {
      "definition_site": "004cbca0",
      "incomplete_value": true,
      "site": "004cbca0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eec24",
      "incomplete_value": false,
      "site": "004eec44",
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
            "const:87a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cbd8c",
      "incomplete_value": false,
      "site": "004cbdac",
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
            "const:4f5:8"
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
      "definition_site": "004eec2c",
      "incomplete_value": false,
      "site": "004eec44",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cbd94",
      "incomplete_value": false,
      "site": "004cbdac",
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
            "const:286:8"
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
      "004eeb28",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004eec24",
      "PARAM",
      [
        "storage",
        "0029e4f5",
        null,
        "string"
      ]
    ],
    [
      "004eec2c",
      "PARAM",
      [
        "storage",
        "002a8286",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004eeb28",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004eec24",
      "PARAM",
      [
        "storage",
        "002ae87a",
        null,
        "string"
      ]
    ],
    [
      "004eec2c",
      "PARAM",
      [
        "storage",
        "002b8f28",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cbca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cbae4.md#insn-004cbca0) · [`004cbdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cbae4.md#insn-004cbdac) · [`004cbb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cbae4.md#insn-004cbb3c)
- 新版 `004eeb38`（命令位置の公開資料なし） · `004eec44`（命令位置の公開資料なし） · `004ee9d4`（命令位置の公開資料なし）

~~~diff
- 004cbca0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cbca0 ["INT_ADD", "register:40f0:8", ["const:4cbca0:8", "const:4:8"]]
- 004cbca0 ["CALLIND", null, ["register:0:8"]]
+ 004eeb38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eeb38 ["INT_ADD", "register:40f0:8", ["const:4eeb38:8", "const:4:8"]]
+ 004eeb38 ["CALLIND", null, ["register:0:8"]]
- 004cbca0 bytes 20013fd6
+ 004eeb38 bytes 20013fd6
- 004cbdac ["INT_ADD", "register:40f0:8", ["const:4cbdac:8", "const:4:8"]]
- 004cbdac ["CALL", null, ["callee:00c58250:8"]]
+ 004eec44 ["INT_ADD", "register:40f0:8", ["const:4eec44:8", "const:4:8"]]
+ 004eec44 ["CALL", null, ["callee:00c58250:8"]]
- 004cbdac bytes 953e1c94
+ 004eec44 bytes 83a51d94
- 004cbb3c ["INT_ADD", "register:40f0:8", ["const:4cbb3c:8", "const:4:8"]]
- 004cbb3c ["CALL", null, ["callee:004b34c8:8"]]
+ 004ee9d4 ["INT_ADD", "register:40f0:8", ["const:4ee9d4:8", "const:4:8"]]
+ 004ee9d4 ["CALL", null, ["callee:004b34c8:8"]]
- 004cbb3c bytes bd12ff97
+ 004ee9d4 bytes bd12ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3c55b9ff7bb735be1118b6cb561fec3"></a>

### [`004cbe08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cbe08.md) → [`004eeca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004eeca0.md) _ZN5Botan16PK_Encryptor_EMEC2ERKNS_10Public_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorI

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc380.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`00c58dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58dd0.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eecd8",
      "incomplete_value": true,
      "site": "004eecd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004cbe40",
      "incomplete_value": true,
      "site": "004cbe40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004eed88",
      "incomplete_value": false,
      "site": "004eed94",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cbef0",
      "incomplete_value": false,
      "site": "004cbefc",
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
            "const:8de:8"
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
      "definition_site": "004eedb4",
      "incomplete_value": false,
      "site": "004eedbc",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cbf1c",
      "incomplete_value": false,
      "site": "004cbf24",
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
            "const:a02:8"
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
      "004eecc8",
      "READ",
      [
        "storage",
        "00c1b218",
        null,
        "pointer"
      ]
    ],
    [
      "004eecd8",
      "DATA",
      [
        "storage",
        "00be9fb8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004eed88",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004eecc8",
      "READ",
      [
        "storage",
        "00c9ac08",
        null,
        "pointer"
      ]
    ],
    [
      "004eecd8",
      "DATA",
      [
        "storage",
        "00c66b78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004eed88",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cbefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cbe08.md#insn-004cbefc) · [`004cbf24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cbe08.md#insn-004cbf24) · [`004cbf78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cbe08.md#insn-004cbf78)
- 新版 `004eed94`（命令位置の公開資料なし） · `004eedbc`（命令位置の公開資料なし） · `004eee10`（命令位置の公開資料なし）

~~~diff
- 004cbefc ["INT_ADD", "register:40f0:8", ["const:4cbefc:8", "const:4:8"]]
- 004cbefc ["CALL", null, ["callee:00c57b60:8"]]
+ 004eed94 ["INT_ADD", "register:40f0:8", ["const:4eed94:8", "const:4:8"]]
+ 004eed94 ["CALL", null, ["callee:00c57b60:8"]]
- 004cbefc bytes 853c1c94
+ 004eed94 bytes 73a31d94
- 004cbf24 ["INT_ADD", "register:40f0:8", ["const:4cbf24:8", "const:4:8"]]
- 004cbf24 ["CALL", null, ["callee:00c57b70:8"]]
+ 004eedbc ["INT_ADD", "register:40f0:8", ["const:4eedbc:8", "const:4:8"]]
+ 004eedbc ["CALL", null, ["callee:00c57b70:8"]]
- 004cbf24 bytes 7f3c1c94
+ 004eedbc bytes 6da31d94
- 004cbf78 ["INT_ADD", "register:40f0:8", ["const:4cbf78:8", "const:4:8"]]
- 004cbf78 ["CALL", null, ["callee:00c57b10:8"]]
+ 004eee10 ["INT_ADD", "register:40f0:8", ["const:4eee10:8", "const:4:8"]]
+ 004eee10 ["CALL", null, ["callee:00c57b10:8"]]
- 004cbf78 bytes 523c1c94
+ 004eee10 bytes 40a31d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c39a35bedf4e4a9a62eb7684154cb478"></a>

### [`004cc1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc1c4.md) → [`004ef05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef05c.md) _ZN5Botan16PK_Decryptor_EMEC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc390.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`00c58de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58de0.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ef094",
      "incomplete_value": true,
      "site": "004ef094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004cc1fc",
      "incomplete_value": true,
      "site": "004cc1fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ef14c",
      "incomplete_value": false,
      "site": "004ef158",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc2b4",
      "incomplete_value": false,
      "site": "004cc2c0",
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
            "const:8de:8"
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
      "definition_site": "004ef178",
      "incomplete_value": false,
      "site": "004ef180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:add:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc2e0",
      "incomplete_value": false,
      "site": "004cc2e8",
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
            "const:403:8"
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
      "004ef084",
      "READ",
      [
        "storage",
        "00c1b220",
        null,
        "pointer"
      ]
    ],
    [
      "004ef094",
      "DATA",
      [
        "storage",
        "00be9fe8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004ef14c",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ef084",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "004ef094",
      "DATA",
      [
        "storage",
        "00c66ba8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004ef14c",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cc2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc1c4.md#insn-004cc2c0) · [`004cc2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc1c4.md#insn-004cc2e8) · [`004cc33c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc1c4.md#insn-004cc33c)
- 新版 `004ef158`（命令位置の公開資料なし） · `004ef180`（命令位置の公開資料なし） · `004ef1d4`（命令位置の公開資料なし）

~~~diff
- 004cc2c0 ["INT_ADD", "register:40f0:8", ["const:4cc2c0:8", "const:4:8"]]
- 004cc2c0 ["CALL", null, ["callee:00c57b60:8"]]
+ 004ef158 ["INT_ADD", "register:40f0:8", ["const:4ef158:8", "const:4:8"]]
+ 004ef158 ["CALL", null, ["callee:00c57b60:8"]]
- 004cc2c0 bytes 943b1c94
+ 004ef158 bytes 82a21d94
- 004cc2e8 ["INT_ADD", "register:40f0:8", ["const:4cc2e8:8", "const:4:8"]]
- 004cc2e8 ["CALL", null, ["callee:00c57b70:8"]]
+ 004ef180 ["INT_ADD", "register:40f0:8", ["const:4ef180:8", "const:4:8"]]
+ 004ef180 ["CALL", null, ["callee:00c57b70:8"]]
- 004cc2e8 bytes 8e3b1c94
+ 004ef180 bytes 7ca21d94
- 004cc33c ["INT_ADD", "register:40f0:8", ["const:4cc33c:8", "const:4:8"]]
- 004cc33c ["CALL", null, ["callee:00c57b10:8"]]
+ 004ef1d4 ["INT_ADD", "register:40f0:8", ["const:4ef1d4:8", "const:4:8"]]
+ 004ef1d4 ["CALL", null, ["callee:00c57b10:8"]]
- 004cc33c bytes 613b1c94
+ 004ef1d4 bytes 4fa21d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eb4510770bd51a80b0556779a998975"></a>

### [`004cc428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc428.md) → [`004ef2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef2c0.md) _ZN5Botan16PK_Decryptor_EMED0Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "site": "004ef2d0",
      "value": [
        "leaf",
        "ram:c58e00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cc438",
      "value": [
        "leaf",
        "ram:bdc3b0:8"
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
      "004ef2d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc3b0"
      ]
    ]
  ],
  "added": [
    [
      "004ef2d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58e00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cc438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc428.md#insn-004cc438)
- 新版 `004ef2d0`（命令位置の公開資料なし）

~~~diff
- 004cc438 ["INT_ADD", "register:40f0:8", ["const:4cc438:8", "const:4:8"]]
- 004cc438 ["CALL", null, ["ram:bdc3b0:8"]]
+ 004ef2d0 ["INT_ADD", "register:40f0:8", ["const:4ef2d0:8", "const:4:8"]]
+ 004ef2d0 ["CALL", null, ["ram:c58e00:8"]]
- 004cc438 bytes de3f1c94
+ 004ef2d0 bytes cca61d94
~~~


<a id="compare-21a456cbb124559cb32d397b018888c8"></a>

### [`004cc45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc45c.md) → [`004ef2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef2f4.md) _ZN5Botan16PK_KEM_EncryptorC2ERKNS_10Public_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorI

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ef3d0",
      "incomplete_value": false,
      "site": "004ef3dc",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc538",
      "incomplete_value": false,
      "site": "004cc544",
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
            "const:8de:8"
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
      "definition_site": "004ef3fc",
      "incomplete_value": false,
      "site": "004ef404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:abc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc564",
      "incomplete_value": false,
      "site": "004cc56c",
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
            "const:3e2:8"
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
      "definition_site": "004ef44c",
      "incomplete_value": true,
      "site": "004ef458",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc5b4",
      "incomplete_value": true,
      "site": "004cc5c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ef3d0",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      "004ef3fc",
      "PARAM",
      [
        "storage",
        "002a33e2",
        null,
        "string"
      ]
    ],
    [
      "004ef448",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ef3d0",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      "004ef3fc",
      "PARAM",
      [
        "storage",
        "002b3abc",
        null,
        "string"
      ]
    ],
    [
      "004ef448",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cc544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc45c.md#insn-004cc544) · [`004cc56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc45c.md#insn-004cc56c) · [`004cc5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc45c.md#insn-004cc5c0)
- 新版 `004ef3dc`（命令位置の公開資料なし） · `004ef404`（命令位置の公開資料なし） · `004ef458`（命令位置の公開資料なし）

~~~diff
- 004cc544 ["INT_ADD", "register:40f0:8", ["const:4cc544:8", "const:4:8"]]
- 004cc544 ["CALL", null, ["callee:00c57b60:8"]]
+ 004ef3dc ["INT_ADD", "register:40f0:8", ["const:4ef3dc:8", "const:4:8"]]
+ 004ef3dc ["CALL", null, ["callee:00c57b60:8"]]
- 004cc544 bytes f33a1c94
+ 004ef3dc bytes e1a11d94
- 004cc56c ["INT_ADD", "register:40f0:8", ["const:4cc56c:8", "const:4:8"]]
- 004cc56c ["CALL", null, ["callee:00c57b70:8"]]
+ 004ef404 ["INT_ADD", "register:40f0:8", ["const:4ef404:8", "const:4:8"]]
+ 004ef404 ["CALL", null, ["callee:00c57b70:8"]]
- 004cc56c bytes ed3a1c94
+ 004ef404 bytes dba11d94
- 004cc5c0 ["INT_ADD", "register:40f0:8", ["const:4cc5c0:8", "const:4:8"]]
- 004cc5c0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ef458 ["INT_ADD", "register:40f0:8", ["const:4ef458:8", "const:4:8"]]
+ 004ef458 ["CALL", null, ["callee:00c57b10:8"]]
- 004cc5c0 bytes c03a1c94
+ 004ef458 bytes aea11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-212f139e9a13dd7231c22c13ba26b18d"></a>

### [`004cc6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc6bc.md) → [`004ef554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef554.md) _ZN5Botan16PK_KEM_DecryptorC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ef638",
      "incomplete_value": false,
      "site": "004ef644",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc7a0",
      "incomplete_value": false,
      "site": "004cc7ac",
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
            "const:8de:8"
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
      "definition_site": "004ef664",
      "incomplete_value": false,
      "site": "004ef66c",
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
            "const:253:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc7cc",
      "incomplete_value": false,
      "site": "004cc7d4",
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
            "const:5b0:8"
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
      "definition_site": "004ef6b4",
      "incomplete_value": true,
      "site": "004ef6c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cc81c",
      "incomplete_value": true,
      "site": "004cc828",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ef638",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      "004ef664",
      "PARAM",
      [
        "storage",
        "002a95b0",
        null,
        "string"
      ]
    ],
    [
      "004ef6b0",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ef638",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      "004ef664",
      "PARAM",
      [
        "storage",
        "002ba253",
        null,
        "string"
      ]
    ],
    [
      "004ef6b0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cc7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc6bc.md#insn-004cc7ac) · [`004cc7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc6bc.md#insn-004cc7d4) · [`004cc828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc6bc.md#insn-004cc828)
- 新版 `004ef644`（命令位置の公開資料なし） · `004ef66c`（命令位置の公開資料なし） · `004ef6c0`（命令位置の公開資料なし）

~~~diff
- 004cc7ac ["INT_ADD", "register:40f0:8", ["const:4cc7ac:8", "const:4:8"]]
- 004cc7ac ["CALL", null, ["callee:00c57b60:8"]]
+ 004ef644 ["INT_ADD", "register:40f0:8", ["const:4ef644:8", "const:4:8"]]
+ 004ef644 ["CALL", null, ["callee:00c57b60:8"]]
- 004cc7ac bytes 593a1c94
+ 004ef644 bytes 47a11d94
- 004cc7d4 ["INT_ADD", "register:40f0:8", ["const:4cc7d4:8", "const:4:8"]]
- 004cc7d4 ["CALL", null, ["callee:00c57b70:8"]]
+ 004ef66c ["INT_ADD", "register:40f0:8", ["const:4ef66c:8", "const:4:8"]]
+ 004ef66c ["CALL", null, ["callee:00c57b70:8"]]
- 004cc7d4 bytes 533a1c94
+ 004ef66c bytes 41a11d94
- 004cc828 ["INT_ADD", "register:40f0:8", ["const:4cc828:8", "const:4:8"]]
- 004cc828 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ef6c0 ["INT_ADD", "register:40f0:8", ["const:4ef6c0:8", "const:4:8"]]
+ 004ef6c0 ["CALL", null, ["callee:00c57b10:8"]]
- 004cc828 bytes 263a1c94
+ 004ef6c0 bytes 14a11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f2b02a1b7747390a9a3810695daec61"></a>

### [`004cc924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc924.md) → [`004ef7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef7bc.md) _ZN5Botan16PK_Key_AgreementC2ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ef8a0",
      "incomplete_value": false,
      "site": "004ef8ac",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cca08",
      "incomplete_value": false,
      "site": "004cca14",
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
            "const:8de:8"
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
      "definition_site": "004ef8cc",
      "incomplete_value": false,
      "site": "004ef8d4",
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
            "const:fac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cca34",
      "incomplete_value": false,
      "site": "004cca3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:a6a:8"
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
      "definition_site": "004ef91c",
      "incomplete_value": true,
      "site": "004ef928",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cca84",
      "incomplete_value": true,
      "site": "004cca90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ef8a0",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      "004ef8cc",
      "PARAM",
      [
        "storage",
        "00290a6a",
        null,
        "string"
      ]
    ],
    [
      "004ef918",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ef8a0",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      "004ef8cc",
      "PARAM",
      [
        "storage",
        "0029ffac",
        null,
        "string"
      ]
    ],
    [
      "004ef918",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cca14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc924.md#insn-004cca14) · [`004cca3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc924.md#insn-004cca3c) · [`004cca90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc924.md#insn-004cca90)
- 新版 `004ef8ac`（命令位置の公開資料なし） · `004ef8d4`（命令位置の公開資料なし） · `004ef928`（命令位置の公開資料なし）

~~~diff
- 004cca14 ["INT_ADD", "register:40f0:8", ["const:4cca14:8", "const:4:8"]]
- 004cca14 ["CALL", null, ["callee:00c57b60:8"]]
+ 004ef8ac ["INT_ADD", "register:40f0:8", ["const:4ef8ac:8", "const:4:8"]]
+ 004ef8ac ["CALL", null, ["callee:00c57b60:8"]]
- 004cca14 bytes bf391c94
+ 004ef8ac bytes ada01d94
- 004cca3c ["INT_ADD", "register:40f0:8", ["const:4cca3c:8", "const:4:8"]]
- 004cca3c ["CALL", null, ["callee:00c57b70:8"]]
+ 004ef8d4 ["INT_ADD", "register:40f0:8", ["const:4ef8d4:8", "const:4:8"]]
+ 004ef8d4 ["CALL", null, ["callee:00c57b70:8"]]
- 004cca3c bytes b9391c94
+ 004ef8d4 bytes a7a01d94
- 004cca90 ["INT_ADD", "register:40f0:8", ["const:4cca90:8", "const:4:8"]]
- 004cca90 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ef928 ["INT_ADD", "register:40f0:8", ["const:4ef928:8", "const:4:8"]]
+ 004ef928 ["CALL", null, ["callee:00c57b10:8"]]
- 004cca90 bytes 8c391c94
+ 004ef928 bytes 7aa01d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4f76cacc3ae220cefbf16179dc333df"></a>

### [`004ccca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccca0.md) → [`004efb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efb38.md) _ZN5Botan9PK_SignerC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEENS

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3e0.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`00c58e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e30.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004efc5c",
      "incomplete_value": false,
      "site": "004efc68",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ccdc4",
      "incomplete_value": false,
      "site": "004ccdd0",
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
            "const:8de:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004efc88",
      "incomplete_value": false,
      "site": "004efc90",
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
            "const:d45:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ccdf0",
      "incomplete_value": false,
      "site": "004ccdf8",
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
            "const:a1f:8"
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
      "definition_site": "004efcd8",
      "incomplete_value": true,
      "site": "004efce4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cce40",
      "incomplete_value": true,
      "site": "004cce4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004efc5c",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      "004efc88",
      "PARAM",
      [
        "storage",
        "002ada1f",
        null,
        "string"
      ]
    ],
    [
      "004efcd4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004efc5c",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      "004efc88",
      "PARAM",
      [
        "storage",
        "002bed45",
        null,
        "string"
      ]
    ],
    [
      "004efcd4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ccdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccca0.md#insn-004ccdd0) · [`004ccdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccca0.md#insn-004ccdf8) · [`004cce4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccca0.md#insn-004cce4c)
- 新版 `004efc68`（命令位置の公開資料なし） · `004efc90`（命令位置の公開資料なし） · `004efce4`（命令位置の公開資料なし）

~~~diff
- 004ccdd0 ["INT_ADD", "register:40f0:8", ["const:4ccdd0:8", "const:4:8"]]
- 004ccdd0 ["CALL", null, ["callee:00c57b60:8"]]
+ 004efc68 ["INT_ADD", "register:40f0:8", ["const:4efc68:8", "const:4:8"]]
+ 004efc68 ["CALL", null, ["callee:00c57b60:8"]]
- 004ccdd0 bytes d0381c94
+ 004efc68 bytes be9f1d94
- 004ccdf8 ["INT_ADD", "register:40f0:8", ["const:4ccdf8:8", "const:4:8"]]
- 004ccdf8 ["CALL", null, ["callee:00c57b70:8"]]
+ 004efc90 ["INT_ADD", "register:40f0:8", ["const:4efc90:8", "const:4:8"]]
+ 004efc90 ["CALL", null, ["callee:00c57b70:8"]]
- 004ccdf8 bytes ca381c94
+ 004efc90 bytes b89f1d94
- 004cce4c ["INT_ADD", "register:40f0:8", ["const:4cce4c:8", "const:4:8"]]
- 004cce4c ["CALL", null, ["callee:00c57b10:8"]]
+ 004efce4 ["INT_ADD", "register:40f0:8", ["const:4efce4:8", "const:4:8"]]
+ 004efce4 ["CALL", null, ["callee:00c57b10:8"]]
- 004cce4c bytes 9d381c94
+ 004efce4 bytes 8b9f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb4c769daa88f57d320e5fb9cb0a722"></a>

### [`004ccf4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccf4c.md) → [`004efde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efde4.md) _ZN5Botan9PK_Signer9signatureERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc400.md) · 呼出先 21件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md)
- 新版 呼出元 1件 [`00c58e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e50.md) · 呼出先 21件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.84% / 新版 97.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004efeac",
      "incomplete_value": true,
      "site": "004efeac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
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
    "old": {
      "definition_site": "004cd014",
      "incomplete_value": true,
      "site": "004cd014",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f0088",
      "incomplete_value": true,
      "site": "004f0088",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
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
    "old": {
      "definition_site": "004cd1f0",
      "incomplete_value": true,
      "site": "004cd1f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f00ec",
      "incomplete_value": true,
      "site": "004f00ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cd254",
      "incomplete_value": true,
      "site": "004cd254",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 19,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004efe9c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f0078",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f00dc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004efe9c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f0078",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f00dc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cd014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccf4c.md#insn-004cd014) · [`004cd1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccf4c.md#insn-004cd1f0) · [`004cd254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004ccf4c.md#insn-004cd254)
- 新版 `004efeac`（命令位置の公開資料なし） · `004f0088`（命令位置の公開資料なし） · `004f00ec`（命令位置の公開資料なし）

~~~diff
- 004cd014 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cd014 ["INT_ADD", "register:40f0:8", ["const:4cd014:8", "const:4:8"]]
- 004cd014 ["CALLIND", null, ["register:0:8"]]
+ 004efeac ["COPY", "register:0:8", ["register:4048:8"]]
+ 004efeac ["INT_ADD", "register:40f0:8", ["const:4efeac:8", "const:4:8"]]
+ 004efeac ["CALLIND", null, ["register:0:8"]]
- 004cd014 bytes 20013fd6
+ 004efeac bytes 20013fd6
- 004cd1f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cd1f0 ["INT_ADD", "register:40f0:8", ["const:4cd1f0:8", "const:4:8"]]
- 004cd1f0 ["CALLIND", null, ["register:0:8"]]
+ 004f0088 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f0088 ["INT_ADD", "register:40f0:8", ["const:4f0088:8", "const:4:8"]]
+ 004f0088 ["CALLIND", null, ["register:0:8"]]
- 004cd1f0 bytes 20013fd6
+ 004f0088 bytes 20013fd6
- 004cd254 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cd254 ["INT_ADD", "register:40f0:8", ["const:4cd254:8", "const:4:8"]]
- 004cd254 ["CALLIND", null, ["register:0:8"]]
+ 004f00ec ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f00ec ["INT_ADD", "register:40f0:8", ["const:4f00ec:8", "const:4:8"]]
+ 004f00ec ["CALLIND", null, ["register:0:8"]]
- 004cd254 bytes 20013fd6
+ 004f00ec bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8ae3b7de7d5dc8278d0c31616f974ff"></a>

### [`004cd48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd48c.md) → [`004f0324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0324.md) _ZN5Botan11PK_VerifierC2ERKNS_10Public_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS_16Signature_FormatESC_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3f0.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`00c58e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e40.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f042c",
      "incomplete_value": false,
      "site": "004f0438",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cd594",
      "incomplete_value": false,
      "site": "004cd5a0",
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
            "const:8de:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f0458",
      "incomplete_value": false,
      "site": "004f0460",
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
            "const:7f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cd5c0",
      "incomplete_value": false,
      "site": "004cd5c8",
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
            "const:a66:8"
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
      "definition_site": "004f04a8",
      "incomplete_value": true,
      "site": "004f04b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cd610",
      "incomplete_value": true,
      "site": "004cd61c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004f042c",
      "PARAM",
      [
        "storage",
        "002ae8de",
        null,
        "string"
      ]
    ],
    [
      "004f0458",
      "PARAM",
      [
        "storage",
        "00291a66",
        null,
        "string"
      ]
    ],
    [
      "004f04a4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f042c",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      "004f0458",
      "PARAM",
      [
        "storage",
        "002a107f",
        null,
        "string"
      ]
    ],
    [
      "004f04a4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cd5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd48c.md#insn-004cd5a0) · [`004cd5c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd48c.md#insn-004cd5c8) · [`004cd61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd48c.md#insn-004cd61c)
- 新版 `004f0438`（命令位置の公開資料なし） · `004f0460`（命令位置の公開資料なし） · `004f04b4`（命令位置の公開資料なし）

~~~diff
- 004cd5a0 ["INT_ADD", "register:40f0:8", ["const:4cd5a0:8", "const:4:8"]]
- 004cd5a0 ["CALL", null, ["callee:00c57b60:8"]]
+ 004f0438 ["INT_ADD", "register:40f0:8", ["const:4f0438:8", "const:4:8"]]
+ 004f0438 ["CALL", null, ["callee:00c57b60:8"]]
- 004cd5a0 bytes dc361c94
+ 004f0438 bytes ca9d1d94
- 004cd5c8 ["INT_ADD", "register:40f0:8", ["const:4cd5c8:8", "const:4:8"]]
- 004cd5c8 ["CALL", null, ["callee:00c57b70:8"]]
+ 004f0460 ["INT_ADD", "register:40f0:8", ["const:4f0460:8", "const:4:8"]]
+ 004f0460 ["CALL", null, ["callee:00c57b70:8"]]
- 004cd5c8 bytes d6361c94
+ 004f0460 bytes c49d1d94
- 004cd61c ["INT_ADD", "register:40f0:8", ["const:4cd61c:8", "const:4:8"]]
- 004cd61c ["CALL", null, ["callee:00c57b10:8"]]
+ 004f04b4 ["INT_ADD", "register:40f0:8", ["const:4f04b4:8", "const:4:8"]]
+ 004f04b4 ["CALL", null, ["callee:00c57b10:8"]]
- 004cd61c bytes a9361c94
+ 004f04b4 bytes 979d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e1d568967f2d7546417ddc31e4bce20"></a>

### [`004cd70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd70c.md) → [`004f05a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f05a4.md) _ZN5Botan11PK_Verifier16set_input_formatENS_16Signature_FormatE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

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
      "definition_site": "004f0610",
      "incomplete_value": false,
      "site": "004f0618",
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
            "const:f51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cd778",
      "incomplete_value": false,
      "site": "004cd780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:28f000:8"
          ],
          [
            "leaf",
            "const:b11:8"
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
      "definition_site": "004f064c",
      "incomplete_value": true,
      "site": "004f0658",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cd7b4",
      "incomplete_value": true,
      "site": "004cd7c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f0648",
      "incomplete_value": false,
      "site": "004f0658",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004cd7b0",
      "incomplete_value": false,
      "site": "004cd7c0",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004f0610",
      "PARAM",
      [
        "storage",
        "0028fb11",
        null,
        "string"
      ]
    ],
    [
      "004f0648",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004f064c",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f0610",
      "PARAM",
      [
        "storage",
        "0029ef51",
        null,
        "string"
      ]
    ],
    [
      "004f0648",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f064c",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cd780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd70c.md#insn-004cd780) · [`004cd7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd70c.md#insn-004cd7c0) · [`004cd76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd70c.md#insn-004cd76c)
- 新版 `004f0618`（命令位置の公開資料なし） · `004f0658`（命令位置の公開資料なし） · `004f0604`（命令位置の公開資料なし）

~~~diff
- 004cd780 ["INT_ADD", "register:40f0:8", ["const:4cd780:8", "const:4:8"]]
- 004cd780 ["CALL", null, ["callee:0043dd98:8"]]
+ 004f0618 ["INT_ADD", "register:40f0:8", ["const:4f0618:8", "const:4:8"]]
+ 004f0618 ["CALL", null, ["callee:0043dd98:8"]]
- 004cd780 bytes c636fd97
+ 004f0618 bytes e035fd97
- 004cd7c0 ["INT_ADD", "register:40f0:8", ["const:4cd7c0:8", "const:4:8"]]
- 004cd7c0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f0658 ["INT_ADD", "register:40f0:8", ["const:4f0658:8", "const:4:8"]]
+ 004f0658 ["CALL", null, ["callee:00c57b10:8"]]
- 004cd7c0 bytes 40361c94
+ 004f0658 bytes 2e9d1d94
- 004cd76c ["INT_ADD", "register:40f0:8", ["const:4cd76c:8", "const:4:8"]]
- 004cd76c ["CALL", null, ["callee:00c57af0:8"]]
+ 004f0604 ["INT_ADD", "register:40f0:8", ["const:4f0604:8", "const:4:8"]]
+ 004f0604 ["CALL", null, ["callee:00c57af0:8"]]
- 004cd76c bytes 4d361c94
+ 004f0604 bytes 3b9d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abf7274697139fea0a2320e8253aa923"></a>

### [`004cd86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd86c.md) → [`004f0704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0704.md) _ZN5Botan11PK_Verifier15check_signatureEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc410.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`004cdca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cdca8.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c58e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e60.md) · 呼出先 16件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`004f0b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0b40.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.19% / 新版 93.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 5件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004f0764",
      "value": [
        "leaf",
        "ram:c58340:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cd8cc",
      "value": [
        "leaf",
        "ram:bdb8f0:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f0828",
      "incomplete_value": true,
      "site": "004f0828",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cd990",
      "incomplete_value": true,
      "site": "004cd990",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f0854",
      "incomplete_value": true,
      "site": "004f0854",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cd9bc",
      "incomplete_value": true,
      "site": "004cd9bc",
      "value": [
        "LOAD",
        "8",
        [
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
      "004f0764",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb8f0"
      ]
    ],
    [
      "004f0818",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f0844",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f0764",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58340"
      ]
    ],
    [
      "004f0818",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f0844",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cd8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd86c.md#insn-004cd8cc) · [`004cd990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd86c.md#insn-004cd990) · [`004cd9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cd86c.md#insn-004cd9bc)
- 新版 `004f0764`（命令位置の公開資料なし） · `004f0828`（命令位置の公開資料なし） · `004f0854`（命令位置の公開資料なし）

~~~diff
- 004cd8cc ["INT_ADD", "register:40f0:8", ["const:4cd8cc:8", "const:4:8"]]
- 004cd8cc ["CALL", null, ["ram:bdb8f0:8"]]
+ 004f0764 ["INT_ADD", "register:40f0:8", ["const:4f0764:8", "const:4:8"]]
+ 004f0764 ["CALL", null, ["ram:c58340:8"]]
- 004cd8cc bytes 09381c94
+ 004f0764 bytes f79e1d94
- 004cd990 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cd990 ["INT_ADD", "register:40f0:8", ["const:4cd990:8", "const:4:8"]]
- 004cd990 ["CALLIND", null, ["register:0:8"]]
+ 004f0828 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f0828 ["INT_ADD", "register:40f0:8", ["const:4f0828:8", "const:4:8"]]
+ 004f0828 ["CALLIND", null, ["register:0:8"]]
- 004cd990 bytes 20013fd6
+ 004f0828 bytes 20013fd6
- 004cd9bc ["COPY", "register:0:8", ["register:4048:8"]]
- 004cd9bc ["INT_ADD", "register:40f0:8", ["const:4cd9bc:8", "const:4:8"]]
- 004cd9bc ["CALLIND", null, ["register:0:8"]]
+ 004f0854 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f0854 ["INT_ADD", "register:40f0:8", ["const:4f0854:8", "const:4:8"]]
+ 004f0854 ["CALLIND", null, ["register:0:8"]]
- 004cd9bc bytes 20013fd6
+ 004f0854 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-883d71c6d9b8839573acca2e2a2ac7ac"></a>

### [`004cddd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cddd0.md) → [`004f0c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0c68.md) _ZN5Botan14if_work_factorEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5f0.md) [`00bdc860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc860.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004f0cbc",
      "incomplete_value": true,
      "site": "004f0cc8",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cde24",
      "incomplete_value": true,
      "site": "004cde30",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
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
      "004f0c7c",
      "READ",
      [
        "storage",
        "002b2c08",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0ca8",
      "READ",
      [
        "storage",
        "002b27c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0cb4",
      "READ",
      [
        "storage",
        "002b2c38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004f0c7c",
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0ca8",
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0cb4",
      "READ",
      [
        "storage",
        "002c4348",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cdde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cddd0.md#insn-004cdde0) · [`004cdde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cddd0.md#insn-004cdde4) · [`004cddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cddd0.md#insn-004cddf0)
- 新版 `004f0c78`（命令位置の公開資料なし） · `004f0c7c`（命令位置の公開資料なし） · `004f0c88`（命令位置の公開資料なし）

~~~diff
- 004cdde0 ["COPY", "register:4040:8", ["const:2b2000:8"]]
+ 004f0c78 ["COPY", "register:4040:8", ["const:2c4000:8"]]
- 004cdde0 bytes 28efffb0
+ 004f0c78 bytes a8eeff90
- 004cdde4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
- 004cdde4 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
- 004cdde4 ["COPY", "register:5128:8", ["const:0:8"]]
- 004cdde4 ["COPY", "register:5130:8", ["const:0:8"]]
+ 004f0c7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004f0c7c ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f0c7c ["COPY", "register:5128:8", ["const:0:8"]]
+ 004f0c7c ["COPY", "register:5130:8", ["const:0:8"]]
- 004cdde4 bytes 090546fd
+ 004f0c7c bytes 098d41fd
- 004cddf0 ["INT_ADD", "register:40f0:8", ["const:4cddf0:8", "const:4:8"]]
- 004cddf0 ["CALL", null, ["callee:00c592b0:8"]]
+ 004f0c88 ["INT_ADD", "register:40f0:8", ["const:4f0c88:8", "const:4:8"]]
+ 004f0c88 ["CALL", null, ["callee:00c592b0:8"]]
- 004cddf0 bytes 9c3a1c94
+ 004f0c88 bytes 8aa11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86f8f9abe965e744b7b57bfa1abe5ec5"></a>

### [`004cde34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cde34.md) → [`004f0ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0ccc.md) _ZN5Botan14dl_work_factorEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5f0.md) [`00bdc860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc860.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004f0d20",
      "incomplete_value": true,
      "site": "004f0d2c",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cde88",
      "incomplete_value": true,
      "site": "004cde94",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
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
      "004f0ce0",
      "READ",
      [
        "storage",
        "002b2c08",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0d0c",
      "READ",
      [
        "storage",
        "002b27c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0d18",
      "READ",
      [
        "storage",
        "002b2c38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004f0ce0",
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0d0c",
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0d18",
      "READ",
      [
        "storage",
        "002c4348",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cde44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cde34.md#insn-004cde44) · [`004cde48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cde34.md#insn-004cde48) · [`004cde54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cde34.md#insn-004cde54)
- 新版 `004f0cdc`（命令位置の公開資料なし） · `004f0ce0`（命令位置の公開資料なし） · `004f0cec`（命令位置の公開資料なし）

~~~diff
- 004cde44 ["COPY", "register:4040:8", ["const:2b2000:8"]]
+ 004f0cdc ["COPY", "register:4040:8", ["const:2c4000:8"]]
- 004cde44 bytes 28efffb0
+ 004f0cdc bytes a8eeff90
- 004cde48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
- 004cde48 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
- 004cde48 ["COPY", "register:5128:8", ["const:0:8"]]
- 004cde48 ["COPY", "register:5130:8", ["const:0:8"]]
+ 004f0ce0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004f0ce0 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f0ce0 ["COPY", "register:5128:8", ["const:0:8"]]
+ 004f0ce0 ["COPY", "register:5130:8", ["const:0:8"]]
- 004cde48 bytes 090546fd
+ 004f0ce0 bytes 098d41fd
- 004cde54 ["INT_ADD", "register:40f0:8", ["const:4cde54:8", "const:4:8"]]
- 004cde54 ["CALL", null, ["callee:00c592b0:8"]]
+ 004f0cec ["INT_ADD", "register:40f0:8", ["const:4f0cec:8", "const:4:8"]]
+ 004f0cec ["CALL", null, ["callee:00c592b0:8"]]
- 004cde54 bytes 833a1c94
+ 004f0cec bytes 71a11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43be5c0a4bf3affa62f490fcbdd9dac0"></a>

### [`004cdf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cdf20.md) → [`004f0db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0db8.md) _ZN5Botan4X50910PEM_encodeERKNS_10Public_KeyE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc870.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) [`00bdc780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc780.md)
- 新版 呼出元 1件 [`00c592c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592c0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c591d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591d0.md)

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
      "definition_site": "004f0e08",
      "incomplete_value": true,
      "site": "004f0e08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:dcc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cdf70",
      "incomplete_value": true,
      "site": "004cdf70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e8:8"
              ]
            ]
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
      "004f0df4",
      "READ",
      [
        "storage",
        "002ae8e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f0df4",
      "READ",
      [
        "storage",
        "002bfdcc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cdf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cdf20.md#insn-004cdf44) · [`004cdf4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cdf20.md#insn-004cdf4c) · [`004cdf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cd/004cdf20.md#insn-004cdf50)
- 新版 `004f0ddc`（命令位置の公開資料なし） · `004f0de4`（命令位置の公開資料なし） · `004f0de8`（命令位置の公開資料なし）

~~~diff
- 004cdf44 ["INT_ADD", "register:40f0:8", ["const:4cdf44:8", "const:4:8"]]
- 004cdf44 ["CALL", null, ["callee:00c591d0:8"]]
+ 004f0ddc ["INT_ADD", "register:40f0:8", ["const:4f0ddc:8", "const:4:8"]]
+ 004f0ddc ["CALL", null, ["callee:00c591d0:8"]]
- 004cdf44 bytes 0f3a1c94
+ 004f0ddc bytes fda01d94
- 004cdf4c ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 004f0de4 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 004cdf4c bytes 09efffb0
+ 004f0de4 bytes 69eefff0
- 004cdf50 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 004cdf50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004cdf50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004cdf50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f0de8 ["COPY", "tmp:0:8", ["const:dcc:8"]]
+ 004f0de8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f0de8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f0de8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004cdf50 bytes 29a12391
+ 004f0de8 bytes 29313791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2dd1e809e3f1821c265767e06867f4f"></a>

### [`004ce004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md) → [`004f0e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md) _ZN5Botan4X5098load_keyERNS_10DataSourceE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md) · 呼出先 20件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md) [`004840c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/004840c4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md)
- 新版 呼出元 1件 [`00c592d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md) · 呼出先 20件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004a6f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.39% / 新版 93.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 4件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f0ed0",
      "incomplete_value": true,
      "site": "004f0ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ce038",
      "incomplete_value": true,
      "site": "004ce038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f0f5c",
      "incomplete_value": true,
      "site": "004f0f5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:dcc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ce0c4",
      "incomplete_value": true,
      "site": "004ce0c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e8:8"
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
      "definition_site": "004f0f88",
      "incomplete_value": true,
      "site": "004f0f88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ce0f0",
      "incomplete_value": true,
      "site": "004ce0f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f0ec0",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004f0ed0",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f0f4c",
      "READ",
      [
        "storage",
        "002ae8e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f0ec0",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004f0ed0",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f0f4c",
      "READ",
      [
        "storage",
        "002bfdcc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ce12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md#insn-004ce12c) · [`004ce1d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md#insn-004ce1d4) · [`004ce218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md#insn-004ce218)
- 新版 `004f0fc4`（命令位置の公開資料なし） · `004f106c`（命令位置の公開資料なし） · `004f10b0`（命令位置の公開資料なし）

~~~diff
- 004ce12c ["COPY", "register:0:8", ["register:4048:8"]]
- 004ce12c ["INT_ADD", "register:40f0:8", ["const:4ce12c:8", "const:4:8"]]
- 004ce12c ["CALLIND", null, ["register:0:8"]]
+ 004f0fc4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f0fc4 ["INT_ADD", "register:40f0:8", ["const:4f0fc4:8", "const:4:8"]]
+ 004f0fc4 ["CALLIND", null, ["register:0:8"]]
- 004ce12c bytes 20013fd6
+ 004f0fc4 bytes 20013fd6
- 004ce1d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ce1d4 ["INT_ADD", "register:40f0:8", ["const:4ce1d4:8", "const:4:8"]]
- 004ce1d4 ["CALLIND", null, ["register:0:8"]]
+ 004f106c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f106c ["INT_ADD", "register:40f0:8", ["const:4f106c:8", "const:4:8"]]
+ 004f106c ["CALLIND", null, ["register:0:8"]]
- 004ce1d4 bytes 20013fd6
+ 004f106c bytes 20013fd6
- 004ce218 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ce218 ["INT_ADD", "register:40f0:8", ["const:4ce218:8", "const:4:8"]]
- 004ce218 ["CALLIND", null, ["register:0:8"]]
+ 004f10b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f10b0 ["INT_ADD", "register:40f0:8", ["const:4f10b0:8", "const:4:8"]]
+ 004f10b0 ["CALLIND", null, ["register:0:8"]]
- 004ce218 bytes 20013fd6
+ 004f10b0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-107259265f46add42966e6b2bd7ed79b"></a>

### [`004ce670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce670.md) → [`004f1508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1508.md) _ZN5Botan4X5098load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md) [`00bdc820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md) [`00bdc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md) [`00c592d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

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
      "site": "004f1544",
      "value": [
        "leaf",
        "ram:c59270:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ce6ac",
      "value": [
        "leaf",
        "ram:bdc820:8"
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
      "004f1544",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc820"
      ]
    ]
  ],
  "added": [
    [
      "004f1544",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59270"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ce6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce670.md#insn-004ce6ac) · [`004ce698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce670.md#insn-004ce698) · [`004ce6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce670.md#insn-004ce6a0)
- 新版 `004f1544`（命令位置の公開資料なし） · `004f1530`（命令位置の公開資料なし） · `004f1538`（命令位置の公開資料なし）

~~~diff
- 004ce6ac ["INT_ADD", "register:40f0:8", ["const:4ce6ac:8", "const:4:8"]]
- 004ce6ac ["CALL", null, ["ram:bdc820:8"]]
+ 004f1544 ["INT_ADD", "register:40f0:8", ["const:4f1544:8", "const:4:8"]]
+ 004f1544 ["CALL", null, ["ram:c59270:8"]]
- 004ce6ac bytes 5d381c94
+ 004f1544 bytes 4b9f1d94
- 004ce698 ["INT_ADD", "register:40f0:8", ["const:4ce698:8", "const:4:8"]]
- 004ce698 ["CALL", null, ["callee:00c59260:8"]]
+ 004f1530 ["INT_ADD", "register:40f0:8", ["const:4f1530:8", "const:4:8"]]
+ 004f1530 ["CALL", null, ["callee:00c59260:8"]]
- 004ce698 bytes 5e381c94
+ 004f1530 bytes 4c9f1d94
- 004ce6a0 ["INT_ADD", "register:40f0:8", ["const:4ce6a0:8", "const:4:8"]]
- 004ce6a0 ["CALL", null, ["callee:00c592d0:8"]]
+ 004f1538 ["INT_ADD", "register:40f0:8", ["const:4f1538:8", "const:4:8"]]
+ 004f1538 ["CALL", null, ["callee:00c592d0:8"]]
- 004ce6a0 bytes 78381c94
+ 004f1538 bytes 669f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a306b57ac63a133da3dab4f38fad996"></a>

### [`004ce6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce6fc.md) → [`004f1594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1594.md) _ZN5Botan4X5098load_keyERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8a0.md) · 呼出先 5件 [`00513e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513e2c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00c592f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592f0.md) · 呼出先 5件 [`00536cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536cc4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c592d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f15c4",
      "incomplete_value": true,
      "site": "004f15c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ce72c",
      "incomplete_value": true,
      "site": "004ce72c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f1610",
      "incomplete_value": true,
      "site": "004f1610",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
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
    "old": {
      "definition_site": "004ce778",
      "incomplete_value": true,
      "site": "004ce778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004f15b0",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "004f15c4",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004f1600",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f15b0",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f15c4",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004f1600",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ce778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce6fc.md#insn-004ce778) · [`004ce714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce6fc.md#insn-004ce714) · [`004ce718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce6fc.md#insn-004ce718)
- 新版 `004f1610`（命令位置の公開資料なし） · `004f15ac`（命令位置の公開資料なし） · `004f15b0`（命令位置の公開資料なし）

~~~diff
- 004ce778 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ce778 ["INT_ADD", "register:40f0:8", ["const:4ce778:8", "const:4:8"]]
- 004ce778 ["CALLIND", null, ["register:0:8"]]
+ 004f1610 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f1610 ["INT_ADD", "register:40f0:8", ["const:4f1610:8", "const:4:8"]]
+ 004f1610 ["CALLIND", null, ["register:0:8"]]
- 004ce778 bytes 20013fd6
+ 004f1610 bytes 20013fd6
- 004ce714 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004f15ac ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004ce714 bytes 683a0090
+ 004f15ac bytes 483d00b0
- 004ce718 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
- 004ce718 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f15b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9e0:8"]]
+ 004f15b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ce718 bytes 08f947f9
+ 004f15b0 bytes 08f144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60e8ce0b63ca5db9a457de955d9f2cab"></a>

### [`004ce7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce7d8.md) → [`004f1670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1670.md) _ZN5Botan4X5098copy_keyERKNS_10Public_KeyE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc670.md) [`00bdc870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc870.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c590c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590c0.md) [`00c592c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592c0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.02% / 新版 93.02%

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
      "site": "004f16a0",
      "value": [
        "leaf",
        "ram:c590c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ce808",
      "value": [
        "leaf",
        "ram:bdc670:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f16e4",
      "incomplete_value": true,
      "site": "004f16e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
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
    "old": {
      "definition_site": "004ce84c",
      "incomplete_value": true,
      "site": "004ce84c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004f16a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc670"
      ]
    ],
    [
      "004f16d4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f16a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c590c0"
      ]
    ],
    [
      "004f16d4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ce808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce7d8.md#insn-004ce808) · [`004ce84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce7d8.md#insn-004ce84c) · [`004ce7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce7d8.md#insn-004ce7fc)
- 新版 `004f16a0`（命令位置の公開資料なし） · `004f16e4`（命令位置の公開資料なし） · `004f1694`（命令位置の公開資料なし）

~~~diff
- 004ce808 ["INT_ADD", "register:40f0:8", ["const:4ce808:8", "const:4:8"]]
- 004ce808 ["CALL", null, ["ram:bdc670:8"]]
+ 004f16a0 ["INT_ADD", "register:40f0:8", ["const:4f16a0:8", "const:4:8"]]
+ 004f16a0 ["CALL", null, ["ram:c590c0:8"]]
- 004ce808 bytes 9a371c94
+ 004f16a0 bytes 889e1d94
- 004ce84c ["COPY", "register:0:8", ["register:4048:8"]]
- 004ce84c ["INT_ADD", "register:40f0:8", ["const:4ce84c:8", "const:4:8"]]
- 004ce84c ["CALLIND", null, ["register:0:8"]]
+ 004f16e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f16e4 ["INT_ADD", "register:40f0:8", ["const:4f16e4:8", "const:4:8"]]
+ 004f16e4 ["CALLIND", null, ["register:0:8"]]
- 004ce84c bytes 20013fd6
+ 004f16e4 bytes 20013fd6
- 004ce7fc ["INT_ADD", "register:40f0:8", ["const:4ce7fc:8", "const:4:8"]]
- 004ce7fc ["CALL", null, ["callee:00c592c0:8"]]
+ 004f1694 ["INT_ADD", "register:40f0:8", ["const:4f1694:8", "const:4:8"]]
+ 004f1694 ["CALL", null, ["callee:00c592c0:8"]]
- 004ce7fc bytes 1d381c94
+ 004f1694 bytes 0b9f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16f6ad619dc3bdf1e019ffaf8b3d36cd"></a>

### [`004cec60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cec60.md) → [`004f1af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1af8.md) _ZN5Botan21RandomNumberGenerator8make_rngEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f1b3c",
      "incomplete_value": true,
      "site": "004f1b48",
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
                "const:160:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ceca4",
      "incomplete_value": true,
      "site": "004cecb0",
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
                "const:2b1000:8"
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f1b38",
      "incomplete_value": true,
      "site": "004f1b4c",
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
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:d6c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ceca0",
      "incomplete_value": true,
      "site": "004cecb4",
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
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:a46:8"
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
      "definition_site": "004f1b38",
      "incomplete_value": true,
      "site": "004f1b4c",
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
      "definition_site": "004ceca0",
      "incomplete_value": true,
      "site": "004cecb4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f1b38",
      "READ",
      [
        "storage",
        "002ada46",
        null,
        "string"
      ]
    ],
    [
      "004f1b38",
      "READ",
      [
        "storage",
        "002ada56",
        null,
        "string"
      ]
    ],
    [
      "004f1b3c",
      "READ",
      [
        "storage",
        "002b1a90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f1b38",
      "READ",
      [
        "storage",
        "002bed6c",
        null,
        "string"
      ]
    ],
    [
      "004f1b38",
      "READ",
      [
        "storage",
        "002bed7c",
        null,
        "string"
      ]
    ],
    [
      "004f1b3c",
      "READ",
      [
        "storage",
        "002c3160",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cecf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cec60.md#insn-004cecf8) · [`004cec84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cec60.md#insn-004cec84) · [`004cec90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cec60.md#insn-004cec90)
- 新版 `004f1b90`（命令位置の公開資料なし） · `004f1b1c`（命令位置の公開資料なし） · `004f1b28`（命令位置の公開資料なし）

~~~diff
- 004cecf8 ["INT_ADD", "register:40f0:8", ["const:4cecf8:8", "const:4:8"]]
- 004cecf8 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f1b90 ["INT_ADD", "register:40f0:8", ["const:4f1b90:8", "const:4:8"]]
+ 004f1b90 ["CALL", null, ["callee:00c57b10:8"]]
- 004cecf8 bytes f2301c94
+ 004f1b90 bytes e0971d94
- 004cec84 ["INT_ADD", "register:40f0:8", ["const:4cec84:8", "const:4:8"]]
- 004cec84 ["CALL", null, ["callee:00c57af0:8"]]
+ 004f1b1c ["INT_ADD", "register:40f0:8", ["const:4f1b1c:8", "const:4:8"]]
+ 004f1b1c ["CALL", null, ["callee:00c57af0:8"]]
- 004cec84 bytes 07311c94
+ 004f1b1c bytes f5971d94
- 004cec90 ["INT_ADD", "register:40f0:8", ["const:4cec90:8", "const:4:8"]]
- 004cec90 ["CALL", null, ["callee:00c57a90:8"]]
+ 004f1b28 ["INT_ADD", "register:40f0:8", ["const:4f1b28:8", "const:4:8"]]
+ 004f1b28 ["CALL", null, ["callee:00c57a90:8"]]
- 004cec90 bytes ec301c94
+ 004f1b28 bytes da971d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70ee6b1a1b9eaf2bd5ed458517740e9d"></a>

### [`004ced48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ced48.md) → [`004f1be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1be0.md) _ZN5Botan14Serialized_RNGC1Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 73.58% / 新版 73.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f1c14",
      "incomplete_value": true,
      "site": "004f1c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ced7c",
      "incomplete_value": true,
      "site": "004ced84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f1c50",
      "incomplete_value": true,
      "site": "004f1c5c",
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cedb8",
      "incomplete_value": true,
      "site": "004cedc4",
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
                "const:2b1000:8"
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f1c4c",
      "incomplete_value": true,
      "site": "004f1c60",
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
      "definition_site": "004cedb4",
      "incomplete_value": true,
      "site": "004cedc8",
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
      "004f1c04",
      "READ",
      [
        "storage",
        "00c1b228",
        null,
        "pointer"
      ]
    ],
    [
      "004f1c1c",
      "DATA",
      [
        "storage",
        "00bea010",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "004f1c4c",
      "READ",
      [
        "storage",
        "002aa61f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f1c04",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "004f1c1c",
      "DATA",
      [
        "storage",
        "00c66bd0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "004f1c4c",
      "READ",
      [
        "storage",
        "002bb39b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cee14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ced48.md#insn-004cee14) · [`004ced60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ced48.md#insn-004ced60) · [`004ced6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ced48.md#insn-004ced6c)
- 新版 `004f1cac`（命令位置の公開資料なし） · `004f1bf8`（命令位置の公開資料なし） · `004f1c04`（命令位置の公開資料なし）

~~~diff
- 004cee14 ["INT_ADD", "register:40f0:8", ["const:4cee14:8", "const:4:8"]]
- 004cee14 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f1cac ["INT_ADD", "register:40f0:8", ["const:4f1cac:8", "const:4:8"]]
+ 004f1cac ["CALL", null, ["callee:00c57b10:8"]]
- 004cee14 bytes ab301c94
+ 004f1cac bytes 99971d94
- 004ced60 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004f1bf8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004ced60 bytes 683a00b0
+ 004f1bf8 bytes 483d00b0
- 004ced6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
- 004ced6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f1c04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
+ 004f1c04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ced6c bytes 081541f9
+ 004f1c04 bytes 080d46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff4a2e2659690c10c57e357efbec31bf"></a>

### [`004cef80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cef80.md) → [`004f1e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e18.md) _ZNK5Botan13RSA_PublicKey18estimated_strengthEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5f0.md) [`00bdc860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc860.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004f1e78",
      "incomplete_value": true,
      "site": "004f1e84",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cefe0",
      "incomplete_value": true,
      "site": "004cefec",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
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
      "004f1e38",
      "READ",
      [
        "storage",
        "002b2c08",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1e64",
      "READ",
      [
        "storage",
        "002b27c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1e70",
      "READ",
      [
        "storage",
        "002b2c38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004f1e38",
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1e64",
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1e70",
      "READ",
      [
        "storage",
        "002c4348",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cef94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cef80.md#insn-004cef94) · [`004cef9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cef80.md#insn-004cef9c) · [`004cefa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004cef80.md#insn-004cefa0)
- 新版 `004f1e2c`（命令位置の公開資料なし） · `004f1e34`（命令位置の公開資料なし） · `004f1e38`（命令位置の公開資料なし）

~~~diff
- 004cef94 ["COPY", "register:0:8", ["register:4040:8"]]
- 004cef94 ["INT_ADD", "register:40f0:8", ["const:4cef94:8", "const:4:8"]]
- 004cef94 ["CALLIND", null, ["register:0:8"]]
+ 004f1e2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f1e2c ["INT_ADD", "register:40f0:8", ["const:4f1e2c:8", "const:4:8"]]
+ 004f1e2c ["CALLIND", null, ["register:0:8"]]
- 004cef94 bytes 00013fd6
+ 004f1e2c bytes 00013fd6
- 004cef9c ["COPY", "register:4040:8", ["const:2b2000:8"]]
+ 004f1e34 ["COPY", "register:4040:8", ["const:2c4000:8"]]
- 004cef9c bytes 28efff90
+ 004f1e34 bytes 88eefff0
- 004cefa0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
- 004cefa0 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
- 004cefa0 ["COPY", "register:5128:8", ["const:0:8"]]
- 004cefa0 ["COPY", "register:5130:8", ["const:0:8"]]
+ 004f1e38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004f1e38 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f1e38 ["COPY", "register:5128:8", ["const:0:8"]]
+ 004f1e38 ["COPY", "register:5130:8", ["const:0:8"]]
- 004cefa0 bytes 090546fd
+ 004f1e38 bytes 098d41fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1710c09c893dceea4eff2f36075dd8bc"></a>

### [`004ceff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ceff0.md) → [`004f1e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e88.md) _ZTv0_n40_NK5Botan13RSA_PublicKey18estimated_strengthEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5f0.md) [`00bdc860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc860.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004f1ef4",
      "incomplete_value": true,
      "site": "004f1f00",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cf05c",
      "incomplete_value": true,
      "site": "004cf068",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
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
      "004f1eb4",
      "READ",
      [
        "storage",
        "002b2c08",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1ee0",
      "READ",
      [
        "storage",
        "002b27c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1eec",
      "READ",
      [
        "storage",
        "002b2c38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004f1eb4",
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1ee0",
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1eec",
      "READ",
      [
        "storage",
        "002c4348",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cf010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ceff0.md#insn-004cf010) · [`004cf018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ceff0.md#insn-004cf018) · [`004cf01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ceff0.md#insn-004cf01c)
- 新版 `004f1ea8`（命令位置の公開資料なし） · `004f1eb0`（命令位置の公開資料なし） · `004f1eb4`（命令位置の公開資料なし）

~~~diff
- 004cf010 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cf010 ["INT_ADD", "register:40f0:8", ["const:4cf010:8", "const:4:8"]]
- 004cf010 ["CALLIND", null, ["register:0:8"]]
+ 004f1ea8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f1ea8 ["INT_ADD", "register:40f0:8", ["const:4f1ea8:8", "const:4:8"]]
+ 004f1ea8 ["CALLIND", null, ["register:0:8"]]
- 004cf010 bytes 20013fd6
+ 004f1ea8 bytes 20013fd6
- 004cf018 ["COPY", "register:4040:8", ["const:2b2000:8"]]
+ 004f1eb0 ["COPY", "register:4040:8", ["const:2c4000:8"]]
- 004cf018 bytes 08effff0
+ 004f1eb0 bytes 88eefff0
- 004cf01c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
- 004cf01c ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
- 004cf01c ["COPY", "register:5128:8", ["const:0:8"]]
- 004cf01c ["COPY", "register:5130:8", ["const:0:8"]]
+ 004f1eb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 004f1eb4 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f1eb4 ["COPY", "register:5128:8", ["const:0:8"]]
+ 004f1eb4 ["COPY", "register:5130:8", ["const:0:8"]]
- 004cf01c bytes 090546fd
+ 004f1eb4 bytes 098d41fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5796d17a5c92d3b1eb90ebff1e2da201"></a>

### [`004cf06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf06c.md) → [`004f1f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1f04.md) _ZNK5Botan13RSA_PublicKey20algorithm_identifierEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59320.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

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
      "site": "004f1f4c",
      "value": [
        "leaf",
        "ram:c59320:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cf0b4",
      "value": [
        "leaf",
        "ram:bdc8d0:8"
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
      "004f1f4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc8d0"
      ]
    ]
  ],
  "added": [
    [
      "004f1f4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59320"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cf0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf06c.md#insn-004cf0b4) · [`004cf0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf06c.md#insn-004cf0a4) · [`004cf0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf06c.md#insn-004cf0c4)
- 新版 `004f1f4c`（命令位置の公開資料なし） · `004f1f3c`（命令位置の公開資料なし） · `004f1f5c`（命令位置の公開資料なし）

~~~diff
- 004cf0b4 ["INT_ADD", "register:40f0:8", ["const:4cf0b4:8", "const:4:8"]]
- 004cf0b4 ["CALL", null, ["ram:bdc8d0:8"]]
+ 004f1f4c ["INT_ADD", "register:40f0:8", ["const:4f1f4c:8", "const:4:8"]]
+ 004f1f4c ["CALL", null, ["ram:c59320:8"]]
- 004cf0b4 bytes 07361c94
+ 004f1f4c bytes f59c1d94
- 004cf0a4 ["COPY", "register:0:8", ["register:4050:8"]]
- 004cf0a4 ["INT_ADD", "register:40f0:8", ["const:4cf0a4:8", "const:4:8"]]
- 004cf0a4 ["CALLIND", null, ["register:0:8"]]
+ 004f1f3c ["COPY", "register:0:8", ["register:4050:8"]]
+ 004f1f3c ["INT_ADD", "register:40f0:8", ["const:4f1f3c:8", "const:4:8"]]
+ 004f1f3c ["CALLIND", null, ["register:0:8"]]
- 004cf0a4 bytes 40013fd6
+ 004f1f3c bytes 40013fd6
- 004cf0c4 ["INT_ADD", "register:40f0:8", ["const:4cf0c4:8", "const:4:8"]]
- 004cf0c4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004f1f5c ["INT_ADD", "register:40f0:8", ["const:4f1f5c:8", "const:4:8"]]
+ 004f1f5c ["CALL", null, ["callee:00c57ab0:8"]]
- 004cf0c4 bytes e72f1c94
+ 004f1f5c bytes d5961d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34410c77e192ae4799deb3e167b9fc4d"></a>

### [`004cf11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf11c.md) → [`004f1fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1fb4.md) _ZTv0_n72_NK5Botan13RSA_PublicKey20algorithm_identifierEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59320.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

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
      "site": "004f2008",
      "value": [
        "leaf",
        "ram:c59320:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cf170",
      "value": [
        "leaf",
        "ram:bdc8d0:8"
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
      "004f2008",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc8d0"
      ]
    ]
  ],
  "added": [
    [
      "004f2008",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59320"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cf170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf11c.md#insn-004cf170) · [`004cf160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf11c.md#insn-004cf160) · [`004cf180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf11c.md#insn-004cf180)
- 新版 `004f2008`（命令位置の公開資料なし） · `004f1ff8`（命令位置の公開資料なし） · `004f2018`（命令位置の公開資料なし）

~~~diff
- 004cf170 ["INT_ADD", "register:40f0:8", ["const:4cf170:8", "const:4:8"]]
- 004cf170 ["CALL", null, ["ram:bdc8d0:8"]]
+ 004f2008 ["INT_ADD", "register:40f0:8", ["const:4f2008:8", "const:4:8"]]
+ 004f2008 ["CALL", null, ["ram:c59320:8"]]
- 004cf170 bytes d8351c94
+ 004f2008 bytes c69c1d94
- 004cf160 ["COPY", "register:0:8", ["register:4058:8"]]
- 004cf160 ["INT_ADD", "register:40f0:8", ["const:4cf160:8", "const:4:8"]]
- 004cf160 ["CALLIND", null, ["register:0:8"]]
+ 004f1ff8 ["COPY", "register:0:8", ["register:4058:8"]]
+ 004f1ff8 ["INT_ADD", "register:40f0:8", ["const:4f1ff8:8", "const:4:8"]]
+ 004f1ff8 ["CALLIND", null, ["register:0:8"]]
- 004cf160 bytes 60013fd6
+ 004f1ff8 bytes 60013fd6
- 004cf180 ["INT_ADD", "register:40f0:8", ["const:4cf180:8", "const:4:8"]]
- 004cf180 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004f2018 ["INT_ADD", "register:40f0:8", ["const:4f2018:8", "const:4:8"]]
+ 004f2018 ["CALL", null, ["callee:00c57ab0:8"]]
- 004cf180 bytes b82f1c94
+ 004f2018 bytes a6961d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cee9f11c09cf3f527180b63a741ff0d2"></a>

### [`004cf328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf328.md) → [`004f21c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f21c0.md) _ZN5Botan13RSA_PublicKeyC2ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) [`00bdb8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8c0.md) [`00bdba30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba30.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) [`00c58310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58310.md) [`00c58480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58480.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.25% / 新版 94.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004f2220",
      "value": [
        "leaf",
        "ram:c58480:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cf388",
      "value": [
        "leaf",
        "ram:bdba30:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f22a4",
      "incomplete_value": true,
      "site": "004f22a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cf40c",
      "incomplete_value": true,
      "site": "004cf40c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f22e8",
      "incomplete_value": true,
      "site": "004f22e8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cf450",
      "incomplete_value": true,
      "site": "004cf450",
      "value": [
        "LOAD",
        "8",
        [
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
      "004f2220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba30"
      ]
    ],
    [
      "004f2294",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f22d8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f2220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58480"
      ]
    ],
    [
      "004f2294",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f22d8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cf388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf328.md#insn-004cf388) · [`004cf40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf328.md#insn-004cf40c) · [`004cf450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf328.md#insn-004cf450)
- 新版 `004f2220`（命令位置の公開資料なし） · `004f22a4`（命令位置の公開資料なし） · `004f22e8`（命令位置の公開資料なし）

~~~diff
- 004cf388 ["INT_ADD", "register:40f0:8", ["const:4cf388:8", "const:4:8"]]
- 004cf388 ["CALL", null, ["ram:bdba30:8"]]
+ 004f2220 ["INT_ADD", "register:40f0:8", ["const:4f2220:8", "const:4:8"]]
+ 004f2220 ["CALL", null, ["ram:c58480:8"]]
- 004cf388 bytes aa311c94
+ 004f2220 bytes 98981d94
- 004cf40c ["COPY", "register:0:8", ["register:4048:8"]]
- 004cf40c ["INT_ADD", "register:40f0:8", ["const:4cf40c:8", "const:4:8"]]
- 004cf40c ["CALLIND", null, ["register:0:8"]]
+ 004f22a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f22a4 ["INT_ADD", "register:40f0:8", ["const:4f22a4:8", "const:4:8"]]
+ 004f22a4 ["CALLIND", null, ["register:0:8"]]
- 004cf40c bytes 20013fd6
+ 004f22a4 bytes 20013fd6
- 004cf450 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cf450 ["INT_ADD", "register:40f0:8", ["const:4cf450:8", "const:4:8"]]
- 004cf450 ["CALLIND", null, ["register:0:8"]]
+ 004f22e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f22e8 ["INT_ADD", "register:40f0:8", ["const:4f22e8:8", "const:4:8"]]
+ 004f22e8 ["CALLIND", null, ["register:0:8"]]
- 004cf450 bytes 20013fd6
+ 004f22e8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-033d984ae9807ca4895aec0cad6a95fd"></a>

### [`004cf634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf634.md) → [`004f24cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f24cc.md) _ZNK5Botan14RSA_PrivateKey16private_key_bitsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f2558",
      "incomplete_value": true,
      "site": "004f2558",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cf6c0",
      "incomplete_value": true,
      "site": "004cf6c0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f2678",
      "incomplete_value": true,
      "site": "004f2678",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cf7e0",
      "incomplete_value": true,
      "site": "004cf7e0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 17,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f2548",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f2668",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f2548",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f2668",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cf6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf634.md#insn-004cf6c0) · [`004cf7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf634.md#insn-004cf7e0) · [`004cf678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf634.md#insn-004cf678)
- 新版 `004f2558`（命令位置の公開資料なし） · `004f2678`（命令位置の公開資料なし） · `004f2510`（命令位置の公開資料なし）

~~~diff
- 004cf6c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cf6c0 ["INT_ADD", "register:40f0:8", ["const:4cf6c0:8", "const:4:8"]]
- 004cf6c0 ["CALLIND", null, ["register:0:8"]]
+ 004f2558 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2558 ["INT_ADD", "register:40f0:8", ["const:4f2558:8", "const:4:8"]]
+ 004f2558 ["CALLIND", null, ["register:0:8"]]
- 004cf6c0 bytes 20013fd6
+ 004f2558 bytes 20013fd6
- 004cf7e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cf7e0 ["INT_ADD", "register:40f0:8", ["const:4cf7e0:8", "const:4:8"]]
- 004cf7e0 ["CALLIND", null, ["register:0:8"]]
+ 004f2678 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2678 ["INT_ADD", "register:40f0:8", ["const:4f2678:8", "const:4:8"]]
+ 004f2678 ["CALLIND", null, ["register:0:8"]]
- 004cf7e0 bytes 20013fd6
+ 004f2678 bytes 20013fd6
- 004cf678 ["INT_ADD", "register:40f0:8", ["const:4cf678:8", "const:4:8"]]
- 004cf678 ["CALL", null, ["callee:00c582b0:8"]]
+ 004f2510 ["INT_ADD", "register:40f0:8", ["const:4f2510:8", "const:4:8"]]
+ 004f2510 ["CALL", null, ["callee:00c582b0:8"]]
- 004cf678 bytes 7a301c94
+ 004f2510 bytes 68971d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e01f000cb720be9c6e6735c1addf17bb"></a>

### [`004cf854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf854.md) → [`004f26ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f26ec.md) _ZN5Botan14RSA_PrivateKeyC2ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.81% / 新版 93.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f2828",
      "incomplete_value": true,
      "site": "004f283c",
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
                "const:260:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cf990",
      "incomplete_value": true,
      "site": "004cf9a4",
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
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:b80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f2824",
      "incomplete_value": true,
      "site": "004f2840",
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
                "const:d96:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cf98c",
      "incomplete_value": true,
      "site": "004cf9a8",
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
                "const:529:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f2824",
      "incomplete_value": true,
      "site": "004f2840",
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
      "definition_site": "004cf98c",
      "incomplete_value": true,
      "site": "004cf9a8",
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
      "004f27f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba40"
      ]
    ],
    [
      "004f2824",
      "READ",
      [
        "storage",
        "002a4529",
        null,
        "string"
      ]
    ],
    [
      "004f2824",
      "READ",
      [
        "storage",
        "002a4539",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f27f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58490"
      ]
    ],
    [
      "004f2824",
      "READ",
      [
        "storage",
        "002b4d96",
        null,
        "string"
      ]
    ],
    [
      "004f2824",
      "READ",
      [
        "storage",
        "002b4da6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cf960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf854.md#insn-004cf960) · [`004cfa94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf854.md#insn-004cfa94) · [`004cfad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cf854.md#insn-004cfad8)
- 新版 `004f27f8`（命令位置の公開資料なし） · `004f292c`（命令位置の公開資料なし） · `004f2970`（命令位置の公開資料なし）

~~~diff
- 004cf960 ["INT_ADD", "register:40f0:8", ["const:4cf960:8", "const:4:8"]]
- 004cf960 ["CALL", null, ["ram:bdba40:8"]]
+ 004f27f8 ["INT_ADD", "register:40f0:8", ["const:4f27f8:8", "const:4:8"]]
+ 004f27f8 ["CALL", null, ["ram:c58490:8"]]
- 004cf960 bytes 38301c94
+ 004f27f8 bytes 26971d94
- 004cfa94 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cfa94 ["INT_ADD", "register:40f0:8", ["const:4cfa94:8", "const:4:8"]]
- 004cfa94 ["CALLIND", null, ["register:0:8"]]
+ 004f292c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f292c ["INT_ADD", "register:40f0:8", ["const:4f292c:8", "const:4:8"]]
+ 004f292c ["CALLIND", null, ["register:0:8"]]
- 004cfa94 bytes 20013fd6
+ 004f292c bytes 20013fd6
- 004cfad8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cfad8 ["INT_ADD", "register:40f0:8", ["const:4cfad8:8", "const:4:8"]]
- 004cfad8 ["CALLIND", null, ["register:0:8"]]
+ 004f2970 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2970 ["INT_ADD", "register:40f0:8", ["const:4f2970:8", "const:4:8"]]
+ 004f2970 ["CALLIND", null, ["register:0:8"]]
- 004cfad8 bytes 20013fd6
+ 004f2970 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a231f3b01626d84ad15ebc5169af7102"></a>

### [`004cfc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cfc08.md) → [`004f2aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2aa0.md) FUN_004f2aa0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f2aec",
      "incomplete_value": true,
      "site": "004f2aec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cfc54",
      "incomplete_value": true,
      "site": "004cfc54",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f2b18",
      "incomplete_value": true,
      "site": "004f2b18",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cfc80",
      "incomplete_value": true,
      "site": "004cfc80",
      "value": [
        "LOAD",
        "8",
        [
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
      "004f2adc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f2b08",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f2adc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f2b08",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cfc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cfc08.md#insn-004cfc54) · [`004cfc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cfc08.md#insn-004cfc80) · [`004cfc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cfc08.md#insn-004cfc24)
- 新版 `004f2aec`（命令位置の公開資料なし） · `004f2b18`（命令位置の公開資料なし） · `004f2abc`（命令位置の公開資料なし）

~~~diff
- 004cfc54 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cfc54 ["INT_ADD", "register:40f0:8", ["const:4cfc54:8", "const:4:8"]]
- 004cfc54 ["CALLIND", null, ["register:0:8"]]
+ 004f2aec ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2aec ["INT_ADD", "register:40f0:8", ["const:4f2aec:8", "const:4:8"]]
+ 004f2aec ["CALLIND", null, ["register:0:8"]]
- 004cfc54 bytes 20013fd6
+ 004f2aec bytes 20013fd6
- 004cfc80 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cfc80 ["INT_ADD", "register:40f0:8", ["const:4cfc80:8", "const:4:8"]]
- 004cfc80 ["CALLIND", null, ["register:0:8"]]
+ 004f2b18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2b18 ["INT_ADD", "register:40f0:8", ["const:4f2b18:8", "const:4:8"]]
+ 004f2b18 ["CALLIND", null, ["register:0:8"]]
- 004cfc80 bytes 20013fd6
+ 004f2b18 bytes 20013fd6
- 004cfc24 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 004f2abc ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 004cfc24 bytes d53800f0
+ 004f2abc bytes b53b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb47b737883dbf2c6011827b20fd2d28"></a>

### [`004cfcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cfcb0.md) → [`004f2b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2b48.md) _ZN5Botan14RSA_PrivateKeyC2ERKNS_6BigIntES3_S3_S3_S3_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.99% / 新版 91.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004f2c08",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cfd70",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
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
      "site": "004f2c14",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cfd7c",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004f2c20",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cfd88",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
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
      "004f2c08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004f2c14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004f2c20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ]
  ],
  "added": [
    [
      "004f2c08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004f2c14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004f2c20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cfd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cfcb0.md#insn-004cfd70) · [`004cfd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cfcb0.md#insn-004cfd7c) · [`004cfd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cf/004cfcb0.md#insn-004cfd88)
- 新版 `004f2c08`（命令位置の公開資料なし） · `004f2c14`（命令位置の公開資料なし） · `004f2c20`（命令位置の公開資料なし）

~~~diff
- 004cfd70 ["INT_ADD", "register:40f0:8", ["const:4cfd70:8", "const:4:8"]]
- 004cfd70 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004f2c08 ["INT_ADD", "register:40f0:8", ["const:4f2c08:8", "const:4:8"]]
+ 004f2c08 ["CALL", null, ["ram:c58740:8"]]
- 004cfd70 bytes e02f1c94
+ 004f2c08 bytes ce961d94
- 004cfd7c ["INT_ADD", "register:40f0:8", ["const:4cfd7c:8", "const:4:8"]]
- 004cfd7c ["CALL", null, ["ram:bdbcf0:8"]]
+ 004f2c14 ["INT_ADD", "register:40f0:8", ["const:4f2c14:8", "const:4:8"]]
+ 004f2c14 ["CALL", null, ["ram:c58740:8"]]
- 004cfd7c bytes dd2f1c94
+ 004f2c14 bytes cb961d94
- 004cfd88 ["INT_ADD", "register:40f0:8", ["const:4cfd88:8", "const:4:8"]]
- 004cfd88 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004f2c20 ["INT_ADD", "register:40f0:8", ["const:4f2c20:8", "const:4:8"]]
+ 004f2c20 ["CALL", null, ["ram:c58740:8"]]
- 004cfd88 bytes da2f1c94
+ 004f2c20 bytes c8961d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66e06aaea26d129bb8e5e932711f892f"></a>

### [`004d04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d04c0.md) → [`004f3358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3358.md) _ZN5Botan14RSA_PrivateKeyC1ERKNS_6BigIntES3_S3_S3_S3_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.54% / 新版 90.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 18件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f33c4",
      "incomplete_value": true,
      "site": "004f33c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d052c",
      "incomplete_value": true,
      "site": "004d052c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1a0:8"
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
      "definition_site": "004f33bc",
      "incomplete_value": true,
      "site": "004f33d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004d0524",
      "incomplete_value": true,
      "site": "004d0540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004f33e4",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d054c",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
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
      "004f3388",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "004f33c4",
      "DATA",
      [
        "storage",
        "00bea2f8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004f33d8",
      "DATA",
      [
        "storage",
        "00bea1d8",
        null,
        "undefined1[528]"
      ]
    ]
  ],
  "added": [
    [
      "004f3388",
      "READ",
      [
        "storage",
        "00c9abe0",
        null,
        "pointer"
      ]
    ],
    [
      "004f33c4",
      "DATA",
      [
        "storage",
        "00c66eb8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004f33d8",
      "DATA",
      [
        "storage",
        "00c66d98",
        null,
        "undefined1[528]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d054c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d04c0.md#insn-004d054c) · [`004d0558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d04c0.md#insn-004d0558) · [`004d0564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d04c0.md#insn-004d0564)
- 新版 `004f33e4`（命令位置の公開資料なし） · `004f33f0`（命令位置の公開資料なし） · `004f33fc`（命令位置の公開資料なし）

~~~diff
- 004d054c ["INT_ADD", "register:40f0:8", ["const:4d054c:8", "const:4:8"]]
- 004d054c ["CALL", null, ["ram:bdbcf0:8"]]
+ 004f33e4 ["INT_ADD", "register:40f0:8", ["const:4f33e4:8", "const:4:8"]]
+ 004f33e4 ["CALL", null, ["ram:c58740:8"]]
- 004d054c bytes e92d1c94
+ 004f33e4 bytes d7941d94
- 004d0558 ["INT_ADD", "register:40f0:8", ["const:4d0558:8", "const:4:8"]]
- 004d0558 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004f33f0 ["INT_ADD", "register:40f0:8", ["const:4f33f0:8", "const:4:8"]]
+ 004f33f0 ["CALL", null, ["ram:c58740:8"]]
- 004d0558 bytes e62d1c94
+ 004f33f0 bytes d4941d94
- 004d0564 ["INT_ADD", "register:40f0:8", ["const:4d0564:8", "const:4:8"]]
- 004d0564 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004f33fc ["INT_ADD", "register:40f0:8", ["const:4f33fc:8", "const:4:8"]]
+ 004f33fc ["CALL", null, ["ram:c58740:8"]]
- 004d0564 bytes e32d1c94
+ 004f33fc bytes d1941d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f42b5713f8b14602b9194aed49e2dfae"></a>

### [`004d0c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d0c9c.md) → [`004f3b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3b34.md) _ZN5Botan14RSA_PrivateKeyC2ERNS_21RandomNumberGeneratorEmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 17件 [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f3cd4",
      "incomplete_value": true,
      "site": "004f3cd4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
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
    "old": {
      "definition_site": "004d0e3c",
      "incomplete_value": true,
      "site": "004d0e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f3d78",
      "incomplete_value": true,
      "site": "004f3d78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
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
    "old": {
      "definition_site": "004d0ee0",
      "incomplete_value": true,
      "site": "004d0ee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f3e74",
      "incomplete_value": true,
      "site": "004f3e74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
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
    "old": {
      "definition_site": "004d0fdc",
      "incomplete_value": true,
      "site": "004d0fdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004f3cc4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f3d68",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f3e64",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f3cc4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f3d68",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f3e64",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d0e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d0c9c.md#insn-004d0e3c) · [`004d0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d0c9c.md#insn-004d0ee0) · [`004d0fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d0/004d0c9c.md#insn-004d0fdc)
- 新版 `004f3cd4`（命令位置の公開資料なし） · `004f3d78`（命令位置の公開資料なし） · `004f3e74`（命令位置の公開資料なし）

~~~diff
- 004d0e3c ["COPY", "register:0:8", ["register:4048:8"]]
- 004d0e3c ["INT_ADD", "register:40f0:8", ["const:4d0e3c:8", "const:4:8"]]
- 004d0e3c ["CALLIND", null, ["register:0:8"]]
+ 004f3cd4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f3cd4 ["INT_ADD", "register:40f0:8", ["const:4f3cd4:8", "const:4:8"]]
+ 004f3cd4 ["CALLIND", null, ["register:0:8"]]
- 004d0e3c bytes 20013fd6
+ 004f3cd4 bytes 20013fd6
- 004d0ee0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004d0ee0 ["INT_ADD", "register:40f0:8", ["const:4d0ee0:8", "const:4:8"]]
- 004d0ee0 ["CALLIND", null, ["register:0:8"]]
+ 004f3d78 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f3d78 ["INT_ADD", "register:40f0:8", ["const:4f3d78:8", "const:4:8"]]
+ 004f3d78 ["CALLIND", null, ["register:0:8"]]
- 004d0ee0 bytes 20013fd6
+ 004f3d78 bytes 20013fd6
- 004d0fdc ["COPY", "register:0:8", ["register:4048:8"]]
- 004d0fdc ["INT_ADD", "register:40f0:8", ["const:4d0fdc:8", "const:4:8"]]
- 004d0fdc ["CALLIND", null, ["register:0:8"]]
+ 004f3e74 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f3e74 ["INT_ADD", "register:40f0:8", ["const:4f3e74:8", "const:4:8"]]
+ 004f3e74 ["CALLIND", null, ["register:0:8"]]
- 004d0fdc bytes 20013fd6
+ 004f3e74 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b027fd7b75dcd9acc0405cf6a7fd092"></a>

### [`004d1904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d1/004d1904.md) → [`004f479c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f4/004f479c.md) _ZNK5Botan14RSA_PrivateKey9check_keyERNS_21RandomNumberGeneratorEb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc900.md) · 呼出先 13件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md)
- 新版 呼出元 1件 [`00c59350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59350.md) · 呼出先 13件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.60% / 新版 95.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 2件

アドレスに依存する影響 `call_target` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f4e70",
      "incomplete_value": true,
      "site": "004f4e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b9d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d1fd8",
      "incomplete_value": true,
      "site": "004d1fd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5e3:8"
              ]
            ]
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
      "definition_site": "004f4e74",
      "incomplete_value": true,
      "site": "004f4e74",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004d1fdc",
      "incomplete_value": true,
      "site": "004d1fdc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f48d4",
      "incomplete_value": true,
      "site": "004f48d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d1a3c",
      "incomplete_value": true,
      "site": "004d1a3c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 12,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f48c4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f48f0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f491c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f48c4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f48f0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f491c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d1a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d1/004d1904.md#insn-004d1a3c) · [`004d1a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d1/004d1904.md#insn-004d1a68) · [`004d1a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d1/004d1904.md#insn-004d1a94)
- 新版 `004f48d4`（命令位置の公開資料なし） · `004f4900`（命令位置の公開資料なし） · `004f492c`（命令位置の公開資料なし）

~~~diff
- 004d1a3c ["COPY", "register:0:8", ["register:4048:8"]]
- 004d1a3c ["INT_ADD", "register:40f0:8", ["const:4d1a3c:8", "const:4:8"]]
- 004d1a3c ["CALLIND", null, ["register:0:8"]]
+ 004f48d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f48d4 ["INT_ADD", "register:40f0:8", ["const:4f48d4:8", "const:4:8"]]
+ 004f48d4 ["CALLIND", null, ["register:0:8"]]
- 004d1a3c bytes 20013fd6
+ 004f48d4 bytes 20013fd6
- 004d1a68 ["COPY", "register:0:8", ["register:4048:8"]]
- 004d1a68 ["INT_ADD", "register:40f0:8", ["const:4d1a68:8", "const:4:8"]]
- 004d1a68 ["CALLIND", null, ["register:0:8"]]
+ 004f4900 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f4900 ["INT_ADD", "register:40f0:8", ["const:4f4900:8", "const:4:8"]]
+ 004f4900 ["CALLIND", null, ["register:0:8"]]
- 004d1a68 bytes 20013fd6
+ 004f4900 bytes 20013fd6
- 004d1a94 ["COPY", "register:0:8", ["register:4048:8"]]
- 004d1a94 ["INT_ADD", "register:40f0:8", ["const:4d1a94:8", "const:4:8"]]
- 004d1a94 ["CALLIND", null, ["register:0:8"]]
+ 004f492c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f492c ["INT_ADD", "register:40f0:8", ["const:4f492c:8", "const:4:8"]]
+ 004f492c ["CALLIND", null, ["register:0:8"]]
- 004d1a94 bytes 20013fd6
+ 004f492c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dddbba60aa0f51c2f37be1a1edb6875"></a>

### [`004d21d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d21d0.md) → [`004f5068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5068.md) _ZNK5Botan13RSA_PublicKey20create_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorI

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc910.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md)
- 新版 呼出元 1件 [`00c59360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59360.md) · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f50fc",
      "incomplete_value": true,
      "site": "004f5104",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2264",
      "incomplete_value": true,
      "site": "004d226c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
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
      "definition_site": "004f50f8",
      "incomplete_value": false,
      "site": "004f5104",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004d2260",
      "incomplete_value": false,
      "site": "004d226c",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004f5140",
      "value": [
        "leaf",
        "ram:c59370:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d22a8",
      "value": [
        "leaf",
        "ram:bdc920:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f50f8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004f50fc",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f50fc",
      "PARAM",
      [
        "storage",
        "00be9a58",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004f50f8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f50fc",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      "004f50fc",
      "PARAM",
      [
        "storage",
        "00c66618",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d21d0.md#insn-004d226c) · [`004d22a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d21d0.md#insn-004d22a8) · [`004d22d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d21d0.md#insn-004d22d4)
- 新版 `004f5104`（命令位置の公開資料なし） · `004f5140`（命令位置の公開資料なし） · `004f516c`（命令位置の公開資料なし）

~~~diff
- 004d226c ["INT_ADD", "register:40f0:8", ["const:4d226c:8", "const:4:8"]]
- 004d226c ["CALL", null, ["callee:00c57b10:8"]]
+ 004f5104 ["INT_ADD", "register:40f0:8", ["const:4f5104:8", "const:4:8"]]
+ 004f5104 ["CALL", null, ["callee:00c57b10:8"]]
- 004d226c bytes 95231c94
+ 004f5104 bytes 838a1d94
- 004d22a8 ["INT_ADD", "register:40f0:8", ["const:4d22a8:8", "const:4:8"]]
- 004d22a8 ["CALL", null, ["ram:bdc920:8"]]
+ 004f5140 ["INT_ADD", "register:40f0:8", ["const:4f5140:8", "const:4:8"]]
+ 004f5140 ["CALL", null, ["ram:c59370:8"]]
- 004d22a8 bytes 9e291c94
+ 004f5140 bytes 8c901d94
- 004d22d4 ["INT_ADD", "register:40f0:8", ["const:4d22d4:8", "const:4:8"]]
- 004d22d4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f516c ["INT_ADD", "register:40f0:8", ["const:4f516c:8", "const:4:8"]]
+ 004f516c ["CALL", null, ["callee:00c57b10:8"]]
- 004d22d4 bytes 7b231c94
+ 004f516c bytes 698a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-512889bcbe87c7fe514b9da8af729f92"></a>

### [`004d2348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2348.md) → [`004f51e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f51e0.md) _ZNK5Botan13RSA_PublicKey24create_kem_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9alloca

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc930.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c59380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59380.md) · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.77% / 新版 92.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004f5264",
      "incomplete_value": false,
      "site": "004f5264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d23cc",
      "incomplete_value": false,
      "site": "004d23cc",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004f528c",
      "incomplete_value": false,
      "site": "004f5294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d23f4",
      "incomplete_value": false,
      "site": "004d23fc",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004f52f8",
      "value": [
        "leaf",
        "ram:c59370:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d2460",
      "value": [
        "leaf",
        "ram:bdc920:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f5264",
      "DATA",
      [
        "storage",
        "00be9f58",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5294",
      "DATA",
      [
        "storage",
        "00becf28",
        null,
        "undefined *"
      ]
    ],
    [
      "004f52f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc920"
      ]
    ]
  ],
  "added": [
    [
      "004f5264",
      "DATA",
      [
        "storage",
        "00c66b18",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5294",
      "DATA",
      [
        "storage",
        "00c69ae8",
        null,
        "undefined *"
      ]
    ],
    [
      "004f52f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59370"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d2460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2348.md#insn-004d2460) · [`004d248c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2348.md#insn-004d248c) · [`004d23bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2348.md#insn-004d23bc)
- 新版 `004f52f8`（命令位置の公開資料なし） · `004f5324`（命令位置の公開資料なし） · `004f5254`（命令位置の公開資料なし）

~~~diff
- 004d2460 ["INT_ADD", "register:40f0:8", ["const:4d2460:8", "const:4:8"]]
- 004d2460 ["CALL", null, ["ram:bdc920:8"]]
+ 004f52f8 ["INT_ADD", "register:40f0:8", ["const:4f52f8:8", "const:4:8"]]
+ 004f52f8 ["CALL", null, ["ram:c59370:8"]]
- 004d2460 bytes 30291c94
+ 004f52f8 bytes 1e901d94
- 004d248c ["INT_ADD", "register:40f0:8", ["const:4d248c:8", "const:4:8"]]
- 004d248c ["CALL", null, ["callee:00c57b10:8"]]
+ 004f5324 ["INT_ADD", "register:40f0:8", ["const:4f5324:8", "const:4:8"]]
+ 004f5324 ["CALL", null, ["callee:00c57b10:8"]]
- 004d248c bytes 0d231c94
+ 004f5324 bytes fb891d94
- 004d23bc ["INT_ADD", "register:40f0:8", ["const:4d23bc:8", "const:4:8"]]
- 004d23bc ["CALL", null, ["callee:00c57a90:8"]]
+ 004f5254 ["INT_ADD", "register:40f0:8", ["const:4f5254:8", "const:4:8"]]
+ 004f5254 ["CALL", null, ["callee:00c57a90:8"]]
- 004d23bc bytes 21231c94
+ 004f5254 bytes 0f8a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acf9408d88848bde243db07c37c49cb9"></a>

### [`004d2528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2528.md) → [`004f53c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f53c0.md) _ZNK5Botan13RSA_PublicKey22create_verification_opERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc940.md) · 呼出先 8件 [`004c8590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8590.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c59390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59390.md) · 呼出先 8件 [`004eb428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb428.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004f5460",
      "incomplete_value": false,
      "site": "004f5468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d25c8",
      "incomplete_value": false,
      "site": "004d25d0",
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
            "const:f90:8"
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
      "site": "004f54cc",
      "value": [
        "leaf",
        "ram:c59370:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d2634",
      "value": [
        "leaf",
        "ram:bdc920:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f54ec",
      "incomplete_value": true,
      "site": "004f54f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2654",
      "incomplete_value": true,
      "site": "004d2660",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:230:8"
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
      "004f5468",
      "DATA",
      [
        "storage",
        "00becf90",
        null,
        "undefined *"
      ]
    ],
    [
      "004f54cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc920"
      ]
    ],
    [
      "004f54e8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f5468",
      "DATA",
      [
        "storage",
        "00c69b50",
        null,
        "undefined *"
      ]
    ],
    [
      "004f54cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59370"
      ]
    ],
    [
      "004f54e8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d2634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2528.md#insn-004d2634) · [`004d2660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2528.md#insn-004d2660) · [`004d259c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2528.md#insn-004d259c)
- 新版 `004f54cc`（命令位置の公開資料なし） · `004f54f8`（命令位置の公開資料なし） · `004f5434`（命令位置の公開資料なし）

~~~diff
- 004d2634 ["INT_ADD", "register:40f0:8", ["const:4d2634:8", "const:4:8"]]
- 004d2634 ["CALL", null, ["ram:bdc920:8"]]
+ 004f54cc ["INT_ADD", "register:40f0:8", ["const:4f54cc:8", "const:4:8"]]
+ 004f54cc ["CALL", null, ["ram:c59370:8"]]
- 004d2634 bytes bb281c94
+ 004f54cc bytes a98f1d94
- 004d2660 ["INT_ADD", "register:40f0:8", ["const:4d2660:8", "const:4:8"]]
- 004d2660 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f54f8 ["INT_ADD", "register:40f0:8", ["const:4f54f8:8", "const:4:8"]]
+ 004f54f8 ["CALL", null, ["callee:00c57b10:8"]]
- 004d2660 bytes 98221c94
+ 004f54f8 bytes 86891d94
- 004d259c ["INT_ADD", "register:40f0:8", ["const:4d259c:8", "const:4:8"]]
- 004d259c ["CALL", null, ["callee:00c57a90:8"]]
+ 004f5434 ["INT_ADD", "register:40f0:8", ["const:4f5434:8", "const:4:8"]]
+ 004f5434 ["CALL", null, ["callee:00c57a90:8"]]
- 004d259c bytes a9221c94
+ 004f5434 bytes 97891d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b97dbff21b3e0c831d72d8a3880c0853"></a>

### [`004d26e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d26e0.md) → [`004f5578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5578.md) _ZNK5Botan14RSA_PrivateKey20create_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocator

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f5610",
      "incomplete_value": true,
      "site": "004f5618",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2778",
      "incomplete_value": true,
      "site": "004d2780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
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
      "definition_site": "004f560c",
      "incomplete_value": false,
      "site": "004f5618",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004d2774",
      "incomplete_value": false,
      "site": "004d2780",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004f5648",
      "value": [
        "leaf",
        "ram:c59370:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d27b0",
      "value": [
        "leaf",
        "ram:bdc920:8"
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
      "004f560c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004f5610",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f5610",
      "PARAM",
      [
        "storage",
        "00be9a58",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004f560c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f5610",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      "004f5610",
      "PARAM",
      [
        "storage",
        "00c66618",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d2780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d26e0.md#insn-004d2780) · [`004d27b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d26e0.md#insn-004d27b0) · [`004d27dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d26e0.md#insn-004d27dc)
- 新版 `004f5618`（命令位置の公開資料なし） · `004f5648`（命令位置の公開資料なし） · `004f5674`（命令位置の公開資料なし）

~~~diff
- 004d2780 ["INT_ADD", "register:40f0:8", ["const:4d2780:8", "const:4:8"]]
- 004d2780 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f5618 ["INT_ADD", "register:40f0:8", ["const:4f5618:8", "const:4:8"]]
+ 004f5618 ["CALL", null, ["callee:00c57b10:8"]]
- 004d2780 bytes 50221c94
+ 004f5618 bytes 3e891d94
- 004d27b0 ["INT_ADD", "register:40f0:8", ["const:4d27b0:8", "const:4:8"]]
- 004d27b0 ["CALL", null, ["ram:bdc920:8"]]
+ 004f5648 ["INT_ADD", "register:40f0:8", ["const:4f5648:8", "const:4:8"]]
+ 004f5648 ["CALL", null, ["ram:c59370:8"]]
- 004d27b0 bytes 5c281c94
+ 004f5648 bytes 4a8f1d94
- 004d27dc ["INT_ADD", "register:40f0:8", ["const:4d27dc:8", "const:4:8"]]
- 004d27dc ["CALL", null, ["callee:00c57b10:8"]]
+ 004f5674 ["INT_ADD", "register:40f0:8", ["const:4f5674:8", "const:4:8"]]
+ 004f5674 ["CALL", null, ["callee:00c57b10:8"]]
- 004d27dc bytes 39221c94
+ 004f5674 bytes 27891d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbcfe7763417501e2198a93402b48eca"></a>

### [`004d2830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2830.md) → [`004f56c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f56c8.md) _ZNK5Botan14RSA_PrivateKey24create_kem_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9alloc

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051483c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/0051483c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005376d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/005376d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.77% / 新版 92.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004f5754",
      "incomplete_value": false,
      "site": "004f5754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d28bc",
      "incomplete_value": false,
      "site": "004d28bc",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004f5778",
      "incomplete_value": false,
      "site": "004f5780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d28e0",
      "incomplete_value": false,
      "site": "004d28e8",
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
            "const:1f0:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004f57e0",
      "value": [
        "leaf",
        "ram:c59370:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d2948",
      "value": [
        "leaf",
        "ram:bdc920:8"
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
      "004f5754",
      "DATA",
      [
        "storage",
        "00be9f88",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5780",
      "DATA",
      [
        "storage",
        "00bed1f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004f57d4",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "byte[43]"
      ]
    ]
  ],
  "added": [
    [
      "004f5754",
      "DATA",
      [
        "storage",
        "00c66b48",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5780",
      "DATA",
      [
        "storage",
        "00c69db0",
        null,
        "undefined *"
      ]
    ],
    [
      "004f57d4",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d2948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2830.md#insn-004d2948) · [`004d2974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2830.md#insn-004d2974) · [`004d28ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2830.md#insn-004d28ac)
- 新版 `004f57e0`（命令位置の公開資料なし） · `004f580c`（命令位置の公開資料なし） · `004f5744`（命令位置の公開資料なし）

~~~diff
- 004d2948 ["INT_ADD", "register:40f0:8", ["const:4d2948:8", "const:4:8"]]
- 004d2948 ["CALL", null, ["ram:bdc920:8"]]
+ 004f57e0 ["INT_ADD", "register:40f0:8", ["const:4f57e0:8", "const:4:8"]]
+ 004f57e0 ["CALL", null, ["ram:c59370:8"]]
- 004d2948 bytes f6271c94
+ 004f57e0 bytes e48e1d94
- 004d2974 ["INT_ADD", "register:40f0:8", ["const:4d2974:8", "const:4:8"]]
- 004d2974 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f580c ["INT_ADD", "register:40f0:8", ["const:4f580c:8", "const:4:8"]]
+ 004f580c ["CALL", null, ["callee:00c57b10:8"]]
- 004d2974 bytes d3211c94
+ 004f580c bytes c1881d94
- 004d28ac ["INT_ADD", "register:40f0:8", ["const:4d28ac:8", "const:4:8"]]
- 004d28ac ["CALL", null, ["callee:00c57a90:8"]]
+ 004f5744 ["INT_ADD", "register:40f0:8", ["const:4f5744:8", "const:4:8"]]
+ 004f5744 ["CALL", null, ["callee:00c57a90:8"]]
- 004d28ac bytes e5211c94
+ 004f5744 bytes d3881d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b2763b032b7522146761304226c5e24"></a>

### [`004d29f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d29f8.md) → [`004f5890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5890.md) _ZNK5Botan14RSA_PrivateKey19create_signature_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorI

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`004c824c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c824c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051483c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/0051483c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004eb0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb0e4.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005376d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/005376d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.81% / 新版 94.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004f592c",
      "incomplete_value": false,
      "site": "004f5934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2a94",
      "incomplete_value": false,
      "site": "004d2a9c",
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
            "const:258:8"
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
      "site": "004f5990",
      "value": [
        "leaf",
        "ram:c59370:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d2af8",
      "value": [
        "leaf",
        "ram:bdc920:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f59b0",
      "incomplete_value": true,
      "site": "004f59bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d2b18",
      "incomplete_value": true,
      "site": "004d2b24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:230:8"
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
      "004f5934",
      "DATA",
      [
        "storage",
        "00bed258",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5984",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "byte[43]"
      ]
    ],
    [
      "004f5990",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc920"
      ]
    ]
  ],
  "added": [
    [
      "004f5934",
      "DATA",
      [
        "storage",
        "00c69e18",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5984",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "qword"
      ]
    ],
    [
      "004f5990",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59370"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d2af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d29f8.md#insn-004d2af8) · [`004d2b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d29f8.md#insn-004d2b24) · [`004d2a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d29f8.md#insn-004d2a70)
- 新版 `004f5990`（命令位置の公開資料なし） · `004f59bc`（命令位置の公開資料なし） · `004f5908`（命令位置の公開資料なし）

~~~diff
- 004d2af8 ["INT_ADD", "register:40f0:8", ["const:4d2af8:8", "const:4:8"]]
- 004d2af8 ["CALL", null, ["ram:bdc920:8"]]
+ 004f5990 ["INT_ADD", "register:40f0:8", ["const:4f5990:8", "const:4:8"]]
+ 004f5990 ["CALL", null, ["ram:c59370:8"]]
- 004d2af8 bytes 8a271c94
+ 004f5990 bytes 788e1d94
- 004d2b24 ["INT_ADD", "register:40f0:8", ["const:4d2b24:8", "const:4:8"]]
- 004d2b24 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f59bc ["INT_ADD", "register:40f0:8", ["const:4f59bc:8", "const:4:8"]]
+ 004f59bc ["CALL", null, ["callee:00c57b10:8"]]
- 004d2b24 bytes 67211c94
+ 004f59bc bytes 55881d94
- 004d2a70 ["INT_ADD", "register:40f0:8", ["const:4d2a70:8", "const:4:8"]]
- 004d2a70 ["CALL", null, ["callee:00c57a90:8"]]
+ 004f5908 ["INT_ADD", "register:40f0:8", ["const:4f5908:8", "const:4:8"]]
+ 004f5908 ["CALL", null, ["callee:00c57a90:8"]]
- 004d2a70 bytes 74211c94
+ 004f5908 bytes 62881d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-433a5fc3770fc4588170f036d0f1f5c2"></a>

### [`004d2b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2b8c.md) → [`004f5a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5a24.md) _ZNK5Botan7SHA_16010copy_stateEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f5a58",
      "incomplete_value": true,
      "site": "004f5a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d2bc0",
      "incomplete_value": true,
      "site": "004d2bc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f5a84",
      "incomplete_value": true,
      "site": "004f5a8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d2bec",
      "incomplete_value": true,
      "site": "004d2bf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f5a4c",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004f5a5c",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f5a74",
      "READ",
      [
        "storage",
        "00c1b150",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f5a4c",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004f5a5c",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f5a74",
      "READ",
      [
        "storage",
        "00c9ab40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d2ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2b8c.md#insn-004d2ba8) · [`004d2bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2b8c.md#insn-004d2bac) · [`004d2bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2b8c.md#insn-004d2bb4)
- 新版 `004f5a40`（命令位置の公開資料なし） · `004f5a44`（命令位置の公開資料なし） · `004f5a4c`（命令位置の公開資料なし）

~~~diff
- 004d2ba8 ["INT_ADD", "register:40f0:8", ["const:4d2ba8:8", "const:4:8"]]
- 004d2ba8 ["CALL", null, ["callee:00c57a90:8"]]
+ 004f5a40 ["INT_ADD", "register:40f0:8", ["const:4f5a40:8", "const:4:8"]]
+ 004f5a40 ["CALL", null, ["callee:00c57a90:8"]]
- 004d2ba8 bytes 26211c94
+ 004f5a40 bytes 14881d94
- 004d2bac ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004f5a44 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d2bac bytes 483a00b0
+ 004f5a44 bytes 283d00b0
- 004d2bb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
- 004d2bb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f5a4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
+ 004f5a4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d2bb4 bytes 08a540f9
+ 004f5a4c bytes 089d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-051401a1f5b419d6c8111711cb0eda78"></a>

### [`004d3a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3a84.md) → [`004f691c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f691c.md) _ZN5Botan7SHA_1605clearEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

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
      "definition_site": "004f6964",
      "incomplete_value": true,
      "site": "004f6970",
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d3acc",
      "incomplete_value": true,
      "site": "004d3ad8",
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
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
      "004f6964",
      "READ",
      [
        "storage",
        "002b0d30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f6964",
      "READ",
      [
        "storage",
        "002c2330",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d3aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3a84.md#insn-004d3aa8) · [`004d3ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3a84.md#insn-004d3ac0) · [`004d3ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3a84.md#insn-004d3ac4)
- 新版 `004f6940`（命令位置の公開資料なし） · `004f6958`（命令位置の公開資料なし） · `004f695c`（命令位置の公開資料なし）

~~~diff
- 004d3aa8 ["INT_ADD", "register:40f0:8", ["const:4d3aa8:8", "const:4:8"]]
- 004d3aa8 ["CALL", null, ["callee:00c57c90:8"]]
+ 004f6940 ["INT_ADD", "register:40f0:8", ["const:4f6940:8", "const:4:8"]]
+ 004f6940 ["CALL", null, ["callee:00c57c90:8"]]
- 004d3aa8 bytes e61d1c94
+ 004f6940 bytes d4841d94
- 004d3ac0 ["INT_ADD", "register:40f0:8", ["const:4d3ac0:8", "const:4:8"]]
- 004d3ac0 ["CALL", null, ["callee:00c57c90:8"]]
+ 004f6958 ["INT_ADD", "register:40f0:8", ["const:4f6958:8", "const:4:8"]]
+ 004f6958 ["CALL", null, ["callee:00c57c90:8"]]
- 004d3ac0 bytes e01d1c94
+ 004f6958 bytes ce841d94
- 004d3ac4 ["COPY", "register:4040:8", ["const:2b0000:8"]]
+ 004f695c ["COPY", "register:4040:8", ["const:2c2000:8"]]
- 004d3ac4 bytes e8eeffb0
+ 004f695c bytes 68eeff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd1d1c26866b84f8c30574f41df0bdfa"></a>

### [`004d3aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3aec.md) → [`004f6984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6984.md) _ZNK5Botan7SHA_22410copy_stateEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "004f69b8",
      "incomplete_value": true,
      "site": "004f69bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d3b20",
      "incomplete_value": true,
      "site": "004d3b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f69e4",
      "incomplete_value": true,
      "site": "004f69ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d3b4c",
      "incomplete_value": true,
      "site": "004d3b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004f69ac",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004f69bc",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f69d4",
      "READ",
      [
        "storage",
        "00c1b158",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f69ac",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004f69bc",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f69d4",
      "READ",
      [
        "storage",
        "00c9ab48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d3b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3aec.md#insn-004d3b08) · [`004d3b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3aec.md#insn-004d3b0c) · [`004d3b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3aec.md#insn-004d3b14)
- 新版 `004f69a0`（命令位置の公開資料なし） · `004f69a4`（命令位置の公開資料なし） · `004f69ac`（命令位置の公開資料なし）

~~~diff
- 004d3b08 ["INT_ADD", "register:40f0:8", ["const:4d3b08:8", "const:4:8"]]
- 004d3b08 ["CALL", null, ["callee:00c57a90:8"]]
+ 004f69a0 ["INT_ADD", "register:40f0:8", ["const:4f69a0:8", "const:4:8"]]
+ 004f69a0 ["CALL", null, ["callee:00c57a90:8"]]
- 004d3b08 bytes 4e1d1c94
+ 004f69a0 bytes 3c841d94
- 004d3b0c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004f69a4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d3b0c bytes 483a0090
+ 004f69a4 bytes 283d0090
- 004d3b14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
- 004d3b14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f69ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
+ 004f69ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d3b14 bytes 08a540f9
+ 004f69ac bytes 089d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03d6f4bf885cdb51586b99d387f94607"></a>

### [`004d3ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3ba0.md) → [`004f6a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6a38.md) _ZNK5Botan7SHA_25610copy_stateEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "004f6a6c",
      "incomplete_value": true,
      "site": "004f6a70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d3bd4",
      "incomplete_value": true,
      "site": "004d3bd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f6a98",
      "incomplete_value": true,
      "site": "004f6aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d3c00",
      "incomplete_value": true,
      "site": "004d3c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004f6a60",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004f6a70",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f6a88",
      "READ",
      [
        "storage",
        "00c1b160",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f6a60",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004f6a70",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f6a88",
      "READ",
      [
        "storage",
        "00c9ab50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d3bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3ba0.md#insn-004d3bbc) · [`004d3bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3ba0.md#insn-004d3bc0) · [`004d3bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3ba0.md#insn-004d3bc8)
- 新版 `004f6a54`（命令位置の公開資料なし） · `004f6a58`（命令位置の公開資料なし） · `004f6a60`（命令位置の公開資料なし）

~~~diff
- 004d3bbc ["INT_ADD", "register:40f0:8", ["const:4d3bbc:8", "const:4:8"]]
- 004d3bbc ["CALL", null, ["callee:00c57a90:8"]]
+ 004f6a54 ["INT_ADD", "register:40f0:8", ["const:4f6a54:8", "const:4:8"]]
+ 004f6a54 ["CALL", null, ["callee:00c57a90:8"]]
- 004d3bbc bytes 211d1c94
+ 004f6a54 bytes 0f841d94
- 004d3bc0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004f6a58 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d3bc0 bytes 483a0090
+ 004f6a58 bytes 283d0090
- 004d3bc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
- 004d3bc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f6a60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
+ 004f6a60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d3bc8 bytes 08a540f9
+ 004f6a60 bytes 089d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-613bfc79af9c07261f9ca2c3910f98dc"></a>

### [`004d5b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5b18.md) → [`004f89b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f89b0.md) _ZN5Botan7SHA_2245clearEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f89e4",
      "incomplete_value": true,
      "site": "004f89f0",
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
                "const:1d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5b4c",
      "incomplete_value": true,
      "site": "004d5b58",
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
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:b00:8"
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
      "definition_site": "004f89e8",
      "incomplete_value": true,
      "site": "004f89f0",
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5b50",
      "incomplete_value": true,
      "site": "004d5b58",
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
                "const:2b1000:8"
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
      "004f89e4",
      "READ",
      [
        "storage",
        "002b1b00",
        null,
        null
      ]
    ],
    [
      "004f89e8",
      "READ",
      [
        "storage",
        "002b1580",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f89e4",
      "READ",
      [
        "storage",
        "002c31d0",
        null,
        null
      ]
    ],
    [
      "004f89e8",
      "READ",
      [
        "storage",
        "002c2bd0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d5b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5b18.md#insn-004d5b3c) · [`004d5b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5b18.md#insn-004d5b40) · [`004d5b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5b18.md#insn-004d5b44)
- 新版 `004f89d4`（命令位置の公開資料なし） · `004f89d8`（命令位置の公開資料なし） · `004f89dc`（命令位置の公開資料なし）

~~~diff
- 004d5b3c ["INT_ADD", "register:40f0:8", ["const:4d5b3c:8", "const:4:8"]]
- 004d5b3c ["CALL", null, ["callee:00c57c90:8"]]
+ 004f89d4 ["INT_ADD", "register:40f0:8", ["const:4f89d4:8", "const:4:8"]]
+ 004f89d4 ["CALL", null, ["callee:00c57c90:8"]]
- 004d5b3c bytes c1151c94
+ 004f89d4 bytes af7c1d94
- 004d5b40 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004f89d8 ["COPY", "register:4048:8", ["const:2c3000:8"]]
- 004d5b40 bytes e9eeff90
+ 004f89d8 bytes 49eefff0
- 004d5b44 ["COPY", "register:4050:8", ["const:2b1000:8"]]
+ 004f89dc ["COPY", "register:4050:8", ["const:2c2000:8"]]
- 004d5b44 bytes eaeeff90
+ 004f89dc bytes 4aeeffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5fb123e43f95eba40d8780c20db474f"></a>

### [`004d5be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5be0.md) → [`004f8a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8a78.md) _ZN5Botan7SHA_2565clearEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8aac",
      "incomplete_value": true,
      "site": "004f8ab8",
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
                "const:120:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5c14",
      "incomplete_value": true,
      "site": "004d5c20",
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
                "const:2b1000:8"
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8ab0",
      "incomplete_value": true,
      "site": "004f8ab8",
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
                "const:cb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5c18",
      "incomplete_value": true,
      "site": "004d5c20",
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
                "const:2b1000:8"
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
      "004f8aac",
      "READ",
      [
        "storage",
        "002b1a50",
        null,
        null
      ]
    ],
    [
      "004f8ab0",
      "READ",
      [
        "storage",
        "002b1660",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f8aac",
      "READ",
      [
        "storage",
        "002c3120",
        null,
        null
      ]
    ],
    [
      "004f8ab0",
      "READ",
      [
        "storage",
        "002c2cb0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d5c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5be0.md#insn-004d5c04) · [`004d5c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5be0.md#insn-004d5c08) · [`004d5c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5be0.md#insn-004d5c0c)
- 新版 `004f8a9c`（命令位置の公開資料なし） · `004f8aa0`（命令位置の公開資料なし） · `004f8aa4`（命令位置の公開資料なし）

~~~diff
- 004d5c04 ["INT_ADD", "register:40f0:8", ["const:4d5c04:8", "const:4:8"]]
- 004d5c04 ["CALL", null, ["callee:00c57c90:8"]]
+ 004f8a9c ["INT_ADD", "register:40f0:8", ["const:4f8a9c:8", "const:4:8"]]
+ 004f8a9c ["CALL", null, ["callee:00c57c90:8"]]
- 004d5c04 bytes 8f151c94
+ 004f8a9c bytes 7d7c1d94
- 004d5c08 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 004f8aa0 ["COPY", "register:4048:8", ["const:2c3000:8"]]
- 004d5c08 bytes e9eeff90
+ 004f8aa0 bytes 49eefff0
- 004d5c0c ["COPY", "register:4050:8", ["const:2b1000:8"]]
+ 004f8aa4 ["COPY", "register:4050:8", ["const:2c2000:8"]]
- 004d5c0c bytes eaeeff90
+ 004f8aa4 bytes 4aeeffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91a1980a7e6c2a7d90d60c729bb7d490"></a>

### [`004d5ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5ed0.md) → [`004f8d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8d68.md) _ZN5Botan10system_rngEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc960.md) · 呼出先 5件 [`004d5f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5f58.md) [`004d6094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6094.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00c593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593b0.md) · 呼出先 5件 [`004f8df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md) [`004f8f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f2c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f8d9c",
      "incomplete_value": false,
      "site": "004f8da0",
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
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5f04",
      "incomplete_value": false,
      "site": "004d5f08",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f8db0",
      "incomplete_value": false,
      "site": "004f8dc4",
      "value": [
        "leaf",
        "const:4f8f2c:8"
      ]
    },
    "old": {
      "definition_site": "004d5f18",
      "incomplete_value": false,
      "site": "004d5f2c",
      "value": [
        "leaf",
        "const:4d6094:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f8db8",
      "incomplete_value": false,
      "site": "004f8dc4",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5f20",
      "incomplete_value": false,
      "site": "004d5f2c",
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
      "004f8d7c",
      "READ",
      [
        "storage",
        "00c253d0",
        null,
        "undefined1"
      ]
    ],
    [
      "004f8d88",
      "DATA",
      [
        "storage",
        "00c253c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f8d9c",
      "PARAM",
      [
        "storage",
        "00c253d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004f8d7c",
      "READ",
      [
        "storage",
        "00ca4e90",
        null,
        "undefined1"
      ]
    ],
    [
      "004f8d88",
      "DATA",
      [
        "storage",
        "00ca4e80",
        null,
        "undefined8"
      ]
    ],
    [
      "004f8d9c",
      "PARAM",
      [
        "storage",
        "00ca4e90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d5f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5ed0.md#insn-004d5f08) · [`004d5f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5ed0.md#insn-004d5f2c) · [`004d5f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5ed0.md#insn-004d5f38)
- 新版 `004f8da0`（命令位置の公開資料なし） · `004f8dc4`（命令位置の公開資料なし） · `004f8dd0`（命令位置の公開資料なし）

~~~diff
- 004d5f08 ["INT_ADD", "register:40f0:8", ["const:4d5f08:8", "const:4:8"]]
- 004d5f08 ["CALL", null, ["callee:00c57a50:8"]]
+ 004f8da0 ["INT_ADD", "register:40f0:8", ["const:4f8da0:8", "const:4:8"]]
+ 004f8da0 ["CALL", null, ["callee:00c57a50:8"]]
- 004d5f08 bytes 3e141c94
+ 004f8da0 bytes 2c7b1d94
- 004d5f2c ["INT_ADD", "register:40f0:8", ["const:4d5f2c:8", "const:4:8"]]
- 004d5f2c ["CALL", null, ["callee:00c57a30:8"]]
+ 004f8dc4 ["INT_ADD", "register:40f0:8", ["const:4f8dc4:8", "const:4:8"]]
+ 004f8dc4 ["CALL", null, ["callee:00c57a30:8"]]
- 004d5f2c bytes 2d141c94
+ 004f8dc4 bytes 1b7b1d94
- 004d5f38 ["INT_ADD", "register:40f0:8", ["const:4d5f38:8", "const:4:8"]]
- 004d5f38 ["CALL", null, ["callee:00c57a70:8"]]
+ 004f8dd0 ["INT_ADD", "register:40f0:8", ["const:4f8dd0:8", "const:4:8"]]
+ 004f8dd0 ["CALL", null, ["callee:00c57a70:8"]]
- 004d5f38 bytes 3a141c94
+ 004f8dd0 bytes 287b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7d6b0c11341033af5a06d30cd90c4c4"></a>

### [`004d5f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5f58.md) → [`004f8df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md) FUN_004f8df0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004d5ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5ed0.md) [`0051308c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051308c.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 2件 [`004f8d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8d68.md) [`00535f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.33% / 新版 88.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004f8e2c",
      "incomplete_value": false,
      "site": "004f8e2c",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5f94",
      "incomplete_value": false,
      "site": "004d5f94",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8e28",
      "incomplete_value": false,
      "site": "004f8e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5f90",
      "incomplete_value": false,
      "site": "004d5f94",
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
            "const:2e0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004f8e50",
      "incomplete_value": false,
      "site": "004f8e50",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d5fb8",
      "incomplete_value": false,
      "site": "004d5fb8",
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
            "const:3c8:8"
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
      "004f8e18",
      "PARAM",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "004f8e2c",
      "WRITE",
      [
        "storage",
        "00c253c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f8e2c",
      "DATA",
      [
        "storage",
        "00bed2e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004f8e18",
      "PARAM",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "004f8e2c",
      "WRITE",
      [
        "storage",
        "00ca4e80",
        null,
        "undefined8"
      ]
    ],
    [
      "004f8e2c",
      "DATA",
      [
        "storage",
        "00c69ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d5f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5f58.md#insn-004d5f98) · [`004d5fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5f58.md#insn-004d5fb0) · [`004d5fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5f58.md#insn-004d5fb8)
- 新版 `004f8e30`（命令位置の公開資料なし） · `004f8e48`（命令位置の公開資料なし） · `004f8e50`（命令位置の公開資料なし）

~~~diff
- 004d5f98 ["INT_ADD", "register:40f0:8", ["const:4d5f98:8", "const:4:8"]]
- 004d5f98 ["CALL", null, ["callee:00c593c0:8"]]
+ 004f8e30 ["INT_ADD", "register:40f0:8", ["const:4f8e30:8", "const:4:8"]]
+ 004f8e30 ["CALL", null, ["callee:00c593c0:8"]]
- 004d5f98 bytes 761a1c94
+ 004f8e30 bytes 64811d94
- 004d5fb0 ["INT_ADD", "register:40f0:8", ["const:4d5fb0:8", "const:4:8"]]
- 004d5fb0 ["CALL", null, ["callee:00c593c0:8"]]
+ 004f8e48 ["INT_ADD", "register:40f0:8", ["const:4f8e48:8", "const:4:8"]]
+ 004f8e48 ["CALL", null, ["callee:00c593c0:8"]]
- 004d5fb0 bytes 701a1c94
+ 004f8e48 bytes 5e811d94
- 004d5fb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3c8:8"]]
- 004d5fb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 004f8e50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
+ 004f8e50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 004d5fb8 bytes 00c903b9
+ 004f8e50 bytes 00890eb9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f937042cf8136fa57a956e7d73e3c0c4"></a>

### [`004d60c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d60c4.md) → [`004f8f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f5c.md) _ZNK5Botan14calendar_point9to_stringEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.89% / 新版 94.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件

アドレスに依存する影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f9100",
      "incomplete_value": true,
      "site": "004f9108",
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
      "definition_site": "004d6268",
      "incomplete_value": true,
      "site": "004d6270",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004f9110",
      "incomplete_value": true,
      "site": "004f9110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
      "definition_site": "004d6278",
      "incomplete_value": true,
      "site": "004d6278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f9110",
      "incomplete_value": true,
      "site": "004f9110",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004d6278",
      "incomplete_value": true,
      "site": "004d6278",
      "value": [
        "LOAD",
        "8",
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
      "004f8fc4",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004f8fc4",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004f8fe0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "004f8fc4",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "004f8fc4",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004f8fe0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d6130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d60c4.md#insn-004d6130) · [`004d6148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d60c4.md#insn-004d6148) · [`004d6180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d60c4.md#insn-004d6180)
- 新版 `004f8fc8`（命令位置の公開資料なし） · `004f8fe0`（命令位置の公開資料なし） · `004f9018`（命令位置の公開資料なし）

~~~diff
- 004d6130 ["INT_ADD", "register:40f0:8", ["const:4d6130:8", "const:4:8"]]
- 004d6130 ["CALL", null, ["callee:00c57e80:8"]]
+ 004f8fc8 ["INT_ADD", "register:40f0:8", ["const:4f8fc8:8", "const:4:8"]]
+ 004f8fc8 ["CALL", null, ["callee:00c57e80:8"]]
- 004d6130 bytes c0141c94
+ 004f8fc8 bytes ae7b1d94
- 004d6148 ["INT_ADD", "register:40f0:8", ["const:4d6148:8", "const:4:8"]]
- 004d6148 ["CALL", null, ["ram:bdb440:8"]]
+ 004f8fe0 ["INT_ADD", "register:40f0:8", ["const:4f8fe0:8", "const:4:8"]]
+ 004f8fe0 ["CALL", null, ["ram:c57e90:8"]]
- 004d6148 bytes be141c94
+ 004f8fe0 bytes ac7b1d94
- 004d6180 ["INT_ADD", "register:40f0:8", ["const:4d6180:8", "const:4:8"]]
- 004d6180 ["CALL", null, ["callee:00459490:8"]]
+ 004f9018 ["INT_ADD", "register:40f0:8", ["const:4f9018:8", "const:4:8"]]
+ 004f9018 ["CALL", null, ["callee:00459490:8"]]
- 004d6180 bytes 1e81fd97
+ 004f9018 bytes 1e81fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ff319833ff8161f6a5172aa0432168c"></a>

### [`004d6338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6338.md) → [`004f91d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f91d0.md) FUN_004f91d0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0048aad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048aad4.md) [`0048ac0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ac0c.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 2件 [`004ad96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad96c.md) [`004adaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adaa4.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.52% / 新版 96.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f92f8",
      "incomplete_value": false,
      "site": "004f9300",
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
            "const:155:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6460",
      "incomplete_value": false,
      "site": "004d6468",
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
            "const:727:8"
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
      "definition_site": "004f9330",
      "incomplete_value": true,
      "site": "004f933c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6498",
      "incomplete_value": true,
      "site": "004d64a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f932c",
      "incomplete_value": false,
      "site": "004f933c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004d6494",
      "incomplete_value": false,
      "site": "004d64a4",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f92f8",
      "PARAM",
      [
        "storage",
        "002a5727",
        null,
        "string"
      ]
    ],
    [
      "004f932c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004f9330",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f92f8",
      "PARAM",
      [
        "storage",
        "002b6155",
        null,
        "string"
      ]
    ],
    [
      "004f932c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f9330",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d6468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6338.md#insn-004d6468) · [`004d64a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6338.md#insn-004d64a4) · [`004d64c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6338.md#insn-004d64c4)
- 新版 `004f9300`（命令位置の公開資料なし） · `004f933c`（命令位置の公開資料なし） · `004f935c`（命令位置の公開資料なし）

~~~diff
- 004d6468 ["INT_ADD", "register:40f0:8", ["const:4d6468:8", "const:4:8"]]
- 004d6468 ["CALL", null, ["callee:0043dd98:8"]]
+ 004f9300 ["INT_ADD", "register:40f0:8", ["const:4f9300:8", "const:4:8"]]
+ 004f9300 ["CALL", null, ["callee:0043dd98:8"]]
- 004d6468 bytes 8c13fd97
+ 004f9300 bytes a612fd97
- 004d64a4 ["INT_ADD", "register:40f0:8", ["const:4d64a4:8", "const:4:8"]]
- 004d64a4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f933c ["INT_ADD", "register:40f0:8", ["const:4f933c:8", "const:4:8"]]
+ 004f933c ["CALL", null, ["callee:00c57b10:8"]]
- 004d64a4 bytes 07131c94
+ 004f933c bytes f5791d94
- 004d64c4 ["INT_ADD", "register:40f0:8", ["const:4d64c4:8", "const:4:8"]]
- 004d64c4 ["CALL", null, ["callee:0043dd98:8"]]
+ 004f935c ["INT_ADD", "register:40f0:8", ["const:4f935c:8", "const:4:8"]]
+ 004f935c ["CALL", null, ["callee:0043dd98:8"]]
- 004d64c4 bytes 7513fd97
+ 004f935c bytes 8f12fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de8d96953a21db0b663884af8e1891e4"></a>

### [`004d6550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6550.md) → [`004f93e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f93e8.md) _ZN5Botan7Charset9transcodeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_13Character_SetESA_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f962c",
      "incomplete_value": false,
      "site": "004f9634",
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
            "const:9b1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6794",
      "incomplete_value": false,
      "site": "004d679c",
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
            "const:62c:8"
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
      "definition_site": "004f9664",
      "incomplete_value": true,
      "site": "004f9670",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d67cc",
      "incomplete_value": true,
      "site": "004d67d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f9660",
      "incomplete_value": false,
      "site": "004f9670",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004d67c8",
      "incomplete_value": false,
      "site": "004d67d8",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f962c",
      "PARAM",
      [
        "storage",
        "0029e62c",
        null,
        "string"
      ]
    ],
    [
      "004f9660",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004f9664",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f962c",
      "PARAM",
      [
        "storage",
        "002ae9b1",
        null,
        "string"
      ]
    ],
    [
      "004f9660",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f9664",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d679c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6550.md#insn-004d679c) · [`004d67d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6550.md#insn-004d67d8) · [`004d680c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6550.md#insn-004d680c)
- 新版 `004f9634`（命令位置の公開資料なし） · `004f9670`（命令位置の公開資料なし） · `004f96a4`（命令位置の公開資料なし）

~~~diff
- 004d679c ["INT_ADD", "register:40f0:8", ["const:4d679c:8", "const:4:8"]]
- 004d679c ["CALL", null, ["callee:0043dd98:8"]]
+ 004f9634 ["INT_ADD", "register:40f0:8", ["const:4f9634:8", "const:4:8"]]
+ 004f9634 ["CALL", null, ["callee:0043dd98:8"]]
- 004d679c bytes bf12fd97
+ 004f9634 bytes d911fd97
- 004d67d8 ["INT_ADD", "register:40f0:8", ["const:4d67d8:8", "const:4:8"]]
- 004d67d8 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f9670 ["INT_ADD", "register:40f0:8", ["const:4f9670:8", "const:4:8"]]
+ 004f9670 ["CALL", null, ["callee:00c57b10:8"]]
- 004d67d8 bytes 3a121c94
+ 004f9670 bytes 28791d94
- 004d680c ["INT_ADD", "register:40f0:8", ["const:4d680c:8", "const:4:8"]]
- 004d680c ["CALL", null, ["callee:00c57b60:8"]]
+ 004f96a4 ["INT_ADD", "register:40f0:8", ["const:4f96a4:8", "const:4:8"]]
+ 004f96a4 ["CALL", null, ["callee:00c57b60:8"]]
- 004d680c bytes 41121c94
+ 004f96a4 bytes 2f791d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11175055d86250a847135265adac2f91"></a>

### [`004d6c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6c30.md) → [`004f9ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9ac8.md) _ZN5Botan17DataSource_MemoryC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc670.md) · 呼出先 1件 [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md)
- 新版 呼出元 1件 [`00c590c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590c0.md) · 呼出先 1件 [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md)

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
      "definition_site": "004f9ae0",
      "incomplete_value": true,
      "site": "004f9ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d6c48",
      "incomplete_value": true,
      "site": "004d6c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004f9adc",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "004f9ae4",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004f9adc",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f9ae4",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6c30.md#insn-004d6c3c) · [`004d6c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6c30.md#insn-004d6c44) · [`004d6c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6c30.md#insn-004d6c78)
- 新版 `004f9ad4`（命令位置の公開資料なし） · `004f9adc`（命令位置の公開資料なし） · `004f9b10`（命令位置の公開資料なし）

~~~diff
- 004d6c3c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004f9ad4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d6c3c bytes 283a0090
+ 004f9ad4 bytes 083d00b0
- 004d6c44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
- 004d6c44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f9adc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9e0:8"]]
+ 004f9adc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d6c44 bytes 08f947f9
+ 004f9adc bytes 08f144f9
- 004d6c78 ["INT_ADD", "register:40f0:8", ["const:4d6c78:8", "const:4:8"]]
- 004d6c78 ["CALL", null, ["callee:00540388:8"]]
+ 004f9b10 ["INT_ADD", "register:40f0:8", ["const:4f9b10:8", "const:4:8"]]
+ 004f9b10 ["CALL", null, ["callee:00540388:8"]]
- 004d6c78 bytes 1e1a0194
+ 004f9b10 bytes 1e1a0194
~~~


<a id="compare-ea329ce8195c9b3b0abb82cd174a3ab9"></a>

### [`004d6c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6c8c.md) → [`004f9b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9b24.md) _ZN5Botan17DataSource_Stream4readEPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

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
      "definition_site": "004f9bb0",
      "incomplete_value": false,
      "site": "004f9bb8",
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
            "const:79e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6d18",
      "incomplete_value": false,
      "site": "004d6d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:514:8"
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
      "definition_site": "004f9bec",
      "incomplete_value": true,
      "site": "004f9bf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:980:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6d54",
      "incomplete_value": true,
      "site": "004d6d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f90:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f9be8",
      "incomplete_value": false,
      "site": "004f9bf8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004d6d50",
      "incomplete_value": false,
      "site": "004d6d60",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f9bb0",
      "PARAM",
      [
        "storage",
        "0029d514",
        null,
        "string"
      ]
    ],
    [
      "004f9be8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004f9bec",
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
      "004f9bb0",
      "PARAM",
      [
        "storage",
        "002ad79e",
        null,
        "string"
      ]
    ],
    [
      "004f9be8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f9bec",
      "READ",
      [
        "storage",
        "00c9a980",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d6d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6c8c.md#insn-004d6d20) · [`004d6d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6c8c.md#insn-004d6d60) · [`004d6cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6c8c.md#insn-004d6cb4)
- 新版 `004f9bb8`（命令位置の公開資料なし） · `004f9bf8`（命令位置の公開資料なし） · `004f9b4c`（命令位置の公開資料なし）

~~~diff
- 004d6d20 ["INT_ADD", "register:40f0:8", ["const:4d6d20:8", "const:4:8"]]
- 004d6d20 ["CALL", null, ["callee:0043dd98:8"]]
+ 004f9bb8 ["INT_ADD", "register:40f0:8", ["const:4f9bb8:8", "const:4:8"]]
+ 004f9bb8 ["CALL", null, ["callee:0043dd98:8"]]
- 004d6d20 bytes 5e11fd97
+ 004f9bb8 bytes 7810fd97
- 004d6d60 ["INT_ADD", "register:40f0:8", ["const:4d6d60:8", "const:4:8"]]
- 004d6d60 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f9bf8 ["INT_ADD", "register:40f0:8", ["const:4f9bf8:8", "const:4:8"]]
+ 004f9bf8 ["CALL", null, ["callee:00c57b10:8"]]
- 004d6d60 bytes d8101c94
+ 004f9bf8 bytes c6771d94
- 004d6cb4 ["INT_ADD", "register:40f0:8", ["const:4d6cb4:8", "const:4:8"]]
- 004d6cb4 ["CALL", null, ["callee:00c58cd0:8"]]
+ 004f9b4c ["INT_ADD", "register:40f0:8", ["const:4f9b4c:8", "const:4:8"]]
+ 004f9b4c ["CALL", null, ["callee:00c58cd0:8"]]
- 004d6cb4 bytes 73151c94
+ 004f9b4c bytes 617c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-272ae4eceeb14bf9aa7496bd59a94f22"></a>

### [`004d6e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6e20.md) → [`004f9cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9cb8.md) _ZNK5Botan17DataSource_Stream4peekEPhmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f9d68",
      "incomplete_value": true,
      "site": "004f9d68",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
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
    "old": {
      "definition_site": "004d6ed0",
      "incomplete_value": true,
      "site": "004d6ed0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f9e2c",
      "incomplete_value": false,
      "site": "004f9e34",
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
            "const:892:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6f94",
      "incomplete_value": false,
      "site": "004d6f9c",
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
            "const:50d:8"
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
      "definition_site": "004f9e64",
      "incomplete_value": true,
      "site": "004f9e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d6fcc",
      "incomplete_value": true,
      "site": "004d6fd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004f9d58",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004f9e2c",
      "PARAM",
      [
        "storage",
        "0029e50d",
        null,
        "string"
      ]
    ],
    [
      "004f9e60",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f9d58",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f9e2c",
      "PARAM",
      [
        "storage",
        "002ae892",
        null,
        "string"
      ]
    ],
    [
      "004f9e60",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d6ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6e20.md#insn-004d6ed0) · [`004d6f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6e20.md#insn-004d6f9c) · [`004d6fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6e20.md#insn-004d6fd8)
- 新版 `004f9d68`（命令位置の公開資料なし） · `004f9e34`（命令位置の公開資料なし） · `004f9e70`（命令位置の公開資料なし）

~~~diff
- 004d6ed0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004d6ed0 ["INT_ADD", "register:40f0:8", ["const:4d6ed0:8", "const:4:8"]]
- 004d6ed0 ["CALLIND", null, ["register:0:8"]]
+ 004f9d68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f9d68 ["INT_ADD", "register:40f0:8", ["const:4f9d68:8", "const:4:8"]]
+ 004f9d68 ["CALLIND", null, ["register:0:8"]]
- 004d6ed0 bytes 20013fd6
+ 004f9d68 bytes 20013fd6
- 004d6f9c ["INT_ADD", "register:40f0:8", ["const:4d6f9c:8", "const:4:8"]]
- 004d6f9c ["CALL", null, ["callee:0043dd98:8"]]
+ 004f9e34 ["INT_ADD", "register:40f0:8", ["const:4f9e34:8", "const:4:8"]]
+ 004f9e34 ["CALL", null, ["callee:0043dd98:8"]]
- 004d6f9c bytes bf10fd97
+ 004f9e34 bytes d90ffd97
- 004d6fd8 ["INT_ADD", "register:40f0:8", ["const:4d6fd8:8", "const:4:8"]]
- 004d6fd8 ["CALL", null, ["callee:00c57b10:8"]]
+ 004f9e70 ["INT_ADD", "register:40f0:8", ["const:4f9e70:8", "const:4:8"]]
+ 004f9e70 ["CALL", null, ["callee:00c57b10:8"]]
- 004d6fd8 bytes 3a101c94
+ 004f9e70 bytes 28771d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d457cdfbd2c499cc2a084d289431b14"></a>

### [`004d717c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d717c.md) → [`004fa014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa014.md) _ZN5Botan17DataSource_StreamC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004d7338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7338.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004fa1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa1d0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa054",
      "incomplete_value": true,
      "site": "004fa054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d71bc",
      "incomplete_value": true,
      "site": "004d71bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fa0f8",
      "incomplete_value": false,
      "site": "004fa104",
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
            "const:8c2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7260",
      "incomplete_value": false,
      "site": "004d726c",
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
            "const:53d:8"
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
      "definition_site": "004fa134",
      "incomplete_value": true,
      "site": "004fa140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:980:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d729c",
      "incomplete_value": true,
      "site": "004d72a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f90:8"
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
      "004fa038",
      "READ",
      [
        "storage",
        "00c1b238",
        null,
        "pointer"
      ]
    ],
    [
      "004fa054",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004fa0f8",
      "PARAM",
      [
        "storage",
        "0029e53d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fa038",
      "READ",
      [
        "storage",
        "00c9ac28",
        null,
        "pointer"
      ]
    ],
    [
      "004fa054",
      "DATA",
      [
        "storage",
        "00c66fd8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004fa0f8",
      "PARAM",
      [
        "storage",
        "002ae8c2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d726c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d717c.md#insn-004d726c) · [`004d72a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d717c.md#insn-004d72a8) · [`004d7194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d717c.md#insn-004d7194)
- 新版 `004fa104`（命令位置の公開資料なし） · `004fa140`（命令位置の公開資料なし） · `004fa02c`（命令位置の公開資料なし）

~~~diff
- 004d726c ["INT_ADD", "register:40f0:8", ["const:4d726c:8", "const:4:8"]]
- 004d726c ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fa104 ["INT_ADD", "register:40f0:8", ["const:4fa104:8", "const:4:8"]]
+ 004fa104 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d726c bytes fd0f1c94
+ 004fa104 bytes eb761d94
- 004d72a8 ["INT_ADD", "register:40f0:8", ["const:4d72a8:8", "const:4:8"]]
- 004d72a8 ["CALL", null, ["callee:00c57b10:8"]]
+ 004fa140 ["INT_ADD", "register:40f0:8", ["const:4fa140:8", "const:4:8"]]
+ 004fa140 ["CALL", null, ["callee:00c57b10:8"]]
- 004d72a8 bytes 860f1c94
+ 004fa140 bytes 74761d94
- 004d7194 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004fa02c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d7194 bytes 283a0090
+ 004fa02c bytes 083d0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-851c2a96f318219642cca57ebc5bedbe"></a>

### [`004d7338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7338.md) → [`004fa1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa1d0.md) FUN_004fa1d0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004d717c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d717c.md) · 呼出先 4件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0b0.md) [`00bdc0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0c0.md)
- 新版 呼出元 1件 [`004fa014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa014.md) · 呼出先 4件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c58b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b00.md) [`00c58b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b10.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa214",
      "incomplete_value": true,
      "site": "004fa214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004d737c",
      "incomplete_value": true,
      "site": "004d737c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa20c",
      "incomplete_value": true,
      "site": "004fa218",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004d7374",
      "incomplete_value": true,
      "site": "004d7380",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004fa224",
      "incomplete_value": true,
      "site": "004fa224",
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
      "definition_site": "004d738c",
      "incomplete_value": true,
      "site": "004d738c",
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
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fa1f4",
      "READ",
      [
        "storage",
        "00c1b240",
        null,
        "pointer"
      ]
    ],
    [
      "004fa1f8",
      "READ",
      [
        "storage",
        "00c1b248",
        null,
        "pointer"
      ]
    ],
    [
      "004fa20c",
      "READ",
      [
        "storage",
        "00c13308",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004fa1f4",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "004fa1f8",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      "004fa20c",
      "READ",
      [
        "storage",
        "00c92cb0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7338.md#insn-004d7350) · [`004d7354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7338.md#insn-004d7354) · [`004d735c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7338.md#insn-004d735c)
- 新版 `004fa1e8`（命令位置の公開資料なし） · `004fa1ec`（命令位置の公開資料なし） · `004fa1f4`（命令位置の公開資料なし）

~~~diff
- 004d7350 ["COPY", "register:40c8:8", ["const:c1b000:8"]]
+ 004fa1e8 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
- 004d7350 bytes 393a0090
+ 004fa1e8 bytes 193d0090
- 004d7354 ["COPY", "register:40c0:8", ["const:c1b000:8"]]
+ 004fa1ec ["COPY", "register:40c0:8", ["const:c9a000:8"]]
- 004d7354 bytes 383a0090
+ 004fa1ec bytes 183d0090
- 004d735c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:240:8"]]
- 004d735c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa1f4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:c30:8"]]
+ 004fa1f4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004d735c bytes 392341f9
+ 004fa1f4 bytes 391b46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85b41ced8018120b3e5561e2c5ec6ef3"></a>

### [`004d7450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7450.md) → [`004fa2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa2e8.md) _ZN5Botan17DataSource_StreamC2ERNSt6__ndk113basic_istreamIcNS1_11char_traitsIcEEEERKNS1_12basic_stringIcS4_NS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

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
      "definition_site": "004fa308",
      "incomplete_value": true,
      "site": "004fa308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d7470",
      "incomplete_value": true,
      "site": "004d7470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fa300",
      "READ",
      [
        "storage",
        "00c1b238",
        null,
        "pointer"
      ]
    ],
    [
      "004fa308",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004fa300",
      "READ",
      [
        "storage",
        "00c9ac28",
        null,
        "pointer"
      ]
    ],
    [
      "004fa308",
      "DATA",
      [
        "storage",
        "00c66fd8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d745c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7450.md#insn-004d745c) · [`004d7468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7450.md#insn-004d7468) · [`004d7494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7450.md#insn-004d7494)
- 新版 `004fa2f4`（命令位置の公開資料なし） · `004fa300`（命令位置の公開資料なし） · `004fa32c`（命令位置の公開資料なし）

~~~diff
- 004d745c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004fa2f4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d745c bytes 283a0090
+ 004fa2f4 bytes 083d0090
- 004d7468 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:238:8"]]
- 004d7468 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa300 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c28:8"]]
+ 004fa300 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d7468 bytes 081d41f9
+ 004fa300 bytes 081546f9
- 004d7494 ["INT_ADD", "register:40f0:8", ["const:4d7494:8", "const:4:8"]]
- 004d7494 ["CALL", null, ["callee:0043bae0:8"]]
+ 004fa32c ["INT_ADD", "register:40f0:8", ["const:4fa32c:8", "const:4:8"]]
+ 004fa32c ["CALL", null, ["callee:0043bae0:8"]]
- 004d7494 bytes d306fd97
+ 004fa32c bytes ed05fd97
~~~


<a id="compare-5bb85db5d2c2991b270a4d61bb2f5fec"></a>

### [`004d74f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d74f8.md) → [`004fa390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa390.md) _ZN5Botan17DataSource_StreamD0Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "site": "004fa3a0",
      "value": [
        "leaf",
        "ram:c59270:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d7508",
      "value": [
        "leaf",
        "ram:bdc820:8"
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
      "004fa3a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc820"
      ]
    ]
  ],
  "added": [
    [
      "004fa3a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59270"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d74f8.md#insn-004d7508)
- 新版 `004fa3a0`（命令位置の公開資料なし）

~~~diff
- 004d7508 ["INT_ADD", "register:40f0:8", ["const:4d7508:8", "const:4:8"]]
- 004d7508 ["CALL", null, ["ram:bdc820:8"]]
+ 004fa3a0 ["INT_ADD", "register:40f0:8", ["const:4fa3a0:8", "const:4:8"]]
+ 004fa3a0 ["CALL", null, ["ram:c59270:8"]]
- 004d7508 bytes c6141c94
+ 004fa3a0 bytes b47b1d94
~~~


<a id="compare-ca385c05c26b0735fdd29c6b9683813d"></a>

### [`004d751c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d751c.md) → [`004fa3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa3b4.md) _ZN5Botan9ExceptionC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb970.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00c583c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583c0.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

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
      "definition_site": "004fa3d0",
      "incomplete_value": true,
      "site": "004fa3d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d7538",
      "incomplete_value": true,
      "site": "004d7538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fa3c8",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004fa3d0",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fa3c8",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fa3d0",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d751c.md#insn-004d7528) · [`004d7530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d751c.md#insn-004d7530) · [`004d7560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d751c.md#insn-004d7560)
- 新版 `004fa3c0`（命令位置の公開資料なし） · `004fa3c8`（命令位置の公開資料なし） · `004fa3f8`（命令位置の公開資料なし）

~~~diff
- 004d7528 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004fa3c0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004d7528 bytes 083a00f0
+ 004fa3c0 bytes 083d0090
- 004d7530 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 004d7530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa3c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 004fa3c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d7530 bytes 08f147f9
+ 004fa3c8 bytes 08e944f9
- 004d7560 ["INT_ADD", "register:40f0:8", ["const:4d7560:8", "const:4:8"]]
- 004d7560 ["CALL", null, ["callee:0043bae0:8"]]
+ 004fa3f8 ["INT_ADD", "register:40f0:8", ["const:4fa3f8:8", "const:4:8"]]
+ 004fa3f8 ["CALL", null, ["callee:0043bae0:8"]]
- 004d7560 bytes a006fd97
+ 004fa3f8 bytes ba05fd97
~~~


<a id="compare-a49e34e6df4b07919d2409aae6bd5b3a"></a>

### [`004d7584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7584.md) → [`004fa41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa41c.md) _ZN5Botan9ExceptionC1EPKcRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md) · 呼出先 8件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md) · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa464",
      "incomplete_value": true,
      "site": "004fa464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d75cc",
      "incomplete_value": true,
      "site": "004d75cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fa4e0",
      "incomplete_value": false,
      "site": "004fa4e8",
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
            "const:efa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7648",
      "incomplete_value": false,
      "site": "004d7650",
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
            "const:8e1:8"
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
      "004fa448",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004fa464",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004fa4e0",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004fa448",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fa464",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004fa4e0",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7584.md#insn-004d7650) · [`004d75a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7584.md#insn-004d75a4) · [`004d75b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7584.md#insn-004d75b0)
- 新版 `004fa4e8`（命令位置の公開資料なし） · `004fa43c`（命令位置の公開資料なし） · `004fa448`（命令位置の公開資料なし）

~~~diff
- 004d7650 ["INT_ADD", "register:40f0:8", ["const:4d7650:8", "const:4:8"]]
- 004d7650 ["CALL", null, ["callee:00c57b70:8"]]
+ 004fa4e8 ["INT_ADD", "register:40f0:8", ["const:4fa4e8:8", "const:4:8"]]
+ 004fa4e8 ["CALL", null, ["callee:00c57b70:8"]]
- 004d7650 bytes b40e1c94
+ 004fa4e8 bytes a2751d94
- 004d75a4 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004fa43c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004d75a4 bytes 093a00f0
+ 004fa43c bytes 093d0090
- 004d75b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fe0:8"]]
- 004d75b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa448 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9d0:8"]]
+ 004fa448 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004d75b0 bytes 29f147f9
+ 004fa448 bytes 29e944f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22ed90eb792393d1f19f79f42c79db41"></a>

### [`004d7760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7760.md) → [`004fa5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa5f8.md) _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb820.md) · 呼出先 1件 [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c58270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58270.md) · 呼出先 1件 [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa620",
      "incomplete_value": true,
      "site": "004fa624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d7788",
      "incomplete_value": true,
      "site": "004d778c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004fa614",
      "value": [
        "leaf",
        "ram:c58380:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d777c",
      "value": [
        "leaf",
        "ram:bdb930:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fa60c",
      "incomplete_value": false,
      "site": "004fa614",
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
            "const:372:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7774",
      "incomplete_value": false,
      "site": "004d777c",
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
            "const:83d:8"
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
      "004fa60c",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004fa614",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb930"
      ]
    ],
    [
      "004fa61c",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fa60c",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "004fa614",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58380"
      ]
    ],
    [
      "004fa61c",
      "READ",
      [
        "storage",
        "00c9a960",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d777c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7760.md#insn-004d777c) · [`004d7770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7760.md#insn-004d7770) · [`004d7774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7760.md#insn-004d7774)
- 新版 `004fa614`（命令位置の公開資料なし） · `004fa608`（命令位置の公開資料なし） · `004fa60c`（命令位置の公開資料なし）

~~~diff
- 004d777c ["INT_ADD", "register:40f0:8", ["const:4d777c:8", "const:4:8"]]
- 004d777c ["CALL", null, ["ram:bdb930:8"]]
+ 004fa614 ["INT_ADD", "register:40f0:8", ["const:4fa614:8", "const:4:8"]]
+ 004fa614 ["CALL", null, ["ram:c58380:8"]]
- 004d777c bytes 6d101c94
+ 004fa614 bytes 5b771d94
- 004d7770 ["COPY", "register:4008:8", ["const:296000:8"]]
+ 004fa608 ["COPY", "register:4008:8", ["const:2a6000:8"]]
- 004d7770 bytes e1edfff0
+ 004fa608 bytes 61edff90
- 004d7774 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 004d7774 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d7774 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d7774 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fa60c ["COPY", "tmp:0:8", ["const:372:8"]]
+ 004fa60c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa60c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa60c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d7774 bytes 21f42091
+ 004fa60c bytes 21c80d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23bb143b0d7774b18ba8303ac3ba62bf"></a>

### [`004d779c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d779c.md) → [`004fa634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa634.md) _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa784",
      "incomplete_value": true,
      "site": "004fa788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d78ec",
      "incomplete_value": true,
      "site": "004d78f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004fa758",
      "value": [
        "leaf",
        "ram:c58380:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d78c0",
      "value": [
        "leaf",
        "ram:bdb930:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fa74c",
      "incomplete_value": false,
      "site": "004fa758",
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
            "const:372:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d78b4",
      "incomplete_value": false,
      "site": "004d78c0",
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
            "const:83d:8"
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
      "004fa74c",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004fa758",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb930"
      ]
    ],
    [
      "004fa780",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fa74c",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "004fa758",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58380"
      ]
    ],
    [
      "004fa780",
      "READ",
      [
        "storage",
        "00c9a960",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d78c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d779c.md#insn-004d78c0) · [`004d7838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d779c.md#insn-004d7838) · [`004d7860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d779c.md#insn-004d7860)
- 新版 `004fa758`（命令位置の公開資料なし） · `004fa6d0`（命令位置の公開資料なし） · `004fa6f8`（命令位置の公開資料なし）

~~~diff
- 004d78c0 ["INT_ADD", "register:40f0:8", ["const:4d78c0:8", "const:4:8"]]
- 004d78c0 ["CALL", null, ["ram:bdb930:8"]]
+ 004fa758 ["INT_ADD", "register:40f0:8", ["const:4fa758:8", "const:4:8"]]
+ 004fa758 ["CALL", null, ["ram:c58380:8"]]
- 004d78c0 bytes 1c101c94
+ 004fa758 bytes 0a771d94
- 004d7838 ["INT_ADD", "register:40f0:8", ["const:4d7838:8", "const:4:8"]]
- 004d7838 ["CALL", null, ["callee:00c57a90:8"]]
+ 004fa6d0 ["INT_ADD", "register:40f0:8", ["const:4fa6d0:8", "const:4:8"]]
+ 004fa6d0 ["CALL", null, ["callee:00c57a90:8"]]
- 004d7838 bytes 020e1c94
+ 004fa6d0 bytes f0741d94
- 004d7860 ["INT_ADD", "register:40f0:8", ["const:4d7860:8", "const:4:8"]]
- 004d7860 ["CALL", null, ["callee:00c57b40:8"]]
+ 004fa6f8 ["INT_ADD", "register:40f0:8", ["const:4fa6f8:8", "const:4:8"]]
+ 004fa6f8 ["CALL", null, ["callee:00c57b40:8"]]
- 004d7860 bytes 240e1c94
+ 004fa6f8 bytes 12751d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed681e53acd7c25e17209c3a424112ef"></a>

### [`004d7984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7984.md) → [`004fa81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa81c.md) _ZN5Botan12Lookup_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf00.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00c58950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58950.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa940",
      "incomplete_value": true,
      "site": "004fa940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d7aa8",
      "incomplete_value": true,
      "site": "004d7aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa998",
      "incomplete_value": true,
      "site": "004fa99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d7b00",
      "incomplete_value": true,
      "site": "004d7b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "004fa83c",
      "incomplete_value": false,
      "site": "004fa854",
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
            "const:dd7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d79a4",
      "incomplete_value": false,
      "site": "004d79bc",
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
            "const:8f3:8"
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
      "004fa83c",
      "PARAM",
      [
        "storage",
        "002ae8f3",
        null,
        "string"
      ]
    ],
    [
      "004fa85c",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        null
      ]
    ],
    [
      "004fa8d4",
      "PARAM",
      [
        "storage",
        "0029c667",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fa83c",
      "PARAM",
      [
        "storage",
        "002bfdd7",
        null,
        "string"
      ]
    ],
    [
      "004fa85c",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        null
      ]
    ],
    [
      "004fa8d4",
      "PARAM",
      [
        "storage",
        "002ac800",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7984.md#insn-004d79bc) · [`004d79cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7984.md#insn-004d79cc) · [`004d7a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7984.md#insn-004d7a48)
- 新版 `004fa854`（命令位置の公開資料なし） · `004fa864`（命令位置の公開資料なし） · `004fa8e0`（命令位置の公開資料なし）

~~~diff
- 004d79bc ["INT_ADD", "register:40f0:8", ["const:4d79bc:8", "const:4:8"]]
- 004d79bc ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fa854 ["INT_ADD", "register:40f0:8", ["const:4fa854:8", "const:4:8"]]
+ 004fa854 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d79bc bytes 290e1c94
+ 004fa854 bytes 17751d94
- 004d79cc ["INT_ADD", "register:40f0:8", ["const:4d79cc:8", "const:4:8"]]
- 004d79cc ["CALL", null, ["callee:00c57b70:8"]]
+ 004fa864 ["INT_ADD", "register:40f0:8", ["const:4fa864:8", "const:4:8"]]
+ 004fa864 ["CALL", null, ["callee:00c57b70:8"]]
- 004d79cc bytes d50d1c94
+ 004fa864 bytes c3741d94
- 004d7a48 ["INT_ADD", "register:40f0:8", ["const:4d7a48:8", "const:4:8"]]
- 004d7a48 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fa8e0 ["INT_ADD", "register:40f0:8", ["const:4fa8e0:8", "const:4:8"]]
+ 004fa8e0 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d7a48 bytes 060e1c94
+ 004fa8e0 bytes f4741d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aa902b5ff68ddc2dcb2e7f72a305df6"></a>

### [`004d7c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7c34.md) → [`004faacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004faacc.md) _ZN5Botan14Internal_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bdbcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcb0.md) [`00bdc9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9d0.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 2件 [`00c58700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58700.md) [`00c59420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59420.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fab14",
      "incomplete_value": true,
      "site": "004fab14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d7c7c",
      "incomplete_value": true,
      "site": "004d7c7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fab50",
      "incomplete_value": true,
      "site": "004fab54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d7cb8",
      "incomplete_value": true,
      "site": "004d7cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004faaec",
      "incomplete_value": false,
      "site": "004faafc",
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
            "const:bf2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7c54",
      "incomplete_value": false,
      "site": "004d7c64",
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
            "const:638:8"
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
      "004faaec",
      "PARAM",
      [
        "storage",
        "002a0638",
        null,
        "string"
      ]
    ],
    [
      "004fab08",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004fab14",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004faaec",
      "PARAM",
      [
        "storage",
        "002b0bf2",
        null,
        "string"
      ]
    ],
    [
      "004fab08",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fab14",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7c34.md#insn-004d7c64) · [`004d7c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7c34.md#insn-004d7c50) · [`004d7c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7c34.md#insn-004d7c54)
- 新版 `004faafc`（命令位置の公開資料なし） · `004faae8`（命令位置の公開資料なし） · `004faaec`（命令位置の公開資料なし）

~~~diff
- 004d7c64 ["INT_ADD", "register:40f0:8", ["const:4d7c64:8", "const:4:8"]]
- 004d7c64 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004faafc ["INT_ADD", "register:40f0:8", ["const:4faafc:8", "const:4:8"]]
+ 004faafc ["CALL", null, ["callee:00c57cb0:8"]]
- 004d7c64 bytes 7f0d1c94
+ 004faafc bytes 6d741d94
- 004d7c50 ["COPY", "register:4000:8", ["const:2a0000:8"]]
+ 004faae8 ["COPY", "register:4000:8", ["const:2b0000:8"]]
- 004d7c50 bytes 40eeffb0
+ 004faae8 bytes a0edffd0
- 004d7c54 ["COPY", "tmp:0:8", ["const:638:8"]]
- 004d7c54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d7c54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d7c54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004faaec ["COPY", "tmp:0:8", ["const:bf2:8"]]
+ 004faaec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004faaec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004faaec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d7c54 bytes 00e01891
+ 004faaec bytes 00c82f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37d5b148462ddec2c116ac148787e730"></a>

### [`004d7d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7d1c.md) → [`004fabb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fabb4.md) _ZN5Botan18Invalid_Key_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf30.md) · 呼出先 8件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c58980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58980.md) · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.40% / 新版 94.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fac88",
      "incomplete_value": true,
      "site": "004fac94",
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
                "const:126:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7df0",
      "incomplete_value": true,
      "site": "004d7dfc",
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
                "const:810:8"
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
      "definition_site": "004fac8c",
      "incomplete_value": true,
      "site": "004fac98",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7df4",
      "incomplete_value": true,
      "site": "004d7e00",
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
                "const:f:8"
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
      "definition_site": "004fad04",
      "incomplete_value": true,
      "site": "004fad08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d7e6c",
      "incomplete_value": true,
      "site": "004d7e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fac88",
      "READ",
      [
        "storage",
        "00294810",
        null,
        "string"
      ]
    ],
    [
      "004fac8c",
      "READ",
      [
        "storage",
        "0029481f",
        null,
        "string"
      ]
    ],
    [
      "004face8",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fac88",
      "READ",
      [
        "storage",
        "002a4126",
        null,
        "string"
      ]
    ],
    [
      "004fac8c",
      "READ",
      [
        "storage",
        "002a4135",
        null,
        "string"
      ]
    ],
    [
      "004face8",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7d1c.md#insn-004d7e5c) · [`004d7db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7d1c.md#insn-004d7db4) · [`004d7de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7d1c.md#insn-004d7de0)
- 新版 `004facf4`（命令位置の公開資料なし） · `004fac4c`（命令位置の公開資料なし） · `004fac78`（命令位置の公開資料なし）

~~~diff
- 004d7e5c ["INT_ADD", "register:40f0:8", ["const:4d7e5c:8", "const:4:8"]]
- 004d7e5c ["CALL", null, ["ram:bdb930:8"]]
+ 004facf4 ["INT_ADD", "register:40f0:8", ["const:4facf4:8", "const:4:8"]]
+ 004facf4 ["CALL", null, ["ram:c58380:8"]]
- 004d7e5c bytes b50e1c94
+ 004facf4 bytes a3751d94
- 004d7db4 ["INT_ADD", "register:40f0:8", ["const:4d7db4:8", "const:4:8"]]
- 004d7db4 ["CALL", null, ["callee:00c57a90:8"]]
+ 004fac4c ["INT_ADD", "register:40f0:8", ["const:4fac4c:8", "const:4:8"]]
+ 004fac4c ["CALL", null, ["callee:00c57a90:8"]]
- 004d7db4 bytes a30c1c94
+ 004fac4c bytes 91731d94
- 004d7de0 ["INT_ADD", "register:40f0:8", ["const:4d7de0:8", "const:4:8"]]
- 004d7de0 ["CALL", null, ["callee:00c57b40:8"]]
+ 004fac78 ["INT_ADD", "register:40f0:8", ["const:4fac78:8", "const:4:8"]]
+ 004fac78 ["CALL", null, ["callee:00c57b40:8"]]
- 004d7de0 bytes c40c1c94
+ 004fac78 bytes b2731d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8012ee14a7f139b4753b158641b12db"></a>

### [`004d7f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7f90.md) → [`004fae28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fae28.md) _ZN5Botan17Invalid_IV_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf40.md) · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00c58990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58990.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004faf08",
      "incomplete_value": true,
      "site": "004faf0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8070",
      "incomplete_value": true,
      "site": "004d8074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "004faf3c",
      "incomplete_value": true,
      "site": "004faf40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d80a4",
      "incomplete_value": true,
      "site": "004d80a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fae60",
      "incomplete_value": false,
      "site": "004fae6c",
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
            "const:dbd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d7fc8",
      "incomplete_value": false,
      "site": "004d7fd4",
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
            "const:550:8"
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
      "004fae60",
      "PARAM",
      [
        "storage",
        "002a4550",
        null,
        "string"
      ]
    ],
    [
      "004fae8c",
      "PARAM",
      [
        "storage",
        "0029e55f",
        null,
        "string"
      ]
    ],
    [
      "004faeec",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fae60",
      "PARAM",
      [
        "storage",
        "002b4dbd",
        null,
        "string"
      ]
    ],
    [
      "004fae8c",
      "PARAM",
      [
        "storage",
        "002ae8e4",
        null,
        "string"
      ]
    ],
    [
      "004faeec",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7f90.md#insn-004d7fd4) · [`004d7ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7f90.md#insn-004d7ffc) · [`004d8060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d7/004d7f90.md#insn-004d8060)
- 新版 `004fae6c`（命令位置の公開資料なし） · `004fae94`（命令位置の公開資料なし） · `004faef8`（命令位置の公開資料なし）

~~~diff
- 004d7fd4 ["INT_ADD", "register:40f0:8", ["const:4d7fd4:8", "const:4:8"]]
- 004d7fd4 ["CALL", null, ["callee:00c57b60:8"]]
+ 004fae6c ["INT_ADD", "register:40f0:8", ["const:4fae6c:8", "const:4:8"]]
+ 004fae6c ["CALL", null, ["callee:00c57b60:8"]]
- 004d7fd4 bytes 4f0c1c94
+ 004fae6c bytes 3d731d94
- 004d7ffc ["INT_ADD", "register:40f0:8", ["const:4d7ffc:8", "const:4:8"]]
- 004d7ffc ["CALL", null, ["callee:00c57b70:8"]]
+ 004fae94 ["INT_ADD", "register:40f0:8", ["const:4fae94:8", "const:4:8"]]
+ 004fae94 ["CALL", null, ["callee:00c57b70:8"]]
- 004d7ffc bytes 490c1c94
+ 004fae94 bytes 37731d94
- 004d8060 ["INT_ADD", "register:40f0:8", ["const:4d8060:8", "const:4:8"]]
- 004d8060 ["CALL", null, ["ram:bdb930:8"]]
+ 004faef8 ["INT_ADD", "register:40f0:8", ["const:4faef8:8", "const:4:8"]]
+ 004faef8 ["CALL", null, ["ram:c58380:8"]]
- 004d8060 bytes 340e1c94
+ 004faef8 bytes 22751d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-096a4e257390f5b7c04d98791222eda4"></a>

### [`004d81b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d81b0.md) → [`004fb048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb048.md) _ZN5Botan11Key_Not_SetC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7f0.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c58240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58240.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

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
      "definition_site": "004fb090",
      "incomplete_value": true,
      "site": "004fb090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d81f8",
      "incomplete_value": true,
      "site": "004d81f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb0ac",
      "incomplete_value": true,
      "site": "004fb0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8214",
      "incomplete_value": true,
      "site": "004d821c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb0d0",
      "incomplete_value": true,
      "site": "004fb0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8238",
      "incomplete_value": true,
      "site": "004d823c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fb068",
      "PARAM",
      [
        "storage",
        "00299c6b",
        null,
        "string"
      ]
    ],
    [
      "004fb084",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb090",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fb068",
      "PARAM",
      [
        "storage",
        "002a9b44",
        null,
        "string"
      ]
    ],
    [
      "004fb084",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb090",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d81e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d81b0.md#insn-004d81e0) · [`004d81cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d81b0.md#insn-004d81cc) · [`004d81d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d81b0.md#insn-004d81d0)
- 新版 `004fb078`（命令位置の公開資料なし） · `004fb064`（命令位置の公開資料なし） · `004fb068`（命令位置の公開資料なし）

~~~diff
- 004d81e0 ["INT_ADD", "register:40f0:8", ["const:4d81e0:8", "const:4:8"]]
- 004d81e0 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fb078 ["INT_ADD", "register:40f0:8", ["const:4fb078:8", "const:4:8"]]
+ 004fb078 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d81e0 bytes 200c1c94
+ 004fb078 bytes 0e731d94
- 004d81cc ["COPY", "register:4000:8", ["const:299000:8"]]
+ 004fb064 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 004d81cc bytes 00eeffb0
+ 004fb064 bytes 60edffd0
- 004d81d0 ["COPY", "tmp:0:8", ["const:c6b:8"]]
- 004d81d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d81d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d81d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fb068 ["COPY", "tmp:0:8", ["const:b44:8"]]
+ 004fb068 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb068 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb068 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d81d0 bytes 00ac3191
+ 004fb068 bytes 00102d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3a4067b002697af284af256bda045fc"></a>

### [`004d82b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d82b8.md) → [`004fb150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb150.md) _ZN5Botan16Policy_ViolationC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

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
      "definition_site": "004fb198",
      "incomplete_value": true,
      "site": "004fb198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8300",
      "incomplete_value": true,
      "site": "004d8300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb1b4",
      "incomplete_value": true,
      "site": "004fb1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d831c",
      "incomplete_value": true,
      "site": "004d8324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb1d8",
      "incomplete_value": true,
      "site": "004fb1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8340",
      "incomplete_value": true,
      "site": "004d8344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fb170",
      "PARAM",
      [
        "storage",
        "002a95ff",
        null,
        "string"
      ]
    ],
    [
      "004fb18c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb198",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fb170",
      "PARAM",
      [
        "storage",
        "002ba2a2",
        null,
        "string"
      ]
    ],
    [
      "004fb18c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb198",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d82e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d82b8.md#insn-004d82e8) · [`004d82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d82b8.md#insn-004d82d4) · [`004d82d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d82b8.md#insn-004d82d8)
- 新版 `004fb180`（命令位置の公開資料なし） · `004fb16c`（命令位置の公開資料なし） · `004fb170`（命令位置の公開資料なし）

~~~diff
- 004d82e8 ["INT_ADD", "register:40f0:8", ["const:4d82e8:8", "const:4:8"]]
- 004d82e8 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fb180 ["INT_ADD", "register:40f0:8", ["const:4fb180:8", "const:4:8"]]
+ 004fb180 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d82e8 bytes de0b1c94
+ 004fb180 bytes cc721d94
- 004d82d4 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 004fb16c ["COPY", "register:4000:8", ["const:2ba000:8"]]
- 004d82d4 bytes 80eeffb0
+ 004fb16c bytes e0edfff0
- 004d82d8 ["COPY", "tmp:0:8", ["const:5ff:8"]]
- 004d82d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d82d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d82d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fb170 ["COPY", "tmp:0:8", ["const:2a2:8"]]
+ 004fb170 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb170 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb170 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d82d8 bytes 00fc1791
+ 004fb170 bytes 00880a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b88ebc0c00c1c0813623962d1c7e45b4"></a>

### [`004d83c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d83c0.md) → [`004fb258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb258.md) _ZN5Botan13PRNG_UnseededC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd130.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c59b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b80.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

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
      "definition_site": "004fb2a0",
      "incomplete_value": true,
      "site": "004fb2a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8408",
      "incomplete_value": true,
      "site": "004d8408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb2bc",
      "incomplete_value": true,
      "site": "004fb2c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8424",
      "incomplete_value": true,
      "site": "004d842c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb2e0",
      "incomplete_value": true,
      "site": "004fb2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8448",
      "incomplete_value": true,
      "site": "004d844c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fb278",
      "PARAM",
      [
        "storage",
        "002afaef",
        null,
        "string"
      ]
    ],
    [
      "004fb294",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb2a0",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fb278",
      "PARAM",
      [
        "storage",
        "002c1113",
        null,
        "string"
      ]
    ],
    [
      "004fb294",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb2a0",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d83f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d83c0.md#insn-004d83f0) · [`004d83dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d83c0.md#insn-004d83dc) · [`004d83e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d83c0.md#insn-004d83e0)
- 新版 `004fb288`（命令位置の公開資料なし） · `004fb274`（命令位置の公開資料なし） · `004fb278`（命令位置の公開資料なし）

~~~diff
- 004d83f0 ["INT_ADD", "register:40f0:8", ["const:4d83f0:8", "const:4:8"]]
- 004d83f0 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fb288 ["INT_ADD", "register:40f0:8", ["const:4fb288:8", "const:4:8"]]
+ 004fb288 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d83f0 bytes 9c0b1c94
+ 004fb288 bytes 8a721d94
- 004d83dc ["COPY", "register:4000:8", ["const:2af000:8"]]
+ 004fb274 ["COPY", "register:4000:8", ["const:2c1000:8"]]
- 004d83dc bytes a0eefff0
+ 004fb274 bytes 20eeffd0
- 004d83e0 ["COPY", "tmp:0:8", ["const:aef:8"]]
- 004d83e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d83e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d83e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fb278 ["COPY", "tmp:0:8", ["const:113:8"]]
+ 004fb278 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb278 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb278 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d83e0 bytes 00bc2b91
+ 004fb278 bytes 004c0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d690d446cc8f4392846498b5bdefd2bb"></a>

### [`004d84c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d84c8.md) → [`004fb360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb360.md) _ZN5Botan19Algorithm_Not_FoundC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb3d4",
      "incomplete_value": true,
      "site": "004fb3d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d853c",
      "incomplete_value": true,
      "site": "004d853c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb3fc",
      "incomplete_value": true,
      "site": "004fb400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8564",
      "incomplete_value": true,
      "site": "004d8568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "004fb41c",
      "incomplete_value": true,
      "site": "004fb420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8584",
      "incomplete_value": true,
      "site": "004d8588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fb380",
      "PARAM",
      [
        "storage",
        "002a1617",
        null,
        "string"
      ]
    ],
    [
      "004fb398",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "004fb3c0",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fb380",
      "PARAM",
      [
        "storage",
        "002b1c63",
        null,
        "string"
      ]
    ],
    [
      "004fb398",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      "004fb3c0",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d84f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d84c8.md#insn-004d84f8) · [`004d8508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d84c8.md#insn-004d8508) · [`004d84e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d84c8.md#insn-004d84e4)
- 新版 `004fb390`（命令位置の公開資料なし） · `004fb3a0`（命令位置の公開資料なし） · `004fb37c`（命令位置の公開資料なし）

~~~diff
- 004d84f8 ["INT_ADD", "register:40f0:8", ["const:4d84f8:8", "const:4:8"]]
- 004d84f8 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fb390 ["INT_ADD", "register:40f0:8", ["const:4fb390:8", "const:4:8"]]
+ 004fb390 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d84f8 bytes 5a0b1c94
+ 004fb390 bytes 48721d94
- 004d8508 ["INT_ADD", "register:40f0:8", ["const:4d8508:8", "const:4:8"]]
- 004d8508 ["CALL", null, ["callee:00c57b70:8"]]
+ 004fb3a0 ["INT_ADD", "register:40f0:8", ["const:4fb3a0:8", "const:4:8"]]
+ 004fb3a0 ["CALL", null, ["callee:00c57b70:8"]]
- 004d8508 bytes 060b1c94
+ 004fb3a0 bytes f4711d94
- 004d84e4 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 004fb37c ["COPY", "register:4000:8", ["const:2b1000:8"]]
- 004d84e4 bytes 40eeffb0
+ 004fb37c bytes a0edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61c87b410402cd503f849b2fa03dd130"></a>

### [`004d8628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8628.md) → [`004fb4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb4c0.md) _ZN5Botan17No_Provider_FoundC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

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
      "definition_site": "004fb534",
      "incomplete_value": true,
      "site": "004fb534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d869c",
      "incomplete_value": true,
      "site": "004d869c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb56c",
      "incomplete_value": true,
      "site": "004fb570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d86d4",
      "incomplete_value": true,
      "site": "004d86d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "004fb4e0",
      "incomplete_value": false,
      "site": "004fb4f0",
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
            "const:4a3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8648",
      "incomplete_value": false,
      "site": "004d8658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:a6a:8"
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
      "004fb4e0",
      "PARAM",
      [
        "storage",
        "00295a6a",
        null,
        "string"
      ]
    ],
    [
      "004fb4f8",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "004fb520",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fb4e0",
      "PARAM",
      [
        "storage",
        "002a54a3",
        null,
        "string"
      ]
    ],
    [
      "004fb4f8",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      "004fb520",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8628.md#insn-004d8658) · [`004d8668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8628.md#insn-004d8668) · [`004d8644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8628.md#insn-004d8644)
- 新版 `004fb4f0`（命令位置の公開資料なし） · `004fb500`（命令位置の公開資料なし） · `004fb4dc`（命令位置の公開資料なし）

~~~diff
- 004d8658 ["INT_ADD", "register:40f0:8", ["const:4d8658:8", "const:4:8"]]
- 004d8658 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fb4f0 ["INT_ADD", "register:40f0:8", ["const:4fb4f0:8", "const:4:8"]]
+ 004fb4f0 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d8658 bytes 020b1c94
+ 004fb4f0 bytes f0711d94
- 004d8668 ["INT_ADD", "register:40f0:8", ["const:4d8668:8", "const:4:8"]]
- 004d8668 ["CALL", null, ["callee:00c57b70:8"]]
+ 004fb500 ["INT_ADD", "register:40f0:8", ["const:4fb500:8", "const:4:8"]]
+ 004fb500 ["CALL", null, ["callee:00c57b70:8"]]
- 004d8668 bytes ae0a1c94
+ 004fb500 bytes 9c711d94
- 004d8644 ["COPY", "register:4000:8", ["const:295000:8"]]
+ 004fb4dc ["COPY", "register:4000:8", ["const:2a5000:8"]]
- 004d8644 bytes e0edffb0
+ 004fb4dc bytes 40edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bf07e20b9c6740727355665f0a5fff8"></a>

### [`004d8768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8768.md) → [`004fb600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb600.md) _ZN5Botan18Provider_Not_FoundC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc920.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00c59370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59370.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.21% / 新版 91.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb6b4",
      "incomplete_value": true,
      "site": "004fb6b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d881c",
      "incomplete_value": true,
      "site": "004d881c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb6dc",
      "incomplete_value": true,
      "site": "004fb6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8844",
      "incomplete_value": true,
      "site": "004d8848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb70c",
      "incomplete_value": true,
      "site": "004fb710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8874",
      "incomplete_value": true,
      "site": "004d8878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fb628",
      "PARAM",
      [
        "storage",
        "0029284e",
        null,
        "string"
      ]
    ],
    [
      "004fb640",
      "PARAM",
      [
        "storage",
        "0029c676",
        null,
        "string"
      ]
    ],
    [
      "004fb6a0",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fb628",
      "PARAM",
      [
        "storage",
        "002a1f5e",
        null,
        "string"
      ]
    ],
    [
      "004fb640",
      "PARAM",
      [
        "storage",
        "002ac80f",
        null,
        "string"
      ]
    ],
    [
      "004fb6a0",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d87a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8768.md#insn-004d87a0) · [`004d87b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8768.md#insn-004d87b0) · [`004d878c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8768.md#insn-004d878c)
- 新版 `004fb638`（命令位置の公開資料なし） · `004fb648`（命令位置の公開資料なし） · `004fb624`（命令位置の公開資料なし）

~~~diff
- 004d87a0 ["INT_ADD", "register:40f0:8", ["const:4d87a0:8", "const:4:8"]]
- 004d87a0 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fb638 ["INT_ADD", "register:40f0:8", ["const:4fb638:8", "const:4:8"]]
+ 004fb638 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d87a0 bytes b00a1c94
+ 004fb638 bytes 9e711d94
- 004d87b0 ["INT_ADD", "register:40f0:8", ["const:4d87b0:8", "const:4:8"]]
- 004d87b0 ["CALL", null, ["callee:00c57b70:8"]]
+ 004fb648 ["INT_ADD", "register:40f0:8", ["const:4fb648:8", "const:4:8"]]
+ 004fb648 ["CALL", null, ["callee:00c57b70:8"]]
- 004d87b0 bytes 5c0a1c94
+ 004fb648 bytes 4a711d94
- 004d878c ["COPY", "register:4000:8", ["const:292000:8"]]
+ 004fb624 ["COPY", "register:4000:8", ["const:2a1000:8"]]
- 004d878c bytes c0edffd0
+ 004fb624 bytes 20edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-061dcb36ddbf04be6d6aa930e27ed248"></a>

### [`004d8930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8930.md) → [`004fb7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb7c8.md) _ZN5Botan22Invalid_Algorithm_NameC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc450.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c58ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ea0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb818",
      "incomplete_value": true,
      "site": "004fb81c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8980",
      "incomplete_value": true,
      "site": "004d8984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb834",
      "incomplete_value": true,
      "site": "004fb838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d899c",
      "incomplete_value": true,
      "site": "004d89a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb7e4",
      "incomplete_value": false,
      "site": "004fb7f4",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d894c",
      "incomplete_value": false,
      "site": "004d895c",
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
            "const:575:8"
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
      "004fb7e4",
      "PARAM",
      [
        "storage",
        "0029f575",
        null,
        "string"
      ]
    ],
    [
      "004fb7fc",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004fb808",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb930"
      ]
    ]
  ],
  "added": [
    [
      "004fb7e4",
      "PARAM",
      [
        "storage",
        "002af988",
        null,
        "string"
      ]
    ],
    [
      "004fb7fc",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "004fb808",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58380"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d895c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8930.md#insn-004d895c) · [`004d8970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8930.md#insn-004d8970) · [`004d8948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8930.md#insn-004d8948)
- 新版 `004fb7f4`（命令位置の公開資料なし） · `004fb808`（命令位置の公開資料なし） · `004fb7e0`（命令位置の公開資料なし）

~~~diff
- 004d895c ["INT_ADD", "register:40f0:8", ["const:4d895c:8", "const:4:8"]]
- 004d895c ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fb7f4 ["INT_ADD", "register:40f0:8", ["const:4fb7f4:8", "const:4:8"]]
+ 004fb7f4 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d895c bytes 410a1c94
+ 004fb7f4 bytes 2f711d94
- 004d8970 ["INT_ADD", "register:40f0:8", ["const:4d8970:8", "const:4:8"]]
- 004d8970 ["CALL", null, ["ram:bdb930:8"]]
+ 004fb808 ["INT_ADD", "register:40f0:8", ["const:4fb808:8", "const:4:8"]]
+ 004fb808 ["CALL", null, ["ram:c58380:8"]]
- 004d8970 bytes f00b1c94
+ 004fb808 bytes de721d94
- 004d8948 ["COPY", "register:4000:8", ["const:29f000:8"]]
+ 004fb7e0 ["COPY", "register:4000:8", ["const:2af000:8"]]
- 004d8948 bytes 20eefff0
+ 004fb7e0 bytes a0edff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a3a49011ce3d220034abc6f4787eaf2"></a>

### [`004d89f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d89f4.md) → [`004fb88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb88c.md) _ZN5Botan14Encoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9e0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c58430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58430.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb8dc",
      "incomplete_value": true,
      "site": "004fb8e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8a44",
      "incomplete_value": true,
      "site": "004d8a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb8f8",
      "incomplete_value": true,
      "site": "004fb8fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8a60",
      "incomplete_value": true,
      "site": "004d8a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb8a8",
      "incomplete_value": false,
      "site": "004fb8b8",
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
            "const:bcf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8a10",
      "incomplete_value": false,
      "site": "004d8a20",
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
            "const:e11:8"
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
      "004fb8a8",
      "PARAM",
      [
        "storage",
        "00298e11",
        null,
        "string"
      ]
    ],
    [
      "004fb8c0",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004fb8cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb930"
      ]
    ]
  ],
  "added": [
    [
      "004fb8a8",
      "PARAM",
      [
        "storage",
        "002a8bcf",
        null,
        "string"
      ]
    ],
    [
      "004fb8c0",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "004fb8cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58380"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d89f4.md#insn-004d8a20) · [`004d8a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d89f4.md#insn-004d8a34) · [`004d8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d89f4.md#insn-004d8a0c)
- 新版 `004fb8b8`（命令位置の公開資料なし） · `004fb8cc`（命令位置の公開資料なし） · `004fb8a4`（命令位置の公開資料なし）

~~~diff
- 004d8a20 ["INT_ADD", "register:40f0:8", ["const:4d8a20:8", "const:4:8"]]
- 004d8a20 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fb8b8 ["INT_ADD", "register:40f0:8", ["const:4fb8b8:8", "const:4:8"]]
+ 004fb8b8 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d8a20 bytes 100a1c94
+ 004fb8b8 bytes fe701d94
- 004d8a34 ["INT_ADD", "register:40f0:8", ["const:4d8a34:8", "const:4:8"]]
- 004d8a34 ["CALL", null, ["ram:bdb930:8"]]
+ 004fb8cc ["INT_ADD", "register:40f0:8", ["const:4fb8cc:8", "const:4:8"]]
+ 004fb8cc ["CALL", null, ["ram:c58380:8"]]
- 004d8a34 bytes bf0b1c94
+ 004fb8cc bytes ad721d94
- 004d8a0c ["COPY", "register:4000:8", ["const:298000:8"]]
+ 004fb8a4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 004d8a0c bytes 00eeff90
+ 004fb8a4 bytes 60edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0a7873f1198d17127c5342587e39468"></a>

### [`004d8ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8ab8.md) → [`004fb950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb950.md) _ZN5Botan14Decoding_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKc

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcfa0.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c599f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599f0.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb9f4",
      "incomplete_value": true,
      "site": "004fb9f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8b5c",
      "incomplete_value": true,
      "site": "004d8b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fba20",
      "incomplete_value": true,
      "site": "004fba24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8b88",
      "incomplete_value": true,
      "site": "004d8b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fb970",
      "incomplete_value": false,
      "site": "004fb984",
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
            "const:de4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8ad8",
      "incomplete_value": false,
      "site": "004d8aec",
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
            "const:900:8"
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
      "004fb970",
      "PARAM",
      [
        "storage",
        "002ae900",
        null,
        "string"
      ]
    ],
    [
      "004fb98c",
      "PARAM",
      [
        "storage",
        "00292868",
        null,
        "string"
      ]
    ],
    [
      "004fb9d8",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fb970",
      "PARAM",
      [
        "storage",
        "002bfde4",
        null,
        "string"
      ]
    ],
    [
      "004fb98c",
      "PARAM",
      [
        "storage",
        "002a1f78",
        null,
        "string"
      ]
    ],
    [
      "004fb9d8",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8ab8.md#insn-004d8aec) · [`004d8afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8ab8.md#insn-004d8afc) · [`004d8b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8ab8.md#insn-004d8b4c)
- 新版 `004fb984`（命令位置の公開資料なし） · `004fb994`（命令位置の公開資料なし） · `004fb9e4`（命令位置の公開資料なし）

~~~diff
- 004d8aec ["INT_ADD", "register:40f0:8", ["const:4d8aec:8", "const:4:8"]]
- 004d8aec ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fb984 ["INT_ADD", "register:40f0:8", ["const:4fb984:8", "const:4:8"]]
+ 004fb984 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d8aec bytes dd091c94
+ 004fb984 bytes cb701d94
- 004d8afc ["INT_ADD", "register:40f0:8", ["const:4d8afc:8", "const:4:8"]]
- 004d8afc ["CALL", null, ["callee:00c57b70:8"]]
+ 004fb994 ["INT_ADD", "register:40f0:8", ["const:4fb994:8", "const:4:8"]]
+ 004fb994 ["CALL", null, ["callee:00c57b70:8"]]
- 004d8afc bytes 89091c94
+ 004fb994 bytes 77701d94
- 004d8b4c ["INT_ADD", "register:40f0:8", ["const:4d8b4c:8", "const:4:8"]]
- 004d8b4c ["CALL", null, ["ram:bdb930:8"]]
+ 004fb9e4 ["INT_ADD", "register:40f0:8", ["const:4fb9e4:8", "const:4:8"]]
+ 004fb9e4 ["CALL", null, ["ram:c58380:8"]]
- 004d8b4c bytes 790b1c94
+ 004fb9e4 bytes 67721d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9b3dec8d7eb1b2af9541bcedec4220f"></a>

### [`004d8c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8c5c.md) → [`004fbaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbaf4.md) _ZN5Botan17Integrity_FailureC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbb3c",
      "incomplete_value": true,
      "site": "004fbb3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8ca4",
      "incomplete_value": true,
      "site": "004d8ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbb78",
      "incomplete_value": true,
      "site": "004fbb7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8ce0",
      "incomplete_value": true,
      "site": "004d8ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fbb14",
      "incomplete_value": false,
      "site": "004fbb24",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8c7c",
      "incomplete_value": false,
      "site": "004d8c8c",
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
            "const:a7b:8"
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
      "004fbb14",
      "PARAM",
      [
        "storage",
        "00296a7b",
        null,
        "string"
      ]
    ],
    [
      "004fbb30",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbb3c",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fbb14",
      "PARAM",
      [
        "storage",
        "002a65b0",
        null,
        "string"
      ]
    ],
    [
      "004fbb30",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbb3c",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8c5c.md#insn-004d8c8c) · [`004d8c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8c5c.md#insn-004d8c78) · [`004d8c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8c5c.md#insn-004d8c7c)
- 新版 `004fbb24`（命令位置の公開資料なし） · `004fbb10`（命令位置の公開資料なし） · `004fbb14`（命令位置の公開資料なし）

~~~diff
- 004d8c8c ["INT_ADD", "register:40f0:8", ["const:4d8c8c:8", "const:4:8"]]
- 004d8c8c ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fbb24 ["INT_ADD", "register:40f0:8", ["const:4fbb24:8", "const:4:8"]]
+ 004fbb24 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d8c8c bytes 75091c94
+ 004fbb24 bytes 63701d94
- 004d8c78 ["COPY", "register:4000:8", ["const:296000:8"]]
+ 004fbb10 ["COPY", "register:4000:8", ["const:2a6000:8"]]
- 004d8c78 bytes e0edffd0
+ 004fbb10 bytes 40edfff0
- 004d8c7c ["COPY", "tmp:0:8", ["const:a7b:8"]]
- 004d8c7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8c7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8c7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fbb14 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 004fbb14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbb14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbb14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8c7c bytes 00ec2991
+ 004fbb14 bytes 00c01691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32c5907e0921686119d181446036183b"></a>

### [`004d8d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8d44.md) → [`004fbbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbbdc.md) _ZN5Botan11Invalid_OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb990.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c583e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583e0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbc40",
      "incomplete_value": true,
      "site": "004fbc44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8da8",
      "incomplete_value": true,
      "site": "004d8dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbc60",
      "incomplete_value": true,
      "site": "004fbc64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8dc8",
      "incomplete_value": true,
      "site": "004d8dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbc7c",
      "incomplete_value": true,
      "site": "004fbc80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8de4",
      "incomplete_value": true,
      "site": "004d8de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fbbf8",
      "PARAM",
      [
        "storage",
        "002a9612",
        null,
        "string"
      ]
    ],
    [
      "004fbc10",
      "PARAM",
      [
        "storage",
        "002ae900",
        null,
        "string"
      ]
    ],
    [
      "004fbc24",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fbbf8",
      "PARAM",
      [
        "storage",
        "002ba2b5",
        null,
        "string"
      ]
    ],
    [
      "004fbc10",
      "PARAM",
      [
        "storage",
        "002bfde4",
        null,
        "string"
      ]
    ],
    [
      "004fbc24",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8d44.md#insn-004d8d70) · [`004d8d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8d44.md#insn-004d8d84) · [`004d8d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8d44.md#insn-004d8d98)
- 新版 `004fbc08`（命令位置の公開資料なし） · `004fbc1c`（命令位置の公開資料なし） · `004fbc30`（命令位置の公開資料なし）

~~~diff
- 004d8d70 ["INT_ADD", "register:40f0:8", ["const:4d8d70:8", "const:4:8"]]
- 004d8d70 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fbc08 ["INT_ADD", "register:40f0:8", ["const:4fbc08:8", "const:4:8"]]
+ 004fbc08 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d8d70 bytes 3c091c94
+ 004fbc08 bytes 2a701d94
- 004d8d84 ["INT_ADD", "register:40f0:8", ["const:4d8d84:8", "const:4:8"]]
- 004d8d84 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fbc1c ["INT_ADD", "register:40f0:8", ["const:4fbc1c:8", "const:4:8"]]
+ 004fbc1c ["CALL", null, ["callee:00c57cb0:8"]]
- 004d8d84 bytes 37091c94
+ 004fbc1c bytes 25701d94
- 004d8d98 ["INT_ADD", "register:40f0:8", ["const:4d8d98:8", "const:4:8"]]
- 004d8d98 ["CALL", null, ["ram:bdb930:8"]]
+ 004fbc30 ["INT_ADD", "register:40f0:8", ["const:4fbc30:8", "const:4:8"]]
+ 004fbc30 ["CALL", null, ["ram:c58380:8"]]
- 004d8d98 bytes e60a1c94
+ 004fbc30 bytes d4711d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb13e921795aba31ca8f8cd6a3f5999f"></a>

### [`004d8e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8e54.md) → [`004fbcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbcec.md) _ZN5Botan15Stream_IO_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb960.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c583b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583b0.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbd34",
      "incomplete_value": true,
      "site": "004fbd34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8e9c",
      "incomplete_value": true,
      "site": "004d8e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbd70",
      "incomplete_value": true,
      "site": "004fbd74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8ed8",
      "incomplete_value": true,
      "site": "004d8edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fbd0c",
      "incomplete_value": false,
      "site": "004fbd1c",
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
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8e74",
      "incomplete_value": false,
      "site": "004d8e84",
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
            "const:55b:8"
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
      "004fbd0c",
      "PARAM",
      [
        "storage",
        "002a455b",
        null,
        "string"
      ]
    ],
    [
      "004fbd28",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbd34",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fbd0c",
      "PARAM",
      [
        "storage",
        "002b4dc8",
        null,
        "string"
      ]
    ],
    [
      "004fbd28",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbd34",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8e54.md#insn-004d8e84) · [`004d8e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8e54.md#insn-004d8e70) · [`004d8e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8e54.md#insn-004d8e74)
- 新版 `004fbd1c`（命令位置の公開資料なし） · `004fbd08`（命令位置の公開資料なし） · `004fbd0c`（命令位置の公開資料なし）

~~~diff
- 004d8e84 ["INT_ADD", "register:40f0:8", ["const:4d8e84:8", "const:4:8"]]
- 004d8e84 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fbd1c ["INT_ADD", "register:40f0:8", ["const:4fbd1c:8", "const:4:8"]]
+ 004fbd1c ["CALL", null, ["callee:00c57cb0:8"]]
- 004d8e84 bytes f7081c94
+ 004fbd1c bytes e56f1d94
- 004d8e70 ["COPY", "register:4000:8", ["const:2a4000:8"]]
+ 004fbd08 ["COPY", "register:4000:8", ["const:2b4000:8"]]
- 004d8e70 bytes 60eeff90
+ 004fbd08 bytes c0edffb0
- 004d8e74 ["COPY", "tmp:0:8", ["const:55b:8"]]
- 004d8e74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8e74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8e74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fbd0c ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 004fbd0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbd0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbd0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8e74 bytes 006c1591
+ 004fbd0c bytes 00203791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8cba5f7cd730f95c457a43f62520081"></a>

### [`004d8f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8f3c.md) → [`004fbdd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbdd4.md) _ZN5Botan17Self_Test_FailureC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c59420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59420.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbe28",
      "incomplete_value": true,
      "site": "004fbe2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d8f90",
      "incomplete_value": true,
      "site": "004d8f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fbdf0",
      "incomplete_value": false,
      "site": "004fbe00",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8f58",
      "incomplete_value": false,
      "site": "004d8f68",
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
            "const:63c:8"
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
      "004fbdf0",
      "PARAM",
      [
        "storage",
        "002a163c",
        null,
        "string"
      ]
    ],
    [
      "004fbe24",
      "READ",
      [
        "storage",
        "00c1b2c0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbe2c",
      "DATA",
      [
        "storage",
        "00bea738",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fbdf0",
      "PARAM",
      [
        "storage",
        "002b1c88",
        null,
        "string"
      ]
    ],
    [
      "004fbe24",
      "READ",
      [
        "storage",
        "00c9acb0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbe2c",
      "DATA",
      [
        "storage",
        "00c672f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d8f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8f3c.md#insn-004d8f68) · [`004d8f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8f3c.md#insn-004d8f54) · [`004d8f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8f3c.md#insn-004d8f58)
- 新版 `004fbe00`（命令位置の公開資料なし） · `004fbdec`（命令位置の公開資料なし） · `004fbdf0`（命令位置の公開資料なし）

~~~diff
- 004d8f68 ["INT_ADD", "register:40f0:8", ["const:4d8f68:8", "const:4:8"]]
- 004d8f68 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fbe00 ["INT_ADD", "register:40f0:8", ["const:4fbe00:8", "const:4:8"]]
+ 004fbe00 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d8f68 bytes be081c94
+ 004fbe00 bytes ac6f1d94
- 004d8f54 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 004fbdec ["COPY", "register:4000:8", ["const:2b1000:8"]]
- 004d8f54 bytes 40eeffb0
+ 004fbdec bytes a0edffd0
- 004d8f58 ["COPY", "tmp:0:8", ["const:63c:8"]]
- 004d8f58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d8f58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d8f58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fbdf0 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 004fbdf0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbdf0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbdf0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d8f58 bytes 00f01891
+ 004fbdf0 bytes 00203291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57f079d5f442a2c26508010e526836c6"></a>

### [`004d8fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8fe8.md) → [`004fbe80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbe80.md) _ZN5Botan15Not_ImplementedC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc690.md) · 呼出先 1件 [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)
- 新版 呼出元 1件 [`00c590e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590e0.md) · 呼出先 1件 [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbea8",
      "incomplete_value": true,
      "site": "004fbeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004d9010",
      "incomplete_value": true,
      "site": "004d9014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004fbe9c",
      "value": [
        "leaf",
        "ram:c58380:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d9004",
      "value": [
        "leaf",
        "ram:bdb930:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fbe94",
      "incomplete_value": false,
      "site": "004fbe9c",
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
            "const:9a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d8ffc",
      "incomplete_value": false,
      "site": "004d9004",
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
            "const:58e:8"
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
      "004fbe94",
      "PARAM",
      [
        "storage",
        "0029f58e",
        null,
        "string"
      ]
    ],
    [
      "004fbe9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb930"
      ]
    ],
    [
      "004fbea4",
      "READ",
      [
        "storage",
        "00c1b2c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fbe94",
      "PARAM",
      [
        "storage",
        "002af9a1",
        null,
        "string"
      ]
    ],
    [
      "004fbe9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58380"
      ]
    ],
    [
      "004fbea4",
      "READ",
      [
        "storage",
        "00c9acb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d9004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8fe8.md#insn-004d9004) · [`004d8ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8fe8.md#insn-004d8ff8) · [`004d8ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8fe8.md#insn-004d8ffc)
- 新版 `004fbe9c`（命令位置の公開資料なし） · `004fbe90`（命令位置の公開資料なし） · `004fbe94`（命令位置の公開資料なし）

~~~diff
- 004d9004 ["INT_ADD", "register:40f0:8", ["const:4d9004:8", "const:4:8"]]
- 004d9004 ["CALL", null, ["ram:bdb930:8"]]
+ 004fbe9c ["INT_ADD", "register:40f0:8", ["const:4fbe9c:8", "const:4:8"]]
+ 004fbe9c ["CALL", null, ["ram:c58380:8"]]
- 004d9004 bytes 4b0a1c94
+ 004fbe9c bytes 39711d94
- 004d8ff8 ["COPY", "register:4008:8", ["const:29f000:8"]]
+ 004fbe90 ["COPY", "register:4008:8", ["const:2af000:8"]]
- 004d8ff8 bytes 21eefff0
+ 004fbe90 bytes a1edff90
- 004d8ffc ["COPY", "tmp:0:8", ["const:58e:8"]]
- 004d8ffc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d8ffc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d8ffc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fbe94 ["COPY", "tmp:0:8", ["const:9a1:8"]]
+ 004fbe94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fbe94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fbe94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d8ffc bytes 21381691
+ 004fbe94 bytes 21842691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fb81ccb59f5dd72d0853d363ce719e8"></a>

### [`004d9024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9024.md) → [`004fbebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md) _ZN5Botan19get_files_recursiveERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9e0.md) · 呼出先 20件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00517044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517044.md) [`005171dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/005171dc.md)
- 新版 呼出元 1件 [`00c59430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59430.md) · 呼出先 20件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00539edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539edc.md) [`0053a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.11% / 新版 99.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004fc0e0",
      "incomplete_value": false,
      "site": "004fc0e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:f48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d9248",
      "incomplete_value": false,
      "site": "004d9248",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fc0f4",
      "incomplete_value": true,
      "site": "004fc0f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d925c",
      "incomplete_value": true,
      "site": "004d925c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fc0e0",
      "DATA",
      [
        "storage",
        "00bed388",
        null,
        "undefined *"
      ]
    ],
    [
      "004fc0f0",
      "READ",
      [
        "storage",
        "00c1b2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fc0f4",
      "DATA",
      [
        "storage",
        "010a5148",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004fc0e0",
      "DATA",
      [
        "storage",
        "00c69f48",
        null,
        "undefined *"
      ]
    ],
    [
      "004fc0f0",
      "READ",
      [
        "storage",
        "00c9acc0",
        null,
        "pointer"
      ]
    ],
    [
      "004fc0f4",
      "DATA",
      [
        "storage",
        "0112a148",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d9080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9024.md#insn-004d9080) · [`004d90ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9024.md#insn-004d90ec) · [`004d9104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9024.md#insn-004d9104)
- 新版 `004fbf18`（命令位置の公開資料なし） · `004fbf84`（命令位置の公開資料なし） · `004fbf9c`（命令位置の公開資料なし）

~~~diff
- 004d9080 ["INT_ADD", "register:40f0:8", ["const:4d9080:8", "const:4:8"]]
- 004d9080 ["CALL", null, ["callee:0053a074:8"]]
+ 004fbf18 ["INT_ADD", "register:40f0:8", ["const:4fbf18:8", "const:4:8"]]
+ 004fbf18 ["CALL", null, ["callee:0053a074:8"]]
- 004d9080 bytes 57f80094
+ 004fbf18 bytes 57f80094
- 004d90ec ["INT_ADD", "register:40f0:8", ["const:4d90ec:8", "const:4:8"]]
- 004d90ec ["CALL", null, ["callee:0043bae0:8"]]
+ 004fbf84 ["INT_ADD", "register:40f0:8", ["const:4fbf84:8", "const:4:8"]]
+ 004fbf84 ["CALL", null, ["callee:0043bae0:8"]]
- 004d90ec bytes bdfffc97
+ 004fbf84 bytes d7fefc97
- 004d9104 ["INT_ADD", "register:40f0:8", ["const:4d9104:8", "const:4:8"]]
- 004d9104 ["CALL", null, ["callee:00539edc:8"]]
+ 004fbf9c ["INT_ADD", "register:40f0:8", ["const:4fbf9c:8", "const:4:8"]]
+ 004fbf9c ["CALL", null, ["callee:00539edc:8"]]
- 004d9104 bytes d0f70094
+ 004fbf9c bytes d0f70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df6f469e423e9483afb7da332c295689"></a>

### [`004d989c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d989c.md) → [`004fc734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc734.md) _ZN5Botan15allocate_memoryEmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdca20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca20.md) · 呼出先 5件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbe0.md) [`00bdbbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbf0.md)
- 新版 呼出元 1件 [`00c59470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59470.md) · 呼出先 5件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58630.md) [`00c58640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58640.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004fc760",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d98c8",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fc770",
      "incomplete_value": true,
      "site": "004fc778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d98d8",
      "incomplete_value": true,
      "site": "004d98e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fc774",
      "incomplete_value": true,
      "site": "004fc778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d98dc",
      "incomplete_value": true,
      "site": "004d98e0",
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
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fc760",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "004fc770",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004fc770",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004fc760",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "004fc770",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004fc770",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d98c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d989c.md#insn-004d98c8) · [`004d98e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d989c.md#insn-004d98e0) · [`004d98a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d989c.md#insn-004d98a8)
- 新版 `004fc760`（命令位置の公開資料なし） · `004fc778`（命令位置の公開資料なし） · `004fc740`（命令位置の公開資料なし）

~~~diff
- 004d98c8 ["INT_ADD", "register:40f0:8", ["const:4d98c8:8", "const:4:8"]]
- 004d98c8 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004fc760 ["INT_ADD", "register:40f0:8", ["const:4fc760:8", "const:4:8"]]
+ 004fc760 ["CALL", null, ["ram:c58640:8"]]
- 004d98c8 bytes ca081c94
+ 004fc760 bytes b86f1d94
- 004d98e0 ["INT_ADD", "register:40f0:8", ["const:4d98e0:8", "const:4:8"]]
- 004d98e0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004fc778 ["INT_ADD", "register:40f0:8", ["const:4fc778:8", "const:4:8"]]
+ 004fc778 ["CALL", null, ["callee:00c57b10:8"]]
- 004d98e0 bytes f8051c94
+ 004fc778 bytes e66c1d94
- 004d98a8 ["INT_ADD", "register:40f0:8", ["const:4d98a8:8", "const:4:8"]]
- 004d98a8 ["CALL", null, ["callee:00c58630:8"]]
+ 004fc740 ["INT_ADD", "register:40f0:8", ["const:4fc740:8", "const:4:8"]]
+ 004fc740 ["CALL", null, ["callee:00c58630:8"]]
- 004d98a8 bytes ce081c94
+ 004fc740 bytes bc6f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1714f69a0a250fe5aadc6589e33997a6"></a>

### [`004d98e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d98e4.md) → [`004fc77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc77c.md) _ZN5Botan17deallocate_memoryEPvmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdca30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca30.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00c59480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59480.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fc7a0",
      "incomplete_value": true,
      "site": "004fc7a0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
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
    "old": {
      "definition_site": "004d9908",
      "incomplete_value": true,
      "site": "004d9908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004fc798",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fc798",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d9908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d98e4.md#insn-004d9908) · [`004d98f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d98e4.md#insn-004d98f8) · [`004d9900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d98e4.md#insn-004d9900)
- 新版 `004fc7a0`（命令位置の公開資料なし） · `004fc790`（命令位置の公開資料なし） · `004fc798`（命令位置の公開資料なし）

~~~diff
- 004d9908 ["COPY", "register:0:8", ["register:4040:8"]]
- 004d9908 ["INT_ADD", "register:40f0:8", ["const:4d9908:8", "const:4:8"]]
- 004d9908 ["CALLIND", null, ["register:0:8"]]
+ 004fc7a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004fc7a0 ["INT_ADD", "register:40f0:8", ["const:4fc7a0:8", "const:4:8"]]
+ 004fc7a0 ["CALLIND", null, ["register:0:8"]]
- 004d9908 bytes 00013fd6
+ 004fc7a0 bytes 00013fd6
- 004d98f8 ["COPY", "register:4040:8", ["const:bea000:8"]]
+ 004fc790 ["COPY", "register:4040:8", ["const:c67000:8"]]
- 004d98f8 bytes 883800b0
+ 004fc790 bytes 483b00f0
- 004d9900 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:778:8"]]
- 004d9900 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fc798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
+ 004fc798 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004d9900 bytes 08bd43f9
+ 004fc798 bytes 089d41f9
~~~


<a id="compare-2dadb7e2a8d0964d3decd5cfc107725a"></a>

### [`004d9940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9940.md) → [`004fc7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc7d8.md) _ZN5Botan2OS25run_cpu_instruction_probeENSt6__ndk18functionIFivEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`004d9b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9b40.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`004fc9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc9d8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004fc80c",
      "incomplete_value": false,
      "site": "004fc814",
      "value": [
        "leaf",
        "const:4fc9d8:8"
      ]
    },
    "old": {
      "definition_site": "004d9974",
      "incomplete_value": false,
      "site": "004d997c",
      "value": [
        "leaf",
        "const:4d9b40:8"
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fc838",
      "incomplete_value": false,
      "site": "004fc840",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d99a0",
      "incomplete_value": false,
      "site": "004d99a8",
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
            "const:3d8:8"
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
      "definition_site": "004fc8c4",
      "incomplete_value": false,
      "site": "004fc8cc",
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
            "const:9b1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d9a2c",
      "incomplete_value": false,
      "site": "004d9a34",
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
            "const:59e:8"
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
      "004fc814",
      "DATA",
      [
        "storage",
        "004d9b40",
        null,
        null
      ]
    ],
    [
      "004fc838",
      "PARAM",
      [
        "storage",
        "00c253d8",
        null,
        null
      ]
    ],
    [
      "004fc8c4",
      "PARAM",
      [
        "storage",
        "0029f59e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fc814",
      "DATA",
      [
        "storage",
        "004fc9d8",
        null,
        null
      ]
    ],
    [
      "004fc838",
      "PARAM",
      [
        "storage",
        "00ca4e98",
        null,
        null
      ]
    ],
    [
      "004fc8c4",
      "PARAM",
      [
        "storage",
        "002af9b1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d99a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9940.md#insn-004d99a8) · [`004d9a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9940.md#insn-004d9a34) · [`004d9a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9940.md#insn-004d9a70)
- 新版 `004fc840`（命令位置の公開資料なし） · `004fc8cc`（命令位置の公開資料なし） · `004fc908`（命令位置の公開資料なし）

~~~diff
- 004d99a8 ["INT_ADD", "register:40f0:8", ["const:4d99a8:8", "const:4:8"]]
- 004d99a8 ["CALL", null, ["callee:00c594d0:8"]]
+ 004fc840 ["INT_ADD", "register:40f0:8", ["const:4fc840:8", "const:4:8"]]
+ 004fc840 ["CALL", null, ["callee:00c594d0:8"]]
- 004d99a8 bytes 360c1c94
+ 004fc840 bytes 24731d94
- 004d9a34 ["INT_ADD", "register:40f0:8", ["const:4d9a34:8", "const:4:8"]]
- 004d9a34 ["CALL", null, ["callee:0043dd98:8"]]
+ 004fc8cc ["INT_ADD", "register:40f0:8", ["const:4fc8cc:8", "const:4:8"]]
+ 004fc8cc ["CALL", null, ["callee:0043dd98:8"]]
- 004d9a34 bytes 1906fd97
+ 004fc8cc bytes 3305fd97
- 004d9a70 ["INT_ADD", "register:40f0:8", ["const:4d9a70:8", "const:4:8"]]
- 004d9a70 ["CALL", null, ["callee:00c57b10:8"]]
+ 004fc908 ["INT_ADD", "register:40f0:8", ["const:4fc908:8", "const:4:8"]]
+ 004fc908 ["CALL", null, ["callee:00c57b10:8"]]
- 004d9a70 bytes 94051c94
+ 004fc908 bytes 826c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98f9fc8e7ecff9a4286085548987d83a"></a>

### [`004d9b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9b58.md) → [`004fc9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc9f0.md) _ZN5Botan9to_uint16ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

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
      "definition_site": "004fca54",
      "incomplete_value": false,
      "site": "004fca5c",
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
            "const:115:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d9bbc",
      "incomplete_value": false,
      "site": "004d9bc4",
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
            "const:91c:8"
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
      "definition_site": "004fca90",
      "incomplete_value": true,
      "site": "004fca9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d9bf8",
      "incomplete_value": true,
      "site": "004d9c04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fca8c",
      "incomplete_value": false,
      "site": "004fca9c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004d9bf4",
      "incomplete_value": false,
      "site": "004d9c04",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fca54",
      "PARAM",
      [
        "storage",
        "0029391c",
        null,
        "string"
      ]
    ],
    [
      "004fca8c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004fca90",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fca54",
      "PARAM",
      [
        "storage",
        "002a3115",
        null,
        "string"
      ]
    ],
    [
      "004fca8c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004fca90",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d9bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9b58.md#insn-004d9bc4) · [`004d9c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9b58.md#insn-004d9c04) · [`004d9b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9b58.md#insn-004d9b78)
- 新版 `004fca5c`（命令位置の公開資料なし） · `004fca9c`（命令位置の公開資料なし） · `004fca10`（命令位置の公開資料なし）

~~~diff
- 004d9bc4 ["INT_ADD", "register:40f0:8", ["const:4d9bc4:8", "const:4:8"]]
- 004d9bc4 ["CALL", null, ["callee:0043dd98:8"]]
+ 004fca5c ["INT_ADD", "register:40f0:8", ["const:4fca5c:8", "const:4:8"]]
+ 004fca5c ["CALL", null, ["callee:0043dd98:8"]]
- 004d9bc4 bytes b505fd97
+ 004fca5c bytes cf04fd97
- 004d9c04 ["INT_ADD", "register:40f0:8", ["const:4d9c04:8", "const:4:8"]]
- 004d9c04 ["CALL", null, ["callee:00c57b10:8"]]
+ 004fca9c ["INT_ADD", "register:40f0:8", ["const:4fca9c:8", "const:4:8"]]
+ 004fca9c ["CALL", null, ["callee:00c57b10:8"]]
- 004d9c04 bytes 2f051c94
+ 004fca9c bytes 1d6c1d94
- 004d9b78 ["INT_ADD", "register:40f0:8", ["const:4d9b78:8", "const:4:8"]]
- 004d9b78 ["CALL", null, ["callee:00c583f0:8"]]
+ 004fca10 ["INT_ADD", "register:40f0:8", ["const:4fca10:8", "const:4:8"]]
+ 004fca10 ["CALL", null, ["callee:00c583f0:8"]]
- 004d9b78 bytes 8a071c94
+ 004fca10 bytes 786e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f90ebb80b18c41c7cb66020a6a0e950d"></a>

### [`004d9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9c58.md) → [`004fcaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcaf0.md) _ZN5Botan18timespec_to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

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
      "definition_site": "004fccb8",
      "incomplete_value": false,
      "site": "004fccc4",
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
            "const:dd4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d9e20",
      "incomplete_value": false,
      "site": "004d9e2c",
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
            "const:567:8"
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
      "definition_site": "004fccf4",
      "incomplete_value": true,
      "site": "004fcd00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004d9e5c",
      "incomplete_value": true,
      "site": "004d9e68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fccf0",
      "incomplete_value": false,
      "site": "004fcd00",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004d9e58",
      "incomplete_value": false,
      "site": "004d9e68",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fccb8",
      "PARAM",
      [
        "storage",
        "002a4567",
        null,
        "string"
      ]
    ],
    [
      "004fccf0",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004fccf4",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fccb8",
      "PARAM",
      [
        "storage",
        "002b4dd4",
        null,
        "string"
      ]
    ],
    [
      "004fccf0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004fccf4",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d9e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9c58.md#insn-004d9e2c) · [`004d9e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9c58.md#insn-004d9e68) · [`004d9cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9c58.md#insn-004d9cfc)
- 新版 `004fccc4`（命令位置の公開資料なし） · `004fcd00`（命令位置の公開資料なし） · `004fcb94`（命令位置の公開資料なし）

~~~diff
- 004d9e2c ["INT_ADD", "register:40f0:8", ["const:4d9e2c:8", "const:4:8"]]
- 004d9e2c ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fccc4 ["INT_ADD", "register:40f0:8", ["const:4fccc4:8", "const:4:8"]]
+ 004fccc4 ["CALL", null, ["callee:00c57cb0:8"]]
- 004d9e2c bytes 0d051c94
+ 004fccc4 bytes fb6b1d94
- 004d9e68 ["INT_ADD", "register:40f0:8", ["const:4d9e68:8", "const:4:8"]]
- 004d9e68 ["CALL", null, ["callee:00c57b10:8"]]
+ 004fcd00 ["INT_ADD", "register:40f0:8", ["const:4fcd00:8", "const:4:8"]]
+ 004fcd00 ["CALL", null, ["callee:00c57b10:8"]]
- 004d9e68 bytes 96041c94
+ 004fcd00 bytes 846b1d94
- 004d9cfc ["INT_ADD", "register:40f0:8", ["const:4d9cfc:8", "const:4:8"]]
- 004d9cfc ["CALL", null, ["callee:00c57a90:8"]]
+ 004fcb94 ["INT_ADD", "register:40f0:8", ["const:4fcb94:8", "const:4:8"]]
+ 004fcb94 ["CALL", null, ["callee:00c57a90:8"]]
- 004d9cfc bytes d1041c94
+ 004fcb94 bytes bf6b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-352c30e177287ff48b724bd72f0ef738"></a>

### [`004d9ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9ed0.md) → [`004fcd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcd68.md) _ZN5Botan13split_on_predERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFbcEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc160.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c58bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bb0.md) · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "definition_site": "004fcf78",
      "incomplete_value": false,
      "site": "004fcf84",
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
            "const:7dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004da0e0",
      "incomplete_value": false,
      "site": "004da0ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:552:8"
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
      "definition_site": "004fcfb4",
      "incomplete_value": true,
      "site": "004fcfc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004da11c",
      "incomplete_value": true,
      "site": "004da128",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fcfb0",
      "incomplete_value": false,
      "site": "004fcfc0",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004da118",
      "incomplete_value": false,
      "site": "004da128",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004fcf78",
      "PARAM",
      [
        "storage",
        "0029d552",
        null,
        "string"
      ]
    ],
    [
      "004fcfb0",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004fcfb4",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fcf78",
      "PARAM",
      [
        "storage",
        "002ad7dc",
        null,
        "string"
      ]
    ],
    [
      "004fcfb0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004fcfb4",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004da0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9ed0.md#insn-004da0ec) · [`004da128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9ed0.md#insn-004da128) · [`004d9f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d9/004d9ed0.md#insn-004d9f48)
- 新版 `004fcf84`（命令位置の公開資料なし） · `004fcfc0`（命令位置の公開資料なし） · `004fcde0`（命令位置の公開資料なし）

~~~diff
- 004da0ec ["INT_ADD", "register:40f0:8", ["const:4da0ec:8", "const:4:8"]]
- 004da0ec ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fcf84 ["INT_ADD", "register:40f0:8", ["const:4fcf84:8", "const:4:8"]]
+ 004fcf84 ["CALL", null, ["callee:00c57cb0:8"]]
- 004da0ec bytes 5d041c94
+ 004fcf84 bytes 4b6b1d94
- 004da128 ["INT_ADD", "register:40f0:8", ["const:4da128:8", "const:4:8"]]
- 004da128 ["CALL", null, ["callee:00c57b10:8"]]
+ 004fcfc0 ["INT_ADD", "register:40f0:8", ["const:4fcfc0:8", "const:4:8"]]
+ 004fcfc0 ["CALL", null, ["callee:00c57b10:8"]]
- 004da128 bytes e6031c94
+ 004fcfc0 bytes d46a1d94
- 004d9f48 ["INT_ADD", "register:40f0:8", ["const:4d9f48:8", "const:4:8"]]
- 004d9f48 ["CALL", null, ["callee:00c58200:8"]]
+ 004fcde0 ["INT_ADD", "register:40f0:8", ["const:4fcde0:8", "const:4:8"]]
+ 004fcde0 ["CALL", null, ["callee:00c58200:8"]]
- 004d9f48 bytes 1a061c94
+ 004fcde0 bytes 086d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f664759180310be3558084239b1b2a5"></a>

### [`004da474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004da474.md) → [`004fd30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd30c.md) _ZN5Botan14string_to_ipv4ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcab0.md) · 呼出先 11件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c98.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59500.md) · 呼出先 11件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004fd330",
      "incomplete_value": false,
      "site": "004fd344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004da498",
      "incomplete_value": false,
      "site": "004da4ac",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fd45c",
      "incomplete_value": false,
      "site": "004fd468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:b3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004da5c4",
      "incomplete_value": false,
      "site": "004da5d0",
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
            "const:464:8"
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
      "definition_site": "004fd498",
      "incomplete_value": true,
      "site": "004fd4a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004da600",
      "incomplete_value": true,
      "site": "004da60c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
              ]
            ]
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
      "004fd344",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004fd380",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      "004fd380",
      "READ",
      [
        "storage",
        "00bed718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004fd344",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004fd380",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fd380",
      "READ",
      [
        "storage",
        "00c6a2d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004da5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004da474.md#insn-004da5d0) · [`004da60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004da474.md#insn-004da60c) · [`004da630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004da474.md#insn-004da630)
- 新版 `004fd468`（命令位置の公開資料なし） · `004fd4a4`（命令位置の公開資料なし） · `004fd4c8`（命令位置の公開資料なし）

~~~diff
- 004da5d0 ["INT_ADD", "register:40f0:8", ["const:4da5d0:8", "const:4:8"]]
- 004da5d0 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fd468 ["INT_ADD", "register:40f0:8", ["const:4fd468:8", "const:4:8"]]
+ 004fd468 ["CALL", null, ["callee:00c57cb0:8"]]
- 004da5d0 bytes 24031c94
+ 004fd468 bytes 126a1d94
- 004da60c ["INT_ADD", "register:40f0:8", ["const:4da60c:8", "const:4:8"]]
- 004da60c ["CALL", null, ["callee:00c57b10:8"]]
+ 004fd4a4 ["INT_ADD", "register:40f0:8", ["const:4fd4a4:8", "const:4:8"]]
+ 004fd4a4 ["CALL", null, ["callee:00c57b10:8"]]
- 004da60c bytes ad021c94
+ 004fd4a4 bytes 9b691d94
- 004da630 ["INT_ADD", "register:40f0:8", ["const:4da630:8", "const:4:8"]]
- 004da630 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fd4c8 ["INT_ADD", "register:40f0:8", ["const:4fd4c8:8", "const:4:8"]]
+ 004fd4c8 ["CALL", null, ["callee:00c57cb0:8"]]
- 004da630 bytes 0c031c94
+ 004fd4c8 bytes fa691d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72b932ae801464fb0f51bc41996e258c"></a>

### [`004daaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004daaa4.md) → [`004fd93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md) _ZN5Botan19host_wildcard_matchERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcad0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`0041f280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f280.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md)
- 新版 呼出元 1件 [`00c59520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59520.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`00441d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441d80.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.42% / 新版 99.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fddb4",
      "incomplete_value": false,
      "site": "004fddc0",
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
            "const:34a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004daf1c",
      "incomplete_value": false,
      "site": "004daf28",
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
            "const:859:8"
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
      "definition_site": "004fde08",
      "incomplete_value": false,
      "site": "004fde14",
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
    "old": {
      "definition_site": "004daf70",
      "incomplete_value": false,
      "site": "004daf7c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fde88",
      "incomplete_value": false,
      "site": "004fde90",
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
    "old": {
      "definition_site": "004daff0",
      "incomplete_value": false,
      "site": "004daff8",
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
      "004fddb4",
      "PARAM",
      [
        "storage",
        "002a6859",
        null,
        null
      ]
    ],
    [
      "004fde08",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "004fde88",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004fddb4",
      "PARAM",
      [
        "storage",
        "002b734a",
        null,
        null
      ]
    ],
    [
      "004fde08",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "004fde88",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004daf28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004daaa4.md#insn-004daf28) · [`004daf7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004daaa4.md#insn-004daf7c) · [`004daff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004daaa4.md#insn-004daff8)
- 新版 `004fddc0`（命令位置の公開資料なし） · `004fde14`（命令位置の公開資料なし） · `004fde90`（命令位置の公開資料なし）

~~~diff
- 004daf28 ["INT_ADD", "register:40f0:8", ["const:4daf28:8", "const:4:8"]]
- 004daf28 ["CALL", null, ["callee:00441e54:8"]]
+ 004fddc0 ["INT_ADD", "register:40f0:8", ["const:4fddc0:8", "const:4:8"]]
+ 004fddc0 ["CALL", null, ["callee:00441e54:8"]]
- 004daf28 bytes 0b11fd97
+ 004fddc0 bytes 2510fd97
- 004daf7c ["INT_ADD", "register:40f0:8", ["const:4daf7c:8", "const:4:8"]]
- 004daf7c ["CALL", null, ["callee:0043dd98:8"]]
+ 004fde14 ["INT_ADD", "register:40f0:8", ["const:4fde14:8", "const:4:8"]]
+ 004fde14 ["CALL", null, ["callee:0043dd98:8"]]
- 004daf7c bytes c700fd97
+ 004fde14 bytes e1fffc97
- 004daff8 ["INT_ADD", "register:40f0:8", ["const:4daff8:8", "const:4:8"]]
- 004daff8 ["CALL", null, ["callee:0043dd98:8"]]
+ 004fde90 ["INT_ADD", "register:40f0:8", ["const:4fde90:8", "const:4:8"]]
+ 004fde90 ["CALL", null, ["callee:0043dd98:8"]]
- 004daff8 bytes a800fd97
+ 004fde90 bytes c2fffc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e8915c416f04ea9b99656c834451dab"></a>

### [`004db550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004db550.md) → [`004fe3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe3e8.md) _ZN5Botan8read_cfgERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00471da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471da4.md) [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00494c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md) [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.27% / 新版 98.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004fe4f4",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004db65c",
      "value": [
        "leaf",
        "ram:bdb440:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fe7ec",
      "incomplete_value": false,
      "site": "004fe7f0",
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
    "old": {
      "definition_site": "004db954",
      "incomplete_value": false,
      "site": "004db958",
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
            "const:fa5:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fe848",
      "incomplete_value": false,
      "site": "004fe854",
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
            "const:4d5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004db9b0",
      "incomplete_value": false,
      "site": "004db9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:a9c:8"
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
      "004fe4a0",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004fe4d4",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004fe4f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "004fe4a0",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "004fe4d4",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004fe4f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004db65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004db550.md#insn-004db65c) · [`004db958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004db550.md#insn-004db958) · [`004db9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004db550.md#insn-004db9bc)
- 新版 `004fe4f4`（命令位置の公開資料なし） · `004fe7f0`（命令位置の公開資料なし） · `004fe854`（命令位置の公開資料なし）

~~~diff
- 004db65c ["INT_ADD", "register:40f0:8", ["const:4db65c:8", "const:4:8"]]
- 004db65c ["CALL", null, ["ram:bdb440:8"]]
+ 004fe4f4 ["INT_ADD", "register:40f0:8", ["const:4fe4f4:8", "const:4:8"]]
+ 004fe4f4 ["CALL", null, ["ram:c57e90:8"]]
- 004db65c bytes 79ff1b94
+ 004fe4f4 bytes 67661d94
- 004db958 ["INT_ADD", "register:40f0:8", ["const:4db958:8", "const:4:8"]]
- 004db958 ["CALL", null, ["callee:00494c3c:8"]]
+ 004fe7f0 ["INT_ADD", "register:40f0:8", ["const:4fe7f0:8", "const:4:8"]]
+ 004fe7f0 ["CALL", null, ["callee:00494c3c:8"]]
- 004db958 bytes 1359fe97
+ 004fe7f0 bytes 1359fe97
- 004db9bc ["INT_ADD", "register:40f0:8", ["const:4db9bc:8", "const:4:8"]]
- 004db9bc ["CALL", null, ["callee:00c57cb0:8"]]
+ 004fe854 ["INT_ADD", "register:40f0:8", ["const:4fe854:8", "const:4:8"]]
+ 004fe854 ["CALL", null, ["callee:00c57cb0:8"]]
- 004db9bc bytes 29fe1b94
+ 004fe854 bytes 17651d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03d644efd5ebc17cf4daca77814f0fd5"></a>

### [`004dbc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc40.md) → [`004fead8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fead8.md) _ZN5Botan18short_version_cstrEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004feadc",
      "incomplete_value": false,
      "site": "004feae0",
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
            "const:9dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dbc44",
      "incomplete_value": false,
      "site": "004dbc48",
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
            "const:5c9:8"
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
      "004feadc",
      "DATA",
      [
        "storage",
        "0029f5c9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004feadc",
      "DATA",
      [
        "storage",
        "002af9dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dbc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc40.md#insn-004dbc40) · [`004dbc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc40.md#insn-004dbc44)
- 新版 `004fead8`（命令位置の公開資料なし） · `004feadc`（命令位置の公開資料なし）

~~~diff
- 004dbc40 ["COPY", "register:4000:8", ["const:29f000:8"]]
+ 004fead8 ["COPY", "register:4000:8", ["const:2af000:8"]]
- 004dbc40 bytes 20eeff90
+ 004fead8 bytes 80edffb0
- 004dbc44 ["COPY", "tmp:0:8", ["const:5c9:8"]]
- 004dbc44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004dbc44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004dbc44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004feadc ["COPY", "tmp:0:8", ["const:9dc:8"]]
+ 004feadc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004feadc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004feadc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004dbc44 bytes 00241791
+ 004feadc bytes 00702791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d5fcc566b6efe32519922a9433bae06"></a>

### [`004dbc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc4c.md) → [`004feae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feae4.md) _ZN5Botan12version_cstrEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004feae8",
      "incomplete_value": false,
      "site": "004feaec",
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
            "const:58e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dbc50",
      "incomplete_value": false,
      "site": "004dbc54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:66b:8"
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
      "004feae8",
      "DATA",
      [
        "storage",
        "002ab66b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004feae8",
      "DATA",
      [
        "storage",
        "002bc58e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dbc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc4c.md#insn-004dbc4c) · [`004dbc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc4c.md#insn-004dbc50)
- 新版 `004feae4`（命令位置の公開資料なし） · `004feae8`（命令位置の公開資料なし）

~~~diff
- 004dbc4c ["COPY", "register:4000:8", ["const:2ab000:8"]]
+ 004feae4 ["COPY", "register:4000:8", ["const:2bc000:8"]]
- 004dbc4c bytes 80eeff90
+ 004feae4 bytes e0edffd0
- 004dbc50 ["COPY", "tmp:0:8", ["const:66b:8"]]
- 004dbc50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004dbc50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004dbc50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004feae8 ["COPY", "tmp:0:8", ["const:58e:8"]]
+ 004feae8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004feae8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004feae8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004dbc50 bytes 00ac1991
+ 004feae8 bytes 00381691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86862d2bdacfbdab7f283b499251de03"></a>

### [`004dbd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbd04.md) → [`004feb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feb9c.md) _ZN5Botan21runtime_version_checkEjjj

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.65% / 新版 88.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004febe4",
      "incomplete_value": true,
      "site": "004febf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004dbd4c",
      "incomplete_value": true,
      "site": "004dbd5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004febec",
      "incomplete_value": true,
      "site": "004febfc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004dbd54",
      "incomplete_value": true,
      "site": "004dbd64",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004fec04",
      "incomplete_value": true,
      "site": "004fec04",
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
                "const:28:8"
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
      "definition_site": "004dbd6c",
      "incomplete_value": true,
      "site": "004dbd6c",
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
                "const:28:8"
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
      "004febd0",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "004febd4",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "004febec",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004febd0",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "004febd4",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "004febec",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dbdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbd04.md#insn-004dbdec) · [`004dbe28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbd04.md#insn-004dbe28) · [`004dbe38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbd04.md#insn-004dbe38)
- 新版 `004fec84`（命令位置の公開資料なし） · `004fecc0`（命令位置の公開資料なし） · `004fecd0`（命令位置の公開資料なし）

~~~diff
- 004dbdec ["INT_ADD", "register:40f0:8", ["const:4dbdec:8", "const:4:8"]]
- 004dbdec ["CALL", null, ["callee:00459490:8"]]
+ 004fec84 ["INT_ADD", "register:40f0:8", ["const:4fec84:8", "const:4:8"]]
+ 004fec84 ["CALL", null, ["callee:00459490:8"]]
- 004dbdec bytes 036afd97
+ 004fec84 bytes 036afd97
- 004dbe28 ["INT_ADD", "register:40f0:8", ["const:4dbe28:8", "const:4:8"]]
- 004dbe28 ["CALL", null, ["callee:00459490:8"]]
+ 004fecc0 ["INT_ADD", "register:40f0:8", ["const:4fecc0:8", "const:4:8"]]
+ 004fecc0 ["CALL", null, ["callee:00459490:8"]]
- 004dbe28 bytes f469fd97
+ 004fecc0 bytes f469fd97
- 004dbe38 ["INT_ADD", "register:40f0:8", ["const:4dbe38:8", "const:4:8"]]
- 004dbe38 ["CALL", null, ["callee:00459490:8"]]
+ 004fecd0 ["INT_ADD", "register:40f0:8", ["const:4fecd0:8", "const:4:8"]]
+ 004fecd0 ["CALL", null, ["callee:00459490:8"]]
- 004dbe38 bytes f069fd97
+ 004fecd0 bytes f069fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

