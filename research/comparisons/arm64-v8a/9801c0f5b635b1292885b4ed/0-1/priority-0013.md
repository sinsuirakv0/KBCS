# v15.7.4 → v16.0.0 · 最優先の変更候補 (13)

[一覧の目次](README.md)

<a id="compare-67ad278e1b2fa3b00bcc5354d4e25e77"></a>

### [`0050d830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d830.md) → [`005306c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005306c8.md) FUN_005306c8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "005306ec",
      "incomplete_value": true,
      "site": "005306f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00530710",
      "incomplete_value": true,
      "site": "00530710",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0053073c",
      "incomplete_value": true,
      "site": "0053073c",
      "value": [
        "LOAD",
        "8",
        [
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
      "005306e4",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "005306f0",
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00530700",
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
      "005306e4",
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      "005306f0",
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00530700",
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

- 旧版 [`0050d878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d830.md#insn-0050d878) · [`0050d8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d830.md#insn-0050d8a4) · [`0050d840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d830.md#insn-0050d840)
- 新版 [`00530710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005306c8.md#insn-00530710) · [`0053073c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005306c8.md#insn-0053073c) · [`005306d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005306c8.md#insn-005306d8)

~~~diff
- 0050d878 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d878 ["INT_ADD", "register:40f0:8", ["const:50d878:8", "const:4:8"]]
- 0050d878 ["CALLIND", null, ["register:0:8"]]
+ 00530710 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530710 ["INT_ADD", "register:40f0:8", ["const:530710:8", "const:4:8"]]
+ 00530710 ["CALLIND", null, ["register:0:8"]]
- 0050d878 bytes 20013fd6
+ 00530710 bytes 20013fd6
- 0050d8a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d8a4 ["INT_ADD", "register:40f0:8", ["const:50d8a4:8", "const:4:8"]]
- 0050d8a4 ["CALLIND", null, ["register:0:8"]]
+ 0053073c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053073c ["INT_ADD", "register:40f0:8", ["const:53073c:8", "const:4:8"]]
+ 0053073c ["CALLIND", null, ["register:0:8"]]
- 0050d8a4 bytes 20013fd6
+ 0053073c bytes 20013fd6
- 0050d840 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005306d8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050d840 bytes 683800d0
+ 005306d8 bytes 483b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c2b821ea6f3bea1964ac856aeb38188"></a>

### [`0050d8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md) → [`0053078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) FUN_0053078c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`004a4d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d4c.md) [`004a4d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d88.md) [`0050d9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d9e0.md) [`0050da6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da6c.md) [`0050da74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da74.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 6件 [`004c7be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7be4.md) [`004c7c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7c20.md) [`00530878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530878.md) [`00530904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530904.md) [`0053090c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053090c.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "005307c4",
      "incomplete_value": true,
      "site": "005307c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "005307f8",
      "incomplete_value": true,
      "site": "005307f8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0053084c",
      "incomplete_value": true,
      "site": "0053084c",
      "value": [
        "LOAD",
        "8",
        [
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
      "005307b8",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "005307c8",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "005307e8",
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
      "005307b8",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "005307c8",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "005307e8",
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

- 旧版 [`0050d960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md#insn-0050d960) · [`0050d9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md#insn-0050d9b4) · [`0050d910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md#insn-0050d910)
- 新版 [`005307f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md#insn-005307f8) · [`0053084c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md#insn-0053084c) · [`005307a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md#insn-005307a8)

~~~diff
- 0050d960 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d960 ["INT_ADD", "register:40f0:8", ["const:50d960:8", "const:4:8"]]
- 0050d960 ["CALLIND", null, ["register:0:8"]]
+ 005307f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005307f8 ["INT_ADD", "register:40f0:8", ["const:5307f8:8", "const:4:8"]]
+ 005307f8 ["CALLIND", null, ["register:0:8"]]
- 0050d960 bytes 20013fd6
+ 005307f8 bytes 20013fd6
- 0050d9b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d9b4 ["INT_ADD", "register:40f0:8", ["const:50d9b4:8", "const:4:8"]]
- 0050d9b4 ["CALLIND", null, ["register:0:8"]]
+ 0053084c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053084c ["INT_ADD", "register:40f0:8", ["const:53084c:8", "const:4:8"]]
+ 0053084c ["CALLIND", null, ["register:0:8"]]
- 0050d9b4 bytes 20013fd6
+ 0053084c bytes 20013fd6
- 0050d910 ["COPY", "register:40b0:8", ["const:bea000:8"]]
+ 005307a8 ["COPY", "register:40b0:8", ["const:c67000:8"]]
- 0050d910 bytes f63600b0
+ 005307a8 bytes b63900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bee2fe0f1ff4e899f198c23839c75303"></a>

### [`0050da9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da9c.md) → [`00530934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530934.md) FUN_00530934

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050db70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050db70.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00530a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a08.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "005309b0",
      "incomplete_value": true,
      "site": "005309b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "0053096c",
      "incomplete_value": true,
      "site": "0053096c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530998",
      "incomplete_value": true,
      "site": "00530998",
      "value": [
        "LOAD",
        "8",
        [
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
      "0053095c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00530988",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "005309a8",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053095c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00530988",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "005309a8",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da9c.md#insn-0050dad4) · [`0050db00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da9c.md#insn-0050db00) · [`0050db3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050da9c.md#insn-0050db3c)
- 新版 [`0053096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530934.md#insn-0053096c) · [`00530998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530934.md#insn-00530998) · [`005309d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530934.md#insn-005309d4)

~~~diff
- 0050dad4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050dad4 ["INT_ADD", "register:40f0:8", ["const:50dad4:8", "const:4:8"]]
- 0050dad4 ["CALLIND", null, ["register:0:8"]]
+ 0053096c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053096c ["INT_ADD", "register:40f0:8", ["const:53096c:8", "const:4:8"]]
+ 0053096c ["CALLIND", null, ["register:0:8"]]
- 0050dad4 bytes 20013fd6
+ 0053096c bytes 20013fd6
- 0050db00 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050db00 ["INT_ADD", "register:40f0:8", ["const:50db00:8", "const:4:8"]]
- 0050db00 ["CALLIND", null, ["register:0:8"]]
+ 00530998 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530998 ["INT_ADD", "register:40f0:8", ["const:530998:8", "const:4:8"]]
+ 00530998 ["CALLIND", null, ["register:0:8"]]
- 0050db00 bytes 20013fd6
+ 00530998 bytes 20013fd6
- 0050db3c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050db3c ["INT_ADD", "register:40f0:8", ["const:50db3c:8", "const:4:8"]]
- 0050db3c ["CALLIND", null, ["register:0:8"]]
+ 005309d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005309d4 ["INT_ADD", "register:40f0:8", ["const:5309d4:8", "const:4:8"]]
+ 005309d4 ["CALLIND", null, ["register:0:8"]]
- 0050db3c bytes 20013fd6
+ 005309d4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99002731a8095be92fb0a932a4e04781"></a>

### [`0050dbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dbfc.md) → [`00530a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a94.md) FUN_00530a94

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00530ae4",
      "incomplete_value": true,
      "site": "00530ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00530acc",
      "incomplete_value": true,
      "site": "00530acc",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530b08",
      "incomplete_value": true,
      "site": "00530b08",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530abc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00530adc",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "00530ae8",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530abc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00530adc",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "00530ae8",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dbfc.md#insn-0050dc34) · [`0050dc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dbfc.md#insn-0050dc70) · [`0050dc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dbfc.md#insn-0050dc14)
- 新版 [`00530acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a94.md#insn-00530acc) · [`00530b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a94.md#insn-00530b08) · [`00530aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a94.md#insn-00530aac)

~~~diff
- 0050dc34 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050dc34 ["INT_ADD", "register:40f0:8", ["const:50dc34:8", "const:4:8"]]
- 0050dc34 ["CALLIND", null, ["register:0:8"]]
+ 00530acc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530acc ["INT_ADD", "register:40f0:8", ["const:530acc:8", "const:4:8"]]
+ 00530acc ["CALLIND", null, ["register:0:8"]]
- 0050dc34 bytes 20013fd6
+ 00530acc bytes 20013fd6
- 0050dc70 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050dc70 ["INT_ADD", "register:40f0:8", ["const:50dc70:8", "const:4:8"]]
- 0050dc70 ["CALLIND", null, ["register:0:8"]]
+ 00530b08 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530b08 ["INT_ADD", "register:40f0:8", ["const:530b08:8", "const:4:8"]]
+ 00530b08 ["CALLIND", null, ["register:0:8"]]
- 0050dc70 bytes 20013fd6
+ 00530b08 bytes 20013fd6
- 0050dc14 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00530aac ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0050dc14 bytes f53600b0
+ 00530aac bytes b53900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e0c08261823ec713eb84ed19b2e2fdb"></a>

### [`0050dca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dca0.md) → [`00530b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530b38.md) FUN_00530b38

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00530b88",
      "incomplete_value": true,
      "site": "00530b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00530b70",
      "incomplete_value": true,
      "site": "00530b70",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530bac",
      "incomplete_value": true,
      "site": "00530bac",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530b60",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00530b80",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "00530b8c",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530b60",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00530b80",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "00530b8c",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dca0.md#insn-0050dcd8) · [`0050dd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dca0.md#insn-0050dd14) · [`0050dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dca0.md#insn-0050dcb8)
- 新版 [`00530b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530b38.md#insn-00530b70) · [`00530bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530b38.md#insn-00530bac) · [`00530b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530b38.md#insn-00530b50)

~~~diff
- 0050dcd8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050dcd8 ["INT_ADD", "register:40f0:8", ["const:50dcd8:8", "const:4:8"]]
- 0050dcd8 ["CALLIND", null, ["register:0:8"]]
+ 00530b70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530b70 ["INT_ADD", "register:40f0:8", ["const:530b70:8", "const:4:8"]]
+ 00530b70 ["CALLIND", null, ["register:0:8"]]
- 0050dcd8 bytes 20013fd6
+ 00530b70 bytes 20013fd6
- 0050dd14 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050dd14 ["INT_ADD", "register:40f0:8", ["const:50dd14:8", "const:4:8"]]
- 0050dd14 ["CALLIND", null, ["register:0:8"]]
+ 00530bac ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530bac ["INT_ADD", "register:40f0:8", ["const:530bac:8", "const:4:8"]]
+ 00530bac ["CALLIND", null, ["register:0:8"]]
- 0050dd14 bytes 20013fd6
+ 00530bac bytes 20013fd6
- 0050dcb8 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00530b50 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0050dcb8 bytes f53600b0
+ 00530b50 bytes b53900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a87c6b8a8c0fb95a9d560a450b2fdd4"></a>

### [`0050dd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dd3c.md) → [`00530bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530bd4.md) FUN_00530bd4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`004a8a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8a10.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cb8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb8a8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00530bec",
      "value": [
        "leaf",
        "ram:4cb8a8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0050dd54",
      "value": [
        "leaf",
        "ram:4a8a10:8"
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
      "00530bec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004a8a10"
      ]
    ]
  ],
  "added": [
    [
      "00530bec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004cb8a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dd3c.md#insn-0050dd54) · [`0050dd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dd3c.md#insn-0050dd4c)
- 新版 [`00530bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530bd4.md#insn-00530bec) · [`00530be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530bd4.md#insn-00530be4)

~~~diff
- 0050dd54 ["INT_ADD", "register:40f0:8", ["const:50dd54:8", "const:4:8"]]
- 0050dd54 ["CALL", null, ["ram:4a8a10:8"]]
+ 00530bec ["INT_ADD", "register:40f0:8", ["const:530bec:8", "const:4:8"]]
+ 00530bec ["CALL", null, ["ram:4cb8a8:8"]]
- 0050dd54 bytes 2f6bfe97
+ 00530bec bytes 2f6bfe97
- 0050dd4c ["INT_ADD", "register:40f0:8", ["const:50dd4c:8", "const:4:8"]]
- 0050dd4c ["CALL", null, ["callee:00c57a90:8"]]
+ 00530be4 ["INT_ADD", "register:40f0:8", ["const:530be4:8", "const:4:8"]]
+ 00530be4 ["CALL", null, ["callee:00c57a90:8"]]
- 0050dd4c bytes bd341b94
+ 00530be4 bytes ab9b1c94
~~~


<a id="compare-7161fac14587f2b0b5be80294a272ebd"></a>

### [`0050dda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dda4.md) → [`00530c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530c3c.md) FUN_00530c3c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00530c8c",
      "incomplete_value": true,
      "site": "00530c90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00530c74",
      "incomplete_value": true,
      "site": "00530c74",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530cb0",
      "incomplete_value": true,
      "site": "00530cb0",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530c64",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00530c84",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "00530c90",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530c64",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00530c84",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "00530c90",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dda4.md#insn-0050dddc) · [`0050de18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dda4.md#insn-0050de18) · [`0050ddbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dda4.md#insn-0050ddbc)
- 新版 [`00530c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530c3c.md#insn-00530c74) · [`00530cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530c3c.md#insn-00530cb0) · [`00530c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530c3c.md#insn-00530c54)

~~~diff
- 0050dddc ["COPY", "register:0:8", ["register:4048:8"]]
- 0050dddc ["INT_ADD", "register:40f0:8", ["const:50dddc:8", "const:4:8"]]
- 0050dddc ["CALLIND", null, ["register:0:8"]]
+ 00530c74 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530c74 ["INT_ADD", "register:40f0:8", ["const:530c74:8", "const:4:8"]]
+ 00530c74 ["CALLIND", null, ["register:0:8"]]
- 0050dddc bytes 20013fd6
+ 00530c74 bytes 20013fd6
- 0050de18 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050de18 ["INT_ADD", "register:40f0:8", ["const:50de18:8", "const:4:8"]]
- 0050de18 ["CALLIND", null, ["register:0:8"]]
+ 00530cb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530cb0 ["INT_ADD", "register:40f0:8", ["const:530cb0:8", "const:4:8"]]
+ 00530cb0 ["CALLIND", null, ["register:0:8"]]
- 0050de18 bytes 20013fd6
+ 00530cb0 bytes 20013fd6
- 0050ddbc ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00530c54 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0050ddbc bytes f53600b0
+ 00530c54 bytes b53900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ae7b2877374224fbb0960acaeec8a3c"></a>

### [`0050de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050de48.md) → [`00530ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530ce0.md) FUN_00530ce0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00530d30",
      "incomplete_value": true,
      "site": "00530d34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00530d18",
      "incomplete_value": true,
      "site": "00530d18",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530d54",
      "incomplete_value": true,
      "site": "00530d54",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530d08",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00530d28",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "00530d34",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530d08",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00530d28",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "00530d34",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050de80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050de48.md#insn-0050de80) · [`0050debc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050de48.md#insn-0050debc) · [`0050de60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050de48.md#insn-0050de60)
- 新版 [`00530d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530ce0.md#insn-00530d18) · [`00530d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530ce0.md#insn-00530d54) · [`00530cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530ce0.md#insn-00530cf8)

~~~diff
- 0050de80 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050de80 ["INT_ADD", "register:40f0:8", ["const:50de80:8", "const:4:8"]]
- 0050de80 ["CALLIND", null, ["register:0:8"]]
+ 00530d18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530d18 ["INT_ADD", "register:40f0:8", ["const:530d18:8", "const:4:8"]]
+ 00530d18 ["CALLIND", null, ["register:0:8"]]
- 0050de80 bytes 20013fd6
+ 00530d18 bytes 20013fd6
- 0050debc ["COPY", "register:0:8", ["register:4048:8"]]
- 0050debc ["INT_ADD", "register:40f0:8", ["const:50debc:8", "const:4:8"]]
- 0050debc ["CALLIND", null, ["register:0:8"]]
+ 00530d54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530d54 ["INT_ADD", "register:40f0:8", ["const:530d54:8", "const:4:8"]]
+ 00530d54 ["CALLIND", null, ["register:0:8"]]
- 0050debc bytes 20013fd6
+ 00530d54 bytes 20013fd6
- 0050de60 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00530cf8 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0050de60 bytes f53600b0
+ 00530cf8 bytes b53900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4f863ba6b963e450b0d09c1506ab220"></a>

### [`0050dfd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dfd4.md) → [`00530e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530e6c.md) FUN_00530e6c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "00530ea4",
      "incomplete_value": true,
      "site": "00530ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:277:8"
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
                "const:786:8"
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
      "00530e94",
      "READ",
      [
        "storage",
        "002a6786",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00530e94",
      "READ",
      [
        "storage",
        "002b7277",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050dfec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dfd4.md#insn-0050dfec) · [`0050dff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dfd4.md#insn-0050dff0) · [`0050e018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dfd4.md#insn-0050e018)
- 新版 [`00530e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530e6c.md#insn-00530e84) · [`00530e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530e6c.md#insn-00530e88) · [`00530eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530e6c.md#insn-00530eb0)

~~~diff
- 0050dfec ["COPY", "register:4048:8", ["const:2a6000:8"]]
+ 00530e84 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 0050dfec bytes c9ecffb0
+ 00530e84 bytes 29ecfff0
- 0050dff0 ["COPY", "tmp:0:8", ["const:786:8"]]
- 0050dff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050dff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050dff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00530e88 ["COPY", "tmp:0:8", ["const:277:8"]]
+ 00530e88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00530e88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00530e88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050dff0 bytes 29191e91
+ 00530e88 bytes 29dd0991
- 0050e018 ["INT_ADD", "register:40f0:8", ["const:50e018:8", "const:4:8"]]
- 0050e018 ["CALL", null, ["callee:00c58290:8"]]
+ 00530eb0 ["INT_ADD", "register:40f0:8", ["const:530eb0:8", "const:4:8"]]
+ 00530eb0 ["CALL", null, ["callee:00c58290:8"]]
- 0050e018 bytes 0a361b94
+ 00530eb0 bytes f89c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1abb8b057eb62af16d59563643c33a3"></a>

### [`0050e0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e0cc.md) → [`00530f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530f64.md) FUN_00530f64

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00530f90",
      "incomplete_value": true,
      "site": "00530f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00530f84",
      "READ",
      [
        "storage",
        "00c1b398",
        null,
        "pointer"
      ]
    ],
    [
      "00530f94",
      "DATA",
      [
        "storage",
        "00bea990",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00530f84",
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ],
    [
      "00530f94",
      "DATA",
      [
        "storage",
        "00c67550",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e0cc.md#insn-0050e0e0) · [`0050e0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e0cc.md#insn-0050e0e4) · [`0050e0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e0cc.md#insn-0050e0ec)
- 新版 [`00530f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530f64.md#insn-00530f78) · [`00530f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530f64.md#insn-00530f7c) · [`00530f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530f64.md#insn-00530f84)

~~~diff
- 0050e0e0 ["INT_ADD", "register:40f0:8", ["const:50e0e0:8", "const:4:8"]]
- 0050e0e0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00530f78 ["INT_ADD", "register:40f0:8", ["const:530f78:8", "const:4:8"]]
+ 00530f78 ["CALL", null, ["callee:00c57a90:8"]]
- 0050e0e0 bytes d8331b94
+ 00530f78 bytes c69a1c94
- 0050e0e4 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 00530f7c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0050e0e4 bytes 693800b0
+ 00530f7c bytes 493b00d0
- 0050e0ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:398:8"]]
- 0050e0ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530f84 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d88:8"]]
+ 00530f84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e0ec bytes 29cd41f9
+ 00530f84 bytes 29c546f9
~~~


<a id="compare-387a275f1a77f310e40eff1c68d7e832"></a>

### [`0050e114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e114.md) → [`00530fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530fac.md) FUN_00530fac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "00530fe4",
      "incomplete_value": true,
      "site": "00530fe4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:79d:8"
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
                "const:418:8"
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
      "00530fd4",
      "READ",
      [
        "storage",
        "0029e418",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00530fd4",
      "READ",
      [
        "storage",
        "002ae79d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e114.md#insn-0050e12c) · [`0050e130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e114.md#insn-0050e130) · [`0050e158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e114.md#insn-0050e158)
- 新版 [`00530fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530fac.md#insn-00530fc4) · [`00530fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530fac.md#insn-00530fc8) · [`00530ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530fac.md#insn-00530ff0)

~~~diff
- 0050e12c ["COPY", "register:4048:8", ["const:29e000:8"]]
+ 00530fc4 ["COPY", "register:4048:8", ["const:2ae000:8"]]
- 0050e12c bytes 89ecff90
+ 00530fc4 bytes e9ebffd0
- 0050e130 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0050e130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00530fc8 ["COPY", "tmp:0:8", ["const:79d:8"]]
+ 00530fc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00530fc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00530fc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e130 bytes 29611091
+ 00530fc8 bytes 29751e91
- 0050e158 ["INT_ADD", "register:40f0:8", ["const:50e158:8", "const:4:8"]]
- 0050e158 ["CALL", null, ["callee:00c58290:8"]]
+ 00530ff0 ["INT_ADD", "register:40f0:8", ["const:530ff0:8", "const:4:8"]]
+ 00530ff0 ["CALL", null, ["callee:00c58290:8"]]
- 0050e158 bytes ba351b94
+ 00530ff0 bytes a89c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-799c09fed46c260a5523f84441ea21ee"></a>

### [`0050e1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e1bc.md) → [`00531054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531054.md) FUN_00531054

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00531070",
      "incomplete_value": true,
      "site": "00531070",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a8d:8"
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
                "const:bb4:8"
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
      "definition_site": "00531068",
      "incomplete_value": true,
      "site": "00531074",
      "value": [
        "LOAD",
        "8",
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
      "00531060",
      "READ",
      [
        "storage",
        "00299bb4",
        null,
        "string"
      ]
    ],
    [
      "00531068",
      "READ",
      [
        "storage",
        "00299bbb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531060",
      "READ",
      [
        "storage",
        "002a9a8d",
        null,
        "string"
      ]
    ],
    [
      "00531068",
      "READ",
      [
        "storage",
        "002a9a94",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e1bc.md#insn-0050e1c0) · [`0050e1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e1bc.md#insn-0050e1c4)
- 新版 [`00531058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531054.md#insn-00531058) · [`0053105c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531054.md#insn-0053105c)

~~~diff
- 0050e1c0 ["COPY", "register:4050:8", ["const:299000:8"]]
+ 00531058 ["COPY", "register:4050:8", ["const:2a9000:8"]]
- 0050e1c0 bytes 4aecfff0
+ 00531058 bytes caebff90
- 0050e1c4 ["COPY", "tmp:0:8", ["const:bb4:8"]]
- 0050e1c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050e1c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050e1c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0053105c ["COPY", "tmp:0:8", ["const:a8d:8"]]
+ 0053105c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0053105c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0053105c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050e1c4 bytes 4ad12e91
+ 0053105c bytes 4a352a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7c0833805666e3df63f77c10c413e2b"></a>

### [`0050e234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e234.md) → [`005310cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005310cc.md) FUN_005310cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "00531104",
      "incomplete_value": true,
      "site": "00531104",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ccb:8"
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
                "const:45e:8"
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
      "005310f4",
      "READ",
      [
        "storage",
        "002a445e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005310f4",
      "READ",
      [
        "storage",
        "002b4ccb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e234.md#insn-0050e24c) · [`0050e250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e234.md#insn-0050e250) · [`0050e278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e234.md#insn-0050e278)
- 新版 [`005310e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005310cc.md#insn-005310e4) · [`005310e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005310cc.md#insn-005310e8) · [`00531110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005310cc.md#insn-00531110)

~~~diff
- 0050e24c ["COPY", "register:4048:8", ["const:2a4000:8"]]
+ 005310e4 ["COPY", "register:4048:8", ["const:2b4000:8"]]
- 0050e24c bytes a9ecffd0
+ 005310e4 bytes 09ecfff0
- 0050e250 ["COPY", "tmp:0:8", ["const:45e:8"]]
- 0050e250 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e250 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e250 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005310e8 ["COPY", "tmp:0:8", ["const:ccb:8"]]
+ 005310e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005310e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005310e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e250 bytes 29791191
+ 005310e8 bytes 292d3391
- 0050e278 ["INT_ADD", "register:40f0:8", ["const:50e278:8", "const:4:8"]]
- 0050e278 ["CALL", null, ["callee:00c58290:8"]]
+ 00531110 ["INT_ADD", "register:40f0:8", ["const:531110:8", "const:4:8"]]
+ 00531110 ["CALL", null, ["callee:00c58290:8"]]
- 0050e278 bytes 72351b94
+ 00531110 bytes 609c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30a73098596ed37fa9f8e9cf6214f993"></a>

### [`0050e32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e32c.md) → [`005311c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005311c4.md) FUN_005311c4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

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
      "definition_site": "005311f8",
      "incomplete_value": true,
      "site": "00531204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005311e8",
      "READ",
      [
        "storage",
        "00c1b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "00531204",
      "DATA",
      [
        "storage",
        "00beaa68",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005311e8",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "00531204",
      "DATA",
      [
        "storage",
        "00c67628",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e32c.md#insn-0050e344) · [`0050e348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e32c.md#insn-0050e348) · [`0050e350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e32c.md#insn-0050e350)
- 新版 [`005311dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005311c4.md#insn-005311dc) · [`005311e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005311c4.md#insn-005311e0) · [`005311e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005311c4.md#insn-005311e8)

~~~diff
- 0050e344 ["INT_ADD", "register:40f0:8", ["const:50e344:8", "const:4:8"]]
- 0050e344 ["CALL", null, ["callee:00c57a90:8"]]
+ 005311dc ["INT_ADD", "register:40f0:8", ["const:5311dc:8", "const:4:8"]]
+ 005311dc ["CALL", null, ["callee:00c57a90:8"]]
- 0050e344 bytes 3f331b94
+ 005311dc bytes 2d9a1c94
- 0050e348 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005311e0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050e348 bytes 683800b0
+ 005311e0 bytes 483b00b0
- 0050e350 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3c0:8"]]
- 0050e350 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005311e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db0:8"]]
+ 005311e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e350 bytes 08e141f9
+ 005311e8 bytes 08d946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d49a57dd0f2db2ba3b1db4be20680cb9"></a>

### [`0050e43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e43c.md) → [`005312d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005312d4.md) FUN_005312d4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "0053130c",
      "incomplete_value": true,
      "site": "0053130c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:36:8"
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
                "const:720:8"
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
      "005312fc",
      "READ",
      [
        "storage",
        "00294720",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005312fc",
      "READ",
      [
        "storage",
        "002a4036",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e43c.md#insn-0050e454) · [`0050e458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e43c.md#insn-0050e458) · [`0050e480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e43c.md#insn-0050e480)
- 新版 [`005312ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005312d4.md#insn-005312ec) · [`005312f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005312d4.md#insn-005312f0) · [`00531318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005312d4.md#insn-00531318)

~~~diff
- 0050e454 ["COPY", "register:4048:8", ["const:294000:8"]]
+ 005312ec ["COPY", "register:4048:8", ["const:2a4000:8"]]
- 0050e454 bytes 29ecffd0
+ 005312ec bytes 89ebfff0
- 0050e458 ["COPY", "tmp:0:8", ["const:720:8"]]
- 0050e458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005312f0 ["COPY", "tmp:0:8", ["const:36:8"]]
+ 005312f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005312f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005312f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e458 bytes 29811c91
+ 005312f0 bytes 29d90091
- 0050e480 ["INT_ADD", "register:40f0:8", ["const:50e480:8", "const:4:8"]]
- 0050e480 ["CALL", null, ["callee:00c58290:8"]]
+ 00531318 ["INT_ADD", "register:40f0:8", ["const:531318:8", "const:4:8"]]
+ 00531318 ["CALL", null, ["callee:00c58290:8"]]
- 0050e480 bytes f0341b94
+ 00531318 bytes de9b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2022302e6554178d75b64e04f4f5eef"></a>

### [`0050e534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e534.md) → [`005313cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005313cc.md) FUN_005313cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

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
      "definition_site": "00531400",
      "incomplete_value": true,
      "site": "0053140c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005313f0",
      "READ",
      [
        "storage",
        "00c1b3a0",
        null,
        "pointer"
      ]
    ],
    [
      "0053140c",
      "DATA",
      [
        "storage",
        "00beba00",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005313f0",
      "READ",
      [
        "storage",
        "00c9ad90",
        null,
        "pointer"
      ]
    ],
    [
      "0053140c",
      "DATA",
      [
        "storage",
        "00c685c0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e534.md#insn-0050e54c) · [`0050e550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e534.md#insn-0050e550) · [`0050e558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e534.md#insn-0050e558)
- 新版 [`005313e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005313cc.md#insn-005313e4) · [`005313e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005313cc.md#insn-005313e8) · [`005313f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005313cc.md#insn-005313f0)

~~~diff
- 0050e54c ["INT_ADD", "register:40f0:8", ["const:50e54c:8", "const:4:8"]]
- 0050e54c ["CALL", null, ["callee:00c57a90:8"]]
+ 005313e4 ["INT_ADD", "register:40f0:8", ["const:5313e4:8", "const:4:8"]]
+ 005313e4 ["CALL", null, ["callee:00c57a90:8"]]
- 0050e54c bytes bd321b94
+ 005313e4 bytes ab991c94
- 0050e550 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005313e8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050e550 bytes 683800b0
+ 005313e8 bytes 483b00b0
- 0050e558 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
- 0050e558 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005313f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d90:8"]]
+ 005313f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e558 bytes 08d141f9
+ 005313f0 bytes 08c946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e5cb11c8f281ce5bf6210a62d3588f8"></a>

### [`0050e67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e67c.md) → [`00531514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531514.md) FUN_00531514

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "0053154c",
      "incomplete_value": true,
      "site": "0053154c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e6b4",
      "incomplete_value": true,
      "site": "0050e6b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:564:8"
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
      "0053153c",
      "READ",
      [
        "storage",
        "002aa564",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053153c",
      "READ",
      [
        "storage",
        "002bb2e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e67c.md#insn-0050e694) · [`0050e698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e67c.md#insn-0050e698) · [`0050e6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e67c.md#insn-0050e6c0)
- 新版 [`0053152c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531514.md#insn-0053152c) · [`00531530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531514.md#insn-00531530) · [`00531558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531514.md#insn-00531558)

~~~diff
- 0050e694 ["COPY", "register:4048:8", ["const:2aa000:8"]]
+ 0053152c ["COPY", "register:4048:8", ["const:2bb000:8"]]
- 0050e694 bytes e9ecff90
+ 0053152c bytes 49ecffd0
- 0050e698 ["COPY", "tmp:0:8", ["const:564:8"]]
- 0050e698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050e698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050e698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531530 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00531530 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531530 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531530 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050e698 bytes 29911591
+ 00531530 bytes 29810b91
- 0050e6c0 ["INT_ADD", "register:40f0:8", ["const:50e6c0:8", "const:4:8"]]
- 0050e6c0 ["CALL", null, ["callee:00c58290:8"]]
+ 00531558 ["INT_ADD", "register:40f0:8", ["const:531558:8", "const:4:8"]]
+ 00531558 ["CALL", null, ["callee:00c58290:8"]]
- 0050e6c0 bytes 60341b94
+ 00531558 bytes 4e9b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83855309d62e9255a41a9d22bfef0261"></a>

### [`0050e774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e774.md) → [`0053160c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053160c.md) FUN_0053160c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00531634",
      "incomplete_value": true,
      "site": "00531634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "0053162c",
      "READ",
      [
        "storage",
        "00c1b3a8",
        null,
        "pointer"
      ]
    ],
    [
      "00531634",
      "DATA",
      [
        "storage",
        "00beba90",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0053162c",
      "READ",
      [
        "storage",
        "00c9ad98",
        null,
        "pointer"
      ]
    ],
    [
      "00531634",
      "DATA",
      [
        "storage",
        "00c68650",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e774.md#insn-0050e788) · [`0050e78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e774.md#insn-0050e78c) · [`0050e794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e774.md#insn-0050e794)
- 新版 [`00531620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053160c.md#insn-00531620) · [`00531624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053160c.md#insn-00531624) · [`0053162c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053160c.md#insn-0053162c)

~~~diff
- 0050e788 ["INT_ADD", "register:40f0:8", ["const:50e788:8", "const:4:8"]]
- 0050e788 ["CALL", null, ["callee:00c57a90:8"]]
+ 00531620 ["INT_ADD", "register:40f0:8", ["const:531620:8", "const:4:8"]]
+ 00531620 ["CALL", null, ["callee:00c57a90:8"]]
- 0050e788 bytes 2e321b94
+ 00531620 bytes 1c991c94
- 0050e78c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00531624 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050e78c bytes 683800b0
+ 00531624 bytes 483b00b0
- 0050e794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a8:8"]]
- 0050e794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053162c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
+ 0053162c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e794 bytes 08d541f9
+ 0053162c bytes 08cd46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6e95a475e585494156e0c81aa69825c"></a>

### [`0050e944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e944.md) → [`005317dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005317dc.md) FUN_005317dc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00531804",
      "incomplete_value": true,
      "site": "00531804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005317fc",
      "READ",
      [
        "storage",
        "00c1b3c8",
        null,
        "pointer"
      ]
    ],
    [
      "00531804",
      "DATA",
      [
        "storage",
        "00bebb08",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005317fc",
      "READ",
      [
        "storage",
        "00c9adb8",
        null,
        "pointer"
      ]
    ],
    [
      "00531804",
      "DATA",
      [
        "storage",
        "00c686c8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e944.md#insn-0050e958) · [`0050e95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e944.md#insn-0050e95c) · [`0050e964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e944.md#insn-0050e964)
- 新版 [`005317f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005317dc.md#insn-005317f0) · [`005317f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005317dc.md#insn-005317f4) · [`005317fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005317dc.md#insn-005317fc)

~~~diff
- 0050e958 ["INT_ADD", "register:40f0:8", ["const:50e958:8", "const:4:8"]]
- 0050e958 ["CALL", null, ["callee:00c57a90:8"]]
+ 005317f0 ["INT_ADD", "register:40f0:8", ["const:5317f0:8", "const:4:8"]]
+ 005317f0 ["CALL", null, ["callee:00c57a90:8"]]
- 0050e958 bytes ba311b94
+ 005317f0 bytes a8981c94
- 0050e95c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005317f4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050e95c bytes 683800b0
+ 005317f4 bytes 483b00b0
- 0050e964 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3c8:8"]]
- 0050e964 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005317fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
+ 005317fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050e964 bytes 08e541f9
+ 005317fc bytes 08dd46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91f8bd2a17f6dcac688c490747c532fc"></a>

### [`0050ea1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ea1c.md) → [`005318b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005318b4.md) FUN_005318b4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "005318ec",
      "incomplete_value": true,
      "site": "005318ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3d7:8"
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
                "const:369:8"
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
      "005318dc",
      "READ",
      [
        "storage",
        "0029b369",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005318dc",
      "READ",
      [
        "storage",
        "002ab3d7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ea34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ea1c.md#insn-0050ea34) · [`0050ea38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ea1c.md#insn-0050ea38) · [`0050ea60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ea1c.md#insn-0050ea60)
- 新版 [`005318cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005318b4.md#insn-005318cc) · [`005318d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005318b4.md#insn-005318d0) · [`005318f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005318b4.md#insn-005318f8)

~~~diff
- 0050ea34 ["COPY", "register:4048:8", ["const:29b000:8"]]
+ 005318cc ["COPY", "register:4048:8", ["const:2ab000:8"]]
- 0050ea34 bytes 69ecffb0
+ 005318cc bytes c9ebffd0
- 0050ea38 ["COPY", "tmp:0:8", ["const:369:8"]]
- 0050ea38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050ea38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050ea38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005318d0 ["COPY", "tmp:0:8", ["const:3d7:8"]]
+ 005318d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005318d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005318d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050ea38 bytes 29a50d91
+ 005318d0 bytes 295d0f91
- 0050ea60 ["INT_ADD", "register:40f0:8", ["const:50ea60:8", "const:4:8"]]
- 0050ea60 ["CALL", null, ["callee:00c58290:8"]]
+ 005318f8 ["INT_ADD", "register:40f0:8", ["const:5318f8:8", "const:4:8"]]
+ 005318f8 ["CALL", null, ["callee:00c58290:8"]]
- 0050ea60 bytes 78331b94
+ 005318f8 bytes 669a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-614e46e3f4c042b82f3b5bdaac335df5"></a>

### [`0050eb14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050eb14.md) → [`005319ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005319ac.md) FUN_005319ac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0051bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) [`0053efc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`00540694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "005319f8",
      "incomplete_value": true,
      "site": "00531a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005319ec",
      "READ",
      [
        "storage",
        "00c1b390",
        null,
        "pointer"
      ]
    ],
    [
      "00531a04",
      "DATA",
      [
        "storage",
        "00bea930",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005319ec",
      "READ",
      [
        "storage",
        "00c9ad80",
        null,
        "pointer"
      ]
    ],
    [
      "00531a04",
      "DATA",
      [
        "storage",
        "00c674f0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050eb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050eb14.md#insn-0050eb44) · [`0050eb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050eb14.md#insn-0050eb48) · [`0050eb54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050eb14.md#insn-0050eb54)
- 新版 [`005319dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005319ac.md#insn-005319dc) · [`005319e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005319ac.md#insn-005319e0) · [`005319ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005319ac.md#insn-005319ec)

~~~diff
- 0050eb44 ["INT_ADD", "register:40f0:8", ["const:50eb44:8", "const:4:8"]]
- 0050eb44 ["CALL", null, ["callee:00c57a90:8"]]
+ 005319dc ["INT_ADD", "register:40f0:8", ["const:5319dc:8", "const:4:8"]]
+ 005319dc ["CALL", null, ["callee:00c57a90:8"]]
- 0050eb44 bytes 3f311b94
+ 005319dc bytes 2d981c94
- 0050eb48 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005319e0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050eb48 bytes 683800b0
+ 005319e0 bytes 483b00b0
- 0050eb54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
- 0050eb54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005319ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 005319ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050eb54 bytes 08c941f9
+ 005319ec bytes 08c146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6099867837647ef44dfb56c2e1b91a19"></a>

### [`0050ed2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ed2c.md) → [`00531bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531bc4.md) FUN_00531bc4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "00531bfc",
      "incomplete_value": true,
      "site": "00531bfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ed64",
      "incomplete_value": true,
      "site": "0050ed64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:28f000:8"
              ],
              [
                "leaf",
                "const:a60:8"
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
      "00531bec",
      "READ",
      [
        "storage",
        "0028fa60",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531bec",
      "READ",
      [
        "storage",
        "0029eea0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ed44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ed2c.md#insn-0050ed44) · [`0050ed48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ed2c.md#insn-0050ed48) · [`0050ed70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ed2c.md#insn-0050ed70)
- 新版 [`00531bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531bc4.md#insn-00531bdc) · [`00531be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531bc4.md#insn-00531be0) · [`00531c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531bc4.md#insn-00531c08)

~~~diff
- 0050ed44 ["COPY", "register:4048:8", ["const:28f000:8"]]
+ 00531bdc ["COPY", "register:4048:8", ["const:29e000:8"]]
- 0050ed44 bytes 09ecffb0
+ 00531bdc bytes 69ebffb0
- 0050ed48 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 0050ed48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050ed48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050ed48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531be0 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00531be0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531be0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531be0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050ed48 bytes 29812991
+ 00531be0 bytes 29813a91
- 0050ed70 ["INT_ADD", "register:40f0:8", ["const:50ed70:8", "const:4:8"]]
- 0050ed70 ["CALL", null, ["callee:00c58290:8"]]
+ 00531c08 ["INT_ADD", "register:40f0:8", ["const:531c08:8", "const:4:8"]]
+ 00531c08 ["CALL", null, ["callee:00c58290:8"]]
- 0050ed70 bytes b4321b94
+ 00531c08 bytes a2991c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7a16d17235cd03c598ad52a8f192aca"></a>

### [`0050edd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050edd4.md) → [`00531c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c6c.md) FUN_00531c6c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00531c78",
      "incomplete_value": true,
      "site": "00531c88",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:3b3:8"
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
                "const:97a:8"
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
      "definition_site": "00531c8c",
      "incomplete_value": true,
      "site": "00531c8c",
      "value": [
        "LOAD",
        "8",
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
      "00531c78",
      "READ",
      [
        "storage",
        "0029597a",
        null,
        "string"
      ]
    ],
    [
      "00531c80",
      "READ",
      [
        "storage",
        "00295988",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531c78",
      "READ",
      [
        "storage",
        "002a53b3",
        null,
        "string"
      ]
    ],
    [
      "00531c80",
      "READ",
      [
        "storage",
        "002a53c1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050edd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050edd4.md#insn-0050edd8) · [`0050eddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050edd4.md#insn-0050eddc)
- 新版 [`00531c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c6c.md#insn-00531c70) · [`00531c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c6c.md#insn-00531c74)

~~~diff
- 0050edd8 ["COPY", "register:4050:8", ["const:295000:8"]]
+ 00531c70 ["COPY", "register:4050:8", ["const:2a5000:8"]]
- 0050edd8 bytes 2aecfff0
+ 00531c70 bytes aaebff90
- 0050eddc ["COPY", "tmp:0:8", ["const:97a:8"]]
- 0050eddc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050eddc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050eddc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00531c74 ["COPY", "tmp:0:8", ["const:3b3:8"]]
+ 00531c74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00531c74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00531c74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050eddc bytes 4ae92591
+ 00531c74 bytes 4acd0e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0ea485a2ec99cd150712654f44c67d4"></a>

### [`0050edfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050edfc.md) → [`00531c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c94.md) FUN_00531c94

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051ca38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051ca38.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00531cbc",
      "incomplete_value": true,
      "site": "00531cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00531cb4",
      "READ",
      [
        "storage",
        "00c1b3d0",
        null,
        "pointer"
      ]
    ],
    [
      "00531cbc",
      "DATA",
      [
        "storage",
        "00bebb98",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531cb4",
      "READ",
      [
        "storage",
        "00c9adc0",
        null,
        "pointer"
      ]
    ],
    [
      "00531cbc",
      "DATA",
      [
        "storage",
        "00c68758",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ee10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050edfc.md#insn-0050ee10) · [`0050ee14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050edfc.md#insn-0050ee14) · [`0050ee1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050edfc.md#insn-0050ee1c)
- 新版 [`00531ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c94.md#insn-00531ca8) · [`00531cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c94.md#insn-00531cac) · [`00531cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531c94.md#insn-00531cb4)

~~~diff
- 0050ee10 ["INT_ADD", "register:40f0:8", ["const:50ee10:8", "const:4:8"]]
- 0050ee10 ["CALL", null, ["callee:00c57a90:8"]]
+ 00531ca8 ["INT_ADD", "register:40f0:8", ["const:531ca8:8", "const:4:8"]]
+ 00531ca8 ["CALL", null, ["callee:00c57a90:8"]]
- 0050ee10 bytes 8c301b94
+ 00531ca8 bytes 7a971c94
- 0050ee14 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00531cac ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050ee14 bytes 683800b0
+ 00531cac bytes 483b00b0
- 0050ee1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3d0:8"]]
- 0050ee1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531cb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00531cb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ee1c bytes 08e941f9
+ 00531cb4 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2994454a3e18c41971e0f8064fdb954e"></a>

### [`0050ee8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee8c.md) → [`00531d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531d24.md) FUN_00531d24

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "00531d5c",
      "incomplete_value": true,
      "site": "00531d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:701:8"
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
                "const:477:8"
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
      "00531d4c",
      "READ",
      [
        "storage",
        "0029d477",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531d4c",
      "READ",
      [
        "storage",
        "002ad701",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050eea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee8c.md#insn-0050eea4) · [`0050eea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee8c.md#insn-0050eea8) · [`0050eed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ee8c.md#insn-0050eed0)
- 新版 [`00531d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531d24.md#insn-00531d3c) · [`00531d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531d24.md#insn-00531d40) · [`00531d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531d24.md#insn-00531d68)

~~~diff
- 0050eea4 ["COPY", "register:4048:8", ["const:29d000:8"]]
+ 00531d3c ["COPY", "register:4048:8", ["const:2ad000:8"]]
- 0050eea4 bytes 69ecfff0
+ 00531d3c bytes e9ebff90
- 0050eea8 ["COPY", "tmp:0:8", ["const:477:8"]]
- 0050eea8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050eea8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050eea8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531d40 ["COPY", "tmp:0:8", ["const:701:8"]]
+ 00531d40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531d40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531d40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050eea8 bytes 29dd1191
+ 00531d40 bytes 29051c91
- 0050eed0 ["INT_ADD", "register:40f0:8", ["const:50eed0:8", "const:4:8"]]
- 0050eed0 ["CALL", null, ["callee:00c58290:8"]]
+ 00531d68 ["INT_ADD", "register:40f0:8", ["const:531d68:8", "const:4:8"]]
+ 00531d68 ["CALL", null, ["callee:00c58290:8"]]
- 0050eed0 bytes 5c321b94
+ 00531d68 bytes 4a991c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31efdcaa7e8a05179f736be7b75e1f4f"></a>

### [`0050ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ef84.md) → [`00531e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531e1c.md) FUN_00531e1c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0051bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) [`0053efc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`00540694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00531e68",
      "incomplete_value": true,
      "site": "00531e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00531e5c",
      "READ",
      [
        "storage",
        "00c1b3e0",
        null,
        "pointer"
      ]
    ],
    [
      "00531e74",
      "DATA",
      [
        "storage",
        "00bebc10",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531e5c",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "00531e74",
      "DATA",
      [
        "storage",
        "00c687d0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050efb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ef84.md#insn-0050efb4) · [`0050efb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ef84.md#insn-0050efb8) · [`0050efc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ef84.md#insn-0050efc4)
- 新版 [`00531e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531e1c.md#insn-00531e4c) · [`00531e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531e1c.md#insn-00531e50) · [`00531e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531e1c.md#insn-00531e5c)

~~~diff
- 0050efb4 ["INT_ADD", "register:40f0:8", ["const:50efb4:8", "const:4:8"]]
- 0050efb4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00531e4c ["INT_ADD", "register:40f0:8", ["const:531e4c:8", "const:4:8"]]
+ 00531e4c ["CALL", null, ["callee:00c57a90:8"]]
- 0050efb4 bytes 23301b94
+ 00531e4c bytes 11971c94
- 0050efb8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00531e50 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050efb8 bytes 683800b0
+ 00531e50 bytes 483b00b0
- 0050efc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3e0:8"]]
- 0050efc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531e5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 00531e5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050efc4 bytes 08f141f9
+ 00531e5c bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a56958a56ea652842187895fa6267c6c"></a>

### [`0050f19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f19c.md) → [`00532034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532034.md) FUN_00532034

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "0053205c",
      "incomplete_value": true,
      "site": "0053206c",
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
                "const:a57:8"
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
                "const:49d:8"
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
      "0053205c",
      "READ",
      [
        "storage",
        "002a049d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053205c",
      "READ",
      [
        "storage",
        "002b0a57",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f19c.md#insn-0050f1b4) · [`0050f1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f19c.md#insn-0050f1b8) · [`0050f1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f19c.md#insn-0050f1e0)
- 新版 [`0053204c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532034.md#insn-0053204c) · [`00532050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532034.md#insn-00532050) · [`00532078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532034.md#insn-00532078)

~~~diff
- 0050f1b4 ["COPY", "register:4048:8", ["const:2a0000:8"]]
+ 0053204c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0050f1b4 bytes 89ecffb0
+ 0053204c bytes e9ebffd0
- 0050f1b8 ["COPY", "tmp:0:8", ["const:49d:8"]]
- 0050f1b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050f1b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050f1b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532050 ["COPY", "tmp:0:8", ["const:a57:8"]]
+ 00532050 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532050 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532050 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050f1b8 bytes 29751291
+ 00532050 bytes 295d2991
- 0050f1e0 ["INT_ADD", "register:40f0:8", ["const:50f1e0:8", "const:4:8"]]
- 0050f1e0 ["CALL", null, ["callee:00c58290:8"]]
+ 00532078 ["INT_ADD", "register:40f0:8", ["const:532078:8", "const:4:8"]]
+ 00532078 ["CALL", null, ["callee:00c58290:8"]]
- 0050f1e0 bytes 98311b94
+ 00532078 bytes 86981c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5b77708a7ecb35d0d6923748888cfec"></a>

### [`0050f294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f294.md) → [`0053212c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053212c.md) FUN_0053212c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00532164",
      "incomplete_value": true,
      "site": "00532164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00532154",
      "READ",
      [
        "storage",
        "00c1b3e8",
        null,
        "pointer"
      ]
    ],
    [
      "00532164",
      "DATA",
      [
        "storage",
        "00bebc88",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00532154",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "00532164",
      "DATA",
      [
        "storage",
        "00c68848",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f294.md#insn-0050f2ac) · [`0050f2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f294.md#insn-0050f2b0) · [`0050f2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f294.md#insn-0050f2bc)
- 新版 [`00532144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053212c.md#insn-00532144) · [`00532148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053212c.md#insn-00532148) · [`00532154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053212c.md#insn-00532154)

~~~diff
- 0050f2ac ["INT_ADD", "register:40f0:8", ["const:50f2ac:8", "const:4:8"]]
- 0050f2ac ["CALL", null, ["callee:00c57a90:8"]]
+ 00532144 ["INT_ADD", "register:40f0:8", ["const:532144:8", "const:4:8"]]
+ 00532144 ["CALL", null, ["callee:00c57a90:8"]]
- 0050f2ac bytes 652f1b94
+ 00532144 bytes 53961c94
- 0050f2b0 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 00532148 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0050f2b0 bytes 69380090
+ 00532148 bytes 493b0090
- 0050f2bc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3e8:8"]]
- 0050f2bc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00532154 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd8:8"]]
+ 00532154 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0050f2bc bytes 29f541f9
+ 00532154 bytes 29ed46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8bad2cf04bee0a494aea4bd21de65a8"></a>

### [`0050f48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f48c.md) → [`00532324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532324.md) FUN_00532324

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "0053235c",
      "incomplete_value": true,
      "site": "0053235c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c5e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f4c4",
      "incomplete_value": true,
      "site": "0050f4c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:938:8"
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
      "0053234c",
      "READ",
      [
        "storage",
        "002ad938",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053234c",
      "READ",
      [
        "storage",
        "002bec5e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f48c.md#insn-0050f4a4) · [`0050f4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f48c.md#insn-0050f4a8) · [`0050f4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f48c.md#insn-0050f4d0)
- 新版 [`0053233c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532324.md#insn-0053233c) · [`00532340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532324.md#insn-00532340) · [`00532368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532324.md#insn-00532368)

~~~diff
- 0050f4a4 ["COPY", "register:4048:8", ["const:2ad000:8"]]
+ 0053233c ["COPY", "register:4048:8", ["const:2be000:8"]]
- 0050f4a4 bytes e9ecffd0
+ 0053233c bytes 69ecff90
- 0050f4a8 ["COPY", "tmp:0:8", ["const:938:8"]]
- 0050f4a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050f4a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050f4a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532340 ["COPY", "tmp:0:8", ["const:c5e:8"]]
+ 00532340 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532340 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532340 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050f4a8 bytes 29e12491
+ 00532340 bytes 29793191
- 0050f4d0 ["INT_ADD", "register:40f0:8", ["const:50f4d0:8", "const:4:8"]]
- 0050f4d0 ["CALL", null, ["callee:00c58290:8"]]
+ 00532368 ["INT_ADD", "register:40f0:8", ["const:532368:8", "const:4:8"]]
+ 00532368 ["CALL", null, ["callee:00c58290:8"]]
- 0050f4d0 bytes dc301b94
+ 00532368 bytes ca971c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50c6a91ebcd1c70f2664cff1f55764d0"></a>

### [`0050f534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f534.md) → [`005323cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323cc.md) FUN_005323cc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "005323d8",
      "incomplete_value": true,
      "site": "005323e4",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:3bc:8"
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
                "const:34e:8"
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
      "005323d8",
      "READ",
      [
        "storage",
        "0029b34e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005323d8",
      "READ",
      [
        "storage",
        "002ab3bc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f534.md#insn-0050f534) · [`0050f538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f534.md#insn-0050f538)
- 新版 [`005323cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323cc.md#insn-005323cc) · [`005323d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323cc.md#insn-005323d0)

~~~diff
- 0050f534 ["COPY", "register:4050:8", ["const:29b000:8"]]
+ 005323cc ["COPY", "register:4050:8", ["const:2ab000:8"]]
- 0050f534 bytes 6aecff90
+ 005323cc bytes caebffb0
- 0050f538 ["COPY", "tmp:0:8", ["const:34e:8"]]
- 0050f538 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050f538 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050f538 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005323d0 ["COPY", "tmp:0:8", ["const:3bc:8"]]
+ 005323d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005323d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005323d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050f538 bytes 4a390d91
+ 005323d0 bytes 4af10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf2b103f5e85e49dbe601ca60bb44abb"></a>

### [`0050f560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f560.md) → [`005323f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323f8.md) FUN_005323f8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "00532430",
      "incomplete_value": true,
      "site": "00532430",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:498:8"
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
                "const:963:8"
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
      "00532420",
      "READ",
      [
        "storage",
        "00296963",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00532420",
      "READ",
      [
        "storage",
        "002a6498",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f560.md#insn-0050f578) · [`0050f57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f560.md#insn-0050f57c) · [`0050f5a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f560.md#insn-0050f5a4)
- 新版 [`00532410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323f8.md#insn-00532410) · [`00532414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323f8.md#insn-00532414) · [`0053243c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005323f8.md#insn-0053243c)

~~~diff
- 0050f578 ["COPY", "register:4048:8", ["const:296000:8"]]
+ 00532410 ["COPY", "register:4048:8", ["const:2a6000:8"]]
- 0050f578 bytes 29ecfff0
+ 00532410 bytes a9ebff90
- 0050f57c ["COPY", "tmp:0:8", ["const:963:8"]]
- 0050f57c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050f57c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050f57c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532414 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 00532414 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532414 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532414 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050f57c bytes 298d2591
+ 00532414 bytes 29611291
- 0050f5a4 ["INT_ADD", "register:40f0:8", ["const:50f5a4:8", "const:4:8"]]
- 0050f5a4 ["CALL", null, ["callee:00c58290:8"]]
+ 0053243c ["INT_ADD", "register:40f0:8", ["const:53243c:8", "const:4:8"]]
+ 0053243c ["CALL", null, ["callee:00c58290:8"]]
- 0050f5a4 bytes a7301b94
+ 0053243c bytes 95971c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1f54d41162712a5333a9c13ce5f592b"></a>

### [`0050f608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f608.md) → [`005324a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005324a0.md) FUN_005324a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "005324ac",
      "incomplete_value": true,
      "site": "005324bc",
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
                "const:f0d:8"
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
                "const:26b:8"
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
      "005324ac",
      "READ",
      [
        "storage",
        "002a826b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005324ac",
      "READ",
      [
        "storage",
        "002b8f0d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f608.md#insn-0050f608) · [`0050f60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f608.md#insn-0050f60c)
- 新版 [`005324a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005324a0.md#insn-005324a0) · [`005324a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005324a0.md#insn-005324a4)

~~~diff
- 0050f608 ["COPY", "register:4050:8", ["const:2a8000:8"]]
+ 005324a0 ["COPY", "register:4050:8", ["const:2b8000:8"]]
- 0050f608 bytes caecffb0
+ 005324a0 bytes 2aecffd0
- 0050f60c ["COPY", "tmp:0:8", ["const:26b:8"]]
- 0050f60c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050f60c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050f60c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005324a4 ["COPY", "tmp:0:8", ["const:f0d:8"]]
+ 005324a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005324a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005324a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050f60c bytes 4aad0991
+ 005324a4 bytes 4a353c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c07dc29ef03310f3abd90570a8db93c1"></a>

### [`0050f680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f680.md) → [`00532518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532518.md) FUN_00532518

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "00532550",
      "incomplete_value": true,
      "site": "00532550",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ad:8"
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
                "const:a54:8"
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
      "00532540",
      "READ",
      [
        "storage",
        "00297a54",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00532540",
      "READ",
      [
        "storage",
        "002a76ad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f680.md#insn-0050f698) · [`0050f69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f680.md#insn-0050f69c) · [`0050f6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f680.md#insn-0050f6c4)
- 新版 [`00532530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532518.md#insn-00532530) · [`00532534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532518.md#insn-00532534) · [`0053255c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532518.md#insn-0053255c)

~~~diff
- 0050f698 ["COPY", "register:4048:8", ["const:297000:8"]]
+ 00532530 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0050f698 bytes 49ecff90
+ 00532530 bytes a9ebffb0
- 0050f69c ["COPY", "tmp:0:8", ["const:a54:8"]]
- 0050f69c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050f69c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050f69c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532534 ["COPY", "tmp:0:8", ["const:6ad:8"]]
+ 00532534 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532534 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532534 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050f69c bytes 29512991
+ 00532534 bytes 29b51a91
- 0050f6c4 ["INT_ADD", "register:40f0:8", ["const:50f6c4:8", "const:4:8"]]
- 0050f6c4 ["CALL", null, ["callee:00c58290:8"]]
+ 0053255c ["INT_ADD", "register:40f0:8", ["const:53255c:8", "const:4:8"]]
+ 0053255c ["CALL", null, ["callee:00c58290:8"]]
- 0050f6c4 bytes 5f301b94
+ 0053255c bytes 4d971c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e8c42c15c1abcb62168b120de7fdecd"></a>

### [`0050f778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f778.md) → [`00532610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532610.md) FUN_00532610

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051cc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cc00.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053fa98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fa98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0053263c",
      "incomplete_value": true,
      "site": "00532640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00532630",
      "READ",
      [
        "storage",
        "00c1b3d8",
        null,
        "pointer"
      ]
    ],
    [
      "00532640",
      "DATA",
      [
        "storage",
        "00bebdf0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00532630",
      "READ",
      [
        "storage",
        "00c9adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00532640",
      "DATA",
      [
        "storage",
        "00c689b0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f778.md#insn-0050f78c) · [`0050f790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f778.md#insn-0050f790) · [`0050f798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f778.md#insn-0050f798)
- 新版 [`00532624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532610.md#insn-00532624) · [`00532628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532610.md#insn-00532628) · [`00532630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532610.md#insn-00532630)

~~~diff
- 0050f78c ["INT_ADD", "register:40f0:8", ["const:50f78c:8", "const:4:8"]]
- 0050f78c ["CALL", null, ["callee:00c57a90:8"]]
+ 00532624 ["INT_ADD", "register:40f0:8", ["const:532624:8", "const:4:8"]]
+ 00532624 ["CALL", null, ["callee:00c57a90:8"]]
- 0050f78c bytes 2d2e1b94
+ 00532624 bytes 1b951c94
- 0050f790 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00532628 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050f790 bytes 68380090
+ 00532628 bytes 483b0090
- 0050f798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3d8:8"]]
- 0050f798 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00532630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc8:8"]]
+ 00532630 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050f798 bytes 08ed41f9
+ 00532630 bytes 08e546f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebd9821d0691d1ad5eb18641c40ebd64"></a>

### [`0050f9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f9f0.md) → [`00532888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532888.md) FUN_00532888

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "005328c0",
      "incomplete_value": true,
      "site": "005328c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
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
      "definition_site": "0050fa28",
      "incomplete_value": true,
      "site": "0050fa28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:57a:8"
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
      "005328b0",
      "READ",
      [
        "storage",
        "002ab57a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005328b0",
      "READ",
      [
        "storage",
        "002bc49d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050fa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f9f0.md#insn-0050fa08) · [`0050fa0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f9f0.md#insn-0050fa0c) · [`0050fa34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050f9f0.md#insn-0050fa34)
- 新版 [`005328a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532888.md#insn-005328a0) · [`005328a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532888.md#insn-005328a4) · [`005328cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532888.md#insn-005328cc)

~~~diff
- 0050fa08 ["COPY", "register:4048:8", ["const:2ab000:8"]]
+ 005328a0 ["COPY", "register:4048:8", ["const:2bc000:8"]]
- 0050fa08 bytes e9ecff90
+ 005328a0 bytes 49ecffd0
- 0050fa0c ["COPY", "tmp:0:8", ["const:57a:8"]]
- 0050fa0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050fa0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050fa0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005328a4 ["COPY", "tmp:0:8", ["const:49d:8"]]
+ 005328a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005328a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005328a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050fa0c bytes 29e91591
+ 005328a4 bytes 29751291
- 0050fa34 ["INT_ADD", "register:40f0:8", ["const:50fa34:8", "const:4:8"]]
- 0050fa34 ["CALL", null, ["callee:00c58290:8"]]
+ 005328cc ["INT_ADD", "register:40f0:8", ["const:5328cc:8", "const:4:8"]]
+ 005328cc ["CALL", null, ["callee:00c58290:8"]]
- 0050fa34 bytes 832f1b94
+ 005328cc bytes 71961c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecceabe43c74973ab303076425425a99"></a>

### [`0050fae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fae8.md) → [`00532980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532980.md) FUN_00532980

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00519a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "005329b0",
      "incomplete_value": false,
      "site": "005329b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c68000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
            "const:eb0:8"
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
      "definition_site": "005329b0",
      "incomplete_value": true,
      "site": "005329b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005329a8",
      "READ",
      [
        "storage",
        "00c1b3f8",
        null,
        "pointer"
      ]
    ],
    [
      "005329b0",
      "DATA",
      [
        "storage",
        "00bebeb0",
        null,
        "undefined *"
      ]
    ],
    [
      "005329b0",
      "DATA",
      [
        "storage",
        "00bebe68",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005329a8",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "005329b0",
      "DATA",
      [
        "storage",
        "00c68a70",
        null,
        "undefined *"
      ]
    ],
    [
      "005329b0",
      "DATA",
      [
        "storage",
        "00c68a28",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050fafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fae8.md#insn-0050fafc) · [`0050fb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fae8.md#insn-0050fb00) · [`0050fb08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fae8.md#insn-0050fb08)
- 新版 [`00532994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532980.md#insn-00532994) · [`00532998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532980.md#insn-00532998) · [`005329a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532980.md#insn-005329a0)

~~~diff
- 0050fafc ["INT_ADD", "register:40f0:8", ["const:50fafc:8", "const:4:8"]]
- 0050fafc ["CALL", null, ["callee:00c57a90:8"]]
+ 00532994 ["INT_ADD", "register:40f0:8", ["const:532994:8", "const:4:8"]]
+ 00532994 ["CALL", null, ["callee:00c57a90:8"]]
- 0050fafc bytes 512d1b94
+ 00532994 bytes 3f941c94
- 0050fb00 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00532998 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050fb00 bytes 68380090
+ 00532998 bytes 483b0090
- 0050fb08 ["COPY", "register:4048:8", ["const:beb000:8"]]
+ 005329a0 ["COPY", "register:4048:8", ["const:c68000:8"]]
- 0050fb08 bytes e9360090
+ 005329a0 bytes a93900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-080fad805d015fae0e5876ae2832593d"></a>

### [`0050fc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fc5c.md) → [`00532af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532af4.md) FUN_00532af4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

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
      "definition_site": "00532b3c",
      "incomplete_value": true,
      "site": "00532b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00532b3c",
      "incomplete_value": true,
      "site": "00532b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00532b20",
      "READ",
      [
        "storage",
        "00c1b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "00532b24",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "00532b3c",
      "DATA",
      [
        "storage",
        "00bebf28",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00532b20",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "00532b24",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "00532b3c",
      "DATA",
      [
        "storage",
        "00c68ae8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050fc78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fc5c.md#insn-0050fc78) · [`0050fc7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fc5c.md#insn-0050fc7c) · [`0050fc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fc5c.md#insn-0050fc80)
- 新版 [`00532b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532af4.md#insn-00532b10) · [`00532b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532af4.md#insn-00532b14) · [`00532b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532af4.md#insn-00532b18)

~~~diff
- 0050fc78 ["INT_ADD", "register:40f0:8", ["const:50fc78:8", "const:4:8"]]
- 0050fc78 ["CALL", null, ["callee:00c57a90:8"]]
+ 00532b10 ["INT_ADD", "register:40f0:8", ["const:532b10:8", "const:4:8"]]
+ 00532b10 ["CALL", null, ["callee:00c57a90:8"]]
- 0050fc78 bytes f22c1b94
+ 00532b10 bytes e0931c94
- 0050fc7c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00532b14 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0050fc7c bytes 68380090
+ 00532b14 bytes 483b0090
- 0050fc80 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 00532b18 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0050fc80 bytes 493800f0
+ 00532b18 bytes 493b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7d97d519fd5338f80e7b008c55b5f6d"></a>

### [`0050ffa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050ffa4.md) → [`00532e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md) FUN_00532e3c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00510074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510074.md) · 呼出先 4件 [`004bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00532f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f0c.md) · 呼出先 4件 [`004de6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00532ea4",
      "incomplete_value": true,
      "site": "00532ea4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00532ee0",
      "incomplete_value": true,
      "site": "00532ee0",
      "value": [
        "LOAD",
        "8",
        [
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
      "00532e94",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00532ed0",
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
      "00532e94",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00532ed0",
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

- 旧版 [`0051000c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050ffa4.md#insn-0051000c) · [`00510048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050ffa4.md#insn-00510048) · [`0050ffc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050ffa4.md#insn-0050ffc0)
- 新版 [`00532ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md#insn-00532ea4) · [`00532ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md#insn-00532ee0) · [`00532e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md#insn-00532e58)

~~~diff
- 0051000c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051000c ["INT_ADD", "register:40f0:8", ["const:51000c:8", "const:4:8"]]
- 0051000c ["CALLIND", null, ["register:0:8"]]
+ 00532ea4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00532ea4 ["INT_ADD", "register:40f0:8", ["const:532ea4:8", "const:4:8"]]
+ 00532ea4 ["CALLIND", null, ["register:0:8"]]
- 0051000c bytes 20013fd6
+ 00532ea4 bytes 20013fd6
- 00510048 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510048 ["INT_ADD", "register:40f0:8", ["const:510048:8", "const:4:8"]]
- 00510048 ["CALLIND", null, ["register:0:8"]]
+ 00532ee0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00532ee0 ["INT_ADD", "register:40f0:8", ["const:532ee0:8", "const:4:8"]]
+ 00532ee0 ["CALLIND", null, ["register:0:8"]]
- 00510048 bytes 20013fd6
+ 00532ee0 bytes 20013fd6
- 0050ffc0 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00532e58 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0050ffc0 bytes d53600f0
+ 00532e58 bytes b53900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcc7104915cead9aebbda934bf2e5d55"></a>

### [`00510098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510098.md) → [`00532f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f30.md) FUN_00532f30

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d0c8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053ff60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053ff60.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "site": "00532f50",
      "value": [
        "leaf",
        "ram:53ff60:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005100b8",
      "value": [
        "leaf",
        "ram:51d0c8:8"
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
      "00532f50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0051d0c8"
      ]
    ]
  ],
  "added": [
    [
      "00532f50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0053ff60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005100b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510098.md#insn-005100b8) · [`005100ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510098.md#insn-005100ac)
- 新版 [`00532f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f30.md#insn-00532f50) · [`00532f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f30.md#insn-00532f44)

~~~diff
- 005100b8 ["INT_ADD", "register:40f0:8", ["const:5100b8:8", "const:4:8"]]
- 005100b8 ["CALL", null, ["ram:51d0c8:8"]]
+ 00532f50 ["INT_ADD", "register:40f0:8", ["const:532f50:8", "const:4:8"]]
+ 00532f50 ["CALL", null, ["ram:53ff60:8"]]
- 005100b8 bytes 04340094
+ 00532f50 bytes 04340094
- 005100ac ["INT_ADD", "register:40f0:8", ["const:5100ac:8", "const:4:8"]]
- 005100ac ["CALL", null, ["callee:00c57a90:8"]]
+ 00532f44 ["INT_ADD", "register:40f0:8", ["const:532f44:8", "const:4:8"]]
+ 00532f44 ["CALL", null, ["callee:00c57a90:8"]]
- 005100ac bytes e52b1b94
+ 00532f44 bytes d3921c94
~~~


<a id="compare-9a35dc05054fee1954de5e1a55e87a3d"></a>

### [`005100e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005100e0.md) → [`00532f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md) FUN_00532f78

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00510254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510254.md) · 呼出先 4件 [`004bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`005330ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005330ec.md) · 呼出先 4件 [`004de6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00532fe0",
      "incomplete_value": true,
      "site": "00532fe0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533024",
      "incomplete_value": true,
      "site": "00533024",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533050",
      "incomplete_value": true,
      "site": "00533050",
      "value": [
        "LOAD",
        "8",
        [
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
      "00532fd0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00533014",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00533040",
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
      "00532fd0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533014",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533040",
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

- 旧版 [`00510148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005100e0.md#insn-00510148) · [`0051018c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005100e0.md#insn-0051018c) · [`005101b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005100e0.md#insn-005101b8)
- 新版 [`00532fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md#insn-00532fe0) · [`00533024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md#insn-00533024) · [`00533050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md#insn-00533050)

~~~diff
- 00510148 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510148 ["INT_ADD", "register:40f0:8", ["const:510148:8", "const:4:8"]]
- 00510148 ["CALLIND", null, ["register:0:8"]]
+ 00532fe0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00532fe0 ["INT_ADD", "register:40f0:8", ["const:532fe0:8", "const:4:8"]]
+ 00532fe0 ["CALLIND", null, ["register:0:8"]]
- 00510148 bytes 20013fd6
+ 00532fe0 bytes 20013fd6
- 0051018c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051018c ["INT_ADD", "register:40f0:8", ["const:51018c:8", "const:4:8"]]
- 0051018c ["CALLIND", null, ["register:0:8"]]
+ 00533024 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533024 ["INT_ADD", "register:40f0:8", ["const:533024:8", "const:4:8"]]
+ 00533024 ["CALLIND", null, ["register:0:8"]]
- 0051018c bytes 20013fd6
+ 00533024 bytes 20013fd6
- 005101b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005101b8 ["INT_ADD", "register:40f0:8", ["const:5101b8:8", "const:4:8"]]
- 005101b8 ["CALLIND", null, ["register:0:8"]]
+ 00533050 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533050 ["INT_ADD", "register:40f0:8", ["const:533050:8", "const:4:8"]]
+ 00533050 ["CALLIND", null, ["register:0:8"]]
- 005101b8 bytes 20013fd6
+ 00533050 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8221c0bdd0730630b00bf648dc9492c8"></a>

### [`00510588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510588.md) → [`00533420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533420.md) FUN_00533420

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

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
      "definition_site": "005334c4",
      "incomplete_value": true,
      "site": "005334c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:caa:8"
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
                "const:eec:8"
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
      "definition_site": "00533460",
      "incomplete_value": false,
      "site": "00533468",
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
            "const:e5b:8"
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
            "const:977:8"
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
      "definition_site": "00533470",
      "incomplete_value": false,
      "site": "00533478",
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
            "const:265:8"
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
            "const:284:8"
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
      "00533460",
      "PARAM",
      [
        "storage",
        "002ae977",
        null,
        "string"
      ]
    ],
    [
      "00533470",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ],
    [
      "005334b4",
      "READ",
      [
        "storage",
        "00298eec",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00533460",
      "PARAM",
      [
        "storage",
        "002bfe5b",
        null,
        "string"
      ]
    ],
    [
      "00533470",
      "PARAM",
      [
        "storage",
        "002ab265",
        null,
        null
      ]
    ],
    [
      "005334b4",
      "READ",
      [
        "storage",
        "002a8caa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005105d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510588.md#insn-005105d0) · [`005105e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510588.md#insn-005105e0) · [`005105c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510588.md#insn-005105c4)
- 新版 [`00533468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533420.md#insn-00533468) · [`00533478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533420.md#insn-00533478) · [`0053345c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533420.md#insn-0053345c)

~~~diff
- 005105d0 ["INT_ADD", "register:40f0:8", ["const:5105d0:8", "const:4:8"]]
- 005105d0 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00533468 ["INT_ADD", "register:40f0:8", ["const:533468:8", "const:4:8"]]
+ 00533468 ["CALL", null, ["callee:00c57cb0:8"]]
- 005105d0 bytes 242b1b94
+ 00533468 bytes 12921c94
- 005105e0 ["INT_ADD", "register:40f0:8", ["const:5105e0:8", "const:4:8"]]
- 005105e0 ["CALL", null, ["callee:00c57b70:8"]]
+ 00533478 ["INT_ADD", "register:40f0:8", ["const:533478:8", "const:4:8"]]
+ 00533478 ["CALL", null, ["callee:00c57b70:8"]]
- 005105e0 bytes d02a1b94
+ 00533478 bytes be911c94
- 005105c4 ["COPY", "register:4000:8", ["const:2ae000:8"]]
+ 0053345c ["COPY", "register:4000:8", ["const:2bf000:8"]]
- 005105c4 bytes e0ecffd0
+ 0053345c bytes 60ecff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41686bb5fe1871e4621836aba0b59018"></a>

### [`00510894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510894.md) → [`0053372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053372c.md) FUN_0053372c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00510960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510960.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`005337f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005337f8.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00533794",
      "incomplete_value": true,
      "site": "00533798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "0053377c",
      "incomplete_value": true,
      "site": "0053377c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005337c8",
      "incomplete_value": true,
      "site": "005337c8",
      "value": [
        "LOAD",
        "8",
        [
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
      "0053376c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0053378c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00533798",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "0053376c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0053378c",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "00533798",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005108e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510894.md#insn-005108e4) · [`00510930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510894.md#insn-00510930) · [`005108bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510894.md#insn-005108bc)
- 新版 [`0053377c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053372c.md#insn-0053377c) · [`005337c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053372c.md#insn-005337c8) · [`00533754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/0053372c.md#insn-00533754)

~~~diff
- 005108e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005108e4 ["INT_ADD", "register:40f0:8", ["const:5108e4:8", "const:4:8"]]
- 005108e4 ["CALLIND", null, ["register:0:8"]]
+ 0053377c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053377c ["INT_ADD", "register:40f0:8", ["const:53377c:8", "const:4:8"]]
+ 0053377c ["CALLIND", null, ["register:0:8"]]
- 005108e4 bytes 20013fd6
+ 0053377c bytes 20013fd6
- 00510930 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510930 ["INT_ADD", "register:40f0:8", ["const:510930:8", "const:4:8"]]
- 00510930 ["CALLIND", null, ["register:0:8"]]
+ 005337c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005337c8 ["INT_ADD", "register:40f0:8", ["const:5337c8:8", "const:4:8"]]
+ 005337c8 ["CALLIND", null, ["register:0:8"]]
- 00510930 bytes 20013fd6
+ 005337c8 bytes 20013fd6
- 005108bc ["COPY", "register:0:8", ["register:4040:8"]]
- 005108bc ["INT_ADD", "register:40f0:8", ["const:5108bc:8", "const:4:8"]]
- 005108bc ["CALLIND", null, ["register:0:8"]]
+ 00533754 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00533754 ["INT_ADD", "register:40f0:8", ["const:533754:8", "const:4:8"]]
+ 00533754 ["CALLIND", null, ["register:0:8"]]
- 005108bc bytes 00013fd6
+ 00533754 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63a9cb2521804c31040641d46c80c9c1"></a>

### [`005109d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005109d8.md) → [`00533870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533870.md) FUN_00533870

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "0053388c",
      "incomplete_value": true,
      "site": "00533890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "005338c4",
      "incomplete_value": true,
      "site": "005338c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00533884",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00533890",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "005338b4",
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
      "00533884",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "00533890",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "005338b4",
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

- 旧版 [`00510a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005109d8.md#insn-00510a2c) · [`005109e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005109d8.md#insn-005109e4) · [`005109ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005109d8.md#insn-005109ec)
- 新版 [`005338c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533870.md#insn-005338c4) · [`0053387c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533870.md#insn-0053387c) · [`00533884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533870.md#insn-00533884)

~~~diff
- 00510a2c ["COPY", "register:0:8", ["register:4048:8"]]
- 00510a2c ["INT_ADD", "register:40f0:8", ["const:510a2c:8", "const:4:8"]]
- 00510a2c ["CALLIND", null, ["register:0:8"]]
+ 005338c4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005338c4 ["INT_ADD", "register:40f0:8", ["const:5338c4:8", "const:4:8"]]
+ 005338c4 ["CALLIND", null, ["register:0:8"]]
- 00510a2c bytes 20013fd6
+ 005338c4 bytes 20013fd6
- 005109e4 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 0053387c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005109e4 bytes 483800f0
+ 0053387c bytes 283b00f0
- 005109ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 005109ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 00533884 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005109ec bytes 084140f9
+ 00533884 bytes 083945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd0afd6a363ef0ad0ca9de6136f9e63a"></a>

### [`00510a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510a58.md) → [`005338f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005338f0.md) FUN_005338f0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "0053390c",
      "incomplete_value": true,
      "site": "00533910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00533944",
      "incomplete_value": true,
      "site": "00533944",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00533904",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00533910",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00533934",
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
      "00533904",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "00533910",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00533934",
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

- 旧版 [`00510aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510a58.md#insn-00510aac) · [`00510a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510a58.md#insn-00510a64) · [`00510a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510a58.md#insn-00510a6c)
- 新版 [`00533944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005338f0.md#insn-00533944) · [`005338fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005338f0.md#insn-005338fc) · [`00533904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005338f0.md#insn-00533904)

~~~diff
- 00510aac ["COPY", "register:0:8", ["register:4048:8"]]
- 00510aac ["INT_ADD", "register:40f0:8", ["const:510aac:8", "const:4:8"]]
- 00510aac ["CALLIND", null, ["register:0:8"]]
+ 00533944 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533944 ["INT_ADD", "register:40f0:8", ["const:533944:8", "const:4:8"]]
+ 00533944 ["CALLIND", null, ["register:0:8"]]
- 00510aac bytes 20013fd6
+ 00533944 bytes 20013fd6
- 00510a64 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005338fc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00510a64 bytes 483800f0
+ 005338fc bytes 283b00f0
- 00510a6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 00510a6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533904 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 00533904 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00510a6c bytes 084140f9
+ 00533904 bytes 083945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4536e9e81c1732784c7167bb9b55b6c0"></a>

### [`00510acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510acc.md) → [`00533964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md) FUN_00533964

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00510be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510be8.md) [`00510c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c0c.md) [`00510c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c14.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 3件 [`00533a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533a80.md) [`00533aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533aa4.md) [`00533aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533aac.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "005339dc",
      "incomplete_value": true,
      "site": "005339e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00533a18",
      "incomplete_value": true,
      "site": "00533a1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "0053399c",
      "incomplete_value": true,
      "site": "0053399c",
      "value": [
        "LOAD",
        "8",
        [
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
      "0053398c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "005339d4",
      "READ",
      [
        "storage",
        "00c1b0b0",
        null,
        "pointer"
      ]
    ],
    [
      "005339e0",
      "DATA",
      [
        "storage",
        "00be98e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0053398c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "005339d4",
      "READ",
      [
        "storage",
        "00c9aaa0",
        null,
        "pointer"
      ]
    ],
    [
      "005339e0",
      "DATA",
      [
        "storage",
        "00c664a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00510b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510acc.md#insn-00510b04) · [`00510b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510acc.md#insn-00510b68) · [`00510bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510acc.md#insn-00510bb4)
- 新版 [`0053399c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md#insn-0053399c) · [`00533a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md#insn-00533a00) · [`00533a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533964.md#insn-00533a4c)

~~~diff
- 00510b04 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510b04 ["INT_ADD", "register:40f0:8", ["const:510b04:8", "const:4:8"]]
- 00510b04 ["CALLIND", null, ["register:0:8"]]
+ 0053399c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053399c ["INT_ADD", "register:40f0:8", ["const:53399c:8", "const:4:8"]]
+ 0053399c ["CALLIND", null, ["register:0:8"]]
- 00510b04 bytes 20013fd6
+ 0053399c bytes 20013fd6
- 00510b68 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510b68 ["INT_ADD", "register:40f0:8", ["const:510b68:8", "const:4:8"]]
- 00510b68 ["CALLIND", null, ["register:0:8"]]
+ 00533a00 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533a00 ["INT_ADD", "register:40f0:8", ["const:533a00:8", "const:4:8"]]
+ 00533a00 ["CALLIND", null, ["register:0:8"]]
- 00510b68 bytes 20013fd6
+ 00533a00 bytes 20013fd6
- 00510bb4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510bb4 ["INT_ADD", "register:40f0:8", ["const:510bb4:8", "const:4:8"]]
- 00510bb4 ["CALLIND", null, ["register:0:8"]]
+ 00533a4c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533a4c ["INT_ADD", "register:40f0:8", ["const:533a4c:8", "const:4:8"]]
+ 00533a4c ["CALLIND", null, ["register:0:8"]]
- 00510bb4 bytes 20013fd6
+ 00533a4c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3504fa824d91116b170486fbf3e3178"></a>

### [`00510c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c70.md) → [`00533b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533b08.md) FUN_00533b08

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00533b40",
      "incomplete_value": true,
      "site": "00533b40",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533b6c",
      "incomplete_value": true,
      "site": "00533b6c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00533b30",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00533b5c",
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
      "00533b30",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533b5c",
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

- 旧版 [`00510ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c70.md#insn-00510ca8) · [`00510cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c70.md#insn-00510cd4) · [`00510c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510c70.md#insn-00510c88)
- 新版 [`00533b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533b08.md#insn-00533b40) · [`00533b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533b08.md#insn-00533b6c) · [`00533b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533b08.md#insn-00533b20)

~~~diff
- 00510ca8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510ca8 ["INT_ADD", "register:40f0:8", ["const:510ca8:8", "const:4:8"]]
- 00510ca8 ["CALLIND", null, ["register:0:8"]]
+ 00533b40 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533b40 ["INT_ADD", "register:40f0:8", ["const:533b40:8", "const:4:8"]]
+ 00533b40 ["CALLIND", null, ["register:0:8"]]
- 00510ca8 bytes 20013fd6
+ 00533b40 bytes 20013fd6
- 00510cd4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510cd4 ["INT_ADD", "register:40f0:8", ["const:510cd4:8", "const:4:8"]]
- 00510cd4 ["CALLIND", null, ["register:0:8"]]
+ 00533b6c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533b6c ["INT_ADD", "register:40f0:8", ["const:533b6c:8", "const:4:8"]]
+ 00533b6c ["CALLIND", null, ["register:0:8"]]
- 00510cd4 bytes 20013fd6
+ 00533b6c bytes 20013fd6
- 00510c88 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00533b20 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00510c88 bytes d53600d0
+ 00533b20 bytes b5390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e9b7627bf7fdf1769cc45087cf56c0e"></a>

### [`00510d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510d1c.md) → [`00533bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533bb4.md) FUN_00533bb4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00533bec",
      "incomplete_value": true,
      "site": "00533bec",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533c18",
      "incomplete_value": true,
      "site": "00533c18",
      "value": [
        "LOAD",
        "8",
        [
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
      "00533bdc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00533c08",
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
      "00533bdc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533c08",
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

- 旧版 [`00510d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510d1c.md#insn-00510d54) · [`00510d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510d1c.md#insn-00510d80) · [`00510d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510d1c.md#insn-00510d34)
- 新版 [`00533bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533bb4.md#insn-00533bec) · [`00533c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533bb4.md#insn-00533c18) · [`00533bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533bb4.md#insn-00533bcc)

~~~diff
- 00510d54 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510d54 ["INT_ADD", "register:40f0:8", ["const:510d54:8", "const:4:8"]]
- 00510d54 ["CALLIND", null, ["register:0:8"]]
+ 00533bec ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533bec ["INT_ADD", "register:40f0:8", ["const:533bec:8", "const:4:8"]]
+ 00533bec ["CALLIND", null, ["register:0:8"]]
- 00510d54 bytes 20013fd6
+ 00533bec bytes 20013fd6
- 00510d80 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510d80 ["INT_ADD", "register:40f0:8", ["const:510d80:8", "const:4:8"]]
- 00510d80 ["CALLIND", null, ["register:0:8"]]
+ 00533c18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533c18 ["INT_ADD", "register:40f0:8", ["const:533c18:8", "const:4:8"]]
+ 00533c18 ["CALLIND", null, ["register:0:8"]]
- 00510d80 bytes 20013fd6
+ 00533c18 bytes 20013fd6
- 00510d34 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00533bcc ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00510d34 bytes d53600d0
+ 00533bcc bytes b5390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40411a51321ee612afc6ff608004c0ef"></a>

### [`00510dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510dc0.md) → [`00533c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533c58.md) FUN_00533c58

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58990.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "definition_site": "00533d00",
      "incomplete_value": true,
      "site": "00533d0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00533cfc",
      "incomplete_value": false,
      "site": "00533d0c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00510e64",
      "incomplete_value": false,
      "site": "00510e74",
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
      "00533cfc",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "00533d00",
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ],
    [
      "00533d00",
      "PARAM",
      [
        "storage",
        "00be94f0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00533cfc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00533d00",
      "READ",
      [
        "storage",
        "00c9aa40",
        null,
        "pointer"
      ]
    ],
    [
      "00533d00",
      "PARAM",
      [
        "storage",
        "00c660b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00510e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510dc0.md#insn-00510e74) · [`00510e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510dc0.md#insn-00510e18) · [`00510e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510dc0.md#insn-00510e30)
- 新版 [`00533d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533c58.md#insn-00533d0c) · [`00533cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533c58.md#insn-00533cb0) · [`00533cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533c58.md#insn-00533cc8)

~~~diff
- 00510e74 ["INT_ADD", "register:40f0:8", ["const:510e74:8", "const:4:8"]]
- 00510e74 ["CALL", null, ["callee:00c57b10:8"]]
+ 00533d0c ["INT_ADD", "register:40f0:8", ["const:533d0c:8", "const:4:8"]]
+ 00533d0c ["CALL", null, ["callee:00c57b10:8"]]
- 00510e74 bytes 93281b94
+ 00533d0c bytes 818f1c94
- 00510e18 ["INT_ADD", "register:40f0:8", ["const:510e18:8", "const:4:8"]]
- 00510e18 ["CALL", null, ["callee:00c57af0:8"]]
+ 00533cb0 ["INT_ADD", "register:40f0:8", ["const:533cb0:8", "const:4:8"]]
+ 00533cb0 ["CALL", null, ["callee:00c57af0:8"]]
- 00510e18 bytes a2281b94
+ 00533cb0 bytes 908f1c94
- 00510e30 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510e30 ["INT_ADD", "register:40f0:8", ["const:510e30:8", "const:4:8"]]
- 00510e30 ["CALLIND", null, ["register:0:8"]]
+ 00533cc8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533cc8 ["INT_ADD", "register:40f0:8", ["const:533cc8:8", "const:4:8"]]
+ 00533cc8 ["CALLIND", null, ["register:0:8"]]
- 00510e30 bytes 20013fd6
+ 00533cc8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77702e919b12e649c77193dc6fcf50a5"></a>

### [`00510f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510f14.md) → [`00533dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533dac.md) FUN_00533dac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00533de4",
      "incomplete_value": true,
      "site": "00533de4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533e10",
      "incomplete_value": true,
      "site": "00533e10",
      "value": [
        "LOAD",
        "8",
        [
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
      "00533dd4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00533e00",
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
      "00533dd4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533e00",
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

- 旧版 [`00510f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510f14.md#insn-00510f4c) · [`00510f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510f14.md#insn-00510f78) · [`00510f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510f14.md#insn-00510f2c)
- 新版 [`00533de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533dac.md#insn-00533de4) · [`00533e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533dac.md#insn-00533e10) · [`00533dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533dac.md#insn-00533dc4)

~~~diff
- 00510f4c ["COPY", "register:0:8", ["register:4048:8"]]
- 00510f4c ["INT_ADD", "register:40f0:8", ["const:510f4c:8", "const:4:8"]]
- 00510f4c ["CALLIND", null, ["register:0:8"]]
+ 00533de4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533de4 ["INT_ADD", "register:40f0:8", ["const:533de4:8", "const:4:8"]]
+ 00533de4 ["CALLIND", null, ["register:0:8"]]
- 00510f4c bytes 20013fd6
+ 00533de4 bytes 20013fd6
- 00510f78 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510f78 ["INT_ADD", "register:40f0:8", ["const:510f78:8", "const:4:8"]]
- 00510f78 ["CALLIND", null, ["register:0:8"]]
+ 00533e10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533e10 ["INT_ADD", "register:40f0:8", ["const:533e10:8", "const:4:8"]]
+ 00533e10 ["CALLIND", null, ["register:0:8"]]
- 00510f78 bytes 20013fd6
+ 00533e10 bytes 20013fd6
- 00510f2c ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00533dc4 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00510f2c bytes d53600d0
+ 00533dc4 bytes b5390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b35b9fc1037471c79523c1913480ab25"></a>

### [`00510fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510fc0.md) → [`00533e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533e58.md) FUN_00533e58

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00533e90",
      "incomplete_value": true,
      "site": "00533e90",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533ebc",
      "incomplete_value": true,
      "site": "00533ebc",
      "value": [
        "LOAD",
        "8",
        [
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
      "00533e80",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00533eac",
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
      "00533e80",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00533eac",
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

- 旧版 [`00510ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510fc0.md#insn-00510ff8) · [`00511024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510fc0.md#insn-00511024) · [`00510fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/00510fc0.md#insn-00510fd8)
- 新版 [`00533e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533e58.md#insn-00533e90) · [`00533ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533e58.md#insn-00533ebc) · [`00533e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533e58.md#insn-00533e70)

~~~diff
- 00510ff8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00510ff8 ["INT_ADD", "register:40f0:8", ["const:510ff8:8", "const:4:8"]]
- 00510ff8 ["CALLIND", null, ["register:0:8"]]
+ 00533e90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533e90 ["INT_ADD", "register:40f0:8", ["const:533e90:8", "const:4:8"]]
+ 00533e90 ["CALLIND", null, ["register:0:8"]]
- 00510ff8 bytes 20013fd6
+ 00533e90 bytes 20013fd6
- 00511024 ["COPY", "register:0:8", ["register:4048:8"]]
- 00511024 ["INT_ADD", "register:40f0:8", ["const:511024:8", "const:4:8"]]
- 00511024 ["CALLIND", null, ["register:0:8"]]
+ 00533ebc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533ebc ["INT_ADD", "register:40f0:8", ["const:533ebc:8", "const:4:8"]]
+ 00533ebc ["CALLIND", null, ["register:0:8"]]
- 00511024 bytes 20013fd6
+ 00533ebc bytes 20013fd6
- 00510fd8 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00533e70 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00510fd8 bytes d53600d0
+ 00533e70 bytes b5390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-480a4e5f6fb689166cd35867f2ee55ef"></a>

### [`00511164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511164.md) → [`00533ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533ffc.md) FUN_00533ffc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00534014",
      "incomplete_value": false,
      "site": "00534018",
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
            "const:a68:8"
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
      "00534018",
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
      "00534018",
      "DATA",
      [
        "storage",
        "00c66a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511164.md#insn-00511178) · [`0051117c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511164.md#insn-0051117c) · [`0051118c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511164.md#insn-0051118c)
- 新版 [`00534010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533ffc.md#insn-00534010) · [`00534014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533ffc.md#insn-00534014) · [`00534024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533ffc.md#insn-00534024)

~~~diff
- 00511178 ["COPY", "register:4048:8", ["const:be9000:8"]]
+ 00534010 ["COPY", "register:4048:8", ["const:c66000:8"]]
- 00511178 bytes c9360090
+ 00534010 bytes 893900d0
- 0051117c ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 0051117c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051117c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051117c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534014 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 00534014 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534014 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534014 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051117c bytes 29a13a91
+ 00534014 bytes 29a12991
- 0051118c ["INT_ADD", "register:40f0:8", ["const:51118c:8", "const:4:8"]]
- 0051118c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00534024 ["INT_ADD", "register:40f0:8", ["const:534024:8", "const:4:8"]]
+ 00534024 ["CALL", null, ["callee:00c57ab0:8"]]
- 0051118c bytes b5271b94
+ 00534024 bytes a38e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-130aa31ad1ce4b1b92fed4c3c102fa4d"></a>

### [`005111c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005111c8.md) → [`00534060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534060.md) FUN_00534060

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb970.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c583c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005340a8",
      "incomplete_value": true,
      "site": "005340a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e2:8"
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
                "const:8f1:8"
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
      "definition_site": "005340d4",
      "incomplete_value": true,
      "site": "005340e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
                "const:f98:8"
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
      "definition_site": "005340d0",
      "incomplete_value": false,
      "site": "005340e0",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00511238",
      "incomplete_value": false,
      "site": "00511248",
      "value": [
        "leaf",
        "const:512990:8"
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
      "00534094",
      "READ",
      [
        "storage",
        "002a68f1",
        null,
        "string"
      ]
    ],
    [
      "005340d0",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "005340d4",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534094",
      "READ",
      [
        "storage",
        "002b73e2",
        null,
        "string"
      ]
    ],
    [
      "005340d0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005340d4",
      "READ",
      [
        "storage",
        "00c9a988",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005111c8.md#insn-00511248) · [`005111ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005111c8.md#insn-005111ec) · [`005111f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005111c8.md#insn-005111f0)
- 新版 [`005340e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534060.md#insn-005340e0) · [`00534084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534060.md#insn-00534084) · [`00534088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534060.md#insn-00534088)

~~~diff
- 00511248 ["INT_ADD", "register:40f0:8", ["const:511248:8", "const:4:8"]]
- 00511248 ["CALL", null, ["callee:00c57b10:8"]]
+ 005340e0 ["INT_ADD", "register:40f0:8", ["const:5340e0:8", "const:4:8"]]
+ 005340e0 ["CALL", null, ["callee:00c57b10:8"]]
- 00511248 bytes 9e271b94
+ 005340e0 bytes 8c8e1c94
- 005111ec ["INT_ADD", "register:40f0:8", ["const:5111ec:8", "const:4:8"]]
- 005111ec ["CALL", null, ["callee:00c57af0:8"]]
+ 00534084 ["INT_ADD", "register:40f0:8", ["const:534084:8", "const:4:8"]]
+ 00534084 ["CALL", null, ["callee:00c57af0:8"]]
- 005111ec bytes ad271b94
+ 00534084 bytes 9b8e1c94
- 005111f0 ["COPY", "register:4048:8", ["const:2a6000:8"]]
+ 00534088 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 005111f0 bytes a9ecffb0
+ 00534088 bytes 09ecfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac8d8b02a356d27ceb6c0024fcfb8ad6"></a>

### [`00511290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511290.md) → [`00534128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534128.md) FUN_00534128

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00534140",
      "incomplete_value": false,
      "site": "00534144",
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
            "const:ab8:8"
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
            "const:ef8:8"
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
      "00534144",
      "DATA",
      [
        "storage",
        "00be9ef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00534144",
      "DATA",
      [
        "storage",
        "00c66ab8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005112a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511290.md#insn-005112a4) · [`005112a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511290.md#insn-005112a8) · [`005112b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511290.md#insn-005112b8)
- 新版 [`0053413c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534128.md#insn-0053413c) · [`00534140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534128.md#insn-00534140) · [`00534150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534128.md#insn-00534150)

~~~diff
- 005112a4 ["COPY", "register:4048:8", ["const:be9000:8"]]
+ 0053413c ["COPY", "register:4048:8", ["const:c66000:8"]]
- 005112a4 bytes c9360090
+ 0053413c bytes 893900d0
- 005112a8 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 005112a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005112a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005112a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534140 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 00534140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005112a8 bytes 29e13b91
+ 00534140 bytes 29e12a91
- 005112b8 ["INT_ADD", "register:40f0:8", ["const:5112b8:8", "const:4:8"]]
- 005112b8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00534150 ["INT_ADD", "register:40f0:8", ["const:534150:8", "const:4:8"]]
+ 00534150 ["CALL", null, ["callee:00c57ab0:8"]]
- 005112b8 bytes 6a271b94
+ 00534150 bytes 588e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cd25ba263c4b4ac566e6099c24b1537"></a>

### [`005112f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005112f4.md) → [`0053418c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053418c.md) FUN_0053418c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb970.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c583c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005341d4",
      "incomplete_value": true,
      "site": "005341d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e2:8"
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
                "const:8f1:8"
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
      "definition_site": "00534200",
      "incomplete_value": true,
      "site": "0053420c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
                "const:f98:8"
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
      "definition_site": "005341fc",
      "incomplete_value": false,
      "site": "0053420c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00511364",
      "incomplete_value": false,
      "site": "00511374",
      "value": [
        "leaf",
        "const:512990:8"
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
      "005341c0",
      "READ",
      [
        "storage",
        "002a68f1",
        null,
        "string"
      ]
    ],
    [
      "005341fc",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "00534200",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005341c0",
      "READ",
      [
        "storage",
        "002b73e2",
        null,
        "string"
      ]
    ],
    [
      "005341fc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00534200",
      "READ",
      [
        "storage",
        "00c9a988",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005112f4.md#insn-00511374) · [`00511318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005112f4.md#insn-00511318) · [`0051131c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005112f4.md#insn-0051131c)
- 新版 [`0053420c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053418c.md#insn-0053420c) · [`005341b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053418c.md#insn-005341b0) · [`005341b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053418c.md#insn-005341b4)

~~~diff
- 00511374 ["INT_ADD", "register:40f0:8", ["const:511374:8", "const:4:8"]]
- 00511374 ["CALL", null, ["callee:00c57b10:8"]]
+ 0053420c ["INT_ADD", "register:40f0:8", ["const:53420c:8", "const:4:8"]]
+ 0053420c ["CALL", null, ["callee:00c57b10:8"]]
- 00511374 bytes 53271b94
+ 0053420c bytes 418e1c94
- 00511318 ["INT_ADD", "register:40f0:8", ["const:511318:8", "const:4:8"]]
- 00511318 ["CALL", null, ["callee:00c57af0:8"]]
+ 005341b0 ["INT_ADD", "register:40f0:8", ["const:5341b0:8", "const:4:8"]]
+ 005341b0 ["CALL", null, ["callee:00c57af0:8"]]
- 00511318 bytes 62271b94
+ 005341b0 bytes 508e1c94
- 0051131c ["COPY", "register:4048:8", ["const:2a6000:8"]]
+ 005341b4 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 0051131c bytes a9ecffb0
+ 005341b4 bytes 09ecfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d36077c921ad208194238c5f7cc9aa1"></a>

### [`005113bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005113bc.md) → [`00534254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534254.md) FUN_00534254

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534284",
      "incomplete_value": true,
      "site": "00534298",
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
                "const:d90:8"
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
                "const:744:8"
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
      "definition_site": "00534288",
      "incomplete_value": true,
      "site": "0053429c",
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
      "definition_site": "005342a8",
      "incomplete_value": true,
      "site": "005342a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00534284",
      "READ",
      [
        "storage",
        "002a1744",
        null,
        "string"
      ]
    ],
    [
      "00534288",
      "READ",
      [
        "storage",
        "002a174d",
        null,
        "string"
      ]
    ],
    [
      "00534290",
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
      "00534284",
      "READ",
      [
        "storage",
        "002b1d90",
        null,
        "string"
      ]
    ],
    [
      "00534288",
      "READ",
      [
        "storage",
        "002b1d99",
        null,
        "string"
      ]
    ],
    [
      "00534290",
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

- 旧版 [`00511444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005113bc.md#insn-00511444) · [`005113d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005113bc.md#insn-005113d0) · [`005113dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005113bc.md#insn-005113dc)
- 新版 [`005342dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534254.md#insn-005342dc) · [`00534268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534254.md#insn-00534268) · [`00534274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534254.md#insn-00534274)

~~~diff
- 00511444 ["INT_ADD", "register:40f0:8", ["const:511444:8", "const:4:8"]]
- 00511444 ["CALL", null, ["callee:00c57b10:8"]]
+ 005342dc ["INT_ADD", "register:40f0:8", ["const:5342dc:8", "const:4:8"]]
+ 005342dc ["CALL", null, ["callee:00c57b10:8"]]
- 00511444 bytes 1f271b94
+ 005342dc bytes 0d8e1c94
- 005113d0 ["INT_ADD", "register:40f0:8", ["const:5113d0:8", "const:4:8"]]
- 005113d0 ["CALL", null, ["callee:00c57af0:8"]]
+ 00534268 ["INT_ADD", "register:40f0:8", ["const:534268:8", "const:4:8"]]
+ 00534268 ["CALL", null, ["callee:00c57af0:8"]]
- 005113d0 bytes 34271b94
+ 00534268 bytes 228e1c94
- 005113dc ["INT_ADD", "register:40f0:8", ["const:5113dc:8", "const:4:8"]]
- 005113dc ["CALL", null, ["callee:00c57a90:8"]]
+ 00534274 ["INT_ADD", "register:40f0:8", ["const:534274:8", "const:4:8"]]
+ 00534274 ["CALL", null, ["callee:00c57a90:8"]]
- 005113dc bytes 19271b94
+ 00534274 bytes 078e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f089e93fca6d4e7a52ca8eeee9791838"></a>

### [`00511488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511488.md) → [`00534320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534320.md) FUN_00534320

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534350",
      "incomplete_value": true,
      "site": "00534364",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:6c8:8"
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
                "const:b93:8"
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
      "definition_site": "00534354",
      "incomplete_value": true,
      "site": "00534368",
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
      "definition_site": "00534374",
      "incomplete_value": true,
      "site": "00534374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00534350",
      "READ",
      [
        "storage",
        "00296b93",
        null,
        "string"
      ]
    ],
    [
      "00534354",
      "READ",
      [
        "storage",
        "00296ba1",
        null,
        "string"
      ]
    ],
    [
      "0053435c",
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
      "00534350",
      "READ",
      [
        "storage",
        "002a66c8",
        null,
        "string"
      ]
    ],
    [
      "00534354",
      "READ",
      [
        "storage",
        "002a66d6",
        null,
        "string"
      ]
    ],
    [
      "0053435c",
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

- 旧版 [`00511510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511488.md#insn-00511510) · [`0051149c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511488.md#insn-0051149c) · [`005114a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511488.md#insn-005114a8)
- 新版 [`005343a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534320.md#insn-005343a8) · [`00534334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534320.md#insn-00534334) · [`00534340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534320.md#insn-00534340)

~~~diff
- 00511510 ["INT_ADD", "register:40f0:8", ["const:511510:8", "const:4:8"]]
- 00511510 ["CALL", null, ["callee:00c57b10:8"]]
+ 005343a8 ["INT_ADD", "register:40f0:8", ["const:5343a8:8", "const:4:8"]]
+ 005343a8 ["CALL", null, ["callee:00c57b10:8"]]
- 00511510 bytes ec261b94
+ 005343a8 bytes da8d1c94
- 0051149c ["INT_ADD", "register:40f0:8", ["const:51149c:8", "const:4:8"]]
- 0051149c ["CALL", null, ["callee:00c57af0:8"]]
+ 00534334 ["INT_ADD", "register:40f0:8", ["const:534334:8", "const:4:8"]]
+ 00534334 ["CALL", null, ["callee:00c57af0:8"]]
- 0051149c bytes 01271b94
+ 00534334 bytes ef8d1c94
- 005114a8 ["INT_ADD", "register:40f0:8", ["const:5114a8:8", "const:4:8"]]
- 005114a8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00534340 ["INT_ADD", "register:40f0:8", ["const:534340:8", "const:4:8"]]
+ 00534340 ["CALL", null, ["callee:00c57a90:8"]]
- 005114a8 bytes e6261b94
+ 00534340 bytes d48d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c815bd15f1637330a1a1fcb51d1b349"></a>

### [`00511554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511554.md) → [`005343ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005343ec.md) FUN_005343ec

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005343fc",
      "incomplete_value": false,
      "site": "005343fc",
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
      "005343fc",
      "DATA",
      [
        "storage",
        "00be9f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005343fc",
      "DATA",
      [
        "storage",
        "00c66b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051155c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511554.md#insn-0051155c) · [`00511560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511554.md#insn-00511560)
- 新版 [`005343f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005343ec.md#insn-005343f4) · [`005343f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005343ec.md#insn-005343f8)

~~~diff
- 0051155c ["COPY", "register:4048:8", ["const:be9000:8"]]
+ 005343f4 ["COPY", "register:4048:8", ["const:c66000:8"]]
- 0051155c bytes c9360090
+ 005343f4 bytes 893900d0
- 00511560 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00511560 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00511560 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00511560 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005343f8 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 005343f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005343f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005343f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00511560 bytes 29613d91
+ 005343f8 bytes 29612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56f4ba8c7de0dee7e94ea561f968ec45"></a>

### [`00511580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511580.md) → [`00534418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534418.md) FUN_00534418

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00534428",
      "incomplete_value": false,
      "site": "00534428",
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
      "00534428",
      "DATA",
      [
        "storage",
        "00be9f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00534428",
      "DATA",
      [
        "storage",
        "00c66b48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511580.md#insn-00511588) · [`0051158c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511580.md#insn-0051158c)
- 新版 [`00534420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534418.md#insn-00534420) · [`00534424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534418.md#insn-00534424)

~~~diff
- 00511588 ["COPY", "register:4048:8", ["const:be9000:8"]]
+ 00534420 ["COPY", "register:4048:8", ["const:c66000:8"]]
- 00511588 bytes c9360090
+ 00534420 bytes 893900d0
- 0051158c ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0051158c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051158c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051158c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534424 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00534424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051158c bytes 29213e91
+ 00534424 bytes 29212d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9102f90651401957f392eacb68459b73"></a>

### [`005115ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005115ac.md) → [`00534444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534444.md) FUN_00534444

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00534468",
      "incomplete_value": true,
      "site": "00534474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00534494",
      "incomplete_value": true,
      "site": "00534494",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005344c0",
      "incomplete_value": true,
      "site": "005344c0",
      "value": [
        "LOAD",
        "8",
        [
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
      "0053445c",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "00534474",
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00534484",
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
      "0053445c",
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      "00534474",
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00534484",
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

- 旧版 [`005115fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005115ac.md#insn-005115fc) · [`00511628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005115ac.md#insn-00511628) · [`005115bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005115ac.md#insn-005115bc)
- 新版 [`00534494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534444.md#insn-00534494) · [`005344c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534444.md#insn-005344c0) · [`00534454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534444.md#insn-00534454)

~~~diff
- 005115fc ["COPY", "register:0:8", ["register:4048:8"]]
- 005115fc ["INT_ADD", "register:40f0:8", ["const:5115fc:8", "const:4:8"]]
- 005115fc ["CALLIND", null, ["register:0:8"]]
+ 00534494 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534494 ["INT_ADD", "register:40f0:8", ["const:534494:8", "const:4:8"]]
+ 00534494 ["CALLIND", null, ["register:0:8"]]
- 005115fc bytes 20013fd6
+ 00534494 bytes 20013fd6
- 00511628 ["COPY", "register:0:8", ["register:4048:8"]]
- 00511628 ["INT_ADD", "register:40f0:8", ["const:511628:8", "const:4:8"]]
- 00511628 ["CALLIND", null, ["register:0:8"]]
+ 005344c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005344c0 ["INT_ADD", "register:40f0:8", ["const:5344c0:8", "const:4:8"]]
+ 005344c0 ["CALLIND", null, ["register:0:8"]]
- 00511628 bytes 20013fd6
+ 005344c0 bytes 20013fd6
- 005115bc ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00534454 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005115bc bytes 483800d0
+ 00534454 bytes 283b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7b6bb1b768f63b8dcc672657b99d87c"></a>

### [`00511658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511658.md) → [`005344f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005344f0.md) FUN_005344f0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00534514",
      "incomplete_value": true,
      "site": "00534520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00534540",
      "incomplete_value": true,
      "site": "00534540",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0053456c",
      "incomplete_value": true,
      "site": "0053456c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00534508",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "00534520",
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00534530",
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
      "00534508",
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      "00534520",
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00534530",
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

- 旧版 [`005116a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511658.md#insn-005116a8) · [`005116d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511658.md#insn-005116d4) · [`00511668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511658.md#insn-00511668)
- 新版 [`00534540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005344f0.md#insn-00534540) · [`0053456c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005344f0.md#insn-0053456c) · [`00534500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005344f0.md#insn-00534500)

~~~diff
- 005116a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005116a8 ["INT_ADD", "register:40f0:8", ["const:5116a8:8", "const:4:8"]]
- 005116a8 ["CALLIND", null, ["register:0:8"]]
+ 00534540 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534540 ["INT_ADD", "register:40f0:8", ["const:534540:8", "const:4:8"]]
+ 00534540 ["CALLIND", null, ["register:0:8"]]
- 005116a8 bytes 20013fd6
+ 00534540 bytes 20013fd6
- 005116d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005116d4 ["INT_ADD", "register:40f0:8", ["const:5116d4:8", "const:4:8"]]
- 005116d4 ["CALLIND", null, ["register:0:8"]]
+ 0053456c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053456c ["INT_ADD", "register:40f0:8", ["const:53456c:8", "const:4:8"]]
+ 0053456c ["CALLIND", null, ["register:0:8"]]
- 005116d4 bytes 20013fd6
+ 0053456c bytes 20013fd6
- 00511668 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00534500 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00511668 bytes 483800d0
+ 00534500 bytes 283b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a80c2bd9f0220a532ecfb77bcb8f1ce1"></a>

### [`00511720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511720.md) → [`005345b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345b8.md) FUN_005345b8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d1fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00540094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "005345cc",
      "incomplete_value": true,
      "site": "005345d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
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
                "const:1f8:8"
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
      "005345cc",
      "READ",
      [
        "storage",
        "00c1b1f8",
        null,
        "pointer"
      ]
    ],
    [
      "005345cc",
      "PARAM",
      [
        "storage",
        "00bea368",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      "005345cc",
      "READ",
      [
        "storage",
        "00c9abe8",
        null,
        "pointer"
      ]
    ],
    [
      "005345cc",
      "PARAM",
      [
        "storage",
        "00c66f28",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511720.md#insn-00511738) · [`0051172c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511720.md#insn-0051172c) · [`00511734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511720.md#insn-00511734)
- 新版 [`005345d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345b8.md#insn-005345d0) · [`005345c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345b8.md#insn-005345c4) · [`005345cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345b8.md#insn-005345cc)

~~~diff
- 00511738 ["INT_ADD", "register:40f0:8", ["const:511738:8", "const:4:8"]]
- 00511738 ["CALL", null, ["callee:00540094:8"]]
+ 005345d0 ["INT_ADD", "register:40f0:8", ["const:5345d0:8", "const:4:8"]]
+ 005345d0 ["CALL", null, ["callee:00540094:8"]]
- 00511738 bytes b12e0094
+ 005345d0 bytes b12e0094
- 0051172c ["COPY", "register:4008:8", ["const:c1b000:8"]]
+ 005345c4 ["COPY", "register:4008:8", ["const:c9a000:8"]]
- 0051172c bytes 413800d0
+ 005345c4 bytes 213b00d0
- 00511734 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1f8:8"]]
- 00511734 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005345cc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:be8:8"]]
+ 005345cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00511734 bytes 21fc40f9
+ 005345cc bytes 21f445f9
~~~


<a id="compare-9a5c26d241d18911a6f098a650dd70fc"></a>

### [`0051175c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051175c.md) → [`005345f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345f4.md) FUN_005345f4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d1fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00540094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540094.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00534608",
      "incomplete_value": true,
      "site": "00534610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
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
                "const:1f8:8"
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
      "00534608",
      "READ",
      [
        "storage",
        "00c1b1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00534608",
      "PARAM",
      [
        "storage",
        "00bea368",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      "00534608",
      "READ",
      [
        "storage",
        "00c9abe8",
        null,
        "pointer"
      ]
    ],
    [
      "00534608",
      "PARAM",
      [
        "storage",
        "00c66f28",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051175c.md#insn-00511778) · [`00511768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051175c.md#insn-00511768) · [`00511770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/0051175c.md#insn-00511770)
- 新版 [`00534610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345f4.md#insn-00534610) · [`00534600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345f4.md#insn-00534600) · [`00534608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005345f4.md#insn-00534608)

~~~diff
- 00511778 ["INT_ADD", "register:40f0:8", ["const:511778:8", "const:4:8"]]
- 00511778 ["CALL", null, ["callee:00540094:8"]]
+ 00534610 ["INT_ADD", "register:40f0:8", ["const:534610:8", "const:4:8"]]
+ 00534610 ["CALL", null, ["callee:00540094:8"]]
- 00511778 bytes a12e0094
+ 00534610 bytes a12e0094
- 00511768 ["COPY", "register:4008:8", ["const:c1b000:8"]]
+ 00534600 ["COPY", "register:4008:8", ["const:c9a000:8"]]
- 00511768 bytes 413800d0
+ 00534600 bytes 213b00d0
- 00511770 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:1f8:8"]]
- 00511770 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534608 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:be8:8"]]
+ 00534608 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00511770 bytes 21fc40f9
+ 00534608 bytes 21f445f9
~~~


<a id="compare-719f243a005d2460a6bb09e38e396db4"></a>

### [`00511934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511934.md) → [`005347cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005347cc.md) FUN_005347cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "005347e8",
      "incomplete_value": true,
      "site": "005347ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00534828",
      "incomplete_value": true,
      "site": "0053482c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005347e0",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "005347ec",
      "DATA",
      [
        "storage",
        "00beaac8",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00534820",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005347e0",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "005347ec",
      "DATA",
      [
        "storage",
        "00c67688",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00534820",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511934.md#insn-00511940) · [`00511948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511934.md#insn-00511948) · [`00511964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511934.md#insn-00511964)
- 新版 [`005347d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005347cc.md#insn-005347d8) · [`005347e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005347cc.md#insn-005347e0) · [`005347fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/005347cc.md#insn-005347fc)

~~~diff
- 00511940 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005347d8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00511940 bytes 483800d0
+ 005347d8 bytes 283b00d0
- 00511948 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
- 00511948 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005347e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce0:8"]]
+ 005347e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00511948 bytes 087941f9
+ 005347e0 bytes 087146f9
- 00511964 ["INT_ADD", "register:40f0:8", ["const:511964:8", "const:4:8"]]
- 00511964 ["CALL", null, ["callee:00c538e0:8"]]
+ 005347fc ["INT_ADD", "register:40f0:8", ["const:5347fc:8", "const:4:8"]]
+ 005347fc ["CALL", null, ["callee:00c538e0:8"]]
- 00511964 bytes 4b151b94
+ 005347fc bytes 397c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2db1dfd9f7f85443cf05d376df191004"></a>

### [`005119e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005119e4.md) → [`0053487c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053487c.md) FUN_0053487c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00534898",
      "incomplete_value": true,
      "site": "0053489c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00534890",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "0053489c",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00534890",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "0053489c",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005119f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005119e4.md#insn-005119f0) · [`005119f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005119e4.md#insn-005119f8) · [`00511a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/005119e4.md#insn-00511a10)
- 新版 [`00534888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053487c.md#insn-00534888) · [`00534890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053487c.md#insn-00534890) · [`005348a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/0053487c.md#insn-005348a8)

~~~diff
- 005119f0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00534888 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005119f0 bytes 483800d0
+ 00534888 bytes 283b00d0
- 005119f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
- 005119f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534890 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 00534890 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005119f8 bytes 08b541f9
+ 00534890 bytes 08ad46f9
- 00511a10 ["INT_ADD", "register:40f0:8", ["const:511a10:8", "const:4:8"]]
- 00511a10 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005348a8 ["INT_ADD", "register:40f0:8", ["const:5348a8:8", "const:4:8"]]
+ 005348a8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00511a10 bytes 94251b94
+ 005348a8 bytes 828c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10231d7473b8c4af9b885318920daf30"></a>

### [`00511eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511eb0.md) → [`00534d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534d48.md) FUN_00534d48

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00534d64",
      "incomplete_value": true,
      "site": "00534d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00534d5c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00534d68",
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
      "00534d5c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00534d68",
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

- 旧版 [`00511ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511eb0.md#insn-00511ebc) · [`00511ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511eb0.md#insn-00511ec4) · [`00511edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511eb0.md#insn-00511edc)
- 新版 [`00534d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534d48.md#insn-00534d54) · [`00534d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534d48.md#insn-00534d5c) · [`00534d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534d48.md#insn-00534d74)

~~~diff
- 00511ebc ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00534d54 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00511ebc bytes 483800b0
+ 00534d54 bytes 283b00d0
- 00511ec4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00511ec4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534d5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00534d5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00511ec4 bytes 08f147f9
+ 00534d5c bytes 08e944f9
- 00511edc ["INT_ADD", "register:40f0:8", ["const:511edc:8", "const:4:8"]]
- 00511edc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00534d74 ["INT_ADD", "register:40f0:8", ["const:534d74:8", "const:4:8"]]
+ 00534d74 ["CALL", null, ["callee:00c57ab0:8"]]
- 00511edc bytes 61241b94
+ 00534d74 bytes 4f8b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad198a2b59558650516ff723cb461956"></a>

### [`00511f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511f10.md) → [`00534da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534da8.md) FUN_00534da8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00534dc4",
      "incomplete_value": true,
      "site": "00534dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00534dbc",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00534dc8",
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
      "00534dbc",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00534dc8",
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

- 旧版 [`00511f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511f10.md#insn-00511f1c) · [`00511f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511f10.md#insn-00511f24) · [`00511f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511f10.md#insn-00511f3c)
- 新版 [`00534db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534da8.md#insn-00534db4) · [`00534dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534da8.md#insn-00534dbc) · [`00534dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534da8.md#insn-00534dd4)

~~~diff
- 00511f1c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00534db4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00511f1c bytes 483800b0
+ 00534db4 bytes 283b00d0
- 00511f24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00511f24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534dbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00534dbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00511f24 bytes 08f147f9
+ 00534dbc bytes 08e944f9
- 00511f3c ["INT_ADD", "register:40f0:8", ["const:511f3c:8", "const:4:8"]]
- 00511f3c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00534dd4 ["INT_ADD", "register:40f0:8", ["const:534dd4:8", "const:4:8"]]
+ 00534dd4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00511f3c bytes 49241b94
+ 00534dd4 bytes 378b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9bfcc74e437d87c55c0f3bec7546edd"></a>

### [`00511fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511fe0.md) → [`00534e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534e78.md) FUN_00534e78

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00534e94",
      "incomplete_value": true,
      "site": "00534e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00534ecc",
      "incomplete_value": true,
      "site": "00534ecc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00534e8c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00534e98",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534ebc",
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
      "00534e8c",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "00534e98",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534ebc",
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

- 旧版 [`00512034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511fe0.md#insn-00512034) · [`00511fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511fe0.md#insn-00511fec) · [`00511ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00511/00511fe0.md#insn-00511ff4)
- 新版 [`00534ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534e78.md#insn-00534ecc) · [`00534e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534e78.md#insn-00534e84) · [`00534e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534e78.md#insn-00534e8c)

~~~diff
- 00512034 ["COPY", "register:0:8", ["register:4048:8"]]
- 00512034 ["INT_ADD", "register:40f0:8", ["const:512034:8", "const:4:8"]]
- 00512034 ["CALLIND", null, ["register:0:8"]]
+ 00534ecc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534ecc ["INT_ADD", "register:40f0:8", ["const:534ecc:8", "const:4:8"]]
+ 00534ecc ["CALLIND", null, ["register:0:8"]]
- 00512034 bytes 20013fd6
+ 00534ecc bytes 20013fd6
- 00511fec ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00534e84 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00511fec bytes 483800d0
+ 00534e84 bytes 283b00d0
- 00511ff4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 00511ff4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534e8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 00534e8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00511ff4 bytes 084140f9
+ 00534e8c bytes 083945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f25470d318b5281b1cd06d172680a46"></a>

### [`00512058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512058.md) → [`00534ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ef0.md) FUN_00534ef0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00534f0c",
      "incomplete_value": true,
      "site": "00534f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00534f44",
      "incomplete_value": true,
      "site": "00534f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00534f04",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00534f10",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534f34",
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
      "00534f04",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "00534f10",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00534f34",
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

- 旧版 [`005120ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512058.md#insn-005120ac) · [`00512064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512058.md#insn-00512064) · [`0051206c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512058.md#insn-0051206c)
- 新版 [`00534f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ef0.md#insn-00534f44) · [`00534efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ef0.md#insn-00534efc) · [`00534f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ef0.md#insn-00534f04)

~~~diff
- 005120ac ["COPY", "register:0:8", ["register:4048:8"]]
- 005120ac ["INT_ADD", "register:40f0:8", ["const:5120ac:8", "const:4:8"]]
- 005120ac ["CALLIND", null, ["register:0:8"]]
+ 00534f44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534f44 ["INT_ADD", "register:40f0:8", ["const:534f44:8", "const:4:8"]]
+ 00534f44 ["CALLIND", null, ["register:0:8"]]
- 005120ac bytes 20013fd6
+ 00534f44 bytes 20013fd6
- 00512064 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00534efc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512064 bytes 483800b0
+ 00534efc bytes 283b00d0
- 0051206c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 0051206c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534f04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 00534f04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051206c bytes 084140f9
+ 00534f04 bytes 083945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbc1355cb75f0b274de7c86ea059de22"></a>

### [`0051215c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/0051215c.md) → [`00534ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ff4.md) FUN_00534ff4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00535008",
      "incomplete_value": true,
      "site": "00535008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00534ffc",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00535008",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00534ffc",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "00535008",
      "DATA",
      [
        "storage",
        "00c66958",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051215c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/0051215c.md#insn-0051215c) · [`00512164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/0051215c.md#insn-00512164)
- 新版 [`00534ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ff4.md#insn-00534ff4) · [`00534ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00534/00534ff4.md#insn-00534ffc)

~~~diff
- 0051215c ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 00534ff4 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0051215c bytes 493800b0
+ 00534ff4 bytes 293b00d0
- 00512164 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1c0:8"]]
- 00512164 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534ffc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bb0:8"]]
+ 00534ffc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00512164 bytes 29e140f9
+ 00534ffc bytes 29d945f9
~~~


<a id="compare-0f635d445cfcc7ff223332ab5f3a4bb8"></a>

### [`00512480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512480.md) → [`00535318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535318.md) FUN_00535318

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00535334",
      "incomplete_value": true,
      "site": "00535338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "0053532c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535338",
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
      "0053532c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535338",
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

- 旧版 [`0051248c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512480.md#insn-0051248c) · [`00512494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512480.md#insn-00512494) · [`005124ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512480.md#insn-005124ac)
- 新版 [`00535324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535318.md#insn-00535324) · [`0053532c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535318.md#insn-0053532c) · [`00535344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535318.md#insn-00535344)

~~~diff
- 0051248c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535324 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051248c bytes 48380090
+ 00535324 bytes 283b00b0
- 00512494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00512494 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053532c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 0053532c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512494 bytes 08f147f9
+ 0053532c bytes 08e944f9
- 005124ac ["INT_ADD", "register:40f0:8", ["const:5124ac:8", "const:4:8"]]
- 005124ac ["CALL", null, ["callee:00c57ab0:8"]]
+ 00535344 ["INT_ADD", "register:40f0:8", ["const:535344:8", "const:4:8"]]
+ 00535344 ["CALL", null, ["callee:00c57ab0:8"]]
- 005124ac bytes ed221b94
+ 00535344 bytes db891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ab883f0606592c4edfce42a0112c82"></a>

### [`005124c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005124c8.md) → [`00535360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535360.md) FUN_00535360

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "0053537c",
      "incomplete_value": true,
      "site": "00535380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00535374",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535380",
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
      "00535374",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535380",
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

- 旧版 [`005124d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005124c8.md#insn-005124d4) · [`005124dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005124c8.md#insn-005124dc) · [`005124f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005124c8.md#insn-005124f4)
- 新版 [`0053536c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535360.md#insn-0053536c) · [`00535374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535360.md#insn-00535374) · [`0053538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535360.md#insn-0053538c)

~~~diff
- 005124d4 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0053536c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005124d4 bytes 48380090
+ 0053536c bytes 283b00b0
- 005124dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 005124dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535374 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00535374 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005124dc bytes 08f147f9
+ 00535374 bytes 08e944f9
- 005124f4 ["INT_ADD", "register:40f0:8", ["const:5124f4:8", "const:4:8"]]
- 005124f4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053538c ["INT_ADD", "register:40f0:8", ["const:53538c:8", "const:4:8"]]
+ 0053538c ["CALL", null, ["callee:00c57ab0:8"]]
- 005124f4 bytes db221b94
+ 0053538c bytes c9891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-225b075d5a6463aa3de30781473b7b90"></a>

### [`00512510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512510.md) → [`005353a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353a8.md) FUN_005353a8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "005353c4",
      "incomplete_value": true,
      "site": "005353c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005353bc",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005353c8",
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
      "005353bc",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005353c8",
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

- 旧版 [`0051251c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512510.md#insn-0051251c) · [`00512524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512510.md#insn-00512524) · [`0051253c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512510.md#insn-0051253c)
- 新版 [`005353b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353a8.md#insn-005353b4) · [`005353bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353a8.md#insn-005353bc) · [`005353d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353a8.md#insn-005353d4)

~~~diff
- 0051251c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005353b4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051251c bytes 48380090
+ 005353b4 bytes 283b00b0
- 00512524 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00512524 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005353bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 005353bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512524 bytes 08f147f9
+ 005353bc bytes 08e944f9
- 0051253c ["INT_ADD", "register:40f0:8", ["const:51253c:8", "const:4:8"]]
- 0051253c ["CALL", null, ["callee:00c57ab0:8"]]
+ 005353d4 ["INT_ADD", "register:40f0:8", ["const:5353d4:8", "const:4:8"]]
+ 005353d4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0051253c bytes c9221b94
+ 005353d4 bytes b7891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ce7a66dac5d34b1f2568a7eafb5e048"></a>

### [`00512558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512558.md) → [`005353f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353f0.md) FUN_005353f0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "0053540c",
      "incomplete_value": true,
      "site": "00535410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00535404",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535410",
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
      "00535404",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535410",
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

- 旧版 [`00512564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512558.md#insn-00512564) · [`0051256c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512558.md#insn-0051256c) · [`00512584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512558.md#insn-00512584)
- 新版 [`005353fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353f0.md#insn-005353fc) · [`00535404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353f0.md#insn-00535404) · [`0053541c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005353f0.md#insn-0053541c)

~~~diff
- 00512564 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005353fc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512564 bytes 48380090
+ 005353fc bytes 283b00b0
- 0051256c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 0051256c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535404 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00535404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051256c bytes 08f147f9
+ 00535404 bytes 08e944f9
- 00512584 ["INT_ADD", "register:40f0:8", ["const:512584:8", "const:4:8"]]
- 00512584 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053541c ["INT_ADD", "register:40f0:8", ["const:53541c:8", "const:4:8"]]
+ 0053541c ["CALL", null, ["callee:00c57ab0:8"]]
- 00512584 bytes b7221b94
+ 0053541c bytes a5891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4d5cce830a66992ced4fd585cbeebb2"></a>

### [`005125a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125a0.md) → [`00535438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535438.md) FUN_00535438

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00535454",
      "incomplete_value": true,
      "site": "00535458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "0053544c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535458",
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
      "0053544c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535458",
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

- 旧版 [`005125ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125a0.md#insn-005125ac) · [`005125b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125a0.md#insn-005125b4) · [`005125cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125a0.md#insn-005125cc)
- 新版 [`00535444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535438.md#insn-00535444) · [`0053544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535438.md#insn-0053544c) · [`00535464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535438.md#insn-00535464)

~~~diff
- 005125ac ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535444 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005125ac bytes 48380090
+ 00535444 bytes 283b00b0
- 005125b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 005125b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053544c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 0053544c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005125b4 bytes 08f147f9
+ 0053544c bytes 08e944f9
- 005125cc ["INT_ADD", "register:40f0:8", ["const:5125cc:8", "const:4:8"]]
- 005125cc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00535464 ["INT_ADD", "register:40f0:8", ["const:535464:8", "const:4:8"]]
+ 00535464 ["CALL", null, ["callee:00c57ab0:8"]]
- 005125cc bytes a5221b94
+ 00535464 bytes 93891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-510921021bb1e73f6770e3e85d56790a"></a>

### [`005125e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125e8.md) → [`00535480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535480.md) FUN_00535480

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "0053549c",
      "incomplete_value": true,
      "site": "005354a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00535494",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005354a0",
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
      "00535494",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005354a0",
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

- 旧版 [`005125f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125e8.md#insn-005125f4) · [`005125fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125e8.md#insn-005125fc) · [`00512614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005125e8.md#insn-00512614)
- 新版 [`0053548c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535480.md#insn-0053548c) · [`00535494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535480.md#insn-00535494) · [`005354ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535480.md#insn-005354ac)

~~~diff
- 005125f4 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0053548c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005125f4 bytes 48380090
+ 0053548c bytes 283b00b0
- 005125fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 005125fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00535494 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005125fc bytes 08f147f9
+ 00535494 bytes 08e944f9
- 00512614 ["INT_ADD", "register:40f0:8", ["const:512614:8", "const:4:8"]]
- 00512614 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005354ac ["INT_ADD", "register:40f0:8", ["const:5354ac:8", "const:4:8"]]
+ 005354ac ["CALL", null, ["callee:00c57ab0:8"]]
- 00512614 bytes 93221b94
+ 005354ac bytes 81891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-862b2e77152cd94a72f1839e4897b35d"></a>

### [`00512630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512630.md) → [`005354c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005354c8.md) FUN_005354c8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "005354e4",
      "incomplete_value": true,
      "site": "005354e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005354dc",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005354e8",
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
      "005354dc",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005354e8",
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

- 旧版 [`0051263c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512630.md#insn-0051263c) · [`00512644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512630.md#insn-00512644) · [`0051265c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512630.md#insn-0051265c)
- 新版 [`005354d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005354c8.md#insn-005354d4) · [`005354dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005354c8.md#insn-005354dc) · [`005354f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005354c8.md#insn-005354f4)

~~~diff
- 0051263c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005354d4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051263c bytes 48380090
+ 005354d4 bytes 283b00b0
- 00512644 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00512644 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005354dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 005354dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512644 bytes 08f147f9
+ 005354dc bytes 08e944f9
- 0051265c ["INT_ADD", "register:40f0:8", ["const:51265c:8", "const:4:8"]]
- 0051265c ["CALL", null, ["callee:00c57ab0:8"]]
+ 005354f4 ["INT_ADD", "register:40f0:8", ["const:5354f4:8", "const:4:8"]]
+ 005354f4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0051265c bytes 81221b94
+ 005354f4 bytes 6f891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7590d616cd692e3894e4ff4fb535a6a"></a>

### [`00512678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512678.md) → [`00535510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535510.md) FUN_00535510

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "0053552c",
      "incomplete_value": true,
      "site": "00535530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00535524",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535530",
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
      "00535524",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535530",
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

- 旧版 [`00512684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512678.md#insn-00512684) · [`0051268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512678.md#insn-0051268c) · [`005126a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512678.md#insn-005126a4)
- 新版 [`0053551c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535510.md#insn-0053551c) · [`00535524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535510.md#insn-00535524) · [`0053553c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535510.md#insn-0053553c)

~~~diff
- 00512684 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0053551c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512684 bytes 48380090
+ 0053551c bytes 283b00b0
- 0051268c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 0051268c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535524 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00535524 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051268c bytes 08f147f9
+ 00535524 bytes 08e944f9
- 005126a4 ["INT_ADD", "register:40f0:8", ["const:5126a4:8", "const:4:8"]]
- 005126a4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053553c ["INT_ADD", "register:40f0:8", ["const:53553c:8", "const:4:8"]]
+ 0053553c ["CALL", null, ["callee:00c57ab0:8"]]
- 005126a4 bytes 6f221b94
+ 0053553c bytes 5d891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32492db7c510d1a2a75d75196e977851"></a>

### [`005126c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005126c0.md) → [`00535558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535558.md) FUN_00535558

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00535574",
      "incomplete_value": true,
      "site": "00535578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "0053556c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535578",
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
      "0053556c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535578",
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

- 旧版 [`005126cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005126c0.md#insn-005126cc) · [`005126d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005126c0.md#insn-005126d4) · [`005126ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005126c0.md#insn-005126ec)
- 新版 [`00535564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535558.md#insn-00535564) · [`0053556c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535558.md#insn-0053556c) · [`00535584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535558.md#insn-00535584)

~~~diff
- 005126cc ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535564 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005126cc bytes 48380090
+ 00535564 bytes 283b00b0
- 005126d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 005126d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053556c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 0053556c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005126d4 bytes 08f147f9
+ 0053556c bytes 08e944f9
- 005126ec ["INT_ADD", "register:40f0:8", ["const:5126ec:8", "const:4:8"]]
- 005126ec ["CALL", null, ["callee:00c57ab0:8"]]
+ 00535584 ["INT_ADD", "register:40f0:8", ["const:535584:8", "const:4:8"]]
+ 00535584 ["CALL", null, ["callee:00c57ab0:8"]]
- 005126ec bytes 5d221b94
+ 00535584 bytes 4b891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e30fda47cb7596fd698dce43a3cb0438"></a>

### [`00512708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512708.md) → [`005355a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355a0.md) FUN_005355a0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "005355bc",
      "incomplete_value": true,
      "site": "005355c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005355b4",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005355c0",
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
      "005355b4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005355c0",
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

- 旧版 [`00512714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512708.md#insn-00512714) · [`0051271c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512708.md#insn-0051271c) · [`00512734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512708.md#insn-00512734)
- 新版 [`005355ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355a0.md#insn-005355ac) · [`005355b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355a0.md#insn-005355b4) · [`005355cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355a0.md#insn-005355cc)

~~~diff
- 00512714 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005355ac ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512714 bytes 48380090
+ 005355ac bytes 283b00b0
- 0051271c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 0051271c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005355b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 005355b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051271c bytes 08f147f9
+ 005355b4 bytes 08e944f9
- 00512734 ["INT_ADD", "register:40f0:8", ["const:512734:8", "const:4:8"]]
- 00512734 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005355cc ["INT_ADD", "register:40f0:8", ["const:5355cc:8", "const:4:8"]]
+ 005355cc ["CALL", null, ["callee:00c57ab0:8"]]
- 00512734 bytes 4b221b94
+ 005355cc bytes 39891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c6ee1e7387c67caa42d946a60423ce1"></a>

### [`00512750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512750.md) → [`005355e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355e8.md) FUN_005355e8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00535604",
      "incomplete_value": true,
      "site": "00535608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005355fc",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535608",
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
      "005355fc",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535608",
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

- 旧版 [`0051275c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512750.md#insn-0051275c) · [`00512764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512750.md#insn-00512764) · [`0051277c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512750.md#insn-0051277c)
- 新版 [`005355f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355e8.md#insn-005355f4) · [`005355fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355e8.md#insn-005355fc) · [`00535614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005355e8.md#insn-00535614)

~~~diff
- 0051275c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005355f4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051275c bytes 48380090
+ 005355f4 bytes 283b00b0
- 00512764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00512764 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005355fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 005355fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512764 bytes 08f147f9
+ 005355fc bytes 08e944f9
- 0051277c ["INT_ADD", "register:40f0:8", ["const:51277c:8", "const:4:8"]]
- 0051277c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00535614 ["INT_ADD", "register:40f0:8", ["const:535614:8", "const:4:8"]]
+ 00535614 ["CALL", null, ["callee:00c57ab0:8"]]
- 0051277c bytes 39221b94
+ 00535614 bytes 27891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e992483db257973547eacb7a71f30064"></a>

### [`00512798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512798.md) → [`00535630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535630.md) FUN_00535630

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "0053564c",
      "incomplete_value": true,
      "site": "00535650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00535644",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535650",
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
      "00535644",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535650",
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

- 旧版 [`005127a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512798.md#insn-005127a4) · [`005127ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512798.md#insn-005127ac) · [`005127c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512798.md#insn-005127c4)
- 新版 [`0053563c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535630.md#insn-0053563c) · [`00535644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535630.md#insn-00535644) · [`0053565c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535630.md#insn-0053565c)

~~~diff
- 005127a4 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0053563c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005127a4 bytes 48380090
+ 0053563c bytes 283b00b0
- 005127ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 005127ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535644 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00535644 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005127ac bytes 08f147f9
+ 00535644 bytes 08e944f9
- 005127c4 ["INT_ADD", "register:40f0:8", ["const:5127c4:8", "const:4:8"]]
- 005127c4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053565c ["INT_ADD", "register:40f0:8", ["const:53565c:8", "const:4:8"]]
+ 0053565c ["CALL", null, ["callee:00c57ab0:8"]]
- 005127c4 bytes 27221b94
+ 0053565c bytes 15891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0213f5ef20d605de13c66bcbfff4afd"></a>

### [`005127e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005127e0.md) → [`00535678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535678.md) FUN_00535678

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00535694",
      "incomplete_value": true,
      "site": "00535698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "0053568c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535698",
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
      "0053568c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535698",
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

- 旧版 [`005127ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005127e0.md#insn-005127ec) · [`005127f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005127e0.md#insn-005127f4) · [`0051280c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005127e0.md#insn-0051280c)
- 新版 [`00535684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535678.md#insn-00535684) · [`0053568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535678.md#insn-0053568c) · [`005356a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535678.md#insn-005356a4)

~~~diff
- 005127ec ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535684 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005127ec bytes 48380090
+ 00535684 bytes 283b00b0
- 005127f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 005127f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053568c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 0053568c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005127f4 bytes 08f147f9
+ 0053568c bytes 08e944f9
- 0051280c ["INT_ADD", "register:40f0:8", ["const:51280c:8", "const:4:8"]]
- 0051280c ["CALL", null, ["callee:00c57ab0:8"]]
+ 005356a4 ["INT_ADD", "register:40f0:8", ["const:5356a4:8", "const:4:8"]]
+ 005356a4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0051280c bytes 15221b94
+ 005356a4 bytes 03891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d199442d58a31cb99fae7012a32039bd"></a>

### [`00512828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512828.md) → [`005356c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005356c0.md) FUN_005356c0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "005356dc",
      "incomplete_value": true,
      "site": "005356e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005356d4",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005356e0",
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
      "005356d4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005356e0",
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

- 旧版 [`00512834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512828.md#insn-00512834) · [`0051283c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512828.md#insn-0051283c) · [`00512854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512828.md#insn-00512854)
- 新版 [`005356cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005356c0.md#insn-005356cc) · [`005356d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005356c0.md#insn-005356d4) · [`005356ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005356c0.md#insn-005356ec)

~~~diff
- 00512834 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005356cc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512834 bytes 48380090
+ 005356cc bytes 283b00b0
- 0051283c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 0051283c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005356d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 005356d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051283c bytes 08f147f9
+ 005356d4 bytes 08e944f9
- 00512854 ["INT_ADD", "register:40f0:8", ["const:512854:8", "const:4:8"]]
- 00512854 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005356ec ["INT_ADD", "register:40f0:8", ["const:5356ec:8", "const:4:8"]]
+ 005356ec ["CALL", null, ["callee:00c57ab0:8"]]
- 00512854 bytes 03221b94
+ 005356ec bytes f1881c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-949587ae67d2c486045a7ac024786fe9"></a>

### [`00512870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512870.md) → [`00535708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535708.md) FUN_00535708

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00535724",
      "incomplete_value": true,
      "site": "00535728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "0053571c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535728",
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
      "0053571c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535728",
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

- 旧版 [`0051287c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512870.md#insn-0051287c) · [`00512884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512870.md#insn-00512884) · [`0051289c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512870.md#insn-0051289c)
- 新版 [`00535714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535708.md#insn-00535714) · [`0053571c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535708.md#insn-0053571c) · [`00535734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535708.md#insn-00535734)

~~~diff
- 0051287c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535714 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051287c bytes 48380090
+ 00535714 bytes 283b00b0
- 00512884 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00512884 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053571c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 0053571c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512884 bytes 08f147f9
+ 0053571c bytes 08e944f9
- 0051289c ["INT_ADD", "register:40f0:8", ["const:51289c:8", "const:4:8"]]
- 0051289c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00535734 ["INT_ADD", "register:40f0:8", ["const:535734:8", "const:4:8"]]
+ 00535734 ["CALL", null, ["callee:00c57ab0:8"]]
- 0051289c bytes f1211b94
+ 00535734 bytes df881c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75d38c36fc52f2d4d5222ae6cbdc9782"></a>

### [`005128b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005128b8.md) → [`00535750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535750.md) FUN_00535750

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "0053576c",
      "incomplete_value": true,
      "site": "00535770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00535764",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535770",
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
      "00535764",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535770",
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

- 旧版 [`005128c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005128b8.md#insn-005128c4) · [`005128cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005128b8.md#insn-005128cc) · [`005128e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005128b8.md#insn-005128e4)
- 新版 [`0053575c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535750.md#insn-0053575c) · [`00535764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535750.md#insn-00535764) · [`0053577c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535750.md#insn-0053577c)

~~~diff
- 005128c4 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0053575c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005128c4 bytes 48380090
+ 0053575c bytes 283b00b0
- 005128cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 005128cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00535764 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005128cc bytes 08f147f9
+ 00535764 bytes 08e944f9
- 005128e4 ["INT_ADD", "register:40f0:8", ["const:5128e4:8", "const:4:8"]]
- 005128e4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053577c ["INT_ADD", "register:40f0:8", ["const:53577c:8", "const:4:8"]]
+ 0053577c ["CALL", null, ["callee:00c57ab0:8"]]
- 005128e4 bytes df211b94
+ 0053577c bytes cd881c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b049919ebab76f20ba02cc882b8ed3e9"></a>

### [`00512900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512900.md) → [`00535798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535798.md) FUN_00535798

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "005357b4",
      "incomplete_value": true,
      "site": "005357b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005357ac",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005357b8",
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
      "005357ac",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005357b8",
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

- 旧版 [`0051290c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512900.md#insn-0051290c) · [`00512914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512900.md#insn-00512914) · [`0051292c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512900.md#insn-0051292c)
- 新版 [`005357a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535798.md#insn-005357a4) · [`005357ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535798.md#insn-005357ac) · [`005357c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535798.md#insn-005357c4)

~~~diff
- 0051290c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005357a4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0051290c bytes 48380090
+ 005357a4 bytes 283b00b0
- 00512914 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00512914 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005357ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 005357ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512914 bytes 08f147f9
+ 005357ac bytes 08e944f9
- 0051292c ["INT_ADD", "register:40f0:8", ["const:51292c:8", "const:4:8"]]
- 0051292c ["CALL", null, ["callee:00c57ab0:8"]]
+ 005357c4 ["INT_ADD", "register:40f0:8", ["const:5357c4:8", "const:4:8"]]
+ 005357c4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0051292c bytes cd211b94
+ 005357c4 bytes bb881c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-623a5142f839f2efe9738f710b2ad54e"></a>

### [`00512948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512948.md) → [`005357e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005357e0.md) FUN_005357e0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "005357fc",
      "incomplete_value": true,
      "site": "00535800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005357f4",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535800",
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
      "005357f4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535800",
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

- 旧版 [`00512954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512948.md#insn-00512954) · [`0051295c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512948.md#insn-0051295c) · [`00512974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512948.md#insn-00512974)
- 新版 [`005357ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005357e0.md#insn-005357ec) · [`005357f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005357e0.md#insn-005357f4) · [`0053580c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005357e0.md#insn-0053580c)

~~~diff
- 00512954 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005357ec ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512954 bytes 48380090
+ 005357ec bytes 283b00b0
- 0051295c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 0051295c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005357f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 005357f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051295c bytes 08f147f9
+ 005357f4 bytes 08e944f9
- 00512974 ["INT_ADD", "register:40f0:8", ["const:512974:8", "const:4:8"]]
- 00512974 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053580c ["INT_ADD", "register:40f0:8", ["const:53580c:8", "const:4:8"]]
+ 0053580c ["CALL", null, ["callee:00c57ab0:8"]]
- 00512974 bytes bb211b94
+ 0053580c bytes a9881c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-983f87b24b1d07fb8bfc117956a25bbd"></a>

### [`005129d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005129d4.md) → [`0053586c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/0053586c.md) FUN_0053586c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00535888",
      "incomplete_value": true,
      "site": "0053588c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00535880",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "0053588c",
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
      "00535880",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "0053588c",
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

- 旧版 [`005129e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005129d4.md#insn-005129e0) · [`005129e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005129d4.md#insn-005129e8) · [`00512a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/005129d4.md#insn-00512a00)
- 新版 [`00535878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/0053586c.md#insn-00535878) · [`00535880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/0053586c.md#insn-00535880) · [`00535898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/0053586c.md#insn-00535898)

~~~diff
- 005129e0 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535878 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005129e0 bytes 48380090
+ 00535878 bytes 283b00b0
- 005129e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 005129e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00535880 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005129e8 bytes 08f147f9
+ 00535880 bytes 08e944f9
- 00512a00 ["INT_ADD", "register:40f0:8", ["const:512a00:8", "const:4:8"]]
- 00512a00 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00535898 ["INT_ADD", "register:40f0:8", ["const:535898:8", "const:4:8"]]
+ 00535898 ["CALL", null, ["callee:00c57ab0:8"]]
- 00512a00 bytes 98211b94
+ 00535898 bytes 86881c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0afec571a2473290eabfb72ae8ee28a3"></a>

### [`00512a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512a1c.md) → [`005358b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005358b4.md) FUN_005358b4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "005358d0",
      "incomplete_value": true,
      "site": "005358d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "005358c8",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "005358d4",
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
      "005358c8",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "005358d4",
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

- 旧版 [`00512a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512a1c.md#insn-00512a28) · [`00512a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512a1c.md#insn-00512a30) · [`00512a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512a1c.md#insn-00512a48)
- 新版 [`005358c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005358b4.md#insn-005358c0) · [`005358c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005358b4.md#insn-005358c8) · [`005358e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005358b4.md#insn-005358e0)

~~~diff
- 00512a28 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 005358c0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512a28 bytes 48380090
+ 005358c0 bytes 283b00b0
- 00512a30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00512a30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005358c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 005358c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512a30 bytes 08f147f9
+ 005358c8 bytes 08e944f9
- 00512a48 ["INT_ADD", "register:40f0:8", ["const:512a48:8", "const:4:8"]]
- 00512a48 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005358e0 ["INT_ADD", "register:40f0:8", ["const:5358e0:8", "const:4:8"]]
+ 005358e0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00512a48 bytes 86211b94
+ 005358e0 bytes 74881c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af8908b203ffe657f8e03ddbb97983be"></a>

### [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) → [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) FUN_00535b2c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 35件 [`0047f2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f2d0.md) [`00482154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482154.md) [`00482df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482df4.md) [`00484754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484754.md) [`00484d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484d30.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 35件 [`004a2168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md) [`004a4fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a4/004a4fec.md) [`004a5c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5c8c.md) [`004a75ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md) [`004a7bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7bc8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00535b3c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00512ca4",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00535b38",
      "incomplete_value": false,
      "site": "00535b3c",
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
            "const:39d:8"
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
      "00535b38",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00535b3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00535b38",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00535b3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md#insn-00512ca4) · [`00512c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md#insn-00512c9c) · [`00512ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md#insn-00512ca0)
- 新版 [`00535b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md#insn-00535b3c) · [`00535b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md#insn-00535b34) · [`00535b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md#insn-00535b38)

~~~diff
- 00512ca4 ["INT_ADD", "register:40f0:8", ["const:512ca4:8", "const:4:8"]]
- 00512ca4 ["CALL", null, ["ram:418c38:8"]]
+ 00535b3c ["INT_ADD", "register:40f0:8", ["const:535b3c:8", "const:4:8"]]
+ 00535b3c ["CALL", null, ["ram:43b738:8"]]
- 00512ca4 bytes e517fc97
+ 00535b3c bytes ff16fc97
- 00512c9c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00535b34 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00512c9c bytes a0ecffb0
+ 00535b34 bytes 00ecffd0
- 00512ca0 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00512ca0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00512ca0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00512ca0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00535b38 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00535b38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00535b38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00535b38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00512ca0 bytes 00740e91
+ 00535b38 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bcff205d894e5c1a6ea6814964ef2c3"></a>

### [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) → [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) FUN_00535b40

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 32件 [`004826c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004826c4.md) [`00483d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483d44.md) [`00484024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484024.md) [`00485f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485f54.md) [`0049f624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f624.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 32件 [`004a555c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md) [`004a6bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6bdc.md) [`004a6ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6ebc.md) [`004a8dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md) [`004c24bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c24bc.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "00535ba8",
      "incomplete_value": true,
      "site": "00535ba8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00535be4",
      "incomplete_value": true,
      "site": "00535be4",
      "value": [
        "LOAD",
        "8",
        [
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
      "00535b98",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00535bd4",
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
      "00535b98",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00535bd4",
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

- 旧版 [`00512d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md#insn-00512d10) · [`00512d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md#insn-00512d4c) · [`00512cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md#insn-00512cc4)
- 新版 [`00535ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md#insn-00535ba8) · [`00535be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md#insn-00535be4) · [`00535b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md#insn-00535b5c)

~~~diff
- 00512d10 ["COPY", "register:0:8", ["register:4048:8"]]
- 00512d10 ["INT_ADD", "register:40f0:8", ["const:512d10:8", "const:4:8"]]
- 00512d10 ["CALLIND", null, ["register:0:8"]]
+ 00535ba8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00535ba8 ["INT_ADD", "register:40f0:8", ["const:535ba8:8", "const:4:8"]]
+ 00535ba8 ["CALLIND", null, ["register:0:8"]]
- 00512d10 bytes 20013fd6
+ 00535ba8 bytes 20013fd6
- 00512d4c ["COPY", "register:0:8", ["register:4048:8"]]
- 00512d4c ["INT_ADD", "register:40f0:8", ["const:512d4c:8", "const:4:8"]]
- 00512d4c ["CALLIND", null, ["register:0:8"]]
+ 00535be4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00535be4 ["INT_ADD", "register:40f0:8", ["const:535be4:8", "const:4:8"]]
+ 00535be4 ["CALLIND", null, ["register:0:8"]]
- 00512d4c bytes 20013fd6
+ 00535be4 bytes 20013fd6
- 00512cc4 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 00535b5c ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 00512cc4 bytes d5360090
+ 00535b5c bytes 953900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f39d73b5a87e97919091cebe668b2fd0"></a>

### [`00512d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512d84.md) → [`00535c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c1c.md) FUN_00535c1c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00535c38",
      "incomplete_value": true,
      "site": "00535c3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00535c30",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535c3c",
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
      "00535c30",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535c3c",
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

- 旧版 [`00512d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512d84.md#insn-00512d90) · [`00512d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512d84.md#insn-00512d98) · [`00512db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512d84.md#insn-00512db0)
- 新版 [`00535c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c1c.md#insn-00535c28) · [`00535c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c1c.md#insn-00535c30) · [`00535c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c1c.md#insn-00535c48)

~~~diff
- 00512d90 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535c28 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512d90 bytes 48380090
+ 00535c28 bytes 283b00b0
- 00512d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00512d98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535c30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00535c30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512d98 bytes 08f147f9
+ 00535c30 bytes 08e944f9
- 00512db0 ["INT_ADD", "register:40f0:8", ["const:512db0:8", "const:4:8"]]
- 00512db0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00535c48 ["INT_ADD", "register:40f0:8", ["const:535c48:8", "const:4:8"]]
+ 00535c48 ["CALL", null, ["callee:00c57ab0:8"]]
- 00512db0 bytes ac201b94
+ 00535c48 bytes 9a871c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e669cd7cc4964885e37168582fc3e8c"></a>

### [`00512dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512dcc.md) → [`00535c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c64.md) FUN_00535c64

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb100.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

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
      "definition_site": "00535d24",
      "incomplete_value": true,
      "site": "00535d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00535d70",
      "incomplete_value": false,
      "site": "00535d74",
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
            "const:838:8"
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
            "const:c78:8"
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
      "definition_site": "00535c84",
      "incomplete_value": false,
      "site": "00535c98",
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
            "const:20c:8"
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
            "const:be8:8"
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
      "00535c84",
      "PARAM",
      [
        "storage",
        "002afbe8",
        null,
        "string"
      ]
    ],
    [
      "00535ca0",
      "PARAM",
      [
        "storage",
        "002a03cd",
        null,
        null
      ]
    ],
    [
      "00535d10",
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
      "00535c84",
      "PARAM",
      [
        "storage",
        "002c120c",
        null,
        "string"
      ]
    ],
    [
      "00535ca0",
      "PARAM",
      [
        "storage",
        "002b0987",
        null,
        null
      ]
    ],
    [
      "00535d10",
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

- 旧版 [`00512e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512dcc.md#insn-00512e00) · [`00512e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512dcc.md#insn-00512e10) · [`00512de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512dcc.md#insn-00512de8)
- 新版 [`00535c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c64.md#insn-00535c98) · [`00535ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c64.md#insn-00535ca8) · [`00535c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535c64.md#insn-00535c80)

~~~diff
- 00512e00 ["INT_ADD", "register:40f0:8", ["const:512e00:8", "const:4:8"]]
- 00512e00 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00535c98 ["INT_ADD", "register:40f0:8", ["const:535c98:8", "const:4:8"]]
+ 00535c98 ["CALL", null, ["callee:00c57cb0:8"]]
- 00512e00 bytes 18211b94
+ 00535c98 bytes 06881c94
- 00512e10 ["INT_ADD", "register:40f0:8", ["const:512e10:8", "const:4:8"]]
- 00512e10 ["CALL", null, ["callee:00c57b70:8"]]
+ 00535ca8 ["INT_ADD", "register:40f0:8", ["const:535ca8:8", "const:4:8"]]
+ 00535ca8 ["CALL", null, ["callee:00c57b70:8"]]
- 00512e10 bytes c4201b94
+ 00535ca8 bytes b2871c94
- 00512de8 ["COPY", "register:4000:8", ["const:2af000:8"]]
+ 00535c80 ["COPY", "register:4000:8", ["const:2c1000:8"]]
- 00512de8 bytes e0ecffb0
+ 00535c80 bytes 60ecff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cc50151d4b9611f5d5fa0de5f0bae46"></a>

### [`00512fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512fd4.md) → [`00535e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535e6c.md) FUN_00535e6c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00535e88",
      "incomplete_value": true,
      "site": "00535e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00535e80",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535e8c",
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
      "00535e80",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535e8c",
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

- 旧版 [`00512fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512fd4.md#insn-00512fe0) · [`00512fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512fd4.md#insn-00512fe8) · [`00513000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512fd4.md#insn-00513000)
- 新版 [`00535e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535e6c.md#insn-00535e78) · [`00535e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535e6c.md#insn-00535e80) · [`00535e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535e6c.md#insn-00535e98)

~~~diff
- 00512fe0 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535e78 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00512fe0 bytes 48380090
+ 00535e78 bytes 283b00b0
- 00512fe8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00512fe8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535e80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00535e80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512fe8 bytes 08f147f9
+ 00535e80 bytes 08e944f9
- 00513000 ["INT_ADD", "register:40f0:8", ["const:513000:8", "const:4:8"]]
- 00513000 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00535e98 ["INT_ADD", "register:40f0:8", ["const:535e98:8", "const:4:8"]]
+ 00535e98 ["CALL", null, ["callee:00c57ab0:8"]]
- 00513000 bytes 18201b94
+ 00535e98 bytes 06871c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-554e4794a7345af0555e589038f32707"></a>

### [`0051301c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051301c.md) → [`00535eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535eb4.md) FUN_00535eb4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00535ed0",
      "incomplete_value": true,
      "site": "00535ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00535ec8",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00535ed4",
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
      "00535ec8",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00535ed4",
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

- 旧版 [`00513028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051301c.md#insn-00513028) · [`00513030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051301c.md#insn-00513030) · [`00513048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051301c.md#insn-00513048)
- 新版 [`00535ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535eb4.md#insn-00535ec0) · [`00535ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535eb4.md#insn-00535ec8) · [`00535ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535eb4.md#insn-00535ee0)

~~~diff
- 00513028 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00535ec0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00513028 bytes 283800f0
+ 00535ec0 bytes 283b00b0
- 00513030 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 00513030 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535ec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00535ec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00513030 bytes 08f147f9
+ 00535ec8 bytes 08e944f9
- 00513048 ["INT_ADD", "register:40f0:8", ["const:513048:8", "const:4:8"]]
- 00513048 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00535ee0 ["INT_ADD", "register:40f0:8", ["const:535ee0:8", "const:4:8"]]
+ 00535ee0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00513048 bytes 06201b94
+ 00535ee0 bytes f4861c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e18519aff18f8c9bf053c2ea62d19155"></a>

### [`0051308c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051308c.md) → [`00535f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md) FUN_00535f24

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004d5f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d5/004d5f58.md) [`004d6094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6094.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004f8df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md) [`004f8f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f2c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

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
      "definition_site": "00535f4c",
      "incomplete_value": false,
      "site": "00535f5c",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00535f74",
      "incomplete_value": false,
      "site": "00535f78",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00535f88",
      "incomplete_value": false,
      "site": "00535f9c",
      "value": [
        "leaf",
        "const:4f8f2c:8"
      ]
    },
    "old": {
      "definition_site": "005130f0",
      "incomplete_value": false,
      "site": "00513104",
      "value": [
        "leaf",
        "const:4d6094:8"
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
      "00535f3c",
      "READ",
      [
        "storage",
        "00c253d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00535f4c",
      "PARAM",
      [
        "storage",
        "00c253c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00535f74",
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
      "00535f3c",
      "READ",
      [
        "storage",
        "00ca4e90",
        null,
        "undefined1"
      ]
    ],
    [
      "00535f4c",
      "PARAM",
      [
        "storage",
        "00ca4e80",
        null,
        "undefined8"
      ]
    ],
    [
      "00535f74",
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

- 旧版 [`005130c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051308c.md#insn-005130c4) · [`005130e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051308c.md#insn-005130e0) · [`00513104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051308c.md#insn-00513104)
- 新版 [`00535f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md#insn-00535f5c) · [`00535f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md#insn-00535f78) · [`00535f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md#insn-00535f9c)

~~~diff
- 005130c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005130c4 ["INT_ADD", "register:40f0:8", ["const:5130c4:8", "const:4:8"]]
- 005130c4 ["CALLIND", null, ["register:0:8"]]
+ 00535f5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00535f5c ["INT_ADD", "register:40f0:8", ["const:535f5c:8", "const:4:8"]]
+ 00535f5c ["CALLIND", null, ["register:0:8"]]
- 005130c4 bytes 00013fd6
+ 00535f5c bytes 00013fd6
- 005130e0 ["INT_ADD", "register:40f0:8", ["const:5130e0:8", "const:4:8"]]
- 005130e0 ["CALL", null, ["callee:00c57a50:8"]]
+ 00535f78 ["INT_ADD", "register:40f0:8", ["const:535f78:8", "const:4:8"]]
+ 00535f78 ["CALL", null, ["callee:00c57a50:8"]]
- 005130e0 bytes c81f1b94
+ 00535f78 bytes b6861c94
- 00513104 ["INT_ADD", "register:40f0:8", ["const:513104:8", "const:4:8"]]
- 00513104 ["CALL", null, ["callee:00c57a30:8"]]
+ 00535f9c ["INT_ADD", "register:40f0:8", ["const:535f9c:8", "const:4:8"]]
+ 00535f9c ["CALL", null, ["callee:00c57a30:8"]]
- 00513104 bytes b71f1b94
+ 00535f9c bytes a5861c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d4158a82936163c8d0b8e32f316007c"></a>

### [`00513138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513138.md) → [`00535fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535fd0.md) FUN_00535fd0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004a2edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2edc.md) [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`004c05ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md) · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf30.md)
- 新版 呼出元 3件 [`004c5d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5d74.md) [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`004e3484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md) · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58980.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

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
      "definition_site": "005360c8",
      "incomplete_value": true,
      "site": "005360d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a38:8"
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005360c4",
      "incomplete_value": false,
      "site": "005360d4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0051322c",
      "incomplete_value": false,
      "site": "0051323c",
      "value": [
        "leaf",
        "const:512990:8"
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
      "005360c4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "005360c8",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      "005360c8",
      "PARAM",
      [
        "storage",
        "00be9e68",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005360c4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005360c8",
      "READ",
      [
        "storage",
        "00c9aa38",
        null,
        "pointer"
      ]
    ],
    [
      "005360c8",
      "PARAM",
      [
        "storage",
        "00c66a28",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051323c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513138.md#insn-0051323c) · [`00513170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513138.md#insn-00513170) · [`005131b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513138.md#insn-005131b0)
- 新版 [`005360d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535fd0.md#insn-005360d4) · [`00536008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535fd0.md#insn-00536008) · [`00536048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535fd0.md#insn-00536048)

~~~diff
- 0051323c ["INT_ADD", "register:40f0:8", ["const:51323c:8", "const:4:8"]]
- 0051323c ["CALL", null, ["callee:00c57b10:8"]]
+ 005360d4 ["INT_ADD", "register:40f0:8", ["const:5360d4:8", "const:4:8"]]
+ 005360d4 ["CALL", null, ["callee:00c57b10:8"]]
- 0051323c bytes a11f1b94
+ 005360d4 bytes 8f861c94
- 00513170 ["COPY", "register:0:8", ["register:4048:8"]]
- 00513170 ["INT_ADD", "register:40f0:8", ["const:513170:8", "const:4:8"]]
- 00513170 ["CALLIND", null, ["register:0:8"]]
+ 00536008 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00536008 ["INT_ADD", "register:40f0:8", ["const:536008:8", "const:4:8"]]
+ 00536008 ["CALLIND", null, ["register:0:8"]]
- 00513170 bytes 20013fd6
+ 00536008 bytes 20013fd6
- 005131b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005131b0 ["INT_ADD", "register:40f0:8", ["const:5131b0:8", "const:4:8"]]
- 005131b0 ["CALLIND", null, ["register:0:8"]]
+ 00536048 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00536048 ["INT_ADD", "register:40f0:8", ["const:536048:8", "const:4:8"]]
+ 00536048 ["CALLIND", null, ["register:0:8"]]
- 005131b0 bytes 00013fd6
+ 00536048 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fee758bac5c50abefcc328f07a5f8a29"></a>

### [`0051328c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051328c.md) → [`00536124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536124.md) FUN_00536124

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

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
      "definition_site": "00536140",
      "incomplete_value": true,
      "site": "00536144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "00536138",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "00536144",
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
      "00536138",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00536144",
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

- 旧版 [`00513298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051328c.md#insn-00513298) · [`005132a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051328c.md#insn-005132a0) · [`005132b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051328c.md#insn-005132b8)
- 新版 [`00536130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536124.md#insn-00536130) · [`00536138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536124.md#insn-00536138) · [`00536150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536124.md#insn-00536150)

~~~diff
- 00513298 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00536130 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00513298 bytes 283800f0
+ 00536130 bytes 283b0090
- 005132a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 005132a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00536138 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00536138 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005132a0 bytes 08f147f9
+ 00536138 bytes 08e944f9
- 005132b8 ["INT_ADD", "register:40f0:8", ["const:5132b8:8", "const:4:8"]]
- 005132b8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00536150 ["INT_ADD", "register:40f0:8", ["const:536150:8", "const:4:8"]]
+ 00536150 ["CALL", null, ["callee:00c57ab0:8"]]
- 005132b8 bytes 6a1f1b94
+ 00536150 bytes 58861c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d75093fbafb306a6a08f19683207bec"></a>

### [`005132d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) → [`0053616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) FUN_0053616c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`004ababc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ababc.md) [`004d2b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2b8c.md) [`004d3aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3aec.md) [`004d3ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d3/004d3ba0.md) · 呼出先 8件 [`0051345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051345c.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 4件 [`004ce954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce954.md) [`004f5a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5a24.md) [`004f6984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6984.md) [`004f6a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6a38.md) · 呼出先 8件 [`005362f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.38% / 新版 95.38%

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
      "site": "00536250",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005133b8",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536260",
      "incomplete_value": true,
      "site": "00536268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536264",
      "incomplete_value": true,
      "site": "00536268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00536250",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "00536260",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "00536260",
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
      "00536250",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "00536260",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00536260",
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

- 旧版 [`005133b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md#insn-005133b8) · [`005133d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md#insn-005133d0) · [`00513324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md#insn-00513324)
- 新版 [`00536250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md#insn-00536250) · [`00536268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md#insn-00536268) · [`005361bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md#insn-005361bc)

~~~diff
- 005133b8 ["INT_ADD", "register:40f0:8", ["const:5133b8:8", "const:4:8"]]
- 005133b8 ["CALL", null, ["ram:bdbbf0:8"]]
+ 00536250 ["INT_ADD", "register:40f0:8", ["const:536250:8", "const:4:8"]]
+ 00536250 ["CALL", null, ["ram:c58640:8"]]
- 005133b8 bytes 0e221b94
+ 00536250 bytes fc881c94
- 005133d0 ["INT_ADD", "register:40f0:8", ["const:5133d0:8", "const:4:8"]]
- 005133d0 ["CALL", null, ["callee:00c57b10:8"]]
+ 00536268 ["INT_ADD", "register:40f0:8", ["const:536268:8", "const:4:8"]]
+ 00536268 ["CALL", null, ["callee:00c57b10:8"]]
- 005133d0 bytes 3c1f1b94
+ 00536268 bytes 2a861c94
- 00513324 ["INT_ADD", "register:40f0:8", ["const:513324:8", "const:4:8"]]
- 00513324 ["CALL", null, ["callee:00c58630:8"]]
+ 005361bc ["INT_ADD", "register:40f0:8", ["const:5361bc:8", "const:4:8"]]
+ 005361bc ["CALL", null, ["callee:00c58630:8"]]
- 00513324 bytes 2f221b94
+ 005361bc bytes 1d891c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27ee93e0f2835a7c739e3bc360c90e63"></a>

### [`0051345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051345c.md) → [`005362f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md) FUN_005362f4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`005132d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 4件 [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`0053616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00536304",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0051346c",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536300",
      "incomplete_value": false,
      "site": "00536304",
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
            "const:39d:8"
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
      "00536300",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00536304",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00536300",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00536304",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051346c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051345c.md#insn-0051346c) · [`00513464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051345c.md#insn-00513464) · [`00513468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051345c.md#insn-00513468)
- 新版 [`00536304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md#insn-00536304) · [`005362fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md#insn-005362fc) · [`00536300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md#insn-00536300)

~~~diff
- 0051346c ["INT_ADD", "register:40f0:8", ["const:51346c:8", "const:4:8"]]
- 0051346c ["CALL", null, ["ram:418c38:8"]]
+ 00536304 ["INT_ADD", "register:40f0:8", ["const:536304:8", "const:4:8"]]
+ 00536304 ["CALL", null, ["ram:43b738:8"]]
- 0051346c bytes f315fc97
+ 00536304 bytes 0d15fc97
- 00513464 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 005362fc ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00513464 bytes a0ecff90
+ 005362fc bytes 00ecffb0
- 00513468 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00513468 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00513468 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00513468 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00536300 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00536300 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00536300 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00536300 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00513468 bytes 00740e91
+ 00536300 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

